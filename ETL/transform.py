import extract as e

def clean_csv():
    df = e.read_ftx()
    df.pop("Time")
    df.pop("Description")
    df = df.add_prefix("clean_")
    return df