#!/usr/bin/python3
import output
import argparse
import os

parser = argparse.ArgumentParser(
        description='List information about the FILEs (the current directory by default)')

parser.add_argument('files', metavar='File', default='.', nargs='*',
        help='The files about which the information will be listed')

#options:
parser.add_argument('-l', '--long', action='store_true',
        help='use a long listing format')
parser.add_argument('-a', '--all', action='store_true',
        help='do not ignore entries starting with .')
parser.add_argument('-A', '--almost_all', action='store_true',
        help='do not list implied . and ..')
parser.add_argument('-H', '--human_readable', action='store_true',
        help='with -l and/or -s, print human readable sizes')
parser.add_argument('-i', '--inode', action='store_true',
        help=' print the index number of each file')
parser.add_argument('-n', '--numeric_uid_gid', action='store_true',
        help=' with -l, list numeric user and group IDs')
parser.add_argument('-R', '--recursive', action='store_true',
        help='list subdirectories recursively')
args = parser.parse_args()


#如果使用-R 这将替换args.files
if args.recursive:
    num_of_args = len(args.files)
    args_files_new = []
    n=0
    while n < num_of_args:
        for i in os.walk(args.files[n]):
            args_files_new += [i[0]]
        n += 1
    args.files = args_files_new


#遍历args.files列表中的路径参数
n = 0
num_of_args = len(args.files)
while n < num_of_args:

    print('\033[0;33;40m{0}:\033[0m'.format(os.path.realpath(args.files[n])))

    filename_list = output.get_filename_list(
            args.files[n], args.all, args.almost_all)   #获取路径下的文件列表

    m = 0
    num_of_files = len(filename_list)
    while m < num_of_files:
        print(output.gen_line(filename_list[m], args.long,
            args.numeric_uid_gid, args.inode, args.human_readable))     #对文件列表中的每项打印生成信息行
        m += 1
    n += 1

exit()
