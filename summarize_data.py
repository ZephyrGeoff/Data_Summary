import pandas as pd 

def summarizeData(file_path):
    try:
        #load csv file
        df = pd.read_csv(file_path)
        print("File loaded successfully.\n")

        #Basic descriptive statistics
        print("--- Data Summary ---")
        print(df.describe())

        #Count rows and columns
        rows, cols = df.shape
        print(f"\nRows: {rows}, Columns: {cols}")

        #Calculate custom summaries (mean for numeric columns)
        print("\nColumn Means:")
        print(df.mean(numeric_only=True))

    except FileNotFoundError:
        print("Error: File not found. Please check the path.")
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
    except Exception as e:
        print(f"Unexpected error: {e}")

