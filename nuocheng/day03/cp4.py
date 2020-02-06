src_fname = '/bin/cat'
dst_fname = '/tmp/catbakkk'
src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')
while 1:
    data = src_fobj.read(4096)
    if data:
        dst_fobj.write(data)
        continue
    break
src_fobj.close()
dst_fobj.close()