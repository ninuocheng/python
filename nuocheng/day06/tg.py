import os
for path, folders, files in os.walk('/tmp/nsd1909/demo/anquan'):
    print('%s: ' % path)
    for dir in folders:
        print('\033[34;1m%s\033[0m' % dir, end='\t')
    for file in files:
        print(file, end='\t')
    print('\n')