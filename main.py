from pathlib import Path
import csv

DATA_FILE = Path("orders.csv")
OUTPUT_DIR = Path("output")
REPORT_TITLE = "Daily Order Summary"


def is_valid_order_id(order_id: str) -> bool:
    """Return True when an order ID contains non-whitespace text."""
    return bool(order_id.strip())


def load_orders(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def main() -> None:
    orders = load_orders(DATA_FILE)

    accepted = sum(
        is_valid_order_id(order["order_id"])
        for order in orders
    )
    rejected = len(orders) - accepted

    lines = [
        REPORT_TITLE,
        f"Source: {DATA_FILE.name}",
        f"Processed: {len(orders)}",
        f"Accepted: {accepted}",
        f"Rejected: {rejected}",
    ]

    for line in lines:
        print(line)

    OUTPUT_DIR.mkdir(exist_ok=True)
    (OUTPUT_DIR / "summary.txt").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
