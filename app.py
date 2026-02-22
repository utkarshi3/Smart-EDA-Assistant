import argparse
from eda_engine import (
    load_dataset,
    get_basic_summary,
    get_column_types,
    get_statistical_summary
)

def main():
    parser = argparse.ArgumentParser(description="Smart EDA Assistant")
    parser.add_argument("--file", type=str, required=True, help="Path to dataset file")

    args = parser.parse_args()

    df = load_dataset(args.file)

    print("\n===== BASIC SUMMARY =====")
    print(get_basic_summary(df))

    print("\n===== COLUMN TYPES =====")
    print(get_column_types(df))

    print("\n===== STATISTICAL SUMMARY =====")
    print(get_statistical_summary(df))

if __name__ == "__main__":
    main()