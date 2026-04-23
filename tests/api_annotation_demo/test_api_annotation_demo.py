import allure


@allure.id("21453")
@allure.title("Validate beneficiary creation API request")
@allure.epic("Retail Banking")
@allure.feature("Beneficiaries")
@allure.story("Beneficiary API")
@allure.suite("Beneficiary API")
@allure.tag("annotation-demo", "annotated", "api")
def test_beneficiary_creation_001():
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "team-banking")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("Service Level 2", "Beneficiaries")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")

    with allure.step("Prepare beneficiary creation payload"):
        request_payload = {"beneficiary": "John Smith", "iban": "RS35260005601001611379"}

    with allure.step("Validate request payload"):
        assert request_payload["beneficiary"] == "John Smith"

    with allure.step("Validate successful response"):
        response_status = 201
        assert response_status == 201


@allure.id("21451")
@allure.title("Validate domestic transfer API request")
@allure.epic("Retail Banking")
@allure.feature("Payments")
@allure.story("Transfer API")
@allure.suite("Payments API")
@allure.tag("annotation-demo", "annotated", "api")
def test_domestic_transfer_002():
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "team-banking")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("Service Level 2", "Transfers")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")

    with allure.step("Prepare domestic transfer payload"):
        request_payload = {"amount": 1500, "currency": "EUR"}

    with allure.step("Validate transfer amount"):
        assert request_payload["amount"] > 0

    with allure.step("Validate successful response"):
        response_status = 200
        assert response_status == 200


@allure.id("21458")
@allure.title("Validate card status update API request")
@allure.epic("Retail Banking")
@allure.feature("Cards")
@allure.story("Card API")
@allure.suite("Card Control API")
@allure.tag("annotation-demo", "annotated", "api")
def test_card_status_update_003():
    allure.dynamic.severity(allure.severity_level.NORMAL)
    allure.dynamic.label("owner", "team-banking")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("Service Level 2", "Cards")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")

    with allure.step("Request card status update"):
        current_status = "BLOCKED"
        expected_status = "ACTIVE"

    with allure.step("Validate updated status response"):
        assert current_status == expected_status, (
            f"Card status mismatch: expected '{expected_status}', but got '{current_status}'"
        )


@allure.id("21452")
@allure.title("Validate statement generation API request")
@allure.epic("Retail Banking")
@allure.feature("Statements")
@allure.story("Statement API")
@allure.suite("Statement API")
@allure.tag("annotation-demo", "annotated", "api")
def test_statement_generation_004():
    allure.dynamic.severity(allure.severity_level.NORMAL)
    allure.dynamic.label("owner", "team-banking")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("Service Level 2", "Statements")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")

    with allure.step("Request monthly statement generation"):
        statement_month = "2026-03"
        generated = True

    with allure.step("Validate statement generation response"):
        assert statement_month == "2026-03"
        assert generated is True


@allure.id("21450")
@allure.title("Validate transfer review API request")
@allure.epic("Retail Banking")
@allure.feature("Payments")
@allure.story("Transfer API")
@allure.suite("Payments API")
@allure.tag("annotation-demo", "annotated", "api")
def test_transfer_review_005():
    allure.dynamic.severity(allure.severity_level.MINOR)
    allure.dynamic.label("owner", "team-banking")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("Service Level 2", "Transfers")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")

    with allure.step("Request transfer review data"):
        review_data = {"payer": "Retail Customer", "payee": "Utility Provider", "amount": 200}

    with allure.step("Validate review response fields"):
        response_status = 200
        assert review_data["amount"] == 200
        assert response_status == 200