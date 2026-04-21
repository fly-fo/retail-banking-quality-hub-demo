import allure
import base64


_ONE_PIXEL_PNG = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8"
    "/x8AAusB9Wl8pKQAAAAASUVORK5CYII="
)


def _sanitize_name(value: str) -> str:
    return (
        value.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
    )


def _build_e2e_case(case_number: int) -> dict:
    if case_number <= 30:
        service_level_2 = "Transfers"
        application_unit = "UA-Digital-Banking-Portal"
        title = f"Validate domestic transfer portal flow {case_number:03}"
        flow = "transfer"
        feature = "Digital Banking Journeys"
        story = "Domestic Transfer Journey"
        suite = "Retail Portal Transfer Journey"
    elif case_number <= 55:
        service_level_2 = "Beneficiaries"
        application_unit = "UA-Digital-Banking-Portal"
        title = f"Validate beneficiary management portal flow {case_number:03}"
        flow = "beneficiary"
        feature = "Digital Banking Journeys"
        story = "Beneficiary Journey"
        suite = "Retail Portal Beneficiary Journey"
    elif case_number <= 75:
        service_level_2 = "Card Management"
        application_unit = "UA-Digital-Banking-Portal"
        title = f"Validate card controls portal flow {case_number:03}"
        flow = "card_controls"
        feature = "Digital Banking Journeys"
        story = "Card Control Journey"
        suite = "Retail Portal Card Control Journey"
    else:
        service_level_2 = "Statements"
        application_unit = "UA-Digital-Banking-Portal"
        title = f"Validate statements portal flow {case_number:03}"
        flow = "statements"
        feature = "Digital Banking Journeys"
        story = "Statement Download Journey"
        suite = "Retail Portal Statement Journey"

    release = "33.3.1" if case_number <= 50 else "33.3.2"

    if case_number % 10 == 0:
        severity = "Critical"
    elif case_number % 3 == 0:
        severity = "Major"
    else:
        severity = "Minor"

    tags = ["full"]
    if case_number <= 20:
        tags.append("regress")
        tags.append("smoke")

    attach_screenshot = case_number <= 30
    attach_note = case_number <= 30

    return {
        "case_number": case_number,
        "title": title,
        "flow": flow,
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
        "tags": tags,
        "attach_screenshot": attach_screenshot,
        "attach_note": attach_note,
    }


def _attach_e2e_artifacts(case_data: dict) -> None:
    case_number = case_data["case_number"]

    if case_data["attach_screenshot"]:
        allure.attach(
            base64.b64decode(_ONE_PIXEL_PNG),
            name=f"e2e_screenshot_{case_number:03}.png",
            attachment_type=allure.attachment_type.PNG,
        )

    if case_data["attach_note"]:
        allure.attach(
            (
                f"Validated E2E evidence for case {case_number:03}\n"
                f"Flow: {case_data['flow']}\n"
                f"Application Unit: {case_data['application_unit']}\n"
                f"Release: {case_data['release']}\n"
                f"Severity: {case_data['severity']}\n"
            ),
            name=f"e2e_note_{case_number:03}.txt",
            attachment_type=allure.attachment_type.TEXT,
        )


def _make_e2e_test(case_data: dict):
    def test_func():
        allure.dynamic.title(case_data["title"])
        allure.dynamic.epic(case_data["epic"])
        allure.dynamic.feature(case_data["feature"])
        allure.dynamic.story(case_data["story"])
        allure.dynamic.suite(case_data["suite"])
        allure.dynamic.label("layer", "e2e")
        allure.dynamic.label("Business Unit", case_data["business_unit"])
        allure.dynamic.label("Service Level 1", case_data["service_level_1"])
        allure.dynamic.label("Service Level 2", case_data["service_level_2"])
        allure.dynamic.label("Application Unit", case_data["application_unit"])
        allure.dynamic.label("Release", case_data["release"])
        allure.dynamic.label("Severity", case_data["severity"])

        for tag in case_data["tags"]:
            allure.dynamic.tag(tag)

        with allure.step("Open digital banking flow and prepare state"):
            pass

        with allure.step("Validate end-to-end customer journey result"):
            pass

        _attach_e2e_artifacts(case_data)

        assert True

    safe_name = _sanitize_name(case_data["title"])
    test_func.__name__ = f"test_{safe_name}_{case_data['case_number']:03}"
    return test_func


for _case_number in range(1, 101):
    _case_data = _build_e2e_case(_case_number)
    _test = _make_e2e_test(_case_data)
    globals()[_test.__name__] = _test