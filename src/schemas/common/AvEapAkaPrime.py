# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.Autn import Autn
from fiveg_core_common_schemas.Rand import Rand
from pydantic import BaseModel

from schemas.common.AvType import AvType
from schemas.common.CkPrime import CkPrime
from schemas.common.IkPrime import IkPrime
from schemas.common.Xres import Xres


class AvEapAkaPrime(BaseModel):
    avType: AvType
    rand: Rand
    xres: Xres
    autn: Autn
    ckPrime: CkPrime
    ikPrime: IkPrime
