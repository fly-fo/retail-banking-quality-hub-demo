import allure


@allure.id("21454")
@allure.title("Validate domestic transfer portal journey")
@allure.epic("Retail Banking")
@allure.feature("Portal Journeys")
@allure.story("Transfer Journey")
@allure.suite("Portal Journeys")
@allure.tag("annotation-demo", "annotated", "e2e")
def test_transfer_portal_001():
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "team-banking")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("Service Level 2", "Transfers")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")

    with allure.step("Open transfer page"):
        page_opened = True
        assert page_opened is True

    with allure.step("Enter valid transfer data"):
        transfer_entered = True
        assert transfer_entered is True

    with allure.step("Verify confirmation is shown"):
        confirmation_visible = True
        assert confirmation_visible is True


@allure.id("21457")
@allure.title("Validate beneficiary creation portal journey")
@allure.epic("Retail Banking")
@allure.feature("Portal Journeys")
@allure.story("Beneficiary Journey")
@allure.suite("Portal Journeys")
@allure.tag("annotation-demo", "annotated", "e2e")
def test_beneficiary_portal_002():
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "team-banking")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("Service Level 2", "Beneficiaries")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")

    with allure.step("Open beneficiary page"):
        page_opened = True
        assert page_opened is True

    with allure.step("Create beneficiary with valid data"):
        beneficiary_created = True
        assert beneficiary_created is True

    with allure.step("Verify creation confirmation"):
        confirmation_visible = True
        assert confirmation_visible is True


@allure.id("21459")
@allure.title("Validate card control portal journey")
@allure.epic("Retail Banking")
@allure.feature("Portal Journeys")
@allure.story("Card Journey")
@allure.suite("Portal Journeys")
@allure.tag("annotation-demo", "annotated", "e2e")
def test_card_portal_003():
    allure.dynamic.severity(allure.severity_level.NORMAL)
    allure.dynamic.label("owner", "team-banking")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("Service Level 2", "Cards")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")

    with allure.step("Open card controls"):
        page_opened = True
        assert page_opened is True

    with allure.step("Trigger unblock action"):
        actual_status = "Card remains blocked after unblock action"
        expected_status = "Card is active after unblock action"

    with allure.step("Verify card status update"):
        assert actual_status == expected_status, (
            f"Portal card control failed: expected '{expected_status}', but got '{actual_status}'"
        )


@allure.id("21455")
@allure.title("Validate statement download portal journey")
@allure.epic("Retail Banking")
@allure.feature("Portal Journeys")
@allure.story("Statement Journey")
@allure.suite("Portal Journeys")
@allure.tag("annotation-demo", "annotated", "e2e")
def test_statement_portal_004():
    allure.dynamic.severity(allure.severity_level.NORMAL)
    allure.dynamic.label("owner", "team-banking")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("Service Level 2", "Statements")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")

    with allure.step("Open statements page"):
        statements_page_opened = True
        assert statements_page_opened is True

    with allure.step("Download monthly statement"):
        pdf_downloaded = True
        assert pdf_downloaded is True

    with allure.step("Verify statement availability"):
        statement_visible = True
        assert statement_visible is True


@allure.id("21456")
@allure.title("Validate transfer confirmation portal journey")
@allure.epic("Retail Banking")
@allure.feature("Portal Journeys")
@allure.story("Transfer Journey")
@allure.suite("Portal Journeys")
@allure.tag("annotation-demo", "annotated", "e2e")
def test_transfer_confirmation_005():
    allure.dynamic.severity(allure.severity_level.MINOR)
    allure.dynamic.label("owner", "team-banking")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("Service Level 2", "Transfers")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")

    with allure.step("Submit transfer"):
        transfer_submitted = True
        assert transfer_submitted is True

    with allure.step("Open confirmation screen"):
        confirmation_screen_opened = True
        assert confirmation_screen_opened is True

    with allure.step("Validate confirmation details"):
        confirmation_details_visible = True
        assert confirmation_details_visible is True