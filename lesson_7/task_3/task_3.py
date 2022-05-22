import os
import os.path
import shutil

try:
    path_conf = os.path.join('.','config_2.yaml')
    path_conf = os.path.abspath(path_conf)
    f = open(path_conf,'r')

    lst_conf = []

    for line in f:
        lst_conf.append(line)
    f.close()


    for el in lst_conf:
        if el.startswith(' ') is False and ':' in el:
            main_path = os.path.join('.',lst_conf[0].replace(':','').strip())
            main_path = os.path.abspath(main_path)
        elif el.startswith('  - ') and ':' in el:
            sec_path = os.path.join(main_path,el.strip().replace('- ','').replace(':',''))
            sec_path = os.path.abspath(sec_path)
            os.makedirs(sec_path,exist_ok=True)
        elif el.startswith('    - ') and ':' in el:
            third_path = os.path.join(sec_path,el.strip().replace('- ','').replace(':',''))
            third_path = os.path.abspath(third_path)
            os.makedirs(third_path,exist_ok=True)
        elif el.startswith('      - ') and ':' in el:
            fourth_path = os.path.join(third_path,el.strip().replace('- ','').replace(':',''))
            fourth_path = os.path.abspath(fourth_path)
            os.makedirs(fourth_path,exist_ok=True)
        elif el.startswith('    - ') and '.' in el:
            file_path = os.path.join(sec_path, el.strip().replace('- ', '').replace(':', ''))
            file_path = os.path.abspath(file_path)
            with open(file_path,'w') as f:
                pass
        elif el.startswith('        - ') and '.' in el:
            file_sec_path = os.path.join(fourth_path, el.strip().replace('- ', '').replace(':', ''))
            file_sec_path = os.path.abspath(file_sec_path)
            with open(file_sec_path, 'w') as f:
                pass
    path_in_myproject = [os.path.join(main_path,item) for item in os.listdir(main_path)]
    for path in path_in_myproject:
        for root,dirs,files in os.walk(path):
            if 'templates' in dirs:
                shutil.copytree(os.path.join(path,'templates'),os.path.join(main_path,'templates'),dirs_exist_ok=True)
except (FileNotFoundError,EOFError) as e:
    print(f'concrete error: {e}')

