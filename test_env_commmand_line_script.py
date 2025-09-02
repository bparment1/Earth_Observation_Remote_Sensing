import numpy as np
import rasterio 
import pandas as pd
import argparse

def create_parser():
    parser_agent = argparse.ArgumentParser(description='Example command line script')
    #parser_agent.add_argument('--environment', '--env', choices=valid_environments(), default=DEFAULT_ENVIRONMENT)
    parser_agent.add_argument('--input_file',type=str, help='A .csv (or) .json file.', required=True)

    return parser_agent

def main():

    parser = create_parser()
    args = parser.parse_args()

    file_path = args.input_file

    df = pd.read_csv(file_path)

    print(f'Read in file{file_path}')
    print(df.to_string())

    return 1

if __name__ == "__main__":
     main()

"""#End of script"""

'''
#python test_env_command_line_script.py --input_file ./data/Sentinel2_level2A_band_description_updated.csv

'''