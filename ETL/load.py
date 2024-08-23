import paths
import transform as tr

def write_csv():
    csv = open(paths.CLEAN_CSV, 'w+', newline='')
    df = tr.clean_csv()
    df.to_csv(csv, index=False, header=True)