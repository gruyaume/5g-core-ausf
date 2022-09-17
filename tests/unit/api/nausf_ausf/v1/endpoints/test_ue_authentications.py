# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app

BASE_URL = "nausf-ausf/v1"
UE_AUTHENTICATION_ENDPOINT = f"{BASE_URL}/ue-authentications/"


class MockRequestsPost:
    def __init__(self, requests_response_dict):
        """Sets requests response."""
        self.requests_response_dict = requests_response_dict

    def json(self):
        return self.requests_response_dict

    def raise_for_status(self):
        pass


@patch("requests.post")
def test_given_udm_responds_with_authentication_info_when_ue_authentication_then_authentication_info_is_returned(  # noqa: E501
    requests_post,
):
    serving_network_name = "whatever snn"
    auth_type = "5G_AKA"
    av_type = "5G_HE_AKA"
    rand = "whatever rand"
    xres_star = "whatever xres_star"
    autn = "whatever autn"
    kausf = "whatever kausf"
    requests_response_dict = {
        "authType": auth_type,
        "authenticationVector": {
            "avType": av_type,
            "rand": rand,
            "xresStar": xres_star,
            "autn": autn,
            "kausf": kausf,
        },
    }
    requests_post.return_value = MockRequestsPost(requests_response_dict=requests_response_dict)
    client = TestClient(app)
    authentication_info = {
        "supiOrSuci": "",
        "servingNetworkName": serving_network_name,
    }

    response = client.post(f"{UE_AUTHENTICATION_ENDPOINT}", json=authentication_info)

    response_content = response.json()
    assert response_content == {
        "authType": auth_type,
        "fivegAuthData": {
            "rand": rand,
            "autn": autn,
            "hxresStar": xres_star,
        },
        "servingNetworkName": serving_network_name,
    }
