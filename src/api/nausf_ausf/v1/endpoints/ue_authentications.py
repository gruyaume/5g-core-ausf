# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

import uuid

import requests
from fastapi import APIRouter, Response
from fiveg_core_common_schemas.CagId import CagId
from fiveg_core_common_schemas.NfInstanceId import NfInstanceId
from fiveg_core_common_schemas.ServingNetworkName import ServingNetworkName
from fiveg_core_common_schemas.SupiOrSuci import SupiOrSuci

from schemas.AuthenticationInfo import AuthenticationInfo
from schemas.Av5gAka import Av5gAka
from schemas.common.AuthenticationInfoResult import AuthenticationInfoResult
from schemas.common.ResynchronizationInfo import ResynchronizationInfo
from schemas.common.SupportedFeatures import SupportedFeatures
from schemas.ConfirmationData import ConfirmationData
from schemas.UEAuthenticationCtx import UEAuthenticationCtx

AUSF_INSTANCE_ID = str(uuid.uuid4())
UDM_BASE_URL = "http://127.0.0.1:8001"

router = APIRouter()


def get_auth_data_from_udm(
    serving_network_name: ServingNetworkName,
    ausf_instance_id: NfInstanceId,
    supi_or_suci: SupiOrSuci,
    resynchronization_info: ResynchronizationInfo,
    cag_id: CagId,
    n5gc_ind: bool,
    supported_features: SupportedFeatures = None,
) -> AuthenticationInfoResult:
    ue_authentication_data = {
        "servingNetworkName": serving_network_name,
        "resynchronizationInfo": resynchronization_info,
        "supportedFeatures": supported_features,
        "ausfInstanceId": ausf_instance_id,
        "cagId": cag_id,
        "n5gcInd": n5gc_ind,
    }
    udm_url = f"{UDM_BASE_URL}/nudm-ueau/v1/{supi_or_suci}/security-information/generate-auth-data"
    udm_post_response = requests.post(url=udm_url, json=ue_authentication_data)
    udm_post_response.raise_for_status()
    return AuthenticationInfoResult.parse_obj(obj=udm_post_response.json())


@router.post(
    path="/",
    status_code=201,
    response_model=UEAuthenticationCtx,
)
async def authenticate(
    authentication_info: AuthenticationInfo,
    response: Response,
):
    authentication_info_result = get_auth_data_from_udm(
        serving_network_name=authentication_info.servingNetworkName,
        ausf_instance_id=NfInstanceId(AUSF_INSTANCE_ID),
        supi_or_suci=authentication_info.supiOrSuci,
        resynchronization_info=authentication_info.resynchronizationInfo,
        cag_id=authentication_info.cagId,
        n5gc_ind=authentication_info.n5gcInd,
    )
    auth_ctx_id = str(uuid.uuid4())
    response.headers["Location"] = f"/ue-authentications/{auth_ctx_id}"
    return UEAuthenticationCtx(
        authType=authentication_info_result.authType,
        fivegAuthData=Av5gAka(
            rand=authentication_info_result.authenticationVector.rand,
            autn=authentication_info_result.authenticationVector.autn,
            hxresStar=authentication_info_result.authenticationVector.xresStar,  # TODO: Validate that hxresStar is really xresStar. This looks like a mistake.  # noqa: E501
        ),
        servingNetworkName=authentication_info.servingNetworkName,
    )


@router.put(
    path="/{auth_ctx_id}/5g-aka-confirmation",
    status_code=200,
    response_model=UEAuthenticationCtx,
)
async def confirmation_5g_aka(
    confirmation_data: ConfirmationData,
    response: Response,
):
    return True
