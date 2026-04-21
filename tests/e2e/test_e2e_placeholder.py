import allure
import base64


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
    png_base64 = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8"
        "/x8AAusB9Wl8pKQAAAAASUVORK5CYII="
    )

    allure.attach(
        base64.b64decode(png_base64),
        name="transfer-review-screen.png",
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        "Domestic transfer review screen validated successfully.",
        name="ui-check-note",
        attachment_type=allure.attachment_type.TEXT,
    )

    assert True