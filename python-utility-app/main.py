from file_handler import read_csv, write_csv
from processor import filter_rows
import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple CSV Filter Utility")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path to output CSV file")
    args = parser.parse_args()

    data = read_csv(args.input)
    filtered = filter_rows(data)
    write_csv(args.output, filtered)
    print(f"Filtered data written to {args.output}")

if __name__ == "__main__":
    main()
