hi = 'hello world'
def pstar(n = 30):
    print('*' * n)
# name = 'gzc'
# def age(n = 29):
#     print(n)
# def file():
#     src_fname = open('/bin/ls', 'rb')
#     dst_fname = open('/tmp/lss', 'wb')
#     while 1:
#         data = src_fname.read(4096)
#         if data:
#             dst_fname.write(data)
#             continue
#         break
#     src_fname.close()
#     dst_fname.close()
if __name__ == '__main__':
    print(hi)
    pstar()
    pstar(50)