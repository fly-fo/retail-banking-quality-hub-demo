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


def _build_manual_case(case_number: int) -> dict:
    if case_number <= 4:
        service_level_2 = "Statements"
        application_unit = "UA-Statement-Service"
        title = f"Validate statement evidence package {case_number:03}"
        scenario = "statement_evidence"
        feature = "Acceptance Evidence"
        story = "Statement Evidence Pack"
        suite = "Statement Evidence Validation"
    elif case_number <= 8:
        service_level_2 = "Transfers"
        application_unit = "UA-Digital-Banking-Portal"
        title = f"Validate transfer evidence package {case_number:03}"
        scenario = "transfer_evidence"
        feature = "Acceptance Evidence"
        story = "Transfer Evidence Pack"
        suite = "Transfer Evidence Validation"
    elif case_number <= 12:
        service_level_2 = "Beneficiaries"
        application_unit = "UA-Digital-Banking-Portal"
        title = f"Validate beneficiary evidence package {case_number:03}"
        scenario = "beneficiary_evidence"
        feature = "Acceptance Evidence"
        story = "Beneficiary Evidence Pack"
        suite = "Beneficiary Evidence Validation"
    else:
        service_level_2 = "Card Management"
        application_unit = "UA-Card-Control-Service"
        title = f"Validate card-control evidence package {case_number:03}"
        scenario = "card_control_evidence"
        feature = "Acceptance Evidence"
        story = "Card Control Evidence Pack"
        suite = "Card Control Evidence Validation"

    release = "33.3.1" if case_number <= 7 else "33.3.2"

    if case_number % 10 == 0:
        severity = "Critical"
    elif case_number % 3 == 0:
        severity = "Major"
    else:
        severity = "Minor"

    tags = ["full", "manual-as-code", "evidence-pack"]
    if case_number <= 2:
        tags.append("regress")
        tags.append("smoke")
    if case_number <= 5:
        tags.append("acceptance")

    attach_text = True
    attach_csv = case_number <= 10
    attach_png = case_number <= 8

    return {
        "case_number": case_number,
        "title": title,
        "scenario": scenario,
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
        "attach_text": attach_text,
        "attach_csv": attach_csv,
        "attach_png": attach_png,
    }


def _attach_manual_artifacts(case_data: dict) -> None:
    case_number = case_data["case_number"]

    if case_data["attach_text"]:
        allure.attach(
            (
                f"Manual-as-code evidence for case {case_number:03}\n"
                f"Scenario: {case_data['scenario']}\n"
                f"Application Unit: {case_data['application_unit']}\n"
                f"Release: {case_data['release']}\n"
                f"Severity: {case_data['severity']}\n"
            ),
            name=f"manual_evidence_{case_number:03}.txt",
            attachment_type=allure.attachment_type.TEXT,
        )

    if case_data["attach_csv"]:
        csv_content = (
            "artifact_type,status,reference\n"
            f"evidence_package,generated,MAN-{case_number:03}\n"
        )
        allure.attach(
            csv_content,
            name=f"manual_evidence_{case_number:03}.csv",
            attachment_type=allure.attachment_type.CSV,
        )

    if case_data["attach_png"]:
        allure.attach(
            base64.b64decode(_ONE_PIXEL_PNG),
            name=f"manual_preview_{case_number:03}.png",
            attachment_type=allure.attachment_type.PNG,
        )


def _make_manual_test(case_data: dict):
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

        with allure.step("Prepare evidence-oriented scenario state"):
            pass

        with allure.step("Validate evidence package is complete"):
            pass

        _attach_manual_artifacts(case_data)

        assert True

    safe_name = _sanitize_name(case_data["title"])
    test_func.__name__ = f"test_{safe_name}_{case_data['case_number']:03}"
    return test_func


for _case_number in range(1, 16):
    _case_data = _build_manual_case(_case_number)
    _test = _make_manual_test(_case_data)
    globals()[_test.__name__] = _test