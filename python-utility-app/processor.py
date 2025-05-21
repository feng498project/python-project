def filter_rows(data):
    # Basit filtre: sadece 'active' sütunu 'yes' olanları al
    return [row for row in data if row.get("active", "").lower() == "yes"]
