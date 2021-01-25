'''
Author: JuncFang
Date: 2021-01-23 20:50:26
LastEditTime: 2021-01-25 11:06:19
LastEditors: JuncFang
Description: 
FilePath: \EasyScript\script\cu_version.py
'''
import os
import subprocess

def get_cmd_path(cmd_name):
    where_cmd = 'whereis %s'%cmd_name
    status, res = subprocess.getstatusoutput(where_cmd)
    path = res.split()[-1]
    # print('%s path: '%cmd_name, path)
    return path
    
def print_cuda_version(cuda_path):
    cat_cmd = 'cat %s/version.txt'%cuda_path
    os.system(cat_cmd)
    

def print_cudnn_version(cudnn_path):
    head_file = open(cudnn_path)
    lines = head_file.readlines()
    # print(lines)
    for line in lines:
        line = line.strip()
        if line.startswith('#define CUDNN_MAJOR'):
            line = line.split('#define CUDNN_MAJOR')
            n1 = int(line[1])
            continue
        if line.startswith('#define CUDNN_MINOR'):
            line = line.split('#define CUDNN_MINOR')
            n2 = int(line[1])
            continue
        if line.startswith('#define CUDNN_PATCHLEVEL'):
            line = line.split('#define CUDNN_PATCHLEVEL')
            n3 = int(line[1])
            break
    print('CUDNN Version ', str(n1)+'.'+str(n2)+'.'+str(n3))

if __name__ == "__main__":
    cuda_path = get_cmd_path('cuda')
    cudnn_path = get_cmd_path('cudnn')
    print_cuda_version(cuda_path)
    print_cudnn_version(cudnn_path)