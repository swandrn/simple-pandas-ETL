import paths
import pandas as pd

#Read sample CSV file and return a dataframe
def read_sample():
    pd.set_option("display.max_columns", None)
    df = pd.read_csv(paths.SAMPLE_CSV)
    return df