import os
import glob
import pandas as pd

testcases_path = '/Users/joaomena/Documents/test_cases/'

class Task:
    def __init__(self, task_dict):
        self.name = task_dict['name']
        self.duration = task_dict['duration']
        self.period = task_dict['period']
        self.type = task_dict['type']
        self.priority = task_dict['priority']
        self.deadline = task_dict['deadline']

def tasks_parser(path):
    """
    get all tasks from the .csv files in the testcases folder and return them as objects in a list
    Arguments:
        (string) path - path to folder
    Returns:
        (list) task_list - list with all tasks as Task objects
    """

    # join_files = os.path.join(f"{path}/*/*.csv") #use /*/*/.csv for all tasks or specify path for specific datasets
    # joined_list = glob.glob(join_files)

    # df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True) #read all .csv files into dataframe

    # df.to_csv(f'{path}/tasks.csv', index=False) #export dataframe to single .csv file

    df = pd.read_csv(f'{path}/inf_10_10/taskset__1643188013-a_0.1-b_0.1-n_30-m_20-d_unif-p_2000-q_4000-g_1000-t_5__0__tsk.csv', sep=';').to_dict(orient="index") #read single .csv file and separate columns by ';'

    task_list = []
    for task in df:
        task_list.append(Task(df[task]))

    return task_list

def main():
    task_list = tasks_parser(testcases_path) #creates list with an object Task for every task in  the csv files

if __name__ == "__main__":
    main()