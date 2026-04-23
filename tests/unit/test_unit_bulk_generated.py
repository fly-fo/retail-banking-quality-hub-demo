import allure


FAILED_CASES = {
    4, 9, 13, 18, 22,
    27, 31, 36, 40, 44,
    49, 53, 58, 63, 71,
    76, 82, 88, 94, 99,
}


def _sanitize_name(value: str) -> str:
    return value.lower().replace(" ", "_").replace("/", "_").replace("-", "_")


def _build_unit_case(case_number: int) -> dict:
    if case_number <= 34:
        service_level_2 = "Transfers"
        application_unit = "UA-Payments-Orchestrator"
        title = f"Validate transfer rule {case_number:03}"
        feature = "Payments"
        story = "Transfer Validation"
        suite = "Payments Engine"
        expected = "TRANSFER_RULE_OK"
        actual = "TRANSFER_RULE_OK"
    elif case_number <= 63:
        service_level_2 = "Beneficiaries"
        application_unit = "UA-Payments-Orchestrator"
        title = f"Validate beneficiary rule {case_number:03}"
        feature = "Beneficiaries"
        story = "Beneficiary Validation"
        suite = "Beneficiary Engine"
        expected = "BENEFICIARY_RULE_OK"
        actual = "BENEFICIARY_RULE_OK"
    elif case_number <= 81:
        service_level_2 = "Card Management"
        application_unit = "UA-Card-Control-Service"
        title = f"Validate card rule {case_number:03}"
        feature = "Cards"
        story = "Card Rules"
        suite = "Card Engine"
        expected = "CARD_RULE_OK"
        actual = "CARD_RULE_OK"
    else:
        service_level_2 = "Statements"
        application_unit = "UA-Statement-Service"
        title = f"Validate statement rule {case_number:03}"
        feature = "Statements"
        story = "Statement Rules"
        suite = "Statement Engine"
        expected = "STATEMENT_RULE_OK"
        actual = "STATEMENT_RULE_OK"

    release = "33.3.1" if case_number <= 46 else "33.3.2"

    if case_number % 10 == 0:
        severity = "Critical"
    elif case_number % 3 == 0:
        severity = "Major"
    else:
        severity = "Minor"

    tags = ["full", "regress", "smoke"]

    if case_number in FAILED_CASES:
        if service_level_2 == "Transfers":
            actual = "TRANSFER_LIMIT_CHECK_FAILED"
        elif service_level_2 == "Beneficiaries":
            actual = "BENEFICIARY_VALIDATION_TIMEOUT"
        elif service_level_2 == "Card Management":
            actual = "CARD_STATUS_RULE_MISMATCH"
        else:
            actual = "STATEMENT_PERIOD_VALIDATION_FAILED"

    return {
        "case_number": case_number,
        "title": title,
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
        "expected": expected,
        "actual": actual,
        "should_fail": case_number in FAILED_CASES,
        "attach_text": case_number <= 25,
        "attach_csv": case_number <= 12,
    }


def _attach_unit_artifacts(case_data: dict) -> None:
    n = case_data["case_number"]

    if case_data["attach_text"]:
        allure.attach(
            (
                f"Unit evidence for case {n:03}\n"
                f"Service: {case_data['service_level_2']}\n"
                f"Release: {case_data['release']}\n"
                f"Severity: {case_data['severity']}\n"
                f"Expected: {case_data['expected']}\n"
                f"Actual: {case_data['actual']}\n"
            ),
            name=f"unit_note_{n:03}.txt",
            attachment_type=allure.attachment_type.TEXT,
        )

    if case_data["attach_csv"]:
        allure.attach(
            (
                "case,service,expected,actual,result\n"
                f"{n},{case_data['service_level_2']},{case_data['expected']},"
                f"{case_data['actual']},{'FAILED' if case_data['should_fail'] else 'PASSED'}\n"
            ),
            name=f"unit_data_{n:03}.csv",
            attachment_type=allure.attachment_type.CSV,
        )


def _make_unit_test(case_data: dict):
    def test_func():
        allure.dynamic.title(case_data["title"])
        allure.dynamic.epic(case_data["epic"])
        allure.dynamic.feature(case_data["feature"])
        allure.dynamic.story(case_data["story"])
        allure.dynamic.suite(case_data["suite"])
        allure.dynamic.label("layer", "unit")
        allure.dynamic.label("Business Unit", case_data["business_unit"])
        allure.dynamic.label("Service Level 1", case_data["service_level_1"])
        allure.dynamic.label("Service Level 2", case_data["service_level_2"])
        allure.dynamic.label("Application Unit", case_data["application_unit"])
        allure.dynamic.label("Release", case_data["release"])
        allure.dynamic.label("Severity", case_data["severity"])

        for tag in case_data["tags"]:
            allure.dynamic.tag(tag)

        with allure.step("Prepare validation input"):
            expected = case_data["expected"]
            actual = case_data["actual"]

        with allure.step("Compare actual rule output with expected value"):
            _attach_unit_artifacts(case_data)
            assert actual == expected, (
                f"Validation mismatch in case {case_data['case_number']:03}: "
                f"expected '{expected}', but got '{actual}'"
            )

    test_func.__name__ = f"test_{_sanitize_name(case_data['title'])}_{case_data['case_number']:03}"
    return test_func


for _case_number in range(1, 101):
    _case_data = _build_unit_case(_case_number)
    globals()[_make_unit_test(_case_data).__name__] = _make_unit_test(_case_data)