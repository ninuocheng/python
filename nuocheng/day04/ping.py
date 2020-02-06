import subprocess, sys


def ping(host='127.0.0.1'):
    result = subprocess.run(
        'ping -c2 %s' % host, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE
    )
    if result.returncode:
        print('%s: down' % host)
    else:
        print('%s: up' % host)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ping(sys.argv[1])
    else:
        ping()
