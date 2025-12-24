def process_data(data):
    """
    Process data safely.
    """
    processed = []

    try:
        for item in data:
            processed.append(item * 2)
        return processed
    except Exception as e:
        print("Error processing data:", e)
        return []
