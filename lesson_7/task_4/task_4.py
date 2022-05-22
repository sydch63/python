import os

dct_size_files = {}
lst_size = [100,1000,10000,100000]
main_path = os.path.join('.','some_data')
main_path = os.path.abspath(main_path)

for size in lst_size:
    dct_size_files.setdefault(size,0)

for root,dirs,files in os.walk(main_path):
    for el in files:
        size_file = os.stat(os.path.join(main_path,el))[6]
        for size in lst_size:
            if size > size_file:
                dct_size_files[size] += 1
                break

