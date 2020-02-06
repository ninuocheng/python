import os
os.chdir('/tmp/nsd1909/demo')
for path, folders, files in os.walk('anquan'):
    print('%s: ' % path)
    for dir in folders:
        print('\033[34;1m%s\033[0m' % dir, end='\t')
    for file in files:
        print(file, end='\t')
    print('\n')