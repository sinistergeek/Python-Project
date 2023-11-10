import time
import sys

print('Welcome To fastrack USSD Banking Project...')
time.sleep(8)

bank_list="""
1. Access Bank
2. Fidelity Bank
3. Guarantee Trust Bank
4. Heritage Bank
5. Polaris Bank
6. Stanbic IBTC
7. Unity Bank
8. Wema Bank
"""

get_bvn = ""

def BVN_checker():
    global gen_bvn
    bvn = [str(i) for i in range(5)]
    gen_bvn = "".join(bvn)

def open_acct():
    global gen_bvn
    print("Welcome to our Online Account opening services.")
    print("loading ...")
    temp_storage=[]

