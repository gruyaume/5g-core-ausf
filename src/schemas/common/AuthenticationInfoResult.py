# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import Union

from pydantic import BaseModel

from schemas.AuthType import AuthType
from schemas.common.Av5GHeAka import Av5GHeAka
from schemas.common.AvEapAkaPrime import AvEapAkaPrime
from schemas.common.Supi import Supi
from schemas.common.SupportedFeatures import SupportedFeatures


class AuthenticationInfoResult(BaseModel):
    authType: AuthType
    authenticationVector: Union[AvEapAkaPrime, Av5GHeAka] = None
    supi: Supi = None
    supportedFeatures: SupportedFeatures = None
