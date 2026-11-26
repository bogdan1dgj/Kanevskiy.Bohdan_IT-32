
import pytest

from expenses import parse_line, load_expenses, total_by_category


def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")

    assert record["category"] == "food"
    assert record["amount"] == 85.5
    assert record["date"] == "2026-09-21"


def test_parse_line_valid_second():
    record = parse_line("2026-09-22;transport;20;bus")

    assert record["category"] == "transport"
    assert record["amount"] == 20.0


def test_parse_line_valid_third():
    record = parse_line("2026-09-23;food;14.50;coffee")

    assert record["amount"] == 14.5


def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


def test_total_by_category(tmp_path):
    path = tmp_path / "expenses.csv"

    path.write_text(
        "# date;category;amount;comment\n"
        "2026-09-21;food;85.50;lunch\n"
        "\n"
        "2026-09-22;food;14.50;coffee\n",
        encoding="utf-8"
    )

    totals = total_by_category(load_expenses(path))

    assert totals == {"food": 100.0}
