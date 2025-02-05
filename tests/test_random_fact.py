import logging
from typing import Union

import pytest

from libs.system.cat_facts import RandomFactResponse

TestScenario = pytest.param


class TestGetRandomFact:
    def test__success__get_random_fact(self, cats_api_client):
        """
        T001 Basic API Response Validation
        Verify the basic response of the get_random_fact API endpoint

        * Status Code Verification (Step 2)
        A 200 OK status code confirms the API endpoint is operational and successfully processed the request.
        Invalid status codes (e.g., 4xx/5xx) would indicate fundamental API issues before examining response content.

        * Pydantic Model Validation (Step 3)
        Pydantic models validate the exact response structure (field names, types, nested objects),
        ensuring compliance with the API specification.

        * Fact Length Validation (Step 4)
        Catches implementation bugs where length calculation might be incorrect


        || Test Scenario ||
        | 1. Call get_random_fact endpoint. |
        | 2. Verify the response status code is 200. |
        | 3. Verify response body match expected by loading to pydantic model. |
        | 4. Verify fact length is equal to length field. |
        """
        logging.info(
            "1. Send a GET request to the get_random_fact endpoint to retrieve a random fact."
        )
        response = cats_api_client.get_random_fact()

        logging.info("2. Verify the response status code is 200.")
        assert (
            response.status_code == 200
        ), f"Expected 200, actual {response.status_code=}"

        logging.info(
            "3. Verify response body match expected by loading to pydantic model."
        )
        validated_response = RandomFactResponse(**response.json())

        logging.info("4. Verify fact length is equal to length field.")
        validated_response.verify_fact_length()

    @pytest.mark.parametrize(
        "max_length",
        [
            TestScenario(2000, id="max_length_2000"),
            TestScenario(200, id="max_length_200"),
            TestScenario(20, id="max_length_20"),
        ],
    )
    def test__success__length_of_fact_provided(self, cats_api_client, max_length: int):
        """
        T002 Valid max_length Parameter Behavior
        Verify the max_length parameter behavior in the get_random_fact API

        * Status Code Verification (Step 2)
        A 200 OK status code confirms the API endpoint is operational and successfully processed the request.
        Invalid status codes (e.g., 4xx/5xx) would indicate fundamental API issues before examining response content.

        * Pydantic Model Validation (Step 3)
        Pydantic models validate the exact response structure (field names, types, nested objects),
        ensuring compliance with the API specification.

        * Fact Length Constraint Validation (Step 4)
        Directly tests if the API enforces the max_length limit. This catches logic errors (e.g., incorrect truncation,
        flawed filtering) to ensure returned facts meet the user-defined length constraint.

        || Test Scenario ||
        | 1. Send a GET request with the max_length query parameter set to a specific value. |
        | 2. Verify the response status code is 200. |
        | 3. Verify response body match expected by loading to pydantic model. |
        | 4. Verify fact max length is lesser or equal to max_length parameter. |
        """
        logging.info("1. Call get_random_fact endpoint with max_length provided.")
        response = cats_api_client.get_random_fact(max_length=max_length)

        logging.info("2. Verify the response status code is 200.")
        assert (
            response.status_code == 200
        ), f"Expected 200, actual {response.status_code=}"

        logging.info(
            "3. Verify response body match expected by loading to pydantic model."
        )
        validated_response = RandomFactResponse(**response.json())

        logging.info(
            "4. Verify fact max length is lesser or equal to max_length parameter."
        )
        assert (
            len(validated_response.fact) <= max_length
        ), f"Length of {validated_response.fact=} exceeds {max_length=} query parameter"

    @pytest.mark.parametrize(
        "max_length",
        [
            TestScenario(
                -1,
                id="max_length_-1",
                marks=pytest.mark.xfail(
                    reason="API call with negative max_length should return 404 status code error"
                ),
            ),
            TestScenario(
                "asd",
                id="max_length_as_string",
                marks=pytest.mark.xfail(
                    reason="API call with string value of max_length should return 404 status code error"
                ),
            ),
        ],
    )
    def test__failure__invalid_max_length_provided(
        self, cats_api_client, max_length: Union[int, str]
    ):
        """
        T003 Invalid max_length Handling
        Verify API behavior when invalid max_length values are provided

        * Status Code Validation (Step 2)
        A 404 status confirms the API rejects invalid max_length values (e.g., negative numbers, non-integers)
        gracefully. This prevents silent failures or unexpected behavior, signaling proper input validation.

        * Empty Response Validation (Step 3)
        Ensures no partial or malformed data is returned for invalid requests, avoiding client-side parsing errors
        or misleading information.

        || Test Scenario ||
        | 1. Send a GET request with the max_length query parameter set to a invalid value. |
        | 2. Verify the response status code is 404. |
        | 3. Verify response body is empty. |
        """
        logging.info("1. Call get_random_fact endpoint with max_length provided.")
        response = cats_api_client.get_random_fact(max_length=max_length)

        logging.info("2. Verify the response status code is 404.")
        assert (
            response.status_code == 404
        ), f"Expected 404, actual {response.status_code=}"

        logging.info("3. Verify response body is empty.")
        assert not response.json()
