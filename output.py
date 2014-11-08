#!/usr/bin/python3
import os
import glob
import human_readable
import stat


#传递一个路径，以及-a -A的开启情况，返回路径下的文件名单(可能为绝对路径)
def get_filename_list(path, a_on = False, A_on = False):
    '''input a path and return a list of the files'''

    if os.path.exists(path):
        if stat.S_ISDIR(os.stat(path).st_mode):
            file_list = glob.glob(path+'/*')
        else:
            file_list = [path]
            return file_list
        if a_on:
            file_list = [path+'/.',path+'/..'] + glob.glob(path+'/.*') + file_list
        elif A_on:
            file_list = glob.glob(path+'/.*') + file_list
        return file_list
    else:
        print('error:path does not exist')
        exit()


#根据各参数(-l -n -i -H)启用情况，以及文件路径，返回信息行用于输出
def gen_line(path, l_on = False, n_on = False, i_on = False, h_on = False):
    '''input a filename or path and return a line'''

    if l_on:
        stat = os.stat(path)
        inode = stat.st_ino
        mode = human_readable.mode_convert(stat.st_mode)
        links = stat.st_nlink
        time = human_readable.time_convert(stat.st_mtime)
        #use id or name
        if n_on:
            uid = str(stat.st_uid)
            gid = str(stat.st_gid)
        else:
            uid = human_readable.uid_convert(stat.st_uid)
            gid = human_readable.gid_convert(stat.st_gid)
        #convert the size to readable form or not
        if h_on:
            size = human_readable.size_convert(stat.st_size)
        else:
            size = str(stat.st_size)
        filename = os.path.split(path)[1]

        line = [inode,mode,links,uid,gid,size,time,filename,]
        if i_on:
            return '{0[0]:<7.0f} {0[1]} {0[2]:3.0f} {0[3]:7} {0[4]:7} {0[5]:5} {0[6]} {0[7]}'.format(line)
        else:
            line.pop(0)
            return '{0[0]} {0[1]:3.0f} {0[2]:7} {0[3]:7} {0[4]:5} {0[5]} {0[6]}'.format(line)
    else:
        return os.path.split(path)[1]

