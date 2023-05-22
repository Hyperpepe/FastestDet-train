import os

def count_files(path):
    file_count = 0
    dir_count = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            file_count += 1
        for name in dirs:
            dir_count += 1
    return (file_count, dir_count)

def print_counts(path):
    file_count, dir_count = count_files(path)
    print(f"{path} has {file_count} files and {dir_count} directories.")

def count_files_by_extension(path):
    file_count = {}
    for root, dirs, files in os.walk(path):
        for name in files:
            ext = os.path.splitext(name)[1][1:]
            if ext not in file_count:
                file_count[ext] = 0
            file_count[ext] += 1
    return file_count

def print_counts_by_extension(path):
    file_count = count_files_by_extension(path)
    print(f"{path} has the following files by extension:")
    for ext, count in file_count.items():
        print(f"{ext}: {count}")

def count_files_by_extension_and_directory(path):
    file_count = {}
    for root, dirs, files in os.walk(path):
        for name in files:
            ext = os.path.splitext(name)[1][1:]
            if ext not in file_count:
                file_count[ext] = {}
            if root not in file_count[ext]:
                file_count[ext][root] = 0
            file_count[ext][root] += 1
    return file_count

def print_counts_by_extension_and_directory(path):
    file_count = count_files_by_extension_and_directory(path)
    print(f"{path} has the following files by extension and directory:")
    for ext, dirs in file_count.items():
        print(f"{ext}:")
        for dir, count in dirs.items():
            print(f"    {dir}: {count}")

path = '/mnt/c/linux/FastestDet-main/datasets-daozha/'
print_counts(path)
print_counts_by_extension(path)
print_counts_by_extension_and_directory(path)

