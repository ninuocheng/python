import sys, subprocess, secret


def add_user(un, pas, fn):
    result = subprocess.run(
        'id  %s' % un, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    print(result.returncode)
    if result.returncode:
        subprocess.run(
            'useradd %s' % un, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        subprocess.run(
            'echo %s | passwd --stdin %s' % (pas, un), shell=True, stderr=subprocess.PIPE
        )
        info = '''用户信息:
用户: %s
密码: %s
''' % (un, pas)
        with open(fn, 'a') as fobj:
            fobj.write(info)
    else:
        print('用户已存在.')


if __name__ == '__main__':
    un = sys.argv[1]
    fn = sys.argv[2]
    pas = secret.mk_pas()
    add_user(un, pas, fn)
