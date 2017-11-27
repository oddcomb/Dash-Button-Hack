from scapy.all import *

import requests

ifttt_url_neil = 'https://maker.ifttt.com/trigger/dog_fed/with/key/moh8SPLs5ayavn7uQGO_-u_KcGna_hHpr2j9Z-C2hyH'


def arp_display(pkt):
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc == '18:74:2e:d8:db:a7': #gatorade button no. 1
            print ('dash button pressed! Neil has been fed.')
            requests.post('https://maker.ifttt.com/trigger/dog_fed/with/key/moh8SPLs5ayavn7uQGO_-u_KcGna_hHpr2j9Z-C2hyH')
            print('Hey, Mitsu!')
		

print (sniff(prn=arp_display, filter='arp', store=0, count=0))

