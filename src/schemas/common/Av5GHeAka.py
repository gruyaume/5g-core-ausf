# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.Autn import Autn
from fiveg_core_common_schemas.Rand import Rand
from pydantic import BaseModel

from schemas.common.AvType import AvType
from schemas.common.Kausf import Kausf
from schemas.common.XresStar import XresStar


class Av5GHeAka(BaseModel):
    avType: AvType
    rand: Rand
    xresStar: XresStar
    autn: Autn
    kausf: Kausf
