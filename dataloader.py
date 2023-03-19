import os
import glob
import collections
import random

def list_files(dataset_path):
    return glob.glob(dataset_path+'/*/*')

def get_class(fname):
    return fname.split('/')[-2]

def get_files_per_class(files):
    files_for_class = collections.defaultdict(list)
    for fname in files:
        class_name = get_class(fname)
        files_for_class[class_name].append(fname)
    return files_for_class

def split_class_lists(files_for_class, split_percent):
    """
        Returns the list of files belonging to a subset of data as well as the remainder of
        files.
    """
    split_files = []
    remainder = {}
    for cls in files_for_class:
        count = int(len(files_for_class[cls]) * (split_percent/100))
        split_files.extend(files_for_class[cls][:count])
        remainder[cls] = files_for_class[cls][count:]
    return split_files, remainder

# def download_ufc_101_subset(zip_url, num_classes, splits, download_dir):
def Dataset(dataset_path , num_classes, splits):
    """
        split them into various parts, such as training, validation, and test. 

        Return:
        dir: path of the resulting directories containing the splits of data.
    """
    files = list_files(dataset_path)
    print(f"Total Number of Videos: {len(files)}")
    for f in files:
        tokens = f.split('/')
        if len(tokens) <= 2:
            files.remove(f) #  the list if it doRemove that item fromes not have a filename
        
    files_for_class = get_files_per_class(files)  
    classes = list(files_for_class.keys())
    count = 0

    for cls in classes:
        new_files_for_class = files_for_class[cls]
        random.shuffle(new_files_for_class)
        files_for_class[cls] = new_files_for_class

    dirs = {} 
    for split_name, split_percent in splits.items():
        split_files, files_for_class = split_class_lists(files_for_class, split_percent)
        dirs[split_name] = split_files

    return dirs, classes

