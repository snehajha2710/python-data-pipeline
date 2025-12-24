from data_loader import load_data
from processor import process_data

def main():
    print("Starting Python data pipeline 🚀")

    data = load_data()
    print("Loaded data:", data)

    processed_data = process_data(data)
    print("Processed data:", processed_data)

    with open("output.txt", "w") as file:
        file.write(str(processed_data))

    print("Data saved to output.txt ✅")

if __name__ == "__main__":
    main()
