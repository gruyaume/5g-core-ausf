# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.CagId import CagId
from fiveg_core_common_schemas.NfGroupId import NfGroupId
from fiveg_core_common_schemas.Pei import Pei
from fiveg_core_common_schemas.ResynchronizationInfo import ResynchronizationInfo
from fiveg_core_common_schemas.ServingNetworkName import ServingNetworkName
from fiveg_core_common_schemas.SupiOrSuci import SupiOrSuci
from fiveg_core_common_schemas.TraceData import TraceData
from pydantic import BaseModel


class AuthenticationInfo(BaseModel):
    supiOrSuci: SupiOrSuci
    servingNetworkName: ServingNetworkName
    resynchronizationInfo: ResynchronizationInfo = None
    pei: Pei = None
    traceData: TraceData = None
    udmGroupId: NfGroupId = None
    routingIndicator: str = None
    cagId: CagId = None
    n5gcInd: bool = None
