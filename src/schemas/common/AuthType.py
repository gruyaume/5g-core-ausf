# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum


class AuthType(Enum):
    EAP_AKA_PRIME = "EAP_AKA_PRIME"
    FIVEG_AKA = "5G_AKA"
    EAP_TLS = "EAP_TLS"
