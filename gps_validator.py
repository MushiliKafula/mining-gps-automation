import csv
import os

INPUT_FILE = "data/gps_data.csv"
OUTPUT_FILE = "output/validated_report.csv"

def is_valid_coordinate(lat, lon):
    return -90 <= lat <= 90 and -180 <= lon <= 180

os.makedirs("output", exist_ok=True)

with open(INPUT_FILE, "r") as infile, open(OUTPUT_FILE, "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["status"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        lat = float(row["latitude"])
        lon = float(row["longitude"])
        row["status"] = "VALID" if is_valid_coordinate(lat, lon) else "INVALID"
        writer.writerow(row)

print("✅ GPS validation complete. Report generated.")
