import allure
import base64


_VISIBLE_PNG = (
    "iVBORw0KGgoAAAANSUhEUgAAAHgAAAA8CAIAAAAiz+n/AAAA9UlEQVR4nO3cUWrCQBRA0RlxlW5G3Ey3Of2TKAoVmyu053wlXzNcHiGEMHOtNdjf4dMb+C+EjggdETpyvLuf8/KRffxJa52v1yY6InTk/tFxtR17XvLw8WuiI0JHhI4IHRE6InTk6evdQ/Myd9rHGGOdNx9sv3ZcaJw2C833FvrxR2YTHRE6InRE6IjQEaEjQkeEjggdEToidEToiNARoSNCR4SOCB0ROiJ0ROiI0BGhI0JHhI4IHRE6InRE6IjQEaEjr/22e/Nn7a5O1ULV4Q4mOiJ0ROiI0BGhI0JHnr7eObjjd5noiNCR6dy7homOCB0ROvINoXUZ0tbAJf4AAAAASUVORK5CYII="
)


def _sanitize_name(value: str) -> str:
    return value.lower().replace(" ", "_").replace("/", "_").replace("-", "_")


def _build_e2e_case(case_number: int) -> dict:
    if case_number <= 31:
        service_level_2 = "Transfers"
        application_unit = "UA-Digital-Banking-Portal"
        title = f"Validate transfer portal flow {case_number:03}"
        flow = "transfer"
        feature = "Portal Journeys"
        story = "Transfer Journey"
        suite = "Portal Journeys"
    elif case_number <= 57:
        service_level_2 = "Beneficiaries"
        application_unit = "UA-Digital-Banking-Portal"
        title = f"Validate beneficiary portal flow {case_number:03}"
        flow = "beneficiary"
        feature = "Portal Journeys"
        story = "Beneficiary Journey"
        suite = "Portal Journeys"
    elif case_number <= 79:
        service_level_2 = "Card Management"
        application_unit = "UA-Digital-Banking-Portal"
        title = f"Validate card portal flow {case_number:03}"
        flow = "card_controls"
        feature = "Portal Journeys"
        story = "Card Journey"
        suite = "Portal Journeys"
    else:
        service_level_2 = "Statements"
        application_unit = "UA-Digital-Banking-Portal"
        title = f"Validate statement portal flow {case_number:03}"
        flow = "statements"
        feature = "Portal Journeys"
        story = "Statement Journey"
        suite = "Portal Journeys"

    release = "33.3.1" if case_number <= 44 else "33.3.2"

    if case_number % 10 == 0:
        severity = "Critical"
    elif case_number % 3 == 0:
        severity = "Major"
    else:
        severity = "Minor"

    tags = ["full"]
    if case_number <= 19:
        tags += ["regress", "smoke"]

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
        "attach_screenshot": case_number <= 30,
        "attach_note": case_number <= 30,
    }


def _attach_e2e_artifacts(case_data: dict) -> None:
    n = case_data["case_number"]

    if case_data["attach_screenshot"]:
        allure.attach(
            base64.b64decode(_VISIBLE_PNG),
            name=f"e2e_screenshot_{n:03}.png",
            attachment_type=allure.attachment_type.PNG,
        )

    if case_data["attach_note"]:
        allure.attach(
            (
                f"E2E evidence for case {n:03}\n"
                f"Flow: {case_data['flow']}\n"
                f"Release: {case_data['release']}\n"
                f"Severity: {case_data['severity']}\n"
            ),
            name=f"e2e_note_{n:03}.txt",
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

        with allure.step("Open portal flow"):
            pass

        with allure.step("Validate customer journey result"):
            pass

        _attach_e2e_artifacts(case_data)
        assert True

    test_func.__name__ = f"test_{_sanitize_name(case_data['title'])}_{case_data['case_number']:03}"
    return test_func


for _case_number in range(1, 101):
    _case_data = _build_e2e_case(_case_number)
    globals()[_make_e2e_test(_case_data).__name__] = _make_e2e_test(_case_data)