import sys, subprocess


def ping(host):
    result = subprocess.run(
        'ping -c2 %s' % host, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    # print(result)
    if result.returncode:
        return '%s: down' % host
    else:
        # return '%s: up' % host
        return ('%s: up' % host, result.stderr.decode(), result.stdout.decode(), result.returncode)


if __name__ == '__main__':
    print(sys.argv)
    print(ping(sys.argv))
    print(ping(sys.argv[1]))
    print((ping(sys.argv[1]))[0])
    print(sys.argv[0])
    print(ping(sys.argv[1]))
    print(sys.argv[1])
