import socket,struct,time,os,sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 2)
slowprint ('ASSALAMUALAIKUM WR WB')
print
slowprint('Selamat Datang User Di Newbie Tools')
print
slowprint(' Dan selamat bersenang-senang')
print
slowprint(' TERIMA KASIH YANG UDAH SUPPRORT GW')


os.system('sh loginv2.sh')

exit()
