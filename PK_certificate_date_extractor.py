def parse_expiry_data(timestamp):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    tokens = timestamp.split()
    if len(tokens) < 4:
        return None  # Invalid timestamp format

    month_str, date_str, year_str = tokens[:3]

    month = months.index(month_str) + 1
    date = int(date_str)
    year = int(year_str)

    return f"{year:04d}{month:02d}{date:02d}"

# Example usage:
timestamp = "Jan 15 2024 10:30:00"
expiry_date = parse_expiry_data(timestamp)
print("Expiry Date:", expiry_date)
