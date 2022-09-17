# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Union

from fiveg_core_common_schemas.ServingNetworkName import ServingNetworkName
from pydantic import BaseModel

from schemas.AuthType import AuthType
from schemas.Av5gAka import Av5gAka
from schemas.EapPayload import EapPayload


class UEAuthenticationCtx(BaseModel):
    authType: AuthType
    # _links: Dict[LinksValueSchema]  # TODO: Implement this
    fivegAuthData: Union[Av5gAka, EapPayload]
    servingNetworkName: ServingNetworkName
