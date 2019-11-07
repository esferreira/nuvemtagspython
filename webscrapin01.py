#-*- coding: utf8 -*-

import sys, os
import getpass 
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import urllib.request as req
from bs4 import BeautifulSoup

user = os.getlogin()
script_directory = os.path.split(os.path.abspath(__file__))[0]
proxyy = input('Você está logado numa rede que utiliza o serviço de Proxy? (y | N) .:')
if proxyy.lower() == 'y':
	user_proxy = input("Usuário Proxy.: ")
	pass_proxy = getpass.getpass("Senha Proxy.: ")
	proxy = req.ProxyHandler({'http': r'http://'+user_proxy+':'+pass_proxy+'@10.251.250.250:3128'})
	auth = req.HTTPBasicAuthHandler()
	opener = req.build_opener(proxy, auth, req.HTTPHandler)
	req.install_opener(opener)
  
print("Iniciando...")

def getDiscurso(url, documento):
	if os.path.exists(documento):
		os.remove(documento)
		print("Arquivo removido!")
	else:
		current_work_directory = os.getcwd()  
		print('Current work directory: {}'.format(current_work_directory))
		abs_work_directory = os.path.abspath(current_work_directory)
		print('Current work directory (full path): {}'.format(abs_work_directory))
		print()
		
		if not os.path.isfile(documento):
			print('It seems file "{}" not exists in directory: "{}"'.format(documento, current_work_directory))
			print(script_directory)
			abs_filename = os.path.join(script_directory, documento+'.txt')
			print(abs_filename)
			
			arquivo = open(abs_filename, "w", encoding="utf-8")
		
	try:
		conn = req.urlopen(url)
		bsObj = BeautifulSoup(conn.read(), 'html.parser');
		nameList = bsObj.findAll("p")
		for name in nameList:
			conteudo = name.get_text()
			arquivo.write(conteudo.rstrip('\n'))
		arquivo.close()
	except HTTPError as e:
		print('Error code: ', e.code)
	except URLError as e:
		print('Reason: ', e.reason)
	else:
		print('Usuário logado.: '+str(user)+'!')
	return abs_filename
