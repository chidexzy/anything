import time, os, platform
from time import sleep
green = ('\033[1;32m')
red = ('\033[1;31m')
white = ('\033[1;37m')
os.system('clear')
def brand():
	print("""
:$$$$$$$\  $$$$$$$\  $$$$$$$$\ $$\   $$\ 
$$  __$$\ $$  __$$\ $$  _____|$$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |      \$$\ $$  |
$$ |  $$ |$$$$$$$  |$$$$$\     \$$$$  / 
$$ |  $$ |$$  __$$< $$  __|    $$  $$<  
$$ |  $$ |$$ |  $$ |$$ |      $$  /\$$\ 
$$$$$$$  |$$ |  $$ |$$$$$$$$\ $$ /  $$ |
\_______/ \__|  \__|\________|\__|  \__|
                                        
                                        
                                        """)
	time.sleep(0.5)
	os.system('clear')
	print("""
                                 
 â–ˆâ–€â–ˆ â–„â–€â–ˆ â–ˆâ–€â–€ â–ˆâ–„â–‘â–ˆ â–„â–€â–ˆ â–ˆâ–€â–ˆ â–ˆâ–€â–ˆ â–ˆâ–„â–€
 â–ˆâ–€â–„ â–ˆâ–€â–ˆ â–ˆâ–„â–ˆ â–ˆâ–‘â–€â–ˆ â–ˆâ–€â–ˆ â–ˆâ–€â–„ â–ˆâ–„â–ˆ â–ˆâ–‘â–ˆ""")
	time.sleep(0.5)
	os.system('clear')
brand()
brand()
bit = platform.architecture()[0]
if bit=='64bit':
    print(f'{red}[â€¢] DREX IS KING ðŸ‘‘ {white}')
    time.sleep(0.5)
    import trt1
elif bit=='32bit':
    import trt32
else:
    print(f'{green}[Ã—] Sorry System Not Support{white}')
