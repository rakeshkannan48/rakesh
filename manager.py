# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:32:55 2019

@author: 600040233
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 13:57:09 2019

@author: Ajinkya Indulkar, Vijith Shetty
"""

##----------LOAD CONFIG-----------------------------------##
import yaml 

with open('./config.yml', 'r') as f:
    cfg = yaml.load(f)

##-----------------CONNECT TO AD----------------------------##
import ldap3
import json
from tqdm import tqdm
    
server = ldap3.Server(cfg['host'], get_info=ldap3.ALL)

conn = ldap3.Connection(server, user=cfg['user'], 
                        password=cfg['pwd'], authentication=ldap3.NTLM, auto_bind=True)

conn.start_tls()


#Searching personal account of user MODULARIZE THIS SEGEMENT
emailID="anjan.prasad.guna.seela@signify.com"
conn.search(' ou=Users-AAD,dc=lux,dc=intra,dc=lighting,dc=com','(mail='+emailID+')',
            attributes=ldap3.ALL_ATTRIBUTES) 
personal_entry_user = [json.loads(e.entry_to_json()) for e in tqdm(conn.entries)] 
 

#splicing out the LUX Id of the manager Refer "seeAlso" attribute for user, All LUX IDs do not have uniform number of elements
arrsplit=personal_entry_user[0]['attributes']['seeAlso'][0].split(',')
LUX_ID_Manager=(arrsplit[0].split('=')[1])

# Searching Personal Account of Manager
conn.search(' ou=Users-AAD,dc=lux,dc=intra,dc=lighting,dc=com','(cn='+LUX_ID_Manager+')',
            attributes=ldap3.ALL_ATTRIBUTES)  
personal_entry_manager = [json.loads(e.entry_to_json()) for e in tqdm(conn.entries)]

#Display manager details
print(personal_entry_manager[0]['attributes']['description'][0])
print(personal_entry_manager[0]['attributes']['mail'][0])

 
