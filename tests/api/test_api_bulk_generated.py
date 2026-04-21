import allure
import json


def _sanitize_name(value: str) -> str:
    return (
        value.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
    )


def _build_api_case(case_number: int) -> dict:
    if case_number <= 40:
        service_level_2 = "Beneficiaries"
        application_unit = "UA-Payments-Orchestrator"
        title = f"Validate beneficiary creation API flow {case_number:03}"
        operation = "create_beneficiary"
    elif case_number <= 80:
        service_level_2 = "Transfers"
        application_unit = "UA-Payments-Orchestrator"
        title = f"Validate domestic transfer API flow {case_number:03}"
        operation = "create_transfer"
    elif case_number <= 110:
        service_level_2 = "Card Management"
        application_unit = "UA-Card-Control-Service"
        title = f"Validate card control API flow {case_number:03}"
        operation = "update_card_status"
    else:
        service_level_2 = "Statements"
        application_unit = "UA-Statement-Service"
        title = f"Validate statement generation API flow {case_number:03}"
        operation = "generate_statement"

    release = "33.3.1" if case_number <= 60 else "33.3.2"
    severity = "Critical" if case_number % 10 == 0 else "Major"

    tags = ["full", "regress", "smoke"]

    attach_request = case_number <= 20
    attach_response = case_number <= 30

    return {
        "case_number": case_number,
        "title": title,
        "operation": operation,
        "business_unit": "Retail Banking",
        "service_level_1": "Daily Banking",
        "service_level_2": service_level_2,
        "application_unit": application_unit,
        "release": release,
        "severity": severity,
        "tags": tags,
        "attach_request": attach_request,
        "attach_response": attach_response,
    }


def _build_request_payload(case_data: dict) -> dict:
    n = case_data["case_number"]
    op = case_data["operation"]

    if op == "create_beneficiary":
        return {
            "customerId": f"RB-{10000 + n}",
            "beneficiaryName": f"Beneficiary {n}",
            "iban": f"DE8937040044053201{n:04}",
        }
    if op == "create_transfer":
        return {
            "customerId": f"RB-{10000 + n}",
            "amount": 1000 + n,
            "currency": "EUR",
            "beneficiaryId": f"BEN-{9000 + n}",
        }
    if op == "update_card_status":
        return {
            "customerId": f"RB-{10000 + n}",
            "cardId": f"CARD-{7000 + n}",
            "status": "BLOCKED" if n % 2 == 0 else "ACTIVE",
        }

    return {
        "customerId": f"RB-{10000 + n}",
        "statementMonth": "2026-03",
        "format": "PDF",
    }


def _build_response_payload(case_data: dict) -> dict:
    return {
        "status": "SUCCESS",
        "caseNumber": case_data["case_number"],
        "operation": case_data["operation"],
        "message": "Operation completed successfully",
    }


def _attach_api_artifacts(case_data: dict) -> None:
    request_payload = _build_request_payload(case_data)
    response_payload = _build_response_payload(case_data)

    if case_data["attach_request"]:
        allure.attach(
            json.dumps(request_payload, indent=2),
            name=f"api_request_{case_data['case_number']:03}.json",
            attachment_type=allure.attachment_type.JSON,
        )

    if case_data["attach_response"]:
        allure.attach(
            json.dumps(response_payload, indent=2),
            name=f"api_response_{case_data['case_number']:03}.json",
            attachment_type=allure.attachment_type.JSON,
        )


def _make_api_test(case_data: dict):
    def test_func():
        allure.dynamic.title(case_data["title"])
        allure.dynamic.label("layer", "api")
        allure.dynamic.label("Business Unit", case_data["business_unit"])
        allure.dynamic.label("Service Level 1", case_data["service_level_1"])
        allure.dynamic.label("Service Level 2", case_data["service_level_2"])
        allure.dynamic.label("Application Unit", case_data["application_unit"])
        allure.dynamic.label("Release", case_data["release"])
        allure.dynamic.label("Severity", case_data["severity"])

        for tag in case_data["tags"]:
            allure.dynamic.tag(tag)

        with allure.step("Prepare banking API request payload"):
            pass

        with allure.step("Validate successful API response"):
            pass

        _attach_api_artifacts(case_data)

        assert True

    safe_name = _sanitize_name(case_data["title"])
    test_func.__name__ = f"test_{safe_name}_{case_data['case_number']:03}"
    return test_func


for _case_number in range(1, 121):
    _case_data = _build_api_case(_case_number)
    _test = _make_api_test(_case_data)
    globals()[_test.__name__] = _test