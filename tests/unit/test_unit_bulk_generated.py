import allure


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
    elif case_number <= 63:
        service_level_2 = "Beneficiaries"
        application_unit = "UA-Payments-Orchestrator"
        title = f"Validate beneficiary rule {case_number:03}"
        feature = "Beneficiaries"
        story = "Beneficiary Validation"
        suite = "Beneficiary Engine"
    elif case_number <= 81:
        service_level_2 = "Card Management"
        application_unit = "UA-Card-Control-Service"
        title = f"Validate card rule {case_number:03}"
        feature = "Cards"
        story = "Card Rules"
        suite = "Card Engine"
    else:
        service_level_2 = "Statements"
        application_unit = "UA-Statement-Service"
        title = f"Validate statement rule {case_number:03}"
        feature = "Statements"
        story = "Statement Rules"
        suite = "Statement Engine"

    release = "33.3.1" if case_number <= 46 else "33.3.2"

    if case_number % 10 == 0:
        severity = "Critical"
    elif case_number % 3 == 0:
        severity = "Major"
    else:
        severity = "Minor"

    tags = ["full", "regress"]
    if case_number <= 28:
        tags.append("smoke")

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
        "attach_text": case_number <= 18,
        "attach_csv": case_number <= 9,
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
            ),
            name=f"unit_note_{n:03}.txt",
            attachment_type=allure.attachment_type.TEXT,
        )

    if case_data["attach_csv"]:
        amount = 1000 + n
        fee = 5
        total = amount + fee
        allure.attach(
            f"amount,fee,total\n{amount},{fee},{total}\n",
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

        with allure.step("Prepare rule inputs"):
            pass

        with allure.step("Validate calculation result"):
            pass

        _attach_unit_artifacts(case_data)
        assert True

    test_func.__name__ = f"test_{_sanitize_name(case_data['title'])}_{case_data['case_number']:03}"
    return test_func


for _case_number in range(1, 101):
    _case_data = _build_unit_case(_case_number)
    globals()[_make_unit_test(_case_data).__name__] = _make_unit_test(_case_data)