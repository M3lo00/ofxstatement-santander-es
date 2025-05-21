import os

from ofxstatement.ui import UI

# Import the correct plugin class
from ofxstatement_santander_es.plugin import SantanderPlugin
from datetime import datetime
from decimal import Decimal


def test_santander_plugin() -> None:
    """
    Test the Santander plugin with a sample XLSX file.
    """
    plugin = SantanderPlugin(UI(), {})
    here = os.path.dirname(__file__)
    # Update to reference an XLSX file
    sample_filename = os.path.join(here, "sample-statement.xlsx")

    # Check if the sample file exists before attempting to parse
    if not os.path.exists(sample_filename):
        raise FileNotFoundError(
            f"Sample file not found: {sample_filename}. Please create it."
        )

    parser = plugin.get_parser(sample_filename)
    statement = parser.parse()

    # Add assertions based on your expected sample data
    assert statement is not None
    assert (
        len(statement.lines) > 0
    )  # Assuming the sample file has at least one transaction
    assert statement.currency == "EUR"  # Based on the parser's currency setting

    # Example assertions for dates and balances - adjust these based on your sample file data
    assert isinstance(statement.start_date, datetime)
    assert isinstance(statement.end_date, datetime)
    assert isinstance(statement.start_balance, Decimal)
    assert statement.start_balance == Decimal("1010.73")  # Example start balance
    assert isinstance(statement.end_balance, Decimal)
    assert statement.end_balance == Decimal("1000.23")  # Example end balance

    # You might want to add more specific assertions checking individual transaction details
    # For example:
    first_line = statement.lines[0]
    assert first_line.date == datetime(2023, 10, 26)  # Example date
    assert first_line.amount == Decimal("-10.50")  # Example amount
    assert first_line.memo == "Example Transaction Description"  # Example description
