import os
import json

dct_size_files = {}
lst_size = [100,1000,10000,100000]
main_path = os.path.join('.','some_data_adv')
main_path = os.path.abspath(main_path)

for size in lst_size:
    dct_size_files.setdefault(size,[0,[]])

for root,dirs,files in os.walk(main_path):
    for el in files:
        size_file = os.stat(os.path.join(main_path,el))[6]
        for size in lst_size:
            if size > size_file:
                dct_size_files[size][0] += 1
                type_file = el.split('.')[1]
                if type_file not in dct_size_files[size][1]:
                    dct_size_files[size][1].append(el.split('.')[1])
                    break

print(dct_size_files)

with open(main_path+'_summary.json', 'w') as f:
    f.write(json.dumps(str(dct_size_files), ensure_ascii=False))