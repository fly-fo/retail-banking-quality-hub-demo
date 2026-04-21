import allure
import json


def _sanitize_name(value: str) -> str:
    return value.lower().replace(" ", "_").replace("/", "_").replace("-", "_")


def _build_api_case(case_number: int) -> dict:
    if case_number <= 41:
        service_level_2 = "Transfers"
        application_unit = "UA-Payments-Orchestrator"
        title = f"Validate transfer API flow {case_number:03}"
        operation = "create_transfer"
        feature = "Payments"
        story = "Transfer API"
        suite = "Payments API"
    elif case_number <= 74:
        service_level_2 = "Beneficiaries"
        application_unit = "UA-Payments-Orchestrator"
        title = f"Validate beneficiary API flow {case_number:03}"
        operation = "create_beneficiary"
        feature = "Beneficiaries"
        story = "Beneficiary API"
        suite = "Beneficiary API"
    elif case_number <= 97:
        service_level_2 = "Card Management"
        application_unit = "UA-Card-Control-Service"
        title = f"Validate card API flow {case_number:03}"
        operation = "update_card_status"
        feature = "Cards"
        story = "Card API"
        suite = "Card Control API"
    else:
        service_level_2 = "Statements"
        application_unit = "UA-Statement-Service"
        title = f"Validate statement API flow {case_number:03}"
        operation = "generate_statement"
        feature = "Statements"
        story = "Statement API"
        suite = "Statement API"

    release = "33.3.1" if case_number <= 58 else "33.3.2"

    if case_number % 10 == 0:
        severity = "Critical"
    elif case_number % 3 == 0:
        severity = "Major"
    else:
        severity = "Minor"

    return {
        "case_number": case_number,
        "title": title,
        "operation": operation,
        "epic": "Retail Banking",
        "feature": feature,
        "story": story,
        "suite": suite,
        "business_unit": "Retail Banking",
        "service_level_1": "Daily Banking",
        "service_level_2": service_level_2,
        "application_unit": application_unit,
        "release": release,
        "severity": severity,
        "tags": ["full", "regress", "smoke"],
        "attach_request": case_number <= 19,
        "attach_response": case_number <= 31,
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
    if case_data["attach_request"]:
        allure.attach(
            json.dumps(_build_request_payload(case_data), indent=2),
            name=f"api_request_{case_data['case_number']:03}.json",
            attachment_type=allure.attachment_type.JSON,
        )

    if case_data["attach_response"]:
        allure.attach(
            json.dumps(_build_response_payload(case_data), indent=2),
            name=f"api_response_{case_data['case_number']:03}.json",
            attachment_type=allure.attachment_type.JSON,
        )


def _make_api_test(case_data: dict):
    def test_func():
        allure.dynamic.title(case_data["title"])
        allure.dynamic.epic(case_data["epic"])
        allure.dynamic.feature(case_data["feature"])
        allure.dynamic.story(case_data["story"])
        allure.dynamic.suite(case_data["suite"])
        allure.dynamic.label("layer", "api")
        allure.dynamic.label("Business Unit", case_data["business_unit"])
        allure.dynamic.label("Service Level 1", case_data["service_level_1"])
        allure.dynamic.label("Service Level 2", case_data["service_level_2"])
        allure.dynamic.label("Application Unit", case_data["application_unit"])
        allure.dynamic.label("Release", case_data["release"])
        allure.dynamic.label("Severity", case_data["severity"])

        for tag in case_data["tags"]:
            allure.dynamic.tag(tag)

        with allure.step("Prepare API payload"):
            pass

        with allure.step("Validate API response"):
            pass

        _attach_api_artifacts(case_data)
        assert True

    test_func.__name__ = f"test_{_sanitize_name(case_data['title'])}_{case_data['case_number']:03}"
    return test_func


for _case_number in range(1, 121):
    _case_data = _build_api_case(_case_number)
    globals()[_make_api_test(_case_data).__name__] = _make_api_test(_case_data)