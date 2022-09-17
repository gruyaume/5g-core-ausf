# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from pydantic import BaseModel

from schemas.ResStar import ResStar


class ConfirmationData(BaseModel):
    resStar: ResStar
