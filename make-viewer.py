import os
import shutil

code_path = os.getcwd() + '/input_code.txt'
chn_path = os.getcwd() + '/changed_opening'
base_path = os.getcwd()

chasi_code = []

with open(code_path, "r") as file:
    strings = file.readlines()

for idx in range(len(strings)):
    chasi_code.append( strings[idx].replace('\n', ''))


def createFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        # 해당 디렉토리 삭제
        shutil.rmtree(r'%s' %chn_path)
 

createFolder('./changed_opening')

def createDir(dir):
    os.makedirs('changed_opening/' + dir)


opening_dir = base_path + '/opening'
changed_dir = base_path + '/changed_opening'
reading_dir = base_path + '/reading'

opening_list = os.listdir(opening_dir)

reading_list = os.listdir(reading_dir)

for jdx in range(len(chasi_code)):
    createDir(chasi_code[jdx] + '_01')
    createDir(chasi_code[jdx] + '_02')
    print(chasi_code[jdx], '폴더 생성 완료')


changed_list = os.listdir(changed_dir)  


for kdx in range(len(changed_list)):
    if '_01' in changed_list[kdx]:
        for dir in range(6):
             if dir == 2:
                shutil.copy(opening_dir + '/' + opening_list[dir], chn_path + '/' + changed_list[kdx] + '/' + opening_list[dir])
             else: 
                shutil.copytree(opening_dir + '/' + opening_list[dir], chn_path + '/' + changed_list[kdx] + '/' + opening_list[dir])
       
    else:
        for dir in range(6):
            if  dir == 3:
                shutil.copy(reading_dir + '/' + reading_list[dir], chn_path + '/' + changed_list[kdx] + '/' + reading_list[dir])
            else:
                shutil.copytree(reading_dir + '/' + reading_list[dir], chn_path + '/' + changed_list[kdx] + '/' + reading_list[dir])
       


print('모든 폴더 생성 완료')