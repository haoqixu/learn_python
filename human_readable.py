#!/usr/bin/python3
import time
import grp
import pwd
import stat


def size_convert(size):

    '''convert the size to human-readable form'''

    SUFFIXES = ['KiB','MiB','GiB','TiB','PiB']

    for suffix in SUFFIXES:
        size /= 1024
        if size < 1024:
            return '{0:.1f} {1}'.format(size, suffix)
        else:
            raise ValueError('number too large.')

def mode_convert(st_mode):

    '''convert the bin-number-form mode to rwx-form'''

    mode     = list(bin(st_mode)[-12:])         #for list.pop()
    count    = 3                  #len(mode) // 3 - 1
    mode_rwx = []

    while count:
        if mode.pop() == '1':
            mode_rwx = ['x'] + mode_rwx
        else:
            mode_rwx = ['-'] + mode_rwx

        if mode.pop() == '1':
            mode_rwx = ['w'] + mode_rwx
        else:
            mode_rwx = ['-'] + mode_rwx

        if mode.pop() == '1':
            mode_rwx = ['r'] + mode_rwx
        else:
            mode_rwx = ['-'] + mode_rwx
        count -= 1

    if mode.pop() == '1':
        if mode_rwx[-1] == 'x':
            mode_rwx[-1] = 't'
        else:
            mode_rwx[-1] = 'T'
    if mode.pop() == '1':
        if mode_rwx[-4] == 'x':
            mode_rwx[-4] = 's'
        else:
            mode_rwx[-4] = 'S'
    if mode.pop() == '1':
        if mode_rwx[2]  == 'x':
            mode_rwx[2]  = 's'
        else:
            mode_rwx[2]  = 'S'
    mode_rwx = ''.join(mode_rwx)

    if stat.S_ISREG(st_mode):
        mode_return = '-' + mode_rwx
    elif stat.S_ISDIR(st_mode):
        mode_return = 'd' + mode_rwx
    elif stat.S_ISLNK(st_mode):
        mode_return = 'l' + mode_rwx
    elif stat.S_ISBLK(st_mode):
        mode_return = 'b' + mode_rwx
    elif stat.S_ISCHR(st_mode):
        mode_return = 'c' + mode_rwx
    elif stat.S_ISSOCK(st_mode):
        mode_return = 's' + mode_rwx
    elif stat.S_ISFIFO(st_mode):
        mode_return = 'p' + mode_rwx
    else:
        mode_return = '?' + mode_rwx

    return mode_return


def time_convert(time_unreadable):

    '''convert the time to human-readable form'''

    MONTHS = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aus', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

    time_unreadable = time.localtime(time_unreadable)
    time_readable = '{0} {1} {2:2.0f} {3:2.0f}:{4:2.0f}'.format( time_unreadable.tm_year,MONTHS[time_unreadable.tm_mon], time_unreadable.tm_mday, time_unreadable.tm_hour, time_unreadable.tm_min)

    return time_readable


def uid_convert(uid):
    return pwd.getpwuid(uid).pw_name
def gid_convert(gid):
    return grp.getgrgid(gid).gr_name
