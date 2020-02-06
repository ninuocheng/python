# import shutil
# f1 = open('/etc/hosts', 'rb')
# f2 = open('/tmp/guo.txt', 'wb')
# shutil.copyfileobj(f1, f2)
# f1.close()
# f2.close()
# #cp /etc/hosts /tmp/zj1
# shutil.copy('/etc/hosts', '/tmp/zj1')
# #cp -p /etc/hosts /tmp/zj2
# shutil.copy2('/etc/hosts', '/tmp/zj2')
# #cp -r /etc/security /tmp/anquan
# shutil.copytree('/etc/security', '/tmp/anquan')
# #mv /tmp/anquan /var/tmp/
# shutil.move('/tmp/anquan', '/var/tmp/')
# #chown bob.bob /tmp/zj2
# shutil.chown('/tmp/zj2', user='bob', group='bob')
# rm -rf /var/tmp/anquan
# shutil.rmtree('/var/tmp/anquan')
# import os
# #rm -rf /tmp/zj1
# os.remove('/tmp/zj1')
import subprocess

# subprocess.run('ls ~', shell=True)
# subprocess.run('id root; id john', shell=True)
result = subprocess.run('id root; id john', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if __name__ == '__main__':
    print(result.stdout.decode())
    print(result.stderr)
