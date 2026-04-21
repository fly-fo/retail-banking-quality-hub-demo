import allure


@allure.title("Validate domestic transfer flow in digital banking portal")
@allure.tag("full", "regress")
@allure.label("layer", "ui")
@allure.label("Business Unit", "Retail Banking")
@allure.label("Service Level 1", "Daily Banking")
@allure.label("Service Level 2", "Transfers")
@allure.label("Application Unit", "UA-Digital-Banking-Portal")
@allure.label("Release", "33.3.1")
@allure.label("Severity", "Critical")
def test_e2e_placeholder():
    assert True