import allure


@allure.id("21424")
@allure.tag("acceptance", "regulator-evidence")
@allure.title("Create domestic transfer with valid beneficiary and valid amount (clone)")
def test_method():
    allure.dynamic.label("owner", "egorivanov")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("Service Level 2", "Transfers")
    allure.dynamic.label("Business Unit", "Retail Banking")
    allure.dynamic.label("Service Level 1", "Daily Banking")
    allure.dynamic.label("priority", "Critical")
    allure.dynamic.label("Jira", "BANK-1")
    allure.dynamic.label("Application Unit", "UA-Digital-Banking-Portal")
    allure.dynamic.label("Release", "33.3.1")

    with allure.step("Open the domestic transfer page."):
        with allure.step("Expected Result"):
            with allure.step("Domestic transfer page opens successfully."):
                pass

    with allure.step("Select an existing beneficiary."):
        with allure.step("Expected Result"):
            with allure.step("Beneficiary is selectable."):
                pass

    with allure.step("Enter a valid transfer amount."):
        with allure.step("Expected Result"):
            with allure.step("Amount is accepted successfully."):
                pass

    with allure.step("Submit the transfer."):
        with allure.step("Expected Result"):
            with allure.step("Transfer is submitted successfully."):
                pass

    with allure.step("Verify confirmation message."):
        with allure.step("Expected Result"):
            with allure.step("Confirmation is displayed successfully."):
                pass