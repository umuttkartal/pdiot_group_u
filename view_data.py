import pandas as pd
import matplotlib.pyplot as plt
from typing import List
import os

SRC_DIR = SRC_DIR = os.path.dirname(__file__)
CLEAN_DIR = os.path.join(SRC_DIR, './data/04-10-22:14:50')

def get_files_in_dir(dir) -> List[str]:
    try:
        return os.listdir(dir)
    except Exception as e:
        print(f'Failed to get files in {dir}.\n{e}')
        return []

def read_data(file_dir, filename):
    path = os.path.join(file_dir, filename)

    return pd.read_csv(path)

def plot_respeck(dataframe: pd.DataFrame, filename):
    fig, ax = plt.subplots(2, 1, figsize=(12, 12))

    # plot respeck
    ax[0].plot(dataframe['accel_x'], label="accel_x")
    ax[0].plot(dataframe['accel_y'], label="accel_y")
    ax[0].plot(dataframe['accel_z'], label="accel_z")
    ax[0].legend()

    ax[0].set_title(f"{dataframe['sensor_type'].values[0]} - {dataframe['activity_type'].values[0]} \n Accelerometer data")

    ax[1].plot(dataframe['gyro_x'], label="gyro_x")
    ax[1].plot(dataframe['gyro_y'], label="gyro_y")
    ax[1].plot(dataframe['gyro_z'], label="gyro_z")
    ax[1].legend()

    ax[1].set_title(f"{dataframe['sensor_type'].values[0]} - {dataframe['activity_type'].values[0]} \n Gyroscope data")

    
    # plt.show(block=True)

    plt.savefig("./plotRespeckFinal/" + filename + ".png")

def plot_thingy(dataframe: pd.DataFrame, filename):
    fig, ax = plt.subplots(3, 1, figsize=(12, 18))

    # plot thingy
    ax[0].plot(dataframe['accel_x'], label="accel_x")
    ax[0].plot(dataframe['accel_y'], label="accel_y")
    ax[0].plot(dataframe['accel_z'], label="accel_z")
    ax[0].legend()

    ax[0].set_title(f"{dataframe['sensor_type'].values[0]} - {dataframe['activity_type'].values[0]} \n Accelerometer data")

    ax[1].plot(dataframe['gyro_x'], label="gyro_x")
    ax[1].plot(dataframe['gyro_y'], label="gyro_y")
    ax[1].plot(dataframe['gyro_z'], label="gyro_z")
    ax[1].legend()

    ax[1].set_title(f"{dataframe['sensor_type'].values[0]} - {dataframe['activity_type'].values[0]} \n Gyroscope data")

    ax[2].plot(dataframe['mag_x'], label="mag_x")
    ax[2].plot(dataframe['mag_y'], label="mag_y")
    ax[2].plot(dataframe['mag_z'], label="mag_z")
    ax[2].legend()

    ax[2].set_title(f"{dataframe['sensor_type'].values[0]} - {dataframe['activity_type'].values[0]} \n Magnetometer data")

    # plt.show(block=True)

    plt.savefig("./plotThingyFinal/" + filename + ".png")

def main():
    files = get_files_in_dir(CLEAN_DIR)

    for file in files:
        dataframe = read_data(CLEAN_DIR, file)

        if file.startswith('Respeck'):
            plot_respeck(dataframe, file)

        elif file.startswith('Thingy'):
            plot_thingy(dataframe, file)

        else:
            print(f'Invalid file name {file}')

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        exit(0)