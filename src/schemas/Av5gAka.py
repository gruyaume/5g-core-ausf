# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fiveg_core_common_schemas.Autn import Autn
from fiveg_core_common_schemas.Rand import Rand
from pydantic import BaseModel

from schemas.HxresStar import HxresStar


class Av5gAka(BaseModel):
    rand: Rand
    autn: Autn
    hxresStar: HxresStar
