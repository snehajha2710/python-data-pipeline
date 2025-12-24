def load_data():
    """
    Load sample data.
    Handles errors safely.
    """
    try:
        data = [10, 20, 30, 40, 50]
        return data
    except Exception as e:
        print("Error loading data:", e)
        return []
