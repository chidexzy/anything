import os,time,platform
os.system('clear')
print('[•] Not UpdatIng 😜...')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')

print('<------------------------------------>')
bit = platform.architecture()[0]
if bit=='64bit':
    print(f'{red}[•] DREX IS KING 👑 {white}')
    time.sleep(0.5)
    import trt1
elif bit=='32bit':
    import trt32
else:
    print(f'{green}[×] Sorry System Not Support{white}')
