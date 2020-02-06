import random, subprocess, sys
ch = 'qwertyuiopasdfghjklzxcvbnm,7894561230QWERTYUIOPASDFGHJKLZXCVBNM<>!@#$%^&*()_+<>?'

def mk_user(uname, pas, fname):
    result = subprocess.run(
        'id %s' % uname, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode:
        subprocess.run(
            'useradd  %s' % uname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        subprocess.run(
            'echo %s | passwd --stdin %s' % (pas, uname), shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        info = '''用户信息:
用户: %s
密码: %s
''' % (uname, pas)
        with open(fname, 'a') as fobj:
            fobj.write(info)
    else:
        print('用户已存在.')
def set_pass():
    ps = ''
    while 1:
        pa = random.choice(ch)
        ps += pa
        if len(ps) == 8:
#return默认返回None,类似于break, 函数遇到return也会提前结束
            return ps
if __name__ == '__main__':
    pas = set_pass()
    uname = sys.argv[1]
    fname = sys.argv[2]
    mk_user(uname, pas, fname)