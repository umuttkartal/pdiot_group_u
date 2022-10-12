import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List
import os

SRC_DIR = SRC_DIR = os.path.dirname(__file__)
RAW_DIR = os.path.join(SRC_DIR, './data/raw/')
CLEAN_DIR = os.path.join(SRC_DIR, './data/04-10-22:14:50/')

HEADER_SIZE = 5

def get_files_in_dir(dir) -> List[str]:
    try:
        return os.listdir(dir)
    except Exception as e:
        print(f'Failed to get files in {dir}.\n{e}')
        return []

def extract_header_info(file_dir: str, filename: str, header_size: int = HEADER_SIZE) -> Tuple[str, str, int, str, str]:
    """
    :param filename: Path to recording file.
    :param header_size: The size of the header, defaults to 5.
    :returns: A 5-tuple containing the sensor type, activity type, activity code, subject id and any notes.
    """
    sensor_type = ""
    activity_type = ""
    activity_code = -1
    subject_id = ""
    notes = ""

    path = os.path.join(file_dir, filename)

    with open(path) as f:
        head = [next(f).rstrip().split('# ')[1] for x in range(header_size)]
        for l in head:
            # print(l)

            title, value = l.split(":")

            if title == "Sensor type":
                sensor_type = value.strip()
            elif title == "Activity type":
                activity_type = value.strip()
            elif title == "Activity code":
                activity_code = int(value.strip())
            elif title == "Subject id":
                subject_id = value.strip()
            elif title == "Notes":
                notes = value.strip()
    
    return sensor_type, activity_type, activity_code, subject_id, notes

def format_data(file_dir: str, filename: str, header_size: int = HEADER_SIZE):
    print(filename)
    sensor_type, activity_type, activity_code, subject_id, notes = extract_header_info(file_dir, filename)
    recording_id = os.path.splitext(filename)[0]

    path = os.path.join(file_dir, filename)
    
    dataframe = pd.read_csv(path, header=header_size)

    # Add additional columns for metadata
    dataframe['sensor_type'] = sensor_type
    dataframe['activity_type'] = activity_type
    dataframe['activity_code'] = activity_code
    dataframe['subject_id'] = subject_id
    dataframe['notes'] = notes
    dataframe['recording_id'] = recording_id

    return dataframe

def save_data(dataframe: pd.DataFrame):
    rec_name = dataframe.recording_id.values[0]
    path = os.path.join(CLEAN_DIR, rec_name + '.csv')
    dataframe.to_csv(path, index=False)

    print(f'{rec_name}.csv saved.')

def get_frequency(dataframe: pd.DataFrame, ts_column: str = 'timestamp') -> float:
    """
    :param dataframe: Dataframe containing sensor data. It needs to have a 'timestamp' column.
    :param ts_column: The name of the column containing the timestamps. Default is 'timestamp'.
    :returns: Frequency in Hz (samples per second)
    """

    return len(dataframe) / ((dataframe[ts_column].iloc[-1] - dataframe[ts_column].iloc[0]) / 1000)

def main():
    # Create directory for clean data if does not exist
    if not os.path.exists(CLEAN_DIR):
        os.makedirs(CLEAN_DIR)

    files = get_files_in_dir(RAW_DIR)

    for file in files:
        dataframe = format_data(RAW_DIR, file)
        save_data(dataframe)


if __name__ == '__main__':
    main()