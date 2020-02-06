# src_fname ='/bin/ls'
# dst_fname = '/tmp/list2'
# src_fobj = open(src_fname, 'rb')
# dst_fobj = open(dst_fname, 'wb')
# while 1:
#     data = src_fobj.read(4096)
#     if data == b'':
#         break
#     dst_fobj.write(data)
# src_fobj.close()
# dst_fobj.close()
src_fname = '/bin/ls'
dst_fname = '/tmp/list3'
src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')
while 1:
    data = src_fobj.read(4096)
    if not data:
        break
    dst_fobj.write(data)
src_fobj.close()
dst_fobj.close()