import socket
import select
import requests
import threading
import re
import time
import struct
import urllib3
import random
import os
from datetime import datetime, timedelta
import json
import requests
from datetime import datetime, timedelta
import time
import threading
#################################

RbGx = False
back = False
enc_client_id = None
inviteD = False
inviteD = False
back = False
invit_spam = False

#################################

SOCKS_VERSION = 5

#################################


def generate_random_color():
	color_list = [
    "[00FF00][b][c]",
    "[FFDD00][b][c]",
    "[3813F3][b][c]",
    "[FF0000][b][c]",
    "[0000FF][b][c]",
    "[FFA500][b][c]",
    "[DF07F8][b][c]",
    "[11EAFD][b][c]",
    "[DCE775][b][c]",
    "[A8E6CF][b][c]",
    "[7CB342][b][c]",
    "[FF0000][b][c]",
    "[FFB300][b][c]",
    "[90EE90][b][c]"
]
	random_color = random.choice(color_list)
	return  random_color
	
def get_status(user_id):
    try:
        r = requests.get(f'https://ff.garena.com/api/antihack/check_banned?lang=en&uid={user_id}')
        if "0" in r.text:
            return f"{get_random_color()}▶PLAYER STATUS: {get_random_color()} Account Clear!"
        else:
            return "{get_random_color()}▶PLAYER STATUS: {get_random_color()} Account Ban!"
    except Exception as e:
        return f"Error checking status: {e}"
def get_player_info(user_id):
    try:
        cookies = {
            '_ga': 'GA1.1.2123120599.1674510784',
            '_fbp': 'fb.1.1674510785537.363500115',
            '_ga_7JZFJ14B0B': 'GS1.1.1674510784.1.1.1674510789.0.0.0',
            'source': 'mb',
            'region': 'MA',
            'language': 'ar',
            '_ga_TVZ1LG7BEB': 'GS1.1.1674930050.3.1.1674930171.0.0.0',
            'datadome': '6h5F5cx_GpbuNtAkftMpDjsbLcL3op_5W5Z-npxeT_qcEe_7pvil2EuJ6l~JlYDxEALeyvKTz3~LyC1opQgdP~7~UDJ0jYcP5p20IQlT3aBEIKDYLH~cqdfXnnR6FAL0',
            'session_key': 'efwfzwesi9ui8drux4pmqix4cosane0y',
        }
        headers = {
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://shop2game.com',
            'Referer': 'https://shop2game.com/app/100067/idlogin',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'accept': 'application/json',
            'content-type': 'application/json',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'x-datadome-clientid': '20ybNpB7Icy69F~RH~hbsvm6XFZADUC-2_--r5gBq49C8uqabutQ8DV_IZp0cw2y5Erk-KbiNZa-rTk1PKC900mf3lpvEP~95Pmut_FlHnIXqxqC4znsakWbqSX3gGlg',
        }
        json_data = {
            'app_id': 100067,
            'login_id': str(user_id),
            'app_server_id': 0,
        }
        response = requests.post(
            'https://shop2game.com/api/auth/player_id_login',
            cookies=cookies,
            headers=headers,
            json=json_data
        )

        if response.status_code == 200:
            player_info = response.json()
            if 'region' in player_info and 'nickname' in player_info:
                return {
                    "region": f"{get_random_color()}\n\n⏯PLAYER REGION: {player_info['region']}\n\n",
                    "nickname": f"{get_random_color()}\n\n⏭PLAYER NAME: {player_info['nickname']}\n\n"
                }
            else:
                return {"error": "Invalid response format"}
        else:
            return {"error": f"Failed to fetch player info: {response.status_code}"}

    except Exception as e:
        return {"error": f"Error fetching player info: {e}"}
##########DEF INFO REGION############
def getname(Id):    
    url = "https://shop2game.com/api/auth/player_id_login"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,en;q=0.8",
        "Content-Type": "application/json",
        "Origin": "https://shop2game.com",
        "Referer": "https://shop2game.com/app",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "x-datadome-clientid": "10BIK2pOeN3Cw42~iX48rEAd2OmRt6MZDJQsEeK5uMirIKyTLO2bV5Ku6~7pJl_3QOmDkJoSzDcAdCAC8J5WRG_fpqrU7crOEq0~_5oqbgJIuVFWkbuUPD~lUpzSweEa",
    }
    payload = {
        "app_id": 100067,
        "login_id": f"{Id}",
        "app_server_id": 0,
    }
    response = requests.post(url, headers=headers, json=payload)
    try:
        if response.status_code == 200:
            return response.json()['nickname']
        else:
            return("ERROR")
    except:
        return("Name unknown??")
####################################
def gen_squad(clisocks, packet: str):
        header = packet[0:62]
        lastpacket = packet[64:]
        squadcount = "04"
        NewSquadData = header + squadcount + lastpacket
        clisocks.send(bytes.fromhex(NewSquadData))
        
def gen_msg4(packet, content):
        content = content.encode("utf-8")
        content = content.hex()
        header = packet[0:8]
        packetLength = packet[8:10]
        packetBody = packet[10:32]
        pyloadbodyLength = packet[32:34]
        pyloadbody2 = packet[34:62]
        pyloadlength = packet[62:64]
        pyloadtext= re.findall(r"{}(.*?)28".format(pyloadlength) , packet[50:])[0]
        pyloadTile = packet[int(int(len(pyloadtext))+64):]
        NewTextLength = (hex((int(f"0x{pyloadlength}", 16) - int(len(pyloadtext)//2) ) + int(len(content)//2))[2:])
        if len(NewTextLength) == 1:
                NewTextLength = "0"+str(NewTextLength)
        NewpaketLength = hex(((int(f"0x{packetLength}", 16) - int((len(pyloadtext))//2) ) ) + int(len(content)//2) )[2:]
        NewPyloadLength = hex(((int(f"0x{pyloadbodyLength}", 16) - int(len(pyloadtext)//2)))+ int(len(content)//2) )[2:]
        NewMsgPacket = header + NewpaketLength + packetBody + NewPyloadLength + pyloadbody2 + NewTextLength + content + pyloadTile
        return str(NewMsgPacket)
        
def gen_msgv3(packet , replay):
        replay = replay.encode('utf-8')
        replay = replay.hex()
        hedar = packet[0:8]
        packetLength = packet[8:10]
        paketBody = packet[10:32]
        pyloadbodyLength = packet[32:34]
        pyloadbody2= packet[34:60]
        pyloadlength = packet[60:62]
        pyloadtext= re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
        pyloadTile = packet[int(int(len(pyloadtext))+62):]
        NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
        if len(NewTextLength) == 1:
                NewTextLength = "0"+str(NewTextLength)
        NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
        NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)))+ int(len(replay)//2) )[2:]
        finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile
        return str(finallyPacket)    
          
def Clan(replay,packet):
    replay  = replay.encode('utf-8')
    replay = replay.hex()
    hedar = packet[0:8]
    packetLength = packet[8:10] #
    paketBody = packet[10:32]
    pyloadbodyLength = packet[32:34]#
    pyloadbody2= packet[34:64]
    if "googleusercontent" in str(bytes.fromhex(packet)):
        pyloadlength = packet[64:68]#
        pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
        pyloadTile = packet[int(int(len(pyloadtext))+68):]
    elif "https" in str(bytes.fromhex(packet)) and "googleusercontent" not in str(bytes.fromhex(packet)):
        pyloadlength = packet[64:68]#
        pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
        pyloadTile = packet[int(int(len(pyloadtext))+68):]
    else:
        pyloadlength = packet[64:66]#
        pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
        pyloadTile = packet[int(int(len(pyloadtext))+66):]
    NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
    if len(NewTextLength) ==1:
        NewTextLength = "0"+str(NewTextLength)
    NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int(len(pyloadtext)//2) ) - int(len(pyloadlength))) + int(len(replay)//2) + int(len(NewTextLength)))[2:]
    NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)) -int(len(pyloadlength)) )+ int(len(replay)//2) + int(len(NewTextLength)))[2:]
    finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile
    return finallyPacket

def send_msg_friends(replay, packet):
	replay  = replay.encode('utf-8')
	replay = replay.hex()
	hd = packet[0:8]
	packetLength = packet[8:10]
	paketBody = packet[10:32]
	pyloadbodyLength = packet[32:34]
	pyloadbody2 = packet[34:60]
	pyloadlength = packet[60:62]
	pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
	Tipy = packet[int(int(len(pyloadtext))+62):]
	NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
	if len(NewTextLength) ==1:
		NewTextLength = "0"+str(NewTextLength)
	Nepalh = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
	Nepylh = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2))  )+ int(len(replay)//2) )[2:]
	st_pack = hd + Nepalh + paketBody + Nepylh + pyloadbody2 + NewTextLength + replay + Tipy
	return st_pack

def send_msg_clan(replay, packet):
	replay  = replay.encode('utf-8')
	replay = replay.hex()
	hd = packet[0:8]
	packetLength = packet[8:10] #
	paketBody = packet[10:32]
	pyloadbodyLength = packet[32:34]#
	pyloadbody2 = packet[34:64]
	if "googleusercontent" in str(bytes.fromhex(packet)):
		pyloadlength = packet[64:68]#
		pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
		Tipy = packet[int(int(len(pyloadtext))+68):]
	elif "https" in str(bytes.fromhex(packet)) and "googleusercontent" not in str(bytes.fromhex(packet)):
		pyloadlength = packet[64:68]#
		pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
		Tipy = packet[int(int(len(pyloadtext))+68):]
		print(bytes.fromhex(pyloadlength))
	else:
		pyloadlength = packet[64:66]#
		pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
		Tipy = packet[int(int(len(pyloadtext))+66):]
	NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
	if len(NewTextLength) ==1:
		NewTextLength = "0"+str(NewTextLength)
	NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int(len(pyloadtext)//2) ) - int(len(pyloadlength))) + int(len(replay)//2) + int(len(NewTextLength)))[2:]
	NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)) -int(len(pyloadlength)) )+ int(len(replay)//2) + int(len(NewTextLength)))[2:]
	st_pack = hd + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + Tipy
	return st_pack

def gen_msg(packet, content):
	content = content.encode("utf-8")
	content = content.hex()	
	header = packet[0:8]
	packetLength = packet[8:10]
	packetBody = packet[10:32]
	pyloadbodyLength = packet[32:34]
	pyloadbody2 = packet[34:62]
	pyloadlength = packet[62:64]	
	pyloadtext= re.findall(r"{}(.*?)28".format(pyloadlength) , packet[50:])[0]
	pyloadTile = packet[int(int(len(pyloadtext))+64):]	
	NewTextLength = (hex((int(f"0x{pyloadlength}", 16) - int(len(pyloadtext)//2) ) + int(len(content)//2))[2:])
	if len(NewTextLength) == 1:
		NewTextLength = "0"+str(NewTextLength)	
	NewpaketLength = hex(((int(f"0x{packetLength}", 16) - int((len(pyloadtext))//2) ) ) + int(len(content)//2) )[2:]
	NewPyloadLength = hex(((int(f"0x{pyloadbodyLength}", 16) - int(len(pyloadtext)//2)))+ int(len(content)//2) )[2:]
	NewMsgPacket = header + NewpaketLength + packetBody + NewPyloadLength + pyloadbody2 + NewTextLength + content + pyloadTile
	return str(NewMsgPacket)	
def gen_msgv2(packet , replay):
	replay = replay.encode('utf-8')
	replay = replay.hex()		
	hedar = packet[0:8]
	packetLength = packet[8:10] #
	paketBody = packet[10:32]
	pyloadbodyLength = packet[32:34]
	pyloadbody2= packet[34:60]	
	pyloadlength = packet[60:62]
	pyloadtext= re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
	pyloadTile = packet[int(int(len(pyloadtext))+62):]	
	NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
	if len(NewTextLength) == 1:
		NewTextLength = "0"+str(NewTextLength)
	NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
	NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)))+ int(len(replay)//2) )[2:]	
	finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile	
	return str(finallyPacket)	
def send_msg(sock, packet, content, delay:int):
	time.sleep(delay)
	try:
		sock.send(bytes.fromhex(gen_msg(packet, content)))
		sock.send(bytes.fromhex(gen_msgv2(packet, content)))
	except Exception as e:
		print(e)
		pass
def adjust_text_length(text, target_length=22, fill_char="20"):
    if len(text) > target_length:
        return text[:target_length]
    elif len(text) < target_length:
        fill_length = target_length - len(text)
        return text + (fill_char * (fill_length // len(fill_char)))[:fill_length]
    else:
        return text
def adjust_text_length(text, target_length=22, fill_char="20"):
    if len(text) > target_length:
        return text[:target_length]
    elif len(text) < target_length:
        fill_length = target_length - len(text)
        return text + (fill_char * (fill_length // len(fill_char)))[:fill_length]
    else:
        return text

def send_msg(sock, packet, content, delay:int):
	time.sleep(delay)
	try:
		sock.send(bytes.fromhex(gen_msg(packet, content)))
		sock.send(bytes.fromhex(gen_msgv2(packet, content)))
	except Exception as e:
		print(e)
		pass	
#################################

yout1 = b"\x06\x00\x00\x00{\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*o\x08\x81\x80\x83\xb6\x01\x1a)[18ffff]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf\xe3\x85\xa4\xd8\xa7\xd9\x84\xd8\xa8\xd9\x87\xd8\xa7\xd8\xa6\xd9\x85[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xdc)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\tAO'-'TEAM\xf0\x01\x01\xf8\x01\xdc\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02F"
yout2 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xd6\xd1\xb9(\x1a![18ffff]\xef\xbc\xa8\xef\xbc\xac\xe3\x85\xa4Hassone.[18ffff]2\x02ME@G\xb0\x01\x13\xb8\x01\xcf\x1e\xd8\x01\xcc\xd6\xd0\xad\x03\xe0\x01\xed\xdc\x8d\xae\x03\xea\x01\x1d\xef\xbc\xb4\xef\xbc\xa8\xef\xbc\xa5\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xac\xef\xbc\xac\xe0\xbf\x90\xc2\xb9\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout3 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xe9\xa7\xe9\x1b\x1a [18ffff]DS\xe3\x85\xa4WAJIHANO\xe3\x85\xa4[18ffff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xca2\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x10.DICTATORS\xe3\x85\xa4\xe2\x88\x9a\xf0\x01\x01\xf8\x01\xc4\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
yout4 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*n\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[18ffff]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[18ffff]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout5 = b"\x06\x00\x00\x00\x84\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*x\x08\xb6\xc0\xf1\xcc\x01\x1a'[18ffff]\xd9\x85\xd9\x84\xd9\x83\xd8\xa9*\xd9\x84\xd9\x85\xd8\xb9\xd9\x88\xd9\x82\xd9\x8a\xd9\x86[18ffff]2\x02ME@G\xb0\x01\x05\xb8\x01\x82\x0b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x15\xe9\xbf\x84\xef\xbc\xac\xef\xbc\xaf\xef\xbc\xb2\xef\xbc\xa4\xef\xbc\xb3\xe9\xbf\x84\xf0\x01\x01\xf8\x01>\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x05\xd8\x02\x0e"
yout6 = b'\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xeb\x98\x88\x8e\x01\x1a"[18ffff]OP\xe3\x85\xa4BNL\xe3\x85\xa4\xe2\x9a\xa1\xe3\x85\xa4*[18ffff]2\x02ME@R\xb0\x01\x10\xb8\x01\xce\x16\xd8\x01\x84\xf0\xd2\xad\x03\xe0\x01\xa8\xdb\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x8f\xe1\xb4\xa0\xe1\xb4\x87\xca\x80\xe3\x85\xa4\xe1\xb4\x98\xe1\xb4\x8f\xe1\xb4\xa1\xe1\xb4\x87\xca\x80\xe2\x9a\xa1\xf0\x01\x01\xf8\x01A\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01\xe0\x02\xf3\x94\xf6\xb1\x03'
yout7 = b"\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xb0\xa4\xdb\x80\x01\x1a'[18ffff]\xd9\x85\xd9\x83\xd8\xa7\xd9\x81\xd8\xad\xd8\xa9.\xe2\x84\x93\xca\x99\xe3\x80\xb5..[18ffff]2\x02ME@T\xb0\x01\x13\xb8\x01\xfc$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x1d\xef\xbc\xad\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa1\xe3\x85\xa4\xe2\x8e\xb0\xe2\x84\x93\xca\x99\xe2\x8e\xb1\xf0\x01\x01\xf8\x01\xdb\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0f\xd8\x02>"
yout8 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xfd\x8a\xde\xb4\x02\x1a\x1f[18ffff]ITZ\xe4\xb8\xb6MOHA\xe3\x85\xa42M[18ffff]2\x02ME@C\xb0\x01\n\xb8\x01\xdf\x0f\xd8\x01\xac\xd8\xd0\xad\x03\xe0\x01\xf2\xdc\x8d\xae\x03\xea\x01\x15\xe3\x80\x9dITZ\xe3\x80\x9e\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf8\x01\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x026'
yout9 = b'\x06\x00\x00\x00w\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*k\x08\xc6\x99\xddp\x1a\x1b[18ffff]HEROSHIIMA1[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xb2\xef\xbc\xaf\xef\xbc\xb3\xef\xbc\xa8\xef\xbc\xa9\xef\xbc\xad\xef\xbc\xa1\xef\xa3\xbf\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout10 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[18ffff]SH\xe3\x85\xa4SHIMA|M[18ffff]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
yout11 = b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[18ffff]2JZ\xe3\x85\xa4POWER[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
yout12 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[18ffff]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
yout14 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[18ffff]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
yout15 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\x90\xf6\x87\x15\x1a"[18ffff]V4\xe3\x85\xa4RIO\xe3\x85\xa46%\xe3\x85\xa4zt[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\x95&\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x0e\xe1\xb4\xa0\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x8f\xd1\x95\xf0\x01\x01\xf8\x01\xe2\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02^\xe0\x02\x85\xff\xf5\xb1\x03'
yout16 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[18ffff]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
yout17 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[18ffff]SVG.NINJA\xe2\xbc\xbd[18ffff]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
yout18 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
yout19 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[18ffff]FARAMAWY_1M.[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout20 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[18ffff]SH\xe3\x85\xa4SHIMA|M[18ffff]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
yout21= b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[18ffff]2JZ\xe3\x85\xa4POWER[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
yout22 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[18ffff]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
yout23 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[18ffff]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
yout24 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[18ffff]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
yout25 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[18ffff]SVG.NINJA\xe2\xbc\xbd[18ffff]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
yout26 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
yout27 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[18ffff]FARAMAWY_1M.[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout28 = b"\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xaa\xdd\xf1'\x1a\x1d[18ffff]BM\xe3\x85\xa4ABDOU_YT[18ffff]2\x02ME@G\xb0\x01\x13\xb8\x01\xd4$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1d\xe2\x80\xa2\xc9\xae\xe1\xb4\x87\xca\x9f\xca\x9f\xe1\xb4\x80\xca\x8d\xe1\xb4\x80\xd2\x93\xc9\xaa\xe1\xb4\x80\xc2\xb0\xf0\x01\x01\xf8\x01\x8e\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x07\xd8\x02\x16"
yout29 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9a\xd6\xdcL\x1a-[18ffff]\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa4\xef\xbc\xa9[18ffff]2\x02ME@H\xb0\x01\x01\xb8\x01\xe8\x07\xea\x01\x15\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xc9\xb4\xef\xbd\x93\xe1\xb4\x9b\xe1\xb4\x87\xca\x80\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout30 = b'\x06\x00\x00\x00v\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*j\x08\xb6\x92\xa9\xc8\x01\x1a [18ffff]\xef\xbc\xaa\xef\xbc\xad\xef\xbc\xb2\xe3\x85\xa4200K[18ffff]2\x02ME@R\xb0\x01\x13\xb8\x01\xc3(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\n3KASH-TEAM\xf8\x012\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x06\xd8\x02\x13\xe0\x02\x89\xa0\xf8\xb1\x03'
yout31 = b"\x06\x00\x00\x00\x92\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x85\x01\x08\xa2\xd3\xf4\x81\x07\x1a'[18ffff]\xd8\xb3\xd9\x80\xd9\x86\xd9\x80\xd8\xaf\xd8\xb1\xd9\x8a\xd9\x84\xd8\xa71M\xe3\x85\xa4[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xc1 \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xad\xef\xbc\xa6\xef\xbc\x95\xef\xbc\xb2\xef\xbc\xa8\xe3\x85\xa4\xe1\xb4\xa0\xc9\xaa\xe1\xb4\x98\xf0\x01\x01\xf8\x01\x8c\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x024\xe0\x02\x87\xff\xf5\xb1\x03"
yout32 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xe0\xe1\xdeu\x1a\x1a[18ffff]P1\xe3\x85\xa4Fahad[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xd0&\xd8\x01\xea\xd6\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xe3\x85\xa4\xef\xbc\xb0\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xa5\xef\xbc\xae\xef\xbc\xa9\xef\xbc\xb8\xc2\xb9\xf0\x01\x01\xf8\x01\x9e\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02*'
yout33 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xc5\xcf\x94\x8b\x02\x1a\x18[18ffff]@EL9YSAR[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\x86+\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\x89\xae\x8f\xae\x03\xea\x01\x1d-\xc9\xaa\xe1\xb4\x8d\xe1\xb4\x8d\xe1\xb4\x8f\xca\x80\xe1\xb4\x9b\xe1\xb4\x80\xca\x9fs\xe2\xac\x86\xef\xb8\x8f\xf8\x01j\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xe2\x02\xe0\x02\x9f\xf1\xf7\xb1\x03'
yout34 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xa9\x81\xe6^\x1a\x1e[18ffff]STRONG\xe3\x85\xa4CRONA[18ffff]2\x02ME@J\xb0\x01\x13\xb8\x01\xd8$\xd8\x01\xd8\xd6\xd0\xad\x03\xe0\x01\x92\xdb\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xbc\x01'
yout35 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xeb\x8d\x97\xec\x01\x1a&[18ffff]\xd8\xb9\xd9\x80\xd9\x85\xd9\x80\xd8\xaf\xd9\x86\xd9\x8a\xd9\x80\xd8\xaa\xd9\x80\xd9\x88[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xd3\x1a\xd8\x01\xaf\xd7\xd0\xad\x03\xe0\x01\xf4\xdc\x8d\xae\x03\xea\x01\rOSIRIS\xe3\x85\xa4MASR\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02\\\xe0\x02\xf4\x94\xf6\xb1\x03'
yout36 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xb4\xff\xa3\xef\x01\x1a\x1c[18ffff]ZAIN_YT_500K[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xa3#\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\xbb\xdb\x8d\xae\x03\xea\x01\x1b\xe1\xb6\xbb\xe1\xb5\x83\xe1\xb6\xa4\xe1\xb6\xb0\xe3\x85\xa4\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\\\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02('
yout37 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\x86\xa7\x9e\xa7\x0b\x1a([18ffff]\xe2\x80\x94\xcd\x9e\xcd\x9f\xcd\x9e\xe2\x98\x85\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8[18ffff]2\x02ME@d\xb0\x01\x13\xb8\x01\xe3\x1c\xe0\x01\xf2\x83\x90\xae\x03\xea\x01!\xe3\x85\xa4\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf8\x01u\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Y\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout38 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xc3\xcf\xe5H\x1a([18ffff]\xe3\x85\xa4BEE\xe2\x9c\xbfSTO\xe3\x85\xa4\xe1\xb5\x80\xe1\xb4\xb5\xe1\xb4\xb7[18ffff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xffP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x15TIK\xe2\x9c\xbfTOK\xe1\xb5\x80\xe1\xb4\xb1\xe1\xb4\xac\xe1\xb4\xb9\xf0\x01\x01\xf8\x01\xc8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02q'
yout39 = b'\x06\x00\x00\x00\x94\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x87\x01\x08\x97\xd5\x9a.\x1a%[18ffff]\xd8\xb9\xd9\x86\xd9\x83\xd9\x88\xd8\xb4\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe3\x85\xa4[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\xe8(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe1\xb4\x9c\xea\x9c\xb1\xca\x9c\xe3\x85\xa4\xe1\xb4\x9b\xe1\xb4\x87\xe1\xb4\x80\xe1\xb4\x8d\xf0\x01\x01\xf8\x01\xb6\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02"\xe0\x02\xf2\x94\xf6\xb1\x03'
yout40 = b'\x06\x00\x00\x00\x8a\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*~\x08\xf7\xdf\xda\\\x1a/[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xad\xef\xbc\xb3\xef\xbc\xa9_\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\xb9*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\x8e\x0e\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02S\xe0\x02\xc3\xb7\xf8\xb1\x03'
yout41 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xb5\xdd\xec\x8e\x01\x1a%[18ffff]\xd8\xa7\xd9\x88\xd9\x81\xe3\x80\x80\xd9\x85\xd9\x86\xd9\x83\xe3\x85\xa4\xe2\x9c\x93[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xdd#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x18\xef\xbc\xaf\xef\xbc\xa6\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf0\x01\x01\xf8\x01\xe8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Q'
yout42 = b'\x06\x00\x00\x00\x8b\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x7f\x08\x81\xf4\xba\xf8\x01\x1a%[18ffff]\xef\xbc\xa7\xef\xbc\xa2\xe3\x85\xa4\xef\xbc\xae\xef\xbc\xaf\xef\xbc\x91\xe3\x81\x95[18ffff]2\x02ME@N\xb0\x01\x0c\xb8\x01\xbd\x11\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xa7\xef\xbc\xb2\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xb4__\xef\xbc\xa2\xef\xbc\xaf\xef\xbc\xb9\xf8\x018\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02-\xe0\x02\x85\xff\xf5\xb1\x03'
yout43 = b'\x06\x00\x00\x00o\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*c\x08\xfb\x9d\xb9\xae\x06\x1a\x1c[18ffff]BT\xe3\x85\xa4BadroTV[18ffff]2\x02ME@@\xb0\x01\x13\xb8\x01\xe7\x1c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x91\xdb\x8d\xae\x03\xea\x01\nBadro_TV_F\xf0\x01\x01\xf8\x01\x91\x1a\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02!'
yout44 = b"\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xc4\xe5\xe1>\x1a'[18ffff]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf~\xd8\xa7\xd9\x84\xd8\xba\xd9\x86\xd8\xa7\xd8\xa6\xd9\x85[18ffff]2\x02ME@J\xb0\x01\x14\xb8\x01\xceP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x03Z7F\xf0\x01\x01\xf8\x01\xd0\x19\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\x9c\x01"
yout45 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xfd\xa4\xa6i\x1a$[18ffff]\xd8\xb2\xd9\x8a\xd9\x80\xd8\xb1\xc9\xb4\xcc\xb67\xcc\xb6\xca\x80\xe3\x85\xa4[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xe1(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x19\xc2\xb7\xe3\x85\xa4\xe3\x85\xa4N\xe3\x85\xa47\xe3\x85\xa4R\xe3\x85\xa4\xe3\x85\xa4\xc2\xb7\xf0\x01\x01\xf8\x01\x8f\t\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02k'
yout46 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xcc\xb9\xcc\xd4\x06\x1a"[18ffff]\xd8\xa8\xd9\x88\xd8\xad\xd8\xa7\xd9\x83\xd9\x80\xd9\x80\xd9\x80\xd9\x85[18ffff]2\x02ME@9\xb0\x01\x07\xb8\x01\xca\x0c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x11*\xef\xbc\x97\xef\xbc\xaf\xef\xbc\xab\xef\xbc\xa1\xef\xbc\xad*\xf0\x01\x01\xf8\x01\xad\x05\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout47 = b'\x06\x00\x00\x00e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*Y\x08\xe8\xbd\xc9b\x1a [18ffff]\xe3\x80\x8cvip\xe3\x80\x8dDR999FF[18ffff]2\x02ME@Q\xb0\x01\x10\xb8\x01\x94\x16\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xf0\x01\x01\xf8\x01\xa0\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
yout48 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\x86\xb7\x84\xf1\x01\x1a&[18ffff]\xd8\xa2\xd9\x86\xd9\x8a\xd9\x80\xd9\x80\xd9\x84\xd8\xa7\xce\x92\xe2\x92\x91\xe3\x85\xa4[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\x82)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x13\xce\x92\xe2\x92\x91\xe3\x85\xa4MAFIA\xe3\x85\xa4\xef\xa3\xbf\xf0\x01\x01\xf8\x01\x95\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02W'
yout49 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [18ffff]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[18ffff]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
yout50 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [18ffff]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[18ffff]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
yout51 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x028c8d99a21bn\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[18ffff]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[18ffff]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout_list = [yout1,yout2,yout3,yout4,yout5,yout6,yout7,yout8,yout9,yout10,yout11,yout12,yout14,yout15,yout16,yout17,yout18,yout19,yout20,yout21,yout22,yout23,yout24,yout25,yout26,yout27,yout28,yout29,yout30,yout31,yout32,yout33,yout34,yout35,yout36,yout37,yout38,yout39,yout40,yout41,yout42,yout43,yout44,yout45,yout46,yout47,yout48,yout49,yout50,yout51]

                      
               
#################################


def GT500_msg(mess, data, clin):
    data = data[12:22]
    api_url = f"https://long-message-gt-500-karm.vercel.app/PaCKet-Msg-Gt-500?Id={data}&Msg={mess}&Key=GT-500-QF"
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        packet = response.text
        clin.send(bytes.fromhex(packet.strip('"')))
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"    
                        

#################################

                                
class Proxy:
    def __init__(self):
        self.username = "bot"
        self.password = "bot"
        self.last_check_time = 0
        self.comand = True
        self.yout_list = yout_list
        self.RbGx = False
         
              
#################################

        
    def spam__invite(self, data, remote):
        global invit_spam
        while invit_spam:
            try:
                for _ in range(5):
                    remote.send(data)
                    time.sleep(0.04)
                time.sleep(0.2)
            except:
                pass
            
                                
#################################

    def fake_friend(self, client, id: str):
        if len(id) == 8:
            packet = '060000007708d4d7faba1d100620022a6b08cec2f1051a1b5b3030464630305d2b2b202020205A495800005b3030464630305d32024d454049b00101b801e807d801d4d8d0ad03e001b2dd8dae03ea011eefbca8efbca5efbcb2efbcafefbcb3efbca8efbca9efbcadefbca1efa3bf8002fd98a8dd03900201d00201'
            packet = re.sub(r'cec2f105', id, packet)
            client.send(bytes.fromhex(packet))
        elif len(id) == 10:
            packet = '060000006f08d4d7faba1d100620022a6308fb9db9ae061a1c5b3030464630305d2b2be385a45A4958000020205b3030464630305d32024d454040b00113b801e71cd801d4d8d0ad03e00191db8dae03ea010a5a45522d49534b494e47f00101f801911a8002fd98a8dd03900201d0020ad80221'
            packet = re.sub(r'fb9db9ae06', id, packet)
            client.send(bytes.fromhex(packet))
        else:
            print(id)
            
    def Encrypt_ID(self, id):
        try:
            number = int(id)
            encoded_bytes = []
            while True:
                byte = number & 0x7F   
                number >>= 7
                if number:
                    byte |= 0x80     
                encoded_bytes.append(byte)
                if not number:
                    break

            return ''.join(f'{b:02x}' for b in encoded_bytes)

        except Exception as e:
            print("فشل التشفير:", e)
            return None
    def split_message(self, text, max_length=3704):
        """تقسيم الرسالة الطويلة إلى أجزاء"""
        parts = []
        current_part = ""
        lines = text.split('\n')
        
        for line in lines:
            if len(current_part) + len(line) + 1 <= max_length:
                if current_part:
                    current_part += '\n' + line
                else:
                    current_part = line
            else:
                if current_part:
                    parts.append(current_part)
                current_part = line
        
        if current_part:
            parts.append(current_part)
        
        final_parts = []
        for i, part in enumerate(parts, 1):
            header = f"[FFD700]الجزء {i}{len(parts)}[FFD700]\n"
            final_parts.append(header + part)
        
        return final_parts
              
    def process_packet_data(self, text, user_id):
        text = text[:3704].ljust(3704, 'ً')  #改用 ً بدلاً من المسافات
        packet_structure = (
            b'\x12\x00\x00\x0f/\x08\xce\xc2\xf1\x05\x10\x12 \x02*\xa2\x1e\x08\xce\xc2\xf1\x05\x10\xce\xc2\xf1\x05"\xfa\x1c\n'
            + text.encode('utf-8') 
            + b' \n(\xa0\x83\xca\xbd\x06J%\n\x0bOUT\xe3\x85\xa4ALVIN\x10\xe7\xb2\x90\xae\x03 \xd2\x01(\xc1\xb7\xf8\xb1\x03B\x077Radaa!R\x02arjd\n^https://lh3.googleusercontent.com/a/ACg8ocJaMCcUolCU9qHWll-yPnvQm3Tx-0F00M0Yjc3PCw72ozDP=s96-c\x10\x01\x18\x01r\x00'
        )
        hex_data = packet_structure.hex().upper()    
        modified_hex = hex_data.replace('CEC2F105', user_id.upper())    
    
        if len(modified_hex) > 7784:
            extra = len(modified_hex) - 7784
            mid_point = len(modified_hex) // 2
            start = mid_point - (extra // 2)
            end = mid_point + (extra // 2)
            if extra % 2 != 0:
                end += 1
            modified_hex = modified_hex[:start] + modified_hex[end:]
        elif len(modified_hex) < 7784:
            modified_hex = modified_hex.ljust(7784, '0')  # هنا لازم تبقى 0 لأنها هيكس
    
        return modified_hex[:7784]
        

    def gen_zixhelp(self, id, message_text):
        try:
            encrypted_packet = self.process_packet_data(message_text, id)
            encrypted_packet = encrypted_packet.replace("{id}", id)
            if self.sock1200:
                self.sock1200.send(bytes.fromhex(encrypted_packet))
                print(f"[✓] تم إرسال الرسالة المشفرة إلى {id}")
            else:
                print("[!] sock1200 غير متصل")
        except Exception as e:
            print(f"[!] خطأ في التشفير أو الإرسال: {e}")

#################################

    def fetch_player_info(self, uid):
        """جلب معلومات اللاعب من API"""
        try:
            url = f"https://fffinfo.tsunstudio.pw/get?uid={uid}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                error_msg = f"⚠️ خطأ من API: {response.status_code}"
                print(error_msg)
                return {"error": error_msg}
        except Exception as e:
            error_msg = f"⚠️ فشل الاتصال: {e}"
            print(error_msg)
            return {"error": error_msg}

    def format_info_message(self, data):
        """تحويل JSON إلى نص بدون إيموجي"""
        if "error" in data:
            return data["error"]
        
        try:
            message = "[c][b][FFD700]════════════════════════════════════════[FFD700]\n"
            message += "[00FF00]● معلومات الحساب ●[00FF00]\n"
            message += "[FFD700]════════════════════════════════════════[FFD700]\n\n"
            
            # معلومات الحساب الأساسية
            acc = data.get('AccountInfo', {})
            message += f"الاسم: {acc.get('AccountName', 'غير معروف')}\n"
            message += f"المنطقة: {acc.get('AccountRegion', 'غير معروف')}\n"
            message += f"المستوى: {acc.get('AccountLevel', 'غير معروف')}\n"
            message += f"النقاط: {acc.get('AccountEXP', 'غير معروف')}\n"
            message += f"الإعجابات: {acc.get('AccountLikes', 'غير معروف')}\n"
            message += f"تاريخ الإنشاء: {acc.get('AccountCreateTime', 'غير معروف')}\n"
            message += f"آخر دخول: {acc.get('AccountLastLogin', 'غير معروف')}\n"
            message += f"الموسم: {acc.get('AccountSeasonId', 'غير معروف')}\n\n"
            
            # الرتب
            profile = data.get('AccountProfileInfo', {})
            message += "[FFA500]────────────────────────────────[FFA500]\n"
            message += "[FFA500]● الرتب ●[FFA500]\n"
            message += "[FFA500]────────────────────────────────[FFA500]\n\n"
            
            if profile.get('ShowBrRank'):
                message += f"رتبة BR: {profile.get('BrMaxRank', 'غير معروف')} (نقاط: {profile.get('BrRankPoint', 'غير معروف')})\n"
            if profile.get('ShowCsRank'):
                message += f"رتبة CS: {profile.get('CsMaxRank', 'غير معروف')} (نقاط: {profile.get('CsRankPoint', 'غير معروف')})\n"
            message += f"اللقب: {profile.get('Title', 'غير معروف')}\n\n"
            
            # الطاقم
            guild = data.get('GuildInfo', {})
            if guild and guild.get('GuildName'):
                message += "[FF69B4]────────────────────────────────[FF69B4]\n"
                message += "[FF69B4]● الطاقم ●[FF69B4]\n"
                message += "[FF69B4]────────────────────────────────[FF69B4]\n\n"
                
                message += f"اسم الطاقم: {guild.get('GuildName', 'لا يوجد')}\n"
                message += f"الأعضاء: {guild.get('GuildMember', 0)}/{guild.get('GuildCapacity', 0)}\n"
                message += f"مستوى الطاقم: {guild.get('GuildLevel', 'غير معروف')}\n"
                
                owner = data.get('GuildOwnerInfo', {})
                message += f"مالك الطاقم: {owner.get('nickname', 'غير معروف')}\n"
                message += f"آخر ظهور للمالك: {owner.get('lastLoginAt', 'غير معروف')}\n\n"
            
            # التجهيزات
            equipped = data.get('EquippedItemsInfo', {})
            message += "[FF6347]────────────────────────────────[FF6347]\n"
            message += "[FF6347]● التجهيزات ●[FF6347]\n"
            message += "[FF6347]────────────────────────────────[FF6347]\n\n"
            
            weapons = equipped.get('EquippedWeapon', [])
            if weapons:
                message += f"السلاح 1: {weapons[0] if len(weapons) > 0 else 'لا يوجد'}\n"
                message += f"السلاح 2: {weapons[1] if len(weapons) > 1 else 'لا يوجد'}\n"
            
            outfit = equipped.get('EquippedOutfit', [])
            if outfit:
                message += f"اللباس: {', '.join(map(str, outfit[:3]))}\n"
            
            message += f"الافاتار: {equipped.get('EquippedAvatarId', 'غير معروف')}\n"
            message += f"الراية: {equipped.get('EquippedBannerId', 'غير معروف')}\n"
            message += f"الشارة: {equipped.get('EquippedBPBadges', 'غير معروف')}\n\n"
            
            # البت والمهارات
            pet = data.get('PetInfo', {})
            if pet and pet.get('id'):
                message += "[98FB98]────────────────────────────────[98FB98]\n"
                message += "[98FB98]● البت ●[98FB98]\n"
                message += "[98FB98]────────────────────────────────[98FB98]\n\n"
                
                message += f"معرف البت: {pet.get('id', 'غير معروف')}\n"
                message += f"مستوى البت: {pet.get('level', 'غير معروف')}\n"
                message += f"نقاط البت: {pet.get('exp', 'غير معروف')}\n"
                message += f"المهارة: {pet.get('selectedSkillId', 'غير معروف')}\n\n"
            
            # نقاط الثقة
            credit = data.get('CreditScoreInfo', {})
            if credit:
                message += f"نقاط الثقة: {credit.get('creditScore', 'غير معروف')}\n\n"
            
            # التوقيع
            social = data.get('SocialInfo', {})
            if social.get('signature'):
                signature = social.get('signature', '').replace('[b][c]', '').replace('[b][c]', '')
                message += f"التوقيع: {signature}\n"
            
            message += "\n[FFD700]════════════════════════════════════════[FFD700]"
            
            return message
            
        except Exception as e:
            print(f"خطأ في التنسيق: {e}")
            return f"⚠️ حدث خطأ: {e}"


    def send_chat_message(self, data, message):
        try:
            msg_packet = gen_msgv2(data.hex(), message)
            if self.sock1200:
                self.sock1200.send(bytes.fromhex(msg_packet))
        except Exception as e:
            print(f"[!] Error sending chat message: {e}")

            
    def tens_command(self, data):
        try:
            print("[DENS] ==================================")
            print("[DENS] Command received!") 
            try:
                data_text = data.decode('utf-8', errors='ignore')
                print(f"[DENS] Decoded text: {data_text[:200]}")
            except:
                data_text = str(data)
                print(f"[DENS] Raw string: {data_text[:200]}")
            
            
            if '@dens' in data_text:
                print("[DENS] @dens found in data")
                                
                import re
                match = re.search(r'@dens\s+(\d+(?:\s+\d+)*)', data_text)
                
                if match:
                    command_part = match.group(1)
                    print(f"[DENS] Command part: {command_part}")
                    
                    numbers = command_part.strip().split()
                    print(f"[DENS] Split numbers: {numbers}")
                    
                    clean_numbers = []
                    for num in numbers:
                        
                        clean_num = re.sub(r'[^0-9]', '', num)
                        if clean_num: 
                            clean_numbers.append(clean_num)
                    
                    print(f"[DENS] Clean numbers: {clean_numbers}")
                    
                    if len(clean_numbers) >= 4:
                        
                        team_code = clean_numbers[0]
                        
                        repeat_count = int(clean_numbers[-1])
                        
                        emote_number = clean_numbers[-2]
                        
         
                        uid_count = min(4, len(clean_numbers) - 3)
                        uids = clean_numbers[1:1+uid_count]
                        
                        if emote_number in uids:
                            uids.remove(emote_number)
                        if str(repeat_count) in uids:
                            uids.remove(str(repeat_count))
                        
                        emote_id = self.get_evo_id(emote_number)
                        
                        player_id = data.hex()[12:22]
                        
                        print(f"[DENS] Team Code: {team_code}")
                        print(f"[DENS] UIDs: {uids}")
                        print(f"[DENS] Emote Number: {emote_number} -> ID: {emote_id}")
                        print(f"[DENS] Repeat Count: {repeat_count}")
                        
                        if repeat_count <= 0 or repeat_count > 100:
                            print("[DENS] Invalid repeat count")
                            error_msg = "[FF0000]❌ عدد التكرارات يجب أن يكون بين 1 و 100[c]"
                            self.send_chat_message(data, error_msg)
                            return
                        
                        if len(uids) == 0:
                            print("[DENS] No UIDs provided")
                            error_msg = "[FF0000]❌ يجب إدخال على الأقل UID واحد[c]"
                            self.send_chat_message(data, error_msg)
                            return
                        
                        if int(emote_number) < 1 or int(emote_number) > 50:
                            print("[DENS] Invalid emote number")
                            error_msg = "[FF0000]❌ رقم الرقصة يجب أن يكون بين 1 و 50[c]"
                            self.send_chat_message(data, error_msg)
                            return
                        
                        print("[DENS] Starting thread for sending requests")
                        threading.Thread(target=self.send_denn_requests, args=(
                            team_code, 
                            uids, 
                            emote_id, 
                            emote_number,
                            repeat_count, 
                            player_id, 
                            data
                        )).start()
                        
                        uid_list_str = ', '.join(uids)
                        confirm_msg = f"[00FF00]✓ تم بدء إرسال {repeat_count} رقصة رقم {emote_number} للأيدي: {uid_list_str}[c]"
                        self.send_chat_message(data, confirm_msg)
                        print(f"[DENS] Confirmation message sent")
                        
                    else:
                        print(f"[DENS] Insufficient numbers: {len(clean_numbers)}")
                        error_msg = "[FF0000]❌ التنسيق الصحيح: @dens [كود الفريق] [UID1] [UID2] [UID3] [UID4] [رقم الرقصة] [عدد التكرارات][c]\n"
                        error_msg += "[FF0000]📌 مثال: @dens 5286170 14727683166 6 10[c]"
                        self.send_chat_message(data, error_msg)
                else:
                    print("[DENS] Could not extract command part")
                    error_msg = "[FF0000]❌ التنسيق غير صحيح. استخدم: @dens [كود الفريق] [UID] [رقم الرقصة] [عدد التكرارات][c]"
                    self.send_chat_message(data, error_msg)
            else:
                print("[DENS] @dens not found in data")
                    
        except Exception as e:
            print(f"[DENS] Error in dens_command: {e}")
            import traceback
            traceback.print_exc()
            error_msg = f"[FF0000]❌ حدث خطأ: {str(e)[:50]}[c]"
            self.send_chat_message(data, error_msg)
            
    def send_denn_requests(self, team_code, uids, emote_id, emote_number, repeat_count, requester_id, original_data):
        try:
            print("[DENS] ==================================")
            print("[DENS] Starting to send requests to API")
       
            uid_list = ['', '', '', '']
            for i in range(min(len(uids), 4)):
                uid_list[i] = uids[i]
            
            uid1, uid2, uid3, uid4 = uid_list
            
            print(f"[DENS] Prepared UIDs - UID1: '{uid1}', UID2: '{uid2}', UID3: '{uid3}', UID4: '{uid4}'")
            print(f"[DENS] Emote ID: {emote_id}, Team Code: {team_code}, Repeat: {repeat_count}")
            
            success_count = 0
            fail_count = 0
            
            for i in range(repeat_count):
                try:
                    api_url = f"http://217.160.125.125:13699/join?tc={team_code}&uid1={uid}&uid2={uid2}&uid3={uid3}&uid4={uid4}&emote_id={emote_id}"
                    
                    print(f"[DENS] Request {i+1}/{repeat_count}: Sending to {api_url}")
                    
                    response = requests.get(api_url, timeout=10)
                    
                    print(f"[DENS] Request {i+1} Response Status: {response.status_code}")
                    
                    if response.status_code == 200:
                        success_count += 1
                        try:
                            response_text = response.text
                            print(f"[DENS] Request {i+1} Response Text: {response_text[:100]}")
                        except:
                            pass
                    else:
                        fail_count += 1
                        print(f"[DENS] Request {i+1} Failed with status {response.status_code}")
                    
                    if i < repeat_count - 1:
                        print(f"[DENS] Waiting 0.3 seconds before next request...")
                        time.sleep(0.3)
                    
                except requests.exceptions.Timeout:
                    fail_count += 1
                    print(f"[DENS] Request {i+1} Timeout")
                except requests.exceptions.ConnectionError:
                    fail_count += 1
                    print(f"[DENS] Request {i+1} Connection Error")
                except Exception as e:
                    fail_count += 1
                    print(f"[DENS] Request {i+1} Error: {e}")
            
            print(f"[DENS] Final Result: {success_count} Success, {fail_count} Failed")
            
            if success_count > 0:
                result_msg = f"[00FF00]✅ تم الانتهاء من {repeat_count} رقصة: [FFDD00]{success_count} نجاح[00FF00] - [FF0000]{fail_count} فشل[c]"
            else:
                result_msg = f"[FF0000]❌ فشل جميع الطلبات ({fail_count})[c]"
            
            self.send_chat_message(original_data, result_msg)
            print("[DENS] ==================================")
            
        except Exception as e:
            print(f"[DENS] Error in send_denn_requests: {e}")
            import traceback
            traceback.print_exc()
            error_msg = f"[FF0000]❌ حدث خطأ أثناء إرسال الطلبات: {str(e)[:50]}[c]"
            self.send_chat_message(original_data, error_msg)            
            

    def get_evo_id(self, emote_number):
        emote_list = {
            '1': '909000063',
            '2': '909000068',
            '3': '909000075',
            '4': '909000081',
            '5': '909000085',
            '6': '909000090',
            '7': '909000098',
            '8': '909033001',
            '9': '909035007',
            '10': '909037011',
            '11': '909038010',
            '12': '909038012',
            '13': '909039011',
            '14': '909040010',
            '15': '909041005',
            '16': '909042008',
            '17': '909045001',
            '18': '909051003'
        }
        emote_id = emote_list.get(str(emote_number), '909000063')
        print(f"[DENS] Emote {emote_number} -> ID: {emote_id}")
        return emote_id        

        
    def check_firebase_code(self, code, user_id):
        """التحقق من صحة كود التفعيل من Firebase مع ربطه بالمستخدم"""
        try:
            # رابط Firebase للأكواد
            url = f"https://zixoff-default-rtdb.firebaseio.com/codes/{code}.json"
            print(f"[FIREBASE] Checking URL: {url}")
            
            response = requests.get(url, timeout=10)
            print(f"[FIREBASE] Response status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"[FIREBASE] Data received: {data}")
                
                # التحقق من أن الكود موجود وله بنية صحيحة
                if data and isinstance(data, dict):
                    # التحقق من تاريخ انتهاء الصلاحية
                    expire = data.get('expire')
                    used_count = data.get('used_count', 0)
                    limit = data.get('limit', 0)
                    activated_users = data.get('activated_users', [])  # قائمة المستخدمين المفعلين بهذا الكود
                    
                    # التحقق من الصلاحية
                    if expire and int(datetime.now().timestamp()) > int(expire):
                        print(f"[FIREBASE] Code {code} expired")
                        return {"valid": False, "reason": "expired", "message": "❌ هذا الكود منتهي الصلاحية"}
                    
                    # التحقق مما إذا كان المستخدم قد استخدم الكود من قبل
                    if str(user_id) in activated_users:
                        print(f"[FIREBASE] User {user_id} already used this code")
                        return {"valid": True, "expire": datetime.fromtimestamp(int(expire)).strftime('%Y-%m-%d %H:%M:%S'), "already_activated": True}
                    
                    # التحقق من الحد الأقصى للمستخدمين
                    if len(activated_users) >= limit:
                        print(f"[FIREBASE] Code {code} reached maximum users limit ({limit})")
                        return {"valid": False, "reason": "max_users_reached", "message": f"❌ هذا الكود وصل للحد الأقصى من المستخدمين ({limit})"}
                    
                    # كود صالح - زيادة عدد المستخدمين
                    activated_users.append(str(user_id))
                    new_used_count = len(activated_users)
                    
                    # تحديث البيانات في Firebase
                    update_success = self.update_code_activation(code, activated_users, new_used_count)
                    
                    if update_success:
                        expire_date = datetime.fromtimestamp(int(expire)).strftime('%Y-%m-%d %H:%M:%S')
                        return {
                            "valid": True, 
                            "expire": expire_date,
                            "message": f"✅ تم تفعيل الكود بنجاح!\n📅 تاريخ الانتهاء: {expire_date}\n👥 عدد المستخدمين: {new_used_count}/{limit}"
                        }
                    else:
                        return {"valid": False, "reason": "error", "message": "❌ حدث خطأ في حفظ البيانات"}
                else:
                    print(f"[FIREBASE] Code {code} invalid structure")
                    return {"valid": False, "reason": "invalid", "message": "❌ كود غير صالح"}
            else:
                print(f"[FIREBASE] Error: {response.status_code}")
                return {"valid": False, "reason": "error", "message": "❌ حدث خطأ في الاتصال"}
        except Exception as e:
            print(f"[FIREBASE] Exception: {e}")
            return {"valid": False, "reason": "error", "message": "❌ حدث خطأ في النظام"}

    def update_code_activation(self, code, activated_users, used_count):
        """تحديث بيانات الكود بعد تفعيل مستخدم جديد"""
        try:
            # تحديث قائمة المستخدمين المفعلين
            users_url = f"https://zixoff-default-rtdb.firebaseio.com/codes/{code}/activated_users.json"
            users_response = requests.put(users_url, json=activated_users, timeout=10)
            
            # تحديث عدد المستخدمين
            count_url = f"https://zixoff-default-rtdb.firebaseio.com/codes/{code}/used_count.json"
            count_response = requests.put(count_url, json=used_count, timeout=10)
            
            if users_response.status_code == 200 and count_response.status_code == 200:
                print(f"[FIREBASE] Code {code} updated with new user. Total users: {used_count}")
                
                # حفظ المستخدم في قائمة المستخدمين المفعلين مع الكود الخاص به
                self.save_user_code_mapping(activated_users[-1], code, used_count)
                
                return True
            else:
                print(f"[FIREBASE] Error updating code: Users={users_response.status_code}, Count={count_response.status_code}")
                return False
        except Exception as e:
            print(f"[FIREBASE] Error updating code activation: {e}")
            return False

    def save_user_code_mapping(self, user_id, code, total_users):
        """حفظ علاقة المستخدم بالكود في Firebase"""
        try:
            # حفظ في مسار user_codes
            url = f"https://zixoff-default-rtdb.firebaseio.com/user_codes/{user_id}.json"
            
            # جلب بيانات الكود للحصول على تاريخ الانتهاء
            code_url = f"https://zixoff-default-rtdb.firebaseio.com/codes/{code}.json"
            code_response = requests.get(code_url, timeout=10)
            
            expire_date = "غير محدد"
            if code_response.status_code == 200:
                code_data = code_response.json()
                if code_data and 'expire' in code_data:
                    expire_date = datetime.fromtimestamp(int(code_data['expire'])).strftime('%Y-%m-%d %H:%M:%S')
            
            user_data = {
                "user_id": user_id,
                "code": code,
                "activated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "expire_date": expire_date,
                "total_users_for_this_code": total_users
            }
            
            response = requests.put(url, json=user_data, timeout=10)
            
            if response.status_code == 200:
                print(f"[FIREBASE] User {user_id} mapped to code {code}")
                return True
            else:
                print(f"[FIREBASE] Error mapping user to code: {response.status_code}")
                return False
        except Exception as e:
            print(f"[FIREBASE] Error in save_user_code_mapping: {e}")
            return False

    def save_activated_user(self, user_id, expire_date, code=None):
        """حفظ معرف المستخدم المفعل وتاريخ انتهاء الصلاحية مع الكود المستخدم"""
        try:
            # رابط Firebase للمستخدمين المفعلين
            url = f"https://zixoff-default-rtdb.firebaseio.com/activated_users/{user_id}.json"
            
            # بيانات المستخدم المفعل
            user_data = {
                "user_id": user_id,
                "expire_date": expire_date,
                "activated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "expire_timestamp": int(datetime.strptime(expire_date, '%Y-%m-%d %H:%M:%S').timestamp()) if expire_date else 0,
                "activation_code": code  # حفظ الكود المستخدم
            }
            
            # حفظ البيانات في Firebase
            response = requests.put(url, json=user_data, timeout=10)
            
            if response.status_code == 200:
                print(f"[FIREBASE] User {user_id} saved with expiry {expire_date} using code {code}")
                return True
            else:
                print(f"[FIREBASE] Error saving user: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"[FIREBASE] Error saving user to Firebase: {e}")
            return False

    def is_user_activated(self, user_id):
        """التحقق مما إذا كان المستخدم مفعلاً مسبقاً من Firebase"""
        try:
            # رابط Firebase للمستخدمين المفعلين
            url = f"https://zixoff-default-rtdb.firebaseio.com/activated_users/{user_id}.json"
            
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                user_data = response.json()
                
                # التحقق من وجود المستخدم
                if not user_data:
                    return False
                
                # التحقق من وجود تاريخ انتهاء
                expire_date = user_data.get('expire_date')
                if not expire_date:
                    return False
                
                # التحقق من انتهاء الصلاحية
                try:
                    expire_datetime = datetime.strptime(expire_date, '%Y-%m-%d %H:%M:%S')
                    if datetime.now() > expire_datetime:
                        print(f"[FIREBASE] User {user_id} has expired")
                        # حذف المستخدم المنتهي صلاحيته تلقائياً
                        self.remove_expired_user(user_id)
                        return False
                except Exception as e:
                    print(f"[FIREBASE] Error checking expiry: {e}")
                
                return True
            else:
                print(f"[FIREBASE] Error checking user: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"[FIREBASE] Error checking user in Firebase: {e}")
            return False

    def remove_expired_user(self, user_id):
        """حذف المستخدم المنتهي صلاحيته من Firebase"""
        try:
            url = f"https://zixoff-default-rtdb.firebaseio.com/activated_users/{user_id}.json"
            response = requests.delete(url, timeout=10)
            
            if response.status_code == 200:
                print(f"[FIREBASE] Expired user {user_id} removed")
                return True
        except Exception as e:
            print(f"[FIREBASE] Error removing expired user: {e}")
            return False

    def get_all_activated_users(self):
        """جلب جميع المستخدمين المفعلين من Firebase"""
        try:
            url = "https://zixoff-default-rtdb.firebaseio.com/activated_users.json"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                return response.json() or {}
            else:
                return {}
        except Exception as e:
            print(f"[FIREBASE] Error getting all users: {e}")
            return {}

    def check_expired_users(self):
        """التحقق من المستخدمين المنتهية صلاحيتهم وإزالتهم"""
        try:
            activated_users = self.get_all_activated_users()
            current_time = datetime.now()
            
            for user_id, user_data in activated_users.items():
                expire_date = user_data.get('expire_date')
                if expire_date:
                    try:
                        expire_datetime = datetime.strptime(expire_date, '%Y-%m-%d %H:%M:%S')
                        if current_time > expire_datetime:
                            self.remove_expired_user(user_id)
                            print(f"[FIREBASE] User {user_id} automatically removed (expired)")
                    except Exception as e:
                        print(f"[FIREBASE] Error processing user {user_id}: {e}")
                        
        except Exception as e:
            print(f"[FIREBASE] Error in check_expired_users: {e}")

    def start_expiry_checker(self):
        """بدء مهمة دورية للتحقق من انتهاء الصلاحيات"""
        def check_periodically():
            while True:
                try:
                    self.check_expired_users()
                    # التحقق كل ساعة
                    time.sleep(3600)
                except Exception as e:
                    print(f"[FIREBASE] Error in expiry checker: {e}")
                    time.sleep(3600)
        
        # بدء المهمة في خيط منفصل
        import threading
        thread = threading.Thread(target=check_periodically, daemon=True)
        thread.start()

    def get_code_info(self, code):
        """جلب معلومات كود معين"""
        try:
            url = f"https://zixoff-default-rtdb.firebaseio.com/codes/{code}.json"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            print(f"[FIREBASE] Error getting code info: {e}")
            return None

    def get_user_code(self, user_id):
        """جلب الكود الذي استخدمه المستخدم"""
        try:
            url = f"https://zixoff-default-rtdb.firebaseio.com/user_codes/{user_id}.json"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            print(f"[FIREBASE] Error getting user code: {e}")
            return None

    def send_not_activated_message(self, user_id):
        """إرسال رسالة عدم التفعيل"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = f"""[b][c][FF0000]════════════════════════════════════════
✗ البوت غير مفعل

الوقت: {current_time}

استخدم @help [CODE]

مثال: @help ZIX-CTX-64TE-AM95
[FF0000]════════════════════════════════════════"""
        threading.Thread(target=self.gen_zixhelp, args=(user_id, msg)).start()

    def handle_activation_command(self, user_id, code):
        """معالجة أمر التفعيل - استدعها من بوت التليجرام"""
        result = self.check_firebase_code(code, user_id)
        
        if result["valid"]:
            if result.get("already_activated"):
                # المستخدم مفعل مسبقاً بهذا الكود
                msg = "✅ حسابك مفعل بالفعل بهذا الكود!"
            else:
                # تفعيل جديد
                msg = result["message"]
                # حفظ المستخدم كمفعل
                self.save_activated_user(user_id, result["expire"], code)
        else:
            # فشل التفعيل
            msg = result["message"]
        
        return msg

    def handle_create_code_command(self, admin_id, code, limit, expire_days):
        """إنشاء كود جديد (للآدمن فقط) - استدعها من بوت التليجرام"""
        try:
            expire_timestamp = int((datetime.now() + timedelta(days=expire_days)).timestamp())
            
            code_data = {
                "expire": expire_timestamp,
                "limit": limit,
                "used_count": 0,
                "activated_users": [],
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "created_by": admin_id
            }
            
            url = f"https://zixoff-default-rtdb.firebaseio.com/codes/{code}.json"
            response = requests.put(url, json=code_data)
            
            if response.status_code == 200:
                return f"✅ تم إنشاء الكود بنجاح!\n📌 الكود: {code}\n👥 الحد الأقصى: {limit}\n📅 ينتهي بعد: {expire_days} يوم"
            else:
                return "❌ فشل في إنشاء الكود"
        except Exception as e:
            print(f"[FIREBASE] Error creating code: {e}")
            return "❌ حدث خطأ في إنشاء الكود"

    def handle_check_code_command(self, code):
        """التحقق من معلومات كود معين - استدعها من بوت التليجرام"""
        code_info = self.get_code_info(code)
        
        if code_info:
            expire_date = datetime.fromtimestamp(int(code_info['expire'])).strftime('%Y-%m-%d %H:%M:%S')
            used = code_info.get('used_count', 0)
            limit = code_info.get('limit', 0)
            activated_users = code_info.get('activated_users', [])
            
            msg = f"""📌 معلومات الكود: {code}
📅 تاريخ الانتهاء: {expire_date}
👥 المستخدمون: {used}/{limit}
👤 قائمة المستخدمين: {', '.join(activated_users) if activated_users else 'لا يوجد'}"""
            return msg
        else:
            return "❌ الكود غير موجود"

    #################################

    def spam__invite(self, data, remote):
        global invit_spam
        while invit_spam:
            try:
                for _ in range(5):
                    remote.send(data)
                    time.sleep(0.04)
                time.sleep(0.2)
            except:
                pass    
                              
    def likes_command(self, data):
        try:
            data_text = data.decode('utf-8', errors='ignore')
            
            if '@likes' in data_text:
                parts = data_text.split('@likes')[1].strip()
                import re
                uid_match = re.search(r'(\d+)', parts)
                
                if uid_match:
                    uid = uid_match.group(1)
                    player_id = data.hex()[12:22]
                    
                    print(f"[LIKES] UID: {uid}, Requester ID: {player_id}")
                    
                    threading.Thread(target=self.send_likes_request, 
                                    args=(uid, player_id, data)).start()
                    
                    confirm_msg = f"[00FF00]✓ جاري زيادة الإعجابات لليوزر {uid}...[c]"
                    self.send_chat_message(data, confirm_msg)
                    
                else:
                    error_msg = "[FF0000]❌ الرجاء إدخال UID صحيح. مثال: @likes 1234567890[c]"
                    self.send_chat_message(data, error_msg)
                    
        except Exception as e:
            print(f"[!] Error in likes_command: {e}")
            error_msg = f"[FF0000]❌ حدث خطأ: {str(e)[:50]}[c]"
            self.send_chat_message(data, error_msg)

    def send_likes_request(self, uid, requester_id, original_data):
        try:
            api_url = f"https://s1x-team-like.vercel.app/like?uid={uid}"
            
            print(f"[LIKES] Sending request to: {api_url}")
            
            response = requests.get(api_url, timeout=15)
            
            print(f"[LIKES] Response Status: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    result = response.json()

                    if isinstance(result, dict) and "message" in result:
                        success_msg = f"[00FF00]✅ {result['message']}[c]"
                    else:
                        success_msg = f"[00FF00]✅ تمت زيادة الإعجابات لليوزر {uid} بنجاح![c]"
                except:
                    success_msg = f"[00FF00]✅ تمت زيادة الإعجابات لليوزر {uid} (كود 200)[c]"
            elif response.status_code == 401:
                success_msg = "[FF0000]❌ فشل: الـ API يحتاج إلى مصادقة (Unauthorized)[c]"
            elif response.status_code == 404:
                success_msg = "[FF0000]❌ فشل: الرابط غير صحيح (API not found)[c]"
            else:
                success_msg = f"[FF0000]❌ فشل زيادة الإعجابات. كود الخطأ: {response.status_code}[c]"
            
            self.send_chat_message(original_data, success_msg)
            
        except requests.exceptions.Timeout:
            print("[LIKES] API Timeout")
            error_msg = "[FF0000]❌ انتهت مهلة الطلب، حاول مرة أخرى[c]"
            self.send_chat_message(original_data, error_msg)
        except requests.exceptions.ConnectionError:
            print("[LIKES] Connection Error")
            error_msg = "[FF0000]❌ فشل الاتصال بالسيرفر[c]"
            self.send_chat_message(original_data, error_msg)
        except Exception as e:
            print(f"[LIKES] Error: {e}")
            error_msg = f"[FF0000]❌ حدث خطأ: {str(e)[:50]}[c]"
            self.send_chat_message(original_data, error_msg)


    def spam_command(self, data):
        try:
            data_text = data.decode('utf-8', errors='ignore')
            
            # البحث عن الأمر @likes
            if '@som' in data_text:
                # استخراج الجزء بعد الأمر
                parts = data_text.split('@som')[1].strip()
                
                # البحث عن أول رقم (الـ UID)
                import re
                uid_match = re.search(r'(\d+)', parts)
                
                if uid_match:
                    uid = uid_match.group(1)
                    player_id = data.hex()[12:22]
                    
                    print(f"[LIKES] UID: {uid}, Requester ID: {player_id}")
                    
                    # إرسال الطلب في ثريد منفصل
                    threading.Thread(target=self.send_spam_request, 
                                    args=(uid, player_id, data)).start()
                    
                    # رسالة تأكيد فورية
                    confirm_msg = f"[00FF00]✓ جاري زيادة الإعجابات لليوزر {uid}...[c]"
                    self.send_chat_message(data, confirm_msg)
                    
                else:
                    # إذا لم يجد رقم
                    error_msg = "[FF0000]❌ الرجاء إدخال UID صحيح. مثال: @som 1234567890[c]"
                    self.send_chat_message(data, error_msg)
                    
        except Exception as e:
            print(f"[!] Error in likes_command: {e}")
            error_msg = f"[FF0000]❌ حدث خطأ: {str(e)[:50]}[c]"
            self.send_chat_message(data, error_msg)

    def spam_zix(self, data):
        try:
            data_text = data.decode('utf-8', errors='ignore')
            
            # البحث عن الأمر @likes
            if '@room' in data_text:
                # استخراج الجزء بعد الأمر
                parts = data_text.split('@room')[1].strip()
                
                # البحث عن أول رقم (الـ UID)
                import re
                uid_match = re.search(r'(\d+)', parts)
                
                if uid_match:
                    uid = uid_match.group(1)
                    player_id = data.hex()[12:22]
                    
                    print(f"[LIKES] UID: {uid}, Requester ID: {player_id}")
                    
                    # إرسال الطلب في ثريد منفصل
                    threading.Thread(target=self.send_zpi, 
                                    args=(uid, player_id, data)).start()
                    
                    # رسالة تأكيد فورية
                    confirm_msg = f"[00FF00]✓ جاري زيادة الإعجابات لليوزر {uid}...[c]"
                    self.send_chat_message(data, confirm_msg)
                    
                else:
                    # إذا لم يجد رقم
                    error_msg = "[FF0000]❌ الرجاء إدخال UID صحيح. مثال: @som 1234567890[c]"
                    self.send_chat_message(data, error_msg)
                    
        except Exception as e:
            print(f"[!] Error in likes_command: {e}")
            error_msg = f"[FF0000]❌ حدث خطأ: {str(e)[:50]}[c]"
            self.send_chat_message(data, error_msg)


    def send_spam_request(self, uid, requester_id, original_data):
        """إرسال طلب زيادة الإعجابات إلى الـ API"""
        try:
            # بناء رابط API
            api_url = f"https://masry-spam-gamma.vercel.app/send_requests?uid={uid}&region=me&key=CTX-TEAM"
            
            print(f"[LIKES] Sending request to: {api_url}")
            
            # إرسال الطلب
            response = requests.get(api_url, timeout=15)
            
            print(f"[LIKES] Response Status: {response.status_code}")
            
            # تحليل النتيجة
            if response.status_code == 200:
                try:
                    result = response.json()
                    # محاولة استخراج رسالة النجاح من الـ API إذا وجدت
                    if isinstance(result, dict) and "message" in result:
                        success_msg = f"[00FF00]✅ {result['message']}[c]"
                    else:
                        success_msg = f"[00FF00]✅ تمت زيادة الإعجابات لليوزر {uid} بنجاح![c]"
                except:
                    # إذا لم يكن الرد JSON
                    success_msg = f"[00FF00]✅ تمت زيادة الإعجابات لليوزر {uid} (كود 200)[c]"
            elif response.status_code == 401:
                success_msg = "[FF0000]❌ فشل: الـ API يحتاج إلى مصادقة (Unauthorized)[c]"
            elif response.status_code == 404:
                success_msg = "[FF0000]❌ فشل: الرابط غير صحيح (API not found)[c]"
            else:
                success_msg = f"[FF0000]❌ فشل زيادة الإعجابات. كود الخطأ: {response.status_code}[c]"
            
            self.send_chat_message(original_data, success_msg)
            
        except requests.exceptions.Timeout:
            print("[LIKES] API Timeout")
            error_msg = "[FF0000]❌ انتهت مهلة الطلب، حاول مرة أخرى[c]"
            self.send_chat_message(original_data, error_msg)
        except requests.exceptions.ConnectionError:
            print("[LIKES] Connection Error")
            error_msg = "[FF0000]❌ فشل الاتصال بالسيرفر[c]"
            self.send_chat_message(original_data, error_msg)
        except Exception as e:
            print(f"[LIKES] Error: {e}")
            error_msg = f"[FF0000]❌ حدث خطأ: {str(e)[:50]}[c]"
            self.send_chat_message(original_data, error_msg)

    def send_zpi(self, uid, requester_id, original_data):
        """إرسال طلب زيادة الإعجابات إلى الـ API"""
        try:
            # بناء رابط API
            api_url = f"http://159.89.116.122:1525/spam?user_id={uid}&duration=3"
            
            print(f"[LIKES] Sending request to: {api_url}")
            
            # إرسال الطلب
            response = requests.get(api_url, timeout=15)
            
            print(f"[LIKES] Response Status: {response.status_code}")
            
            # تحليل النتيجة
            if response.status_code == 200:
                try:
                    result = response.json()
                    # محاولة استخراج رسالة النجاح من الـ API إذا وجدت
                    if isinstance(result, dict) and "message" in result:
                        success_msg = f"[00FF00]✅ {result['message']}[c]"
                    else:
                        success_msg = f"[00FF00]✅ تمت زيادة الإعجابات لليوزر {uid} بنجاح![c]"
                except:
                    # إذا لم يكن الرد JSON
                    success_msg = f"[00FF00]✅ تمت زيادة الإعجابات لليوزر {uid} (كود 200)[c]"
            elif response.status_code == 401:
                success_msg = "[FF0000]❌ فشل: الـ API يحتاج إلى مصادقة (Unauthorized)[c]"
            elif response.status_code == 404:
                success_msg = "[FF0000]❌ فشل: الرابط غير صحيح (API not found)[c]"
            else:
                success_msg = f"[FF0000]❌ فشل زيادة الإعجابات. كود الخطأ: {response.status_code}[c]"
            
            self.send_chat_message(original_data, success_msg)
            
        except requests.exceptions.Timeout:
            print("[LIKES] API Timeout")
            error_msg = "[FF0000]❌ انتهت مهلة الطلب، حاول مرة أخرى[c]"
            self.send_chat_message(original_data, error_msg)
        except requests.exceptions.ConnectionError:
            print("[LIKES] Connection Error")
            error_msg = "[FF0000]❌ فشل الاتصال بالسيرفر[c]"
            self.send_chat_message(original_data, error_msg)
        except Exception as e:
            print(f"[LIKES] Error: {e}")
            error_msg = f"[FF0000]❌ حدث خطأ: {str(e)[:50]}[c]"
            self.send_chat_message(original_data, error_msg)
            
    def dens_command(self, data):
        """معالجة أمر الرقصات الجماعية وإرسال طلبات للـ API"""
        try:
            print("[DENS] ==================================")
            print("[DENS] Command received!") 
            
            # تحويل البيانات إلى نص وفك الترميز
            try:
                # محاولة فك التشفير بطريقة صحيحة
                data_text = data.decode('utf-8', errors='ignore')
                print(f"[DENS] Decoded text: {data_text[:200]}")
            except:
                data_text = str(data)
                print(f"[DENS] Raw string: {data_text[:200]}")
            
            # البحث عن @dens
            if '@dens' in data_text:
                print("[DENS] @dens found in data")
                
                # استخراج النص بعد @dens حتى نهاية السطر أو أول رمز غير مرغوب
                import re
                # استخدام regex أكثر دقة
                match = re.search(r'@dens\s+(\d+(?:\s+\d+)*)', data_text)
                
                if match:
                    command_part = match.group(1)
                    print(f"[DENS] Command part: {command_part}")
                    
                    # تقسيم الأرقام
                    numbers = command_part.strip().split()
                    print(f"[DENS] Split numbers: {numbers}")
                    
                    # تنظيف الأرقام من أي رموز
                    clean_numbers = []
                    for num in numbers:
                        # استخراج الأرقام فقط
                        clean_num = re.sub(r'[^0-9]', '', num)
                        if clean_num:  # إذا لم يكن فارغاً
                            clean_numbers.append(clean_num)
                    
                    print(f"[DENS] Clean numbers: {clean_numbers}")
                    
                    # التحقق من وجود أرقام كافية (على الأقل 4: كود فريق + 1 UID + رقصة + تكرار)
                    if len(clean_numbers) >= 4:
                        
                        # كود الفريق (أول رقم)
                        team_code = clean_numbers[0]
                        
                        # عدد التكرارات (آخر رقم)
                        repeat_count = int(clean_numbers[-1])
                        
                        # رقم الرقصة (الرقم قبل الأخير)
                        emote_number = clean_numbers[-2]
                        
                        # UIDs هي الأرقام بين كود الفريق ورقم الرقصة (بحد أقصى 4)
                        uid_count = min(4, len(clean_numbers) - 3)
                        uids = clean_numbers[1:1+uid_count]
                        
                        # التحقق من أن uids لا تحتوي على أرقام الرقصة والتكرار
                        if emote_number in uids:
                            uids.remove(emote_number)
                        if str(repeat_count) in uids:
                            uids.remove(str(repeat_count))
                        
                        # تحويل رقم الرقصة إلى ID حقيقي
                        emote_id = self.get_emote_id(emote_number)
                        
                        player_id = data.hex()[12:22]
                        
                        print(f"[DENS] Team Code: {team_code}")
                        print(f"[DENS] UIDs: {uids}")
                        print(f"[DENS] Emote Number: {emote_number} -> ID: {emote_id}")
                        print(f"[DENS] Repeat Count: {repeat_count}")
                        
                        # التحقق من صحة البيانات
                        if repeat_count <= 0 or repeat_count > 100:
                            print("[DENS] Invalid repeat count")
                            error_msg = "[FF0000]❌ عدد التكرارات يجب أن يكون بين 1 و 100[c]"
                            self.send_chat_message(data, error_msg)
                            return
                        
                        if len(uids) == 0:
                            print("[DENS] No UIDs provided")
                            error_msg = "[FF0000]❌ يجب إدخال على الأقل UID واحد[c]"
                            self.send_chat_message(data, error_msg)
                            return
                        
                        if int(emote_number) < 1 or int(emote_number) > 50:
                            print("[DENS] Invalid emote number")
                            error_msg = "[FF0000]❌ رقم الرقصة يجب أن يكون بين 1 و 50[c]"
                            self.send_chat_message(data, error_msg)
                            return
                        
                        # إرسال الطلبات المتكررة في ثريد منفصل
                        print("[DENS] Starting thread for sending requests")
                        threading.Thread(target=self.send_dens_requests, args=(
                            team_code, 
                            uids, 
                            emote_id, 
                            emote_number,
                            repeat_count, 
                            player_id, 
                            data
                        )).start()
                        
                        # رسالة تأكيد
                        uid_list_str = ', '.join(uids)
                        confirm_msg = f"[00FF00]✓ تم بدء إرسال {repeat_count} رقصة رقم {emote_number} للأيدي: {uid_list_str}[c]"
                        self.send_chat_message(data, confirm_msg)
                        print(f"[DENS] Confirmation message sent")
                        
                    else:
                        print(f"[DENS] Insufficient numbers: {len(clean_numbers)}")
                        error_msg = "[FF0000]❌ التنسيق الصحيح: @dens [كود الفريق] [UID1] [UID2] [UID3] [UID4] [رقم الرقصة] [عدد التكرارات][c]\n"
                        error_msg += "[FF0000]📌 مثال: @dens 5286170 14727683166 6 10[c]"
                        self.send_chat_message(data, error_msg)
                else:
                    print("[DENS] Could not extract command part")
                    error_msg = "[FF0000]❌ التنسيق غير صحيح. استخدم: @dens [كود الفريق] [UID] [رقم الرقصة] [عدد التكرارات][c]"
                    self.send_chat_message(data, error_msg)
            else:
                print("[DENS] @dens not found in data")
                    
        except Exception as e:
            print(f"[DENS] Error in dens_command: {e}")
            import traceback
            traceback.print_exc()
            error_msg = f"[FF0000]❌ حدث خطأ: {str(e)[:50]}[c]"
            self.send_chat_message(data, error_msg)

    def fetch_clan_info(self, clan_id):
        """جلب معلومات الكلان من API"""
        try:
            url = f"https://info-clan-zenith.vercel.app/get_clan_info?clan_id={clan_id}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                error_msg = f"⚠️ خطأ من API: {response.status_code}"
                print(error_msg)
                return {"error": error_msg}
        except Exception as e:
            error_msg = f"⚠️ فشل الاتصال: {e}"
            print(error_msg)
            return {"error": error_msg}

    def format_clan_message(self, data):
        """تحويل JSON الكلان إلى نص منسق بالكامل"""
        if "error" in data:
            return data["error"]
        
        try:
            message = "[c][b][FFD700]━━━━━━━━━━━━━━ معلومات الكلان ━━━━━━━━━━━━━━[FFD700]\n\n"
            
            # اسم الكلان (مع التعامل مع الترميز)
            clan_name = data.get('clan_name', 'غير معروف')
            if isinstance(clan_name, str) and '\\u' in repr(clan_name):
                try:
                    clan_name = clan_name.encode('utf-8').decode('unicode_escape')
                except:
                    pass
            
            message += f"[c][b][00FF00] اسم الكلان:[00FF00] {clan_name}\n"
            message += f"[00FF00]معرف الكلان:[00FF00] {data.get('id', 'غير معروف')}\n"
            message += f"[00FF00] المنطقة:[00FF00] {data.get('region', 'غير معروف')}\n"
            message += f"[00FF00] المستوى:[00FF00] {data.get('level', 'غير معروف')}\n"
            message += f"[00FF00] الرتبة:[00FF00] {data.get('rank', 'غير معروف')}\n"
            message += f"[00FF00]النقاط:[00FF00] {data.get('score', 'غير معروف')}\n"
            message += f"[00FF00] الرصيد:[00FF00] {data.get('balance', 'غير معروف')}\n"
            message += f"[00FF00]الطاقة:[00FF00] {data.get('energy', 'غير معروف')}\n"
            message += f"[00FF00] الإنجازات:[00FF00] {data.get('achievements', 'غير معروف')}\n"
            message += f"[00FF00] التطويرات:[00FF00] {data.get('upgrades', 'غير معروف')}\n"
            message += f"[00FF00]إجمالي وقت اللعب:[00FF00] {data.get('total_playtime', 'غير معروف')} دقيقة\n"
            message += f"[00FF00] رسالة الترحيب:[00FF00] {data.get('welcome_message', 'لا يوجد')}\n"
            message += f"[00FF00]آخر نشاط:[00FF00] {data.get('last_active', 'غير معروف')}\n"
            message += f"[00FF00] آخر تحديث:[00FF00] {data.get('timestamp2', 'غير معروف')}\n"
            message += f"[00FF00] تاريخ الإنشاء:[00FF00] {data.get('timestamp1', 'غير معروف')}\n\n"
            
            # تفاصيل الكلان
            details = data.get('guild_details', {})
            if details:
                message += "[c][b][FFA500]────────────────────────────────[FFA500]\n"
                message += "[FFA500]● تفاصيل إضافية ●[FFA500]\n"
                message += "[FFA500]────────────────────────────────[FFA500]\n\n"
                
                message += f"إجمالي الأعضاء: {details.get('total_members', 'غير معروف')}\n"
                message += f"الأعضاء المتصلون: {details.get('members_online', 'غير معروف')}\n"
                message += f"منطقة الكلان: {details.get('region', 'غير معروف')}\n"
                message += f"وقت المكافأة: {details.get('reward_time', 'غير معروف')}\n"
                message += f"وقت الانتهاء: {details.get('expire_time', 'غير معروف')}\n\n"
            
            # الأرقام الكبيرة
            big_numbers = data.get('big_numbers', '[]')
            if big_numbers and big_numbers != '[]':
                message += "[c][b][FF69B4]────────────────────────────────[FF69B4]\n"
                message += "[FF69B4]● أرقام مهمة ●[/FF69B4]\n"
                message += "[FF69B4]────────────────────────────────[FF69B4]\n\n"
                
                # تنظيف الأرقام من الأقواس
                clean_numbers = big_numbers.strip('[]').replace('"', '')
                message += f"{clean_numbers}\n\n"
            
            # JSON Metadata
            json_meta = data.get('json_metadata', '{}')
            if json_meta and json_meta != '{}':
                try:
                    import json
                    meta = json.loads(json_meta)
                    tags = meta.get('tags', [])
                    if tags:
                        message += "[98FB98]────────────────────────────────[98FB98]\n"
                        message += "[98FB98]● تاجات الكلان ●[98FB98]\n"
                        message += "[98FB98]────────────────────────────────[98FB98]\n\n"
                        message += f"{', '.join(map(str, tags))}\n\n"
                except:
                    pass
            
            # معلومات إضافية
            message += "[FFD700]────────────────────────────────[FFD700]\n"
            message += f"كود الخطأ: {data.get('error_code', 'غير معروف')}\n"
            message += f"الحالة: {data.get('status_code', 'غير معروف')}\n"
            message += f"النوع الفرعي: {data.get('sub_type', 'غير معروف')}\n"
            message += f"الإصدار: {data.get('version', 'غير معروف')}\n"
            message += f"الأعلام: {data.get('flags', 'غير معروف')}\n"
            message += f"القيمة A: {data.get('value_a', 'غير معروف')}\n"
            message += f"نقاط الخبرة: {data.get('xp', 'غير معروف')}\n"
            
            message += "\n[FFD700]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[FFD700]"
            
            return message
            
        except Exception as e:
            print(f"خطأ في تنسيق معلومات الكلان: {e}")
            return f"حدث خطأ في التنسيق: {e}"


    def fetch_ban_status(self, uid):
        """جلب حالة الحظر للاعب من API"""
        try:
            url = f"https://tmk-check.vercel.app/check?uid={uid}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                error_msg = f"⚠️ خطأ من API: {response.status_code}"
                print(error_msg)
                return {"error": error_msg}
        except Exception as e:
            error_msg = f"⚠️ فشل الاتصال: {e}"
            print(error_msg)
            return {"error": error_msg}

    def format_ban_message(self, data):
        """تحويل JSON حالة الحظر إلى نص منسق بدون إيموجي"""
        if "error" in data:
            return data["error"]
        
        try:
            message = "[FFD700]━━━━━━━━━━━━━━ فحص الحظر ━━━━━━━━━━━━━━[FFD700]\n\n"
            
            uid = data.get('uid', 'غير معروف')
            username = data.get('username', 'غير معروف')
            is_banned = data.get('is_banned', False)
            status = data.get('status', 'UNKNOWN')
            ban_period = data.get('ban_period', 0)
            
            # معلومات أساسية
            message += f"[00FF00]UID:[00FF00] {uid}\n"
            message += f"[00FF00]اسم المستخدم:[00FF00] {username}\n\n"
            
            # حالة الحظر
            if is_banned:
                message += f"[FF0000]الحالة: {status}[FF0000]\n"
                message += f"[FF0000]مدة الحظر: {ban_period} أشهر[FF0000]\n"
                
                # رسالة إضافية حسب المدة
                if ban_period <= 3:
                    message += "[FFFF00]تحذير: حظر مؤقت[FFFF00]\n"
                elif ban_period <= 6:
                    message += "[FFA500]تحذير: حظر متوسط[FFA500]\n"
                else:
                    message += "[FF0000]تحذير: حظر طويل المدى[FF0000]\n"
            else:
                message += f"[00FF00]الحالة: غير محظور (ACTIVE)[00FF00]\n"
                message += "[00FF00]الحساب نظيف وآمن[00FF00]\n"
            
            message += "\n[FFD700]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[FFD700]"
            
            return message
            
        except Exception as e:
            print(f"خطأ في تنسيق رسالة الحظر: {e}")
            return f"⚠️ حدث خطأ في التنسيق: {e}"



    def get_emote_id(self, emote_number):
        """تحويل رقم الرقصة إلى ID حقيقي"""
        # قائمة الرقصات مع أرقامها
        emote_list = {
            '1': '909000001',
            '2': '909000002',
            '3': '909000003',
            '4': '909000004',
            '5': '909000005',
            '6': '909000006',
            '7': '909000007',
            '8': '909000008',
            '9': '909000009',
            '10': '909000010',
            '11': '909000011',
            '12': '909000012',
            '13': '909000013',
            '14': '909000014',
            '15': '909000015',
            '16': '909000016',
            '17': '909000017',
            '18': '909000018',
            '19': '909000019',
            '20': '909000020',
            '21': '909000021',
            '22': '909000022',
            '23': '909000023',
            '24': '909000024',
            '25': '909000025',
            '26': '909000026',
            '27': '909000027',
            '28': '909000028',
            '29': '909000029',
            '30': '909000031',
            '31': '909000032',
            '32': '909000033',
            '33': '909000034',
            '34': '909000035',
            '35': '909000036',
            '36': '909000037',
            '37': '909000038',
            '38': '909000039',
            '39': '909000040',
            '40': '909000041',
            '41': '909000042',
            '42': '909000043',
            '43': '909000044',
            '44': '909000045',
            '45': '909000046',
            '46': '909000047',
            '47': '909000048',
            '48': '909000049',
            '49': '909000051',
            '50': '909000052',
            '51': '909000053',
            '52': '909000054',
            '53': '909000055',
            '54': '909000056',
            '55': '909000057',
            '56': '909000058',
            '57': '909000059',
            '58': '909000060',
            '59': '909000061',
            '60': '909000062',
            '61': '909000063',
            '62': '909000064',
            '63': '909000065',
            '64': '909000066',
            '65': '909000067',
            '66': '909000068',
            '67': '909000069',
            '68': '909000070',
            '69': '909000071',
            '70': '909000072',
            '71': '909000073',
            '72': '909000074',
            '73': '909000075',
            '74': '909000076',
            '75': '909000077',
            '76': '909000078',
            '77': '909000079',
            '78': '909000080',
            '79': '909000081',
            '80': '909000082',
            '81': '909000083',
            '82': '909000084',
            '83': '909000085',
            '84': '909000086',
            '85': '909000087',
            '86': '909000088',
            '87': '909000089',
            '88': '909000090',
            '89': '909000091',
            '90': '909000092',
            '91': '909000093',
            '92': '909000094',
            '93': '909000095',
            '94': '909000096',
            '95': '909000097',
            '106': '909000108',
            '119': '909000121',
            '120': '909000122',
            '121': '909000123',
            '122': '909000124',
            '123': '909000125',
            '124': '909000126',
            '125': '909000127',
            '126': '909000128',
            '127': '909000129',
            '128': '909000130',
            '129': '909000131',
            '130': '909000132',
            '131': '909000133',
            '132': '909000134',
            '133': '909000135',
            '134': '909000136',
            '135': '909000137',
            '136': '909000138',
            '137': '909000139',
            '138': '909000140',
            '139': '909000141',
            '140': '909000142',
            '142': '909000144',
            '143': '909000145',
            '144': '909000150',
            '145': '909033001',
            '146': '909033002',
            '147': '909033003',
            '148': '909033004',
            '149': '909033005',
            '150': '909033006',
            '151': '909033007',
            '152': '909033008',
            '153': '909033009',
            '154': '909033010',
            '155': '909034001',
            '156': '909034002',
            '157': '909034003',
            '158': '909034004',
            '159': '909034005',
            '160': '909034006',
            '161': '909034007',
            '162': '909034008',
            '163': '909034009',
            '164': '909034010',
            '165': '909034011',
            '166': '909034012',
            '167': '909034013',
            '168': '909034014',
            '169': '909035001',
            '173': '909035005',
            '174': '909035006',
            '175': '909035007',
            '176': '909035008',
            '177': '909035009',
            '178': '909035010',
            '179': '909035011',
            '180': '909035012',
            '181': '909035013',
            '182': '909035014',
            '183': '909035015',
            '184': '909036001',
            '185': '909036002',
            '186': '909036003',
            '187': '909036004',
            '188': '909036005',
            '189': '909036006',
            '190': '909036008',
            '191': '909036009',
            '192': '909036010',
            '193': '909036011',
            '194': '909036012',
            '195': '909036014',
            '196': '909037001',
            '197': '909037002',
            '198': '909037003',
            '199': '909037004',
            '200': '909037005',
            '201': '909037006',
            '202': '909037007',
            '203': '909037008',
            '204': '909037009',
            '205': '909037010',
            '206': '909037011',
            '207': '909037012',
            '208': '909038001',
            '210': '909038003',
            '211': '909038004',
            '212': '909038005',
            '213': '909038006',
            '214': '909038008',
            '215': '909038009',
            '216': '909038010',
            '217': '909038011',
            '218': '909038012',
            '219': '909038013',
            '220': '909039001',
            '221': '909039002',
            '222': '909039003',
            '223': '909039004',
            '224': '909039005',
            '225': '909039006',
            '226': '909039007',
            '227': '909039008',
            '228': '909039009',
            '229': '909039010',
            '230': '909039011',
            '231': '909039012',
            '232': '909039013',
            '233': '909039014',
            '234': '909040001',
            '235': '909040002',
            '236': '909040003',
            '237': '909040004',
            '238': '909040005',
            '239': '909040006',
            '240': '909040008',
            '241': '909040009',
            '242': '909040010',
            '243': '909040011',
            '244': '909040012',
            '245': '909040013',
            '247': '909041001',
            '248': '909041002',
            '249': '909041003',
            '250': '909041004',
            '251': '909041005',
            '252': '909041006',
            '253': '909041007',
            '254': '909041008',
            '255': '909041009',
            '256': '909041010',
            '257': '909041011',
            '258': '909041012',
            '259': '909041013',
            '260': '909041014',
            '261': '909041015',
            '262': '909042001',
            '263': '909042002',
            '264': '909042003',
            '265': '909042004',
            '266': '909042005',
            '267': '909042006',
            '268': '909042007',
            '269': '909042008',
            '270': '909042009',
            '271': '909042011',
            '272': '909042012',
            '274': '909042016',
            '275': '909042017',
            '276': '909042018',
            '277': '909043001',
            '278': '909043002',
            '279': '909043003',
            '280': '909043004',
            '281': '909043005',
            '282': '909043006',
            '283': '909043007',
            '284': '909043008',
            '285': '909043009',
            '288': '909044001',
            '289': '909044002',
            '290': '909044003',
            '291': '909044004',
            '292': '909044005',
            '294': '909044007',
            '295': '909044008',
            '296': '909044009',
            '297': '909044010',
            '298': '909044011',
            '299': '909044012',
            '300': '909044015',
            '301': '909044016',
            '302': '909045001',
            '303': '909045002',
            '304': '909045003',
            '305': '909045004',
            '306': '909045005',
            '307': '909045006',
            '308': '909045007',
            '309': '909045008',
            '310': '909045009',
            '311': '909045010',
            '312': '909045011',
            '314': '909045015',
            '315': '909045016',
            '316': '909045017',
            '317': '909046001',
            '318': '909046002',
            '319': '909046003',
            '322': '909046006',
            '323': '909046007',
            '324': '909046008',
            '325': '909046009',
            '326': '909046010',
            '327': '909046011',
            '328': '909046012',
            '329': '909046013',
            '330': '909046014',
            '331': '909046015',
            '332': '909046016',
            '333': '909046017',
            '334': '909047001',
            '337': '909047004',
            '338': '909047005',
            '339': '909047006',
            '340': '909047007',
            '341': '909047008',
            '342': '909047009',
            '343': '909047010',
            '344': '909047011',
            '345': '909047012',
            '346': '909047013',
            '347': '909047015',
            '348': '909047016',
            '349': '909047017',
            '350': '909047018',
            '351': '909047019',
            '353': '909048002',
            '354': '909048003',
            '355': '909048004',
            '356': '909048005',
            '357': '909048006',
            '358': '909048007',
            '359': '909048008',
            '361': '909048010',
            '362': '909048011',
            '363': '909048012',
            '364': '909048013',
            '365': '909048014',
            '366': '909048015',
            '367': '909048016',
            '368': '909048017',
            '369': '909048018',
            '370': '909049001',
            '371': '909049002',
            '372': '909049003',
            '373': '909049004',
            '374': '909049005',
            '375': '909049006',
            '376': '909049007',
            '378': '909049009',
            '379': '909049010',
            '380': '909049011',
            '381': '909049012',
            '382': '909049013',
            '383': '909049014',
            '384': '909049015',
            '385': '909049016',
            '386': '909049017',
            '387': '909049018',
            '388': '909049019',
            '389': '909049020',
            '390': '909049021',
            '391': '909050002',
            '393': '909050004',
            '394': '909050005',
            '395': '909050006',
            '396': '909050008',
            '397': '909050009',
            '398': '909050010',
            '399': '909050011',
            '400': '909050012',
            '401': '909050013',
            '402': '909050014',
            '403': '909050015',
            '404': '909050016',
            '405': '909050017',
            '406': '909050018',
            '407': '909050019',
            '408': '909050020',
            '409': '909050021',
        }
        
        # إرجاع ID الرقصة أو الرقم الافتراضي إذا لم يوجد
        emote_id = emote_list.get(str(emote_number), '909000001')
        print(f"[DENS] Emote {emote_number} -> ID: {emote_id}")
        return emote_id

    def send_dens_requests(self, team_code, uids, emote_id, emote_number, repeat_count, requester_id, original_data):
        try:
            print("[DENS] ==================================")
            print("[DENS] Starting to send requests to API")
            

            uid_list = ['', '', '', '']
            for i in range(min(len(uids), 4)):
                uid_list[i] = uids[i]
            
            uid1, uid2, uid3, uid4 = uid_list
            
            print(f"[DENS] Prepared UIDs - UID1: '{uid1}', UID2: '{uid2}', UID3: '{uid3}', UID4: '{uid4}'")
            print(f"[DENS] Emote ID: {emote_id}, Team Code: {team_code}, Repeat: {repeat_count}")
            
            success_count = 0
            fail_count = 0
            
            for i in range(repeat_count):
                try:
                    
                    api_url = f"http://217.160.125.125:13699/join?tc={team_code}&uid1={uid1}&uid2={uid2}&uid3={uid3}&uid4={uid4}&emote_id={emote_id}"
                    
                    print(f"[DENS] Request {i+1}/{repeat_count}: Sending to {api_url}")
                    
                    # إرسال الطلب
                    response = requests.get(api_url, timeout=10)
                    
                    print(f"[DENS] Request {i+1} Response Status: {response.status_code}")
                    
                    if response.status_code == 200:
                        success_count += 1
                        try:
                            response_text = response.text
                            print(f"[DENS] Request {i+1} Response Text: {response_text[:100]}")
                        except:
                            pass
                    else:
                        fail_count += 1
                        print(f"[DENS] Request {i+1} Failed with status {response.status_code}")
                    
                    # انتظار قصير بين الطلبات (0.3 ثانية) لتجنب الحظر
                    if i < repeat_count - 1:
                        print(f"[DENS] Waiting 0.3 seconds before next request...")
                        time.sleep(0.3)
                    
                except requests.exceptions.Timeout:
                    fail_count += 1
                    print(f"[DENS] Request {i+1} Timeout")
                except requests.exceptions.ConnectionError:
                    fail_count += 1
                    print(f"[DENS] Request {i+1} Connection Error")
                except Exception as e:
                    fail_count += 1
                    print(f"[DENS] Request {i+1} Error: {e}")
            
            # إرسال تقرير النتيجة
            print(f"[DENS] Final Result: {success_count} Success, {fail_count} Failed")
            
            if success_count > 0:
                result_msg = f"[00FF00]✅ تم الانتهاء من {repeat_count} رقصة: [FFDD00]{success_count} نجاح[00FF00] - [FF0000]{fail_count} فشل[c]"
            else:
                result_msg = f"[FF0000]❌ فشل جميع الطلبات ({fail_count})[c]"
            
            self.send_chat_message(original_data, result_msg)
            print("[DENS] ==================================")
            
        except Exception as e:
            print(f"[DENS] Error in send_dens_requests: {e}")
            import traceback
            traceback.print_exc()
            error_msg = f"[FF0000]❌ حدث خطأ أثناء إرسال الطلبات: {str(e)[:50]}[c]"
            self.send_chat_message(original_data, error_msg)

    #################################
    # دوال مساعدة لإرسال الرسائل
    #################################

    def send_chat_message(self, data, message):
        """إرسال رسالة في الشات"""
        try:
            print(f"[CHAT] Preparing to send: {message[:50]}...")
            
            # استخدام الدالة الموجودة gen_msgv2 لإرسال الرسالة
            msg_packet = gen_msgv2(data.hex(), message)
            print(f"[CHAT] Generated packet length: {len(msg_packet)}")
            
            # تأكد أن النص يحتوي فقط على أرقام وحروف hex
            import re
            # تنظيف النص من أي أحرف غير hex
            cleaned_packet = re.sub(r'[^0-9a-fA-F]', '', msg_packet)
            print(f"[CHAT] Cleaned packet length: {len(cleaned_packet)}")
            
            if len(cleaned_packet) % 2 == 0:  # تأكد أن الطول زوجي
                if self.sock1200:
                    self.sock1200.send(bytes.fromhex(cleaned_packet))
                    print(f"[CHAT] Message sent successfully")
                else:
                    print("[CHAT] sock1200 is None")
            else:
                print(f"[!] Invalid hex length: {len(cleaned_packet)}")
                
        except Exception as e:
            print(f"[!] Error sending chat message: {e}")
            import traceback
            traceback.print_exc()                   
                                                            
                                                                                    
    def msgz_command(self, data):
        """معالجة أمر الشبح وإرسال البيانات للـ API"""
        try:
            # استخراج النص من البيانات
            data_str = str(data)
            
            # البحث عن النص بعد @ghost
            if '@msg' in data_str:
                # استخراج المحتوى بعد @ghost
                parts = data_str.split('@msg')[1].strip()
                
                # تقسيم النص إلى كود الفريق واسم الشبح
                # نتوقع أن يكون التنسيق: @ghost [كود الفريق] [اسم الشبح]
                import re
                # استخدام regex لاستخراج الكلمات
                words = re.findall(r'[\w]+', parts)
                
                if len(words) >= 2:
                    team_code = words[0]  # أول كلمة بعد @ghost هي كود الفريق
                    ghost_name = words[1]  # ثاني كلمة هي اسم الشبح
                    
                    # استخراج ID اللاعب من البيانات (مثل ما هو موجود في الأوامر الأخرى)
                    player_id = data.hex()[12:22]
                    
                    print(f"[msg] Team Code: {team_code},msg {ghost_name}, Player ID: {player_id}")
                    
                    # إرسال الطلب إلى API في ثريد منفصل حتى لا يتأثر الأداء
                    threading.Thread(target=self.send_to_msg_api, args=(team_code, ghost_name, player_id)).start()
                    
                    # إرسال رسالة تأكيد في الشات
                    confirm_msg = f"[00FF00]تم إرسال بيانات ✓[c]"
                    colored_msg = generate_random_color() + confirm_msg
                    self.send_chat_message(data, colored_msg)
                else:
                    # إذا كان التنسيق غير صحيح
                    error_msg = "[FF0000]التنسيق الصحيح: @msg [كود الفريق] [اسم الشبح][c]"
                    colored_error = generate_random_color() + error_msg
                    self.send_chat_message(data, colored_error)
                    
        except Exception as e:
            print(f"[!] Error in msg_command: {e}")
            
            
    def send_to_msg_api(self, team_code, ghost_name, player_id):
        """إرسال البيانات إلى API الشبح"""
        try:
            # تنظيف الأسماء من الرموز غير المرغوب فيها
            team_code = team_code.strip()
            ghost_name = ghost_name.strip()
            
            # بناء رابط API
            api_url = f"https://alliff-alliff-host.hf.space/proxy/5002/msg?teamcode={team_code}&msg={ghost_name}"
            
            print(f"[msg] Sending to API: {api_url}")
            
            # إرسال الطلب
            response = requests.get(api_url, timeout=10)
            
            if response.status_code == 200:
                print(f"[msg] API Response Success: {response.text[:100]}")
            else:
                print(f"[msg] API Error: Status {response.status_code}")
                
        except requests.exceptions.Timeout:
            print("[msg] API Timeout")
        except requests.exceptions.ConnectionError:
            print("[msg] API Connection Error")
        except Exception as e:
            print(f"[msg] Error: {e}")            

    def ghost_command(self, data):
        """معالجة أمر الشبح وإرسال البيانات للـ API"""
        try:
            # استخراج النص من البيانات
            data_str = str(data)
            
            # البحث عن النص بعد @ghost
            if '@ghost' in data_str:
                # استخراج المحتوى بعد @ghost
                parts = data_str.split('@ghost')[1].strip()
                
                # تقسيم النص إلى كود الفريق واسم الشبح
                # نتوقع أن يكون التنسيق: @ghost [كود الفريق] [اسم الشبح]
                import re
                # استخدام regex لاستخراج الكلمات
                words = re.findall(r'[\w]+', parts)
                
                if len(words) >= 2:
                    team_code = words[0]  # أول كلمة بعد @ghost هي كود الفريق
                    ghost_name = words[1]  # ثاني كلمة هي اسم الشبح
                    
                    # استخراج ID اللاعب من البيانات (مثل ما هو موجود في الأوامر الأخرى)
                    player_id = data.hex()[12:22]
                    
                    print(f"[GHOST] Team Code: {team_code}, Ghost Name: {ghost_name}, Player ID: {player_id}")
                    
                    # إرسال الطلب إلى API في ثريد منفصل حتى لا يتأثر الأداء
                    threading.Thread(target=self.send_to_ghost_api, args=(team_code, ghost_name, player_id)).start()
                    
                    # إرسال رسالة تأكيد في الشات
                    confirm_msg = f"[00FF00]تم إرسال بيانات الشبح بنجاح✓[c]"
                    colored_msg = generate_random_color() + confirm_msg
                    self.send_chat_message(data, colored_msg)
                else:
                    # إذا كان التنسيق غير صحيح
                    error_msg = "[FF0000]التنسيق الصحيح: @ghost [كود الفريق] [اسم الشبح][c]"
                    colored_error = generate_random_color() + error_msg
                    self.send_chat_message(data, colored_error)
                    
        except Exception as e:
            print(f"[!] Error in ghost_command: {e}")
    
    def send_to_ghost_api(self, team_code, ghost_name, player_id):
        """إرسال البيانات إلى API الشبح"""
        try:
            # تنظيف الأسماء من الرموز غير المرغوب فيها
            team_code = team_code.strip()
            ghost_name = ghost_name.strip()
            
            # بناء رابط API
            api_url = f"http://85.215.137.163:15269/ghost?teamcode={team_code}&name={ghost_name}&api_key=YAKOUBxZenith"
            
            print(f"[GHOST] Sending to API: {api_url}")
            
            # إرسال الطلب
            response = requests.get(api_url, timeout=10)
            
            if response.status_code == 200:
                print(f"[GHOST] API Response Success: {response.text[:100]}")
            else:
                print(f"[GHOST] API Error: Status {response.status_code}")
                
        except requests.exceptions.Timeout:
            print("[GHOST] API Timeout")
        except requests.exceptions.ConnectionError:
            print("[GHOST] API Connection Error")
        except Exception as e:
            print(f"[GHOST] Error: {e}")
    


    def handle_client(self, connection):
        version, nmethods = connection.recv(2)
        methods = self.get_available_methods(nmethods, connection)
        if 2 not in set(methods):
            connection.close()
            return
        connection.sendall(bytes([SOCKS_VERSION, 2]))
        if not self.verify_credentials(connection):
            return
        version, cmd, _, address_type = connection.recv(4)
        if address_type == 1:
            address = socket.inet_ntoa(connection.recv(4))
        elif address_type == 3:
            domain_length = connection.recv(1)[0]
            address = connection.recv(domain_length)
            address = socket.gethostbyname(address)
        port = int.from_bytes(connection.recv(2), 'big', signed=False)
        try:
            if cmd == 1:
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address, port))
                bind_address = remote.getsockname()
            else:
                connection.close()
                return
            addr = int.from_bytes(socket.inet_aton(bind_address[0]), 'big', signed=False)
            port = bind_address[1]
            reply = b''.join([
                SOCKS_VERSION.to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(1).to_bytes(1, 'big'),
                addr.to_bytes(4, 'big'),
                port.to_bytes(2, 'big')
            ])
        except Exception as e:
            reply = self.generate_failed_reply(address_type, 5)
        connection.sendall(reply)
        if reply[1] == 0 and cmd == 1:
            self.exchange_loop(connection, remote)
        connection.close()
       
#################################



    def msg_zix(self, id):
        ent_packet = f"120000018d08{id}101220022a800308{id}10{id}22d2015b625d5b635d5b6666303030305dd8aad98520d8a7d984d8aad981d8b9d98ad98420d8a8d986d8acd8a7d8ad20d8a7d8b0d8a720d8b5d8a7d8b120d985d8b9d983d98520d8a7d98a20d8aed8b7d8a320d8aad988d8a7d8b5d98420d985d8b9d98a20d984d8add984d987d8a720d98820d8a7d8b0d8a720d8aad988d981d981d8aa20d8a7d98a20d985d98ad8b2d8a9200a200a5b3030303066665d546865206665617475726520686173206265656e207375636365737366756c6c79206163746976617465642e20547279206974206e6f7728f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")
            
                 
#############################
    def zixctx(self, id):
        ent_packet = f"060000006f08d4d7faba1d100620022a6308c8f0dacb081a1c5b3030464630305d2b2be385a45A4958000020205b3030464630305d32024d454040b00113b801e71cd801d4d8d0ad03e00191db8dae03ea010a5a45522d49534b494e47f00101f801911a8002fd98a8dd03900201d0020ad80221"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")

 
    def gen_squad5(self, id):
        ent_packet = f"05000001ff08{id}1005203a2af20308{id}12024d451801200432f70208{id}12095A49587E4354587E7E1a024d4520d78aa5b40628023085cbd1303832421880c38566fa96e660c19de061d998a36180a89763aab9ce64480150c90158e80792010801090a12191a1e209801c901c00101e801018802039202029603aa0208080110e43218807daa0207080f10e4322001aa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710e432aa0205082310e432aa0205082b10e432aa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910e432aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810e432aa0205082910e432c2022812041a0201041a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a03009203009803b7919db30ba20319c2b27854e19687e197a95fe191ade192aae197a95945e19687e20301523a011a403e50056801721e313732303237323231313638373535353930315f736f3278687a61366e347801820103303b30880180e0aecdacceba8e19a20100b00114ea010449444332fa011e313732303237323231313638373535383330335f71356f79736b3934716d"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")

################skin################
    def skin1(self, id):
        ent_packet = f"050000025808{id}100520542acb0408a5f1a5c90310{id}1abc0408{id}120b2b2b2b2b464f582b2b2b2b1a024d4520f9db8dc50628023087cbd1303832421880a89763f089e361f680e960b185a661a5cfd064c9fb8766480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101d001a1fd89af03e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a030208019203009803fab8cdb80ba20312e385a4e385a4434f444558e385a4424f5453e203024f52ea0300f203008004649004029a040a08f9db8dc50620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042108a5f1a5c903121484a5d164bf9ce061b5c38566839aa361f780e96018b3cbd130f00407fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa0402081580050a9005e907"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
            
    def skin2(self, id):
        ent_packet = f"050000025c08{id}100520542acf0408a5f1a5c90310{id}1ac00408{id}120b2b2b2b2b464f582b2b2b2b1a024d4520f9db8dc50628023087cbd1303832421880a89763f089e361f680e960b185a661a5cfd064c9fb8766480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101d001a1fd89af03e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a030208019203009803fab8cdb80ba20312e385a4e385a4434f444558e385a4424f5453e203024f52ea0300f203008004649004029a040a08f9db8dc50620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042508a5f1a5c90312188cf6d064cf85d164bf9ce061b5c385669abfa5619dcae86018b3cbd130f00406fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa0402081580050a9005e907"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
    def skin3(self, id):
        ent_packet = f"050000025c08{id}100520542acf0408a5f1a5c90310{id}1ac00408{id}120b2b2b2b2b464f582b2b2b2b1a024d4520f9db8dc50628023087cbd1303832421880a89763f089e361f680e960b185a661a5cfd064c9fb8766480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101d001a1fd89af03e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a030208019203009803fab8cdb80ba20312e385a4e385a4434f444558e385a4424f5453e203024f52ea0300f203008004649004029a040a08f9db8dc50620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042508a5f1a5c9031218b5c38566d0fda561c8e1e860d7bace64c9ded064929be06118b3cbd130f00408fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa0402081580050a9005e907"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")

    def skin4(self, id):
        ent_packet = f"050000025a08{id}100520502acd0408a5f1a5c90310{id}1abe0408{id}120b2b2b2b2b464f582b2b2b2b1a024d452099d98dc50628023087cbd1303832421880a89763f089e361f680e960b185a661a5cfd064c9fb876650ad0258e80792010a0107090a0b12191a201d9801ad02c00101d001a1fd89af03e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200ea0204100118018a030208019203009803fab8cdb80ba20312e385a4e385a4434f444558e385a4424f5453e203024f52ea0300f203008004649004029a040a0899d98dc50620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042508a5f1a5c9031218929be061b5c38566d0fda561e0e1e860899dd1648bf6d06418b3cbd130f00409fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa0402081580050a9005e907"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")   
            
    def skin5(self, id):
        ent_packet = f"050000022e08{id}100520502aa10408{id}10{id}1a920408{id}120c75776a736a736a736e646a641a024d4520c6befec40628023087cbd13038324218c09ae06180a89763c091e660c0b5ce6480c385668096a361480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200ea0204100118018a03020801920300ea0300f203008004649004029a040a08b6befec40620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042508{id}1218b597a361909ce660c0b5ce6480a89763929be061b5c3856618b3cbd130f00408fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa04020815"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
                                          
    def skin6(self, id):
        ent_packet = f"050000025c08{id}100520542acf0408a5f1a5c90310{id}1ac00408{id}120b2b2b2b2b464f582b2b2b2b1a024d4520f9db8dc50628023087cbd1303832421880a89763f089e361f680e960b185a661a5cfd064c9fb8766480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101d001a1fd89af03e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a030208019203009803fab8cdb80ba20312e385a4e385a4434f444558e385a4424f5453e203024f52ea0300f203008004649004029a040a08f9db8dc50620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042508a5f1a5c9031218b5c38566d0fda561c8e1e860d0b5ce64c9ded064929be06118b3cbd130f00408fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa0402081580050a9005e907"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
    def skin7(self, id):
        ent_packet = f"050000023708{id}100520502aaa0408{id}10{id}1a9b0408{id}120c75776a736a736a736e646a641a024d4520a0c0fec40628023087cbd13038324218c09ae06180a89763c091e660c0b5ce6480c385668096a361480150ad0258e80792010a0107090a0b12191a201d9801ad02c00101e80101880204920208c205ae2dba109215aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200ea0204100118018a03020801920300e203024f52ea0300f203008004649004029a040a08a0c0fec40620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}e00401ea042908{id}121c909ce660c0b5ce6480a89763929be061b5c38566ddd9e860b597a36118b3cbd130f00407fa04050803108703fa0405080410de02fa0405080510c001fa0405081d109501fa040408161073fa0405080e10af01fa04020815"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")     
            
                   
                          
###############dens#################
    def zix_dens17(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}109184bbb1032a0c08{id}189184bbb10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
            
    def zix_dens16(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}109afbb8b1032a0c08{id}189afbb8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
    def zix_dens15(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10e193bbb1032a0c08{id}18e193bbb10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")


    def zix_dens14(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}108bfbb8b1032a0c08{id}188bfbb8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
            
    def zix_dens13(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}1095fbb8b1032a0c08{id}1895fbb8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
    def zix_dens12(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10d9fab8b1032a0c08{id}18d9fab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")

    def zix_dens11(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10d5fab8b1032a0c08{id}18d5fab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")   
            
    def zix_dens10(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10d0fab8b1032a0c08{id}18d0fab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
                                          
    def zix_dens9(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10f4fab8b1032a0c08{id}18f4fab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
    def zix_dens8(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10fffab8b1032a0c08{id}18fffab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")  
            
    def zix_dens1(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10f0fab8b1032a0c08{id}18f0fab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
            
    def zix_dens2(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10d4fab8b1032a0c08{id}18d4fab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
    def zix_dens3(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10cbfab8b1032a0c08{id}18cbfab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")

    def zix_dens4(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10cefab8b1032a0c08{id}18cefab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")   
            
    def zix_dens5(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10ccfab8b1032a0c08{id}18ccfab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
                                          
    def zix_dens6(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}10c6fab8b1032a0c08{id}18c6fab8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")
            
    def zix_dens7(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}1091fbb8b1032a0c08{id}1891fbb8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")  

    def zix_dens18(self, id):
        ent_packet = f"050000002c08{id}100520162a2008{id}109afbb8b1032a0c08{id}189afbb8b10330b7d7bc8206"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")                             
###################################            
    def pc(self, id):
        ent_packet = f"05000003ff08{id}100520062af20708d3858dd22312024d451801200332cc0408d3858dd22312135b6564303930395d50454741e2808f535553201a024d4520a6e38baa0628443087cbd13038324218e0f38766e796a3618994e660f39ae061e5b7d064bfb8ce64480150ce01588e0c60f5d7d0ad0368c2dc8dae037a05d7d0cab00382012b08b3daf1eb041211d8b2d98ad988d98ad986d983d983e29cbf180620b687d4f0042a0808c49d85f30410038801ed89c5b00392010b0107090a0b1216191a20239801cd01a00111a80185fff5b103c00101c80101d001bace89af03e80101880203920207c20500a606e532aa020a080110c03e18f0602002aa0205080210b232aa0205080310e432aa020a080f10918a0118a09c01aa0205081710e750aa0205081810b768aa0205081a10da74aa0206081b10918a01aa0206081c10958c01aa02050820108b79aa0205082110eb7aaa0205082210a275aa0206082310dc8701aa0205082b10f476aa0205083110f476aa0206083910918a01aa0206083d10918a01aa0206084110918a01aa0205084910e432aa0205084d10e432aa0206083410918a01aa0205082810e432aa0205082910e432c2022112041a0201041a090848120501040506071a0508501201631a0508511201652200ea02520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3237373631373532363237343633352f706963747572653f77696474683d313630266865696768743d31363010011801f202090887cab5ee0110870a8a030808021003180528019203009803f3e78ea30ba20315e298afd986d8a7d8acd988d986d98ae298afe29c9432d00208{id}120b5b6666303030305d5a49581a024d452096ed8baa0628043089cbd13038324214fa96e660b599a361c19de061aab9ce64abb9ce64480150c90158e80792010601090a1219209801c901c00101c80101e80101880204920206ee07ce010000aa0208080110ff34188064aa020b080f10fd3218b086012001aa0205080210e432aa0205081810fd32aa0205081a10fd32aa0205081c10fd32aa0205082010fd32aa0205082210fd32aa0205082110fd32aa0205081710e432aa0205082310fd32aa0205082b10fd32aa0205083110fd32aa0205083910fd32aa0205083d10fd32aa0205084110fd32aa0205084910d836aa0205084d10e432aa0205081b10fd32aa0205083410fd32aa0205082810e432aa0205082910e432c2022112041a0201041a090848120501040506071a0508501201631a0508511201652200ea0204100118018a03009203003a0101400150016801721e313639383838363035353130343733333939355f6a67386c37333431646688018090aefec3978fef17a20100b001e001ea010449444331"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else: 
            print("[!] sock0500 not assigned.")            

    def Dev(self, id):
        ent_packet = f"050000030908{id}1005203f2afc0508{id}12024d451801200332980408{id}120c5a4958c2a1c2bfe280a2607e1a024d4520abbabccc0628023087cbd13038324218c0b5ce64f680e960d998a36180a89763f089e36180c38566480150ad0258e80782011808d1daf1eb04180120d187d4f0042a0808c79d85f304100392010a0107090a0b12191a20279801ad02c00101d001a1fd89af03e80101fa010808021010180f28618802049202089215ba10c205ae2daa0208080110bf3118807daa0208080f10bf3118904eaa0205080210e432aa0205081810bf31aa0205081a10bf31aa0205081c10bf31aa0205082010bf31aa0205082210e432aa0205082110bf31aa0205081710904eaa0205082310bf31aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910bf31aa0205083d10bf31aa0205084110bf31aa0205084910d836aa0205084d10e432aa0205081b10bf31aa0205083410bf31aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200ea0204100118018a0300920300e203034f5219ea0300f203008004619004029a040a08abbabccc0620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}f0040afa04050803108703fa04050804108103fa0405080510c001fa0405081d10cc01fa040408161073fa0405080e10af01fa040208153a0101400150016801721e313737303938363739353836353034323630395f6439756b6b7377766568880180c0f7b0bee7a7881ca20100a80101b001c902ea010449444331f2014908{id}10c8f0dacb081a23e38086efbb9aefbabcefbb8cefba91d8a7e385a4efafbdefbba8efbba4efba98efba912084db8dae0328a3babccc06302b380b4204100118014801fa011e313737303938363739353836353034363037325f3335397568776b6573678a021e313737303938363739353836353034383335305f613133667036386e3364"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")

    def Devv(self, id):
        ent_packet = f"05000002e008{id}1005203f2ad30508{id}12024d4518012003328d0408{id}1210d8a7d984d8b3d8a7d8add8b1324c324d1a024d4520e4a3becc0628023087cbd1303832421880c3856680a89763c09ae061c0b5ce648096a361c091e660480150ad0258e80792010a0107090a0b12191a20279801ad02c00101e80101880208920208c205b622ba10da16aa0208080110e43218807daa0208080f10e43218807daa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710904eaa0205082310e432aa0205082b10b06daa0205084a10b06daa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910d836aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810904eaa0205082910e432aa0205085910e432c2022712031a01001a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200ea0204100118018a030208019203009803d38ffdc10ba2030b77776164616d68616a6a69e203034f5219ea0300f203008004649004029a040a08e4a3becc0620014001a00465aa040408011001aa040408011003aa0407080f1d0000803fba0400ca0400da040608{id}f0040afa04050803108703fa04050804108103fa0405080510c001fa0405081d10cc01fa040408161073fa0405080e10af01fa0402081580050b9005e9073a0101400150016801721e313737313031363637363837343838333631325f7a6b6f6d64736b753264880180a0f79289a7c4881ca20100b001c902ea010449444331f2012e08{id}10d0b8d0a5301a0e5a49587e424f542d56392de280a228daa3becc06302b380b4204100118014801fa011e313737313031363637363837343838363232325f663539756b6978696a318a021e313737313031363637363837343838383430325f75737a6474316c79666b"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")            
 

##########deb8daee36####################
###############################


            
    
    
    def skinaaaat(self, idd):    
        skins = [
    "c091e660","c191e660","c291e660","c391e660","c491e660","c591e660","c691e660","c791e660","c891e660","c991e660","ca91e660","cb91e660","cc91e660","cd91e660","ce91e660","cf91e660","d091e660","d191e660","d291e660","d391e660","d491e660","d591e660","d691e660","d791e660","d891e660","d991e660","da91e660","db91e660","dc91e660","dd91e660","de91e660","df91e660","e091e660","e191e660","e291e660","e391e660","e491e660","e591e660","e691e660","e791e660","e891e660","e991e660","ea91e660","eb91e660","ec91e660","ed91e660","ee91e660","ef91e660","f091e660","f191e660","f291e660","f391e660","f491e660","f591e660","f691e660","f791e660","f891e660","f991e660","fa91e660","fb91e660","fc91e660","fd91e660","fe91e660","ff91e660","8092e660","8192e660","8292e660","8392e660","8492e660","8592e660","8692e660","8792e660","8892e660","8992e660","8a92e660","8b92e660","8c92e660","8d92e660","8e92e660","8f92e660","9092e660","9192e660","9292e660","9392e660","9492e660","9592e660","9692e660","9792e660","9892e660","9992e660","9a92e660","9b92e660","9c92e660","9d92e660","9e92e660","9f92e660","a092e660","a192e660","a292e660","a392e660","a492e660","a592e660","a692e660","a792e660","a892e660","a992e660","aa92e660","ab92e660","ac92e660","ad92e660","ae92e660","af92e660","b092e660","b192e660","b292e660","b392e660","b492e660","b592e660","b692e660","b792e660","b892e660","b992e660","ba92e660","bb92e660","bc92e660","bd92e660","be92e660","bf92e660","c092e660","c192e660","c292e660","c392e660","c492e660","c592e660","c692e660","c792e660","c892e660","c992e660","ca92e660","cb92e660","cc92e660","cd92e660","ce92e660","cf92e660","d092e660","d192e660","d292e660","d392e660","d492e660","d592e660","d692e660","d792e660","d892e660","d992e660","da92e660","db92e660","dc92e660","dd92e660","de92e660","df92e660","e092e660","e192e660","e292e660","e592e660","e692e660","e792e660","e892e660","ea92e660","ec92e660","ed92e660","ee92e660","ef92e660","f092e660","f192e660","f292e660","f392e660","f492e660","f592e660","f692e660","f792e660","f892e660","f992e660","fa92e660","fb92e660","fc92e660","fd92e660","fe92e660","ff92e660","8093e660","8193e660","8293e660","8393e660","8493e660","8593e660","8693e660","8793e660","8893e660","8993e660","8a93e660","8b93e660","8c93e660","8d93e660","8e93e660","8f93e660","9093e660","9193e660","9293e660","9393e660","9493e660","9593e660","9693e660","9793e660","9893e660","9993e660","9a93e660","9b93e660","9c93e660","9d93e660","9e93e660","9f93e660","a093e660","a193e660","a293e660","a393e660","a493e660","a593e660","a693e660","a793e660","a893e660","a993e660","ac93e660","ad93e660","ae93e660","af93e660","b193e660","b293e660","b393e660","b493e660","b593e660","b693e660","b793e660","b893e660","b993e660","ba93e660","bb93e660","bc93e660","bd93e660","be93e660","bf93e660","c093e660","c193e660","c293e660","c393e660","c493e660","c593e660","c693e660","c793e660","c893e660","c993e660","ca93e660","cb93e660","cc93e660","cd93e660","ce93e660","cf93e660","d093e660","d193e660","d293e660","d393e660","d493e660","d593e660","d693e660","d793e660","d893e660","d993e660","da93e660","db93e660","dc93e660","dd93e660","de93e660","df93e660","e093e660","e193e660","e293e660","e393e660","e493e660","e593e660","e693e660","e793e660","e893e660","e993e660","ea93e660","eb93e660","ec93e660","ed93e660","ee93e660","ef93e660","f093e660","f193e660","f293e660","f393e660","f493e660","f593e660","f693e660","f793e660","f893e660","f993e660","fa93e660","fb93e660","fc93e660","fd93e660","fe93e660","ff93e660","8094e660","8194e660","8294e660","8394e660","8494e660","8594e660","8694e660","8794e660","8894e660","8994e660","8a94e660","8b94e660","8c94e660","8d94e660","8e94e660","8f94e660","9094e660","9194e660","9294e660","9394e660","9494e660","9594e660","9694e660","9794e660","9894e660","9994e660","9a94e660","9b94e660","9c94e660","9d94e660","9e94e660","9f94e660","a094e660","a194e660","a294e660","a394e660","a494e660","a594e660","a694e660","a794e660","a894e660","a994e660","aa94e660","ab94e660","ac94e660","ad94e660","ae94e660","af94e660","b094e660","b194e660","b294e660","b394e660","b494e660","b594e660","b694e660","b794e660","b894e660","b994e660","ba94e660","bb94e660","bc94e660","bd94e660","be94e660","bf94e660","c094e660","c194e660","c294e660","c394e660","c494e660","c594e660","c694e660","c794e660","c894e660","c994e660","ca94e660","cb94e660","cc94e660","cd94e660","ce94e660","cf94e660","d094e660","d194e660","d294e660","d394e660","d494e660","d594e660","d694e660","d794e660","d994e660","da94e660","db94e660","dc94e660","dd94e660","de94e660","df94e660","e094e660","e194e660","e294e660","e394e660","e494e660","e594e660","e694e660","e794e660","e894e660","e994e660","ea94e660","eb94e660","ec94e660","ed94e660","ee94e660","ef94e660","f094e660","f194e660","f294e660","f394e660","f494e660","f594e660","f694e660","f794e660","f894e660","f994e660","fa94e660","fb94e660","fc94e660","fd94e660","fe94e660","ff94e660","8095e660","8195e660","8295e660","8395e660","8495e660","8595e660","8695e660","8795e660","8895e660","8995e660","8a95e660","8b95e660","8c95e660","8d95e660","8e95e660","9095e660","9195e660","9295e660","9395e660","9495e660","9595e660","9695e660","9795e660","9895e660","9995e660","9a95e660","9b95e660","9c95e660","9d95e660","9e95e660","9f95e660","a095e660","a195e660","a295e660","a395e660","a495e660","a595e660","a695e660","a795e660","a895e660","a995e660","aa95e660","ab95e660","ac95e660","ad95e660","ae95e660","af95e660","b095e660","b195e660","b295e660","b395e660","b495e660","b595e660","b695e660","b795e660","b895e660","b995e660","ba95e660","bb95e660","bc95e660","bd95e660","be95e660","bf95e660","c095e660","c195e660","c295e660","c395e660","c495e660","c595e660","c695e660","c795e660","c895e660","c995e660","ca95e660","cb95e660","cc95e660","cd95e660","ce95e660","cf95e660","d095e660","d195e660","d295e660","d395e660","d495e660","d595e660","d695e660","d795e660","d895e660","d995e660","da95e660","db95e660","dc95e660","dd95e660","de95e660","df95e660","e095e660","e195e660","e295e660","e395e660","e495e660","e595e660","e695e660","e795e660","e895e660","e995e660","ea95e660","eb95e660","ec95e660","ed95e660","ee95e660","ef95e660","f095e660","f195e660","f295e660","f395e660","f495e660","f595e660","f695e660","f795e660","f895e660","f995e660","fa95e660","fb95e660","fc95e660","fd95e660","fe95e660","ff95e660","8096e660","8196e660","8296e660","8396e660","8496e660","8596e660","8696e660","8796e660","8896e660","8996e660","8a96e660","8b96e660","8c96e660","8d96e660","8e96e660","8f96e660","9096e660","9196e660","9296e660","9396e660","9496e660","9596e660","9696e660","9796e660","9896e660","9996e660","9a96e660","9b96e660","9c96e660","9d96e660","9e96e660","9f96e660","a096e660","a196e660","a296e660","a396e660","a496e660","a596e660","a696e660","a796e660","a896e660","a996e660","aa96e660","ab96e660","ac96e660","ad96e660","ae96e660","af96e660","b096e660","b196e660","b296e660","b396e660","b496e660","b596e660","b696e660","b796e660","b896e660","b996e660","ba96e660","bb96e660","bc96e660","bd96e660","be96e660","bf96e660","c096e660","c196e660","c296e660","c396e660","c496e660","c596e660","c696e660","c796e660","c896e660","c996e660","ca96e660","cb96e660","cc96e660","cd96e660","ce96e660","cf96e660","d096e660","d196e660","d296e660","d396e660","d496e660","d596e660","d696e660","d796e660","d896e660","d996e660","da96e660","db96e660","dc96e660","dd96e660","de96e660","df96e660","e096e660","e196e660","e296e660","e396e660","e496e660","e596e660","e696e660","e796e660","e896e660","e996e660","ea96e660","eb96e660","ec96e660","ed96e660","ee96e660","ef96e660","f096e660","f196e660","f296e660","f396e660","f496e660","f596e660","f696e660","f796e660","f896e660","f996e660","fa96e660","fb96e660","fc96e660","fd96e660","fe96e660","ff96e660","8097e660","8197e660","8297e660","8397e660","8497e660","8597e660","8697e660","8797e660","8897e660","8997e660","8a97e660","8b97e660","8c97e660","8d97e660","8e97e660","8f97e660","9097e660","9197e660","9297e660","9397e660","9497e660","9597e660","9697e660","9797e660","9897e660","9997e660","9a97e660","9b97e660","9c97e660","9d97e660","9e97e660","9f97e660","a097e660","a197e660","a297e660","a397e660","a497e660","a597e660","a697e660","a797e660","a897e660","a997e660","aa97e660","ab97e660","ac97e660","ad97e660","ae97e660","af97e660","b097e660","b197e660","b297e660","b397e660","b497e660","b597e660","b697e660","b797e660","b897e660","b997e660","ba97e660","bb97e660","bc97e660","bd97e660","be97e660","bf97e660","c097e660","c197e660","c297e660","c397e660","c497e660","c597e660","c697e660","c797e660","c897e660","c997e660","ca97e660","cb97e660","cc97e660","cd97e660","ce97e660","cf97e660","d097e660","d197e660","d297e660","d397e660","d497e660","d597e660","d697e660","d797e660","d897e660","d997e660","da97e660","db97e660","dc97e660","dd97e660","de97e660","df97e660","e097e660","e197e660","e297e660","e397e660","e497e660","e597e660","e697e660","e797e660","e897e660","e997e660","ea97e660","eb97e660","ec97e660","ed97e660","ee97e660","ef97e660","f097e660","f197e660","f297e660","f397e660","f497e660","f597e660","f697e660","fa97e660","fb97e660","fc97e660","fd97e660","fe97e660","ff97e660","8098e660","8198e660","8298e660","8398e660","8498e660","8598e660","8698e660","8798e660","8898e660","8998e660","8a98e660","8b98e660","8c98e660","8d98e660","8e98e660","8f98e660","9098e660","9198e660","9298e660","9398e660","9498e660","9598e660","9698e660","9798e660","9898e660","9998e660","9a98e660","9b98e660","9c98e660","9d98e660","9e98e660","9f98e660","a098e660","a198e660","a298e660","a398e660","a498e660","a598e660","a698e660","a798e660","a898e660","a998e660","aa98e660","ab98e660","ac98e660","ad98e660","ae98e660","af98e660","b098e660","b198e660","b298e660","b398e660","b498e660","b598e660","b698e660","b798e660","b898e660","b998e660","ba98e660","bb98e660","bc98e660","bd98e660","be98e660","bf98e660","c098e660","c198e660","c298e660","c398e660","c498e660","c598e660","c698e660","c798e660","c898e660","c998e660","ca98e660","cb98e660","cc98e660","cd98e660","ce98e660","cf98e660","d098e660","d198e660","d298e660","d398e660","d498e660","d598e660","d698e660","d798e660","d898e660","d998e660","da98e660","db98e660","dc98e660","dd98e660","de98e660","df98e660","e098e660","e198e660","e298e660","e398e660","e498e660","e598e660","e698e660","e798e660","e898e660","e998e660","ea98e660","eb98e660","ec98e660","ed98e660","ee98e660","ef98e660","f098e660","f198e660","f298e660","f398e660","f498e660","f598e660","f698e660","f798e660","f898e660","f998e660","fa98e660","fb98e660","fc98e660","fd98e660","fe98e660","ff98e660","8099e660","8199e660","8299e660","8399e660","8499e660","8599e660","8699e660","8799e660","8899e660","8999e660","8a99e660","8b99e660","8c99e660","8d99e660","8e99e660","8f99e660","9099e660","9199e660","9299e660","9399e660","9499e660","9599e660","9699e660","9799e660","9899e660","9999e660","9a99e660","9b99e660","9c99e660","9d99e660","9e99e660","9f99e660","a099e660","a199e660","a299e660","a399e660","a499e660","a599e660","a699e660","a799e660","a899e660","a999e660","aa99e660","ab99e660","ac99e660","ad99e660","ae99e660","af99e660","b199e660","b299e660","b399e660","b499e660","b599e660","b699e660","b799e660","b899e660","b999e660","ba99e660","bb99e660","bc99e660","bd99e660","be99e660","bf99e660","c099e660","c199e660","c299e660","c399e660","c499e660","c599e660","c699e660","c799e660","c899e660","c999e660","ca99e660","cb99e660","cc99e660","cd99e660","ce99e660","cf99e660","d099e660","d199e660","d299e660","d399e660","d499e660","d599e660","d699e660","d799e660","d899e660","d999e660","da99e660","db99e660","dc99e660","dd99e660","de99e660","df99e660","e099e660","e199e660","e299e660","e399e660","e499e660","e599e660","e699e660","e799e660","e899e660","e999e660","ea99e660","eb99e660","ec99e660","ed99e660","ee99e660","ef99e660","f099e660","f199e660","f299e660","f399e660","f499e660","f599e660","f699e660","f799e660","f899e660","f999e660","fa99e660","fb99e660","fc99e660","fd99e660","fe99e660","ff99e660","809ae660","819ae660","829ae660","839ae660","849ae660","859ae660","869ae660","879ae660","889ae660","899ae660","8a9ae660","8b9ae660","8c9ae660","8d9ae660","8e9ae660","8f9ae660","909ae660","919ae660","929ae660","939ae660","949ae660","959ae660","969ae660","979ae660","989ae660","999ae660","9a9ae660","9b9ae660","9c9ae660","9d9ae660","9e9ae660","9f9ae660","a09ae660","a19ae660","a29ae660","a39ae660","a49ae660","a59ae660","a69ae660","a79ae660","a89ae660","a99ae660","aa9ae660","ab9ae660","ac9ae660","ad9ae660","ae9ae660","af9ae660","b09ae660","b19ae660","b29ae660","b39ae660","b49ae660","b59ae660","b69ae660","b79ae660","b89ae660","b99ae660","ba9ae660","bb9ae660","bc9ae660","bd9ae660","be9ae660","bf9ae660","c09ae660","c19ae660","c29ae660","c39ae660","c49ae660","c59ae660","c69ae660","c79ae660","c89ae660","c99ae660","ca9ae660","cb9ae660","cc9ae660","cd9ae660","ce9ae660","cf9ae660","d09ae660","d19ae660","d29ae660","d39ae660","d49ae660","d59ae660","d69ae660","d79ae660","d89ae660","d99ae660","da9ae660","db9ae660","dc9ae660","dd9ae660","de9ae660","df9ae660","e09ae660","e19ae660","e29ae660","e39ae660","e49ae660","e59ae660","e69ae660","e79ae660","e89ae660","e99ae660","ea9ae660","eb9ae660","ec9ae660","ed9ae660","ee9ae660","ef9ae660","f09ae660","f19ae660","f49ae660","f59ae660","f69ae660","f79ae660","f89ae660","f99ae660","fa9ae660","fb9ae660","fc9ae660","fd9ae660","fe9ae660","ff9ae660","829be660","839be660","849be660","859be660","869be660","879be660","889be660","899be660","8a9be660","8b9be660","8c9be660","8d9be660","8e9be660","8f9be660","909be660","919be660","929be660","939be660","949be660","959be660","969be660","979be660","989be660","999be660","9a9be660","9b9be660","9c9be660","9d9be660","9e9be660","9f9be660","a09be660","a19be660","a29be660","a39be660","a49be660","a59be660","a69be660","a79be660","a89be660","a99be660","aa9be660","ab9be660","ac9be660","ad9be660","ae9be660","af9be660","b09be660","b19be660","b29be660","b39be660","b49be660","b59be660","b69be660","b79be660","b89be660","b99be660","ba9be660","bb9be660","bc9be660","bd9be660","be9be660","bf9be660","c09be660","c19be660","c29be660","c39be660","c49be660","c59be660","c69be660","c79be660","c89be660","c99be660","ca9be660","cb9be660","cc9be660","cd9be660","ce9be660","cf9be660","d09be660","d19be660","d29be660","d39be660","d49be660","d59be660","d69be660","d79be660","d89be660","d99be660","da9be660","db9be660","dc9be660","dd9be660","de9be660","df9be660","e09be660","e19be660","e29be660","e39be660","e49be660","e59be660","e69be660","e79be660","e89be660","e99be660","ea9be660","eb9be660","ec9be660","ed9be660","ee9be660","ef9be660","f09be660","f19be660","f29be660","f39be660","f49be660","f59be660","f69be660","f79be660","f89be660","f99be660","fa9be660","fb9be660","fc9be660","fd9be660","fe9be660","ff9be660","809ce660","819ce660","829ce660","839ce660","849ce660","859ce660","869ce660","879ce660","889ce660","8a9ce660","8b9ce660","8c9ce660","8d9ce660","8e9ce660","8f9ce660","909ce660","a993e860","aa93e860","ab93e860","ac93e860","ad93e860","ae93e860","af93e860","b093e860","b193e860","b293e860","b393e860","b493e860","b593e860","b693e860","b793e860","b893e860","b993e860","ba93e860","bb93e860","bc93e860","bd93e860","be93e860","bf93e860","c093e860","c193e860","c293e860","c393e860","c493e860","c593e860","c693e860","c793e860","c893e860","c993e860","ca93e860","cb93e860","cc93e860","cd93e860","ce93e860","cf93e860","d193e860","d293e860","d393e860","d493e860","d593e860","d693e860","d793e860","d893e860","d993e860","da93e860","db93e860","dc93e860","dd93e860","de93e860","df93e860","e093e860","e193e860","e293e860","e393e860","e493e860","e593e860","e693e860","e793e860","e893e860","e993e860","ea93e860","eb93e860","ec93e860","ed93e860","919be860","929be860","939be860","959be860","969be860","979be860","989be860","999be860","9a9be860","9b9be860","9d9be860","9e9be860","9f9be860","a09be860","a19be860","a29be860","a39be860","a49be860","a59be860","a69be860","a79be860","a89be860","a99be860","aa9be860","ab9be860","ac9be860","ad9be860","ae9be860","af9be860","b09be860","b19be860","b29be860","b39be860","b49be860","b59be860","b69be860","b79be860","b89be860","b99be860","ba9be860","bb9be860","bc9be860","bd9be860","be9be860","bf9be860","c09be860","c19be860","c29be860","c39be860","c49be860","c59be860","c69be860","c79be860","c89be860","c99be860","ca9be860","f9a2e860","faa2e860","fba2e860","fca2e860","fda2e860","fea2e860","ffa2e860","80a3e860","81a3e860","82a3e860","83a3e860","84a3e860","85a3e860","86a3e860","87a3e860","88a3e860","89a3e860","8aa3e860","8ba3e860","8ca3e860","8da3e860","8ea3e860","8fa3e860","90a3e860","91a3e860","92a3e860","93a3e860","94a3e860","95a3e860","96a3e860","97a3e860","98a3e860","99a3e860","9aa3e860","9ba3e860","9ca3e860","9da3e860","9ea3e860","9fa3e860","a0a3e860","a1a3e860","a2a3e860","a3a3e860","a4a3e860","a5a3e860","a6a3e860","a7a3e860","a8a3e860","a9a3e860","aaa3e860","aba3e860","aca3e860","ada3e860","aea3e860","afa3e860","b0a3e860","b1a3e860","b2a3e860","b3a3e860","b4a3e860","b5a3e860","e0aae860","e1aae860","e2aae860","e3aae860","e4aae860","e5aae860","e6aae860","e7aae860","e8aae860","e9aae860","eaaae860","ebaae860","ecaae860","edaae860","eeaae860","efaae860","f0aae860","f1aae860","f2aae860","f3aae860","f4aae860","f5aae860","f6aae860","f7aae860","f8aae860","f9aae860","faaae860","fbaae860","fcaae860","fdaae860","feaae860","ffaae860","80abe860","81abe860","82abe860","83abe860","84abe860","85abe860","86abe860","87abe860","88abe860","89abe860","8aabe860","8babe860","8cabe860","8dabe860","8eabe860","8fabe860","90abe860","91abe860","92abe860","95abe860","c8b2e860","c9b2e860","cab2e860","cbb2e860","ceb2e860","cfb2e860","d0b2e860","d1b2e860","d2b2e860","d3b2e860","d4b2e860","d5b2e860","d6b2e860","d7b2e860","d8b2e860","d9b2e860","dab2e860","dbb2e860","dcb2e860","ddb2e860","deb2e860","dfb2e860","e1b2e860","e2b2e860","e3b2e860","e4b2e860","e5b2e860","e6b2e860","e7b2e860","e8b2e860","e9b2e860","eab2e860","ebb2e860","ecb2e860","edb2e860","eeb2e860","efb2e860","f0b2e860","f1b2e860","f3b2e860","f6b2e860","f7b2e860","f8b2e860","f9b2e860","fab2e860","fbb2e860","fcb2e860","fdb2e860","feb2e860","ffb2e860","80b3e860","81b3e860","82b3e860","83b3e860","84b3e860","85b3e860","86b3e860","adbae860","aebae860","afbae860","b0bae860","b1bae860","b2bae860","b3bae860","b4bae860","b5bae860","b6bae860","b7bae860","b8bae860","b9bae860","babae860","bbbae860","bcbae860","bdbae860","bebae860","bfbae860","c0bae860","c1bae860","c2bae860","c3bae860","c4bae860","c5bae860","c6bae860","c7bae860","c8bae860","c9bae860","cdbae860","cebae860","cfbae860","d0bae860","d1bae860","d2bae860","d3bae860","d5bae860","d6bae860","d7bae860","d8bae860","d9bae860","dabae860","dcbae860","ddbae860","debae860","dfbae860","e0bae860","e1bae860","e2bae860","e3bae860","e4bae860","e8bae860","e9bae860","eabae860","ebbae860","ecbae860","edbae860","eebae860","efbae860","f0bae860","f1bae860","98c2e860","99c2e860","9ac2e860","9bc2e860","9cc2e860","9dc2e860","9ec2e860","9fc2e860","a0c2e860","a1c2e860","a2c2e860","a3c2e860","a4c2e860","a5c2e860","a6c2e860","a7c2e860","a8c2e860","a9c2e860","aac2e860","abc2e860","acc2e860","adc2e860","aec2e860","afc2e860","b0c2e860","b1c2e860","b2c2e860","b3c2e860","b4c2e860","b5c2e860","b6c2e860","b7c2e860","b8c2e860","b9c2e860","bec2e860","bfc2e860","c0c2e860","c1c2e860","c2c2e860","c3c2e860","c4c2e860","c5c2e860","c6c2e860","c7c2e860","c8c2e860","c9c2e860","cac2e860","cbc2e860","ccc2e860","cdc2e860","cec2e860","cfc2e860","d0c2e860","d1c2e860","80cae860","81cae860","82cae860","83cae860","84cae860","85cae860","86cae860","87cae860","88cae860","89cae860","8acae860","8bcae860","8ccae860","8dcae860","8ecae860","8fcae860","90cae860","91cae860","92cae860","93cae860","94cae860","95cae860","96cae860","97cae860","98cae860","99cae860","9acae860","9bcae860","9ccae860","9dcae860","9ecae860","9fcae860","a0cae860","a1cae860","a2cae860","a3cae860","a4cae860","a5cae860","a6cae860","a7cae860","a8cae860","a9cae860","aacae860","abcae860","accae860","adcae860","e8d1e860","e9d1e860","ead1e860","ebd1e860","ecd1e860","edd1e860","eed1e860","efd1e860","f0d1e860","f1d1e860","f2d1e860","f3d1e860","f4d1e860","f5d1e860","f6d1e860","f7d1e860","f8d1e860","f9d1e860","fad1e860","fbd1e860","fcd1e860","fdd1e860","fed1e860","ffd1e860","80d2e860","81d2e860","82d2e860","83d2e860","84d2e860","85d2e860","86d2e860","87d2e860","88d2e860","89d2e860","8ad2e860","8bd2e860","8cd2e860","8dd2e860","8ed2e860","8fd2e860","90d2e860","91d2e860","92d2e860","93d2e860","94d2e860","95d2e860","96d2e860","d0d9e860","d1d9e860","d2d9e860","d3d9e860","d4d9e860","d5d9e860","d6d9e860","d7d9e860","d8d9e860","d9d9e860","dad9e860","dbd9e860","dcd9e860","ddd9e860","ded9e860","dfd9e860","e0d9e860","e1d9e860","e2d9e860","e3d9e860","e4d9e860","e5d9e860","e6d9e860","e7d9e860","e8d9e860","e9d9e860","ead9e860","ebd9e860","ecd9e860","edd9e860","eed9e860","efd9e860","f0d9e860","f1d9e860","f2d9e860","b8e1e860","b9e1e860","bae1e860","bbe1e860","bce1e860","bde1e860","bee1e860","bfe1e860","c0e1e860","c1e1e860","c2e1e860","c3e1e860","c4e1e860","c5e1e860","c6e1e860","c7e1e860","c8e1e860","c9e1e860","cae1e860","cbe1e860","cce1e860","cde1e860","cee1e860","cfe1e860","d0e1e860","d1e1e860","d2e1e860","d3e1e860","d4e1e860","d5e1e860","d6e1e860","d7e1e860","d8e1e860","d9e1e860","dae1e860","dbe1e860","dce1e860","dde1e860","dee1e860","dfe1e860","e0e1e860","e1e1e860","e2e1e860","a0e9e860","a1e9e860","a2e9e860","a3e9e860","a4e9e860","a5e9e860","a6e9e860","a7e9e860","a8e9e860","a9e9e860","aae9e860","abe9e860","ace9e860","ade9e860","aee9e860","afe9e860","b0e9e860","b1e9e860","b2e9e860","b3e9e860","b4e9e860","b5e9e860","b6e9e860","b7e9e860","b8e9e860","b9e9e860","bae9e860","bbe9e860","bce9e860","bde9e860","bee9e860","88f1e860","89f1e860","8af1e860","8bf1e860","8cf1e860","8df1e860","8ef1e860","8ff1e860","90f1e860","91f1e860","92f1e860","93f1e860","94f1e860","95f1e860","96f1e860","97f1e860","98f1e860","99f1e860","9af1e860","9bf1e860","9cf1e860","9df1e860","9ef1e860","9ff1e860","a0f1e860","a1f1e860","a2f1e860","a3f1e860","a4f1e860","a5f1e860","a6f1e860","a7f1e860","a8f1e860","a9f1e860","aaf1e860","abf1e860","acf1e860","adf1e860","aef1e860","aff1e860","f0f8e860","f1f8e860","f2f8e860","f3f8e860","f4f8e860","f5f8e860","f6f8e860","f7f8e860","f8f8e860","f9f8e860","faf8e860","fbf8e860","fcf8e860","fdf8e860","fef8e860","fff8e860","80f9e860","81f9e860","82f9e860","83f9e860","84f9e860","85f9e860","86f9e860","87f9e860","88f9e860","89f9e860","8af9e860","8bf9e860","8cf9e860","8df9e860","8ef9e860","8ff9e860","90f9e860","91f9e860","92f9e860","94f9e860","95f9e860","96f9e860","97f9e860","98f9e860","99f9e860","9af9e860","9bf9e860","9cf9e860","9df9e860","9ef9e860","9ff9e860","a0f9e860","a1f9e860","a2f9e860","a3f9e860","a4f9e860","a5f9e860","a6f9e860","a7f9e860","a8f9e860","a9f9e860","aaf9e860","abf9e860","acf9e860","adf9e860","aef9e860","aff9e860","b0f9e860","b1f9e860","d880e960","d980e960","da80e960","db80e960","dc80e960","dd80e960","de80e960","df80e960","e080e960","e180e960","e280e960","e380e960","e480e960","e580e960","e680e960","e780e960","e880e960","e980e960","ea80e960","eb80e960","ec80e960","ee80e960","ef80e960","f080e960","f180e960","f280e960","f380e960","f480e960","f580e960","f680e960","f780e960","f880e960","f980e960","fa80e960","fb80e960","fc80e960","c088e960","c188e960","c288e960","c388e960","c488e960","c588e960","c688e960","c788e960","c888e960","c988e960","ca88e960","cb88e960","cc88e960","cd88e960","ce88e960","cf88e960","d088e960","d188e960","d288e960","d388e960","d488e960","d588e960","d688e960","d788e960","d888e960","d988e960","da88e960","db88e960","dc88e960","dd88e960","de88e960","df88e960","e088e960","e188e960","e288e960","e388e960","e488e960","e588e960","e688e960","e788e960","e888e960","e988e960","ea88e960","eb88e960","ec88e960","a890e960","a990e960","aa90e960","ab90e960","ac90e960","ad90e960","ae90e960","af90e960","b090e960","b190e960","b290e960","b390e960","b490e960","b590e960","b690e960","b790e960","b890e960","b990e960","ba90e960","bb90e960","bc90e960","bd90e960","be90e960","bf90e960","c090e960","c190e960","c290e960","c390e960","c490e960","c590e960","c690e960","c790e960","c890e960","c990e960","ca90e960","cb90e960","cc90e960","cd90e960","ce90e960","cf90e960","d090e960","d190e960","d290e960","d390e960","d490e960","d590e960","d690e960","9098e960","9198e960","9298e960","9398e960","9498e960","9598e960","9698e960","9798e960","9898e960","9998e960","9a98e960","9b98e960","9c98e960","9d98e960","9e98e960","9f98e960","a098e960","a198e960","a298e960","a398e960","a498e960","a598e960","a698e960","a798e960","a898e960","a998e960","aa98e960","ab98e960","ac98e960","ad98e960","ae98e960","af98e960","b098e960","b198e960","b298e960","b398e960","b498e960","b598e960","b698e960","b798e960","b898e960","b998e960","ea98e960","eb98e960","ec98e960","ed98e960","ee98e960","ef98e960","f098e960","f198e960","8096a361","8196a361","8296a361","8396a361","8496a361","8596a361","8696a361","8796a361","8896a361","8996a361","8a96a361","8b96a361","8c96a361","8d96a361","8e96a361","8f96a361","9096a361","9196a361","9296a361","9396a361","9496a361","9596a361","9696a361","9796a361","9896a361","9996a361","9a96a361","9b96a361","9c96a361","9d96a361","9e96a361","9f96a361","a096a361","a196a361","a296a361","a396a361","a496a361","a596a361","a696a361","a796a361","a896a361","a996a361","aa96a361","ab96a361","ac96a361","ad96a361","ae96a361","af96a361","b096a361","b196a361","b296a361","b396a361","b496a361","b596a361","b696a361","b796a361","b896a361","b996a361","ba96a361","bb96a361","bc96a361","bd96a361","be96a361","bf96a361","c096a361","c196a361","c296a361","c396a361","c496a361","c596a361","c696a361","c796a361","c896a361","c996a361","ca96a361","cb96a361","cc96a361","cd96a361","ce96a361","cf96a361","d096a361","d196a361","d296a361","d396a361","d496a361","d596a361","d696a361","d796a361","d896a361","d996a361","da96a361","db96a361","dc96a361","dd96a361","de96a361","df96a361","e096a361","e196a361","e396a361","e496a361","e596a361","e696a361","e796a361","e896a361","e996a361","ea96a361","eb96a361","ec96a361","ed96a361","ee96a361","ef96a361","f096a361","f196a361","f296a361","f396a361","f496a361","f596a361","f696a361","f796a361","f896a361","f996a361","fa96a361","fb96a361","fc96a361","fd96a361","fe96a361","ff96a361","8097a361","8197a361","8297a361","8397a361","8497a361","8597a361","8697a361","8797a361","8897a361","8997a361","8a97a361","8b97a361","8c97a361","8d97a361","8e97a361","8f97a361","9097a361","9197a361","9297a361","9397a361","9497a361","9597a361","9697a361","9797a361","9897a361","9997a361","9a97a361","9b97a361","9c97a361","9d97a361","9e97a361","9f97a361","a097a361","a197a361","a297a361","a397a361","a497a361","a597a361","a697a361","a797a361","a897a361","a997a361","aa97a361","ab97a361","ac97a361","ad97a361","ae97a361","af97a361","b097a361","b197a361","b297a361","b397a361","b497a361","b597a361","b697a361","b797a361","b897a361","b997a361","ba97a361","bb97a361","bc97a361","bd97a361","be97a361","bf97a361","c097a361","c197a361","c297a361","c397a361","c497a361","c597a361","c697a361","c797a361","c897a361","c997a361","ca97a361","cb97a361","cc97a361","cd97a361","ce97a361","cf97a361","d097a361","d197a361","d297a361","d397a361","d497a361","d597a361","d697a361","d797a361","d897a361","d997a361","da97a361","db97a361","dc97a361","dd97a361","de97a361","df97a361","e097a361","e197a361","e297a361","e397a361","e497a361","e597a361","e697a361","e797a361","e897a361","e997a361","ea97a361","eb97a361","ec97a361","ed97a361","ee97a361","ef97a361","f097a361","f197a361","f297a361","f397a361","f497a361","f597a361","f697a361","f797a361","f897a361","f997a361","fa97a361","fb97a361","fc97a361","fd97a361","fe97a361","ff97a361","8098a361","8198a361","8298a361","8398a361","8498a361","8598a361","8698a361","8798a361","8898a361","8998a361","8a98a361","8b98a361","8c98a361","8d98a361","8e98a361","8f98a361","9098a361","9198a361","9298a361","9398a361","9498a361","9598a361","9698a361","9798a361","9898a361","9998a361","9a98a361","9b98a361","9c98a361","9d98a361","9e98a361","9f98a361","a098a361","a198a361","a298a361","a398a361","a498a361","a598a361","a698a361","a798a361","a898a361","a998a361","aa98a361","ab98a361","ac98a361","ad98a361","ae98a361","af98a361","b098a361","b198a361","b298a361","b398a361","b498a361","b598a361","b698a361","b798a361","b898a361","b998a361","ba98a361","bb98a361","bc98a361","bd98a361","be98a361","bf98a361","c098a361","c198a361","c298a361","c398a361","c498a361","c598a361","c698a361","c798a361","c898a361","c998a361","ca98a361","cb98a361","cc98a361","cd98a361","ce98a361","cf98a361","d098a361","d198a361","d298a361","d398a361","d498a361","d598a361","d698a361","d798a361","d898a361","d998a361","da98a361","db98a361","dc98a361","dd98a361","de98a361","df98a361","e098a361","e198a361","e298a361","e398a361","e498a361","e598a361","e698a361","e798a361","e898a361","e998a361","ea98a361","eb98a361","ec98a361","ed98a361","ee98a361","ef98a361","f098a361","f198a361","f298a361","f398a361","f498a361","f698a361","f798a361","f898a361","f998a361","fa98a361","fb98a361","fc98a361","fd98a361","fe98a361","ff98a361","8099a361","8199a361","8299a361","8399a361","8499a361","8599a361","8699a361","8799a361","8899a361","8999a361","8a99a361","8b99a361","8c99a361","8d99a361","8e99a361","8f99a361","9099a361","9199a361","9299a361","9399a361","9499a361","9599a361","9699a361","9799a361","9899a361","9999a361","9a99a361","9b99a361","9c99a361","9d99a361","9e99a361","9f99a361","a099a361","a199a361","a299a361","a399a361","a499a361","a599a361","a699a361","a799a361","a899a361","a999a361","aa99a361","ab99a361","ac99a361","ad99a361","ae99a361","af99a361","b099a361","b199a361","b299a361","b399a361","b499a361","b599a361","b699a361","b799a361","b899a361","b999a361","ba99a361","bb99a361","bc99a361","bd99a361","be99a361","bf99a361","c099a361","c199a361","c299a361","c399a361","c499a361","c599a361","c699a361","c799a361","c899a361","c999a361","ca99a361","cb99a361","cc99a361","cd99a361","ce99a361","cf99a361","d099a361","d199a361","d299a361","d399a361","d499a361","d599a361","d699a361","d799a361","d899a361","d999a361","da99a361","db99a361","dc99a361","dd99a361","de99a361","df99a361","e099a361","e199a361","e299a361","e399a361","e499a361","e599a361","e699a361","e799a361","e899a361","e999a361","ea99a361","eb99a361","ec99a361","ed99a361","ee99a361","ef99a361","f099a361","f199a361","f299a361","f399a361","f499a361","f599a361","f699a361","f799a361","f899a361","f999a361","fa99a361","fb99a361","fc99a361","fd99a361","fe99a361","ff99a361","809aa361","819aa361","829aa361","839aa361","849aa361","859aa361","869aa361","879aa361","889aa361","899aa361","8a9aa361","8b9aa361","8c9aa361","8d9aa361","8e9aa361","8f9aa361","909aa361","919aa361","929aa361","939aa361","949aa361","959aa361","969aa361","979aa361","989aa361","999aa361","9a9aa361","9b9aa361","9c9aa361","9d9aa361","9e9aa361","9f9aa361","a09aa361","a19aa361","a29aa361","a39aa361","a49aa361","a59aa361","a69aa361","a79aa361","a89aa361","a99aa361","aa9aa361","ab9aa361","ac9aa361","ad9aa361","ae9aa361","af9aa361","b09aa361","b19aa361","b29aa361","b39aa361","b49aa361","b59aa361","b69aa361","b79aa361","b89aa361","b99aa361","ba9aa361","bb9aa361","bc9aa361","bd9aa361","be9aa361","bf9aa361","c09aa361","c19aa361","c29aa361","c39aa361","c49aa361","c59aa361","c69aa361","c79aa361","c89aa361","c99aa361","ca9aa361","cb9aa361","cc9aa361","cd9aa361","ce9aa361","cf9aa361","d09aa361","d19aa361","d29aa361","d39aa361","d49aa361","d59aa361","d69aa361","d79aa361","d89aa361","d99aa361","da9aa361","db9aa361","dc9aa361","dd9aa361","de9aa361","df9aa361","e09aa361","e19aa361","e29aa361","e39aa361","e49aa361","e59aa361","e69aa361","e79aa361","e89aa361","e99aa361","ea9aa361","eb9aa361","ec9aa361","ed9aa361","ee9aa361","ef9aa361","f09aa361","f19aa361","f29aa361","f39aa361","f49aa361","f59aa361","f69aa361","f79aa361","f89aa361","f99aa361","fa9aa361","fb9aa361","fc9aa361","fd9aa361","fe9aa361","ff9aa361","809ba361","819ba361","829ba361","839ba361","849ba361","859ba361","869ba361","879ba361","889ba361","899ba361","8a9ba361","8b9ba361","8c9ba361","8d9ba361","8e9ba361","8f9ba361","909ba361","919ba361","929ba361","939ba361","949ba361","959ba361","969ba361","979ba361","989ba361","999ba361","9a9ba361","9b9ba361","9c9ba361","9d9ba361","9e9ba361","9f9ba361","a09ba361","a19ba361","a29ba361","a39ba361","a49ba361","a59ba361","a69ba361","a79ba361","a89ba361","a99ba361","ab9ba361","ac9ba361","ad9ba361","ae9ba361","af9ba361","b09ba361","b19ba361","b49ba361","b59ba361","b69ba361","b79ba361","b89ba361","b99ba361","ba9ba361","bb9ba361","bc9ba361","bd9ba361","be9ba361","bf9ba361","c09ba361","c19ba361","c29ba361","c39ba361","c49ba361","c59ba361","c69ba361","c79ba361","c89ba361","c99ba361","ca9ba361","cb9ba361","cc9ba361","cd9ba361","ce9ba361","cf9ba361","d09ba361","d19ba361","d29ba361","d39ba361","d49ba361","d59ba361","d69ba361","d79ba361","d89ba361","d99ba361","da9ba361","db9ba361","dc9ba361","dd9ba361","de9ba361","df9ba361","e09ba361","e19ba361","e29ba361","e39ba361","e49ba361","e59ba361","e69ba361","e79ba361","e89ba361","e99ba361","ea9ba361","eb9ba361","ec9ba361","ed9ba361","ee9ba361","ef9ba361","f09ba361","f19ba361","f29ba361","f39ba361","f49ba361","f59ba361","f69ba361","f79ba361","f89ba361","f99ba361","fa9ba361","fb9ba361","fc9ba361","fd9ba361","fe9ba361","ff9ba361","809ca361","819ca361","829ca361","839ca361","849ca361","859ca361","869ca361","879ca361","889ca361","899ca361","8a9ca361","8b9ca361","8c9ca361","8d9ca361","8e9ca361","8f9ca361","909ca361","919ca361","929ca361","939ca361","949ca361","959ca361","969ca361","979ca361","989ca361","999ca361","9a9ca361","9b9ca361","9c9ca361","9d9ca361","9e9ca361","9f9ca361","a09ca361","a19ca361","a29ca361","a39ca361","a49ca361","a59ca361","a69ca361","a79ca361","a89ca361","a99ca361","aa9ca361","ab9ca361","ac9ca361","ad9ca361","ae9ca361","af9ca361","b09ca361","b19ca361","b29ca361","b39ca361","b49ca361","b59ca361","b69ca361","b79ca361","b89ca361","b99ca361","ba9ca361","bb9ca361","bc9ca361","bd9ca361","be9ca361","bf9ca361","c09ca361","c19ca361","c29ca361","c39ca361","c49ca361","c59ca361","c89ca361","c99ca361","ca9ca361","cb9ca361","cc9ca361","cd9ca361","ce9ca361","cf9ca361","d09ca361","d19ca361","d29ca361","d39ca361","d69ca361","d79ca361","d89ca361","d99ca361","da9ca361","db9ca361","dc9ca361","dd9ca361","de9ca361","df9ca361","e09ca361","e19ca361","e29ca361","e39ca361","e49ca361","e59ca361","e69ca361","e79ca361","e89ca361","e99ca361","ea9ca361","eb9ca361","ec9ca361","ed9ca361","ee9ca361","ef9ca361","f09ca361","f19ca361","f29ca361","f39ca361","f49ca361","f59ca361","f69ca361","f79ca361","f89ca361","f99ca361","fa9ca361","fb9ca361","fc9ca361","fd9ca361","fe9ca361","ff9ca361","809da361","819da361","829da361","839da361","849da361","859da361","869da361","879da361","889da361","899da361","8a9da361","8b9da361","8c9da361","8d9da361","8e9da361","8f9da361","909da361","919da361","929da361","939da361","949da361","959da361","969da361","979da361","989da361","999da361","9a9da361","9b9da361","9c9da361","9d9da361","9e9da361","9f9da361","a09da361","a19da361","a29da361","a39da361","a49da361","a59da361","a69da361","a79da361","a89da361","a99da361","aa9da361","ab9da361","ac9da361","ad9da361","ae9da361","af9da361","b09da361","b19da361","b29da361","b39da361","b49da361","b59da361","b69da361","b79da361","b89da361","b99da361","ba9da361","bb9da361","bc9da361","bd9da361","be9da361","bf9da361","c09da361","c19da361","c29da361","c39da361","c49da361","c59da361","c69da361","c79da361","c99da361","ca9da361","cb9da361","cc9da361","e997a561","ea97a561","eb97a561","ec97a561","ed97a561","ee97a561","ef97a561","f097a561","f197a561","f297a561","f397a561","f497a561","f597a561","f697a561","f797a561","f897a561","f997a561","fa97a561","fb97a561","fc97a561","fd97a561","fe97a561","ff97a561","8098a561","8198a561","8298a561","8398a561","8498a561","8598a561","8698a561","8898a561","8998a561","8a98a561","8b98a561","8c98a561","8e98a561","8f98a561","9098a561","9198a561","9298a561","9398a561","9498a561","9598a561","9698a561","9798a561","9898a561","d19fa561","d29fa561","d49fa561","d59fa561","d69fa561","d79fa561","d89fa561","d99fa561","da9fa561","db9fa561","dc9fa561","dd9fa561","de9fa561","df9fa561","e09fa561","e19fa561","e29fa561","e39fa561","e49fa561","e59fa561","e69fa561","e79fa561","e89fa561","e99fa561","ea9fa561","eb9fa561","ec9fa561","ed9fa561","ee9fa561","ef9fa561","f09fa561","f19fa561","f29fa561","f39fa561","f49fa561","f59fa561","f69fa561","f79fa561","f89fa561","f99fa561","fa9fa561","fb9fa561","fc9fa561","fd9fa561","fe9fa561","ff9fa561","80a0a561","81a0a561","82a0a561","b9a7a561","baa7a561","bba7a561","bca7a561","bda7a561","bea7a561","bfa7a561","c0a7a561","c1a7a561","c2a7a561","c3a7a561","c4a7a561","c5a7a561","c6a7a561","c7a7a561","c8a7a561","c9a7a561","caa7a561","cba7a561","cca7a561","cda7a561","cea7a561","cfa7a561","d0a7a561","d1a7a561","d2a7a561","d3a7a561","d4a7a561","d5a7a561","d6a7a561","d7a7a561","d8a7a561","d9a7a561","daa7a561","dba7a561","dca7a561","dda7a561","dea7a561","dfa7a561","e0a7a561","e1a7a561","e2a7a561","e3a7a561","e4a7a561","e5a7a561","e6a7a561","e7a7a561","e8a7a561","a0afa561","a1afa561","a2afa561","a3afa561","a4afa561","a5afa561","a6afa561","a7afa561","a8afa561","a9afa561","aaafa561","abafa561","acafa561","adafa561","aeafa561","afafa561","b0afa561","b1afa561","b2afa561","b3afa561","b4afa561","b5afa561","b6afa561","b7afa561","b8afa561","b9afa561","baafa561","bbafa561","bcafa561","bdafa561","beafa561","bfafa561","c0afa561","c1afa561","c2afa561","c3afa561","c4afa561","c5afa561","c6afa561","c7afa561","c8afa561","c9afa561","ccafa561","88b7a561","89b7a561","8ab7a561","8bb7a561","8eb7a561","8fb7a561","90b7a561","91b7a561","92b7a561","93b7a561","94b7a561","95b7a561","96b7a561","97b7a561","98b7a561","99b7a561","9ab7a561","9bb7a561","9cb7a561","9db7a561","9eb7a561","9fb7a561","a1b7a561","a2b7a561","a3b7a561","a4b7a561","a5b7a561","a6b7a561","a7b7a561","a8b7a561","a9b7a561","aab7a561","abb7a561","acb7a561","adb7a561","aeb7a561","afb7a561","b0b7a561","b1b7a561","b2b7a561","b3b7a561","b4b7a561","b5b7a561","b6b7a561","b7b7a561","b8b7a561","b9b7a561","bab7a561","bbb7a561","bcb7a561","bdb7a561","beb7a561","8eb8a561","8fb8a561","edbea561","eebea561","efbea561","f0bea561","f1bea561","f2bea561","f3bea561","f4bea561","f5bea561","f6bea561","f7bea561","f8bea561","f9bea561","fabea561","fbbea561","fcbea561","fdbea561","febea561","ffbea561","80bfa561","81bfa561","82bfa561","83bfa561","84bfa561","85bfa561","87bfa561","8bbfa561","8cbfa561","8dbfa561","8fbfa561","90bfa561","92bfa561","93bfa561","94bfa561","95bfa561","97bfa561","98bfa561","99bfa561","9abfa561","9bbfa561","9cbfa561","9dbfa561","9ebfa561","a5bfa561","a6bfa561","a7bfa561","a8bfa561","a9bfa561","aabfa561","abbfa561","acbfa561","adbfa561","aebfa561","d8c6a561","d9c6a561","dac6a561","dbc6a561","dcc6a561","ddc6a561","dec6a561","dfc6a561","e0c6a561","e1c6a561","e2c6a561","e3c6a561","e4c6a561","e5c6a561","e6c6a561","e7c6a561","e8c6a561","e9c6a561","eac6a561","ebc6a561","ecc6a561","edc6a561","eec6a561","efc6a561","f0c6a561","f1c6a561","f2c6a561","f3c6a561","f4c6a561","f5c6a561","f6c6a561","f7c6a561","f8c6a561","f9c6a561","fec6a561","ffc6a561","80c7a561","81c7a561","82c7a561","83c7a561","84c7a561","85c7a561","86c7a561","87c7a561","88c7a561","89c7a561","8ac7a561","8bc7a561","8cc7a561","c0cea561","c1cea561","c2cea561","c3cea561","c4cea561","c5cea561","c6cea561","c7cea561","c8cea561","c9cea561","cacea561","cbcea561","cccea561","cdcea561","cecea561","cfcea561","d0cea561","d1cea561","d2cea561","d3cea561","d4cea561","d5cea561","d6cea561","d7cea561","d8cea561","d9cea561","dacea561","dbcea561","dccea561","ddcea561","decea561","dfcea561","e0cea561","e1cea561","e2cea561","e3cea561","e4cea561","e5cea561","e6cea561","e7cea561","e8cea561","e9cea561","eacea561","ebcea561","a8d6a561","a9d6a561","aad6a561","abd6a561","acd6a561","add6a561","aed6a561","afd6a561","b0d6a561","b1d6a561","b2d6a561","b3d6a561","b4d6a561","b5d6a561","b6d6a561","b7d6a561","b8d6a561","b9d6a561","bad6a561","bbd6a561","bcd6a561","bdd6a561","bed6a561","bfd6a561","c0d6a561","c1d6a561","c2d6a561","c3d6a561","c4d6a561","c5d6a561","c6d6a561","c7d6a561","c8d6a561","c9d6a561","cad6a561","cbd6a561","ccd6a561","cdd6a561","90dea561","91dea561","92dea561","93dea561","94dea561","95dea561","96dea561","97dea561","98dea561","99dea561","9adea561","9bdea561","9cdea561","9ddea561","9edea561","9fdea561","a0dea561","a1dea561","a2dea561","a3dea561","a4dea561","a5dea561","a6dea561","a7dea561","a8dea561","a9dea561","aadea561","abdea561","acdea561","addea561","aedea561","afdea561","f8e5a561","f9e5a561","fae5a561","fbe5a561","fce5a561","fde5a561","fee5a561","ffe5a561","80e6a561","81e6a561","82e6a561","83e6a561","84e6a561","85e6a561","86e6a561","87e6a561","88e6a561","89e6a561","8ae6a561","8be6a561","8ce6a561","8de6a561","8ee6a561","8fe6a561","90e6a561","91e6a561","92e6a561","93e6a561","94e6a561","95e6a561","96e6a561","97e6a561","98e6a561","99e6a561","9ae6a561","9be6a561","9ce6a561","9de6a561","9ee6a561","e0eda561","e1eda561","e2eda561","e3eda561","e4eda561","e5eda561","e6eda561","e7eda561","e8eda561","e9eda561","eaeda561","ebeda561","eceda561","ededa561","eeeda561","efeda561","f0eda561","f1eda561","f2eda561","f3eda561","f4eda561","f5eda561","f6eda561","f7eda561","f8eda561","f9eda561","faeda561","fbeda561","fceda561","c8f5a561","c9f5a561","caf5a561","cbf5a561","ccf5a561","cdf5a561","cef5a561","cff5a561","d0f5a561","d1f5a561","d2f5a561","d3f5a561","d4f5a561","d5f5a561","d6f5a561","d7f5a561","d8f5a561","d9f5a561","daf5a561","dbf5a561","dcf5a561","ddf5a561","def5a561","dff5a561","e0f5a561","e1f5a561","e2f5a561","e3f5a561","e4f5a561","b0fda561","b1fda561","b2fda561","b3fda561","b4fda561","b5fda561","b6fda561","b7fda561","b8fda561","b9fda561","bafda561","bbfda561","bcfda561","bdfda561","befda561","bffda561","c0fda561","c1fda561","c2fda561","c3fda561","c4fda561","c5fda561","c6fda561","c7fda561","c8fda561","c9fda561","cafda561","cbfda561","ccfda561","cdfda561","cefda561","cffda561","d0fda561","d1fda561","d2fda561","d3fda561","d4fda561","d5fda561","9885a661","9985a661","9a85a661","9b85a661","9c85a661","9d85a661","9e85a661","9f85a661","a085a661","a185a661","a285a661","a385a661","a485a661","a585a661","a685a661","a785a661","a885a661","a985a661","aa85a661","ab85a661","ac85a661","ae85a661","af85a661","b085a661","b185a661","b285a661","b385a661","b485a661","b585a661","b685a661","b785a661","808da661","818da661","828da661","838da661","848da661","858da661","868da661","878da661","888da661","898da661","8a8da661","8b8da661","8c8da661","8d8da661","8e8da661","8f8da661","908da661","918da661","928da661","938da661","948da661","958da661","968da661","978da661","988da661","998da661","9a8da661","9b8da661","9c8da661","9d8da661","9e8da661","9f8da661","a08da661","a18da661","a28da661","a38da661","a48da661","e894a661","e994a661","ea94a661","eb94a661","ec94a661","ed94a661","ee94a661","ef94a661","f094a661","f194a661","f294a661","f394a661","f494a661","f594a661","f694a661","f794a661","f894a661","f994a661","fa94a661","fb94a661","fc94a661","fd94a661","fe94a661","ff94a661","8095a661","8195a661","8295a661","8395a661","8495a661","8595a661","8695a661","8795a661","8895a661","d09ca661","d19ca661","d29ca661","d39ca661","d49ca661","d59ca661","d69ca661","d79ca661","d89ca661","d99ca661","da9ca661","db9ca661","dc9ca661","dd9ca661","de9ca661","df9ca661","e09ca661","e19ca661","e29ca661","e39ca661","e49ca661","e59ca661","e69ca661","e79ca661","e89ca661","e99ca661","ea9ca661","eb9ca661","ec9ca661","ed9ca661","ee9ca661","ef9ca661","f09ca661","f19ca661","f29ca661","aa9da661","ab9da661","ac9da661","ad9da661","ae9da661","af9da661","c09ae061","c19ae061","c29ae061","c39ae061","c49ae061","c59ae061","c69ae061","c79ae061","c89ae061","c99ae061","ca9ae061","cb9ae061","cc9ae061","cd9ae061","ce9ae061","cf9ae061","d09ae061","d19ae061","d29ae061","d39ae061","d49ae061","d59ae061","d69ae061","d79ae061","d89ae061","d99ae061","da9ae061","db9ae061","dc9ae061","dd9ae061","de9ae061","df9ae061","e09ae061","e19ae061","e29ae061","e39ae061","e49ae061","e59ae061","e69ae061","e79ae061","e89ae061","e99ae061","ea9ae061","eb9ae061","ec9ae061","ed9ae061","ee9ae061","ef9ae061","f09ae061","f19ae061","f29ae061","f39ae061","f49ae061","f59ae061","f69ae061","f79ae061","f89ae061","f99ae061","fa9ae061","fb9ae061","fc9ae061","fd9ae061","fe9ae061","ff9ae061","809be061","819be061","829be061","839be061","849be061","859be061","869be061","879be061","889be061","899be061","8a9be061","8b9be061","8d9be061","919be061","929be061","939be061","949be061","959be061","969be061","979be061","989be061","999be061","9a9be061","9b9be061","9c9be061","9d9be061","9e9be061","9f9be061","a19be061","a29be061","a39be061","a49be061","a59be061","a69be061","a79be061","a89be061","a99be061","aa9be061","ab9be061","ac9be061","ad9be061","ae9be061","af9be061","b09be061","b19be061","b29be061","b39be061","b49be061","b59be061","b69be061","b79be061","b89be061","b99be061","ba9be061","bb9be061","bc9be061","bd9be061","be9be061","bf9be061","c09be061","c19be061","c29be061","c39be061","c49be061","c59be061","c69be061","c79be061","c89be061","c99be061","ca9be061","cb9be061","cc9be061","cd9be061","ce9be061","cf9be061","d09be061","d19be061","d29be061","d39be061","d49be061","d59be061","d69be061","d79be061","d89be061","d99be061","da9be061","db9be061","dc9be061","dd9be061","de9be061","df9be061","e09be061","e19be061","e29be061","e39be061","e49be061","e59be061","e69be061","e79be061","e89be061","e99be061","ea9be061","eb9be061","ec9be061","ed9be061","ee9be061","ef9be061","f09be061","f19be061","f29be061","f39be061","f49be061","f59be061","f69be061","f79be061","f89be061","f99be061","fa9be061","fb9be061","fc9be061","fd9be061","fe9be061","ff9be061","809ce061","819ce061","829ce061","839ce061","849ce061","859ce061","869ce061","879ce061","889ce061","899ce061","8a9ce061","8b9ce061","8c9ce061","8d9ce061","8e9ce061","8f9ce061","909ce061","919ce061","929ce061","939ce061","949ce061","959ce061","969ce061","979ce061","989ce061","999ce061","9a9ce061","9b9ce061","9c9ce061","9d9ce061","9e9ce061","9f9ce061","a09ce061","a19ce061","a29ce061","a39ce061","a49ce061","a59ce061","a69ce061","a79ce061","a89ce061","a99ce061","aa9ce061","ab9ce061","ac9ce061","ad9ce061","ae9ce061","af9ce061","b09ce061","b19ce061","b29ce061","b39ce061","b49ce061","b59ce061","b69ce061","b79ce061","b89ce061","b99ce061","ba9ce061","bb9ce061","bc9ce061","bd9ce061","be9ce061","bf9ce061","c09ce061","c19ce061","c29ce061","c39ce061","c49ce061","c59ce061","c69ce061","c79ce061","c89ce061","c99ce061","ca9ce061","cb9ce061","cc9ce061","cd9ce061","ce9ce061","cf9ce061","d09ce061","d19ce061","d29ce061","d39ce061","d49ce061","d59ce061","d69ce061","d79ce061","d89ce061","d99ce061","da9ce061","db9ce061","dc9ce061","dd9ce061","de9ce061","df9ce061","e09ce061","e19ce061","e29ce061","e39ce061","e49ce061","e59ce061","e69ce061","e79ce061","e89ce061","e99ce061","ea9ce061","eb9ce061","ec9ce061","ed9ce061","ee9ce061","ef9ce061","f09ce061","f19ce061","f29ce061","f39ce061","f49ce061","f59ce061","f69ce061","f79ce061","f89ce061","f99ce061","fa9ce061","fb9ce061","fc9ce061","fd9ce061","fe9ce061","ff9ce061","809de061","819de061","829de061","839de061","849de061","869de061","879de061","889de061","899de061","8a9de061","8b9de061","8c9de061","8d9de061","8e9de061","8f9de061","909de061","919de061","929de061","939de061","949de061","959de061","969de061","979de061","989de061","999de061","9a9de061","9b9de061","9c9de061","9d9de061","9e9de061","9f9de061","a09de061","a19de061","a29de061","a39de061","a49de061","a59de061","a69de061","a79de061","a89de061","a99de061","aa9de061","ab9de061","ac9de061","ad9de061","ae9de061","af9de061","b09de061","b19de061","b29de061","b39de061","b49de061","b59de061","b69de061","b79de061","b89de061","b99de061","ba9de061","bb9de061","bc9de061","bd9de061","be9de061","bf9de061","c09de061","c19de061","c29de061","c39de061","c49de061","c59de061","c69de061","c79de061","c89de061","c99de061","ca9de061","cb9de061","cc9de061","cd9de061","ce9de061","cf9de061","d09de061","d19de061","d29de061","d39de061","d49de061","d59de061","d69de061","d79de061","d89de061","d99de061","da9de061","db9de061","dc9de061","dd9de061","de9de061","df9de061","e09de061","e19de061","e29de061","e39de061","e49de061","e59de061","e69de061","e79de061","e89de061","e99de061","ea9de061","eb9de061","ec9de061","ed9de061","ee9de061","ef9de061","f09de061","f19de061","f29de061","f39de061","f49de061","f59de061","f69de061","f79de061","f89de061","f99de061","fa9de061","fb9de061","fc9de061","fd9de061","fe9de061","ff9de061","809ee061","819ee061","829ee061","839ee061","849ee061","859ee061","869ee061","879ee061","889ee061","899ee061","8a9ee061","8b9ee061","8c9ee061","8d9ee061","8e9ee061","8f9ee061","909ee061","919ee061","929ee061","939ee061","949ee061","959ee061","969ee061","979ee061","989ee061","999ee061","9a9ee061","9b9ee061","9c9ee061","9d9ee061","9e9ee061","9f9ee061","a09ee061","a19ee061","a29ee061","a39ee061","a49ee061","a59ee061","a69ee061","a79ee061","a89ee061","a99ee061","aa9ee061","ab9ee061","ac9ee061","ad9ee061","ae9ee061","af9ee061","b09ee061","b19ee061","b29ee061","b39ee061","b49ee061","b59ee061","b69ee061","b79ee061","b89ee061","b99ee061","ba9ee061","bb9ee061","bc9ee061","bd9ee061","be9ee061","bf9ee061","c09ee061","c19ee061","c29ee061","c39ee061","c49ee061","c59ee061","c69ee061","c79ee061","c89ee061","c99ee061","ca9ee061","cb9ee061","cc9ee061","cd9ee061","ce9ee061","cf9ee061","d09ee061","d19ee061","d29ee061","d39ee061","d49ee061","d59ee061","d69ee061","d79ee061","d89ee061","d99ee061","da9ee061","db9ee061","dc9ee061","dd9ee061","de9ee061","df9ee061","e09ee061","e19ee061","e29ee061","e39ee061","e49ee061","e59ee061","e69ee061","e79ee061","e89ee061","e99ee061","ea9ee061","eb9ee061","ec9ee061","ed9ee061","ee9ee061","ef9ee061","f09ee061","f19ee061","f29ee061","f39ee061","f49ee061","f59ee061","f69ee061","f79ee061","f89ee061","f99ee061","fa9ee061","fb9ee061","fc9ee061","fd9ee061","fe9ee061","ff9ee061","809fe061","819fe061","829fe061","839fe061","849fe061","859fe061","869fe061","879fe061","889fe061","899fe061","8a9fe061","8b9fe061","8c9fe061","8d9fe061","8e9fe061","8f9fe061","909fe061","919fe061","929fe061","939fe061","949fe061","959fe061","969fe061","979fe061","989fe061","999fe061","9a9fe061","9b9fe061","9c9fe061","9d9fe061","9e9fe061","9f9fe061","a09fe061","a19fe061","a29fe061","a39fe061","a49fe061","a59fe061","a69fe061","a79fe061","a89fe061","a99fe061","aa9fe061","ab9fe061","ac9fe061","ad9fe061","ae9fe061","b09fe061","b19fe061","b29fe061","b39fe061","b49fe061","b59fe061","b69fe061","b79fe061","b89fe061","b99fe061","ba9fe061","bb9fe061","bc9fe061","bd9fe061","be9fe061","bf9fe061","c09fe061","c19fe061","c29fe061","c39fe061","c49fe061","c59fe061","c69fe061","c79fe061","c89fe061","c99fe061","ca9fe061","cb9fe061","cc9fe061","cd9fe061","ce9fe061","cf9fe061","d09fe061","d19fe061","d29fe061","d39fe061","d49fe061","d59fe061","d69fe061","d79fe061","d89fe061","d99fe061","da9fe061","db9fe061","dc9fe061","dd9fe061","de9fe061","df9fe061","e09fe061","e19fe061","e29fe061","e39fe061","e49fe061","e59fe061","e69fe061","e79fe061","e89fe061","e99fe061","ea9fe061","eb9fe061","ec9fe061","ed9fe061","ee9fe061","ef9fe061","f09fe061","f19fe061","f29fe061","f39fe061","f49fe061","f59fe061","f69fe061","f79fe061","f89fe061","f99fe061","fa9fe061","fb9fe061","fc9fe061","fd9fe061","fe9fe061","ff9fe061","80a0e061","81a0e061","82a0e061","83a0e061","84a0e061","85a0e061","86a0e061","87a0e061","88a0e061","89a0e061","8aa0e061","8ba0e061","8ca0e061","8da0e061","8ea0e061","8fa0e061","90a0e061","91a0e061","92a0e061","93a0e061","94a0e061","95a0e061","96a0e061","97a0e061","98a0e061","99a0e061","9aa0e061","9ba0e061","9ca0e061","9da0e061","9ea0e061","9fa0e061","a0a0e061","a1a0e061","a2a0e061","a3a0e061","a4a0e061","a5a0e061","a6a0e061","a7a0e061","a8a0e061","a9a0e061","aaa0e061","aba0e061","aca0e061","ada0e061","aea0e061","afa0e061","b0a0e061","b1a0e061","b2a0e061","b3a0e061","b4a0e061","b5a0e061","b6a0e061","b7a0e061","b8a0e061","b9a0e061","baa0e061","bba0e061","bca0e061","bda0e061","c0a0e061","c1a0e061","c2a0e061","c3a0e061","c4a0e061","c5a0e061","c6a0e061","c7a0e061","c8a0e061","c9a0e061","cca0e061","cda0e061","cea0e061","cfa0e061","d0a0e061","d1a0e061","d2a0e061","d3a0e061","d4a0e061","d5a0e061","d6a0e061","d7a0e061","d8a0e061","d9a0e061","daa0e061","dba0e061","dca0e061","dda0e061","dea0e061","dfa0e061","e0a0e061","e1a0e061","e2a0e061","e3a0e061","e4a0e061","e5a0e061","e6a0e061","e7a0e061","e8a0e061","e9a0e061","eaa0e061","eba0e061","eca0e061","eda0e061","eea0e061","efa0e061","f0a0e061","f1a0e061","f2a0e061","f3a0e061","f4a0e061","f5a0e061","f6a0e061","f7a0e061","f8a0e061","f9a0e061","faa0e061","fba0e061","fca0e061","fda0e061","fea0e061","ffa0e061","80a1e061","81a1e061","82a1e061","83a1e061","84a1e061","85a1e061","86a1e061","87a1e061","88a1e061","89a1e061","8aa1e061","8ba1e061","8ca1e061","8da1e061","8ea1e061","8fa1e061","90a1e061","91a1e061","92a1e061","93a1e061","94a1e061","95a1e061","96a1e061","97a1e061","98a1e061","99a1e061","9aa1e061","9ba1e061","9ca1e061","9da1e061","9ea1e061","9fa1e061","a0a1e061","a1a1e061","a2a1e061","a3a1e061","a4a1e061","a5a1e061","a6a1e061","a7a1e061","a8a1e061","a9a1e061","aaa1e061","aba1e061","aca1e061","ada1e061","aea1e061","afa1e061","b0a1e061","b1a1e061","b2a1e061","b3a1e061","b4a1e061","b6a1e061","b7a1e061","b8a1e061","b9a1e061","a99ce261","aa9ce261","ab9ce261","ac9ce261","ad9ce261","ae9ce261","af9ce261","b09ce261","b19ce261","b29ce261","b39ce261","b49ce261","b59ce261","b69ce261","b79ce261","b89ce261","b99ce261","ba9ce261","bb9ce261","bc9ce261","bd9ce261","be9ce261","bf9ce261","c09ce261","c19ce261","c29ce261","c39ce261","c49ce261","c69ce261","c79ce261","c89ce261","c99ce261","ca9ce261","cb9ce261","cd9ce261","ce9ce261","cf9ce261","d09ce261","d19ce261","d29ce261","d39ce261","d49ce261","d59ce261","d69ce261","d79ce261","d89ce261","d99ce261","da9ce261","db9ce261","dc9ce261","91a4e261","92a4e261","94a4e261","95a4e261","96a4e261","97a4e261","98a4e261","99a4e261","9aa4e261","9ba4e261","9ca4e261","9da4e261","9ea4e261","9fa4e261","a0a4e261","a1a4e261","a2a4e261","a3a4e261","a4a4e261","a5a4e261","a6a4e261","a7a4e261","a8a4e261","a9a4e261","aaa4e261","aba4e261","aca4e261","ada4e261","aea4e261","afa4e261","b0a4e261","b1a4e261","b2a4e261","b3a4e261","b4a4e261","b5a4e261","b6a4e261","b7a4e261","b8a4e261","b9a4e261","baa4e261","bba4e261","bca4e261","bda4e261","bea4e261","bfa4e261","c0a4e261","c1a4e261","c2a4e261","f9abe261","faabe261","fbabe261","fcabe261","fdabe261","feabe261","ffabe261","80ace261","81ace261","82ace261","83ace261","84ace261","85ace261","86ace261","87ace261","88ace261","89ace261","8aace261","8bace261","8cace261","8dace261","8eace261","8face261","90ace261","91ace261","92ace261","93ace261","94ace261","95ace261","96ace261","97ace261","98ace261","99ace261","9aace261","9bace261","9cace261","9dace261","9eace261","9face261","a0ace261","a1ace261","a2ace261","a3ace261","a4ace261","a5ace261","a7ace261","a8ace261","e0b3e261","e1b3e261","e2b3e261","e3b3e261","e4b3e261","e5b3e261","e6b3e261","e7b3e261","e8b3e261","e9b3e261","eab3e261","ebb3e261","ecb3e261","edb3e261","eeb3e261","efb3e261","f0b3e261","f1b3e261","f2b3e261","f3b3e261","f4b3e261","f5b3e261","f6b3e261","f7b3e261","f8b3e261","f9b3e261","fab3e261","fbb3e261","fcb3e261","fdb3e261","feb3e261","ffb3e261","80b4e261","81b4e261","82b4e261","83b4e261","84b4e261","85b4e261","86b4e261","87b4e261","88b4e261","89b4e261","8ab4e261","c8bbe261","c9bbe261","cabbe261","cbbbe261","cebbe261","cfbbe261","d0bbe261","d1bbe261","d2bbe261","d3bbe261","d4bbe261","d5bbe261","d6bbe261","d7bbe261","d8bbe261","d9bbe261","dabbe261","dbbbe261","dcbbe261","ddbbe261","debbe261","dfbbe261","e1bbe261","e2bbe261","e3bbe261","e4bbe261","e6bbe261","e7bbe261","e8bbe261","eabbe261","ebbbe261","eebbe261","efbbe261","f0bbe261","f1bbe261","f2bbe261","f3bbe261","f4bbe261","f5bbe261","f6bbe261","f7bbe261","f8bbe261","f9bbe261","fabbe261","fbbbe261","fcbbe261","fdbbe261","febbe261","d3bce261","b0c3e261","b1c3e261","b2c3e261","b3c3e261","b4c3e261","b5c3e261","b6c3e261","b7c3e261","b8c3e261","b9c3e261","bac3e261","bbc3e261","bcc3e261","bdc3e261","bec3e261","bfc3e261","c0c3e261","c1c3e261","c2c3e261","c3c3e261","c4c3e261","c5c3e261","c6c3e261","c7c3e261","cbc3e261","ccc3e261","cdc3e261","cec3e261","d0c3e261","d2c3e261","d3c3e261","d4c3e261","d5c3e261","d7c3e261","d8c3e261","d9c3e261","dac3e261","dbc3e261","dcc3e261","ddc3e261","dec3e261","e6c3e261","e7c3e261","e8c3e261","e9c3e261","eac3e261","ebc3e261","ecc3e261","edc3e261","eec3e261","efc3e261","98cbe261","99cbe261","9acbe261","9bcbe261","9ccbe261","9dcbe261","9ecbe261","9fcbe261","a0cbe261","a1cbe261","a2cbe261","a3cbe261","a4cbe261","a5cbe261","a6cbe261","a7cbe261","a8cbe261","a9cbe261","aacbe261","abcbe261","accbe261","adcbe261","aecbe261","afcbe261","b0cbe261","b1cbe261","b2cbe261","b3cbe261","b4cbe261","b5cbe261","b6cbe261","b7cbe261","b8cbe261","b9cbe261","bacbe261","bbcbe261","bccbe261","bdcbe261","becbe261","bfcbe261","c0cbe261","c1cbe261","c2cbe261","c3cbe261","c4cbe261","c5cbe261","c6cbe261","80d3e261","81d3e261","82d3e261","83d3e261","84d3e261","85d3e261","86d3e261","87d3e261","88d3e261","89d3e261","8ad3e261","8bd3e261","8cd3e261","8dd3e261","8ed3e261","8fd3e261","90d3e261","91d3e261","92d3e261","93d3e261","94d3e261","95d3e261","96d3e261","97d3e261","98d3e261","99d3e261","9ad3e261","9bd3e261","9cd3e261","9dd3e261","9ed3e261","9fd3e261","a0d3e261","a1d3e261","a2d3e261","a3d3e261","a4d3e261","a5d3e261","a6d3e261","e8dae261","e9dae261","eadae261","ebdae261","ecdae261","eddae261","eedae261","efdae261","f0dae261","f1dae261","f2dae261","f3dae261","f4dae261","f5dae261","f6dae261","f7dae261","f8dae261","f9dae261","fadae261","fbdae261","fcdae261","fddae261","fedae261","ffdae261","80dbe261","81dbe261","82dbe261","83dbe261","84dbe261","85dbe261","86dbe261","87dbe261","88dbe261","89dbe261","8adbe261","8bdbe261","8cdbe261","8ddbe261","8edbe261","8fdbe261","d0e2e261","d1e2e261","d2e2e261","d3e2e261","d4e2e261","d5e2e261","d6e2e261","d7e2e261","d8e2e261","d9e2e261","dae2e261","dbe2e261","dce2e261","dde2e261","dee2e261","dfe2e261","e0e2e261","e1e2e261","e2e2e261","e3e2e261","e4e2e261","e5e2e261","e6e2e261","e7e2e261","e8e2e261","e9e2e261","eae2e261","ebe2e261","ece2e261","b8eae261","b9eae261","baeae261","bbeae261","bceae261","bdeae261","beeae261","bfeae261","c0eae261","c1eae261","c2eae261","c3eae261","c4eae261","c5eae261","c6eae261","c7eae261","c8eae261","c9eae261","caeae261","cbeae261","cceae261","cdeae261","ceeae261","cfeae261","d0eae261","d1eae261","d2eae261","d3eae261","d4eae261","d5eae261","d6eae261","d7eae261","d8eae261","d9eae261","daeae261","dbeae261","dceae261","ddeae261","deeae261","a0f2e261","a1f2e261","a2f2e261","a3f2e261","a4f2e261","a5f2e261","a6f2e261","a7f2e261","a8f2e261","a9f2e261","aaf2e261","abf2e261","acf2e261","adf2e261","aef2e261","aff2e261","b0f2e261","b1f2e261","b2f2e261","b3f2e261","b4f2e261","b5f2e261","b6f2e261","b7f2e261","b8f2e261","b9f2e261","baf2e261","bbf2e261","bcf2e261","bdf2e261","88fae261","89fae261","8afae261","8bfae261","8cfae261","8dfae261","8efae261","8ffae261","90fae261","91fae261","92fae261","93fae261","94fae261","95fae261","96fae261","97fae261","98fae261","99fae261","9afae261","9bfae261","9cfae261","9dfae261","9efae261","9ffae261","a0fae261","a1fae261","a2fae261","f081e361","f181e361","f281e361","f381e361","f481e361","f581e361","f681e361","f781e361","f881e361","f981e361","fa81e361","fb81e361","fc81e361","fd81e361","fe81e361","ff81e361","8082e361","8182e361","8282e361","8382e361","8482e361","8582e361","8682e361","8782e361","8882e361","8982e361","8a82e361","8b82e361","8c82e361","8d82e361","8e82e361","8f82e361","9082e361","9182e361","d889e361","d989e361","da89e361","db89e361","dc89e361","dd89e361","de89e361","df89e361","e089e361","e189e361","e289e361","e389e361","e489e361","e589e361","e689e361","e789e361","e889e361","e989e361","ea89e361","eb89e361","ed89e361","ee89e361","ef89e361","f089e361","f189e361","f289e361","f389e361","f489e361","f589e361","f689e361","c091e361","c191e361","c291e361","c391e361","c491e361","c591e361","c691e361","c791e361","c891e361","c991e361","ca91e361","cb91e361","cc91e361","cd91e361","ce91e361","cf91e361","d091e361","d191e361","d291e361","d391e361","d491e361","d591e361","d691e361","d791e361","d891e361","d991e361","da91e361","db91e361","dc91e361","dd91e361","de91e361","df91e361","e091e361","e191e361","e291e361","e391e361","e491e361","e591e361","e691e361","a899e361","a999e361","aa99e361","ab99e361","ac99e361","ad99e361","ae99e361","af99e361","b099e361","b199e361","b299e361","b399e361","b499e361","b599e361","b699e361","b799e361","b899e361","b999e361","ba99e361","bb99e361","bc99e361","bd99e361","be99e361","bf99e361","c099e361","c199e361","c299e361","c399e361","c499e361","c599e361","c699e361","c799e361","c899e361","c999e361","ca99e361","cb99e361","cc99e361","cd99e361","90a1e361","91a1e361","92a1e361","93a1e361","94a1e361","95a1e361","96a1e361","97a1e361","98a1e361","99a1e361","9aa1e361","9ba1e361","9ca1e361","9da1e361","9ea1e361","9fa1e361","a0a1e361","a1a1e361","a2a1e361","a3a1e361","a4a1e361","a5a1e361","a6a1e361","a7a1e361","a8a1e361","a9a1e361","aaa1e361","aba1e361","aca1e361","ada1e361","aea1e361","afa1e361","b0a1e361","eaa1e361","eba1e361","eca1e361","eda1e361","eea1e361","efa1e361","80a89763","c0b5ce64","c1b5ce64","c3b5ce64","c4b5ce64","c5b5ce64","c6b5ce64","c7b5ce64","c8b5ce64","c9b5ce64","cab5ce64","cbb5ce64","ccb5ce64","cfb5ce64","d0b5ce64","d1b5ce64","d2b5ce64","d4b5ce64","d6b5ce64","d7b5ce64","d8b5ce64","d9b5ce64","dab5ce64","dbb5ce64","dcb5ce64","ddb5ce64","deb5ce64","dfb5ce64","e0b5ce64","e1b5ce64","e2b5ce64","e3b5ce64","e4b5ce64","e5b5ce64","e6b5ce64","e7b5ce64","e8b5ce64","e9b5ce64","eab5ce64","ebb5ce64","ecb5ce64","edb5ce64","eeb5ce64","efb5ce64","f0b5ce64","f1b5ce64","f2b5ce64","f3b5ce64","f4b5ce64","f7b5ce64","f8b5ce64","f9b5ce64","fab5ce64","fbb5ce64","fcb5ce64","fdb5ce64","feb5ce64","ffb5ce64","80b6ce64","81b6ce64","82b6ce64","83b6ce64","84b6ce64","85b6ce64","86b6ce64","87b6ce64","88b6ce64","89b6ce64","8ab6ce64","8bb6ce64","8cb6ce64","8db6ce64","8eb6ce64","8fb6ce64","90b6ce64","91b6ce64","93b6ce64","94b6ce64","95b6ce64","96b6ce64","97b6ce64","98b6ce64","99b6ce64","9ab6ce64","9bb6ce64","9cb6ce64","9db6ce64","9eb6ce64","9fb6ce64","a0b6ce64","a1b6ce64","a2b6ce64","a3b6ce64","a4b6ce64","a5b6ce64","a6b6ce64","a7b6ce64","a8b6ce64","a9b6ce64","aab6ce64","abb6ce64","acb6ce64","adb6ce64","aeb6ce64","afb6ce64","b0b6ce64","b1b6ce64","b2b6ce64","b3b6ce64","b4b6ce64","b5b6ce64","b6b6ce64","b7b6ce64","b8b6ce64","b9b6ce64","bab6ce64","bbb6ce64","bcb6ce64","bdb6ce64","beb6ce64","bfb6ce64","c0b6ce64","c1b6ce64","c2b6ce64","c3b6ce64","c4b6ce64","c5b6ce64","c6b6ce64","c7b6ce64","c8b6ce64","c9b6ce64","cab6ce64","cbb6ce64","ccb6ce64","cdb6ce64","ceb6ce64","cfb6ce64","d0b6ce64","d1b6ce64","d2b6ce64","d4b6ce64","d5b6ce64","d6b6ce64","d7b6ce64","d8b6ce64","d9b6ce64","dab6ce64","dbb6ce64","dcb6ce64","deb6ce64","dfb6ce64","e0b6ce64","e1b6ce64","e2b6ce64","e3b6ce64","e4b6ce64","e5b6ce64","e6b6ce64","e7b6ce64","e8b6ce64","e9b6ce64","eab6ce64","ebb6ce64","ecb6ce64","edb6ce64","eeb6ce64","efb6ce64","f0b6ce64","f1b6ce64","f2b6ce64","f3b6ce64","f4b6ce64","f5b6ce64","f6b6ce64","f7b6ce64","f8b6ce64","f9b6ce64","fab6ce64","fbb6ce64","fcb6ce64","fdb6ce64","feb6ce64","ffb6ce64","80b7ce64","81b7ce64","82b7ce64","83b7ce64","84b7ce64","85b7ce64","86b7ce64","87b7ce64","88b7ce64","89b7ce64","8ab7ce64","8bb7ce64","8cb7ce64","8db7ce64","8eb7ce64","8fb7ce64","90b7ce64","91b7ce64","92b7ce64","93b7ce64","94b7ce64","95b7ce64","96b7ce64","97b7ce64","98b7ce64","99b7ce64","9ab7ce64","9bb7ce64","9cb7ce64","9db7ce64","9eb7ce64","9fb7ce64","a1b7ce64","a2b7ce64","a3b7ce64","a4b7ce64","a5b7ce64","a6b7ce64","a7b7ce64","a8b7ce64","a9b7ce64","aab7ce64","abb7ce64","acb7ce64","adb7ce64","aeb7ce64","afb7ce64","b0b7ce64","b1b7ce64","b2b7ce64","b3b7ce64","b4b7ce64","b5b7ce64","b6b7ce64","b7b7ce64","b8b7ce64","b9b7ce64","bab7ce64","bbb7ce64","bcb7ce64","bdb7ce64","beb7ce64","bfb7ce64","c0b7ce64","c1b7ce64","c2b7ce64","c3b7ce64","c4b7ce64","c5b7ce64","c6b7ce64","c7b7ce64","c8b7ce64","c9b7ce64","cab7ce64","cbb7ce64","ccb7ce64","cdb7ce64","ceb7ce64","cfb7ce64","d0b7ce64","d1b7ce64","d2b7ce64","d3b7ce64","d4b7ce64","d5b7ce64","d6b7ce64","d7b7ce64","d8b7ce64","d9b7ce64","dab7ce64","dbb7ce64","dcb7ce64","ddb7ce64","deb7ce64","dfb7ce64","e0b7ce64","e1b7ce64","e2b7ce64","e3b7ce64","e4b7ce64","e5b7ce64","e6b7ce64","e7b7ce64","e8b7ce64","e9b7ce64","eab7ce64","ebb7ce64","ecb7ce64","edb7ce64","eeb7ce64","efb7ce64","f0b7ce64","f1b7ce64","f2b7ce64","f3b7ce64","f4b7ce64","f5b7ce64","f6b7ce64","f7b7ce64","f8b7ce64","f9b7ce64","fab7ce64","fbb7ce64","fcb7ce64","fdb7ce64","feb7ce64","ffb7ce64","80b8ce64","81b8ce64","82b8ce64","83b8ce64","84b8ce64","85b8ce64","86b8ce64","87b8ce64","88b8ce64","89b8ce64","8ab8ce64","8bb8ce64","8cb8ce64","8db8ce64","8eb8ce64","8fb8ce64","90b8ce64","91b8ce64","92b8ce64","93b8ce64","94b8ce64","95b8ce64","96b8ce64","97b8ce64","98b8ce64","99b8ce64","9ab8ce64","9bb8ce64","9cb8ce64","9db8ce64","9eb8ce64","a0b8ce64","a1b8ce64","a4b8ce64","a5b8ce64","a8b8ce64","a9b8ce64","abb8ce64","acb8ce64","adb8ce64","aeb8ce64","afb8ce64","b0b8ce64","b1b8ce64","b2b8ce64","b3b8ce64","b4b8ce64","b5b8ce64","b6b8ce64","b7b8ce64","b8b8ce64","b9b8ce64","bab8ce64","bbb8ce64","bcb8ce64","bdb8ce64","beb8ce64","bfb8ce64","c0b8ce64","c1b8ce64","c2b8ce64","c3b8ce64","c4b8ce64","c5b8ce64","c7b8ce64","c8b8ce64","c9b8ce64","cab8ce64","cbb8ce64","ccb8ce64","cdb8ce64","ceb8ce64","cfb8ce64","d0b8ce64","d1b8ce64","d2b8ce64","d3b8ce64","d4b8ce64","d5b8ce64","d6b8ce64","d7b8ce64","d8b8ce64","d9b8ce64","dab8ce64","dbb8ce64","dcb8ce64","ddb8ce64","deb8ce64","dfb8ce64","e0b8ce64","e1b8ce64","e2b8ce64","e3b8ce64","e4b8ce64","e5b8ce64","e6b8ce64","e7b8ce64","e8b8ce64","e9b8ce64","eab8ce64","ebb8ce64","ecb8ce64","edb8ce64","eeb8ce64","efb8ce64","f0b8ce64","f1b8ce64","f2b8ce64","f3b8ce64","f4b8ce64","f5b8ce64","f6b8ce64","f7b8ce64","f8b8ce64","f9b8ce64","fab8ce64","fbb8ce64","fcb8ce64","fdb8ce64","feb8ce64","ffb8ce64","81b9ce64","82b9ce64","83b9ce64","84b9ce64","85b9ce64","86b9ce64","87b9ce64","88b9ce64","89b9ce64","8ab9ce64","8bb9ce64","8cb9ce64","8db9ce64","8eb9ce64","8fb9ce64","90b9ce64","91b9ce64","92b9ce64","93b9ce64","95b9ce64","96b9ce64","97b9ce64","98b9ce64","99b9ce64","9ab9ce64","9bb9ce64","9cb9ce64","9db9ce64","9eb9ce64","9fb9ce64","a0b9ce64","a1b9ce64","a2b9ce64","a3b9ce64","a4b9ce64","a5b9ce64","a6b9ce64","a7b9ce64","a8b9ce64","a9b9ce64","aab9ce64","abb9ce64","acb9ce64","adb9ce64","aeb9ce64","afb9ce64","b0b9ce64","b1b9ce64","b2b9ce64","b3b9ce64","b4b9ce64","b5b9ce64","b6b9ce64","b7b9ce64","b8b9ce64","b9b9ce64","bab9ce64","bbb9ce64","bcb9ce64","bdb9ce64","beb9ce64","bfb9ce64","c0b9ce64","c1b9ce64","c2b9ce64","c3b9ce64","c4b9ce64","c5b9ce64","c6b9ce64","c7b9ce64","c8b9ce64","c9b9ce64","cab9ce64","cbb9ce64","ccb9ce64","cdb9ce64","ceb9ce64","cfb9ce64","d0b9ce64","d1b9ce64","d2b9ce64","d3b9ce64","d4b9ce64","d5b9ce64","d6b9ce64","d7b9ce64","d8b9ce64","d9b9ce64","dab9ce64","dbb9ce64","dcb9ce64","ddb9ce64","dfb9ce64","e0b9ce64","e1b9ce64","e2b9ce64","e3b9ce64","e4b9ce64","e5b9ce64","e6b9ce64","e7b9ce64","e8b9ce64","e9b9ce64","eab9ce64","ebb9ce64","ecb9ce64","edb9ce64","eeb9ce64","efb9ce64","f0b9ce64","f1b9ce64","f2b9ce64","f3b9ce64","f4b9ce64","f5b9ce64","f6b9ce64","f7b9ce64","f8b9ce64","f9b9ce64","fab9ce64","fbb9ce64","fcb9ce64","fdb9ce64","feb9ce64","ffb9ce64","80bace64","81bace64","82bace64","83bace64","84bace64","85bace64","86bace64","87bace64","88bace64","89bace64","8abace64","8bbace64","8cbace64","8dbace64","8ebace64","8fbace64","90bace64","91bace64","92bace64","93bace64","94bace64","95bace64","96bace64","97bace64","98bace64","99bace64","9abace64","9bbace64","9cbace64","9dbace64","9ebace64","9fbace64","a0bace64","a1bace64","a2bace64","a3bace64","a4bace64","a5bace64","a6bace64","a7bace64","a8bace64","a9bace64","aabace64","abbace64","acbace64","adbace64","aebace64","afbace64","b0bace64","b1bace64","b2bace64","b3bace64","b4bace64","b5bace64","b6bace64","b7bace64","b8bace64","b9bace64","babace64","bbbace64","bcbace64","bdbace64","bebace64","bfbace64","c0bace64","c1bace64","c2bace64","c3bace64","c4bace64","c5bace64","c6bace64","c7bace64","c8bace64","c9bace64","cabace64","cbbace64","ccbace64","cdbace64","cebace64","cfbace64","d0bace64","d1bace64","d2bace64","d3bace64","d4bace64","d5bace64","d6bace64","d7bace64","d8bace64","d9bace64","dabace64","dbbace64","dcbace64","ddbace64","debace64","dfbace64","e0bace64","e1bace64","e2bace64","e3bace64","e4bace64","e6bace64","e8bace64","e9bace64","eabace64","ebbace64","ecbace64","edbace64","eebace64","efbace64","f0bace64","f1bace64","f2bace64","f3bace64","f4bace64","f5bace64","f6bace64","f7bace64","f8bace64","f9bace64","fabace64","fbbace64","fcbace64","fdbace64","febace64","ffbace64","80bbce64","81bbce64","83bbce64","84bbce64","85bbce64","86bbce64","87bbce64","88bbce64","89bbce64","8abbce64","8bbbce64","8cbbce64","8dbbce64","8ebbce64","8fbbce64","90bbce64","91bbce64","92bbce64","93bbce64","94bbce64","95bbce64","96bbce64","97bbce64","98bbce64","99bbce64","9abbce64","9bbbce64","9cbbce64","9dbbce64","9ebbce64","9fbbce64","a0bbce64","a1bbce64","a2bbce64","a3bbce64","a4bbce64","a5bbce64","a6bbce64","a7bbce64","a8bbce64","a9bbce64","aabbce64","abbbce64","acbbce64","adbbce64","aebbce64","afbbce64","b0bbce64","b1bbce64","b2bbce64","b3bbce64","b4bbce64","b5bbce64","b6bbce64","b7bbce64","b8bbce64","b9bbce64","babbce64","bbbbce64","bcbbce64","bdbbce64","bebbce64","bfbbce64","c0bbce64","c1bbce64","c2bbce64","c3bbce64","c4bbce64","c5bbce64","c6bbce64","c7bbce64","c8bbce64","c9bbce64","cabbce64","cbbbce64","ccbbce64","cdbbce64","cebbce64","cfbbce64","d0bbce64","d1bbce64","d2bbce64","d3bbce64","d5bbce64","d6bbce64","d7bbce64","d8bbce64","d9bbce64","dabbce64","dbbbce64","dcbbce64","ddbbce64","debbce64","dfbbce64","e0bbce64","e1bbce64","e2bbce64","e3bbce64","e4bbce64","e5bbce64","e6bbce64","e7bbce64","e8bbce64","e9bbce64","eabbce64","ebbbce64","ecbbce64","edbbce64","eebbce64","efbbce64","f0bbce64","f1bbce64","f2bbce64","f3bbce64","f4bbce64","f5bbce64","f6bbce64","f7bbce64","f8bbce64","f9bbce64","fabbce64","fbbbce64","fcbbce64","fdbbce64","febbce64","ffbbce64","80bcce64","82bcce64","83bcce64","84bcce64","85bcce64","86bcce64","87bcce64","88bcce64","89bcce64","8abcce64","8bbcce64","8cbcce64","8dbcce64","8ebcce64","8fbcce64","90bcce64","91bcce64","92bcce64","93bcce64","94bcce64","95bcce64","96bcce64","97bcce64","9bbcce64","9cbcce64","9dbcce64","9ebcce64","9fbcce64","a0bcce64","a1bcce64","a2bcce64","a3bcce64","a4bcce64","a5bcce64","a6bcce64","a7bcce64","a8bcce64","a9bcce64","aabcce64","abbcce64","acbcce64","adbcce64","aebcce64","afbcce64","b0bcce64","b1bcce64","b2bcce64","b3bcce64","b4bcce64","b5bcce64","b6bcce64","b7bcce64","b8bcce64","b9bcce64","babcce64","bbbcce64","bdbcce64","bebcce64","bfbcce64","c0bcce64","c1bcce64","c2bcce64","c3bcce64","c4bcce64","c5bcce64","c6bcce64","c7bcce64","c8bcce64","c9bcce64","cabcce64","cbbcce64","ccbcce64","cdbcce64","cebcce64","cfbcce64","d0bcce64","d2bcce64","d3bcce64","d4bcce64","d5bcce64","d6bcce64","d7bcce64","d8bcce64","d9bcce64","dabcce64","dbbcce64","dcbcce64","ddbcce64","debcce64","dfbcce64","e0bcce64","e1bcce64","e2bcce64","e3bcce64","e4bcce64","e5bcce64","e6bcce64","e7bcce64","e8bcce64","e9bcce64","eabcce64","ebbcce64","ecbcce64","edbcce64","eebcce64","efbcce64","f0bcce64","f1bcce64","f2bcce64","f3bcce64","f4bcce64","f5bcce64","f6bcce64","f7bcce64","f8bcce64","f9bcce64","fabcce64","fbbcce64","fcbcce64","fdbcce64","febcce64","ffbcce64","80bdce64","81bdce64","82bdce64","83bdce64","84bdce64","85bdce64","86bdce64","87bdce64","88bdce64","89bdce64","8abdce64","8bbdce64","8cbdce64","8dbdce64","8ebdce64","8fbdce64","90bdce64","91bdce64","92bdce64","93bdce64","94bdce64","95bdce64","96bdce64","97bdce64","98bdce64","99bdce64","9abdce64","9bbdce64","9cbdce64","9dbdce64","9ebdce64","9fbdce64","a0bdce64","a1bdce64","a2bdce64","a3bdce64","a4bdce64","a5bdce64","a6bdce64","a7bdce64","a8bdce64","a9bdce64","aabdce64","abbdce64","acbdce64","adbdce64","aebdce64","afbdce64","b0bdce64","b1bdce64","b2bdce64","b3bdce64","b4bdce64","b5bdce64","b6bdce64","b7bdce64","b8bdce64","b9bdce64","babdce64","bbbdce64","bcbdce64","bdbdce64","bebdce64","bfbdce64","c0bdce64","c1bdce64","c2bdce64","c3bdce64","c4bdce64","c5bdce64","c6bdce64","c7bdce64","c8bdce64","c9bdce64","cabdce64","cbbdce64","ccbdce64","cdbdce64","cebdce64","cfbdce64","d0bdce64","d1bdce64","d2bdce64","d3bdce64","d4bdce64","d5bdce64","d6bdce64","d7bdce64","d8bdce64","d9bdce64","dabdce64","dbbdce64","dcbdce64","ddbdce64","debdce64","dfbdce64","e0bdce64","e1bdce64","e2bdce64","e3bdce64","e4bdce64","e5bdce64","e6bdce64","e7bdce64","e8bdce64","e9bdce64","eabdce64","ebbdce64","ecbdce64","edbdce64","eebdce64","efbdce64","f0bdce64","f1bdce64","f2bdce64","f3bdce64","f4bdce64","f5bdce64","f6bdce64","f7bdce64","f8bdce64","f9bdce64","fabdce64","fbbdce64","fcbdce64","fdbdce64","febdce64","ffbdce64","80bece64","81bece64","82bece64","83bece64","84bece64","85bece64","86bece64","87bece64","88bece64","89bece64","8abece64","8bbece64","8cbece64","8dbece64","8ebece64","8fbece64","90bece64","91bece64","92bece64","93bece64","94bece64","95bece64","96bece64","97bece64","98bece64","99bece64","9abece64","9bbece64","9cbece64","9dbece64","9ebece64","9fbece64","a0bece64","a1bece64","a2bece64","a3bece64","a6bece64","a7bece64","a8bece64","a9bece64","aabece64","abbece64","acbece64","adbece64","aebece64","afbece64","b2bece64","b3bece64","b4bece64","b5bece64","b6bece64","b7bece64","b8bece64","b9bece64","babece64","bbbece64","bcbece64","bdbece64","bebece64","bfbece64","c0bece64","c1bece64","c2bece64","c3bece64","c4bece64","c5bece64","c6bece64","c7bece64","c8bece64","c9bece64","cabece64","cbbece64","ccbece64","cdbece64","cebece64","cfbece64","d0bece64","d1bece64","d2bece64","d4bece64","d5bece64","d6bece64","d7bece64","d8bece64","dbbece64","dcbece64","debece64","dfbece64","e0bece64","e1bece64","e2bece64","e3bece64","e4bece64","e5bece64","e6bece64","e7bece64","e8bece64","e9bece64","eabece64","ebbece64","ecbece64","edbece64","eebece64","efbece64","f0bece64","f1bece64","f2bece64","f3bece64","f4bece64","f5bece64","f6bece64","f7bece64","f8bece64","f9bece64","fabece64","fbbece64","fcbece64","fdbece64","febece64","ffbece64","80bfce64","81bfce64","82bfce64","83bfce64","84bfce64","85bfce64","86bfce64","87bfce64","88bfce64","89bfce64","8abfce64","8bbfce64","8cbfce64","8dbfce64","8ebfce64","8fbfce64","90bfce64","91bfce64","92bfce64","93bfce64","94bfce64","95bfce64","96bfce64","97bfce64","98bfce64","99bfce64","9abfce64","9bbfce64","9cbfce64","9dbfce64","9ebfce64","9fbfce64","a0bfce64","a1bfce64","a2bfce64","a3bfce64","a6bfce64","a7bfce64","a8bfce64","a9bfce64","aabfce64","abbfce64","acbfce64","adbfce64","aebfce64","afbfce64","b0bfce64","b1bfce64","b2bfce64","b3bfce64","b4bfce64","b5bfce64","b6bfce64","b7bfce64","b8bfce64","b9bfce64","babfce64","bbbfce64","bcbfce64","bdbfce64","bebfce64","bfbfce64","c0bfce64","c1bfce64","c2bfce64","c3bfce64","c4bfce64","c5bfce64","c6bfce64","c7bfce64","c8bfce64","c9bfce64","cabfce64","cbbfce64","ccbfce64","cdbfce64","cebfce64","cfbfce64","d0bfce64","d1bfce64","d2bfce64","d3bfce64","d4bfce64","d5bfce64","d6bfce64","d7bfce64","d8bfce64","d9bfce64","dabfce64","dbbfce64","dcbfce64","ddbfce64","debfce64","dfbfce64","e0bfce64","e1bfce64","e4bfce64","e5bfce64","e6bfce64","e7bfce64","e8bfce64","e9bfce64","eabfce64","ebbfce64","ecbfce64","edbfce64","eebfce64","efbfce64","f0bfce64","f1bfce64","f2bfce64","f3bfce64","f4bfce64","f5bfce64","f6bfce64","f7bfce64","f8bfce64","f9bfce64","fbbfce64","fcbfce64","fdbfce64","febfce64","ffbfce64","80c0ce64","81c0ce64","a9b7d064","aab7d064","acb7d064","adb7d064","aeb7d064","afb7d064","b0b7d064","b1b7d064","b2b7d064","b3b7d064","b4b7d064","b5b7d064","b6b7d064","b7b7d064","b8b7d064","b9b7d064","bab7d064","bbb7d064","bcb7d064","bdb7d064","beb7d064","bfb7d064","c0b7d064","c1b7d064","c2b7d064","c3b7d064","c4b7d064","c5b7d064","c6b7d064","c7b7d064","c8b7d064","c9b7d064","cab7d064","cbb7d064","ccb7d064","cdb7d064","ceb7d064","d1b7d064","d2b7d064","d3b7d064","d4b7d064","d5b7d064","d6b7d064","d7b7d064","d9b7d064","dbb7d064","dcb7d064","ddb7d064","deb7d064","dfb7d064","e0b7d064","e1b7d064","e2b7d064","e3b7d064","e4b7d064","e5b7d064","e6b7d064","e7b7d064","e9b7d064","ecb7d064","edb7d064","eeb7d064","efb7d064","f0b7d064","f1b7d064","f2b7d064","f3b7d064","91bfd064","92bfd064","93bfd064","94bfd064","95bfd064","96bfd064","97bfd064","98bfd064","99bfd064","9abfd064","9bbfd064","9cbfd064","9dbfd064","9ebfd064","9fbfd064","a0bfd064","a1bfd064","a2bfd064","a3bfd064","a4bfd064","a5bfd064","a6bfd064","a7bfd064","a8bfd064","a9bfd064","aabfd064","abbfd064","acbfd064","adbfd064","aebfd064","afbfd064","b0bfd064","b1bfd064","b2bfd064","b3bfd064","b4bfd064","b5bfd064","b6bfd064","b7bfd064","b8bfd064","b9bfd064","babfd064","bbbfd064","bcbfd064","bdbfd064","bebfd064","bfbfd064","c0bfd064","c1bfd064","c2bfd064","c3bfd064","c4bfd064","c5bfd064","c6bfd064","c7bfd064","c8bfd064","c9bfd064","cabfd064","cbbfd064","ccbfd064","cdbfd064","cebfd064","cfbfd064","d0bfd064","d1bfd064","d2bfd064","d3bfd064","d4bfd064","d5bfd064","d6bfd064","d7bfd064","d8bfd064","d9bfd064","dabfd064","dbbfd064","dcbfd064","ddbfd064","debfd064","dfbfd064","e0bfd064","e1bfd064","e2bfd064","f9c6d064","fac6d064","fbc6d064","fcc6d064","fdc6d064","fec6d064","ffc6d064","80c7d064","81c7d064","82c7d064","83c7d064","84c7d064","85c7d064","86c7d064","87c7d064","88c7d064","89c7d064","8ac7d064","8bc7d064","8cc7d064","8dc7d064","8ec7d064","8fc7d064","90c7d064","91c7d064","92c7d064","93c7d064","94c7d064","95c7d064","96c7d064","97c7d064","98c7d064","99c7d064","9ac7d064","9bc7d064","9cc7d064","9dc7d064","9ec7d064","9fc7d064","a0c7d064","a1c7d064","a2c7d064","a3c7d064","a4c7d064","a5c7d064","a6c7d064","a7c7d064","a8c7d064","a9c7d064","aac7d064","abc7d064","acc7d064","adc7d064","aec7d064","afc7d064","b0c7d064","b1c7d064","b2c7d064","b3c7d064","b4c7d064","b5c7d064","b6c7d064","b7c7d064","b8c7d064","b9c7d064","bac7d064","bbc7d064","bcc7d064","bdc7d064","bec7d064","bfc7d064","c0c7d064","c1c7d064","c2c7d064","c3c7d064","c4c7d064","e0ced064","e1ced064","e2ced064","e3ced064","e4ced064","e5ced064","e6ced064","e7ced064","e8ced064","e9ced064","eaced064","ebced064","ecced064","edced064","eeced064","efced064","f0ced064","f1ced064","f2ced064","f3ced064","f4ced064","f5ced064","f6ced064","f7ced064","f8ced064","f9ced064","faced064","fbced064","fcced064","fdced064","feced064","ffced064","80cfd064","82cfd064","83cfd064","84cfd064","85cfd064","86cfd064","87cfd064","88cfd064","89cfd064","8acfd064","8bcfd064","8ccfd064","8dcfd064","8ecfd064","8fcfd064","90cfd064","91cfd064","92cfd064","93cfd064","94cfd064","95cfd064","96cfd064","97cfd064","98cfd064","99cfd064","9acfd064","9bcfd064","9ccfd064","9dcfd064","9ecfd064","9fcfd064","a0cfd064","a1cfd064","a2cfd064","a3cfd064","a4cfd064","a5cfd064","a6cfd064","a7cfd064","a8cfd064","a9cfd064","aacfd064","abcfd064","accfd064","adcfd064","aecfd064","b3cfd064","c8d6d064","c9d6d064","cad6d064","cbd6d064","ccd6d064","cdd6d064","d0d6d064","d1d6d064","d2d6d064","d3d6d064","d4d6d064","d5d6d064","d6d6d064","d7d6d064","d8d6d064","d9d6d064","dad6d064","dbd6d064","dcd6d064","ddd6d064","ded6d064","dfd6d064","e0d6d064","e1d6d064","e2d6d064","e3d6d064","e4d6d064","e5d6d064","e6d6d064","e7d6d064","e9d6d064","ead6d064","ebd6d064","ecd6d064","edd6d064","eed6d064","f0d6d064","f1d6d064","f2d6d064","f3d6d064","f4d6d064","f5d6d064","f9d6d064","fad6d064","fbd6d064","fcd6d064","fdd6d064","fed6d064","ffd6d064","80d7d064","81d7d064","82d7d064","83d7d064","84d7d064","85d7d064","86d7d064","87d7d064","88d7d064","89d7d064","8ad7d064","8bd7d064","8cd7d064","8dd7d064","8ed7d064","8fd7d064","90d7d064","91d7d064","92d7d064","93d7d064","94d7d064","95d7d064","96d7d064","b0ded064","b1ded064","b2ded064","b3ded064","b4ded064","b5ded064","b6ded064","b7ded064","b8ded064","b9ded064","baded064","bbded064","bcded064","bdded064","beded064","bfded064","c0ded064","c1ded064","c2ded064","c3ded064","c4ded064","c5ded064","c6ded064","c7ded064","c8ded064","c9ded064","caded064","cbded064","ccded064","cdded064","ceded064","cfded064","d0ded064","d1ded064","d2ded064","d6ded064","d7ded064","d8ded064","d9ded064","daded064","dbded064","dcded064","ddded064","e0ded064","e1ded064","e2ded064","e3ded064","e4ded064","e5ded064","e6ded064","e7ded064","eaded064","ebded064","ecded064","edded064","eeded064","efded064","f0ded064","f1ded064","f2ded064","a2dfd064","a3dfd064","a4dfd064","a5dfd064","a6dfd064","a7dfd064","a8dfd064","a9dfd064","aadfd064","abdfd064","acdfd064","addfd064","aedfd064","98e6d064","99e6d064","9ae6d064","9be6d064","9ce6d064","9de6d064","9ee6d064","9fe6d064","a0e6d064","a1e6d064","a2e6d064","a3e6d064","a4e6d064","a5e6d064","a6e6d064","a7e6d064","a8e6d064","a9e6d064","aae6d064","abe6d064","ace6d064","ade6d064","aee6d064","afe6d064","b0e6d064","b1e6d064","b2e6d064","b3e6d064","b4e6d064","b5e6d064","b6e6d064","b7e6d064","b8e6d064","b9e6d064","bae6d064","bbe6d064","bce6d064","bde6d064","bee6d064","bfe6d064","c0e6d064","c1e6d064","c2e6d064","c3e6d064","c4e6d064","c5e6d064","c6e6d064","c7e6d064","c8e6d064","c9e6d064","cae6d064","cbe6d064","cce6d064","cde6d064","cee6d064","cfe6d064","d0e6d064","d1e6d064","d2e6d064","d3e6d064","d4e6d064","d5e6d064","d6e6d064","d7e6d064","d8e6d064","d9e6d064","dae6d064","dbe6d064","dce6d064","dde6d064","dee6d064","dfe6d064","e0e6d064","e1e6d064","e2e6d064","fce6d064","80eed064","81eed064","82eed064","83eed064","84eed064","85eed064","86eed064","87eed064","88eed064","89eed064","8aeed064","8beed064","8ceed064","8deed064","8eeed064","8feed064","90eed064","91eed064","92eed064","93eed064","94eed064","95eed064","96eed064","97eed064","98eed064","99eed064","9aeed064","9beed064","9ceed064","9deed064","9eeed064","9feed064","a0eed064","a1eed064","a2eed064","a3eed064","a4eed064","a5eed064","a6eed064","a7eed064","a8eed064","a9eed064","aaeed064","abeed064","aceed064","adeed064","aeeed064","afeed064","b0eed064","b1eed064","b2eed064","b3eed064","b4eed064","b5eed064","b6eed064","b7eed064","b8eed064","b9eed064","baeed064","bbeed064","bceed064","bdeed064","beeed064","bfeed064","c0eed064","c1eed064","c2eed064","c3eed064","e8f5d064","e9f5d064","eaf5d064","ebf5d064","ecf5d064","edf5d064","eef5d064","eff5d064","f0f5d064","f2f5d064","f3f5d064","f4f5d064","f5f5d064","f6f5d064","f7f5d064","f8f5d064","f9f5d064","faf5d064","fbf5d064","fcf5d064","fdf5d064","fef5d064","fff5d064","80f6d064","81f6d064","82f6d064","83f6d064","84f6d064","85f6d064","86f6d064","87f6d064","88f6d064","89f6d064","8af6d064","8bf6d064","8cf6d064","8df6d064","8ef6d064","8ff6d064","90f6d064","91f6d064","92f6d064","93f6d064","94f6d064","95f6d064","96f6d064","97f6d064","98f6d064","99f6d064","9af6d064","9bf6d064","9cf6d064","9df6d064","9ef6d064","9ff6d064","a0f6d064","a2f6d064","a3f6d064","b8f6d064","eaf9d064","d0fdd064","d1fdd064","d2fdd064","d3fdd064","d4fdd064","d5fdd064","d6fdd064","d7fdd064","d8fdd064","d9fdd064","dafdd064","dbfdd064","dcfdd064","ddfdd064","defdd064","dffdd064","e0fdd064","e1fdd064","e2fdd064","e3fdd064","e4fdd064","e5fdd064","e6fdd064","e7fdd064","e8fdd064","e9fdd064","eafdd064","ebfdd064","ecfdd064","edfdd064","eefdd064","effdd064","f0fdd064","f1fdd064","f2fdd064","f3fdd064","f4fdd064","f5fdd064","f6fdd064","f7fdd064","f8fdd064","f9fdd064","b885d164","b985d164","ba85d164","bb85d164","bc85d164","bd85d164","be85d164","bf85d164","c085d164","c185d164","c285d164","c385d164","c485d164","c585d164","c685d164","c785d164","c885d164","c985d164","ca85d164","cb85d164","cc85d164","cd85d164","ce85d164","cf85d164","d085d164","d185d164","d285d164","d385d164","d485d164","d585d164","d685d164","d785d164","d885d164","d985d164","da85d164","db85d164","dc85d164","dd85d164","de85d164","df85d164","e085d164","e185d164","e285d164","e385d164","e485d164","e585d164","e685d164","e785d164","e885d164","e985d164","ea85d164","eb85d164","ec85d164","ed85d164","ee85d164","ef85d164","f085d164","f185d164","a08dd164","a18dd164","a28dd164","a38dd164","a48dd164","a58dd164","a68dd164","a78dd164","a88dd164","a98dd164","aa8dd164","ab8dd164","ac8dd164","ad8dd164","ae8dd164","af8dd164","b08dd164","b18dd164","b28dd164","b38dd164","b48dd164","b58dd164","b68dd164","b78dd164","b88dd164","b98dd164","ba8dd164","bb8dd164","bc8dd164","bd8dd164","be8dd164","bf8dd164","c08dd164","c18dd164","c28dd164","c38dd164","c48dd164","c58dd164","c68dd164","c78dd164","c88dd164","c98dd164","ca8dd164","cb8dd164","cc8dd164","cd8dd164","ce8dd164","cf8dd164","d08dd164","d18dd164","d28dd164","d38dd164","8895d164","8995d164","8a95d164","8b95d164","8c95d164","8d95d164","8e95d164","8f95d164","9095d164","9195d164","9295d164","9395d164","9495d164","9695d164","9895d164","9995d164","9a95d164","9b95d164","9c95d164","9d95d164","9e95d164","9f95d164","a095d164","a195d164","a295d164","a395d164","a495d164","a595d164","a695d164","a795d164","a895d164","a995d164","aa95d164","ab95d164","ac95d164","ad95d164","ae95d164","af95d164","b095d164","b195d164","b295d164","b395d164","b495d164","f09cd164","f19cd164","f29cd164","f39cd164","f49cd164","f59cd164","f69cd164","f79cd164","f89cd164","f99cd164","fa9cd164","fb9cd164","fc9cd164","fd9cd164","fe9cd164","ff9cd164","809dd164","819dd164","829dd164","839dd164","849dd164","859dd164","869dd164","879dd164","889dd164","899dd164","8a9dd164","8b9dd164","8c9dd164","8d9dd164","8e9dd164","8f9dd164","909dd164","919dd164","929dd164","939dd164","949dd164","959dd164","969dd164","979dd164","989dd164","999dd164","9b9dd164","9d9dd164","9e9dd164","a09dd164","a19dd164","a29dd164","a39dd164","a49dd164","a59dd164","a69dd164","a79dd164","a89dd164","ac9dd164","ad9dd164","ae9dd164","d8a4d164","d9a4d164","daa4d164","dca4d164","dea4d164","dfa4d164","e0a4d164","e1a4d164","e2a4d164","e3a4d164","e4a4d164","e5a4d164","e6a4d164","e7a4d164","e8a4d164","e9a4d164","eaa4d164","eba4d164","eca4d164","eea4d164","efa4d164","f0a4d164","f1a4d164","f2a4d164","f3a4d164","f4a4d164","f5a4d164","f6a4d164","f7a4d164","faa4d164","fba4d164","fca4d164","fda4d164","fea4d164","ffa4d164","80a5d164","81a5d164","82a5d164","83a5d164","84a5d164","85a5d164","86a5d164","87a5d164","88a5d164","89a5d164","8aa5d164","8ba5d164","8ca5d164","c0acd164","c1acd164","c2acd164","c3acd164","c4acd164","c5acd164","c6acd164","c7acd164","c8acd164","c9acd164","caacd164","cbacd164","ccacd164","cdacd164","ceacd164","cfacd164","d0acd164","d1acd164","d2acd164","d3acd164","d4acd164","d5acd164","d6acd164","d7acd164","d9acd164","daacd164","dbacd164","dcacd164","ddacd164","deacd164","dfacd164","e0acd164","e1acd164","e2acd164","e3acd164","e4acd164","e5acd164","e6acd164","e7acd164","e8acd164","e9acd164","eaacd164","ecacd164","edacd164","eeacd164","efacd164","f0acd164","f1acd164","f2acd164","f3acd164","f4acd164","f5acd164","f6acd164","a8b4d164","a9b4d164","aab4d164","abb4d164","acb4d164","adb4d164","aeb4d164","afb4d164","b0b4d164","b1b4d164","b2b4d164","b3b4d164","b4b4d164","b5b4d164","b6b4d164","b7b4d164","b8b4d164","b9b4d164","bab4d164","bbb4d164","bcb4d164","bdb4d164","beb4d164","bfb4d164","c0b4d164","c1b4d164","c2b4d164","c3b4d164","c4b4d164","c5b4d164","c6b4d164","c7b4d164","c8b4d164","c9b4d164","cab4d164","cbb4d164","ccb4d164","cdb4d164","ceb4d164","cfb4d164","d0b4d164","d1b4d164","d2b4d164","d3b4d164","d4b4d164","d5b4d164","d6b4d164","d7b4d164","d8b4d164","d9b4d164","dab4d164","dbb4d164","dcb4d164","ddb4d164","dfb4d164","e0b4d164","e1b4d164","e2b4d164","e3b4d164","e4b4d164","e7b4d164","90bcd164","91bcd164","92bcd164","93bcd164","94bcd164","95bcd164","96bcd164","97bcd164","98bcd164","99bcd164","9abcd164","9bbcd164","9cbcd164","9dbcd164","9ebcd164","9fbcd164","a0bcd164","a1bcd164","a2bcd164","a3bcd164","a4bcd164","a5bcd164","a6bcd164","a7bcd164","a8bcd164","a9bcd164","aabcd164","abbcd164","acbcd164","adbcd164","aebcd164","afbcd164","b0bcd164","b1bcd164","b2bcd164","b3bcd164","b4bcd164","b5bcd164","b6bcd164","b7bcd164","b8bcd164","b9bcd164","babcd164","bbbcd164","bcbcd164","bdbcd164","bebcd164","bfbcd164","eabcd164","ebbcd164","ecbcd164","edbcd164","eebcd164","efbcd164","f0bcd164","80ba8b65","80c38566","81c38566","82c38566","83c38566","84c38566","85c38566","86c38566","87c38566","88c38566","89c38566","8ac38566","8bc38566","8cc38566","8dc38566","8ec38566","8fc38566","90c38566","91c38566","92c38566","93c38566","94c38566","95c38566","96c38566","97c38566","98c38566","99c38566","9ac38566","9bc38566","9cc38566","9dc38566","9ec38566","9fc38566","a0c38566","a1c38566","a2c38566","a3c38566","a4c38566","a5c38566","a6c38566","a7c38566","a8c38566","a9c38566","adc38566","aec38566","afc38566","b0c38566","b1c38566","b2c38566","b3c38566","b4c38566","b5c38566","b6c38566","b8c38566","b9c38566","bac38566","bcc38566","bdc38566","bec38566","bfc38566","c0c38566","c1c38566","c2c38566","c3c38566","c4c38566","c5c38566","c6c38566","c7c38566","c8c38566","c9c38566","cac38566","cdc38566","cec38566","cfc38566","d0c38566","d1c38566","d2c38566","d3c38566","d4c38566","d5c38566","d6c38566","d7c38566","d8c38566","d9c38566","dac38566","dbc38566","dcc38566","ddc38566","dec38566","dfc38566","e0c38566","e1c38566","e2c38566","e3c38566","e4c38566","e5c38566","e6c38566","e7c38566","e8c38566","e9c38566","eac38566","ebc38566","ecc38566","edc38566","eec38566","efc38566","f0c38566","f1c38566","f2c38566","f3c38566","f4c38566","f5c38566","f6c38566","f7c38566","f8c38566","f9c38566","fac38566","fbc38566","fcc38566","fdc38566","fec38566","ffc38566","80c48566","81c48566","82c48566","83c48566","84c48566","85c48566","86c48566","87c48566","88c48566","89c48566","8ac48566","8bc48566","8cc48566","8dc48566","8ec48566","8fc48566","90c48566","e9c48766","eac48766","ebc48766","ecc48766","edc48766","eec48766","efc48766","f0c48766","f1c48766","f2c48766","f3c48766","f4c48766","f5c48766","f6c48766","f7c48766","f8c48766","d1cc8766","d2cc8766","d3cc8766","d4cc8766","d6cc8766","d7cc8766","d8cc8766","d9cc8766","dacc8766","dbcc8766","dccc8766","ddcc8766","decc8766","dfcc8766","e0cc8766","e1cc8766","e2cc8766","b9d48766","bad48766","bbd48766","bcd48766","bdd48766","bed48766","bfd48766","c0d48766","c1d48766","c2d48766","c3d48766","c4d48766","c5d48766","c6d48766","c7d48766","a0dc8766","a1dc8766","a2dc8766","a3dc8766","a4dc8766","a5dc8766","a6dc8766","a7dc8766","a8dc8766","aadc8766","abdc8766","88e48766","89e48766","8ae48766","8be48766","8ce48766","8de48766","8fe48766","92e48766","93e48766","94e48766","95e48766","96e48766","97e48766","98e48766","f0eb8766","f1eb8766","f2eb8766","f3eb8766","f4eb8766","f5eb8766","f6eb8766","f7eb8766","f8eb8766","f9eb8766","faeb8766","fbeb8766","feeb8766","d8f38766","d9f38766","daf38766","dbf38766","dcf38766","ddf38766","def38766","dff38766","e0f38766","e1f38766","e2f38766","e3f38766","e4f38766","e5f38766","e6f38766","e7f38766","c0fb8766","c1fb8766","c2fb8766","c3fb8766","c7fb8766","c8fb8766","c9fb8766","cafb8766","a8838866","a9838866","aa838866","ab838866","ac838866","ad838866","ae838866","af838866","b0838866","b1838866","b2838866","908b8866","918b8866","928b8866","938b8866","948b8866","958b8866","968b8866","978b8866","988b8866","998b8866","9a8b8866","9b8b8866","9c8b8866","9d8b8866","f8928866","f9928866","fa928866","fb928866","fc928866","fd928866","fe928866","ff928866","80938866","81938866","82938866","83938866","84938866","e09a8866","e19a8866","e29a8866","e39a8866","e49a8866","e59a8866","e69a8866","e79a8866","e89a8866","e99a8866","ea9a8866","c8a28866","c9a28866","caa28866","cba28866","cca28866","cda28866","b0aa8866","b1aa8866","b2aa8866","b3aa8866","b4aa8866","b5aa8866","b6aa8866","b7aa8866","b8aa8866","b9aa8866","98b28866","99b28866","9ab28866","9bb28866","9cb28866","9db28866","9eb28866","80ba8866","81ba8866","82ba8866","83ba8866","84ba8866","85ba8866","86ba8866","87ba8866","88ba8866","e8c18866","e9c18866","eac18866","ebc18866","ecc18866","edc18866","eec18866","efc18866","f0c18866","f1c18866","d0c98866","d1c98866","d2c98866","d3c98866","d4c98866","d5c98866","d6c98866","d7c98866","d8c98866","d9c98866","dac98866","dbc98866","c1c1c98e01","c08da7b803","c18da7b803"

    ]

        if not hasattr(self, "sock_lock"):
            self.sock_lock = threading.Lock()

        if not hasattr(self, "connect_sock"):
            def connect_sock():
                try:
                    if getattr(self, "sock0500", None):
                        self.sock0500.close()
                    self.sock0500 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock0500.connect(("127.0.0.1", 3000))
                    print("[+] Connected to 127.0.0.1:3000")
                except Exception as e:
                    print(f"[!] Failed to connect -> {e}")
                    self.sock0500 = None
            self.connect_sock = connect_sock

    # نروح مباشرة على الإرسال
        for id_skin in skins:
            ent_packet = f"080000002608{idd}100820062a1a0a1808{id_skin}100120ffffffffffffffffff01280138014002"

            if not getattr(self, "sock0500", None):
                print("[!] No active connection, skipping packet.")
                continue
    
            try:
                with self.sock_lock:
                    self.sock0500.send(bytes.fromhex(ent_packet))
                print(f"[+] Packet sent with id_skin={id_skin}")
                time.sleep(0.001)
            except Exception as e:
                print(f"[!] Error sending packet with id_skin={id_skin} -> {e}")
                self.connect_sock()
                time.sleep(1)



###############################                   
    def suuper(self, idd):
    
        super = [
    "8291eab303","8391eab303","f1b9ecb303","d9c1ecb303","91d9ecb303","e1e8ecb303","9980edb303","9a80edb303","8188edb303","d197edb303"

    ]

        if not hasattr(self, "sock_lock"):
            self.sock_lock = threading.Lock()

        if not hasattr(self, "connect_sock"):
            def connect_sock():
                try:
                    if getattr(self, "sock0500", None):
                        self.sock0500.close()
                    self.sock0500 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock0500.connect(("127.0.0.1", 3000))
                    print("[+] Connected to 127.0.0.1:3000")
                except Exception as e:
                    print(f"[!] Failed to connect -> {e}")
                    self.sock0500 = None
            self.connect_sock = connect_sock

    # نروح مباشرة على الإرسال
        for id_super in super:
            ent_packet = f"080000003208{idd}100820062a260a2408{id_super}100118e5e786c70620ffffffffffffffffff01280130809a9e0138024009"

            if not getattr(self, "sock0500", None):
                print("[!] No active connection, skipping packet.")
                continue
    
            try:
                with self.sock_lock:
                    self.sock0500.send(bytes.fromhex(ent_packet))
                print(f"[+] Packet sent with id_super={id_super}")
                time.sleep(0.001)
            except Exception as e:
                print(f"[!] Error sending packet with id_super={id_super} -> {e}")
                self.connect_sock()
                time.sleep(5.5)

###############################                   
    def daance(self, idd):
    
        entdance = [
    "b2eff2b203","aac8f2b203","cae7f2b203","a2a1f2b203","8ca9f2b203","bc99f2b203","b999f2b203","ba99f2b203","d191f2b203","8588f0b203","8288f0b203","8188f0b203"


    ]

        if not hasattr(self, "sock_lock"):
            self.sock_lock = threading.Lock()

        if not hasattr(self, "connect_sock"):
            def connect_sock():
                try:
                    if getattr(self, "sock0500", None):
                        self.sock0500.close()
                    self.sock0500 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock0500.connect(("127.0.0.1", 3000))
                    print("[+] Connected to 127.0.0.1:3000")
                except Exception as e:
                    print(f"[!] Failed to connect -> {e}")
                    self.sock0500 = None
            self.connect_sock = connect_sock

    # نروح مباشرة على الإرسال
        for id_dance in entdance:
            ent_packet = f"080000003208{idd}100820062a260a2408{id_dance}100118e5e786c70620ffffffffffffffffff01280130809a9e0138024009"

            if not getattr(self, "sock0500", None):
                print("[!] No active connection, skipping packet.")
                continue
    
            try:
                with self.sock_lock:
                    self.sock0500.send(bytes.fromhex(ent_packet))
                print(f"[+] Packet sent with id_dance={id_dance}")
                time.sleep(0.001)
            except Exception as e:
                print(f"[!] Error sending packet with id_dance={id_dance} -> {e}")
                self.connect_sock()
                time.sleep(5)
                                          
################################
###############################

    def YearsOld7(self):
        ent_packet = f"12000000F308{self.EncryptedPlayerid}101220022AE60108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}2883BBBCC40642247B225469746C654944223A3930343039303032372C2274797065223A225469746C65227D4A520A13E29DBC2ECFBB2EE29DBCE385A4524544464F5810EDB58FAE0318B1B1D2AD0320C10228C3B7F8B10338024214E3808E4164E3808FC39FC581C398C48CCCA3C6986A00720C08{self.EncryptedPlayerid}10011A0210155202656E6A520A4C68747470733A2F2F67726170682E66616365626F6F6B2E636F6D2F76392E302F3131393337333137393632373538352F706963747572653F77696474683D313630266865696768743D313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")
            
            
    def YearsOld6(self):
        ent_packet = f"12000000F308{self.EncryptedPlayerid}101220022AE60108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}2883BBBCC40642247B225469746C654944223A3930343039303032362C2274797065223A225469746C65227D4A520A13E29DBC2ECFBB2EE29DBCE385A4524544464F5810EDB58FAE0318B1B1D2AD0320C10228C3B7F8B10338024214E3808E4164E3808FC39FC581C398C48CCCA3C6986A00720C08{self.EncryptedPlayerid}10011A0210155202656E6A520A4C68747470733A2F2F67726170682E66616365626F6F6B2E636F6D2F76392E302F3131393337333137393632373538352F706963747572653F77696474683D313630266865696768743D313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")
                                          

#################################


    def gen_squad6(self, id):
        ent_packet = f"050000032708{id}100520082a9a0608dbdcd7cb251a910608{id}12024d4518012005329d0508{id}121ee28094cd9ecd9fcd9ee29885efbcb6efbca5efbcaeefbcafefbcade385a41a024d4520ebdd88b90628363087cbd1303832421880c38566949be061e1cea561b793e66080a89763e5bfce64480150d60158991468b7db8dae037a05ab93c5b00382011f08d1daf1eb0412054f75656973180420d487d4f0042a0808cc9d85f304100392010b0107090a0b12191a1e20229801db01a0014fc00101d001ada48aaf03e80101880203920208c205d628ae2db202aa02050801109c44aa0208080210ea3018c413aa0208080f10d836188827aa0205081710bd33aa0205082b10e432aa0205083910a070aa0205083d10c16faa02050849108439aa0205081810d836aa0205081a10d836aa0205081c10d836aa0205082010d836aa0205082210d836aa0205082110d836aa0205082310d836aa0205083110e432aa0205084110d836aa0205084d10e432aa0205081b10d836aa0205083410d836aa0205082810e432aa0205082910e432c202cd0112041a0201041a730848121301040506070203f1a802f4a802f2a802f3a8021a0b080110031886032086ac021a0b0802100418810420c59a081a0b0803100418da0620ecb4051a06080520f5ec021a0d08f1a802100318b80320def0041a0d08f2a802100318bc0520d0e90a1a0d08f3a802100318ef032092c9051a1208501201631a0b0863100e188f0420eeba0d1a1b0851120265661a09086520a6910128e7021a08086620822d289e05221f121d65ed0e890ed9049103f503ad02f90abd05e907a1068507cd08950ab109d802a6a38daf03ea020410011801f202080885cab5ee01105c8a0300920300980398e0b3af0ba20319efbca334e385a4eaa884e385a4efbcb4efbca5efbca1efbcada80368b00301c2030a081c100f180320052801e203014fea03003a011a403e50056801721e313733303239333438313635343436323834305f6c646a72387477723378880180909beaf3d18fd919a20100b001e201ea010449444331fa011e313733303239333438313635343436363239355f6f747735637831756c6d050000031e08{id}1005203a2a910608{id}12024d4518012005329d0508{id}121ee28094cd9ecd9fcd9ee29885efbcb6efbca5efbcaeefbcafefbcade385a41a024d4520ebdd88b90628363087cbd1303832421880c38566949be061e1cea561b793e66080a89763e5bfce64480150d60158991468b7db8dae037a05ab93c5b00382011f08d1daf1eb0412054f75656973180420d487d4f0042a0808cc9d85f304100392010b0107090a0b12191a1e20229801db01a0014fc00101d001ada48aaf03e80101880203920208c205d628ae2db202aa02050801109c44aa0208080210ea3018c413aa0208080f10d836188827aa0205081710bd33aa0205082b10e432aa0205083910a070aa0205083d10c16faa02050849108439aa0205081810d836aa0205081a10d836aa0205081c10d836aa0205082010d836aa0205082210d836aa0205082110d836aa0205082310d836aa0205083110e432aa0205084110d836aa0205084d10e432aa0205081b10d836aa0205083410d836aa0205082810e432aa0205082910e432c202cd0112041a0201041a730848121301040506070203f1a802f4a802f2a802f3a8021a0b080110031886032086ac021a0b0802100418810420c59a081a0b0803100418da0620ecb4051a06080520f5ec021a0d08f1a802100318b80320def0041a0d08f2a802100318bc0520d0e90a1a0d08f3a802100318ef032092c9051a1208501201631a0b0863100e188f0420eeba0d1a1b0851120265661a09086520a6910128e7021a08086620822d289e05221f121d65ed0e890ed9049103f503ad02f90abd05e907a1068507cd08950ab109d802a6a38daf03ea020410011801f202080885cab5ee01105c8a0300920300980398e0b3af0ba20319efbca334e385a4eaa884e385a4efbcb4efbca5efbca1efbcada80368b00301c2030a081c100f180320052801e203014fea03003a011a403e50056801721e313733303239333438313635343436323834305f6c646a72387477723378880180909beaf3d18fd919a20100b001e201ea010449444331fa011e313733303239333438313635343436363239355f6f747735637831756c6d"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")




#################################



    def gen_squad3(self):
        ent_packet = f"050000030908{id}1005203a2afc0508{id}12024d451801200232880508{id}1215d8a3d8add881d985d8af4dcda23134e2bc83e29cbf1a024d452093e6c7be0628343084cbd1304218c59be061cc91e6608b9dd164c197a361c8bcce6480c38566480150b60258ed0f6096d9d0ad0368f28390ae037a05acd5cab00382012808f6daf1eb04120ed8b9d980d985d8a7d986d980d98a180720b888d4f0042a0808d19d85f30410039201090107090a0b12191a209801db01a0015aa801d9aff8b103ba010a08b985fe902310011864c00101e80101880208920208b930ea079215b810aa020a080110e43218807d2001aa02050802109035aa020a080f10e43218807d2001aa0205081710be4eaa0205081810b83caa0205081c108139aa0205082010a539aa0205082110e83caa0205082210c63baa0205082b10de3aaa0205083110f02eaa0205083910e052aa02050849109633aa0205081a10e432aa0205082310e432aa0205083d10e432aa0205084110e432aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810c03eaa0205082910e432c2022712031a01011a0f0848120b0104050607f1a802f4a8021a0508501201631a060851120265662200d802a8a38daf03ea020410011801f202080883cab5ee01101b8a03009203009803b198b0b10ba20324efbca7efbca8efbcafefbcb3efbcb4e385a4efbcb4efbca5efbca1efbcade385a4e1b6abc2030a082c1001180320012801c2030a081e100f180320092801ca030a080210eec9d3be061801ca030a080410ba83d3be061805ca030a080510ddb1cdbe061801ca030a080610eec9d3be061801ca030a080b10df9ccdbe061807e203024f52ea0300f20300800464900402aa040408011001aa040408011003aa0411080f1d87b1da3f25e8e7673e2d7683293f3a011a403e50056801721e313734313831323439373339303930373138355f6b663530687473786e638801829080dae083f9ae1aa20100b001e301ea010449444331fa011e313734313831323439373339303931303033375f6b7865696d7a7a72726c"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")

#################################



    def gen_spy(self):
        spy_packet = "050000040108c8f0dacb08100520062af40708d0b8d0a53012024d451801200332c90408d0b8d0a530121a544fe385a4efbcb3efbd81efbd8cefbd81efbd8defbd8fe29cb01a024d452087b68faa06284030a9cbd13038324218dcf38766f4aae860efb7ce64e39ba361e99fe061e8b6ce64480150d30158b9106886db8dae037a05b38ec5b00382011d08efdaf1eb041203357635180620f087d4f0042a0808c89d85f30410038801c2ffc4b00392010c0107090a0b1216191a1e20239801d501a00131a80185fff5b103c00101c80101e80101880203920208b930e532fe0ac205aa020a080110a84618807d2003aa0208080210fa3318f403aa0208080f109b7118904eaa0205081710e751aa0205081810ba41aa0205081a10c435aa0205081b109b71aa0205081c109539aa0205082010d338aa0205082110f736aa0205082210c435aa0205082b108835aa02050823109b71aa02050831108835aa02050839109b71aa0205083d109b71aa02050841109b71aa0205084910e432aa0205084d10e432aa02050834109b71aa0205082810e432aa0205082910e432b00201c2024012041a0201041a21084812060104050607021a0b08011003189b0320bc9b011a08080210022092ed021a0508501201631a0508511201652207120565ed0e890ed802a9a38daf03ea02520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3339303835333639383032393935362f706963747572653f77696474683d313630266865696768743d31363010011801f202090882cab5ee0110f9028a03060802100218059203009803f7c282ac0ba2030c2144454144e385a4484f4d4532d30208c8f0dacb08120b544f502d464952452d50431a024d45208cb68faa0628043085cbd13038324218c09ae061c0b5ce64c091e66080c3856680a897638096a361480150c90158e80792010601090a1219209801c901c00101c80101e801018802049202059603000000aa0208080110ff34188064aa020b080f10fd3218b086012001aa0205080210e432aa0205081810fd32aa0205081a10fd32aa0205081c10fd32aa0205082010fd32aa0205082210fd32aa0205082110fd32aa0205081710e432aa0205082310fd32aa0205082b10fd32aa0205083110fd32aa0205083910fd32aa0205083d10fd32aa0205084110fd32aa0205084910d836aa0205084d10e432aa0205081b10fd32aa0205083410fd32aa0205082810e432aa0205082910e432c2022112041a0201041a0508501201631a0508511201651a090848120501040506072200ea0204100118018a03009203003a0101400150016801721e313639383934353830303230323738373034345f346a7867796f626e397988018190ae92d194c8ef17a20100a80101b001e001ea010449444331"

        if self.sock0500:
            self.sock0500.send(bytes.fromhex(spy_packet))
        else:
            print("[!] sock0500 not assigned.")


    def gen_sqz(self):
        spy_packet = "0315000001c06c03e17766c196a7e5734b2ffc686550e2f36b0582a92cde34b8dd2fa1447f900cf94ed69fc8214ea2974452331d769dcc1ccfac654a5ac6cedd5c049e30c124a3790970ecc0f5937a841a6c61781ce368a854c6ea9d52ed3e585f9dae5b09c3a8f20f5616dcbf6b09866dde0ecd468f343bbcf8fc8e64e8a4baa04a0055429b80b7a9c3c9dcb1154cb59332ffe0ee01f2ea048357e3994e463248f86d00583617a191ea3a04ba6654c814f0d6cb62e132a68e633bb7dbc3f71dbdeba9eff0d2a67052c74e9ebfc5b31205274c2abfe1bd0d6ed9d6945ef548ed8c60848e4e79b43f4abff0db31cd216455f5d718dc4463c52c9c2453f52d0645bb14275167cd4dfc51dcd633d39a2dff56cea674351bbf1ed637677c05d203017bbf1cb5032cf02e298b800d625c998d49caadad1bf6899e37425b58a7c5171fc213647648422ae0e7fa57432cd9b2e03b2a333b9456c7de61e1af62c0bd1f66e1071ddd346c10c01ea92db82acd90f75964fecec88be8388bdd2a7b0e6e7cd5bbd425e54e0b7a54587bc975758dca65dcf1630090e23efdc62f8f82fadeeac71ba4ca68410d60b50a9d81140f6db1f2cc0bc54258ef0ca9e6377656a1985c468d812bde7ae1"

        if self.sock0500:
            self.sock0500.send(bytes.fromhex(spy_packet))
        else:
            print("[!] sock0500 not assigned.")

 
            
            
#################################

            

    def gen_dm(self, player_id):
        dm_packet = f"080000001608{player_id}100820022a0a08e7be0110b24f18c801"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(dm_packet))
        else:
            print("[!] sock0500 not assigned.")
    

#################################
    


    def gen_gold(self, player_id):
        gold_packet = f"080000001308{player_id}100820022a0708a6b10318fa01"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(gold_packet))
        else:
            print("[!] sock0500 not assigned.")
                                 


################################# 



    def gen_spyroom(self):
        spyroom_packet = "0e1500000050d6d519002bdcc64de8a42c1aaedf5c3aaacf7ce694efbfc1f11f026809b625e793614dd13ffa38eecc554ff320a61b8ac69699a8eb5edab73b39e9d9107a50d5e083a2bc8c01fbad64dbce6b8581cd50"
        if self.op:
            self.op.send(bytes.fromhex(spyroom_packet))
        else:
            print("[!] op not assigned.")
            


#################################



    def send_yout_list(self):
        if not self.sock0500:
            print("[!] sock0500 not assigned.")
            return

        for i, packet in enumerate(self.yout_list):
            try:
                self.sock0500.send(packet)
                time.sleep(0.1)
            except Exception as e:
                print(f"[!] Error sending packet {i+1}: {e}")
            


#################################

    
                                
    def exchange_loop(self, client, remote):
        global inviteD
        global back
        global RbGx
        global encid
        global enc_id

        while True:
            r, w, e = select.select([client, remote], [], [])

            if client in r:
                dataC = client.recv(4096)

                if "39699" in str(remote):
                    self.op = remote
                if "39801" in str(remote):
                    self.xz = remote

                if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 820 and inviteD == True:
                    for i in range(10):
                        for _ in range(15):
                            remote.send(dataC)
                            time.sleep(0.04)
                            time.sleep(0.2)

                if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 141:
                    self.data_join = dataC

                if remote.send(dataC) <= 0:
                    break
            if remote in r:
                data = remote.recv(4096)
               
    

#################################

                if '1200' in data.hex()[0:4] and b'GroupID' not in data:
                        start_marker = "08"
                        end_marker = "10"
                        start_index = data.hex().find(start_marker) + len(start_marker)
                        end_index = data.hex().find(end_marker, start_index)

                        if start_index != -1 and end_index != -1:
                            enc_client_id = data.hex()[start_index:end_index]
                            self.EncryptedPlayerid = enc_client_id

                        self.squad_gen = self.Encrypt_ID(8763797454)
                        self.squad_gen5 = self.Encrypt_ID(2064377560)
                        self.squad = self.Encrypt_ID(8679231987)

                        print("zix ")
                        self.RbGx = False

                        # ✅ ما يتحقق من الرابط إلا إذا self.RbGx == True

                            

##############################                                    
         
                if "0500" in data.hex()[:4]:
                    self.sock0500 = client
                if "1200" in data.hex()[:4]:
                    self.sock1200 = client
                if "0500" in data.hex()[:4]:
                    self.sock0500 = client

                      
#################################
#امر help

                if '1200' in data.hex()[0:4] and b'@help' in data and not self.RbGx:
                    try:
                        user_id = data.hex()[12:22]
                        full_msg = data.decode('utf-8', errors='ignore')
                        print(f"[HELP/ACTIVATE] Message: {full_msg} from user: {user_id}")
                        
                        # التحقق أولاً إذا كان المستخدم مفعلاً مسبقاً
                        if self.is_user_activated(user_id):
                            print(f"[ACTIVATION] User {user_id} already activated")
                            # إرسال قائمة الأوامر الكاملة
                            help_message = """[b][c][ff00ff][---------------------------------]
[ff0000]BOT[0000ff] CTX [00ffff]PRO

[FFD700]تحويل وضع الفريق 5
[FF2A2A]@5s

[FFD700]تحويل وضع الفريق 3
[FF2A2A]@3s

[FFD700]تحويل وضع الفريق 6
[FF2A2A]@6s

[FFD700]جلب معلومات كاملة للاعب
[FF2A2A]@info 123456xx

[FFD700]تهكير الجواهر
[FF2A2A]@DIAM

[FFD700]سبام دعوات
[FF2A2A]@inv , -inv
 
[FFD700]تهكير الجولد
[FF2A2A]@GOLD
[ff00ff][---------------------------------]"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, help_message)).start()
                            
                            help_message = """[b][c][ff00ff][---------------------------------]
[FFD700]جلب شبح للفريق
[FF2A2A]@Dev

[FFD700]اضافة اليوتيوبر اصدقاء
[FF2A2A]@YT
 
[FFD700]ارسال شارة ستة سنوات
[FF2A2A]@6old
 
[FFD700]ارسال شارة سبع سنوات
[FF2A2A]@7old
 
[FFD700]دخول الخفي في روم
[FF2A2A]@spyroom
 
[FFD700]دخول المخفي في فريق 
[FF2A2A]@spy

[FFD700]دخول ضاهر للفريق
[FF2A2A]@sqwad
[b][c][ff00ff][---------------------------------]"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, help_message)).start()                          
                            
                            help_message = """[b][c][ff00ff][---------------------------------]
[FFD700]جلب لاعب صديق عبر ايدي
[FF2A2A]++ 123456xx

[FFD700]ارسال اشباح عبر التيم كود
[FF2A2A]@ghost team_code ZIX 

[FFD700]ارسال رسائل عبر التيم كود
[FF2A2A]@msg team_code ZIX

[FFD700]ترقيص الاعبين عبر الايدي
[FF2A2A]@dens team_code 123456xx 1~409 1-3

[FFD700]رقصات إيفو
[FF2A2A]@evo team_code 123456xx 1~409 1-3

[FFD700]تفعيل وضع علامة بيسي بحسابك
[FF2A2A]@pc

[FFD700]سكنات كاملة
[FF2A2A]@skin
[b][c][ff00ff][---------------------------------]"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, help_message)).start()  
                            
                            help_message = """[b][c][ff00ff][---------------------------------]
[FFD700]رقصات تحول
[FF2A2A]@super

[FFD700]رقصات عادية
[FF2A2A]@entdnc

[FFD700]جلب لاعب للفريق عبر الايدي
[FF2A2A]@Get 123456xx 

[FFD700]ارسال طلبات صداقة
[FF2A2A]@som 123456xx

[FFD700]مقبرة سبام روم
[FF2A2A]@room 123456xx 

[FFD700]زيادة لفل ذئب الوحيد
[FF2A2A]@lvl

[FFD700]ارسال مقبرة للفريق
[FF2A2A]@dm
[b][c][ff00ff][---------------------------------]"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, help_message)).start() 
                            
                            help_message = """[b][c][ff00ff][---------------------------------]
[FFD700]جلب اسلحة مطورة
[FF2A2A]@gvo

[FFD700]ارسال زوار للاعب
[FF2A2A]@visit 123456xx

[FFD700]ارسال لايكات 
[FF2A2A]@likes 123456xx

[FFD700]جلب معلومات الكلان كاملة
[FF2A2A]@clan 123456xx

[FFD700]فحص حظر الاعب
[FF2A2A]@check 123456xx

[FFD700]حالة كود التفعيل لديك
[FF2A2A]@status
[b][c][ff00ff][---------------------------------]"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, help_message)).start() 
                            
                            help_message = """[b][c][ff00ff][---------------------------------]
[ff0000]قائمة ترقيص
[00ff00]@dance1
@dance2
@dance3
@dance4
@dance5
@dance6
@dance7
@dance8
@dance9
@dance10
@dance11
@dance12
@dance13
@dance14
@dance15
@dance16
@dance17
@dance18
[b][c][ff00ff][---------------------------------]"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, help_message)).start()
                            
                            help_message = """[b][c][ff00ff][---------------------------------]
[FFD700]قائمة البروكسي
[FF0000]@proxy1
@proxy2
@proxy3
@proxy4
@proxy5
@proxy6
@proxy7
@proxyvip
@bot
@box
[b][c][ff00ff][---------------------------------]"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, help_message)).start()
                            
                            help_message = """[b][c][ff00ff][---------------------------------]
[FFD700]ملابس في الفريق
[FF2A2A]@skin1
@skin2
@skin3
@skin4
@skin5
@skin6
@skin7
[b][c][ff00ff][---------------------------------]"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, help_message)).start()                                                                    



#[FFFFFF] ارسال زوار للاعب
#[FF00CC]@visit 123456xx

                        
                        else:
                            # استخراج الكود إذا كان موجوداً
                            import re
                            match = re.search(r'@help\s+(\w+)', full_msg)
                            
                            if match:
                                code = match.group(1)
                                print(f"[ff00ff][ACTIVATE] Attempting to activate with code: {code}")
                                
                                # رسالة انتظار
                                wait_msg = "[FFFF00]جاري التحقق من كود التفعيل...[FFFF00]..."
                                threading.Thread(target=self.gen_zixhelp, args=(user_id, wait_msg)).start()
                                
                                # التحقق من الكود
                                result = self.check_firebase_code(code, user_id)
                                
                                if result["valid"]:
                                    # تفعيل المستخدم وحفظه مع تاريخ الانتهاء
                                    self.save_activated_user(user_id, result["expire"])
                                    
                                    # إرسال رسالة نجاح مع الوقت
                                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    success_msg = f"""[b][c][00FF00]════════════════════════════════════════
✓ تم التفعيل بنجاح

[ff0000]وقت التفعيل: {current_time}

[00ffff]تاريخ الانتهاء: {result['expire']}

جميع الأوامر متاحة الآن
استخدم @help مرة أخرى لعرض القائمة
[00FF00]════════════════════════════════════════"""
                                    
                                    threading.Thread(target=self.gen_zixhelp, args=(user_id, success_msg)).start()
                                    print(f"[b][c][ff00ff][ACTIVATION] User {user_id} activated successfully until {result['expire']}")
                                else:
                                    # رسالة خطأ حسب السبب
                                    if result["reason"] == "invalid":
                                        error_msg = """[b][c][FF0000]════════════════════════════════════════
✗ كود التفعيل غير صحيح

 تأكد من الكود وحاول مرة أخرى
[b][c][FF0000]════════════════════════════════════════"""
                                    elif result["reason"] == "expired":
                                        error_msg = """[b][c][FF0000]════════════════════════════════════════
✗ الكود منتهي الصلاحية

 يرجى الحصول على كود جديد
[b][c][FF0000]════════════════════════════════════════"""
                                    elif result["reason"] == "limit_reached":
                                        error_msg = """[b][c][FF0000]════════════════════════════════════════
✗ الكود وصل للحد الأقصى

 يرجى الحصول على كود جديد
[b][c][FF0000]════════════════════════════════════════"""
                                    else:
                                        error_msg = """[b][c][FF0000]════════════════════════════════════════
✗ خطأ في الاتصال

 حدث خطأ أثناء التحقق من الكود
[b][c][FF0000]════════════════════════════════════════"""
                                    
                                    threading.Thread(target=self.gen_zixhelp, args=(user_id, error_msg)).start()
                                    print(f"[b][c][ff0000][ACTIVATION] Failed for user {user_id}: {result['reason']}")
                            else:
                                # لم يكتب كوداً، أرسل رسالة تطلب الكود مع الوقت
                                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                request_msg = f"""[b][c][FFFF00]════════════════════════════════════════
اذهب إلى المطور لجلب كود                                
                                
! البوت يحتاج إلى تفعيل

 الوقت الان: {current_time}

 استخدم: @help [كود التفعيل]
مثال: @help ZIX-CTX-75VK-86G8
[FFFF00]════════════════════════════════════════"""
                                threading.Thread(target=self.gen_zixhelp, args=(user_id, request_msg)).start()
                        
                    except Exception as e:
                        print(f"خطأ في @help/activate: {e}")
                        import traceback
                        traceback.print_exc()

                # ===== أمر التحقق من حالة التفعيل =====
                # ===== جميع الأوامر مع رسالة تأكيد =====

                # ===== أمر @sqwad =====
                if '1200' in data.hex()[0:4] and b'@sqwad' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @sqwad بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.gen_sqz).start()

                # ===== أمر @spy =====
                if '1200' in data.hex()[0:4] and b'@spy' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @spy بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.gen_spy).start()

                # ===== أمر ++ =====
                if '1200' in data.hex()[0:4] and b'++' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر ++ بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    i = str(data).split('++')[1]
                    if '***' in i:
                        i = i.replace('***', '106')
                    id = str(i).split('(\\x')[0]
                    id = self.Encrypt_ID(id)
                    self.fake_friend(self.sock0500, id)

                # ===== أمر @DIAM =====
                if b"@DIAM" in data and self.comand and not self.RbGx:
                    player_id = data.hex()[12:22]
                    if not self.is_user_activated(player_id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(player_id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @DIAM بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(player_id, confirm_msg)).start()
                    threading.Thread(target=self.gen_dm, args=(player_id,)).start()

                # ===== أمر @GOLD =====
                if b"@GOLD" in data and self.comand and not self.RbGx:
                    player_id = data.hex()[12:22]
                    if not self.is_user_activated(player_id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(player_id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @GOLD بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(player_id, confirm_msg)).start()
                    threading.Thread(target=self.gen_gold, args=(player_id,)).start()

                # ===== أمر @spyroom =====
                if b"@spyroom" in data and self.comand and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @spyroom بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.gen_spyroom).start()

                # ===== أمر @YT =====
                if b"@YT" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @YT بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.send_yout_list).start()

                # ===== أمر @7old =====
                if '1200' in data.hex()[0:4] and b'@7old' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @7old بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.YearsOld7).start()

                # ===== أمر @6old =====
                if '1200' in data.hex()[0:4] and b'@6old' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @6old بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.YearsOld6).start()

                # ===== أمر @6s =====
                if '1200' in data.hex()[0:4] and b'@6s' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @6s بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.gen_squad6, args=(id,)).start()

                # ===== أمر @skin =====
                if '1200' in data.hex()[0:4] and b'@skin' in data and not self.RbGx:
                    idd = data.hex()[12:22]
                    if not self.is_user_activated(idd):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(idd, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @skin بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(idd, confirm_msg)).start()
                    threading.Thread(target=self.skinaaaat, args=(idd,)).start()

                # ===== أمر @super =====
                if '1200' in data.hex()[0:4] and b'@super' in data and not self.RbGx:
                    idd = data.hex()[12:22]
                    if not self.is_user_activated(idd):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(idd, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @super بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(idd, confirm_msg)).start()
                    threading.Thread(target=self.suuper, args=(idd,)).start()

                # ===== أمر @entdnc =====
                if '1200' in data.hex()[0:4] and b'@entdnc' in data and not self.RbGx:
                    idd = data.hex()[12:22]
                    if not self.is_user_activated(idd):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(idd, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @entdnc بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(idd, confirm_msg)).start()
                    threading.Thread(target=self.daance, args=(idd,)).start()

                # ===== أمر @pc =====
                if '1200' in data.hex()[0:4] and b'@pc' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @pc بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.pc, args=(id,)).start()

                # ===== أمر @5s =====
                if '1200' in data.hex()[0:4] and b'@5s' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @5s بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.gen_squad5, args=(id,)).start()

                # ===== أمر @ghost =====
                if '1200' in data.hex()[0:4] and b'@ghost' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @ghost بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.ghost_command, args=(data,)).start()

                # ===== أمر @likes =====
                if '1200' in data.hex()[0:4] and b'@likes' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم زيادة لايكات بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    print("[LIKES] Command !")
                    threading.Thread(target=self.likes_command, args=(data,)).start()

                # ===== أمر @som =====
                if '1200' in data.hex()[0:4] and b'@som' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم ارسال سبا صداقة بنجاح [00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    print("[LIKES] Command !")
                    threading.Thread(target=self.spam_command, args=(data,)).start()

                if '1200' in data.hex()[0:4] and b'@room' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم ارسال مقبرة سبام بدون توقف لمدة 3 دقائق [00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    print("[LIKES] Command !")
                    threading.Thread(target=self.spam_zix, args=(data,)).start()


                # ===== أمر @msg =====
                if '1200' in data.hex()[0:4] and b'@msg' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @msg بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.msgz_command, args=(data,)).start()

                # ===== أمر @dens =====
                if '1200' in data.hex()[0:4] and b'@dens' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @dens بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    print("[DENS] Command detected in exchange_loop!")
                    threading.Thread(target=self.dens_command, args=(data,)).start()

                # ===== أمر @gvo =====
                if '1200' in data.hex()[0:4] and b'@gvo' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @gvo بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.msgz_command, args=(data,)).start()

                # ===== أمر @Dev =====
                if '1200' in data.hex()[0:4] and b'@Dev' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @Dev بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.Devv, args=(id,)).start()

                # ===== أوامر البروكسي =====
                if b"@proxy1" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @proxy1 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ['d09be660', 'd19be660', 'd29be660', 'd39be660']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy1: {e}")

                if b"@proxy2" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @proxy2 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ["c19ae061", "c29ae061", "c39ae061", "c49ae061"]
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy2: {e}")

                if b"@proxy3" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @proxy3 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ['d49be660', 'd59be660', 'd69be660']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy3: {e}")

                if b"@proxy4" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @proxy4 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ['c1b5ce64', 'c2b5ce64', 'c3b5ce64']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy4: {e}")

                if b"@proxy5" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @proxy5 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ['bebace64', 'f8bfce64', 'f9bfce64', 'fabfce64', 'fbbfce64']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy5: {e}")

                if b"@proxy6" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @proxy6 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ['8196a361', '8296a361']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy6: {e}")

                if b"@proxy7" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @proxy7 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ['81c38566', '82c38566']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy7: {e}")

                if b"@proxyvip" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @proxyvip بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ['a796e660', 'a896e660', 'a996e660', 'aa96e660', 'ab96e660']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxyvip: {e}")

                if b"@bot" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @bot بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ['81fbc6d202', '82fbc6d202', '83fbc6d202']  # يمكن إضافة المزيد
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"08000000be08c0c5cefb18100820062ab1010a1808d885d164100120ffffffffffffffffff012801380140020a1808d985d164100120ffffffffffffffffff012801380140020a1808fe928866100120ffffffffffffffffff012801380140020a1808cfe1e860100120ffffffffffffffffff012801380140020a18088fe6a561100120ffffffffffffffffff012801380140020a1808cfeae261100120ffffffffffffffffff012801380140020a1308{ids}20ffffffffffffffffff013801"))
                            time.sleep(0.16)
                    except Exception as e:
                        print(f"[!] Error in @bot: {e}")

                if b"@box" in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @box بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ['81fd8751', '82fd8751', '83fd8751']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000003a0888d49a9a28100820062a2e0a180896cbd130100120ffffffffffffffffff012801380140010a1208{ids}20ffffffffffffffffff01380108000000150888d49a9a28100820032a090a070896cbd13010010d0000000f0888d49a9a28100d20022a0308ce1a"))
                            time.sleep(0.16)
                    except Exception as e:
                        print(f"[!] Error in @box: {e}")

                # ===== أوامر @skin1-7 =====
                if '1200' in data.hex()[0:4] and b'@skin1' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @skin1 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.skin1, args=(id,)).start()

                if '1200' in data.hex()[0:4] and b'@skin2' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @skin2 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.skin2, args=(id,)).start()

                if '1200' in data.hex()[0:4] and b'@skin3' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @skin3 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.skin3, args=(id,)).start()

                if '1200' in data.hex()[0:4] and b'@skin4' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @skin4 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.skin4, args=(id,)).start()

                if '1200' in data.hex()[0:4] and b'@skin5' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @skin5 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.skin5, args=(id,)).start()

                if '1200' in data.hex()[0:4] and b'@skin6' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @skin6 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.skin6, args=(id,)).start()

                if '1200' in data.hex()[0:4] and b'@skin7' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @skin7 بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.skin7, args=(id,)).start()

                # ===== أمر @3s =====
                if '1200' in data.hex()[0:4] and b'@3s' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @3s بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.gen_squad3, args=(id,)).start()

                # ===== أوامر الرقصات @dance1-18 =====
                dance_commands = ['@dance1', '@dance2', '@dance3', '@dance4', '@dance5', '@dance6', '@dance7', '@dance8', '@dance9', '@dance10', '@dance11', '@dance12', '@dance13', '@dance14', '@dance15', '@dance16', '@dance17', '@dance18']
                for i, cmd in enumerate(dance_commands, 1):
                    if cmd.encode() in data and not self.RbGx:
                        id = data.hex()[12:22]
                        if not self.is_user_activated(id):
                            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                            threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                            continue
                        # رسالة تأكيد
                        confirm_msg = f"[00FF00]✓ تم تنفيذ أمر {cmd} بنجاح[00FF00]"
                        threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                        target_func = getattr(self, f'zix_dens{i}', None)
                        if target_func:
                            threading.Thread(target=target_func, args=(id,)).start()
                        break

                # ===== أمر @inv =====
                if '1200' in data.hex()[0:4] and b'@inv' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @inv بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    inviteD = True

                # ===== أمر -inv =====
                if '1200' in data.hex()[0:4] and b'-inv' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر -inv بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    inviteD = False

                # ===== أمر @skn =====
                if '1200' in data.hex()[0:4] and b'@skn' in data and not self.RbGx:
                    idd = data.hex()[12:22]
                    if not self.is_user_activated(idd):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(idd, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @skn بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(idd, confirm_msg)).start()
                    threading.Thread(target=self.skinaaaat, args=(idd,)).start()
                    
                # ===== أمر @status (بدون رسالة تأكيد) =====
                if '1200' in data.hex()[0:4] and b'@status' in data and not self.RbGx:
                    try:
                        user_id = data.hex()[12:22]
                        
                        if self.is_user_activated(user_id):
                            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            status_msg = f"""[00FF00]════════════════════════════════════════
✓ البوت مفعل

🕐 الوقت الحالي: {current_time}
⚡ جميع الأوامر متاحة
[00FF00]════════════════════════════════════════"""
                        else:
                            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            status_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت الحالي: {current_time}
⚠️ استخدم @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        
                        threading.Thread(target=self.gen_zixhelp, args=(user_id, status_msg)).start()
                        
                    except Exception as e:
                        print(f"خطأ في @status: {e}")

                # ===== أمر @info (بدون رسالة تأكيد - تبقى كما هي) =====
                if '1200' in data.hex()[0:4] and b'@info' in data and not self.RbGx:
                    try:
                        user_id = data.hex()[12:22]
                        if not self.is_user_activated(user_id):
                            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, not_activated_msg)).start()
                            continue
                        
                        full_msg = data.decode('utf-8', errors='ignore')
                        print(f"[INFO] رسالة المعلومات: {full_msg}")
                        
                        import re
                        match = re.search(r'@info\s+(\d+)', full_msg)
                        
                        if match:
                            target_uid = match.group(1)
                            print(f"[INFO] جلب معلومات اللاعب {target_uid} للمستخدم {user_id}")
                            
                            wait_msg = "[FFFF00]⏳ جاري جلب المعلومات...[FFFF00]"
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, wait_msg)).start()
                            
                            info_data = self.fetch_player_info(target_uid)
                            final_message = self.format_info_message(info_data)
                            message_parts = self.split_message(final_message)
                            
                            for part in message_parts:
                                threading.Thread(target=self.gen_zixhelp, args=(user_id, part)).start()
                                time.sleep(0.5)
                                
                        else:
                            error_msg = "[FF0000] خطأ: استخدم @info [UID]\nمثال: @info 2306259016[FF0000]"
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, error_msg)).start()
                            
                    except Exception as e:
                        print(f"خطأ في @info: {e}")
                        import traceback
                        traceback.print_exc()
                        if 'user_id' in locals():
                            error_msg = f"[FF0000] حدث خطأ: {str(e)[:50]}...[FF0000]"
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, error_msg)).start()

                # ===== أمر @check (بدون رسالة تأكيد - تبقى كما هي) =====
                if '1200' in data.hex()[0:4] and b'@check' in data and not self.RbGx:
                    try:
                        user_id = data.hex()[12:22]
                        if not self.is_user_activated(user_id):
                            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, not_activated_msg)).start()
                            continue
                        
                        full_msg = data.decode('utf-8', errors='ignore')
                        print(f"[CHECK] رسالة الفحص: {full_msg}")
                        
                        import re
                        match = re.search(r'@check\s+(\d+)', full_msg)
                        
                        if match:
                            target_uid = match.group(1)
                            print(f"[CHECK] فحص الحظر للاعب {target_uid} للمستخدم {user_id}")
                            
                            wait_msg = "[FFFF00]⏳ جاري فحص حالة الحظر...[FFFF00]"
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, wait_msg)).start()
                            
                            ban_data = self.fetch_ban_status(target_uid)
                            final_message = self.format_ban_message(ban_data)
                            message_parts = self.split_message(final_message)
                            
                            for part in message_parts:
                                threading.Thread(target=self.gen_zixhelp, args=(user_id, part)).start()
                                time.sleep(0.5)
                                
                        else:
                            error_msg = "[FF0000] خطأ: استخدم @check [UID]\nمثال: @check 7555887233[FF0000]"
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, error_msg)).start()
                            
                    except Exception as e:
                        print(f"خطأ في @check: {e}")
                        import traceback
                        traceback.print_exc()
                        if 'user_id' in locals():
                            error_msg = f"[FF0000]حدث خطأ: {str(e)[:50]}...[FF0000]"
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, error_msg)).start()

                # ===== أمر @clan (مع رسالة تأكيد) =====
                if '1200' in data.hex()[0:4] and b'@clan' in data and not self.RbGx:
                    try:
                        user_id = data.hex()[12:22]
                        if not self.is_user_activated(user_id):
                            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, not_activated_msg)).start()
                            continue
                        
                        # رسالة تأكيد
                        confirm_msg = "[00FF00]✓ تم تنفيذ أمر @clan بنجاح[00FF00]"
                        threading.Thread(target=self.gen_zixhelp, args=(user_id, confirm_msg)).start()
                        
                        full_msg = data.decode('utf-8', errors='ignore')
                        print(f"[CLAN] رسالة الكلان: {full_msg}")
                        
                        import re
                        match = re.search(r'@clan\s+(\d+)', full_msg)
                        
                        if match:
                            clan_id = match.group(1)
                            print(f"[CLAN] جلب معلومات الكلان {clan_id} للمستخدم {user_id}")
                            
                            wait_msg = "[FFFF00]⏳ جاري جلب معلومات الكلان...[FFFF00]"
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, wait_msg)).start()
                            
                            clan_data = self.fetch_clan_info(clan_id)
                            final_message = self.format_clan_message(clan_data)
                            message_parts = self.split_message(final_message)
                            
                            for part in message_parts:
                                threading.Thread(target=self.gen_zixhelp, args=(user_id, part)).start()
                                time.sleep(0.5)
                                
                        else:
                            error_msg = "[FF0000]❌ خطأ: استخدم @clan [Clan ID]\nمثال: @clan 3085885666[FF0000]"
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, error_msg)).start()
                            
                    except Exception as e:
                        print(f"خطأ في @clan: {e}")
                        import traceback
                        traceback.print_exc()
                        if 'user_id' in locals():
                            error_msg = f"[FF0000]❌ حدث خطأ: {str(e)[:50]}...[FF0000]"
                            threading.Thread(target=self.gen_zixhelp, args=(user_id, error_msg)).start()

                # ===== أمر @gvo (مع رسالة تأكيد) =====
                if '1200' in data.hex()[0:4] and b'@gvo' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @gvo بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    try:
                        items_ids = ['9181bfb003', '9281bfb003', '9381bfb003', '9481bfb003', '9581bfb003', '9681bfb003', '9781bfb003', '9881bfb003', '9981bfb003', '9a81bfb003', '9b81bfb003', '9c81bfb003', '9d81bfb003', '9e81bfb003', '9f81bfb003', 'a081bfb003', 'a181bfb003', 'a281bfb003', 'a381bfb003', 'a481bfb003', 'a581bfb003', 'a681bfb003', 'a781bfb003', 'a881bfb003', 'c1f1beb003', 'c2f1beb003', 'c3f1beb003', 'c4f1beb003', 'c5f1beb003', 'c6f1beb003', 'c7f1beb003', 'c8f1beb003', 'c9f1beb003', 'caf1beb003', 'cbf1beb003', 'ccf1beb003', 'cdf1beb003', 'cef1beb003', 'cff1beb003', 'd0f1beb003', 'd1f1beb003', 'd2f1beb003', 'd3f1beb003', 'd4f1beb003', 'd5f1beb003', 'd6f1beb003', 'd7f1beb003', 'd8f1beb003', 'd9f1beb003', 'daf1beb003', 'dbf1beb003', 'dcf1beb003', 'ddf1beb003', 'def1beb003', 'dff1beb003', 'e0f1beb003', 'e1f1beb003', 'e2f1beb003', 'e3f1beb003', 'e4f1beb003', 'e5f1beb003', 'e6f1beb003', 'e7f1beb003', 'e8f1beb003', 'e9f1beb003', 'eaf1beb003', 'ebf1beb003', 'ecf1beb003', 'edf1beb003', 'eef1beb003', 'eff1beb003', 'f0f1beb003', 'f1f1beb003', 'f2f1beb003', 'f3f1beb003', 'f4f1beb003', 'f5f1beb003', 'f6f1beb003', 'f7f1beb003', 'f8f1beb003', 'f9f1beb003', 'faf1beb003', 'fbf1beb003', 'fcf1beb003', 'fdf1beb003', 'fef1beb003', 'fff1beb003', '80f2beb003', '81f2beb003', '82f2beb003', '83f2beb003', '84f2beb003', '85f2beb003', '86f2beb003', '87f2beb003', '88f2beb003', '89f2beb003', '8af2beb003', '8bf2beb003', '8cf2beb003', '8df2beb003', '8ef2beb003', '8ff2beb003', '90f2beb003', '91f2beb003', '92f2beb003', '93f2beb003', '94f2beb003', '95f2beb003', '96f2beb003', '97f2beb003', '98f2beb003', '99f2beb003', '9af2beb003', '9bf2beb003', '9cf2beb003', '9dfdbeb003', '9efdbeb003', '9ffdbeb003', 'a0fdbeb003', 'a1fdbeb003', 'a2fdbeb003', 'a3fdbeb003', 'a4fdbeb003', 'a5fdbeb003', 'a6fdbeb003', 'a7fdbeb003', 'a8fdbeb003', 'a9fdbeb003', 'aafdbeb003', 'abfdbeb003', 'acfdbeb003', 'adfdbeb003', 'aefdbeb003', 'affdbeb003', 'b0fdbeb003', 'b1fdbeb003', 'b2fdbeb003', 'b3fdbeb003', 'b4fdbeb003', 'b9fcbeb003', 'bafcbeb003', 'bbfcbeb003', 'bcfcbeb003', 'bdfcbeb003', 'befcbeb003', 'bffcbeb003', 'c0fcbeb003', 'c1fcbeb003', 'c2fcbeb003', 'c3fcbeb003', 'c4fcbeb003', 'c5fcbeb003', 'c6fcbeb003', 'c7fcbeb003', 'c8fcbeb003', 'c9fcbeb003', 'cafcbeb003', 'cbfcbeb003', 'ccfcbeb003', 'cdfcbeb003', 'cefcbeb003', 'cffcbeb003', 'd0fcbeb003', 'd1fcbeb003', 'd2fcbeb003', 'd3fcbeb003', 'd4fcbeb003', 'd5fcbeb003', 'd6fcbeb003', 'd7fcbeb003', 'd8fcbeb003', 'd9fcbeb003', 'dafcbeb003', 'dbfcbeb003', 'dcfcbeb003', 'ddfcbeb003', 'defcbeb003', 'dffcbeb003', 'e0fcbeb003', 'e1fcbeb003', 'e2fcbeb003', 'e3fcbeb003', 'd5fbbeb003', 'd6fbbeb003', 'd7fbbeb003', 'd8fbbeb003', 'd9fbbeb003', 'dafbbeb003', 'dbfbbeb003', 'dcfbbeb003', 'ddfbbeb003', 'defbbeb003', 'dffbbeb003', 'e0fbbeb003', 'e1fbbeb003', 'e2fbbeb003', 'e3fbbeb003', 'e4fbbeb003', 'e5fbbeb003', 'e6fbbeb003', 'e7fbbeb003', '81febeb003', '82febeb003', '83febeb003', '84febeb003', '85febeb003', '86febeb003', '87febeb003', '88febeb003', '89febeb003', '8afebeb003', '8bfebeb003', '8cfebeb003', '8dfebeb003', '8efebeb003', '8ffebeb003', '90febeb003', '91febeb003', '92febeb003', '93febeb003', '94febeb003', '95febeb003', '96febeb003', '97febeb003', '98febeb003', '99febeb003', '9afebeb003', '9bfebeb003', '9cfebeb003', '9dfebeb003', 'e5febeb003', 'e6febeb003', 'e7febeb003', 'e8febeb003', 'e9febeb003', 'eafebeb003', 'ebfebeb003', 'ecfebeb003', 'edfebeb003', 'eefebeb003', 'effebeb003', 'f0febeb003', 'f1febeb003', 'f2febeb003', 'f3febeb003', 'f4febeb003', 'f5febeb003', 'f6febeb003', 'f7febeb003', 'f8febeb003', 'f9febeb003', 'fafebeb003', 'fbfebeb003', 'fcfebeb003', 'c9ffbeb003', 'caffbeb003', 'cbffbeb003', 'ccffbeb003', 'cdffbeb003', 'ceffbeb003', 'cfffbeb003', 'd0ffbeb003', 'd1ffbeb003', 'd2ffbeb003', 'd3ffbeb003', 'd4ffbeb003', 'd5ffbeb003', 'd6ffbeb003', 'd7ffbeb003', 'd8ffbeb003', 'd9ffbeb003', 'daffbeb003', 'dbffbeb003', 'dcffbeb003', 'ddffbeb003', 'deffbeb003', 'dfffbeb003', 'e0ffbeb003', 'ad80bfb003', 'ae80bfb003', 'af80bfb003', 'b080bfb003', 'b180bfb003', 'b280bfb003', 'b380bfb003', 'b480bfb003', 'b580bfb003', 'b680bfb003', 'b780bfb003', 'b880bfb003', 'b980bfb003', 'ba80bfb003', 'bb80bfb003', 'bc80bfb003', 'bd80bfb003', 'be80bfb003', 'bf80bfb003', 'c080bfb003', 'c180bfb003', 'c280bfb003', 'c380bfb003', 'c480bfb003']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000003308e7e8e8ba30100820062a270a2508{ids}100118a5f1bec50620ffffffffffffffffff0128013080e90f380240097003"))
                            time.sleep(0.16)
                    except Exception as e:
                        print(f"[!] Error in @gvo: {e}")

                # ===== أمر @evo (مع رسالة تأكيد) =====
                if '1200' in data.hex()[0:4] and b'@evo' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @evo بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.dens_command, args=(data,)).start()

                # ===== أمر @room (مع رسالة تأكيد) =====
                if '1200' in data.hex()[0:4] and b'@room' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @room بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.gen_spyroom).start()

                # ===== أمر @lvl (مع رسالة تأكيد) =====
                if '1200' in data.hex()[0:4] and b'@lvl' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @lvl بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.msg_zix, args=(id,)).start()

                # ===== أمر @Get (مع رسالة تأكيد) =====
                if '1200' in data.hex()[0:4] and b'@Get' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @Get بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.msg_zix, args=(id,)).start()

                # ===== أمر @visit (مع رسالة تأكيد) =====
                if '1200' in data.hex()[0:4] and b'@visit' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @visit بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.msg_zix, args=(id,)).start()

                # ===== أمر @dm (مع رسالة تأكيد) =====
                if '1200' in data.hex()[0:4] and b'@dm' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    if not self.is_user_activated(id):
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        not_activated_msg = f"""[FF0000]════════════════════════════════════════
✗ البوت غير مفعل

🕐 الوقت: {current_time}
⚠️ يجب تفعيل البوت أولاً
استخدم: @help [كود التفعيل]
[FF0000]════════════════════════════════════════"""
                        threading.Thread(target=self.gen_zixhelp, args=(id, not_activated_msg)).start()
                        continue
                    # رسالة تأكيد
                    confirm_msg = "[00FF00]✓ تم تنفيذ أمر @dm بنجاح[00FF00]"
                    threading.Thread(target=self.gen_zixhelp, args=(id, confirm_msg)).start()
                    threading.Thread(target=self.gen_dm, args=(id,)).start()

                                        
#################################

                
                     
#################################



                    

#################################
                       
            

                                                                        

#################################

                if b"@proxy1" in data and not self.RbGx:
                    try:
                        items_ids = ['a796e660', 'a896e660', 'a996e660', 'aa96e660', 'ab96e660', 'ac96e660', 'ad96e660', 'ae96e660', 'af96e660', 'b096e660', 'b196e660', 'b296e660', 'b396e660', 'b496e660', 'b596e660', 'b696e660', 'b796e660', 'b896e660', 'b996e660', 'ba96e660', 'bb96e660', 'bc96e660', 'bd96e660', 'be96e660', 'bf96e660', 'c096e660', 'c196e660', 'c296e660', 'c396e660', 'c496e660', 'c596e660', 'c696e660', 'c796e660', 'c896e660', 'c996e660', 'ca96e660', 'cb96e660', 'cc96e660', 'cd96e660', 'ce96e660', 'cf96e660', 'd096e660', 'd196e660', 'd296e660', 'd396e660', 'd496e660', 'd596e660', 'd696e660', 'd796e660', 'd896e660', 'd996e660', 'da96e660', 'db96e660', 'dc96e660', 'dd96e660', 'de96e660', 'df96e660', 'e096e660', 'e196e660', 'e296e660', 'e396e660', 'e496e660', 'e596e660', 'e696e660', 'e796e660', 'e896e660', 'e996e660', 'ea96e660', 'eb96e660', 'ec96e660', 'ed96e660', 'ee96e660', 'ef96e660', 'f096e660', 'f196e660', 'f296e660', 'f396e660', 'f496e660', 'f596e660', 'f696e660', 'f796e660', 'f896e660', 'f996e660', 'fa96e660', 'fb96e660', 'fc96e660', 'fd96e660', 'fe96e660', 'ff96e660', '8097e660', '8197e660', '8297e660', '8397e660', '8497e660', '8597e660', '8697e660', '8797e660', '8897e660', '8997e660', '8a97e660', '8b97e660', '8c97e660', '8d97e660', '8e97e660', '8f97e660', '9097e660', '9197e660', '9297e660', '9397e660', '9497e660', '9597e660', '9697e660', '9797e660', '9897e660', '9997e660', '9a97e660', '9b97e660', '9c97e660', '9d97e660', '9e97e660', '9f97e660', 'a097e660', 'a197e660', 'a297e660', 'a397e660', 'a497e660', 'a597e660', 'a697e660', 'a797e660', 'a897e660', 'a997e660', 'aa97e660', 'ab97e660', 'ac97e660', 'ad97e660', 'ae97e660', 'af97e660', 'b097e660', 'b197e660', 'b297e660', 'b397e660', 'b497e660', 'b597e660', 'b697e660', 'b797e660', 'b897e660', 'b997e660', 'ba97e660', 'bb97e660', 'bc97e660', 'bd97e660', 'be97e660', 'bf97e660', 'c097e660', 'c197e660', 'c297e660', 'c397e660', 'c497e660', 'c597e660', 'c697e660', 'c797e660', 'c897e660', 'c997e660', 'ca97e660', 'cb97e660', 'cc97e660', 'cd97e660', 'ce97e660', 'cf97e660', 'd097e660', 'd197e660', 'd297e660', 'd397e660', 'd497e660', 'd597e660', 'd697e660', 'd797e660', 'd897e660', 'd997e660', 'da97e660', 'db97e660', 'dc97e660', 'dd97e660', 'de97e660', 'df97e660', 'e097e660', 'e197e660', 'e297e660', 'e397e660', 'e497e660', 'e597e660', 'e697e660', 'e797e660', 'e897e660', 'e997e660', 'ea97e660', 'eb97e660', 'ec97e660', 'ed97e660', 'ee97e660', 'ef97e660', 'f097e660', 'f197e660', 'f297e660', 'f397e660', 'f497e660', 'f597e660', 'f697e660', 'f797e660', 'f897e660', 'f997e660', 'fa97e660', 'fb97e660', 'fc97e660', 'fd97e660', 'fe97e660', 'ff97e660', '8098e660', '8198e660', '8298e660', '8398e660', '8498e660', '8598e660', '8698e660', '8798e660', '8898e660', '8998e660', '8a98e660', '8b98e660', '8c98e660', '8d98e660', '8e98e660', '8f98e660', '9098e660', '9198e660', '9298e660', '9398e660', '9498e660', '9598e660', '9698e660', '9798e660', '9898e660', '9998e660', '9a98e660', '9b98e660', '9c98e660', '9d98e660', '9e98e660', '9f98e660', 'a098e660', 'a198e660', 'a298e660', 'a398e660', 'a498e660', 'a598e660', 'a698e660', 'a798e660', 'a898e660', 'a998e660', 'aa98e660', 'ab98e660', 'ac98e660', 'ad98e660', 'ae98e660', 'af98e660', 'b098e660', 'b198e660', 'b298e660', 'b398e660', 'b498e660', 'b598e660', 'b698e660', 'b798e660', 'b898e660', 'b998e660', 'ba98e660', 'bb98e660', 'bc98e660', 'bd98e660', 'be98e660', 'bf98e660', 'c098e660', 'c198e660', 'c298e660', 'c398e660', 'c498e660', 'c598e660', 'c698e660', 'c798e660', 'c898e660', 'c998e660', 'ca98e660', 'cb98e660', 'cc98e660', 'cd98e660', 'ce98e660', 'cf98e660', 'd098e660', 'd198e660', 'd298e660', 'd398e660', 'd498e660', 'd598e660', 'd698e660', 'd798e660', 'd898e660', 'd998e660', 'da98e660', 'db98e660', 'dc98e660', 'dd98e660', 'de98e660', 'df98e660', 'e098e660', 'e198e660', 'e298e660', 'e398e660', 'e498e660', 'e598e660', 'e698e660', 'e798e660', 'e898e660', 'e998e660', 'ea98e660', 'eb98e660', 'ec98e660', 'ed98e660', 'ee98e660', 'ef98e660', 'f098e660', 'f198e660', 'f298e660', 'f398e660', 'f498e660', 'f598e660', 'f698e660', 'f798e660', 'f898e660', 'f998e660', 'fa98e660', 'fb98e660', 'fc98e660', 'fd98e660', 'fe98e660', 'ff98e660', '8099e660', '8199e660', '8299e660', '8399e660', '8499e660', '8599e660', '8699e660', '8799e660', '8899e660', '8999e660', '8a99e660', '8b99e660', '8c99e660', '8d99e660', '8e99e660', '8f99e660', '9099e660', '9199e660', '9299e660', '9399e660', '9499e660', '9599e660', '9699e660', '9799e660', '9899e660', '9999e660', '9a99e660', '9b99e660', '9c99e660', '9d99e660', '9e99e660', '9f99e660', 'a099e660', 'a199e660', 'a299e660', 'a399e660', 'a499e660', 'a599e660', 'a699e660', 'a799e660', 'a899e660', 'a999e660', 'aa99e660', 'ab99e660', 'ac99e660', 'ad99e660', 'ae99e660', 'af99e660', 'b099e660', 'b199e660', 'b299e660', 'b399e660', 'b499e660', 'b599e660', 'b699e660', 'b799e660', 'b899e660', 'b999e660', 'ba99e660', 'bb99e660', 'bc99e660', 'bd99e660', 'be99e660', 'bf99e660', 'c099e660', 'c199e660', 'c299e660', 'c399e660', 'c499e660', 'c599e660', 'c699e660', 'c799e660', 'c899e660', 'c999e660', 'ca99e660', 'cb99e660', 'cc99e660', 'cd99e660', 'ce99e660', 'cf99e660', 'd099e660', 'd199e660', 'd299e660', 'd399e660', 'd499e660', 'd599e660', 'd699e660', 'd799e660', 'd899e660', 'd999e660', 'da99e660', 'db99e660', 'dc99e660', 'dd99e660', 'de99e660', 'df99e660', 'e099e660', 'e199e660', 'e299e660', 'e399e660', 'e499e660', 'e599e660', 'e699e660', 'e799e660', 'e899e660', 'e999e660', 'ea99e660', 'eb99e660', 'ec99e660', 'ed99e660', 'ee99e660', 'ef99e660', 'f099e660', 'f199e660', 'f299e660', 'f399e660', 'f499e660', 'f599e660', 'f699e660', 'f799e660', 'f899e660', 'f999e660', 'fa99e660', 'fb99e660', 'fc99e660', 'fd99e660', 'fe99e660', 'ff99e660', '809ae660', '819ae660', '829ae660', '839ae660', '849ae660', '859ae660', '869ae660', '879ae660', '889ae660', '899ae660', '8a9ae660', '8b9ae660', '8c9ae660', '8d9ae660', '8e9ae660', '8f9ae660', '909ae660', '919ae660', '929ae660', '939ae660', '949ae660', '959ae660', '969ae660', '979ae660', '989ae660', '999ae660', '9a9ae660', '9b9ae660', '9c9ae660', '9d9ae660', '9e9ae660', '9f9ae660', 'a09ae660', 'a19ae660', 'a29ae660', 'a39ae660', 'a49ae660', 'a59ae660', 'a69ae660', 'a79ae660', 'a89ae660', 'a99ae660', 'aa9ae660', 'ab9ae660', 'ac9ae660', 'ad9ae660', 'ae9ae660', 'af9ae660', 'b09ae660', 'b19ae660', 'b29ae660', 'b39ae660', 'b49ae660', 'b59ae660', 'b69ae660', 'b79ae660', 'b89ae660', 'b99ae660', 'ba9ae660', 'bb9ae660', 'bc9ae660', 'bd9ae660', 'be9ae660', 'bf9ae660', 'c09ae660', 'c19ae660', 'c29ae660', 'c39ae660', 'c49ae660', 'c59ae660', 'c69ae660', 'c79ae660', 'c89ae660', 'c99ae660', 'ca9ae660', 'cb9ae660', 'cc9ae660', 'cd9ae660', 'ce9ae660', 'cf9ae660', 'd09ae660', 'd19ae660', 'd29ae660', 'd39ae660', 'd49ae660', 'd59ae660', 'd69ae660', 'd79ae660', 'd89ae660', 'd99ae660', 'da9ae660', 'db9ae660', 'dc9ae660', 'dd9ae660', 'de9ae660', 'df9ae660', 'e09ae660', 'e19ae660', 'e29ae660', 'e39ae660', 'e49ae660', 'e59ae660', 'e69ae660', 'e79ae660', 'e89ae660', 'e99ae660', 'ea9ae660', 'eb9ae660', 'ec9ae660', 'ed9ae660', 'ee9ae660', 'ef9ae660', 'f09ae660', 'f19ae660', 'f29ae660', 'f39ae660', 'f49ae660', 'f59ae660', 'f69ae660', 'f79ae660', 'f89ae660', 'f99ae660', 'fa9ae660', 'fb9ae660', 'fc9ae660', 'fd9ae660', 'fe9ae660', 'ff9ae660', '809be660', '819be660', '829be660', '839be660', '849be660', '859be660', '869be660', '879be660', '889be660', '899be660', '8a9be660', '8b9be660', '8c9be660', '8d9be660', '8e9be660', '8f9be660', '909be660', '919be660', '929be660', '939be660', '949be660', '959be660', '969be660', '979be660', '989be660', '999be660', '9a9be660', '9b9be660', '9c9be660', '9d9be660', '9e9be660', '9f9be660', 'a09be660', 'a19be660', 'a29be660', 'a39be660', 'a49be660', 'a59be660', 'a69be660', 'a79be660', 'a89be660', 'a99be660', 'aa9be660', 'ab9be660', 'ac9be660', 'ad9be660', 'ae9be660', 'af9be660', 'b09be660', 'b19be660', 'b29be660', 'b39be660', 'b49be660', 'b59be660', 'b69be660', 'b79be660', 'b89be660', 'b99be660', 'ba9be660', 'bb9be660', 'bc9be660', 'bd9be660', 'be9be660', 'bf9be660', 'c09be660', 'c19be660', 'c29be660', 'c39be660', 'c49be660', 'c59be660', 'c69be660', 'c79be660', 'c89be660', 'c99be660', 'ca9be660', 'cb9be660', 'cc9be660', 'cd9be660', 'ce9be660', 'cf9be660', 'd09be660', 'd19be660', 'd29be660', 'd39be660']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy1: {e}")

                if b"@proxy2" in data and not self.RbGx:
                    try:
                        items_ids = [
    "c19ae061", "c29ae061", "c39ae061", "c49ae061", "c59ae061", "c69ae061", "c79ae061", "c89ae061", "c99ae061", "ca9ae061", "cb9ae061", "cc9ae061", "cd9ae061", "ce9ae061", "cf9ae061",
    "d09ae061", "d19ae061", "d29ae061", "d39ae061", "d49ae061", "d59ae061", "d69ae061", "d79ae061", "d89ae061", "d99ae061", "da9ae061", "db9ae061", "dc9ae061", "dd9ae061", "de9ae061", "df9ae061",
    "e09ae061", "e19ae061", "e29ae061", "e39ae061", "e49ae061", "e59ae061", "e69ae061", "e79ae061", "e89ae061", "e99ae061", "ea9ae061", "eb9ae061", "ec9ae061", "ed9ae061", "ee9ae061", "ef9ae061",
    "f09ae061", "f19ae061", "f29ae061", "f39ae061", "f49ae061", "f59ae061", "f69ae061", "f79ae061", "f89ae061", "f99ae061", "fa9ae061", "fb9ae061", "fc9ae061", "fd9ae061", "fe9ae061", "ff9ae061",
    "809be061", "819be061", "829be061", "839be061", "849be061", "859be061", "869be061", "879be061", "889be061", "899be061", "8a9be061", "8b9be061", "8c9be061", "8d9be061", "8e9be061", "8f9be061",
    "909be061", "919be061", "929be061", "939be061", "949be061", "959be061", "969be061", "979be061", "989be061", "999be061", "9a9be061", "9b9be061", "9c9be061", "9d9be061", "9e9be061", "9f9be061",
    "a09be061", "a19be061", "a29be061", "a39be061", "a49be061", "a59be061", "a69be061", "a79be061", "a89be061", "a99be061", "aa9be061", "ab9be061", "ac9be061", "ad9be061", "ae9be061", "af9be061",
    "b09be061", "b19be061", "b29be061", "b39be061", "b49be061", "b59be061", "b69be061", "b79be061", "b89be061", "b99be061", "ba9be061", "bb9be061", "bc9be061", "bd9be061", "be9be061", "bf9be061",
    "c09be061", "c19be061", "c29be061", "c39be061", "c49be061", "c59be061", "c69be061", "c79be061", "c89be061", "c99be061", "ca9be061", "cb9be061", "cc9be061", "cd9be061", "ce9be061", "cf9be061",
    "d09be061", "d19be061", "d29be061", "d39be061", "d49be061", "d59be061", "d69be061", "d79be061", "d89be061", "d99be061", "da9be061", "db9be061", "dc9be061", "dd9be061", "de9be061", "df9be061",
    "e09be061", "e19be061", "e29be061", "e39be061", "e49be061", "e59be061", "e69be061", "e79be061", "e89be061", "e99be061", "ea9be061", "eb9be061", "ec9be061", "ed9be061", "ee9be061", "ef9be061",
    "f09be061", "f19be061", "f29be061", "f39be061", "f49be061", "f59be061", "f69be061", "f79be061", "f89be061", "f99be061", "fa9be061", "fb9be061", "fc9be061", "fd9be061", "fe9be061", "ff9be061",
    "809ce061", "819ce061", "829ce061", "839ce061", "849ce061", "859ce061", "869ce061", "879ce061", "889ce061", "899ce061", "8a9ce061", "8b9ce061", "8c9ce061", "8d9ce061", "8e9ce061", "8f9ce061",
    "909ce061", "919ce061", "929ce061", "939ce061", "949ce061", "959ce061", "969ce061", "979ce061", "989ce061", "999ce061", "9a9ce061", "9b9ce061", "9c9ce061", "9d9ce061", "9e9ce061", "9f9ce061",
    "a09ce061", "a19ce061", "a29ce061", "a39ce061", "a49ce061", "a59ce061", "a69ce061", "a79ce061", "a89ce061", "a99ce061", "aa9ce061", "ab9ce061", "ac9ce061", "ad9ce061", "ae9ce061", "af9ce061",
    "b09ce061", "b19ce061", "b29ce061", "b39ce061", "b49ce061", "b59ce061", "b69ce061", "b79ce061", "b89ce061", "b99ce061", "ba9ce061", "bb9ce061", "bc9ce061", "bd9ce061", "be9ce061", "bf9ce061",
    "c09ce061", "c19ce061", "c29ce061", "c39ce061", "c49ce061", "c59ce061", "c69ce061", "c79ce061", "c89ce061", "c99ce061", "ca9ce061", "cb9ce061", "cc9ce061", "cd9ce061", "ce9ce061", "cf9ce061",
    "d09ce061", "d19ce061", "d29ce061", "d39ce061", "d49ce061", "d59ce061", "d69ce061", "d79ce061", "d89ce061", "d99ce061", "da9ce061", "db9ce061", "dc9ce061", "dd9ce061", "de9ce061", "df9ce061",
    "e09ce061", "e19ce061", "e29ce061", "e39ce061", "e49ce061", "e59ce061", "e69ce061", "e79ce061", "e89ce061", "e99ce061", "ea9ce061", "eb9ce061", "ec9ce061", "ed9ce061", "ee9ce061", "ef9ce061",
    "f09ce061", "f19ce061", "f29ce061", "f39ce061", "f49ce061", "f59ce061", "f69ce061", "f79ce061", "f89ce061", "f99ce061", "fa9ce061", "fb9ce061", "fc9ce061", "fd9ce061", "fe9ce061", "ff9ce061",
    "809de061", "819de061", "829de061", "839de061", "849de061", "859de061", "869de061", "879de061", "889de061", "899de061", "8a9de061", "8b9de061", "8c9de061", "8d9de061", "8e9de061", "8f9de061",
    "909de061", "919de061", "929de061", "939de061", "949de061", "959de061", "969de061", "979de061", "989de061", "999de061", "9a9de061", "9b9de061", "9c9de061", "9d9de061", "9e9de061", "9f9de061",
    "a09de061", "a19de061", "a29de061", "a39de061", "a49de061", "a59de061", "a69de061", "a79de061", "a89de061", "a99de061", "aa9de061", "ab9de061", "ac9de061", "ad9de061", "ae9de061", "af9de061",
    "b09de061", "b19de061", "b29de061", "b39de061", "b49de061", "b59de061", "b69de061", "b79de061", "b89de061", "b99de061", "ba9de061", "bb9de061", "bc9de061", "bd9de061", "be9de061", "bf9de061",
    "c09de061", "c19de061", "c29de061", "c39de061", "c49de061", "c59de061", "c69de061", "c79de061", "c89de061", "c99de061", "ca9de061", "cb9de061", "cc9de061", "cd9de061", "ce9de061", "cf9de061",
    "d09de061", "d19de061", "d29de061", "d39de061", "d49de061", "d59de061", "d69de061", "d79de061", "d89de061", "d99de061", "da9de061", "db9de061", "dc9de061", "dd9de061", "de9de061", "df9de061",
    "e09de061", "e19de061", "e29de061", "e39de061", "e49de061", "e59de061", "e69de061", "e79de061", "e89de061", "e99de061", "ea9de061", "eb9de061", "ec9de061", "ed9de061", "ee9de061", "ef9de061",
    "f09de061", "f19de061", "f29de061", "f39de061", "f49de061", "f59de061", "f69de061", "f79de061", "f89de061", "f99de061", "fa9de061", "fb9de061", "fc9de061", "fd9de061", "fe9de061", "ff9de061",
    "809ee061", "819ee061", "829ee061", "839ee061", "849ee061", "859ee061", "869ee061", "879ee061", "889ee061", "899ee061", "8a9ee061", "8b9ee061", "8c9ee061", "8d9ee061", "8e9ee061", "8f9ee061",
    "909ee061", "919ee061", "929ee061", "939ee061", "949ee061", "959ee061", "969ee061", "979ee061", "989ee061", "999ee061", "9a9ee061", "9b9ee061", "9c9ee061", "9d9ee061", "9e9ee061", "9f9ee061",
    "a09ee061", "a19ee061", "a29ee061", "a39ee061", "a49ee061", "a59ee061", "a69ee061", "a79ee061", "a89ee061", "a99ee061", "aa9ee061", "ab9ee061", "ac9ee061", "ad9ee061", "ae9ee061", "af9ee061",
    "b09ee061", "b19ee061", "b29ee061", "b39ee061", "b49ee061", "b59ee061", "b69ee061", "b79ee061", "b89ee061", "b99ee061", "ba9ee061", "bb9ee061", "bc9ee061", "bd9ee061", "be9ee061", "bf9ee061",
    "c09ee061", "c19ee061", "c29ee061", "c39ee061", "c49ee061", "c59ee061", "c69ee061", "c79ee061", "c89ee061", "c99ee061", "ca9ee061", "cb9ee061", "cc9ee061", "cd9ee061", "ce9ee061", "cf9ee061",
    "d09ee061", "d19ee061", "d29ee061", "d39ee061", "d49ee061", "d59ee061", "d69ee061", "d79ee061", "d89ee061", "d99ee061", "da9ee061", "db9ee061", "dc9ee061", "dd9ee061", "de9ee061", "df9ee061",
    "e09ee061", "e19ee061", "e29ee061", "e39ee061", "e49ee061", "e59ee061", "e69ee061", "e79ee061", "e89ee061", "e99ee061", "ea9ee061", "eb9ee061", "ec9ee061", "ed9ee061", "ee9ee061", "ef9ee061",
    "f09ee061", "f19ee061", "f29ee061", "f39ee061", "f49ee061", "f59ee061", "f69ee061", "f79ee061", "f89ee061", "f99ee061", "fa9ee061", "fb9ee061", "fc9ee061", "fd9ee061", "fe9ee061", "ff9ee061",
    "809fe061", "819fe061", "829fe061", "839fe061", "849fe061", "859fe061", "869fe061", "879fe061", "889fe061", "899fe061", "8a9fe061", "8b9fe061", "8c9fe061", "8d9fe061", "8e9fe061", "8f9fe061",
    "909fe061", "919fe061", "929fe061", "939fe061", "949fe061", "959fe061", "969fe061", "979fe061", "989fe061", "999fe061", "9a9fe061", "9b9fe061", "9c9fe061", "9d9fe061", "9e9fe061", "9f9fe061",
    "a09fe061", "a1a0e061", "a2a0e061", "a3a0e061", "a4a0e061", "a5a0e061", "a6a0e061", "a7a0e061", "a8a0e061", "a9a0e061", "aaa0e061", "aba0e061", "aca0e061", "ada0e061", "aea0e061", "afa0e061",
    "b0a0e061", "b1a0e061", "b2a0e061", "b3a0e061", "b4a0e061", "b5a0e061", "b6a0e061", "b7a0e061", "b8a0e061", "b9a0e061", "baa0e061", "bba0e061", "bca0e061", "bda0e061", "bea0e061", "bfa0e061",
    "c0a0e061", "c1a0e061", "c2a0e061", "c3a0e061", "c4a0e061", "c5a0e061", "c6a0e061", "c7a0e061", "c8a0e061", "c9a0e061", "caa0e061", "cba0e061", "cca0e061", "cda0e061", "cea0e061", "cfa0e061",
    "d0a0e061", "d1a0e061", "d2a0e061", "d3a0e061", "d4a0e061", "d5a0e061", "d6a0e061", "d7a0e061", "d8a0e061", "d9a0e061", "daa0e061", "dba0e061", "dca0e061", "dda0e061", "dea0e061", "dfa0e061",
    "e0a0e061", "e1a0e061", "e2a0e061", "e3a0e061", "e4a0e061", "e5a0e061", "e6a0e061", "e7a0e061", "e8a0e061", "e9a0e061", "eaa0e061", "eba0e061", "eca0e061", "eda0e061", "eea0e061", "efa0e061",
    "f0a0e061", "f1a0e061", "f2a0e061", "f3a0e061", "f4a0e061", "f5a0e061", "f6a0e061", "f7a0e061", "f8a0e061", "f9a0e061", "faa0e061", "fba0e061", "fca0e061", "fda0e061", "fea0e061", "ffa0e061",
    "80a1e061", "81a1e061", "82a1e061", "83a1e061", "84a1e061", "85a1e061", "86a1e061", "87a1e061", "88a1e061", "89a1e061", "8aa1e061", "8ba1e061", "8ca1e061", "8da1e061", "8ea1e061", "8fa1e061",
    "90a1e061", "91a1e061", "92a1e061", "93a1e061", "94a1e061", "95a1e061", "96a1e061", "97a1e061", "98a1e061", "99a1e061", "9aa1e061", "9ba1e061", "9ca1e061", "9da1e061", "9ea1e061", "9fa1e061",
    "a0a1e061", "a1a1e061", "a2a1e061", "a3a1e061", "a4a1e061", "a5a1e061", "a6a1e061", "a7a1e061", "a8a1e061", "a9a1e061", "aaa1e061", "aba1e061", "aca1e061", "ada1e061", "aea1e061", "afa1e061",
    "b0a1e061", "b1a1e061", "b2a1e061", "b3a1e061", "b4a1e061", "b5a1e061", "b6a1e061", "b7a1e061", "b8a1e061", "b9a1e061", "baa1e061", "bba1e061", "bca1e061", "bda1e061", "bea1e061", "bfa1e061",
    "c0a1e061", "c1a1e061", "c2a1e061", "c3a1e061", "c4a1e061", "c5a1e061", "c6a1e061", "c7a1e061", "c8a1e061", "c9a1e061", "caa1e061", "cba1e061", "cca1e061", "cda1e061", "cea1e061", "cfa1e061",
    "d0a1e061", "d1a1e061", "d2a1e061", "d3a1e061", "d4a1e061", "d5a1e061", "d6a1e061", "d7a1e061", "d8a1e061", "d9a1e061", "daa1e061", "dba1e061", "dca1e061", "dda1e061", "dea1e061", "dfa1e061",
    "e0a1e061", "e1a1e061", "e2a1e061", "e3a1e061", "e4a1e061", "e5a1e061", "e6a1e061", "e7a1e061", "e8a1e061", "e9a1e061", "eaa1e061", "eba1e061", "eca1e061", "eda1e061", "eea1e061", "efa1e061",
    "f0a1e061", "f1a1e061", "f2a1e061", "f3a1e061", "f4a1e061", "f5a1e061", "f6a1e061", "f7a1e061", "f8a1e061", "f9a1e061", "faa1e061", "fba1e061", "fca1e061", "fda1e061", "fea1e061", "ffa1e061"
]  # أضف الباقي حسب المتوفر
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy2: {e}")


                if b"@proxy3" in data and not self.RbGx:
                    try:
                        items_ids = ['d49be660', 'd59be660', 'd69be660', 'd79be660', 'd89be660', 'd99be660', 'da9be660', 'db9be660', 'dc9be660', 'dd9be660', 'de9be660', 'df9be660', 'e09be660', 'e19be660', 'e29be660', 'e39be660', 'e49be660', 'e59be660', 'e69be660', 'e79be660', 'e89be660', 'e99be660', 'ea9be660', 'eb9be660', 'ec9be660', 'ed9be660', 'ee9be660', 'ef9be660', 'f09be660', 'f19be660', 'f29be660', 'f39be660', 'f49be660', 'f59be660', 'f69be660', 'f79be660', 'f89be660', 'f99be660', 'fa9be660', 'fb9be660', 'fc9be660', 'fd9be660', 'fe9be660', 'ff9be660', '809ce660', '819ce660', '829ce660', '839ce660', '849ce660', '859ce660', '869ce660', '879ce660', '889ce660', '899ce660', '8a9ce660', '8b9ce660', '8c9ce660', '8d9ce660', '8e9ce660', '8f9ce660', 'c191e660', 'c291e660', 'c391e660', 'c491e660', 'c591e660', 'c691e660', 'c791e660', 'c891e660', 'c991e660', 'ca91e660', 'cb91e660', 'cc91e660', 'cd91e660', 'ce91e660', 'cf91e660', 'd091e660', 'd191e660', 'd291e660', 'd391e660', 'd491e660', 'd591e660', 'd691e660', 'd791e660', 'd891e660', 'd991e660', 'da91e660', 'db91e660', 'dc91e660', 'dd91e660', 'de91e660', 'df91e660', 'e091e660', 'e191e660', 'e291e660', 'e391e660', 'e491e660', 'e591e660', 'e691e660', 'e791e660', 'e891e660', 'e991e660', 'ea91e660', 'eb91e660', 'ec91e660', 'ed91e660', 'ee91e660', 'ef91e660', 'f091e660', 'f191e660', 'f291e660', 'f391e660', 'f491e660', 'f591e660', 'f691e660', 'f791e660', 'f891e660', 'f991e660', 'fa91e660', 'fb91e660', 'fc91e660', 'fd91e660', 'fe91e660', 'ff91e660', '8092e660', '8192e660', '8292e660', '8392e660', '8492e660', '8592e660', '8692e660', '8792e660', '8892e660', '8992e660', '8a92e660', '8b92e660', '8c92e660', '8d92e660', '8e92e660', '8f92e660', '9092e660', '9192e660', '9292e660', '9392e660', '9492e660', '9592e660', '9692e660', '9792e660', '9892e660', '9992e660', '9a92e660', '9b92e660', '9c92e660', '9d92e660', '9e92e660', '9f92e660', 'a092e660', 'a192e660', 'a292e660', 'a392e660', 'a492e660', 'a592e660', 'a692e660', 'a792e660', 'a892e660', 'a992e660', 'aa92e660', 'ab92e660', 'ac92e660', 'ad92e660', 'ae92e660', 'af92e660', 'b092e660', 'b192e660', 'b292e660', 'b392e660', 'b492e660', 'b592e660', 'b692e660', 'b792e660', 'b892e660', 'b992e660', 'ba92e660', 'bb92e660', 'bc92e660', 'bd92e660', 'be92e660', 'bf92e660', 'c092e660', 'c192e660', 'c292e660', 'c392e660', 'c492e660', 'c592e660', 'c692e660', 'c792e660', 'c892e660', 'c992e660', 'ca92e660', 'cb92e660', 'cc92e660', 'cd92e660', 'ce92e660', 'cf92e660', 'd092e660', 'd192e660', 'd292e660', 'd392e660', 'd492e660', 'd592e660', 'd692e660', 'd792e660', 'd892e660', 'd992e660', 'da92e660', 'db92e660', 'dc92e660', 'dd92e660', 'de92e660', 'df92e660', 'e092e660', 'e192e660', 'e292e660', 'e392e660', 'e492e660', 'e592e660', 'e692e660', 'e792e660', 'e892e660', 'e992e660', 'ea92e660', 'eb92e660', 'ec92e660', 'ed92e660', 'ee92e660', 'ef92e660', 'f092e660', 'f192e660', 'f292e660', 'f392e660', 'f492e660', 'f592e660', 'f692e660', 'f792e660', 'f892e660', 'f992e660', 'fa92e660', 'fb92e660', 'fc92e660', 'fd92e660', 'fe92e660', 'ff92e660', '8093e660', '8193e660', '8293e660', '8393e660', '8493e660', '8593e660', '8693e660', '8793e660', '8893e660', '8993e660', '8a93e660', '8b93e660', '8c93e660', '8d93e660', '8e93e660', '8f93e660', '9093e660', '9193e660', '9293e660', '9393e660', '9493e660', '9593e660', '9693e660', '9793e660', '9893e660', '9993e660', '9a93e660', '9b93e660', '9c93e660', '9d93e660', '9e93e660', '9f93e660', 'a093e660', 'a193e660', 'a293e660', 'a393e660', 'a493e660', 'a593e660', 'a693e660', 'a793e660', 'a893e660', 'a993e660', 'aa93e660', 'ab93e660', 'ac93e660', 'ad93e660', 'ae93e660', 'af93e660', 'b093e660', 'b193e660', 'b293e660', 'b393e660', 'b493e660', 'b593e660', 'b693e660', 'b793e660', 'b893e660', 'b993e660', 'ba93e660', 'bb93e660', 'bc93e660', 'bd93e660', 'be93e660', 'bf93e660', 'c093e660', 'c193e660', 'c293e660', 'c393e660', 'c493e660', 'c593e660', 'c693e660', 'c793e660', 'c893e660', 'c993e660', 'ca93e660', 'cb93e660', 'cc93e660', 'cd93e660', 'ce93e660', 'cf93e660', 'd093e660', 'd193e660', 'd293e660', 'd393e660', 'd493e660', 'd593e660', 'd693e660', 'd793e660', 'd893e660', 'd993e660', 'da93e660', 'db93e660', 'dc93e660', 'dd93e660', 'de93e660', 'df93e660', 'e093e660', 'e193e660', 'e293e660', 'e393e660', 'e493e660', 'e593e660', 'e693e660', 'e793e660', 'e893e660', 'e993e660', 'ea93e660', 'eb93e660', 'ec93e660', 'ed93e660', 'ee93e660', 'ef93e660', 'f093e660', 'f193e660', 'f293e660', 'f393e660', 'f493e660', 'f593e660', 'f693e660', 'f793e660', 'f893e660', 'f993e660', 'fa93e660', 'fb93e660', 'fc93e660', 'fd93e660', 'fe93e660', 'ff93e660', '8094e660', '8194e660', '8294e660', '8394e660', '8494e660', '8594e660', '8694e660', '8794e660', '8894e660', '8994e660', '8a94e660', '8b94e660', '8c94e660', '8d94e660', '8e94e660', '8f94e660', '9094e660', '9194e660', '9294e660', '9394e660', '9494e660', '9594e660', '9694e660', '9794e660', '9894e660', '9994e660', '9a94e660', '9b94e660', '9c94e660', '9d94e660', '9e94e660', '9f94e660', 'a094e660', 'a194e660', 'a294e660', 'a394e660', 'a494e660', 'a594e660', 'a694e660', 'a794e660', 'a894e660', 'a994e660', 'aa94e660', 'ab94e660', 'ac94e660', 'ad94e660', 'ae94e660', 'af94e660', 'b094e660', 'b194e660', 'b294e660', 'b394e660', 'b494e660', 'b594e660', 'b694e660', 'b794e660', 'b894e660', 'b994e660', 'ba94e660', 'bb94e660', 'bc94e660', 'bd94e660', 'be94e660', 'bf94e660', 'c094e660', 'c194e660', 'c294e660', 'c394e660', 'c494e660', 'c594e660', 'c694e660', 'c794e660', 'c894e660', 'c994e660', 'ca94e660', 'cb94e660', 'cc94e660', 'cd94e660', 'ce94e660', 'cf94e660', 'd094e660', 'd194e660', 'd294e660', 'd394e660', 'd494e660', 'd594e660', 'd694e660', 'd794e660', 'd894e660', 'd994e660', 'da94e660', 'db94e660', 'dc94e660', 'dd94e660', 'de94e660', 'df94e660', 'e094e660', 'e194e660', 'e294e660', 'e394e660', 'e494e660', 'e594e660', 'e694e660', 'e794e660', 'e894e660', 'e994e660', 'ea94e660', 'eb94e660', 'ec94e660', 'ed94e660', 'ee94e660', 'ef94e660', 'f094e660', 'f194e660', 'f294e660', 'f394e660', 'f494e660', 'f594e660', 'f694e660', 'f794e660', 'f894e660', 'f994e660', 'fa94e660', 'fb94e660', 'fc94e660', 'fd94e660', 'fe94e660', 'ff94e660', '8095e660', '8195e660', '8295e660', '8395e660', '8495e660', '8595e660', '8695e660', '8795e660', '8895e660', '8995e660', '8a95e660', '8b95e660', '8c95e660', '8d95e660', '8e95e660', '8f95e660', '9095e660', '9195e660', '9295e660', '9395e660', '9495e660', '9595e660', '9695e660', '9795e660', '9895e660', '9995e660', '9a95e660', '9b95e660', '9c95e660', '9d95e660', '9e95e660', '9f95e660', 'a095e660', 'a195e660', 'a295e660', 'a395e660', 'a495e660', 'a595e660', 'a695e660', 'a795e660', 'a895e660', 'a995e660', 'aa95e660', 'ab95e660', 'ac95e660', 'ad95e660', 'ae95e660', 'af95e660', 'b095e660', 'b195e660', 'b295e660', 'b395e660', 'b495e660', 'b595e660', 'b695e660', 'b795e660', 'b895e660', 'b995e660', 'ba95e660', 'bb95e660', 'bc95e660', 'bd95e660', 'be95e660', 'bf95e660', 'c095e660', 'c195e660', 'c295e660', 'c395e660', 'c495e660', 'c595e660', 'c695e660', 'c795e660', 'c895e660', 'c995e660', 'ca95e660', 'cb95e660', 'cc95e660', 'cd95e660', 'ce95e660', 'cf95e660', 'd095e660', 'd195e660', 'd295e660', 'd395e660', 'd495e660', 'd595e660', 'd695e660', 'd795e660', 'd895e660', 'd995e660', 'da95e660', 'db95e660', 'dc95e660', 'dd95e660', 'de95e660', 'df95e660', 'e095e660', 'e195e660', 'e295e660', 'e395e660', 'e495e660', 'e595e660', 'e695e660', 'e795e660', 'e895e660', 'e995e660', 'ea95e660', 'eb95e660', 'ec95e660', 'ed95e660', 'ee95e660', 'ef95e660', 'f095e660', 'f195e660', 'f295e660', 'f395e660', 'f495e660', 'f595e660', 'f695e660', 'f795e660', 'f895e660', 'f995e660', 'fa95e660', 'fb95e660', 'fc95e660', 'fd95e660', 'fe95e660', 'ff95e660', '8096e660', '8196e660', '8296e660', '8396e660', '8496e660', '8596e660', '8696e660', '8796e660', '8896e660', '8996e660', '8a96e660', '8b96e660', '8c96e660', '8d96e660', '8e96e660', '8f96e660', '9096e660', '9196e660', '9296e660', '9396e660', '9496e660', '9596e660', '9696e660', '9796e660', '9896e660', '9996e660', '9a96e660', '9b96e660', '9c96e660', '9d96e660', '9e96e660', '9f96e660', 'a096e660', 'a196e660', 'a296e660', 'a396e660', 'a496e660', 'a596e660', 'a696e660']  # أضف الباقي
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy3: {e}")

                if b"@proxy3" in data and not self.RbGx:
                    try:
                        items_ids = ['d49be660', 'd59be660', 'd69be660', 'd79be660', 'd89be660', 'd99be660', 'da9be660', 'db9be660', 'dc9be660', 'dd9be660', 'de9be660', 'df9be660', 'e09be660', 'e19be660', 'e29be660', 'e39be660', 'e49be660', 'e59be660', 'e69be660', 'e79be660', 'e89be660', 'e99be660', 'ea9be660', 'eb9be660', 'ec9be660', 'ed9be660', 'ee9be660', 'ef9be660', 'f09be660', 'f19be660', 'f29be660', 'f39be660', 'f49be660', 'f59be660', 'f69be660', 'f79be660', 'f89be660', 'f99be660', 'fa9be660', 'fb9be660', 'fc9be660', 'fd9be660', 'fe9be660', 'ff9be660', '809ce660', '819ce660', '829ce660', '839ce660', '849ce660', '859ce660', '869ce660', '879ce660', '889ce660', '899ce660', '8a9ce660', '8b9ce660', '8c9ce660', '8d9ce660', '8e9ce660', '8f9ce660', 'c191e660', 'c291e660', 'c391e660', 'c491e660', 'c591e660', 'c691e660', 'c791e660', 'c891e660', 'c991e660', 'ca91e660', 'cb91e660', 'cc91e660', 'cd91e660', 'ce91e660', 'cf91e660', 'd091e660', 'd191e660', 'd291e660', 'd391e660', 'd491e660', 'd591e660', 'd691e660', 'd791e660', 'd891e660', 'd991e660', 'da91e660', 'db91e660', 'dc91e660', 'dd91e660', 'de91e660', 'df91e660', 'e091e660', 'e191e660', 'e291e660', 'e391e660', 'e491e660', 'e591e660', 'e691e660', 'e791e660', 'e891e660', 'e991e660', 'ea91e660', 'eb91e660', 'ec91e660', 'ed91e660', 'ee91e660', 'ef91e660', 'f091e660', 'f191e660', 'f291e660', 'f391e660', 'f491e660', 'f591e660', 'f691e660', 'f791e660', 'f891e660', 'f991e660', 'fa91e660', 'fb91e660', 'fc91e660', 'fd91e660', 'fe91e660', 'ff91e660', '8092e660', '8192e660', '8292e660', '8392e660', '8492e660', '8592e660', '8692e660', '8792e660', '8892e660', '8992e660', '8a92e660', '8b92e660', '8c92e660', '8d92e660', '8e92e660', '8f92e660', '9092e660', '9192e660', '9292e660', '9392e660', '9492e660', '9592e660', '9692e660', '9792e660', '9892e660', '9992e660', '9a92e660', '9b92e660', '9c92e660', '9d92e660', '9e92e660', '9f92e660', 'a092e660', 'a192e660', 'a292e660', 'a392e660', 'a492e660', 'a592e660', 'a692e660', 'a792e660', 'a892e660', 'a992e660', 'aa92e660', 'ab92e660', 'ac92e660', 'ad92e660', 'ae92e660', 'af92e660', 'b092e660', 'b192e660', 'b292e660', 'b392e660', 'b492e660', 'b592e660', 'b692e660', 'b792e660', 'b892e660', 'b992e660', 'ba92e660', 'bb92e660', 'bc92e660', 'bd92e660', 'be92e660', 'bf92e660', 'c092e660', 'c192e660', 'c292e660', 'c392e660', 'c492e660', 'c592e660', 'c692e660', 'c792e660', 'c892e660', 'c992e660', 'ca92e660', 'cb92e660', 'cc92e660', 'cd92e660', 'ce92e660', 'cf92e660', 'd092e660', 'd192e660', 'd292e660', 'd392e660', 'd492e660', 'd592e660', 'd692e660', 'd792e660', 'd892e660', 'd992e660', 'da92e660', 'db92e660', 'dc92e660', 'dd92e660', 'de92e660', 'df92e660', 'e092e660', 'e192e660', 'e292e660', 'e392e660', 'e492e660', 'e592e660', 'e692e660', 'e792e660', 'e892e660', 'e992e660', 'ea92e660', 'eb92e660', 'ec92e660', 'ed92e660', 'ee92e660', 'ef92e660', 'f092e660', 'f192e660', 'f292e660', 'f392e660', 'f492e660', 'f592e660', 'f692e660', 'f792e660', 'f892e660', 'f992e660', 'fa92e660', 'fb92e660', 'fc92e660', 'fd92e660', 'fe92e660', 'ff92e660', '8093e660', '8193e660', '8293e660', '8393e660', '8493e660', '8593e660', '8693e660', '8793e660', '8893e660', '8993e660', '8a93e660', '8b93e660', '8c93e660', '8d93e660', '8e93e660', '8f93e660', '9093e660', '9193e660', '9293e660', '9393e660', '9493e660', '9593e660', '9693e660', '9793e660', '9893e660', '9993e660', '9a93e660', '9b93e660', '9c93e660', '9d93e660', '9e93e660', '9f93e660', 'a093e660', 'a193e660', 'a293e660', 'a393e660', 'a493e660', 'a593e660', 'a693e660', 'a793e660', 'a893e660', 'a993e660', 'aa93e660', 'ab93e660', 'ac93e660', 'ad93e660', 'ae93e660', 'af93e660', 'b093e660', 'b193e660', 'b293e660', 'b393e660', 'b493e660', 'b593e660', 'b693e660', 'b793e660', 'b893e660', 'b993e660', 'ba93e660', 'bb93e660', 'bc93e660', 'bd93e660', 'be93e660', 'bf93e660', 'c093e660', 'c193e660', 'c293e660', 'c393e660', 'c493e660', 'c593e660', 'c693e660', 'c793e660', 'c893e660', 'c993e660', 'ca93e660', 'cb93e660', 'cc93e660', 'cd93e660', 'ce93e660', 'cf93e660', 'd093e660', 'd193e660', 'd293e660', 'd393e660', 'd493e660', 'd593e660', 'd693e660', 'd793e660', 'd893e660', 'd993e660', 'da93e660', 'db93e660', 'dc93e660', 'dd93e660', 'de93e660', 'df93e660', 'e093e660', 'e193e660', 'e293e660', 'e393e660', 'e493e660', 'e593e660', 'e693e660', 'e793e660', 'e893e660', 'e993e660', 'ea93e660', 'eb93e660', 'ec93e660', 'ed93e660', 'ee93e660', 'ef93e660', 'f093e660', 'f193e660', 'f293e660', 'f393e660', 'f493e660', 'f593e660', 'f693e660', 'f793e660', 'f893e660', 'f993e660', 'fa93e660', 'fb93e660', 'fc93e660', 'fd93e660', 'fe93e660', 'ff93e660', '8094e660', '8194e660', '8294e660', '8394e660', '8494e660', '8594e660', '8694e660', '8794e660', '8894e660', '8994e660', '8a94e660', '8b94e660', '8c94e660', '8d94e660', '8e94e660', '8f94e660', '9094e660', '9194e660', '9294e660', '9394e660', '9494e660', '9594e660', '9694e660', '9794e660', '9894e660', '9994e660', '9a94e660', '9b94e660', '9c94e660', '9d94e660', '9e94e660', '9f94e660', 'a094e660', 'a194e660', 'a294e660', 'a394e660', 'a494e660', 'a594e660', 'a694e660', 'a794e660', 'a894e660', 'a994e660', 'aa94e660', 'ab94e660', 'ac94e660', 'ad94e660', 'ae94e660', 'af94e660', 'b094e660', 'b194e660', 'b294e660', 'b394e660', 'b494e660', 'b594e660', 'b694e660', 'b794e660', 'b894e660', 'b994e660', 'ba94e660', 'bb94e660', 'bc94e660', 'bd94e660', 'be94e660', 'bf94e660', 'c094e660', 'c194e660', 'c294e660', 'c394e660', 'c494e660', 'c594e660', 'c694e660', 'c794e660', 'c894e660', 'c994e660', 'ca94e660', 'cb94e660', 'cc94e660', 'cd94e660', 'ce94e660', 'cf94e660', 'd094e660', 'd194e660', 'd294e660', 'd394e660', 'd494e660', 'd594e660', 'd694e660', 'd794e660', 'd894e660', 'd994e660', 'da94e660', 'db94e660', 'dc94e660', 'dd94e660', 'de94e660', 'df94e660', 'e094e660', 'e194e660', 'e294e660', 'e394e660', 'e494e660', 'e594e660', 'e694e660', 'e794e660', 'e894e660', 'e994e660', 'ea94e660', 'eb94e660', 'ec94e660', 'ed94e660', 'ee94e660', 'ef94e660', 'f094e660', 'f194e660', 'f294e660', 'f394e660', 'f494e660', 'f594e660', 'f694e660', 'f794e660', 'f894e660', 'f994e660', 'fa94e660', 'fb94e660', 'fc94e660', 'fd94e660', 'fe94e660', 'ff94e660', '8095e660', '8195e660', '8295e660', '8395e660', '8495e660', '8595e660', '8695e660', '8795e660', '8895e660', '8995e660', '8a95e660', '8b95e660', '8c95e660', '8d95e660', '8e95e660', '8f95e660', '9095e660', '9195e660', '9295e660', '9395e660', '9495e660', '9595e660', '9695e660', '9795e660', '9895e660', '9995e660', '9a95e660', '9b95e660', '9c95e660', '9d95e660', '9e95e660', '9f95e660', 'a095e660', 'a195e660', 'a295e660', 'a395e660', 'a495e660', 'a595e660', 'a695e660', 'a795e660', 'a895e660', 'a995e660', 'aa95e660', 'ab95e660', 'ac95e660', 'ad95e660', 'ae95e660', 'af95e660', 'b095e660', 'b195e660', 'b295e660', 'b395e660', 'b495e660', 'b595e660', 'b695e660', 'b795e660', 'b895e660', 'b995e660', 'ba95e660', 'bb95e660', 'bc95e660', 'bd95e660', 'be95e660', 'bf95e660', 'c095e660', 'c195e660', 'c295e660', 'c395e660', 'c495e660', 'c595e660', 'c695e660', 'c795e660', 'c895e660', 'c995e660', 'ca95e660', 'cb95e660', 'cc95e660', 'cd95e660', 'ce95e660', 'cf95e660', 'd095e660', 'd195e660', 'd295e660', 'd395e660', 'd495e660', 'd595e660', 'd695e660', 'd795e660', 'd895e660', 'd995e660', 'da95e660', 'db95e660', 'dc95e660', 'dd95e660', 'de95e660', 'df95e660', 'e095e660', 'e195e660', 'e295e660', 'e395e660', 'e495e660', 'e595e660', 'e695e660', 'e795e660', 'e895e660', 'e995e660', 'ea95e660', 'eb95e660', 'ec95e660', 'ed95e660', 'ee95e660', 'ef95e660', 'f095e660', 'f195e660', 'f295e660', 'f395e660', 'f495e660', 'f595e660', 'f695e660', 'f795e660', 'f895e660', 'f995e660', 'fa95e660', 'fb95e660', 'fc95e660', 'fd95e660', 'fe95e660', 'ff95e660', '8096e660', '8196e660', '8296e660', '8396e660', '8496e660', '8596e660', '8696e660', '8796e660', '8896e660', '8996e660', '8a96e660', '8b96e660', '8c96e660', '8d96e660', '8e96e660', '8f96e660', '9096e660', '9196e660', '9296e660', '9396e660', '9496e660', '9596e660', '9696e660', '9796e660', '9896e660', '9996e660', '9a96e660', '9b96e660', '9c96e660', '9d96e660', '9e96e660', '9f96e660', 'a096e660', 'a196e660', 'a296e660', 'a396e660', 'a496e660', 'a596e660', 'a696e660' ,'c1b5ce64', 'c2b5ce64', 'c3b5ce64', 'c4b5ce64', 'c5b5ce64', 'c6b5ce64', 'c7b5ce64', 'c8b5ce64', 'c9b5ce64', 'cab5ce64', 'cbb5ce64', 'ccb5ce64', 'cdb5ce64', 'ceb5ce64', 'cfb5ce64', 'd0b5ce64', 'd1b5ce64', 'd2b5ce64', 'd3b5ce64', 'd4b5ce64', 'd5b5ce64', 'd6b5ce64', 'd7b5ce64', 'd8b5ce64', 'd9b5ce64', 'dab5ce64', 'dbb5ce64', 'dcb5ce64', 'ddb5ce64', 'deb5ce64', 'dfb5ce64', 'e0b5ce64', 'e1b5ce64', 'e2b5ce64', 'e3b5ce64', 'e4b5ce64', 'e5b5ce64', 'e6b5ce64', 'e7b5ce64', 'e8b5ce64', 'e9b5ce64', 'eab5ce64', 'ebb5ce64', 'ecb5ce64', 'edb5ce64', 'eeb5ce64', 'efb5ce64', 'f0b5ce64', 'f1b5ce64', 'f2b5ce64', 'f3b5ce64', 'f4b5ce64', 'f5b5ce64', 'f6b5ce64', 'f7b5ce64', 'f8b5ce64', 'f9b5ce64', 'fab5ce64', 'fbb5ce64', 'fcb5ce64', 'fdb5ce64', 'feb5ce64', 'ffb5ce64', '80b6ce64', '81b6ce64', '82b6ce64', '83b6ce64', '84b6ce64', '85b6ce64', '86b6ce64', '87b6ce64', '88b6ce64', '89b6ce64', '8ab6ce64', '8bb6ce64', '8cb6ce64', '8db6ce64', '8eb6ce64', '8fb6ce64', '90b6ce64', '91b6ce64', '92b6ce64', '93b6ce64', '94b6ce64', '95b6ce64', '96b6ce64', '97b6ce64', '98b6ce64', '99b6ce64', '9ab6ce64', '9bb6ce64', '9cb6ce64', '9db6ce64', '9eb6ce64', '9fb6ce64', 'a0b6ce64', 'a1b6ce64', 'a2b6ce64', 'a3b6ce64', 'a4b6ce64', 'a5b6ce64', 'a6b6ce64', 'a7b6ce64', 'a8b6ce64', 'a9b6ce64', 'aab6ce64', 'abb6ce64', 'acb6ce64', 'adb6ce64', 'aeb6ce64', 'afb6ce64', 'b0b6ce64', 'b1b6ce64', 'b2b6ce64', 'b3b6ce64', 'b4b6ce64', 'b5b6ce64', 'b6b6ce64', 'b7b6ce64', 'b8b6ce64', 'b9b6ce64', 'bab6ce64', 'bbb6ce64', 'bcb6ce64', 'bdb6ce64', 'beb6ce64', 'bfb6ce64', 'c0b6ce64', 'c1b6ce64', 'c2b6ce64', 'c3b6ce64', 'c4b6ce64', 'c5b6ce64', 'c6b6ce64', 'c7b6ce64', 'c8b6ce64', 'c9b6ce64', 'cab6ce64', 'cbb6ce64', 'ccb6ce64', 'cdb6ce64', 'ceb6ce64', 'cfb6ce64', 'd0b6ce64', 'd1b6ce64', 'd2b6ce64', 'd3b6ce64', 'd4b6ce64', 'd5b6ce64', 'd6b6ce64', 'd7b6ce64', 'd8b6ce64', 'd9b6ce64', 'dab6ce64', 'dbb6ce64', 'dcb6ce64', 'ddb6ce64', 'deb6ce64', 'dfb6ce64', 'e0b6ce64', 'e1b6ce64', 'e2b6ce64', 'e3b6ce64', 'e4b6ce64', 'e5b6ce64', 'e6b6ce64', 'e7b6ce64', 'e8b6ce64', 'e9b6ce64', 'eab6ce64', 'ebb6ce64', 'ecb6ce64', 'edb6ce64', 'eeb6ce64', 'efb6ce64', 'f0b6ce64', 'f1b6ce64', 'f2b6ce64', 'f3b6ce64', 'f4b6ce64', 'f5b6ce64', 'f6b6ce64', 'f7b6ce64', 'f8b6ce64', 'f9b6ce64', 'fab6ce64', 'fbb6ce64', 'fcb6ce64', 'fdb6ce64', 'feb6ce64', 'ffb6ce64', '80b7ce64', '81b7ce64', '82b7ce64', '83b7ce64', '84b7ce64', '85b7ce64', '86b7ce64', '87b7ce64', '88b7ce64', '89b7ce64', '8ab7ce64', '8bb7ce64', '8cb7ce64', '8db7ce64', '8eb7ce64', '8fb7ce64', '90b7ce64', '91b7ce64', '92b7ce64', '93b7ce64', '94b7ce64', '95b7ce64', '96b7ce64', '97b7ce64', '98b7ce64', '99b7ce64', '9ab7ce64', '9bb7ce64', '9cb7ce64', '9db7ce64', '9eb7ce64', '9fb7ce64', 'a0b7ce64', 'a1b7ce64', 'a2b7ce64', 'a3b7ce64', 'a4b7ce64', 'a5b7ce64', 'a6b7ce64', 'a7b7ce64', 'a8b7ce64', 'a9b7ce64', 'aab7ce64', 'abb7ce64', 'acb7ce64', 'adb7ce64', 'aeb7ce64', 'afb7ce64', 'b0b7ce64', 'b1b7ce64', 'b2b7ce64', 'b3b7ce64', 'b4b7ce64', 'b5b7ce64', 'b6b7ce64', 'b7b7ce64', 'b8b7ce64', 'b9b7ce64', 'bab7ce64', 'bbb7ce64', 'bcb7ce64', 'bdb7ce64', 'beb7ce64', 'bfb7ce64', 'c0b7ce64', 'c1b7ce64', 'c2b7ce64', 'c3b7ce64', 'c4b7ce64', 'c5b7ce64', 'c6b7ce64', 'c7b7ce64', 'c8b7ce64', 'c9b7ce64', 'cab7ce64', 'cbb7ce64', 'ccb7ce64', 'cdb7ce64', 'ceb7ce64', 'cfb7ce64', 'd0b7ce64', 'd1b7ce64', 'd2b7ce64', 'd3b7ce64', 'd4b7ce64', 'd5b7ce64', 'd6b7ce64', 'd7b7ce64', 'd8b7ce64', 'd9b7ce64', 'dab7ce64', 'dbb7ce64', 'dcb7ce64', 'ddb7ce64', 'deb7ce64', 'dfb7ce64', 'e0b7ce64', 'e1b7ce64', 'e2b7ce64', 'e3b7ce64', 'e4b7ce64', 'e5b7ce64', 'e6b7ce64', 'e7b7ce64', 'e8b7ce64', 'e9b7ce64', 'eab7ce64', 'ebb7ce64', 'ecb7ce64', 'edb7ce64', 'eeb7ce64', 'efb7ce64', 'f0b7ce64', 'f1b7ce64', 'f2b7ce64', 'f3b7ce64', 'f4b7ce64', 'f5b7ce64', 'f6b7ce64', 'f7b7ce64', 'f8b7ce64', 'f9b7ce64', 'fab7ce64', 'fbb7ce64', 'fcb7ce64', 'fdb7ce64', 'feb7ce64', 'ffb7ce64', '80b8ce64', '81b8ce64', '82b8ce64', '83b8ce64', '84b8ce64', '85b8ce64', '86b8ce64', '87b8ce64', '88b8ce64', '89b8ce64', '8ab8ce64', '8bb8ce64', '8cb8ce64', '8db8ce64', '8eb8ce64', '8fb8ce64', '90b8ce64', '91b8ce64', '92b8ce64', '93b8ce64', '94b8ce64', '95b8ce64', '96b8ce64', '97b8ce64', '98b8ce64', '99b8ce64', '9ab8ce64', '9bb8ce64', '9cb8ce64', '9db8ce64', '9eb8ce64', '9fb8ce64', 'a0b8ce64', 'a1b8ce64', 'a2b8ce64', 'a3b8ce64', 'a4b8ce64', 'a5b8ce64', 'a6b8ce64', 'a7b8ce64', 'a8b8ce64', 'a9b8ce64', 'aab8ce64', 'abb8ce64', 'acb8ce64', 'adb8ce64', 'aeb8ce64', 'afb8ce64', 'b0b8ce64', 'b1b8ce64', 'b2b8ce64', 'b3b8ce64', 'b4b8ce64', 'b5b8ce64', 'b6b8ce64', 'b7b8ce64', 'b8b8ce64', 'b9b8ce64', 'bab8ce64', 'bbb8ce64', 'bcb8ce64', 'bdb8ce64', 'beb8ce64', 'bfb8ce64', 'c0b8ce64', 'c1b8ce64', 'c2b8ce64', 'c3b8ce64', 'c4b8ce64', 'c5b8ce64', 'c6b8ce64', 'c7b8ce64', 'c8b8ce64', 'c9b8ce64', 'cab8ce64', 'cbb8ce64', 'ccb8ce64', 'cdb8ce64', 'ceb8ce64', 'cfb8ce64', 'd0b8ce64', 'd1b8ce64', 'd2b8ce64', 'd3b8ce64', 'd4b8ce64', 'd5b8ce64', 'd6b8ce64', 'd7b8ce64', 'd8b8ce64', 'd9b8ce64', 'dab8ce64', 'dbb8ce64', 'dcb8ce64', 'ddb8ce64', 'deb8ce64', 'dfb8ce64', 'e0b8ce64', 'e1b8ce64', 'e2b8ce64', 'e3b8ce64', 'e4b8ce64', 'e5b8ce64', 'e6b8ce64', 'e7b8ce64', 'e8b8ce64', 'e9b8ce64', 'eab8ce64', 'ebb8ce64', 'ecb8ce64', 'edb8ce64', 'eeb8ce64', 'efb8ce64', 'f0b8ce64', 'f1b8ce64', 'f2b8ce64', 'f3b8ce64', 'f4b8ce64', 'f5b8ce64', 'f6b8ce64', 'f7b8ce64', 'f8b8ce64', 'f9b8ce64', 'fab8ce64', 'fbb8ce64', 'fcb8ce64', 'fdb8ce64', 'feb8ce64', 'ffb8ce64', '80b9ce64', '81b9ce64', '82b9ce64', '83b9ce64', '84b9ce64', '85b9ce64', '86b9ce64', '87b9ce64', '88b9ce64', '89b9ce64', '8ab9ce64', '8bb9ce64', '8cb9ce64', '8db9ce64', '8eb9ce64', '8fb9ce64', '90b9ce64', '91b9ce64', '92b9ce64', '93b9ce64', '94b9ce64', '95b9ce64', '96b9ce64', '97b9ce64', '98b9ce64', '99b9ce64', '9ab9ce64', '9bb9ce64', '9cb9ce64', '9db9ce64', '9eb9ce64', '9fb9ce64', 'a0b9ce64', 'a1b9ce64', 'a2b9ce64', 'a3b9ce64', 'a4b9ce64', 'a5b9ce64', 'a6b9ce64', 'a7b9ce64', 'a8b9ce64', 'a9b9ce64', 'aab9ce64', 'abb9ce64', 'acb9ce64', 'adb9ce64', 'aeb9ce64', 'afb9ce64', 'b0b9ce64', 'b1b9ce64', 'b2b9ce64', 'b3b9ce64', 'b4b9ce64', 'b5b9ce64', 'b6b9ce64', 'b7b9ce64', 'b8b9ce64', 'b9b9ce64', 'bab9ce64', 'bbb9ce64', 'bcb9ce64', 'bdb9ce64', 'beb9ce64', 'bfb9ce64', 'c0b9ce64', 'c1b9ce64', 'c2b9ce64', 'c3b9ce64', 'c4b9ce64', 'c5b9ce64', 'c6b9ce64', 'c7b9ce64', 'c8b9ce64', 'c9b9ce64', 'cab9ce64', 'cbb9ce64', 'ccb9ce64', 'cdb9ce64', 'ceb9ce64', 'cfb9ce64', 'd0b9ce64', 'd1b9ce64', 'd2b9ce64', 'd3b9ce64', 'd4b9ce64', 'd5b9ce64', 'd6b9ce64', 'd7b9ce64', 'd8b9ce64', 'd9b9ce64', 'dab9ce64', 'dbb9ce64', 'dcb9ce64', 'ddb9ce64', 'deb9ce64', 'dfb9ce64', 'e0b9ce64', 'e1b9ce64', 'e2b9ce64', 'e3b9ce64', 'e4b9ce64', 'e5b9ce64', 'e6b9ce64', 'e7b9ce64', 'e8b9ce64', 'e9b9ce64', 'eab9ce64', 'ebb9ce64', 'ecb9ce64', 'edb9ce64', 'eeb9ce64', 'efb9ce64', 'f0b9ce64', 'f1b9ce64', 'f2b9ce64', 'f3b9ce64', 'f4b9ce64', 'f5b9ce64', 'f6b9ce64', 'f7b9ce64', 'f8b9ce64', 'f9b9ce64', 'fab9ce64', 'fbb9ce64', 'fcb9ce64', 'fdb9ce64', 'feb9ce64', 'ffb9ce64', '80bace64', '81bace64', '82bace64', '83bace64', '84bace64', '85bace64', '86bace64', '87bace64', '88bace64', '89bace64', '8abace64', '8bbace64', '8cbace64', '8dbace64', '8ebace64', '8fbace64', '90bace64', '91bace64', '92bace64', '93bace64', '94bace64', '95bace64', '96bace64', '97bace64', '98bace64', '99bace64', '9abace64', '9bbace64', '9cbace64', '9dbace64', '9ebace64', '9fbace64', 'a0bace64', 'a1bace64', 'a2bace64', 'a3bace64', 'a4bace64', 'a5bace64', 'a6bace64', 'a7bace64', 'a8bace64', 'a9bace64', 'aabace64', 'abbace64', 'acbace64', 'adbace64', 'aebace64', 'afbace64', 'b0bace64', 'b1bace64', 'b2bace64', 'b3bace64', 'b4bace64', 'b5bace64', 'b6bace64', 'b7bace64', 'b8bace64', 'b9bace64', 'babace64', 'bbbace64', 'bcbace64', 'bdbace64' ,'bebace64', 'bfbace64', 'c0bace64', 'c1bace64', 'c2bace64', 'c3bace64', 'c4bace64', 'c5bace64', 'c6bace64', 'c7bace64', 'c8bace64', 'c9bace64', 'cabace64', 'cbbace64', 'ccbace64', 'cdbace64', 'cebace64', 'cfbace64', 'd0bace64', 'd1bace64', 'd2bace64', 'd3bace64', 'd4bace64', 'd5bace64', 'd6bace64', 'd7bace64', 'd8bace64', 'd9bace64', 'dabace64', 'dbbace64', 'dcbace64', 'ddbace64', 'debace64', 'dfbace64', 'e0bace64', 'e1bace64', 'e2bace64', 'e3bace64', 'e4bace64', 'e5bace64', 'e6bace64', 'e7bace64', 'e8bace64', 'e9bace64', 'eabace64', 'ebbace64', 'ecbace64', 'edbace64', 'eebace64', 'efbace64', 'f0bace64', 'f1bace64', 'f2bace64', 'f3bace64', 'f4bace64', 'f5bace64', 'f6bace64', 'f7bace64', 'f8bace64', 'f9bace64', 'fabace64', 'fbbace64', 'fcbace64', 'fdbace64', 'febace64', 'ffbace64', '80bbce64', '81bbce64', '82bbce64', '83bbce64', '84bbce64', '85bbce64', '86bbce64', '87bbce64', '88bbce64', '89bbce64', '8abbce64', '8bbbce64', '8cbbce64', '8dbbce64', '8ebbce64', '8fbbce64', '90bbce64', '91bbce64', '92bbce64', '93bbce64', '94bbce64', '95bbce64', '96bbce64', '97bbce64', '98bbce64', '99bbce64', '9abbce64', '9bbbce64', '9cbbce64', '9dbbce64', '9ebbce64', '9fbbce64', 'a0bbce64', 'a1bbce64', 'a2bbce64', 'a3bbce64', 'a4bbce64', 'a5bbce64', 'a6bbce64', 'a7bbce64', 'a8bbce64', 'a9bbce64', 'aabbce64', 'abbbce64', 'acbbce64', 'adbbce64', 'aebbce64', 'afbbce64', 'b0bbce64', 'b1bbce64', 'b2bbce64', 'b3bbce64', 'b4bbce64', 'b5bbce64', 'b6bbce64', 'b7bbce64', 'b8bbce64', 'b9bbce64', 'babbce64', 'bbbbce64', 'bcbbce64', 'bdbbce64', 'bebbce64', 'bfbbce64', 'c0bbce64', 'c1bbce64', 'c2bbce64', 'c3bbce64', 'c4bbce64', 'c5bbce64', 'c6bbce64', 'c7bbce64', 'c8bbce64', 'c9bbce64', 'cabbce64', 'cbbbce64', 'ccbbce64', 'cdbbce64', 'cebbce64', 'cfbbce64', 'd0bbce64', 'd1bbce64', 'd2bbce64', 'd3bbce64', 'd4bbce64', 'd5bbce64', 'd6bbce64', 'd7bbce64', 'd8bbce64', 'd9bbce64', 'dabbce64', 'dbbbce64', 'dcbbce64', 'ddbbce64', 'debbce64', 'dfbbce64', 'e0bbce64', 'e1bbce64', 'e2bbce64', 'e3bbce64', 'e4bbce64', 'e5bbce64', 'e6bbce64', 'e7bbce64', 'e8bbce64', 'e9bbce64', 'eabbce64', 'ebbbce64', 'ecbbce64', 'edbbce64', 'eebbce64', 'efbbce64', 'f0bbce64', 'f1bbce64', 'f2bbce64', 'f3bbce64', 'f4bbce64', 'f5bbce64', 'f6bbce64', 'f7bbce64', 'f8bbce64', 'f9bbce64', 'fabbce64', 'fbbbce64', 'fcbbce64', 'fdbbce64', 'febbce64', 'ffbbce64', '80bcce64', '81bcce64', '82bcce64', '83bcce64', '84bcce64', '85bcce64', '86bcce64', '87bcce64', '88bcce64', '89bcce64', '8abcce64', '8bbcce64', '8cbcce64', '8dbcce64', '8ebcce64', '8fbcce64', '90bcce64', '91bcce64', '92bcce64', '93bcce64', '94bcce64', '95bcce64', '96bcce64', '97bcce64', '98bcce64', '99bcce64', '9abcce64', '9bbcce64', '9cbcce64', '9dbcce64', '9ebcce64', '9fbcce64', 'a0bcce64', 'a1bcce64', 'a2bcce64', 'a3bcce64', 'a4bcce64', 'a5bcce64', 'a6bcce64', 'a7bcce64', 'a8bcce64', 'a9bcce64', 'aabcce64', 'abbcce64', 'acbcce64', 'adbcce64', 'aebcce64', 'afbcce64', 'b0bcce64', 'b1bcce64', 'b2bcce64', 'b3bcce64', 'b4bcce64', 'b5bcce64', 'b6bcce64', 'b7bcce64', 'b8bcce64', 'b9bcce64', 'babcce64', 'bbbcce64', 'bcbcce64', 'bdbcce64', 'bebcce64', 'bfbcce64', 'c0bcce64', 'c1bcce64', 'c2bcce64', 'c3bcce64', 'c4bcce64', 'c5bcce64', 'c6bcce64', 'c7bcce64', 'c8bcce64', 'c9bcce64', 'cabcce64', 'cbbcce64', 'ccbcce64', 'cdbcce64', 'cebcce64', 'cfbcce64', 'd0bcce64', 'd1bcce64', 'd2bcce64', 'd3bcce64', 'd4bcce64', 'd5bcce64', 'd6bcce64', 'd7bcce64', 'd8bcce64', 'd9bcce64', 'dabcce64', 'dbbcce64', 'dcbcce64', 'ddbcce64', 'debcce64', 'dfbcce64', 'e0bcce64', 'e1bcce64', 'e2bcce64', 'e3bcce64', 'e4bcce64', 'e5bcce64', 'e6bcce64', 'e7bcce64', 'e8bcce64', 'e9bcce64', 'eabcce64', 'ebbcce64', 'ecbcce64', 'edbcce64', 'eebcce64', 'efbcce64', 'f0bcce64', 'f1bcce64', 'f2bcce64', 'f3bcce64', 'f4bcce64', 'f5bcce64', 'f6bcce64', 'f7bcce64', 'f8bcce64', 'f9bcce64', 'fabcce64', 'fbbcce64', 'fcbcce64', 'fdbcce64', 'febcce64', 'ffbcce64', '80bdce64', '81bdce64', '82bdce64', '83bdce64', '84bdce64', '85bdce64', '86bdce64', '87bdce64', '88bdce64', '89bdce64', '8abdce64', '8bbdce64', '8cbdce64', '8dbdce64', '8ebdce64', '8fbdce64', '90bdce64', '91bdce64', '92bdce64', '93bdce64', '94bdce64', '95bdce64', '96bdce64', '97bdce64', '98bdce64', '99bdce64', '9abdce64', '9bbdce64', '9cbdce64', '9dbdce64', '9ebdce64', '9fbdce64', 'a0bdce64', 'a1bdce64', 'a2bdce64', 'a3bdce64', 'a4bdce64', 'a5bdce64', 'a6bdce64', 'a7bdce64', 'a8bdce64', 'a9bdce64', 'aabdce64', 'abbdce64', 'acbdce64', 'adbdce64', 'aebdce64', 'afbdce64', 'b0bdce64', 'b1bdce64', 'b2bdce64', 'b3bdce64', 'b4bdce64', 'b5bdce64', 'b6bdce64', 'b7bdce64', 'b8bdce64', 'b9bdce64', 'babdce64', 'bbbdce64', 'bcbdce64', 'bdbdce64', 'bebdce64', 'bfbdce64', 'c0bdce64', 'c1bdce64', 'c2bdce64', 'c3bdce64', 'c4bdce64', 'c5bdce64', 'c6bdce64', 'c7bdce64', 'c8bdce64', 'c9bdce64', 'cabdce64', 'cbbdce64', 'ccbdce64', 'cdbdce64', 'cebdce64', 'cfbdce64', 'd0bdce64', 'd1bdce64', 'd2bdce64', 'd3bdce64', 'd4bdce64', 'd5bdce64', 'd6bdce64', 'd7bdce64', 'd8bdce64', 'd9bdce64', 'dabdce64', 'dbbdce64', 'dcbdce64', 'ddbdce64', 'debdce64', 'dfbdce64', 'e0bdce64', 'e1bdce64', 'e2bdce64', 'e3bdce64', 'e4bdce64', 'e5bdce64', 'e6bdce64', 'e7bdce64', 'e8bdce64', 'e9bdce64', 'eabdce64', 'ebbdce64', 'ecbdce64', 'edbdce64', 'eebdce64', 'efbdce64', 'f0bdce64', 'f1bdce64', 'f2bdce64', 'f3bdce64', 'f4bdce64', 'f5bdce64', 'f6bdce64', 'f7bdce64', 'f8bdce64', 'f9bdce64', 'fabdce64', 'fbbdce64', 'fcbdce64', 'fdbdce64', 'febdce64', 'ffbdce64', '80bece64', '81bece64', '82bece64', '83bece64', '84bece64', '85bece64', '86bece64', '87bece64', '88bece64', '89bece64', '8abece64', '8bbece64', '8cbece64', '8dbece64', '8ebece64', '8fbece64', '90bece64', '91bece64', '92bece64', '93bece64', '94bece64', '95bece64', '96bece64', '97bece64', '98bece64', '99bece64', '9abece64', '9bbece64', '9cbece64', '9dbece64', '9ebece64', '9fbece64', 'a0bece64', 'a1bece64', 'a2bece64', 'a3bece64', 'a4bece64', 'a5bece64', 'a6bece64', 'a7bece64', 'a8bece64', 'a9bece64', 'aabece64', 'abbece64', 'acbece64', 'adbece64', 'aebece64', 'afbece64', 'b0bece64', 'b1bece64', 'b2bece64', 'b3bece64', 'b4bece64', 'b5bece64', 'b6bece64', 'b7bece64', 'b8bece64', 'b9bece64', 'babece64', 'bbbece64', 'bcbece64', 'bdbece64', 'bebece64', 'bfbece64', 'c0bece64', 'c1bece64', 'c2bece64', 'c3bece64', 'c4bece64', 'c5bece64', 'c6bece64', 'c7bece64', 'c8bece64', 'c9bece64', 'cabece64', 'cbbece64', 'ccbece64', 'cdbece64', 'cebece64', 'cfbece64', 'd0bece64', 'd1bece64', 'd2bece64', 'd3bece64', 'd4bece64', 'd5bece64', 'd6bece64', 'd7bece64', 'd8bece64', 'd9bece64', 'dabece64', 'dbbece64', 'dcbece64', 'ddbece64', 'debece64', 'dfbece64', 'e0bece64', 'e1bece64', 'e2bece64', 'e3bece64', 'e4bece64', 'e5bece64', 'e6bece64', 'e7bece64', 'e8bece64', 'e9bece64', 'eabece64', 'ebbece64', 'ecbece64', 'edbece64', 'eebece64', 'efbece64', 'f0bece64', 'f1bece64', 'f2bece64', 'f3bece64', 'f4bece64', 'f5bece64', 'f6bece64', 'f7bece64', 'f8bece64', 'f9bece64', 'fabece64', 'fbbece64', 'fcbece64', 'fdbece64', 'febece64', 'ffbece64', '80bfce64', '81bfce64', '82bfce64', '83bfce64', '84bfce64', '85bfce64', '86bfce64', '87bfce64', '88bfce64', '89bfce64', '8abfce64', '8bbfce64', '8cbfce64', '8dbfce64', '8ebfce64', '8fbfce64', '90bfce64', '91bfce64', '92bfce64', '93bfce64', '94bfce64', '95bfce64', '96bfce64', '97bfce64', '98bfce64', '99bfce64', '9abfce64', '9bbfce64', '9cbfce64', '9dbfce64', '9ebfce64', '9fbfce64', 'a0bfce64', 'a1bfce64', 'a2bfce64', 'a3bfce64', 'a4bfce64', 'a5bfce64', 'a6bfce64', 'a7bfce64', 'a8bfce64', 'a9bfce64', 'aabfce64', 'abbfce64', 'acbfce64', 'adbfce64', 'aebfce64', 'afbfce64', 'b0bfce64', 'b1bfce64', 'b2bfce64', 'b3bfce64', 'b4bfce64', 'b5bfce64', 'b6bfce64', 'b7bfce64', 'b8bfce64', 'b9bfce64', 'babfce64', 'bbbfce64', 'bcbfce64', 'bdbfce64', 'bebfce64', 'bfbfce64', 'c0bfce64', 'c1bfce64', 'c2bfce64', 'c3bfce64', 'c4bfce64', 'c5bfce64', 'c6bfce64', 'c7bfce64', 'c8bfce64', 'c9bfce64', 'cabfce64', 'cbbfce64', 'ccbfce64', 'cdbfce64', 'cebfce64', 'cfbfce64', 'd0bfce64', 'd1bfce64', 'd2bfce64', 'd3bfce64', 'd4bfce64', 'd5bfce64', 'd6bfce64', 'd7bfce64', 'd8bfce64', 'd9bfce64', 'dabfce64', 'dbbfce64', 'dcbfce64', 'ddbfce64', 'debfce64', 'dfbfce64', 'e0bfce64', 'e1bfce64', 'e2bfce64', 'e3bfce64', 'e4bfce64', 'e5bfce64', 'e6bfce64', 'e7bfce64', 'e8bfce64', 'e9bfce64', 'eabfce64', 'ebbfce64', 'ecbfce64', 'edbfce64', 'eebfce64', 'efbfce64', 'f0bfce64', 'f1bfce64', 'f2bfce64', 'f3bfce64', 'f4bfce64', 'f5bfce64', 'f6bfce64', 'f7bfce64', 'f8bfce64', 'f9bfce64', 'fabfce64', 'fbbfce64','8196a361', '8296a361', '8396a361', '8496a361', '8596a361', '8696a361', '8796a361', '8896a361', '8996a361', '8a96a361', '8b96a361', '8c96a361', '8d96a361', '8e96a361', '8f96a361', '9096a361', '9196a361', '9296a361', '9396a361', '9496a361', '9596a361', '9696a361', '9796a361', '9896a361', '9996a361', '9a96a361', '9b96a361', '9c96a361', '9d96a361', '9e96a361', '9f96a361', 'a096a361', 'a196a361', 'a296a361', 'a396a361', 'a496a361', 'a596a361', 'a696a361', 'a796a361', 'a896a361', 'a996a361', 'aa96a361', 'ab96a361', 'ac96a361', 'ad96a361', 'ae96a361', 'af96a361', 'b096a361', 'b196a361', 'b296a361', 'b396a361', 'b496a361', 'b596a361', 'b696a361', 'b796a361', 'b896a361', 'b996a361', 'ba96a361', 'bb96a361', 'bc96a361', 'bd96a361', 'be96a361', 'bf96a361', 'c096a361', 'c196a361', 'c296a361', 'c396a361', 'c496a361', 'c596a361', 'c696a361', 'c796a361', 'c896a361', 'c996a361', 'ca96a361', 'cb96a361', 'cc96a361', 'cd96a361', 'ce96a361', 'cf96a361', 'd096a361', 'd196a361', 'd296a361', 'd396a361', 'd496a361', 'd596a361', 'd696a361', 'd796a361', 'd896a361', 'd996a361', 'da96a361', 'db96a361', 'dc96a361', 'dd96a361', 'de96a361', 'df96a361', 'e096a361', 'e196a361', 'e296a361', 'e396a361', 'e496a361', 'e596a361', 'e696a361', 'e796a361', 'e896a361', 'e996a361', 'ea96a361', 'eb96a361', 'ec96a361', 'ed96a361', 'ee96a361', 'ef96a361', 'f096a361', 'f196a361', 'f296a361', 'f396a361', 'f496a361', 'f596a361', 'f696a361', 'f796a361', 'f896a361', 'f996a361', 'fa96a361', 'fb96a361', 'fc96a361', 'fd96a361', 'fe96a361', 'ff96a361', '8097a361', '8197a361', '8297a361', '8397a361', '8497a361', '8597a361', '8697a361', '8797a361', '8897a361', '8997a361', '8a97a361', '8b97a361', '8c97a361', '8d97a361', '8e97a361', '8f97a361', '9097a361', '9197a361', '9297a361', '9397a361', '9497a361', '9597a361', '9697a361', '9797a361', '9897a361', '9997a361', '9a97a361', '9b97a361', '9c97a361', '9d97a361', '9e97a361', '9f97a361', 'a097a361', 'a197a361', 'a297a361', 'a397a361', 'a497a361', 'a597a361', 'a697a361', 'a797a361', 'a897a361', 'a997a361', 'aa97a361', 'ab97a361', 'ac97a361', 'ad97a361', 'ae97a361', 'af97a361', 'b097a361', 'b197a361', 'b297a361', 'b397a361', 'b497a361', 'b597a361', 'b697a361', 'b797a361', 'b897a361', 'b997a361', 'ba97a361', 'bb97a361', 'bc97a361', 'bd97a361', 'be97a361', 'bf97a361', 'c097a361', 'c197a361', 'c297a361', 'c397a361', 'c497a361', 'c597a361', 'c697a361', 'c797a361', 'c897a361', 'c997a361', 'ca97a361', 'cb97a361', 'cc97a361', 'cd97a361', 'ce97a361', 'cf97a361', 'd097a361', 'd197a361', 'd297a361', 'd397a361', 'd497a361', 'd597a361', 'd697a361', 'd797a361', 'd897a361', 'd997a361', 'da97a361', 'db97a361', 'dc97a361', 'dd97a361', 'de97a361', 'df97a361', 'e097a361', 'e197a361', 'e297a361', 'e397a361', 'e497a361', 'e597a361', 'e697a361', 'e797a361', 'e897a361', 'e997a361', 'ea97a361', 'eb97a361', 'ec97a361', 'ed97a361', 'ee97a361', 'ef97a361', 'f097a361', 'f197a361', 'f297a361', 'f397a361', 'f497a361', 'f597a361', 'f697a361', 'f797a361', 'f897a361', 'f997a361', 'fa97a361', 'fb97a361', 'fc97a361', 'fd97a361', 'fe97a361', 'ff97a361', '8098a361', '8198a361', '8298a361', '8398a361', '8498a361', '8598a361', '8698a361', '8798a361', '8898a361', '8998a361', '8a98a361', '8b98a361', '8c98a361', '8d98a361', '8e98a361', '8f98a361', '9098a361', '9198a361', '9298a361', '9398a361', '9498a361', '9598a361', '9698a361', '9798a361', '9898a361', '9998a361', '9a98a361', '9b98a361', '9c98a361', '9d98a361', '9e98a361', '9f98a361', 'a098a361', 'a198a361', 'a298a361', 'a398a361', 'a498a361', 'a598a361', 'a698a361', 'a798a361', 'a898a361', 'a998a361', 'aa98a361', 'ab98a361', 'ac98a361', 'ad98a361', 'ae98a361', 'af98a361', 'b098a361', 'b198a361', 'b298a361', 'b398a361', 'b498a361', 'b598a361', 'b698a361', 'b798a361', 'b898a361', 'b998a361', 'ba98a361', 'bb98a361', 'bc98a361', 'bd98a361', 'be98a361', 'bf98a361', 'c098a361', 'c198a361', 'c298a361', 'c398a361', 'c498a361', 'c598a361', 'c698a361', 'c798a361', 'c898a361', 'c998a361', 'ca98a361', 'cb98a361', 'cc98a361', 'cd98a361', 'ce98a361', 'cf98a361', 'd098a361', 'd198a361', 'd298a361', 'd398a361', 'd498a361', 'd598a361', 'd698a361', 'd798a361', 'd898a361', 'd998a361', 'da98a361', 'db98a361', 'dc98a361', 'dd98a361', 'de98a361', 'df98a361', 'e098a361', 'e198a361', 'e298a361', 'e398a361', 'e498a361', 'e598a361', 'e698a361', 'e798a361', 'e898a361', 'e998a361', 'ea98a361', 'eb98a361', 'ec98a361', 'ed98a361', 'ee98a361', 'ef98a361', 'f098a361', 'f198a361', 'f298a361', 'f398a361', 'f498a361', 'f598a361', 'f698a361', 'f798a361', 'f898a361', 'f998a361', 'fa98a361', 'fb98a361', 'fc98a361', 'fd98a361', 'fe98a361', 'ff98a361', '8099a361', '8199a361', '8299a361', '8399a361', '8499a361', '8599a361', '8699a361', '8799a361', '8899a361', '8999a361', '8a99a361', '8b99a361', '8c99a361', '8d99a361', '8e99a361', '8f99a361', '9099a361', '9199a361', '9299a361', '9399a361', '9499a361', '9599a361', '9699a361', '9799a361', '9899a361', '9999a361', '9a99a361', '9b99a361', '9c99a361', '9d99a361', '9e99a361', '9f99a361', 'a099a361', 'a199a361', 'a299a361', 'a399a361', 'a499a361', 'a599a361', 'a699a361', 'a799a361', 'a899a361', 'a999a361', 'aa99a361', 'ab99a361', 'ac99a361', 'ad99a361', 'ae99a361', 'af99a361', 'b099a361', 'b199a361', 'b299a361', 'b399a361', 'b499a361', 'b599a361', 'b699a361', 'b799a361', 'b899a361', 'b999a361', 'ba99a361', 'bb99a361', 'bc99a361', 'bd99a361', 'be99a361', 'bf99a361', 'c099a361', 'c199a361', 'c299a361', 'c399a361', 'c499a361', 'c599a361', 'c699a361', 'c799a361', 'c899a361', 'c999a361', 'ca99a361', 'cb99a361', 'cc99a361', 'cd99a361', 'ce99a361', 'cf99a361', 'd099a361', 'd199a361', 'd299a361', 'd399a361', 'd499a361', 'd599a361', 'd699a361', 'd799a361', 'd899a361', 'd999a361', 'da99a361', 'db99a361', 'dc99a361', 'dd99a361', 'de99a361', 'df99a361', 'e099a361', 'e199a361', 'e299a361', 'e399a361', 'e499a361', 'e599a361', 'e699a361', 'e799a361', 'e899a361', 'e999a361', 'ea99a361', 'eb99a361', 'ec99a361', 'ed99a361', 'ee99a361', 'ef99a361', 'f099a361', 'f199a361', 'f299a361', 'f399a361', 'f499a361', 'f599a361', 'f699a361', 'f799a361', 'f899a361', 'f999a361', 'fa99a361', 'fb99a361', 'fc99a361', 'fd99a361', 'fe99a361', 'ff99a361', '809aa361', '819aa361', '829aa361', '839aa361', '849aa361', '859aa361', '869aa361', '879aa361', '889aa361', '899aa361', '8a9aa361', '8b9aa361', '8c9aa361', '8d9aa361', '8e9aa361', '8f9aa361', '909aa361', '919aa361', '929aa361', '939aa361', '949aa361', '959aa361', '969aa361', '979aa361', '989aa361', '999aa361', '9a9aa361', '9b9aa361', '9c9aa361', '9d9aa361', '9e9aa361', '9f9aa361', 'a09aa361', 'a19aa361', 'a29aa361', 'a39aa361', 'a49aa361', 'a59aa361', 'a69aa361', 'a79aa361', 'a89aa361', 'a99aa361', 'aa9aa361', 'ab9aa361', 'ac9aa361', 'ad9aa361', 'ae9aa361', 'af9aa361', 'b09aa361', 'b19aa361', 'b29aa361', 'b39aa361', 'b49aa361', 'b59aa361', 'b69aa361', 'b79aa361', 'b89aa361', 'b99aa361', 'ba9aa361', 'bb9aa361', 'bc9aa361', 'bd9aa361', 'be9aa361', 'bf9aa361', 'c09aa361', 'c19aa361', 'c29aa361', 'c39aa361', 'c49aa361', 'c59aa361', 'c69aa361', 'c79aa361', 'c89aa361', 'c99aa361', 'ca9aa361', 'cb9aa361', 'cc9aa361', 'cd9aa361', 'ce9aa361', 'cf9aa361', 'd09aa361', 'd19aa361', 'd29aa361', 'd39aa361', 'd49aa361', 'd59aa361', 'd69aa361', 'd79aa361', 'd89aa361', 'd99aa361', 'da9aa361', 'db9aa361', 'dc9aa361', 'dd9aa361', 'de9aa361', 'df9aa361', 'e09aa361', 'e19aa361', 'e29aa361', 'e39aa361', 'e49aa361', 'e59aa361', 'e69aa361', 'e79aa361', 'e89aa361', 'e99aa361', 'ea9aa361', 'eb9aa361', 'ec9aa361', 'ed9aa361', 'ee9aa361', 'ef9aa361', 'f09aa361', 'f19aa361', 'f29aa361', 'f39aa361', 'f49aa361', 'f59aa361', 'f69aa361', 'f79aa361', 'f89aa361', 'f99aa361', 'fa9aa361', 'fb9aa361', 'fc9aa361', 'fd9aa361', 'fe9aa361', 'ff9aa361', '809ba361', '819ba361', '829ba361', '839ba361', '849ba361', '859ba361', '869ba361', '879ba361', '889ba361', '899ba361', '8a9ba361', '8b9ba361', '8c9ba361', '8d9ba361', '8e9ba361', '8f9ba361', '909ba361', '919ba361', '929ba361', '939ba361', '949ba361', '959ba361', '969ba361', '979ba361', '989ba361', '999ba361', '9a9ba361', '9b9ba361', '9c9ba361', '9d9ba361', '9e9ba361', '9f9ba361', 'a09ba361', 'a19ba361', 'a29ba361', 'a39ba361', 'a49ba361', 'a59ba361', 'a69ba361', 'a79ba361', 'a89ba361', 'a99ba361', 'aa9ba361', 'ab9ba361', 'ac9ba361', 'ad9ba361', 'ae9ba361', 'af9ba361', 'b09ba361', 'b19ba361', 'b29ba361', 'b39ba361', 'b49ba361', 'b59ba361', 'b69ba361', 'b79ba361', 'b89ba361', 'b99ba361', 'ba9ba361', 'bb9ba361', 'bc9ba361', 'bd9ba361', 'be9ba361', 'bf9ba361', 'c09ba361', 'c19ba361', 'c29ba361', 'c39ba361', 'c49ba361', 'c59ba361', 'c69ba361', 'c79ba361', 'c89ba361', 'c99ba361', 'ca9ba361', 'cb9ba361', 'cc9ba361', 'cd9ba361', 'ce9ba361', 'cf9ba361', 'd09ba361', 'd19ba361', 'd29ba361', 'd39ba361', 'd49ba361', 'd59ba361', 'd69ba361', 'd79ba361', 'd89ba361', 'd99ba361', 'da9ba361', 'db9ba361', 'dc9ba361', 'dd9ba361', 'de9ba361', 'df9ba361', 'e09ba361', 'e19ba361', 'e29ba361', 'e39ba361', 'e49ba361', 'e59ba361', 'e69ba361', 'e79ba361', 'e89ba361', 'e99ba361', 'ea9ba361', 'eb9ba361', 'ec9ba361', 'ed9ba361', 'ee9ba361', 'ef9ba361', 'f09ba361', 'f19ba361', 'f29ba361', 'f39ba361', 'f49ba361', 'f59ba361', 'f69ba361', 'f79ba361', 'f89ba361', 'f99ba361', 'fa9ba361', 'fb9ba361', 'fc9ba361', 'fd9ba361', 'fe9ba361', 'ff9ba361', '809ca361', '819ca361', '829ca361', '839ca361', '849ca361', '859ca361', '869ca361', '879ca361', '889ca361', '899ca361', '8a9ca361', '8b9ca361', '8c9ca361', '8d9ca361', '8e9ca361', '8f9ca361', '909ca361', '919ca361', '929ca361', '939ca361', '949ca361', '959ca361', '969ca361', '979ca361', '989ca361', '999ca361', '9a9ca361', '9b9ca361', '9c9ca361', '9d9ca361', '9e9ca361', '9f9ca361', 'a09ca361', 'a19ca361', 'a29ca361', 'a39ca361', 'a49ca361', 'a59ca361', 'a69ca361', 'a79ca361', 'a89ca361', 'a99ca361', 'aa9ca361', 'ab9ca361', 'ac9ca361', 'ad9ca361', 'ae9ca361', 'af9ca361', 'b09ca361', 'b19ca361', 'b29ca361', 'b39ca361', 'b49ca361', 'b59ca361', 'b69ca361', 'b79ca361', 'b89ca361', 'b99ca361', 'ba9ca361', 'bb9ca361', 'bc9ca361', 'bd9ca361', 'be9ca361', 'bf9ca361', 'c09ca361', 'c19ca361', 'c29ca361', 'c39ca361', 'c49ca361', 'c59ca361', 'c69ca361', 'c79ca361', 'c89ca361', 'c99ca361', 'ca9ca361', 'cb9ca361', 'cc9ca361', 'cd9ca361', 'ce9ca361', 'cf9ca361', 'd09ca361', 'd19ca361', 'd29ca361', 'd39ca361', 'd49ca361', 'd59ca361', 'd69ca361', 'd79ca361', 'd89ca361', 'd99ca361', 'da9ca361', 'db9ca361', 'dc9ca361', 'dd9ca361', 'de9ca361', 'df9ca361', 'e09ca361', 'e19ca361', 'e29ca361', 'e39ca361', 'e49ca361', 'e59ca361', 'e69ca361', 'e79ca361', 'e89ca361', 'e99ca361', 'ea9ca361', 'eb9ca361', 'ec9ca361', 'ed9ca361', 'ee9ca361', 'ef9ca361', 'f09ca361', 'f19ca361', 'f29ca361', 'f39ca361', 'f49ca361', 'f59ca361', 'f69ca361', 'f79ca361', 'f89ca361', 'f99ca361', 'fa9ca361', 'fb9ca361', 'fc9ca361', 'fd9ca361', 'fe9ca361', 'ff9ca361', '809da361', '819da361', '829da361', '839da361', '849da361', '859da361', '869da361', '879da361', '889da361', '899da361', '8a9da361', '8b9da361', '8c9da361', '8d9da361', '8e9da361', '8f9da361', '909da361', '919da361', '929da361', '939da361', '949da361', '959da361', '969da361', '979da361', '989da361', '999da361', '9a9da361', '9b9da361', '9c9da361', '9d9da361', '9e9da361', '9f9da361', 'a09da361', 'a19da361', 'a29da361', 'a39da361', 'a49da361', 'a59da361', 'a69da361', 'a79da361', 'a89da361', 'a99da361', 'aa9da361', 'ab9da361', 'ac9da361', 'ad9da361', 'ae9da361', 'af9da361', 'b09da361', 'b19da361', 'b29da361', 'b39da361', 'b49da361', 'b59da361', 'b69da361', 'b79da361', 'b89da361', 'b99da361', 'ba9da361', 'bb9da361', 'bc9da361', 'bd9da361', 'be9da361', 'bf9da361', 'c09da361', 'c19da361', 'c29da361', 'c39da361', 'c49da361', 'c59da361', 'c69da361', 'c79da361', 'c89da361', 'c99da361','81c38566', '82c38566', '83c38566', '84c38566', '85c38566', '86c38566', '87c38566', '88c38566', '89c38566', '8ac38566', '8bc38566', '8cc38566', '8dc38566', '8ec38566', '8fc38566', '90c38566', '91c38566', '92c38566', '93c38566', '94c38566', '95c38566', '96c38566', '97c38566', '98c38566', '99c38566', '9ac38566', '9bc38566', '9cc38566', '9dc38566', '9ec38566', '9fc38566', 'a0c38566', 'a1c38566', 'a2c38566', 'a3c38566', 'a4c38566', 'a5c38566', 'a6c38566', 'a7c38566', 'a8c38566', 'a9c38566', 'aac38566', 'abc38566', 'acc38566', 'adc38566', 'aec38566', 'afc38566', 'b0c38566', 'b1c38566', 'b2c38566', 'b3c38566', 'b4c38566', 'b5c38566', 'b6c38566', 'b7c38566', 'b8c38566', 'b9c38566', 'bac38566', 'bbc38566', 'bcc38566', 'bdc38566', 'bec38566', 'bfc38566', 'c0c38566', 'c1c38566', 'c2c38566', 'c3c38566', 'c4c38566', 'c5c38566', 'c6c38566', 'c7c38566', 'c8c38566', 'c9c38566', 'cac38566', 'cbc38566', 'ccc38566', 'cdc38566', 'cec38566', 'cfc38566', 'd0c38566', 'd1c38566', 'd2c38566', 'd3c38566', 'd4c38566', 'd5c38566', 'd6c38566', 'd7c38566', 'd8c38566', 'd9c38566', 'dac38566', 'dbc38566', 'dcc38566', 'ddc38566', 'dec38566', 'dfc38566', 'e0c38566', 'e1c38566', 'e2c38566', 'e3c38566', 'a0dc8766', 'a1dc8766', 'a2dc8766', 'a3dc8766', 'a4dc8766', 'a5dc8766', 'a6dc8766', 'a7dc8766', 'a8dc8766', 'a9dc8766']  # أضف الباقي
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy3: {e}")

                if b"@proxy4" in data and not self.RbGx:
                    try:
                        items_ids = ['c1b5ce64', 'c2b5ce64', 'c3b5ce64', 'c4b5ce64', 'c5b5ce64', 'c6b5ce64', 'c7b5ce64', 'c8b5ce64', 'c9b5ce64', 'cab5ce64', 'cbb5ce64', 'ccb5ce64', 'cdb5ce64', 'ceb5ce64', 'cfb5ce64', 'd0b5ce64', 'd1b5ce64', 'd2b5ce64', 'd3b5ce64', 'd4b5ce64', 'd5b5ce64', 'd6b5ce64', 'd7b5ce64', 'd8b5ce64', 'd9b5ce64', 'dab5ce64', 'dbb5ce64', 'dcb5ce64', 'ddb5ce64', 'deb5ce64', 'dfb5ce64', 'e0b5ce64', 'e1b5ce64', 'e2b5ce64', 'e3b5ce64', 'e4b5ce64', 'e5b5ce64', 'e6b5ce64', 'e7b5ce64', 'e8b5ce64', 'e9b5ce64', 'eab5ce64', 'ebb5ce64', 'ecb5ce64', 'edb5ce64', 'eeb5ce64', 'efb5ce64', 'f0b5ce64', 'f1b5ce64', 'f2b5ce64', 'f3b5ce64', 'f4b5ce64', 'f5b5ce64', 'f6b5ce64', 'f7b5ce64', 'f8b5ce64', 'f9b5ce64', 'fab5ce64', 'fbb5ce64', 'fcb5ce64', 'fdb5ce64', 'feb5ce64', 'ffb5ce64', '80b6ce64', '81b6ce64', '82b6ce64', '83b6ce64', '84b6ce64', '85b6ce64', '86b6ce64', '87b6ce64', '88b6ce64', '89b6ce64', '8ab6ce64', '8bb6ce64', '8cb6ce64', '8db6ce64', '8eb6ce64', '8fb6ce64', '90b6ce64', '91b6ce64', '92b6ce64', '93b6ce64', '94b6ce64', '95b6ce64', '96b6ce64', '97b6ce64', '98b6ce64', '99b6ce64', '9ab6ce64', '9bb6ce64', '9cb6ce64', '9db6ce64', '9eb6ce64', '9fb6ce64', 'a0b6ce64', 'a1b6ce64', 'a2b6ce64', 'a3b6ce64', 'a4b6ce64', 'a5b6ce64', 'a6b6ce64', 'a7b6ce64', 'a8b6ce64', 'a9b6ce64', 'aab6ce64', 'abb6ce64', 'acb6ce64', 'adb6ce64', 'aeb6ce64', 'afb6ce64', 'b0b6ce64', 'b1b6ce64', 'b2b6ce64', 'b3b6ce64', 'b4b6ce64', 'b5b6ce64', 'b6b6ce64', 'b7b6ce64', 'b8b6ce64', 'b9b6ce64', 'bab6ce64', 'bbb6ce64', 'bcb6ce64', 'bdb6ce64', 'beb6ce64', 'bfb6ce64', 'c0b6ce64', 'c1b6ce64', 'c2b6ce64', 'c3b6ce64', 'c4b6ce64', 'c5b6ce64', 'c6b6ce64', 'c7b6ce64', 'c8b6ce64', 'c9b6ce64', 'cab6ce64', 'cbb6ce64', 'ccb6ce64', 'cdb6ce64', 'ceb6ce64', 'cfb6ce64', 'd0b6ce64', 'd1b6ce64', 'd2b6ce64', 'd3b6ce64', 'd4b6ce64', 'd5b6ce64', 'd6b6ce64', 'd7b6ce64', 'd8b6ce64', 'd9b6ce64', 'dab6ce64', 'dbb6ce64', 'dcb6ce64', 'ddb6ce64', 'deb6ce64', 'dfb6ce64', 'e0b6ce64', 'e1b6ce64', 'e2b6ce64', 'e3b6ce64', 'e4b6ce64', 'e5b6ce64', 'e6b6ce64', 'e7b6ce64', 'e8b6ce64', 'e9b6ce64', 'eab6ce64', 'ebb6ce64', 'ecb6ce64', 'edb6ce64', 'eeb6ce64', 'efb6ce64', 'f0b6ce64', 'f1b6ce64', 'f2b6ce64', 'f3b6ce64', 'f4b6ce64', 'f5b6ce64', 'f6b6ce64', 'f7b6ce64', 'f8b6ce64', 'f9b6ce64', 'fab6ce64', 'fbb6ce64', 'fcb6ce64', 'fdb6ce64', 'feb6ce64', 'ffb6ce64', '80b7ce64', '81b7ce64', '82b7ce64', '83b7ce64', '84b7ce64', '85b7ce64', '86b7ce64', '87b7ce64', '88b7ce64', '89b7ce64', '8ab7ce64', '8bb7ce64', '8cb7ce64', '8db7ce64', '8eb7ce64', '8fb7ce64', '90b7ce64', '91b7ce64', '92b7ce64', '93b7ce64', '94b7ce64', '95b7ce64', '96b7ce64', '97b7ce64', '98b7ce64', '99b7ce64', '9ab7ce64', '9bb7ce64', '9cb7ce64', '9db7ce64', '9eb7ce64', '9fb7ce64', 'a0b7ce64', 'a1b7ce64', 'a2b7ce64', 'a3b7ce64', 'a4b7ce64', 'a5b7ce64', 'a6b7ce64', 'a7b7ce64', 'a8b7ce64', 'a9b7ce64', 'aab7ce64', 'abb7ce64', 'acb7ce64', 'adb7ce64', 'aeb7ce64', 'afb7ce64', 'b0b7ce64', 'b1b7ce64', 'b2b7ce64', 'b3b7ce64', 'b4b7ce64', 'b5b7ce64', 'b6b7ce64', 'b7b7ce64', 'b8b7ce64', 'b9b7ce64', 'bab7ce64', 'bbb7ce64', 'bcb7ce64', 'bdb7ce64', 'beb7ce64', 'bfb7ce64', 'c0b7ce64', 'c1b7ce64', 'c2b7ce64', 'c3b7ce64', 'c4b7ce64', 'c5b7ce64', 'c6b7ce64', 'c7b7ce64', 'c8b7ce64', 'c9b7ce64', 'cab7ce64', 'cbb7ce64', 'ccb7ce64', 'cdb7ce64', 'ceb7ce64', 'cfb7ce64', 'd0b7ce64', 'd1b7ce64', 'd2b7ce64', 'd3b7ce64', 'd4b7ce64', 'd5b7ce64', 'd6b7ce64', 'd7b7ce64', 'd8b7ce64', 'd9b7ce64', 'dab7ce64', 'dbb7ce64', 'dcb7ce64', 'ddb7ce64', 'deb7ce64', 'dfb7ce64', 'e0b7ce64', 'e1b7ce64', 'e2b7ce64', 'e3b7ce64', 'e4b7ce64', 'e5b7ce64', 'e6b7ce64', 'e7b7ce64', 'e8b7ce64', 'e9b7ce64', 'eab7ce64', 'ebb7ce64', 'ecb7ce64', 'edb7ce64', 'eeb7ce64', 'efb7ce64', 'f0b7ce64', 'f1b7ce64', 'f2b7ce64', 'f3b7ce64', 'f4b7ce64', 'f5b7ce64', 'f6b7ce64', 'f7b7ce64', 'f8b7ce64', 'f9b7ce64', 'fab7ce64', 'fbb7ce64', 'fcb7ce64', 'fdb7ce64', 'feb7ce64', 'ffb7ce64', '80b8ce64', '81b8ce64', '82b8ce64', '83b8ce64', '84b8ce64', '85b8ce64', '86b8ce64', '87b8ce64', '88b8ce64', '89b8ce64', '8ab8ce64', '8bb8ce64', '8cb8ce64', '8db8ce64', '8eb8ce64', '8fb8ce64', '90b8ce64', '91b8ce64', '92b8ce64', '93b8ce64', '94b8ce64', '95b8ce64', '96b8ce64', '97b8ce64', '98b8ce64', '99b8ce64', '9ab8ce64', '9bb8ce64', '9cb8ce64', '9db8ce64', '9eb8ce64', '9fb8ce64', 'a0b8ce64', 'a1b8ce64', 'a2b8ce64', 'a3b8ce64', 'a4b8ce64', 'a5b8ce64', 'a6b8ce64', 'a7b8ce64', 'a8b8ce64', 'a9b8ce64', 'aab8ce64', 'abb8ce64', 'acb8ce64', 'adb8ce64', 'aeb8ce64', 'afb8ce64', 'b0b8ce64', 'b1b8ce64', 'b2b8ce64', 'b3b8ce64', 'b4b8ce64', 'b5b8ce64', 'b6b8ce64', 'b7b8ce64', 'b8b8ce64', 'b9b8ce64', 'bab8ce64', 'bbb8ce64', 'bcb8ce64', 'bdb8ce64', 'beb8ce64', 'bfb8ce64', 'c0b8ce64', 'c1b8ce64', 'c2b8ce64', 'c3b8ce64', 'c4b8ce64', 'c5b8ce64', 'c6b8ce64', 'c7b8ce64', 'c8b8ce64', 'c9b8ce64', 'cab8ce64', 'cbb8ce64', 'ccb8ce64', 'cdb8ce64', 'ceb8ce64', 'cfb8ce64', 'd0b8ce64', 'd1b8ce64', 'd2b8ce64', 'd3b8ce64', 'd4b8ce64', 'd5b8ce64', 'd6b8ce64', 'd7b8ce64', 'd8b8ce64', 'd9b8ce64', 'dab8ce64', 'dbb8ce64', 'dcb8ce64', 'ddb8ce64', 'deb8ce64', 'dfb8ce64', 'e0b8ce64', 'e1b8ce64', 'e2b8ce64', 'e3b8ce64', 'e4b8ce64', 'e5b8ce64', 'e6b8ce64', 'e7b8ce64', 'e8b8ce64', 'e9b8ce64', 'eab8ce64', 'ebb8ce64', 'ecb8ce64', 'edb8ce64', 'eeb8ce64', 'efb8ce64', 'f0b8ce64', 'f1b8ce64', 'f2b8ce64', 'f3b8ce64', 'f4b8ce64', 'f5b8ce64', 'f6b8ce64', 'f7b8ce64', 'f8b8ce64', 'f9b8ce64', 'fab8ce64', 'fbb8ce64', 'fcb8ce64', 'fdb8ce64', 'feb8ce64', 'ffb8ce64', '80b9ce64', '81b9ce64', '82b9ce64', '83b9ce64', '84b9ce64', '85b9ce64', '86b9ce64', '87b9ce64', '88b9ce64', '89b9ce64', '8ab9ce64', '8bb9ce64', '8cb9ce64', '8db9ce64', '8eb9ce64', '8fb9ce64', '90b9ce64', '91b9ce64', '92b9ce64', '93b9ce64', '94b9ce64', '95b9ce64', '96b9ce64', '97b9ce64', '98b9ce64', '99b9ce64', '9ab9ce64', '9bb9ce64', '9cb9ce64', '9db9ce64', '9eb9ce64', '9fb9ce64', 'a0b9ce64', 'a1b9ce64', 'a2b9ce64', 'a3b9ce64', 'a4b9ce64', 'a5b9ce64', 'a6b9ce64', 'a7b9ce64', 'a8b9ce64', 'a9b9ce64', 'aab9ce64', 'abb9ce64', 'acb9ce64', 'adb9ce64', 'aeb9ce64', 'afb9ce64', 'b0b9ce64', 'b1b9ce64', 'b2b9ce64', 'b3b9ce64', 'b4b9ce64', 'b5b9ce64', 'b6b9ce64', 'b7b9ce64', 'b8b9ce64', 'b9b9ce64', 'bab9ce64', 'bbb9ce64', 'bcb9ce64', 'bdb9ce64', 'beb9ce64', 'bfb9ce64', 'c0b9ce64', 'c1b9ce64', 'c2b9ce64', 'c3b9ce64', 'c4b9ce64', 'c5b9ce64', 'c6b9ce64', 'c7b9ce64', 'c8b9ce64', 'c9b9ce64', 'cab9ce64', 'cbb9ce64', 'ccb9ce64', 'cdb9ce64', 'ceb9ce64', 'cfb9ce64', 'd0b9ce64', 'd1b9ce64', 'd2b9ce64', 'd3b9ce64', 'd4b9ce64', 'd5b9ce64', 'd6b9ce64', 'd7b9ce64', 'd8b9ce64', 'd9b9ce64', 'dab9ce64', 'dbb9ce64', 'dcb9ce64', 'ddb9ce64', 'deb9ce64', 'dfb9ce64', 'e0b9ce64', 'e1b9ce64', 'e2b9ce64', 'e3b9ce64', 'e4b9ce64', 'e5b9ce64', 'e6b9ce64', 'e7b9ce64', 'e8b9ce64', 'e9b9ce64', 'eab9ce64', 'ebb9ce64', 'ecb9ce64', 'edb9ce64', 'eeb9ce64', 'efb9ce64', 'f0b9ce64', 'f1b9ce64', 'f2b9ce64', 'f3b9ce64', 'f4b9ce64', 'f5b9ce64', 'f6b9ce64', 'f7b9ce64', 'f8b9ce64', 'f9b9ce64', 'fab9ce64', 'fbb9ce64', 'fcb9ce64', 'fdb9ce64', 'feb9ce64', 'ffb9ce64', '80bace64', '81bace64', '82bace64', '83bace64', '84bace64', '85bace64', '86bace64', '87bace64', '88bace64', '89bace64', '8abace64', '8bbace64', '8cbace64', '8dbace64', '8ebace64', '8fbace64', '90bace64', '91bace64', '92bace64', '93bace64', '94bace64', '95bace64', '96bace64', '97bace64', '98bace64', '99bace64', '9abace64', '9bbace64', '9cbace64', '9dbace64', '9ebace64', '9fbace64', 'a0bace64', 'a1bace64', 'a2bace64', 'a3bace64', 'a4bace64', 'a5bace64', 'a6bace64', 'a7bace64', 'a8bace64', 'a9bace64', 'aabace64', 'abbace64', 'acbace64', 'adbace64', 'aebace64', 'afbace64', 'b0bace64', 'b1bace64', 'b2bace64', 'b3bace64', 'b4bace64', 'b5bace64', 'b6bace64', 'b7bace64', 'b8bace64', 'b9bace64', 'babace64', 'bbbace64', 'bcbace64', 'bdbace64']  # أضف الباقي
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy4: {e}")

                if b"@proxy5" in data and not self.RbGx:
                    try:
                        items_ids = [ 'bebace64', 'bfbace64', 'c0bace64', 'c1bace64', 'c2bace64', 'c3bace64', 'c4bace64', 'c5bace64', 'c6bace64', 'c7bace64', 'c8bace64', 'c9bace64', 'cabace64', 'cbbace64', 'ccbace64', 'cdbace64', 'cebace64', 'cfbace64', 'd0bace64', 'd1bace64', 'd2bace64', 'd3bace64', 'd4bace64', 'd5bace64', 'd6bace64', 'd7bace64', 'd8bace64', 'd9bace64', 'dabace64', 'dbbace64', 'dcbace64', 'ddbace64', 'debace64', 'dfbace64', 'e0bace64', 'e1bace64', 'e2bace64', 'e3bace64', 'e4bace64', 'e5bace64', 'e6bace64', 'e7bace64', 'e8bace64', 'e9bace64', 'eabace64', 'ebbace64', 'ecbace64', 'edbace64', 'eebace64', 'efbace64', 'f0bace64', 'f1bace64', 'f2bace64', 'f3bace64', 'f4bace64', 'f5bace64', 'f6bace64', 'f7bace64', 'f8bace64', 'f9bace64', 'fabace64', 'fbbace64', 'fcbace64', 'fdbace64', 'febace64', 'ffbace64', '80bbce64', '81bbce64', '82bbce64', '83bbce64', '84bbce64', '85bbce64', '86bbce64', '87bbce64', '88bbce64', '89bbce64', '8abbce64', '8bbbce64', '8cbbce64', '8dbbce64', '8ebbce64', '8fbbce64', '90bbce64', '91bbce64', '92bbce64', '93bbce64', '94bbce64', '95bbce64', '96bbce64', '97bbce64', '98bbce64', '99bbce64', '9abbce64', '9bbbce64', '9cbbce64', '9dbbce64', '9ebbce64', '9fbbce64', 'a0bbce64', 'a1bbce64', 'a2bbce64', 'a3bbce64', 'a4bbce64', 'a5bbce64', 'a6bbce64', 'a7bbce64', 'a8bbce64', 'a9bbce64', 'aabbce64', 'abbbce64', 'acbbce64', 'adbbce64', 'aebbce64', 'afbbce64', 'b0bbce64', 'b1bbce64', 'b2bbce64', 'b3bbce64', 'b4bbce64', 'b5bbce64', 'b6bbce64', 'b7bbce64', 'b8bbce64', 'b9bbce64', 'babbce64', 'bbbbce64', 'bcbbce64', 'bdbbce64', 'bebbce64', 'bfbbce64', 'c0bbce64', 'c1bbce64', 'c2bbce64', 'c3bbce64', 'c4bbce64', 'c5bbce64', 'c6bbce64', 'c7bbce64', 'c8bbce64', 'c9bbce64', 'cabbce64', 'cbbbce64', 'ccbbce64', 'cdbbce64', 'cebbce64', 'cfbbce64', 'd0bbce64', 'd1bbce64', 'd2bbce64', 'd3bbce64', 'd4bbce64', 'd5bbce64', 'd6bbce64', 'd7bbce64', 'd8bbce64', 'd9bbce64', 'dabbce64', 'dbbbce64', 'dcbbce64', 'ddbbce64', 'debbce64', 'dfbbce64', 'e0bbce64', 'e1bbce64', 'e2bbce64', 'e3bbce64', 'e4bbce64', 'e5bbce64', 'e6bbce64', 'e7bbce64', 'e8bbce64', 'e9bbce64', 'eabbce64', 'ebbbce64', 'ecbbce64', 'edbbce64', 'eebbce64', 'efbbce64', 'f0bbce64', 'f1bbce64', 'f2bbce64', 'f3bbce64', 'f4bbce64', 'f5bbce64', 'f6bbce64', 'f7bbce64', 'f8bbce64', 'f9bbce64', 'fabbce64', 'fbbbce64', 'fcbbce64', 'fdbbce64', 'febbce64', 'ffbbce64', '80bcce64', '81bcce64', '82bcce64', '83bcce64', '84bcce64', '85bcce64', '86bcce64', '87bcce64', '88bcce64', '89bcce64', '8abcce64', '8bbcce64', '8cbcce64', '8dbcce64', '8ebcce64', '8fbcce64', '90bcce64', '91bcce64', '92bcce64', '93bcce64', '94bcce64', '95bcce64', '96bcce64', '97bcce64', '98bcce64', '99bcce64', '9abcce64', '9bbcce64', '9cbcce64', '9dbcce64', '9ebcce64', '9fbcce64', 'a0bcce64', 'a1bcce64', 'a2bcce64', 'a3bcce64', 'a4bcce64', 'a5bcce64', 'a6bcce64', 'a7bcce64', 'a8bcce64', 'a9bcce64', 'aabcce64', 'abbcce64', 'acbcce64', 'adbcce64', 'aebcce64', 'afbcce64', 'b0bcce64', 'b1bcce64', 'b2bcce64', 'b3bcce64', 'b4bcce64', 'b5bcce64', 'b6bcce64', 'b7bcce64', 'b8bcce64', 'b9bcce64', 'babcce64', 'bbbcce64', 'bcbcce64', 'bdbcce64', 'bebcce64', 'bfbcce64', 'c0bcce64', 'c1bcce64', 'c2bcce64', 'c3bcce64', 'c4bcce64', 'c5bcce64', 'c6bcce64', 'c7bcce64', 'c8bcce64', 'c9bcce64', 'cabcce64', 'cbbcce64', 'ccbcce64', 'cdbcce64', 'cebcce64', 'cfbcce64', 'd0bcce64', 'd1bcce64', 'd2bcce64', 'd3bcce64', 'd4bcce64', 'd5bcce64', 'd6bcce64', 'd7bcce64', 'd8bcce64', 'd9bcce64', 'dabcce64', 'dbbcce64', 'dcbcce64', 'ddbcce64', 'debcce64', 'dfbcce64', 'e0bcce64', 'e1bcce64', 'e2bcce64', 'e3bcce64', 'e4bcce64', 'e5bcce64', 'e6bcce64', 'e7bcce64', 'e8bcce64', 'e9bcce64', 'eabcce64', 'ebbcce64', 'ecbcce64', 'edbcce64', 'eebcce64', 'efbcce64', 'f0bcce64', 'f1bcce64', 'f2bcce64', 'f3bcce64', 'f4bcce64', 'f5bcce64', 'f6bcce64', 'f7bcce64', 'f8bcce64', 'f9bcce64', 'fabcce64', 'fbbcce64', 'fcbcce64', 'fdbcce64', 'febcce64', 'ffbcce64', '80bdce64', '81bdce64', '82bdce64', '83bdce64', '84bdce64', '85bdce64', '86bdce64', '87bdce64', '88bdce64', '89bdce64', '8abdce64', '8bbdce64', '8cbdce64', '8dbdce64', '8ebdce64', '8fbdce64', '90bdce64', '91bdce64', '92bdce64', '93bdce64', '94bdce64', '95bdce64', '96bdce64', '97bdce64', '98bdce64', '99bdce64', '9abdce64', '9bbdce64', '9cbdce64', '9dbdce64', '9ebdce64', '9fbdce64', 'a0bdce64', 'a1bdce64', 'a2bdce64', 'a3bdce64', 'a4bdce64', 'a5bdce64', 'a6bdce64', 'a7bdce64', 'a8bdce64', 'a9bdce64', 'aabdce64', 'abbdce64', 'acbdce64', 'adbdce64', 'aebdce64', 'afbdce64', 'b0bdce64', 'b1bdce64', 'b2bdce64', 'b3bdce64', 'b4bdce64', 'b5bdce64', 'b6bdce64', 'b7bdce64', 'b8bdce64', 'b9bdce64', 'babdce64', 'bbbdce64', 'bcbdce64', 'bdbdce64', 'bebdce64', 'bfbdce64', 'c0bdce64', 'c1bdce64', 'c2bdce64', 'c3bdce64', 'c4bdce64', 'c5bdce64', 'c6bdce64', 'c7bdce64', 'c8bdce64', 'c9bdce64', 'cabdce64', 'cbbdce64', 'ccbdce64', 'cdbdce64', 'cebdce64', 'cfbdce64', 'd0bdce64', 'd1bdce64', 'd2bdce64', 'd3bdce64', 'd4bdce64', 'd5bdce64', 'd6bdce64', 'd7bdce64', 'd8bdce64', 'd9bdce64', 'dabdce64', 'dbbdce64', 'dcbdce64', 'ddbdce64', 'debdce64', 'dfbdce64', 'e0bdce64', 'e1bdce64', 'e2bdce64', 'e3bdce64', 'e4bdce64', 'e5bdce64', 'e6bdce64', 'e7bdce64', 'e8bdce64', 'e9bdce64', 'eabdce64', 'ebbdce64', 'ecbdce64', 'edbdce64', 'eebdce64', 'efbdce64', 'f0bdce64', 'f1bdce64', 'f2bdce64', 'f3bdce64', 'f4bdce64', 'f5bdce64', 'f6bdce64', 'f7bdce64', 'f8bdce64', 'f9bdce64', 'fabdce64', 'fbbdce64', 'fcbdce64', 'fdbdce64', 'febdce64', 'ffbdce64', '80bece64', '81bece64', '82bece64', '83bece64', '84bece64', '85bece64', '86bece64', '87bece64', '88bece64', '89bece64', '8abece64', '8bbece64', '8cbece64', '8dbece64', '8ebece64', '8fbece64', '90bece64', '91bece64', '92bece64', '93bece64', '94bece64', '95bece64', '96bece64', '97bece64', '98bece64', '99bece64', '9abece64', '9bbece64', '9cbece64', '9dbece64', '9ebece64', '9fbece64', 'a0bece64', 'a1bece64', 'a2bece64', 'a3bece64', 'a4bece64', 'a5bece64', 'a6bece64', 'a7bece64', 'a8bece64', 'a9bece64', 'aabece64', 'abbece64', 'acbece64', 'adbece64', 'aebece64', 'afbece64', 'b0bece64', 'b1bece64', 'b2bece64', 'b3bece64', 'b4bece64', 'b5bece64', 'b6bece64', 'b7bece64', 'b8bece64', 'b9bece64', 'babece64', 'bbbece64', 'bcbece64', 'bdbece64', 'bebece64', 'bfbece64', 'c0bece64', 'c1bece64', 'c2bece64', 'c3bece64', 'c4bece64', 'c5bece64', 'c6bece64', 'c7bece64', 'c8bece64', 'c9bece64', 'cabece64', 'cbbece64', 'ccbece64', 'cdbece64', 'cebece64', 'cfbece64', 'd0bece64', 'd1bece64', 'd2bece64', 'd3bece64', 'd4bece64', 'd5bece64', 'd6bece64', 'd7bece64', 'd8bece64', 'd9bece64', 'dabece64', 'dbbece64', 'dcbece64', 'ddbece64', 'debece64', 'dfbece64', 'e0bece64', 'e1bece64', 'e2bece64', 'e3bece64', 'e4bece64', 'e5bece64', 'e6bece64', 'e7bece64', 'e8bece64', 'e9bece64', 'eabece64', 'ebbece64', 'ecbece64', 'edbece64', 'eebece64', 'efbece64', 'f0bece64', 'f1bece64', 'f2bece64', 'f3bece64', 'f4bece64', 'f5bece64', 'f6bece64', 'f7bece64', 'f8bece64', 'f9bece64', 'fabece64', 'fbbece64', 'fcbece64', 'fdbece64', 'febece64', 'ffbece64', '80bfce64', '81bfce64', '82bfce64', '83bfce64', '84bfce64', '85bfce64', '86bfce64', '87bfce64', '88bfce64', '89bfce64', '8abfce64', '8bbfce64', '8cbfce64', '8dbfce64', '8ebfce64', '8fbfce64', '90bfce64', '91bfce64', '92bfce64', '93bfce64', '94bfce64', '95bfce64', '96bfce64', '97bfce64', '98bfce64', '99bfce64', '9abfce64', '9bbfce64', '9cbfce64', '9dbfce64', '9ebfce64', '9fbfce64', 'a0bfce64', 'a1bfce64', 'a2bfce64', 'a3bfce64', 'a4bfce64', 'a5bfce64', 'a6bfce64', 'a7bfce64', 'a8bfce64', 'a9bfce64', 'aabfce64', 'abbfce64', 'acbfce64', 'adbfce64', 'aebfce64', 'afbfce64', 'b0bfce64', 'b1bfce64', 'b2bfce64', 'b3bfce64', 'b4bfce64', 'b5bfce64', 'b6bfce64', 'b7bfce64', 'b8bfce64', 'b9bfce64', 'babfce64', 'bbbfce64', 'bcbfce64', 'bdbfce64', 'bebfce64', 'bfbfce64', 'c0bfce64', 'c1bfce64', 'c2bfce64', 'c3bfce64', 'c4bfce64', 'c5bfce64', 'c6bfce64', 'c7bfce64', 'c8bfce64', 'c9bfce64', 'cabfce64', 'cbbfce64', 'ccbfce64', 'cdbfce64', 'cebfce64', 'cfbfce64', 'd0bfce64', 'd1bfce64', 'd2bfce64', 'd3bfce64', 'd4bfce64', 'd5bfce64', 'd6bfce64', 'd7bfce64', 'd8bfce64', 'd9bfce64', 'dabfce64', 'dbbfce64', 'dcbfce64', 'ddbfce64', 'debfce64', 'dfbfce64', 'e0bfce64', 'e1bfce64', 'e2bfce64', 'e3bfce64', 'e4bfce64', 'e5bfce64', 'e6bfce64', 'e7bfce64', 'e8bfce64', 'e9bfce64', 'eabfce64', 'ebbfce64', 'ecbfce64', 'edbfce64', 'eebfce64', 'efbfce64', 'f0bfce64', 'f1bfce64', 'f2bfce64', 'f3bfce64', 'f4bfce64', 'f5bfce64', 'f6bfce64', 'f7bfce64', 'f8bfce64', 'f9bfce64', 'fabfce64', 'fbbfce64']
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy5: {e}")

                if b"@proxy6" in data and not self.RbGx:
                    try:
                        items_ids = ['8196a361', '8296a361', '8396a361', '8496a361', '8596a361', '8696a361', '8796a361', '8896a361', '8996a361', '8a96a361', '8b96a361', '8c96a361', '8d96a361', '8e96a361', '8f96a361', '9096a361', '9196a361', '9296a361', '9396a361', '9496a361', '9596a361', '9696a361', '9796a361', '9896a361', '9996a361', '9a96a361', '9b96a361', '9c96a361', '9d96a361', '9e96a361', '9f96a361', 'a096a361', 'a196a361', 'a296a361', 'a396a361', 'a496a361', 'a596a361', 'a696a361', 'a796a361', 'a896a361', 'a996a361', 'aa96a361', 'ab96a361', 'ac96a361', 'ad96a361', 'ae96a361', 'af96a361', 'b096a361', 'b196a361', 'b296a361', 'b396a361', 'b496a361', 'b596a361', 'b696a361', 'b796a361', 'b896a361', 'b996a361', 'ba96a361', 'bb96a361', 'bc96a361', 'bd96a361', 'be96a361', 'bf96a361', 'c096a361', 'c196a361', 'c296a361', 'c396a361', 'c496a361', 'c596a361', 'c696a361', 'c796a361', 'c896a361', 'c996a361', 'ca96a361', 'cb96a361', 'cc96a361', 'cd96a361', 'ce96a361', 'cf96a361', 'd096a361', 'd196a361', 'd296a361', 'd396a361', 'd496a361', 'd596a361', 'd696a361', 'd796a361', 'd896a361', 'd996a361', 'da96a361', 'db96a361', 'dc96a361', 'dd96a361', 'de96a361', 'df96a361', 'e096a361', 'e196a361', 'e296a361', 'e396a361', 'e496a361', 'e596a361', 'e696a361', 'e796a361', 'e896a361', 'e996a361', 'ea96a361', 'eb96a361', 'ec96a361', 'ed96a361', 'ee96a361', 'ef96a361', 'f096a361', 'f196a361', 'f296a361', 'f396a361', 'f496a361', 'f596a361', 'f696a361', 'f796a361', 'f896a361', 'f996a361', 'fa96a361', 'fb96a361', 'fc96a361', 'fd96a361', 'fe96a361', 'ff96a361', '8097a361', '8197a361', '8297a361', '8397a361', '8497a361', '8597a361', '8697a361', '8797a361', '8897a361', '8997a361', '8a97a361', '8b97a361', '8c97a361', '8d97a361', '8e97a361', '8f97a361', '9097a361', '9197a361', '9297a361', '9397a361', '9497a361', '9597a361', '9697a361', '9797a361', '9897a361', '9997a361', '9a97a361', '9b97a361', '9c97a361', '9d97a361', '9e97a361', '9f97a361', 'a097a361', 'a197a361', 'a297a361', 'a397a361', 'a497a361', 'a597a361', 'a697a361', 'a797a361', 'a897a361', 'a997a361', 'aa97a361', 'ab97a361', 'ac97a361', 'ad97a361', 'ae97a361', 'af97a361', 'b097a361', 'b197a361', 'b297a361', 'b397a361', 'b497a361', 'b597a361', 'b697a361', 'b797a361', 'b897a361', 'b997a361', 'ba97a361', 'bb97a361', 'bc97a361', 'bd97a361', 'be97a361', 'bf97a361', 'c097a361', 'c197a361', 'c297a361', 'c397a361', 'c497a361', 'c597a361', 'c697a361', 'c797a361', 'c897a361', 'c997a361', 'ca97a361', 'cb97a361', 'cc97a361', 'cd97a361', 'ce97a361', 'cf97a361', 'd097a361', 'd197a361', 'd297a361', 'd397a361', 'd497a361', 'd597a361', 'd697a361', 'd797a361', 'd897a361', 'd997a361', 'da97a361', 'db97a361', 'dc97a361', 'dd97a361', 'de97a361', 'df97a361', 'e097a361', 'e197a361', 'e297a361', 'e397a361', 'e497a361', 'e597a361', 'e697a361', 'e797a361', 'e897a361', 'e997a361', 'ea97a361', 'eb97a361', 'ec97a361', 'ed97a361', 'ee97a361', 'ef97a361', 'f097a361', 'f197a361', 'f297a361', 'f397a361', 'f497a361', 'f597a361', 'f697a361', 'f797a361', 'f897a361', 'f997a361', 'fa97a361', 'fb97a361', 'fc97a361', 'fd97a361', 'fe97a361', 'ff97a361', '8098a361', '8198a361', '8298a361', '8398a361', '8498a361', '8598a361', '8698a361', '8798a361', '8898a361', '8998a361', '8a98a361', '8b98a361', '8c98a361', '8d98a361', '8e98a361', '8f98a361', '9098a361', '9198a361', '9298a361', '9398a361', '9498a361', '9598a361', '9698a361', '9798a361', '9898a361', '9998a361', '9a98a361', '9b98a361', '9c98a361', '9d98a361', '9e98a361', '9f98a361', 'a098a361', 'a198a361', 'a298a361', 'a398a361', 'a498a361', 'a598a361', 'a698a361', 'a798a361', 'a898a361', 'a998a361', 'aa98a361', 'ab98a361', 'ac98a361', 'ad98a361', 'ae98a361', 'af98a361', 'b098a361', 'b198a361', 'b298a361', 'b398a361', 'b498a361', 'b598a361', 'b698a361', 'b798a361', 'b898a361', 'b998a361', 'ba98a361', 'bb98a361', 'bc98a361', 'bd98a361', 'be98a361', 'bf98a361', 'c098a361', 'c198a361', 'c298a361', 'c398a361', 'c498a361', 'c598a361', 'c698a361', 'c798a361', 'c898a361', 'c998a361', 'ca98a361', 'cb98a361', 'cc98a361', 'cd98a361', 'ce98a361', 'cf98a361', 'd098a361', 'd198a361', 'd298a361', 'd398a361', 'd498a361', 'd598a361', 'd698a361', 'd798a361', 'd898a361', 'd998a361', 'da98a361', 'db98a361', 'dc98a361', 'dd98a361', 'de98a361', 'df98a361', 'e098a361', 'e198a361', 'e298a361', 'e398a361', 'e498a361', 'e598a361', 'e698a361', 'e798a361', 'e898a361', 'e998a361', 'ea98a361', 'eb98a361', 'ec98a361', 'ed98a361', 'ee98a361', 'ef98a361', 'f098a361', 'f198a361', 'f298a361', 'f398a361', 'f498a361', 'f598a361', 'f698a361', 'f798a361', 'f898a361', 'f998a361', 'fa98a361', 'fb98a361', 'fc98a361', 'fd98a361', 'fe98a361', 'ff98a361', '8099a361', '8199a361', '8299a361', '8399a361', '8499a361', '8599a361', '8699a361', '8799a361', '8899a361', '8999a361', '8a99a361', '8b99a361', '8c99a361', '8d99a361', '8e99a361', '8f99a361', '9099a361', '9199a361', '9299a361', '9399a361', '9499a361', '9599a361', '9699a361', '9799a361', '9899a361', '9999a361', '9a99a361', '9b99a361', '9c99a361', '9d99a361', '9e99a361', '9f99a361', 'a099a361', 'a199a361', 'a299a361', 'a399a361', 'a499a361', 'a599a361', 'a699a361', 'a799a361', 'a899a361', 'a999a361', 'aa99a361', 'ab99a361', 'ac99a361', 'ad99a361', 'ae99a361', 'af99a361', 'b099a361', 'b199a361', 'b299a361', 'b399a361', 'b499a361', 'b599a361', 'b699a361', 'b799a361', 'b899a361', 'b999a361', 'ba99a361', 'bb99a361', 'bc99a361', 'bd99a361', 'be99a361', 'bf99a361', 'c099a361', 'c199a361', 'c299a361', 'c399a361', 'c499a361', 'c599a361', 'c699a361', 'c799a361', 'c899a361', 'c999a361', 'ca99a361', 'cb99a361', 'cc99a361', 'cd99a361', 'ce99a361', 'cf99a361', 'd099a361', 'd199a361', 'd299a361', 'd399a361', 'd499a361', 'd599a361', 'd699a361', 'd799a361', 'd899a361', 'd999a361', 'da99a361', 'db99a361', 'dc99a361', 'dd99a361', 'de99a361', 'df99a361', 'e099a361', 'e199a361', 'e299a361', 'e399a361', 'e499a361', 'e599a361', 'e699a361', 'e799a361', 'e899a361', 'e999a361', 'ea99a361', 'eb99a361', 'ec99a361', 'ed99a361', 'ee99a361', 'ef99a361', 'f099a361', 'f199a361', 'f299a361', 'f399a361', 'f499a361', 'f599a361', 'f699a361', 'f799a361', 'f899a361', 'f999a361', 'fa99a361', 'fb99a361', 'fc99a361', 'fd99a361', 'fe99a361', 'ff99a361', '809aa361', '819aa361', '829aa361', '839aa361', '849aa361', '859aa361', '869aa361', '879aa361', '889aa361', '899aa361', '8a9aa361', '8b9aa361', '8c9aa361', '8d9aa361', '8e9aa361', '8f9aa361', '909aa361', '919aa361', '929aa361', '939aa361', '949aa361', '959aa361', '969aa361', '979aa361', '989aa361', '999aa361', '9a9aa361', '9b9aa361', '9c9aa361', '9d9aa361', '9e9aa361', '9f9aa361', 'a09aa361', 'a19aa361', 'a29aa361', 'a39aa361', 'a49aa361', 'a59aa361', 'a69aa361', 'a79aa361', 'a89aa361', 'a99aa361', 'aa9aa361', 'ab9aa361', 'ac9aa361', 'ad9aa361', 'ae9aa361', 'af9aa361', 'b09aa361', 'b19aa361', 'b29aa361', 'b39aa361', 'b49aa361', 'b59aa361', 'b69aa361', 'b79aa361', 'b89aa361', 'b99aa361', 'ba9aa361', 'bb9aa361', 'bc9aa361', 'bd9aa361', 'be9aa361', 'bf9aa361', 'c09aa361', 'c19aa361', 'c29aa361', 'c39aa361', 'c49aa361', 'c59aa361', 'c69aa361', 'c79aa361', 'c89aa361', 'c99aa361', 'ca9aa361', 'cb9aa361', 'cc9aa361', 'cd9aa361', 'ce9aa361', 'cf9aa361', 'd09aa361', 'd19aa361', 'd29aa361', 'd39aa361', 'd49aa361', 'd59aa361', 'd69aa361', 'd79aa361', 'd89aa361', 'd99aa361', 'da9aa361', 'db9aa361', 'dc9aa361', 'dd9aa361', 'de9aa361', 'df9aa361', 'e09aa361', 'e19aa361', 'e29aa361', 'e39aa361', 'e49aa361', 'e59aa361', 'e69aa361', 'e79aa361', 'e89aa361', 'e99aa361', 'ea9aa361', 'eb9aa361', 'ec9aa361', 'ed9aa361', 'ee9aa361', 'ef9aa361', 'f09aa361', 'f19aa361', 'f29aa361', 'f39aa361', 'f49aa361', 'f59aa361', 'f69aa361', 'f79aa361', 'f89aa361', 'f99aa361', 'fa9aa361', 'fb9aa361', 'fc9aa361', 'fd9aa361', 'fe9aa361', 'ff9aa361', '809ba361', '819ba361', '829ba361', '839ba361', '849ba361', '859ba361', '869ba361', '879ba361', '889ba361', '899ba361', '8a9ba361', '8b9ba361', '8c9ba361', '8d9ba361', '8e9ba361', '8f9ba361', '909ba361', '919ba361', '929ba361', '939ba361', '949ba361', '959ba361', '969ba361', '979ba361', '989ba361', '999ba361', '9a9ba361', '9b9ba361', '9c9ba361', '9d9ba361', '9e9ba361', '9f9ba361', 'a09ba361', 'a19ba361', 'a29ba361', 'a39ba361', 'a49ba361', 'a59ba361', 'a69ba361', 'a79ba361', 'a89ba361', 'a99ba361', 'aa9ba361', 'ab9ba361', 'ac9ba361', 'ad9ba361', 'ae9ba361', 'af9ba361', 'b09ba361', 'b19ba361', 'b29ba361', 'b39ba361', 'b49ba361', 'b59ba361', 'b69ba361', 'b79ba361', 'b89ba361', 'b99ba361', 'ba9ba361', 'bb9ba361', 'bc9ba361', 'bd9ba361', 'be9ba361', 'bf9ba361', 'c09ba361', 'c19ba361', 'c29ba361', 'c39ba361', 'c49ba361', 'c59ba361', 'c69ba361', 'c79ba361', 'c89ba361', 'c99ba361', 'ca9ba361', 'cb9ba361', 'cc9ba361', 'cd9ba361', 'ce9ba361', 'cf9ba361', 'd09ba361', 'd19ba361', 'd29ba361', 'd39ba361', 'd49ba361', 'd59ba361', 'd69ba361', 'd79ba361', 'd89ba361', 'd99ba361', 'da9ba361', 'db9ba361', 'dc9ba361', 'dd9ba361', 'de9ba361', 'df9ba361', 'e09ba361', 'e19ba361', 'e29ba361', 'e39ba361', 'e49ba361', 'e59ba361', 'e69ba361', 'e79ba361', 'e89ba361', 'e99ba361', 'ea9ba361', 'eb9ba361', 'ec9ba361', 'ed9ba361', 'ee9ba361', 'ef9ba361', 'f09ba361', 'f19ba361', 'f29ba361', 'f39ba361', 'f49ba361', 'f59ba361', 'f69ba361', 'f79ba361', 'f89ba361', 'f99ba361', 'fa9ba361', 'fb9ba361', 'fc9ba361', 'fd9ba361', 'fe9ba361', 'ff9ba361', '809ca361', '819ca361', '829ca361', '839ca361', '849ca361', '859ca361', '869ca361', '879ca361', '889ca361', '899ca361', '8a9ca361', '8b9ca361', '8c9ca361', '8d9ca361', '8e9ca361', '8f9ca361', '909ca361', '919ca361', '929ca361', '939ca361', '949ca361', '959ca361', '969ca361', '979ca361', '989ca361', '999ca361', '9a9ca361', '9b9ca361', '9c9ca361', '9d9ca361', '9e9ca361', '9f9ca361', 'a09ca361', 'a19ca361', 'a29ca361', 'a39ca361', 'a49ca361', 'a59ca361', 'a69ca361', 'a79ca361', 'a89ca361', 'a99ca361', 'aa9ca361', 'ab9ca361', 'ac9ca361', 'ad9ca361', 'ae9ca361', 'af9ca361', 'b09ca361', 'b19ca361', 'b29ca361', 'b39ca361', 'b49ca361', 'b59ca361', 'b69ca361', 'b79ca361', 'b89ca361', 'b99ca361', 'ba9ca361', 'bb9ca361', 'bc9ca361', 'bd9ca361', 'be9ca361', 'bf9ca361', 'c09ca361', 'c19ca361', 'c29ca361', 'c39ca361', 'c49ca361', 'c59ca361', 'c69ca361', 'c79ca361', 'c89ca361', 'c99ca361', 'ca9ca361', 'cb9ca361', 'cc9ca361', 'cd9ca361', 'ce9ca361', 'cf9ca361', 'd09ca361', 'd19ca361', 'd29ca361', 'd39ca361', 'd49ca361', 'd59ca361', 'd69ca361', 'd79ca361', 'd89ca361', 'd99ca361', 'da9ca361', 'db9ca361', 'dc9ca361', 'dd9ca361', 'de9ca361', 'df9ca361', 'e09ca361', 'e19ca361', 'e29ca361', 'e39ca361', 'e49ca361', 'e59ca361', 'e69ca361', 'e79ca361', 'e89ca361', 'e99ca361', 'ea9ca361', 'eb9ca361', 'ec9ca361', 'ed9ca361', 'ee9ca361', 'ef9ca361', 'f09ca361', 'f19ca361', 'f29ca361', 'f39ca361', 'f49ca361', 'f59ca361', 'f69ca361', 'f79ca361', 'f89ca361', 'f99ca361', 'fa9ca361', 'fb9ca361', 'fc9ca361', 'fd9ca361', 'fe9ca361', 'ff9ca361', '809da361', '819da361', '829da361', '839da361', '849da361', '859da361', '869da361', '879da361', '889da361', '899da361', '8a9da361', '8b9da361', '8c9da361', '8d9da361', '8e9da361', '8f9da361', '909da361', '919da361', '929da361', '939da361', '949da361', '959da361', '969da361', '979da361', '989da361', '999da361', '9a9da361', '9b9da361', '9c9da361', '9d9da361', '9e9da361', '9f9da361', 'a09da361', 'a19da361', 'a29da361', 'a39da361', 'a49da361', 'a59da361', 'a69da361', 'a79da361', 'a89da361', 'a99da361', 'aa9da361', 'ab9da361', 'ac9da361', 'ad9da361', 'ae9da361', 'af9da361', 'b09da361', 'b19da361', 'b29da361', 'b39da361', 'b49da361', 'b59da361', 'b69da361', 'b79da361', 'b89da361', 'b99da361', 'ba9da361', 'bb9da361', 'bc9da361', 'bd9da361', 'be9da361', 'bf9da361', 'c09da361', 'c19da361', 'c29da361', 'c39da361', 'c49da361', 'c59da361', 'c69da361', 'c79da361', 'c89da361', 'c99da361']  # أضف الباقي
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy6: {e}")

                if b"@proxy7" in data and not self.RbGx:
                    try:
                        items_ids = ['81c38566', '82c38566', '83c38566', '84c38566', '85c38566', '86c38566', '87c38566', '88c38566', '89c38566', '8ac38566', '8bc38566', '8cc38566', '8dc38566', '8ec38566', '8fc38566', '90c38566', '91c38566', '92c38566', '93c38566', '94c38566', '95c38566', '96c38566', '97c38566', '98c38566', '99c38566', '9ac38566', '9bc38566', '9cc38566', '9dc38566', '9ec38566', '9fc38566', 'a0c38566', 'a1c38566', 'a2c38566', 'a3c38566', 'a4c38566', 'a5c38566', 'a6c38566', 'a7c38566', 'a8c38566', 'a9c38566', 'aac38566', 'abc38566', 'acc38566', 'adc38566', 'aec38566', 'afc38566', 'b0c38566', 'b1c38566', 'b2c38566', 'b3c38566', 'b4c38566', 'b5c38566', 'b6c38566', 'b7c38566', 'b8c38566', 'b9c38566', 'bac38566', 'bbc38566', 'bcc38566', 'bdc38566', 'bec38566', 'bfc38566', 'c0c38566', 'c1c38566', 'c2c38566', 'c3c38566', 'c4c38566', 'c5c38566', 'c6c38566', 'c7c38566', 'c8c38566', 'c9c38566', 'cac38566', 'cbc38566', 'ccc38566', 'cdc38566', 'cec38566', 'cfc38566', 'd0c38566', 'd1c38566', 'd2c38566', 'd3c38566', 'd4c38566', 'd5c38566', 'd6c38566', 'd7c38566', 'd8c38566', 'd9c38566', 'dac38566', 'dbc38566', 'dcc38566', 'ddc38566', 'dec38566', 'dfc38566', 'e0c38566', 'e1c38566', 'e2c38566', 'e3c38566', 'a0dc8766', 'a1dc8766', 'a2dc8766', 'a3dc8766', 'a4dc8766', 'a5dc8766', 'a6dc8766', 'a7dc8766', 'a8dc8766', 'a9dc8766']  # أضف الباقي
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxy7: {e}")

                if b"@proxyvip" in data and not self.RbGx:
                    try:
                        items_ids = ['a796e660', 'a896e660', 'a996e660', 'aa96e660', 'ab96e660', 'ac96e660', 'ad96e660', 'ae96e660', 'af96e660', 'b096e660', 'b196e660', 'b296e660', 'b396e660', 'b496e660', 'b596e660', 'b696e660', 'b796e660', 'b896e660', 'b996e660', 'ba96e660', 'bb96e660', 'bc96e660', 'bd96e660', 'be96e660', 'bf96e660', 'c096e660', 'c196e660', 'c296e660', 'c396e660', 'c496e660', 'c596e660', 'c696e660', 'c796e660', 'c896e660', 'c996e660', 'ca96e660', 'cb96e660', 'cc96e660', 'cd96e660', 'ce96e660', 'cf96e660', 'd096e660', 'd196e660', 'd296e660', 'd396e660', 'd496e660', 'd596e660', 'd696e660', 'd796e660', 'd896e660', 'd996e660', 'da96e660', 'db96e660', 'dc96e660', 'dd96e660', 'de96e660', 'df96e660', 'e096e660', 'e196e660', 'e296e660', 'e396e660', 'e496e660', 'e596e660', 'e696e660', 'e796e660', 'e896e660', 'e996e660', 'ea96e660', 'eb96e660', 'ec96e660', 'ed96e660', 'ee96e660', 'ef96e660', 'f096e660', 'f196e660', 'f296e660', 'f396e660', 'f496e660', 'f596e660', 'f696e660', 'f796e660', 'f896e660', 'f996e660', 'fa96e660', 'fb96e660', 'fc96e660', 'fd96e660', 'fe96e660', 'ff96e660', '8097e660', '8197e660', '8297e660', '8397e660', '8497e660', '8597e660', '8697e660', '8797e660', '8897e660', '8997e660', '8a97e660', '8b97e660', '8c97e660', '8d97e660', '8e97e660', '8f97e660', '9097e660', '9197e660', '9297e660', '9397e660', '9497e660', '9597e660', '9697e660', '9797e660', '9897e660', '9997e660', '9a97e660', '9b97e660', '9c97e660', '9d97e660', '9e97e660', '9f97e660', 'a097e660', 'a197e660', 'a297e660', 'a397e660', 'a497e660', 'a597e660', 'a697e660', 'a797e660', 'a897e660', 'a997e660', 'aa97e660', 'ab97e660', 'ac97e660', 'ad97e660', 'ae97e660', 'af97e660', 'b097e660', 'b197e660', 'b297e660', 'b397e660', 'b497e660', 'b597e660', 'b697e660', 'b797e660', 'b897e660', 'b997e660', 'ba97e660', 'bb97e660', 'bc97e660', 'bd97e660', 'be97e660', 'bf97e660', 'c097e660', 'c197e660', 'c297e660', 'c397e660', 'c497e660', 'c597e660', 'c697e660', 'c797e660', 'c897e660', 'c997e660', 'ca97e660', 'cb97e660', 'cc97e660', 'cd97e660', 'ce97e660', 'cf97e660', 'd097e660', 'd197e660', 'd297e660', 'd397e660', 'd497e660', 'd597e660', 'd697e660', 'd797e660', 'd897e660', 'd997e660', 'da97e660', 'db97e660', 'dc97e660', 'dd97e660', 'de97e660', 'df97e660', 'e097e660', 'e197e660', 'e297e660', 'e397e660', 'e497e660', 'e597e660', 'e697e660', 'e797e660', 'e897e660', 'e997e660', 'ea97e660', 'eb97e660', 'ec97e660', 'ed97e660', 'ee97e660', 'ef97e660', 'f097e660', 'f197e660', 'f297e660', 'f397e660', 'f497e660', 'f597e660', 'f697e660', 'f797e660', 'f897e660', 'f997e660', 'fa97e660', 'fb97e660', 'fc97e660', 'fd97e660', 'fe97e660', 'ff97e660', '8098e660', '8198e660', '8298e660', '8398e660', '8498e660', '8598e660', '8698e660', '8798e660', '8898e660', '8998e660', '8a98e660', '8b98e660', '8c98e660', '8d98e660', '8e98e660', '8f98e660', '9098e660', '9198e660', '9298e660', '9398e660', '9498e660', '9598e660', '9698e660', '9798e660', '9898e660', '9998e660', '9a98e660', '9b98e660', '9c98e660', '9d98e660', '9e98e660', '9f98e660', 'a098e660', 'a198e660', 'a298e660', 'a398e660', 'a498e660', 'a598e660', 'a698e660', 'a798e660', 'a898e660', 'a998e660', 'aa98e660', 'ab98e660', 'ac98e660', 'ad98e660', 'ae98e660', 'af98e660', 'b098e660', 'b198e660', 'b298e660', 'b398e660', 'b498e660', 'b598e660', 'b698e660', 'b798e660', 'b898e660', 'b998e660', 'ba98e660', 'bb98e660', 'bc98e660', 'bd98e660', 'be98e660', 'bf98e660', 'c098e660', 'c198e660', 'c298e660', 'c398e660', 'c498e660', 'c598e660', 'c698e660', 'c798e660', 'c898e660', 'c998e660', 'ca98e660', 'cb98e660', 'cc98e660', 'cd98e660', 'ce98e660', 'cf98e660', 'd098e660', 'd198e660', 'd298e660', 'd398e660', 'd498e660', 'd598e660', 'd698e660', 'd798e660', 'd898e660', 'd998e660', 'da98e660', 'db98e660', 'dc98e660', 'dd98e660', 'de98e660', 'df98e660', 'e098e660', 'e198e660', 'e298e660', 'e398e660', 'e498e660', 'e598e660', 'e698e660', 'e798e660', 'e898e660', 'e998e660', 'ea98e660', 'eb98e660', 'ec98e660', 'ed98e660', 'ee98e660', 'ef98e660', 'f098e660', 'f198e660', 'f298e660', 'f398e660', 'f498e660', 'f598e660', 'f698e660', 'f798e660', 'f898e660', 'f998e660', 'fa98e660', 'fb98e660', 'fc98e660', 'fd98e660', 'fe98e660', 'ff98e660', '8099e660', '8199e660', '8299e660', '8399e660', '8499e660', '8599e660', '8699e660', '8799e660', '8899e660', '8999e660', '8a99e660', '8b99e660', '8c99e660', '8d99e660', '8e99e660', '8f99e660', '9099e660', '9199e660', '9299e660', '9399e660', '9499e660', '9599e660', '9699e660', '9799e660', '9899e660', '9999e660', '9a99e660', '9b99e660', '9c99e660', '9d99e660', '9e99e660', '9f99e660', 'a099e660', 'a199e660', 'a299e660', 'a399e660', 'a499e660', 'a599e660', 'a699e660', 'a799e660', 'a899e660', 'a999e660', 'aa99e660', 'ab99e660', 'ac99e660', 'ad99e660', 'ae99e660', 'af99e660', 'b099e660', 'b199e660', 'b299e660', 'b399e660', 'b499e660', 'b599e660', 'b699e660', 'b799e660', 'b899e660', 'b999e660', 'ba99e660', 'bb99e660', 'bc99e660', 'bd99e660', 'be99e660', 'bf99e660', 'c099e660', 'c199e660', 'c299e660', 'c399e660', 'c499e660', 'c599e660', 'c699e660', 'c799e660', 'c899e660', 'c999e660', 'ca99e660', 'cb99e660', 'cc99e660', 'cd99e660', 'ce99e660', 'cf99e660', 'd099e660', 'd199e660', 'd299e660', 'd399e660', 'd499e660', 'd599e660', 'd699e660', 'd799e660', 'd899e660', 'd999e660', 'da99e660', 'db99e660', 'dc99e660', 'dd99e660', 'de99e660', 'df99e660', 'e099e660', 'e199e660', 'e299e660', 'e399e660', 'e499e660', 'e599e660', 'e699e660', 'e799e660', 'e899e660', 'e999e660', 'ea99e660', 'eb99e660', 'ec99e660', 'ed99e660', 'ee99e660', 'ef99e660', 'f099e660', 'f199e660', 'f299e660', 'f399e660', 'f499e660', 'f599e660', 'f699e660', 'f799e660', 'f899e660', 'f999e660', 'fa99e660', 'fb99e660', 'fc99e660', 'fd99e660', 'fe99e660', 'ff99e660', '809ae660', '819ae660', '829ae660', '839ae660', '849ae660', '859ae660', '869ae660', '879ae660', '889ae660', '899ae660', '8a9ae660', '8b9ae660', '8c9ae660', '8d9ae660', '8e9ae660', '8f9ae660', '909ae660', '919ae660', '929ae660', '939ae660', '949ae660', '959ae660', '969ae660', '979ae660', '989ae660', '999ae660', '9a9ae660', '9b9ae660', '9c9ae660', '9d9ae660', '9e9ae660', '9f9ae660', 'a09ae660', 'a19ae660', 'a29ae660', 'a39ae660', 'a49ae660', 'a59ae660', 'a69ae660', 'a79ae660', 'a89ae660', 'a99ae660', 'aa9ae660', 'ab9ae660', 'ac9ae660', 'ad9ae660', 'ae9ae660', 'af9ae660', 'b09ae660', 'b19ae660', 'b29ae660', 'b39ae660', 'b49ae660', 'b59ae660', 'b69ae660', 'b79ae660', 'b89ae660', 'b99ae660', 'ba9ae660', 'bb9ae660', 'bc9ae660', 'bd9ae660', 'be9ae660', 'bf9ae660', 'c09ae660', 'c19ae660', 'c29ae660', 'c39ae660', 'c49ae660', 'c59ae660', 'c69ae660', 'c79ae660', 'c89ae660', 'c99ae660', 'ca9ae660', 'cb9ae660', 'cc9ae660', 'cd9ae660', 'ce9ae660', 'cf9ae660', 'd09ae660', 'd19ae660', 'd29ae660', 'd39ae660', 'd49ae660', 'd59ae660', 'd69ae660', 'd79ae660', 'd89ae660', 'd99ae660', 'da9ae660', 'db9ae660', 'dc9ae660', 'dd9ae660', 'de9ae660', 'df9ae660', 'e09ae660', 'e19ae660', 'e29ae660', 'e39ae660', 'e49ae660', 'e59ae660', 'e69ae660', 'e79ae660', 'e89ae660', 'e99ae660', 'ea9ae660', 'eb9ae660', 'ec9ae660', 'ed9ae660', 'ee9ae660', 'ef9ae660', 'f09ae660', 'f19ae660', 'f29ae660', 'f39ae660', 'f49ae660', 'f59ae660', 'f69ae660', 'f79ae660', 'f89ae660', 'f99ae660', 'fa9ae660', 'fb9ae660', 'fc9ae660', 'fd9ae660', 'fe9ae660', 'ff9ae660', '809be660', '819be660', '829be660', '839be660', '849be660', '859be660', '869be660', '879be660', '889be660', '899be660', '8a9be660', '8b9be660', '8c9be660', '8d9be660', '8e9be660', '8f9be660', '909be660', '919be660', '929be660', '939be660', '949be660', '959be660', '969be660', '979be660', '989be660', '999be660', '9a9be660', '9b9be660', '9c9be660', '9d9be660', '9e9be660', '9f9be660', 'a09be660', 'a19be660', 'a29be660', 'a39be660', 'a49be660', 'a59be660', 'a69be660', 'a79be660', 'a89be660', 'a99be660', 'aa9be660', 'ab9be660', 'ac9be660', 'ad9be660', 'ae9be660', 'af9be660', 'b09be660', 'b19be660', 'b29be660', 'b39be660', 'b49be660', 'b59be660', 'b69be660', 'b79be660', 'b89be660', 'b99be660', 'ba9be660', 'bb9be660', 'bc9be660', 'bd9be660', 'be9be660', 'bf9be660', 'c09be660', 'c19be660', 'c29be660', 'c39be660', 'c49be660', 'c59be660', 'c69be660', 'c79be660', 'c89be660', 'c99be660', 'ca9be660', 'cb9be660', 'cc9be660', 'cd9be660', 'ce9be660', 'cf9be660', 'd09be660', 'd19be660', 'd29be660', 'd39be660',"c19ae061", "c29ae061", "c39ae061", "c49ae061", "c59ae061", "c69ae061", "c79ae061", "c89ae061", "c99ae061", "ca9ae061", "cb9ae061", "cc9ae061", "cd9ae061", "ce9ae061", "cf9ae061",
    "d09ae061", "d19ae061", "d29ae061", "d39ae061", "d49ae061", "d59ae061", "d69ae061", "d79ae061", "d89ae061", "d99ae061", "da9ae061", "db9ae061", "dc9ae061", "dd9ae061", "de9ae061", "df9ae061",
    "e09ae061", "e19ae061", "e29ae061", "e39ae061", "e49ae061", "e59ae061", "e69ae061", "e79ae061", "e89ae061", "e99ae061", "ea9ae061", "eb9ae061", "ec9ae061", "ed9ae061", "ee9ae061", "ef9ae061",
    "f09ae061", "f19ae061", "f29ae061", "f39ae061", "f49ae061", "f59ae061", "f69ae061", "f79ae061", "f89ae061", "f99ae061", "fa9ae061", "fb9ae061", "fc9ae061", "fd9ae061", "fe9ae061", "ff9ae061",
    "809be061", "819be061", "829be061", "839be061", "849be061", "859be061", "869be061", "879be061", "889be061", "899be061", "8a9be061", "8b9be061", "8c9be061", "8d9be061", "8e9be061", "8f9be061",
    "909be061", "919be061", "929be061", "939be061", "949be061", "959be061", "969be061", "979be061", "989be061", "999be061", "9a9be061", "9b9be061", "9c9be061", "9d9be061", "9e9be061", "9f9be061",
    "a09be061", "a19be061", "a29be061", "a39be061", "a49be061", "a59be061", "a69be061", "a79be061", "a89be061", "a99be061", "aa9be061", "ab9be061", "ac9be061", "ad9be061", "ae9be061", "af9be061",
    "b09be061", "b19be061", "b29be061", "b39be061", "b49be061", "b59be061", "b69be061", "b79be061", "b89be061", "b99be061", "ba9be061", "bb9be061", "bc9be061", "bd9be061", "be9be061", "bf9be061",
    "c09be061", "c19be061", "c29be061", "c39be061", "c49be061", "c59be061", "c69be061", "c79be061", "c89be061", "c99be061", "ca9be061", "cb9be061", "cc9be061", "cd9be061", "ce9be061", "cf9be061",
    "d09be061", "d19be061", "d29be061", "d39be061", "d49be061", "d59be061", "d69be061", "d79be061", "d89be061", "d99be061", "da9be061", "db9be061", "dc9be061", "dd9be061", "de9be061", "df9be061",
    "e09be061", "e19be061", "e29be061", "e39be061", "e49be061", "e59be061", "e69be061", "e79be061", "e89be061", "e99be061", "ea9be061", "eb9be061", "ec9be061", "ed9be061", "ee9be061", "ef9be061",
    "f09be061", "f19be061", "f29be061", "f39be061", "f49be061", "f59be061", "f69be061", "f79be061", "f89be061", "f99be061", "fa9be061", "fb9be061", "fc9be061", "fd9be061", "fe9be061", "ff9be061",
    "809ce061", "819ce061", "829ce061", "839ce061", "849ce061", "859ce061", "869ce061", "879ce061", "889ce061", "899ce061", "8a9ce061", "8b9ce061", "8c9ce061", "8d9ce061", "8e9ce061", "8f9ce061",
    "909ce061", "919ce061", "929ce061", "939ce061", "949ce061", "959ce061", "969ce061", "979ce061", "989ce061", "999ce061", "9a9ce061", "9b9ce061", "9c9ce061", "9d9ce061", "9e9ce061", "9f9ce061",
    "a09ce061", "a19ce061", "a29ce061", "a39ce061", "a49ce061", "a59ce061", "a69ce061", "a79ce061", "a89ce061", "a99ce061", "aa9ce061", "ab9ce061", "ac9ce061", "ad9ce061", "ae9ce061", "af9ce061",
    "b09ce061", "b19ce061", "b29ce061", "b39ce061", "b49ce061", "b59ce061", "b69ce061", "b79ce061", "b89ce061", "b99ce061", "ba9ce061", "bb9ce061", "bc9ce061", "bd9ce061", "be9ce061", "bf9ce061",
    "c09ce061", "c19ce061", "c29ce061", "c39ce061", "c49ce061", "c59ce061", "c69ce061", "c79ce061", "c89ce061", "c99ce061", "ca9ce061", "cb9ce061", "cc9ce061", "cd9ce061", "ce9ce061", "cf9ce061",
    "d09ce061", "d19ce061", "d29ce061", "d39ce061", "d49ce061", "d59ce061", "d69ce061", "d79ce061", "d89ce061", "d99ce061", "da9ce061", "db9ce061", "dc9ce061", "dd9ce061", "de9ce061", "df9ce061",
    "e09ce061", "e19ce061", "e29ce061", "e39ce061", "e49ce061", "e59ce061", "e69ce061", "e79ce061", "e89ce061", "e99ce061", "ea9ce061", "eb9ce061", "ec9ce061", "ed9ce061", "ee9ce061", "ef9ce061",
    "f09ce061", "f19ce061", "f29ce061", "f39ce061", "f49ce061", "f59ce061", "f69ce061", "f79ce061", "f89ce061", "f99ce061", "fa9ce061", "fb9ce061", "fc9ce061", "fd9ce061", "fe9ce061", "ff9ce061",
    "809de061", "819de061", "829de061", "839de061", "849de061", "859de061", "869de061", "879de061", "889de061", "899de061", "8a9de061", "8b9de061", "8c9de061", "8d9de061", "8e9de061", "8f9de061",
    "909de061", "919de061", "929de061", "939de061", "949de061", "959de061", "969de061", "979de061", "989de061", "999de061", "9a9de061", "9b9de061", "9c9de061", "9d9de061", "9e9de061", "9f9de061",
    "a09de061", "a19de061", "a29de061", "a39de061", "a49de061", "a59de061", "a69de061", "a79de061", "a89de061", "a99de061", "aa9de061", "ab9de061", "ac9de061", "ad9de061", "ae9de061", "af9de061",
    "b09de061", "b19de061", "b29de061", "b39de061", "b49de061", "b59de061", "b69de061", "b79de061", "b89de061", "b99de061", "ba9de061", "bb9de061", "bc9de061", "bd9de061", "be9de061", "bf9de061",
    "c09de061", "c19de061", "c29de061", "c39de061", "c49de061", "c59de061", "c69de061", "c79de061", "c89de061", "c99de061", "ca9de061", "cb9de061", "cc9de061", "cd9de061", "ce9de061", "cf9de061",
    "d09de061", "d19de061", "d29de061", "d39de061", "d49de061", "d59de061", "d69de061", "d79de061", "d89de061", "d99de061", "da9de061", "db9de061", "dc9de061", "dd9de061", "de9de061", "df9de061",
    "e09de061", "e19de061", "e29de061", "e39de061", "e49de061", "e59de061", "e69de061", "e79de061", "e89de061", "e99de061", "ea9de061", "eb9de061", "ec9de061", "ed9de061", "ee9de061", "ef9de061",
    "f09de061", "f19de061", "f29de061", "f39de061", "f49de061", "f59de061", "f69de061", "f79de061", "f89de061", "f99de061", "fa9de061", "fb9de061", "fc9de061", "fd9de061", "fe9de061", "ff9de061",
    "809ee061", "819ee061", "829ee061", "839ee061", "849ee061", "859ee061", "869ee061", "879ee061", "889ee061", "899ee061", "8a9ee061", "8b9ee061", "8c9ee061", "8d9ee061", "8e9ee061", "8f9ee061",
    "909ee061", "919ee061", "929ee061", "939ee061", "949ee061", "959ee061", "969ee061", "979ee061", "989ee061", "999ee061", "9a9ee061", "9b9ee061", "9c9ee061", "9d9ee061", "9e9ee061", "9f9ee061",
    "a09ee061", "a19ee061", "a29ee061", "a39ee061", "a49ee061", "a59ee061", "a69ee061", "a79ee061", "a89ee061", "a99ee061", "aa9ee061", "ab9ee061", "ac9ee061", "ad9ee061", "ae9ee061", "af9ee061",
    "b09ee061", "b19ee061", "b29ee061", "b39ee061", "b49ee061", "b59ee061", "b69ee061", "b79ee061", "b89ee061", "b99ee061", "ba9ee061", "bb9ee061", "bc9ee061", "bd9ee061", "be9ee061", "bf9ee061",
    "c09ee061", "c19ee061", "c29ee061", "c39ee061", "c49ee061", "c59ee061", "c69ee061", "c79ee061", "c89ee061", "c99ee061", "ca9ee061", "cb9ee061", "cc9ee061", "cd9ee061", "ce9ee061", "cf9ee061",
    "d09ee061", "d19ee061", "d29ee061", "d39ee061", "d49ee061", "d59ee061", "d69ee061", "d79ee061", "d89ee061", "d99ee061", "da9ee061", "db9ee061", "dc9ee061", "dd9ee061", "de9ee061", "df9ee061",
    "e09ee061", "e19ee061", "e29ee061", "e39ee061", "e49ee061", "e59ee061", "e69ee061", "e79ee061", "e89ee061", "e99ee061", "ea9ee061", "eb9ee061", "ec9ee061", "ed9ee061", "ee9ee061", "ef9ee061",
    "f09ee061", "f19ee061", "f29ee061", "f39ee061", "f49ee061", "f59ee061", "f69ee061", "f79ee061", "f89ee061", "f99ee061", "fa9ee061", "fb9ee061", "fc9ee061", "fd9ee061", "fe9ee061", "ff9ee061",
    "809fe061", "819fe061", "829fe061", "839fe061", "849fe061", "859fe061", "869fe061", "879fe061", "889fe061", "899fe061", "8a9fe061", "8b9fe061", "8c9fe061", "8d9fe061", "8e9fe061", "8f9fe061",
    "909fe061", "919fe061", "929fe061", "939fe061", "949fe061", "959fe061", "969fe061", "979fe061", "989fe061", "999fe061", "9a9fe061", "9b9fe061", "9c9fe061", "9d9fe061", "9e9fe061", "9f9fe061",
    "a09fe061", "a1a0e061", "a2a0e061", "a3a0e061", "a4a0e061", "a5a0e061", "a6a0e061", "a7a0e061", "a8a0e061", "a9a0e061", "aaa0e061", "aba0e061", "aca0e061", "ada0e061", "aea0e061", "afa0e061",
    "b0a0e061", "b1a0e061", "b2a0e061", "b3a0e061", "b4a0e061", "b5a0e061", "b6a0e061", "b7a0e061", "b8a0e061", "b9a0e061", "baa0e061", "bba0e061", "bca0e061", "bda0e061", "bea0e061", "bfa0e061",
    "c0a0e061", "c1a0e061", "c2a0e061", "c3a0e061", "c4a0e061", "c5a0e061", "c6a0e061", "c7a0e061", "c8a0e061", "c9a0e061", "caa0e061", "cba0e061", "cca0e061", "cda0e061", "cea0e061", "cfa0e061",
    "d0a0e061", "d1a0e061", "d2a0e061", "d3a0e061", "d4a0e061", "d5a0e061", "d6a0e061", "d7a0e061", "d8a0e061", "d9a0e061", "daa0e061", "dba0e061", "dca0e061", "dda0e061", "dea0e061", "dfa0e061",
    "e0a0e061", "e1a0e061", "e2a0e061", "e3a0e061", "e4a0e061", "e5a0e061", "e6a0e061", "e7a0e061", "e8a0e061", "e9a0e061", "eaa0e061", "eba0e061", "eca0e061", "eda0e061", "eea0e061", "efa0e061",
    "f0a0e061", "f1a0e061", "f2a0e061", "f3a0e061", "f4a0e061", "f5a0e061", "f6a0e061", "f7a0e061", "f8a0e061", "f9a0e061", "faa0e061", "fba0e061", "fca0e061", "fda0e061", "fea0e061", "ffa0e061",
    "80a1e061", "81a1e061", "82a1e061", "83a1e061", "84a1e061", "85a1e061", "86a1e061", "87a1e061", "88a1e061", "89a1e061", "8aa1e061", "8ba1e061", "8ca1e061", "8da1e061", "8ea1e061", "8fa1e061",
    "90a1e061", "91a1e061", "92a1e061", "93a1e061", "94a1e061", "95a1e061", "96a1e061", "97a1e061", "98a1e061", "99a1e061", "9aa1e061", "9ba1e061", "9ca1e061", "9da1e061", "9ea1e061", "9fa1e061",
    "a0a1e061", "a1a1e061", "a2a1e061", "a3a1e061", "a4a1e061", "a5a1e061", "a6a1e061", "a7a1e061", "a8a1e061", "a9a1e061", "aaa1e061", "aba1e061", "aca1e061", "ada1e061", "aea1e061", "afa1e061",
    "b0a1e061", "b1a1e061", "b2a1e061", "b3a1e061", "b4a1e061", "b5a1e061", "b6a1e061", "b7a1e061", "b8a1e061", "b9a1e061", "baa1e061", "bba1e061", "bca1e061", "bda1e061", "bea1e061", "bfa1e061",
    "c0a1e061", "c1a1e061", "c2a1e061", "c3a1e061", "c4a1e061", "c5a1e061", "c6a1e061", "c7a1e061", "c8a1e061", "c9a1e061", "caa1e061", "cba1e061", "cca1e061", "cda1e061", "cea1e061", "cfa1e061",
    "d0a1e061", "d1a1e061", "d2a1e061", "d3a1e061", "d4a1e061", "d5a1e061", "d6a1e061", "d7a1e061", "d8a1e061", "d9a1e061", "daa1e061", "dba1e061", "dca1e061", "dda1e061", "dea1e061", "dfa1e061",
    "e0a1e061", "e1a1e061", "e2a1e061", "e3a1e061", "e4a1e061", "e5a1e061", "e6a1e061", "e7a1e061", "e8a1e061", "e9a1e061", "eaa1e061", "eba1e061", "eca1e061", "eda1e061", "eea1e061", "efa1e061",
    "f0a1e061", "f1a1e061", "f2a1e061", "f3a1e061", "f4a1e061", "f5a1e061", "f6a1e061", "f7a1e061", "f8a1e061", "f9a1e061", "faa1e061", "fba1e061", "fca1e061", "fda1e061", "fea1e061", "ffa1e061"
]
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000002e08c0c5cefb18100820032a220a0f08e4b8ce6410011880e90f3080e90f0a0f08{ids}10011880e90f3080e90f080000006b08c0c5cefb18100820062a5f0a2208e4b8ce64100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a2208{ids}100118a4f7bcc50620ffffffffffffffffff0128013080e90f380240020a1508fcfadfbe01100120ffffffffffffffffff013801"))
                            time.sleep(0.2)
                    except Exception as e:
                        print(f"[!] Error in @proxyvip: {e}")


                if b"@gov" in data and not self.RbGx:
                    try:
                        items_ids = ['9181bfb003', '9281bfb003', '9381bfb003', '9481bfb003', '9581bfb003', '9681bfb003', '9781bfb003', '9881bfb003', '9981bfb003', '9a81bfb003', '9b81bfb003', '9c81bfb003', '9d81bfb003', '9e81bfb003', '9f81bfb003', 'a081bfb003', 'a181bfb003', 'a281bfb003', 'a381bfb003', 'a481bfb003', 'a581bfb003', 'a681bfb003', 'a781bfb003', 'a881bfb003', 'c1f1beb003', 'c2f1beb003', 'c3f1beb003', 'c4f1beb003', 'c5f1beb003', 'c6f1beb003', 'c7f1beb003', 'c8f1beb003', 'c9f1beb003', 'caf1beb003', 'cbf1beb003', 'ccf1beb003', 'cdf1beb003', 'cef1beb003', 'cff1beb003', 'd0f1beb003', 'd1f1beb003', 'd2f1beb003', 'd3f1beb003', 'd4f1beb003', 'd5f1beb003', 'd6f1beb003', 'd7f1beb003', 'd8f1beb003', 'd9f1beb003', 'daf1beb003', 'dbf1beb003', 'dcf1beb003', 'ddf1beb003', 'def1beb003', 'dff1beb003', 'e0f1beb003', 'e1f1beb003', 'e2f1beb003', 'e3f1beb003', 'e4f1beb003', 'e5f1beb003', 'e6f1beb003', 'e7f1beb003', 'e8f1beb003', 'e9f1beb003', 'eaf1beb003', 'ebf1beb003', 'ecf1beb003', 'edf1beb003', 'eef1beb003', 'eff1beb003', 'f0f1beb003', 'f1f1beb003', 'f2f1beb003', 'f3f1beb003', 'f4f1beb003', 'f5f1beb003', 'f6f1beb003', 'f7f1beb003', 'f8f1beb003', 'f9f1beb003', 'faf1beb003', 'fbf1beb003', 'fcf1beb003', 'fdf1beb003', 'fef1beb003', 'fff1beb003', '80f2beb003', '81f2beb003', '82f2beb003', '83f2beb003', '84f2beb003', '85f2beb003', '86f2beb003', '87f2beb003', '88f2beb003', '89f2beb003', '8af2beb003', '8bf2beb003', '8cf2beb003', '8df2beb003', '8ef2beb003', '8ff2beb003', '90f2beb003', '91f2beb003', '92f2beb003', '93f2beb003', '94f2beb003', '95f2beb003', '96f2beb003', '97f2beb003', '98f2beb003', '99f2beb003', '9af2beb003', '9bf2beb003', '9cf2beb003', '9dfdbeb003', '9efdbeb003', '9ffdbeb003', 'a0fdbeb003', 'a1fdbeb003', 'a2fdbeb003', 'a3fdbeb003', 'a4fdbeb003', 'a5fdbeb003', 'a6fdbeb003', 'a7fdbeb003', 'a8fdbeb003', 'a9fdbeb003', 'aafdbeb003', 'abfdbeb003', 'acfdbeb003', 'adfdbeb003', 'aefdbeb003', 'affdbeb003', 'b0fdbeb003', 'b1fdbeb003', 'b2fdbeb003', 'b3fdbeb003', 'b4fdbeb003', 'b9fcbeb003', 'bafcbeb003', 'bbfcbeb003', 'bcfcbeb003', 'bdfcbeb003', 'befcbeb003', 'bffcbeb003', 'c0fcbeb003', 'c1fcbeb003', 'c2fcbeb003', 'c3fcbeb003', 'c4fcbeb003', 'c5fcbeb003', 'c6fcbeb003', 'c7fcbeb003', 'c8fcbeb003', 'c9fcbeb003', 'cafcbeb003', 'cbfcbeb003', 'ccfcbeb003', 'cdfcbeb003', 'cefcbeb003', 'cffcbeb003', 'd0fcbeb003', 'd1fcbeb003', 'd2fcbeb003', 'd3fcbeb003', 'd4fcbeb003', 'd5fcbeb003', 'd6fcbeb003', 'd7fcbeb003', 'd8fcbeb003', 'd9fcbeb003', 'dafcbeb003', 'dbfcbeb003', 'dcfcbeb003', 'ddfcbeb003', 'defcbeb003', 'dffcbeb003', 'e0fcbeb003', 'e1fcbeb003', 'e2fcbeb003', 'e3fcbeb003', 'd5fbbeb003', 'd6fbbeb003', 'd7fbbeb003', 'd8fbbeb003', 'd9fbbeb003', 'dafbbeb003', 'dbfbbeb003', 'dcfbbeb003', 'ddfbbeb003', 'defbbeb003', 'dffbbeb003', 'e0fbbeb003', 'e1fbbeb003', 'e2fbbeb003', 'e3fbbeb003', 'e4fbbeb003', 'e5fbbeb003', 'e6fbbeb003', 'e7fbbeb003', '81febeb003', '82febeb003', '83febeb003', '84febeb003', '85febeb003', '86febeb003', '87febeb003', '88febeb003', '89febeb003', '8afebeb003', '8bfebeb003', '8cfebeb003', '8dfebeb003', '8efebeb003', '8ffebeb003', '90febeb003', '91febeb003', '92febeb003', '93febeb003', '94febeb003', '95febeb003', '96febeb003', '97febeb003', '98febeb003', '99febeb003', '9afebeb003', '9bfebeb003', '9cfebeb003', '9dfebeb003', 'e5febeb003', 'e6febeb003', 'e7febeb003', 'e8febeb003', 'e9febeb003', 'eafebeb003', 'ebfebeb003', 'ecfebeb003', 'edfebeb003', 'eefebeb003', 'effebeb003', 'f0febeb003', 'f1febeb003', 'f2febeb003', 'f3febeb003', 'f4febeb003', 'f5febeb003', 'f6febeb003', 'f7febeb003', 'f8febeb003', 'f9febeb003', 'fafebeb003', 'fbfebeb003', 'fcfebeb003', 'c9ffbeb003', 'caffbeb003', 'cbffbeb003', 'ccffbeb003', 'cdffbeb003', 'ceffbeb003', 'cfffbeb003', 'd0ffbeb003', 'd1ffbeb003', 'd2ffbeb003', 'd3ffbeb003', 'd4ffbeb003', 'd5ffbeb003', 'd6ffbeb003', 'd7ffbeb003', 'd8ffbeb003', 'd9ffbeb003', 'daffbeb003', 'dbffbeb003', 'dcffbeb003', 'ddffbeb003', 'deffbeb003', 'dfffbeb003', 'e0ffbeb003', 'ad80bfb003', 'ae80bfb003', 'af80bfb003', 'b080bfb003', 'b180bfb003', 'b280bfb003', 'b380bfb003', 'b480bfb003', 'b580bfb003', 'b680bfb003', 'b780bfb003', 'b880bfb003', 'b980bfb003', 'ba80bfb003', 'bb80bfb003', 'bc80bfb003', 'bd80bfb003', 'be80bfb003', 'bf80bfb003', 'c080bfb003', 'c180bfb003', 'c280bfb003', 'c380bfb003', 'c480bfb003','cbd4cab003', 'd3d0cab003', 'd4d0cab003', 'd5d0cab003', 'd6d0cab003', 'e985bfb003', 'ea85bfb003', 'eb85bfb003', 'ec85bfb003', 'ed85bfb003', 'ee85bfb003', 'ef85bfb003', 'f085bfb003', 'f185bfb003', 'f285bfb003', 'f385bfb003', 'f485bfb003', 'f585bfb003', 'f685bfb003', 'f785bfb003', 'f885bfb003', 'f985bfb003', 'fa85bfb003', 'fb85bfb003', 'fc85bfb003', 'fd85bfb003', 'fe85bfb003', 'ff85bfb003', '8086bfb003', '8186bfb003', '8286bfb003', '8386bfb003', '8486bfb003', '8586bfb003', '8686bfb003', '8786bfb003', '8886bfb003', '8986bfb003', '8a86bfb003', '8585bfb003', '8685bfb003', '8785bfb003', '8885bfb003', '8985bfb003', '8a85bfb003', '8b85bfb003', '8c85bfb003', '8d85bfb003', '8e85bfb003', '8f85bfb003', '9085bfb003', '9185bfb003', '9285bfb003', '9385bfb003', '9485bfb003', '9585bfb003', '9685bfb003', '9785bfb003', '9885bfb003', '9985bfb003', '9a85bfb003', '9b85bfb003', '9c85bfb003', '9d85bfb003', '9e85bfb003', '9f85bfb003', 'a085bfb003', 'a185bfb003', 'a285bfb003', 'a385bfb003', 'a485bfb003', 'a585bfb003', 'a685bfb003', 'a184bfb003', 'a284bfb003', 'a384bfb003', 'a484bfb003', 'a584bfb003', 'a684bfb003', 'a784bfb003', 'a884bfb003', 'a984bfb003', 'aa84bfb003', 'ab84bfb003', 'ac84bfb003', 'ad84bfb003', 'ae84bfb003', 'af84bfb003', 'b084bfb003', 'b184bfb003', 'b284bfb003', 'b384bfb003', 'b484bfb003', 'b584bfb003', 'b684bfb003', 'b784bfb003', 'b884bfb003', 'b984bfb003', 'ba84bfb003', 'bb84bfb003', 'bc84bfb003', 'bd84bfb003', 'be84bfb003', 'bf84bfb003', 'c084bfb003', 'c184bfb003', 'c284bfb003', 'c384bfb003', 'c484bfb003', 'bd83bfb003', 'be83bfb003', 'bf83bfb003', 'c083bfb003', 'c183bfb003', 'c283bfb003', 'c383bfb003', 'c483bfb003', 'c583bfb003', 'c683bfb003', 'c783bfb003', 'c883bfb003', 'c983bfb003', 'ca83bfb003', 'cb83bfb003', 'cc83bfb003', 'cd83bfb003', 'ce83bfb003', 'cf83bfb003', 'd083bfb003', 'd183bfb003', 'd283bfb003', 'd383bfb003', 'd982bfb003', 'da82bfb003', 'db82bfb003', 'dc82bfb003', 'dd82bfb003', 'de82bfb003', 'df82bfb003', 'e082bfb003', 'e182bfb003', 'e282bfb003', 'e382bfb003', 'e482bfb003', 'e582bfb003', 'e682bfb003', 'e782bfb003', 'e882bfb003', 'e982bfb003', 'ea82bfb003', 'eb82bfb003', 'ec82bfb003', 'ed82bfb003', 'ee82bfb003', 'ef82bfb003', 'f082bfb003', 'f182bfb003', 'f282bfb003', 'f382bfb003', 'f482bfb003', 'f582bfb003', 'f682bfb003', 'f782bfb003', 'f581bfb003', 'f681bfb003', 'f781bfb003', 'f881bfb003', 'f981bfb003', 'fa81bfb003', 'fb81bfb003', 'fc81bfb003', 'fd81bfb003', 'fe81bfb003', 'ff81bfb003', '8082bfb003', '8182bfb003', '8282bfb003', '8382bfb003', '8482bfb003', '8582bfb003', '8682bfb003', '8782bfb003', '8882bfb003', '8982bfb003', '8a82bfb003', 'bbd1cab003', '9fd2cab003', '83d3cab003', 'e7d3cab003','e9decab003', '85decab003', '95e1cab003', 'dfdecab003', 'fbddcab003', '97ddcab003', 'afd5cab003']  # أضف الباقي
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000003308e7e8e8ba30100820062a270a2508{ids}100118a5f1bec50620ffffffffffffffffff0128013080e90f380240097003"))
                            time.sleep(0.16)
                    except Exception as e:
                        print(f"[!] Error in @gvo: {e}")    
                        
                if b"@bot" in data and not self.RbGx:
                    try:
                        items_ids = ['81fbc6d202', '82fbc6d202', '83fbc6d202', '84fbc6d202', '85fbc6d202', '86fbc6d202', '87fbc6d202', '88fbc6d202', '89fbc6d202', '8afbc6d202', '8bfbc6d202', '8cfbc6d202', '8dfbc6d202', '8efbc6d202', '8ffbc6d202', '90fbc6d202', '91fbc6d202', '92fbc6d202', '93fbc6d202', '94fbc6d202', '95fbc6d202', '96fbc6d202', '97fbc6d202', '98fbc6d202', '99fbc6d202', '9afbc6d202', '9bfbc6d202', '9cfbc6d202', '9dfbc6d202', '9efbc6d202', '9ffbc6d202', 'a0fbc6d202', 'a1fbc6d202', 'a2fbc6d202', 'a3fbc6d202', 'a4fbc6d202', 'a5fbc6d202', 'a6fbc6d202', 'a7fbc6d202', 'a8fbc6d202', 'a9fbc6d202', 'aafbc6d202', 'abfbc6d202', 'acfbc6d202', 'adfbc6d202', 'aefbc6d202', 'affbc6d202', 'b0fbc6d202', 'b1fbc6d202', 'b2fbc6d202', 'b3fbc6d202', 'b4fbc6d202', 'b5fbc6d202', 'b6fbc6d202', 'b7fbc6d202', 'b8fbc6d202', 'b9fbc6d202', 'bafbc6d202', 'bbfbc6d202', 'bcfbc6d202', 'bdfbc6d202', 'befbc6d202', 'bffbc6d202', 'c0fbc6d202', 'c1fbc6d202', 'c2fbc6d202', 'c3fbc6d202', 'c4fbc6d202', 'c5fbc6d202', 'c6fbc6d202', 'c7fbc6d202', 'c8fbc6d202', 'c9fbc6d202', 'cafbc6d202', 'cbfbc6d202', 'ccfbc6d202', 'cdfbc6d202', 'cefbc6d202', 'cffbc6d202', 'd0fbc6d202', 'd1fbc6d202', 'd2fbc6d202', 'd3fbc6d202', 'd4fbc6d202', 'd5fbc6d202', 'd6fbc6d202', 'd7fbc6d202', 'd8fbc6d202', 'd9fbc6d202', 'dafbc6d202', 'dbfbc6d202', 'dcfbc6d202', 'ddfbc6d202', 'defbc6d202', 'dffbc6d202', 'e0fbc6d202', 'e1fbc6d202', 'e2fbc6d202', 'e3fbc6d202', 'e4fbc6d202', 'e5fbc6d202', 'e6fbc6d202', 'e7fbc6d202', 'e8fbc6d202', 'e9fbc6d202', 'eafbc6d202', 'ebfbc6d202', 'ecfbc6d202', 'edfbc6d202', 'eefbc6d202', 'effbc6d202', 'f0fbc6d202', 'f1fbc6d202', 'f2fbc6d202', 'f3fbc6d202', 'f4fbc6d202', 'f5fbc6d202', 'f6fbc6d202', 'f7fbc6d202', 'f8fbc6d202', 'f9fbc6d202', 'fafbc6d202', 'fbfbc6d202', 'fcfbc6d202', 'fdfbc6d202', 'fefbc6d202', 'fffbc6d202', '80fcc6d202', '81fcc6d202', '82fcc6d202', '83fcc6d202', '84fcc6d202', '85fcc6d202', '86fcc6d202', '87fcc6d202', '88fcc6d202', '89fcc6d202', '8afcc6d202', '8bfcc6d202', '8cfcc6d202', '8dfcc6d202', '8efcc6d202', '8ffcc6d202', '90fcc6d202', '91fcc6d202', '92fcc6d202','99edc8d202', '9aedc8d202', '9bedc8d202', '9cedc8d202', '9dedc8d202', '9eedc8d202', '9fedc8d202', 'a0edc8d202', 'a1edc8d202', 'a2edc8d202', 'a3edc8d202', 'a4edc8d202', 'a5edc8d202', 'a6edc8d202', 'a7edc8d202', 'a8edc8d202', 'a9edc8d202', 'aaedc8d202', 'abedc8d202', 'acedc8d202', 'adedc8d202', 'aeedc8d202', 'afedc8d202', 'b0edc8d202', 'b1edc8d202', 'b2edc8d202', 'b3edc8d202', 'b4edc8d202', 'b5edc8d202', 'b6edc8d202', 'b7edc8d202', 'b8edc8d202', 'b9edc8d202', 'baedc8d202', 'bbedc8d202', 'bcedc8d202', 'bdedc8d202', 'beedc8d202', 'bfedc8d202', 'c0edc8d202', 'c1edc8d202', 'c2edc8d202', 'c3edc8d202', 'c4edc8d202', 'c5edc8d202', 'c6edc8d202', 'c7edc8d202', 'c8edc8d202', 'c9edc8d202', 'caedc8d202', 'cbedc8d202', 'ccedc8d202', 'cdedc8d202', 'ceedc8d202', 'cfedc8d202', 'd0edc8d202', 'd1edc8d202', 'd2edc8d202', 'd3edc8d202', 'd4edc8d202', 'd5edc8d202', 'd6edc8d202', 'd7edc8d202', 'd8edc8d202', 'd9edc8d202', 'daedc8d202', 'dbedc8d202', 'dcedc8d202', 'ddedc8d202', 'd184c9d202', 'd284c9d202', 'd384c9d202', 'd484c9d202', 'd584c9d202', 'd684c9d202', 'd784c9d202', 'd884c9d202', 'd984c9d202', 'da84c9d202', 'db84c9d202', 'dc84c9d202', 'dd84c9d202', 'de84c9d202', 'df84c9d202', 'e084c9d202', 'e184c9d202', 'e284c9d202', 'e384c9d202', 'e484c9d202', 'e584c9d202', 'e684c9d202', 'e784c9d202', 'e884c9d202', 'e984c9d202', 'ea84c9d202', 'eb84c9d202', 'ec84c9d202', 'ed84c9d202', 'ee84c9d202', 'ef84c9d202', 'f084c9d202', 'f184c9d202', 'f284c9d202', 'f384c9d202', 'f484c9d202', 'f584c9d202', 'f684c9d202', 'f784c9d202', 'f884c9d202', 'f984c9d202', 'fa84c9d202', 'fb84c9d202', 'fc84c9d202', 'fd84c9d202', 'fe84c9d202', 'ff84c9d202', '8085c9d202', '8185c9d202', '8285c9d202', '8385c9d202', '8485c9d202', '8585c9d202', '8685c9d202', '8785c9d202', '8885c9d202', '8985c9d202', '8a85c9d202', '8b85c9d202', '8c85c9d202', '8d85c9d202', '8e85c9d202', '8f85c9d202', '9085c9d202', '9185c9d202', '9285c9d202', '9385c9d202', '9485c9d202', '9585c9d202', 'b98cc9d202', 'ba8cc9d202', 'bb8cc9d202', 'bc8cc9d202', 'bd8cc9d202', 'be8cc9d202', 'bf8cc9d202', 'c08cc9d202', 'c18cc9d202', 'c28cc9d202', 'c38cc9d202', 'c48cc9d202', 'c58cc9d202', 'c68cc9d202', 'c78cc9d202', 'c88cc9d202', 'c98cc9d202', 'ca8cc9d202', 'cb8cc9d202', 'cc8cc9d202', 'cd8cc9d202', 'ce8cc9d202', 'cf8cc9d202', 'd08cc9d202', 'd18cc9d202', 'd28cc9d202', 'd38cc9d202', 'd48cc9d202', 'd58cc9d202', 'd68cc9d202', 'd78cc9d202', 'd88cc9d202', 'd98cc9d202', 'da8cc9d202', 'db8cc9d202', 'dc8cc9d202', 'dd8cc9d202', 'de8cc9d202', 'df8cc9d202', 'e08cc9d202', 'e18cc9d202', 'e28cc9d202', 'e38cc9d202', 'e48cc9d202', 'e58cc9d202', 'e68cc9d202', 'e78cc9d202', 'e88cc9d202', 'e98cc9d202', 'ea8cc9d202', 'eb8cc9d202', 'ec8cc9d202', 'ed8cc9d202', 'ee8cc9d202', 'ef8cc9d202', 'f08cc9d202', 'f18cc9d202', 'f28cc9d202', 'f38cc9d202', 'f48cc9d202', 'f58cc9d202', 'f68cc9d202', 'f78cc9d202', 'f88cc9d202', 'f98cc9d202', 'fa8cc9d202', 'fb8cc9d202', 'fc8cc9d202', 'fd8cc9d202', 'a194c9d202', 'a294c9d202', 'a394c9d202', 'a494c9d202', 'a594c9d202', 'a694c9d202', 'a794c9d202', 'a894c9d202', 'a994c9d202', 'aa94c9d202', 'ab94c9d202', 'ac94c9d202', 'ad94c9d202', 'ae94c9d202', 'af94c9d202', 'b094c9d202', 'b194c9d202', 'b294c9d202', 'b394c9d202', 'b494c9d202', 'b594c9d202', 'b694c9d202', 'b794c9d202', 'b894c9d202', 'b994c9d202', 'ba94c9d202', 'bb94c9d202', 'bc94c9d202', 'bd94c9d202', 'be94c9d202', 'bf94c9d202', 'c094c9d202', 'c194c9d202', 'c294c9d202', 'c394c9d202', 'c494c9d202', 'c594c9d202', 'c694c9d202', 'c794c9d202', 'c894c9d202', 'c994c9d202', 'ca94c9d202', 'cb94c9d202', 'cc94c9d202', 'cd94c9d202', 'ce94c9d202', 'cf94c9d202', 'd094c9d202', 'd194c9d202', 'd294c9d202', 'd394c9d202', 'd494c9d202', 'd594c9d202', 'd694c9d202', 'd794c9d202', 'd894c9d202', 'd994c9d202', 'da94c9d202', 'db94c9d202', 'dc94c9d202', 'dd94c9d202', 'de94c9d202', 'df94c9d202', 'e094c9d202', 'e194c9d202', 'e294c9d202', 'e394c9d202', 'e494c9d202', 'e594c9d202', '899cc9d202', '8a9cc9d202', '8b9cc9d202', '8c9cc9d202', '8d9cc9d202', '8e9cc9d202', '8f9cc9d202', '909cc9d202', '919cc9d202', '929cc9d202', '939cc9d202', '949cc9d202', '959cc9d202', '969cc9d202', '979cc9d202', '989cc9d202', '999cc9d202', '9a9cc9d202', '9b9cc9d202', '9c9cc9d202', '9d9cc9d202', '9e9cc9d202', '9f9cc9d202', 'a09cc9d202', 'a19cc9d202', 'a29cc9d202', 'a39cc9d202', 'a49cc9d202', 'a59cc9d202', 'a69cc9d202', 'a79cc9d202', 'a89cc9d202', 'a99cc9d202', 'aa9cc9d202', 'ab9cc9d202', 'ac9cc9d202', 'ad9cc9d202', 'ae9cc9d202', 'af9cc9d202', 'b09cc9d202', 'b19cc9d202', 'b29cc9d202', 'b39cc9d202', 'b49cc9d202', 'b59cc9d202', 'b69cc9d202', 'b79cc9d202', 'b89cc9d202', 'b99cc9d202', 'ba9cc9d202', 'bb9cc9d202', 'bc9cc9d202', 'bd9cc9d202', 'be9cc9d202', 'bf9cc9d202', 'c09cc9d202', 'c19cc9d202', 'c29cc9d202', 'c39cc9d202', 'c49cc9d202', 'c59cc9d202', 'c69cc9d202', 'c79cc9d202', 'c89cc9d202', 'c99cc9d202', 'ca9cc9d202', 'cb9cc9d202', 'cc9cc9d202', 'cd9cc9d202', 'f1a3c9d202', 'f2a3c9d202', 'f3a3c9d202', 'f4a3c9d202', 'f5a3c9d202', 'f6a3c9d202', 'f7a3c9d202', 'f8a3c9d202', 'f9a3c9d202', 'faa3c9d202', 'fba3c9d202', 'fca3c9d202', 'fda3c9d202', 'fea3c9d202', 'ffa3c9d202', '80a4c9d202', '81a4c9d202', '82a4c9d202', '83a4c9d202', '84a4c9d202', '85a4c9d202', '86a4c9d202', '87a4c9d202', '88a4c9d202', '89a4c9d202', '8aa4c9d202', '8ba4c9d202', '8ca4c9d202', '8da4c9d202', '8ea4c9d202', '8fa4c9d202', '90a4c9d202', '91a4c9d202', '92a4c9d202', '93a4c9d202', '94a4c9d202', '95a4c9d202', '96a4c9d202', '97a4c9d202', '98a4c9d202', '99a4c9d202', '9aa4c9d202', '9ba4c9d202', '9ca4c9d202', '9da4c9d202', '9ea4c9d202', '9fa4c9d202', 'a0a4c9d202', 'a1a4c9d202', 'a2a4c9d202', 'a3a4c9d202', 'a4a4c9d202', 'a5a4c9d202', 'a6a4c9d202', 'a7a4c9d202', 'a8a4c9d202', 'a9a4c9d202', 'aaa4c9d202', 'aba4c9d202', 'aca4c9d202', 'ada4c9d202', 'aea4c9d202', 'afa4c9d202', 'b0a4c9d202', 'b1a4c9d202', 'b2a4c9d202', 'b3a4c9d202', 'b4a4c9d202', 'b5a4c9d202', 'd9abc9d202', 'daabc9d202', 'dbabc9d202', 'dcabc9d202', 'ddabc9d202', 'deabc9d202', 'dfabc9d202', 'e0abc9d202', 'e1abc9d202', 'e2abc9d202', 'e3abc9d202', 'e4abc9d202', 'e5abc9d202', 'e6abc9d202', 'e7abc9d202', 'e8abc9d202', 'e9abc9d202', 'eaabc9d202', 'ebabc9d202', 'ecabc9d202', 'edabc9d202', 'eeabc9d202', 'efabc9d202', 'f0abc9d202', 'f1abc9d202', 'f2abc9d202', 'f3abc9d202', 'f4abc9d202', 'f5abc9d202', 'f6abc9d202', 'f7abc9d202', 'f8abc9d202', 'f9abc9d202', 'faabc9d202', 'fbabc9d202', 'fcabc9d202', 'fdabc9d202', 'feabc9d202', 'ffabc9d202', '80acc9d202', '81acc9d202', '82acc9d202', '83acc9d202', '84acc9d202', '85acc9d202', '86acc9d202', '87acc9d202', '88acc9d202', '89acc9d202', '8aacc9d202', '8bacc9d202', '8cacc9d202', '8dacc9d202', '8eacc9d202', '8facc9d202', '90acc9d202', '91acc9d202', '92acc9d202', '93acc9d202', '94acc9d202', '95acc9d202', '96acc9d202', '97acc9d202', '98acc9d202', '99acc9d202', '9aacc9d202', '9bacc9d202', '9cacc9d202', '9dacc9d202', '91c3c9d202', '92c3c9d202', '93c3c9d202', '94c3c9d202', '95c3c9d202', '96c3c9d202', '97c3c9d202', '98c3c9d202', '99c3c9d202', '9ac3c9d202', '9bc3c9d202', '9cc3c9d202', '9dc3c9d202', '9ec3c9d202', '9fc3c9d202', 'a0c3c9d202', 'a1c3c9d202', 'a2c3c9d202', 'a3c3c9d202', 'a4c3c9d202', 'a5c3c9d202', 'a6c3c9d202', 'a7c3c9d202', 'a8c3c9d202', 'a9c3c9d202', 'aac3c9d202', 'abc3c9d202', 'acc3c9d202', 'adc3c9d202', 'aec3c9d202', 'afc3c9d202', 'b0c3c9d202', 'b1c3c9d202', 'b2c3c9d202', 'b3c3c9d202', 'b4c3c9d202', 'b5c3c9d202', 'b6c3c9d202', 'b7c3c9d202', 'b8c3c9d202', 'b9c3c9d202', 'bac3c9d202', 'bbc3c9d202', 'bcc3c9d202', 'bdc3c9d202', 'bec3c9d202', 'bfc3c9d202', 'c0c3c9d202', 'c1c3c9d202', 'c2c3c9d202', 'c3c3c9d202', 'c4c3c9d202', 'c5c3c9d202', 'c6c3c9d202', 'c7c3c9d202', 'c8c3c9d202', 'c9c3c9d202', 'cac3c9d202', 'cbc3c9d202', 'ccc3c9d202', 'cdc3c9d202', 'cec3c9d202', 'cfc3c9d202', 'd0c3c9d202', 'd1c3c9d202', 'd2c3c9d202', 'd3c3c9d202', 'd4c3c9d202', 'd5c3c9d202', 'f9cac9d202', 'facac9d202', 'fbcac9d202', 'fccac9d202', 'fdcac9d202', 'fecac9d202', 'ffcac9d202', '80cbc9d202', '81cbc9d202', '82cbc9d202', '83cbc9d202', '84cbc9d202', '85cbc9d202', '86cbc9d202', '87cbc9d202', '88cbc9d202', '89cbc9d202', '8acbc9d202', '8bcbc9d202', '8ccbc9d202', '8dcbc9d202', '8ecbc9d202', '8fcbc9d202', '90cbc9d202', '91cbc9d202', '92cbc9d202', '93cbc9d202', '94cbc9d202', '95cbc9d202', '96cbc9d202', '97cbc9d202', '98cbc9d202', '99cbc9d202', '9acbc9d202', '9bcbc9d202', '9ccbc9d202', '9dcbc9d202', '9ecbc9d202', '9fcbc9d202', 'a0cbc9d202', 'a1cbc9d202', 'a2cbc9d202', 'a3cbc9d202', 'a4cbc9d202', 'a5cbc9d202', 'a6cbc9d202', 'a7cbc9d202', 'a8cbc9d202', 'a9cbc9d202', 'aacbc9d202', 'abcbc9d202', 'accbc9d202', 'adcbc9d202', 'aecbc9d202', 'afcbc9d202', 'b0cbc9d202', 'b1cbc9d202', 'b2cbc9d202', 'b3cbc9d202', 'b4cbc9d202', 'b5cbc9d202', 'b6cbc9d202', 'b7cbc9d202', 'b8cbc9d202', 'b9cbc9d202', 'bacbc9d202', 'bbcbc9d202', 'bccbc9d202', 'bdcbc9d202', 'e1d2c9d202', 'e2d2c9d202', 'e3d2c9d202', 'e4d2c9d202', 'e5d2c9d202', 'e6d2c9d202', 'e7d2c9d202', 'e8d2c9d202', 'e9d2c9d202', 'ead2c9d202', 'ebd2c9d202', 'ecd2c9d202', 'edd2c9d202', 'eed2c9d202', 'efd2c9d202', 'f0d2c9d202', 'f1d2c9d202', 'f2d2c9d202', 'f3d2c9d202', 'f4d2c9d202', 'f5d2c9d202', 'f6d2c9d202', 'f7d2c9d202', 'f8d2c9d202', 'f9d2c9d202', 'fad2c9d202', 'fbd2c9d202', 'fcd2c9d202', 'fdd2c9d202', 'fed2c9d202', 'ffd2c9d202', '80d3c9d202', '81d3c9d202', '82d3c9d202', '83d3c9d202', '84d3c9d202', '85d3c9d202', '86d3c9d202', '87d3c9d202', '88d3c9d202', '89d3c9d202', '8ad3c9d202', '8bd3c9d202', '8cd3c9d202', '8dd3c9d202', '8ed3c9d202', '8fd3c9d202', '90d3c9d202', '91d3c9d202', '92d3c9d202', '93d3c9d202', '94d3c9d202', '95d3c9d202', '96d3c9d202', '97d3c9d202', '98d3c9d202', '99d3c9d202', '9ad3c9d202', '9bd3c9d202', '9cd3c9d202', '9dd3c9d202', '9ed3c9d202', '9fd3c9d202', 'a0d3c9d202', 'a1d3c9d202', 'a2d3c9d202', 'a3d3c9d202', 'a4d3c9d202', 'a5d3c9d202', 'c9dac9d202', 'cadac9d202', 'cbdac9d202', 'ccdac9d202', 'cddac9d202', 'cedac9d202', 'cfdac9d202', 'd0dac9d202', 'd1dac9d202', 'd2dac9d202', 'd3dac9d202', 'd4dac9d202', 'd5dac9d202', 'd6dac9d202', 'd7dac9d202', 'd8dac9d202', 'd9dac9d202', 'dadac9d202', 'dbdac9d202', 'dcdac9d202', 'dddac9d202', 'dedac9d202', 'dfdac9d202', 'e0dac9d202', 'e1dac9d202', 'e2dac9d202', 'e3dac9d202', 'e4dac9d202', 'e5dac9d202', 'e6dac9d202', 'e7dac9d202', 'e8dac9d202', 'e9dac9d202', 'eadac9d202', 'ebdac9d202', 'ecdac9d202', 'eddac9d202', 'eedac9d202', 'efdac9d202', 'f0dac9d202', 'f1dac9d202', 'f2dac9d202', 'f3dac9d202', 'f4dac9d202', 'f5dac9d202', 'f6dac9d202', 'f7dac9d202', 'f8dac9d202', 'f9dac9d202', 'fadac9d202', 'fbdac9d202', 'fcdac9d202', 'fddac9d202', 'fedac9d202', 'ffdac9d202', '80dbc9d202', '81dbc9d202', '82dbc9d202', '83dbc9d202', '84dbc9d202', '85dbc9d202', '86dbc9d202', '87dbc9d202', '88dbc9d202', '89dbc9d202', '8adbc9d202', '8bdbc9d202', '8cdbc9d202', '8ddbc9d202', 'b1e2c9d202', 'b2e2c9d202', 'b3e2c9d202', 'b4e2c9d202', 'b5e2c9d202', 'b6e2c9d202', 'b7e2c9d202', 'b8e2c9d202', 'b9e2c9d202', 'bae2c9d202', 'bbe2c9d202', 'bce2c9d202', 'bde2c9d202', 'bee2c9d202', 'bfe2c9d202', 'c0e2c9d202', 'c1e2c9d202', 'c2e2c9d202', 'c3e2c9d202', 'c4e2c9d202', 'c5e2c9d202', 'c6e2c9d202', 'c7e2c9d202', 'c8e2c9d202', 'c9e2c9d202', 'cae2c9d202', 'cbe2c9d202', 'cce2c9d202', 'cde2c9d202', 'cee2c9d202', 'cfe2c9d202', 'd0e2c9d202', 'd1e2c9d202', 'd2e2c9d202', 'd3e2c9d202', 'd4e2c9d202', 'd5e2c9d202', 'd6e2c9d202', 'd7e2c9d202', 'd8e2c9d202', 'd9e2c9d202', 'dae2c9d202', 'dbe2c9d202', 'dce2c9d202', 'dde2c9d202', 'dee2c9d202', 'dfe2c9d202', 'e0e2c9d202', 'e1e2c9d202', 'e2e2c9d202', 'e3e2c9d202', 'e4e2c9d202', 'e5e2c9d202', 'e6e2c9d202', 'e7e2c9d202', 'e8e2c9d202', 'e9e2c9d202', 'eae2c9d202', 'ebe2c9d202', 'ece2c9d202', 'ede2c9d202', 'eee2c9d202', 'efe2c9d202', 'f0e2c9d202', 'f1e2c9d202', 'f2e2c9d202', 'f3e2c9d202', 'f4e2c9d202', 'f5e2c9d202', '99eac9d202', '9aeac9d202', '9beac9d202', '9ceac9d202', '9deac9d202', '9eeac9d202', '9feac9d202', 'a0eac9d202', 'a1eac9d202', 'a2eac9d202', 'a3eac9d202', 'a4eac9d202', 'a5eac9d202', 'a6eac9d202', 'a7eac9d202', 'a8eac9d202', 'a9eac9d202', 'aaeac9d202', 'abeac9d202', 'aceac9d202', 'adeac9d202', 'aeeac9d202', 'afeac9d202', 'b0eac9d202', 'b1eac9d202', 'b2eac9d202', 'b3eac9d202', 'b4eac9d202', 'b5eac9d202', 'b6eac9d202', 'b7eac9d202', 'b8eac9d202', 'b9eac9d202', 'baeac9d202', 'bbeac9d202', 'bceac9d202', 'bdeac9d202', 'beeac9d202', 'bfeac9d202', 'c0eac9d202', 'c1eac9d202', 'c2eac9d202', 'c3eac9d202', 'c4eac9d202', 'c5eac9d202', 'c6eac9d202', 'c7eac9d202', 'c8eac9d202', 'c9eac9d202', 'caeac9d202', 'cbeac9d202', 'cceac9d202', 'cdeac9d202', 'ceeac9d202', 'cfeac9d202', 'd0eac9d202', 'd1eac9d202', 'd2eac9d202', 'd3eac9d202', 'd4eac9d202', 'd5eac9d202', 'd6eac9d202', 'd7eac9d202', 'd8eac9d202', 'd9eac9d202', 'daeac9d202', 'dbeac9d202', 'dceac9d202', 'ddeac9d202', '81f2c9d202', '82f2c9d202', '83f2c9d202', '84f2c9d202', '85f2c9d202', '86f2c9d202', '87f2c9d202', '88f2c9d202', '89f2c9d202', '8af2c9d202', '8bf2c9d202', '8cf2c9d202', '8df2c9d202', '8ef2c9d202', '8ff2c9d202', '90f2c9d202', '91f2c9d202', '92f2c9d202', '93f2c9d202', '94f2c9d202', '95f2c9d202', '96f2c9d202', '97f2c9d202', '98f2c9d202', '99f2c9d202', '9af2c9d202', '9bf2c9d202', '9cf2c9d202', '9df2c9d202', '9ef2c9d202', '9ff2c9d202', 'a0f2c9d202', 'a1f2c9d202', 'a2f2c9d202', 'a3f2c9d202', 'a4f2c9d202', 'a5f2c9d202', 'a6f2c9d202', 'a7f2c9d202', 'a8f2c9d202', 'a9f2c9d202', 'aaf2c9d202', 'abf2c9d202', 'acf2c9d202', 'adf2c9d202', 'aef2c9d202', 'aff2c9d202', 'b0f2c9d202', 'b1f2c9d202', 'b2f2c9d202', 'b3f2c9d202', 'b4f2c9d202', 'b5f2c9d202', 'b6f2c9d202', 'b7f2c9d202', 'b8f2c9d202', 'b9f2c9d202', 'baf2c9d202', 'bbf2c9d202', 'bcf2c9d202', 'bdf2c9d202', 'bef2c9d202', 'bff2c9d202', 'c0f2c9d202', 'c1f2c9d202', 'c2f2c9d202', 'c3f2c9d202', 'c4f2c9d202', 'c5f2c9d202', 'e9f9c9d202', 'eaf9c9d202', 'ebf9c9d202', 'ecf9c9d202', 'edf9c9d202', 'eef9c9d202', 'eff9c9d202', 'f0f9c9d202', 'f1f9c9d202', 'f2f9c9d202', 'f3f9c9d202', 'f4f9c9d202', 'f5f9c9d202', 'f6f9c9d202', 'f7f9c9d202', 'f8f9c9d202', 'f9f9c9d202', 'faf9c9d202', 'fbf9c9d202', 'fcf9c9d202', 'fdf9c9d202', 'fef9c9d202', 'fff9c9d202', '80fac9d202', '81fac9d202', '82fac9d202', '83fac9d202', '84fac9d202', '85fac9d202', '86fac9d202', '87fac9d202', '88fac9d202', '89fac9d202', '8afac9d202', '8bfac9d202', '8cfac9d202', '8dfac9d202', '8efac9d202', '8ffac9d202', '90fac9d202', '91fac9d202', '92fac9d202', '93fac9d202', '94fac9d202', '95fac9d202', '96fac9d202', '97fac9d202', '98fac9d202', '99fac9d202', '9afac9d202', '9bfac9d202', '9cfac9d202', '9dfac9d202', '9efac9d202', '9ffac9d202', 'a0fac9d202', 'a1fac9d202', 'a2fac9d202', 'a3fac9d202', 'a4fac9d202', 'a5fac9d202', 'a6fac9d202', 'a7fac9d202', 'a8fac9d202', 'a9fac9d202', 'aafac9d202', 'abfac9d202', 'acfac9d202', 'adfac9d202']  # أضف الباقي
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"08000000be08c0c5cefb18100820062ab1010a1808d885d164100120ffffffffffffffffff012801380140020a1808d985d164100120ffffffffffffffffff012801380140020a1808fe928866100120ffffffffffffffffff012801380140020a1808cfe1e860100120ffffffffffffffffff012801380140020a18088fe6a561100120ffffffffffffffffff012801380140020a1808cfeae261100120ffffffffffffffffff012801380140020a1308{ids}20ffffffffffffffffff013801"))
                            time.sleep(0.16)
                    except Exception as e:
                        print(f"[!] Error in @bot: {e}")        
                        
                if b"@box" in data and not self.RbGx:
                    try:
                        items_ids = ['81fd8751', '82fd8751', '83fd8751', '84fd8751', '85fd8751', '86fd8751', '87fd8751', '88fd8751', '89fd8751', '8afd8751', '8bfd8751', '8cfd8751', '8dfd8751', '8efd8751', '8ffd8751', '90fd8751', '91fd8751', '92fd8751', '93fd8751', '94fd8751', '95fd8751', '96fd8751', '97fd8751', '98fd8751', '99fd8751', '9afd8751', '9bfd8751', '9cfd8751', '9dfd8751', '9efd8751', '9ffd8751', 'a0fd8751', 'a1fd8751', 'a2fd8751', 'a3fd8751', 'a4fd8751', 'a5fd8751', 'a6fd8751', 'a7fd8751', 'a8fd8751', 'a9fd8751', 'aafd8751', 'abfd8751', 'acfd8751', 'adfd8751', 'aefd8751', 'affd8751', 'b0fd8751', 'b1fd8751', 'b2fd8751', 'b3fd8751', 'b4fd8751', 'b5fd8751', 'b6fd8751', 'b7fd8751', 'b8fd8751', 'b9fd8751', 'bafd8751', 'bbfd8751', 'bcfd8751', 'bdfd8751', 'befd8751', 'bffd8751', 'c0fd8751', 'c1fd8751', 'c2fd8751', 'c3fd8751', 'c4fd8751', 'c5fd8751', 'c6fd8751', 'c7fd8751', 'c8fd8751', 'c9fd8751', 'cafd8751', 'cbfd8751', 'ccfd8751', 'cdfd8751', 'cefd8751', 'cffd8751', 'd0fd8751', 'd1fd8751', 'd2fd8751', 'd3fd8751', 'd4fd8751', 'd5fd8751', 'd6fd8751', 'd7fd8751', 'd8fd8751', 'd9fd8751']  # أضف الباقي
                        for ids in items_ids:
                            self.sock0500.send(bytes.fromhex(f"080000003a0888d49a9a28100820062a2e0a180896cbd130100120ffffffffffffffffff012801380140010a1208{ids}20ffffffffffffffffff01380108000000150888d49a9a28100820032a090a070896cbd13010010d0000000f0888d49a9a28100d20022a0308ce1a"))
                            time.sleep(0.16)
                    except Exception as e:
                        print(f"[!] Error in @box: {e}")                                                                                    
#################################
                if "1200" in data.hex()[:4] and RbGx == True :
                    self.send(bytes.fromhex(gen_msgv2(data.hex() ,"[E0FF00]CHAT SPAME : [E0FF00]ON")))        
                if client.send(data) <= 0:
                    break
                    
                    
#################################
#زكس هون الرد عل رسائل


#بس
####################################

    def generate_failed_reply(self, address_type, error_number):
        return b''.join([
            SOCKS_VERSION.to_bytes(1, 'big'),
            error_number.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            address_type.to_bytes(1, 'big'),
            int(0).to_bytes(4, 'big'),
            int(0).to_bytes(4, 'big')
        ])


#################################


    def verify_credentials(self, connection):
        version = connection.recv(1)[0]
        username_len = connection.recv(1)[0]
        username = connection.recv(username_len).decode('utf-8')
        password_len = connection.recv(1)[0]
        password = connection.recv(password_len).decode('utf-8')

        if username == self.username and password == self.password:
            response = bytes([version, 0])
            connection.sendall(response)
            return True
        else:
            response = bytes([version, 0])
            connection.sendall(response)
            return True


#################################


    def get_available_methods(self, nmethods, connection):
        methods = []
        for _ in range(nmethods):
            methods.append(connection.recv(1)[0])
        return methods

    def run(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen()
        print(f"* Socks5 proxy server is running on {ip}:{port}")

        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=self.handle_client, args=(conn,))
            t.start()


#################################


    def RbGx(self, data_join):
        global back
        while back:
            try:
                self.op.send(data_join)
                time.sleep(9999.0)
            except Exception as e:
                pass

 
                      
 #################################
#الاوامر

                # ===== جميع الأوامر مع التحقق من التفعيل =====

                # ===== أمر @sqwad =====


            
                       
################################

                                    
def gen_msgv2(packet, replay):
    replay = replay.encode('utf-8')
    replay = replay.hex()

    hedar = packet[0:8]
    packetLength = packet[8:10]  #
    paketBody = packet[10:32]
    pyloadbodyLength = packet[32:34]  #
    pyloadbody2 = packet[34:60]

    pyloadlength = packet[60:62]  #
    pyloadtext = re.findall(r'{}(.*?)28'.format(pyloadlength), packet[50:])[0]
    pyloadTile = packet[int(int(len(pyloadtext)) + 62):]

    NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext) // 2)) + int(len(replay) // 2))[2:])
    if len(NewTextLength) == 1:
        NewTextLength = "0" + str(NewTextLength)

    NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext)) // 2))) + int(len(replay) // 2))[2:]
    NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext) // 2))) + int(len(replay) // 2))[2:]

    finallyPacket = hedar + NewpaketLength + paketBody + NewPyloadLength + pyloadbody2 + NewTextLength + replay + pyloadTile

    return str(finallyPacket)


#################################


def startt():
    Proxy().run('127.0.0.1', 3000)


startt()
