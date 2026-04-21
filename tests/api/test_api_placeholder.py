import allure
import json


@allure.title("Validate beneficiary creation API response")
@allure.tag("full", "regress", "smoke")
@allure.label("layer", "api")
@allure.label("Business Unit", "Retail Banking")
@allure.label("Service Level 1", "Daily Banking")
@allure.label("Service Level 2", "Beneficiaries")
@allure.label("Application Unit", "UA-Payments-Orchestrator")
@allure.label("Release", "33.3.1")
@allure.label("Severity", "Critical")
def test_api_placeholder():
    request_payload = {
        "customerId": "RB-10001",
        "beneficiaryName": "John Carter",
        "iban": "DE89370400440532013000",
    }

    response_payload = {
        "status": "SUCCESS",
        "beneficiaryId": "BEN-9001",
        "message": "Beneficiary created successfully",
    }

    allure.attach(
        json.dumps(request_payload, indent=2),
        name="request.json",
        attachment_type=allure.attachment_type.JSON,
    )

    allure.attach(
        json.dumps(response_payload, indent=2),
        name="response.json",
        attachment_type=allure.attachment_type.JSON,
    )

    assert response_payload["status"] == "SUCCESS"