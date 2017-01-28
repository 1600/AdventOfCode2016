#!coding=utf-8

import re
import collections

sample = 'aaaaa-bbb-z-y-x-123[abxyz]'

def generateChecksum(text):
    text = text.replace('-','')
    d = {}
    for i in text:
        if not i in d:
            d[i] = text.count(i)
    return (''.join(sorted(d, key=lambda k:(-d[k],k))))[:5]

def isReal(item):
    '''checksum is a FIVE letter sequence, the letters in the sequence occurs the most in the encrypted room-name in a descent order.
    '''
    delim_pos = item.rfind('-')
    name = item[:delim_pos]
    sectorid_checksum = item[delim_pos:]
    checksum_r = r'(?:\[)([a-z]+)(?:\])'     # matching checksum
    sectorid_r = r'(\d+)(?:\[)'              # matching sector id
    checksum = re.findall(checksum_r,sectorid_checksum)[0]
    sectorID = re.findall(sectorid_r,sectorid_checksum)[0]
    g_cks = generateChecksum(name)
    print "name is >>",name
    print "! Calculated Checksum is : ",g_cks
    print "! Given Checksum is      : ",checksum
    if checksum == g_cks:
        print "Real Room!!! "+sectorID
        return int(sectorID)
    else:
        print "Fake Room..."
        return 0

with open('input.txt','r') as f:
    sum = 0
    for i in f.readlines():
        sum += isReal(i)
    print sum