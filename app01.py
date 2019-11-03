#-*- coding: utf8 -*-

import os
import subprocess as sp
from tkinter import *
from tkinter import filedialog
import webscrapin01
import cloudtags

class Application:
	def __init__(self, master=None):
		global a
		self.a = ""
		self.fontePadrao = ("Arial", "10")
		self.primeiroContainer = Frame(master)
		self.primeiroContainer["pady"] = 10
		self.primeiroContainer.pack()

		self.segundoContainer = Frame(master)
		self.segundoContainer["padx"] = 20
		self.segundoContainer.pack()

		self.terceiroContainer = Frame(master)
		self.terceiroContainer["pady"] = 20
		self.terceiroContainer.pack()
		
		self.quartoContainer = Frame(master)
		self.quartoContainer["pady"] = 20
		self.quartoContainer.pack()

		self.titulo = Label(self.primeiroContainer, text="Seu desejo é uma ordem!")
		self.titulo["font"] = ("Arial", "10", "bold")
		self.titulo.pack()

		self.nomeLabel = Label(self.segundoContainer,text="Colar URL aqui.: ", font=self.fontePadrao)
		self.nomeLabel.pack(side=LEFT)

		self.url = Entry(self.segundoContainer)
		self.url["width"] = 100
		self.url["font"] = self.fontePadrao
		self.url.focus_set()
		self.url.pack(side=LEFT)

		self.buscar = Button(self.terceiroContainer)
		self.buscar["text"] = "Download"
		self.buscar["font"] = ("Calibri", "10")
		self.buscar["width"] = 12
		self.buscar["command"] = self.buscarDiscurso
		self.buscar.pack(side=LEFT)

		self.sair = Button(self.terceiroContainer)
		self.sair["text"] = "Sair"
		self.sair["font"] = ("Calibri", "10")
		self.sair["width"] = 5
		self.sair["command"] = self.sairExit
		self.sair.pack (side=RIGHT)
		
		self.recuperarArquivo = Button(self.terceiroContainer)
		self.recuperarArquivo["text"] = "Abrir"
		self.recuperarArquivo["font"] = ("Calibri", "10")
		self.recuperarArquivo["width"] = 10
		self.recuperarArquivo["command"] = self.abrirArquivo
		self.recuperarArquivo.pack (side=LEFT)
		
		self.gerarNuvemTags = Button(self.terceiroContainer)
		self.gerarNuvemTags["text"] = "Gerar Nuvem de Tags"
		self.gerarNuvemTags["font"] = ("Calibri", "10")
		self.gerarNuvemTags["width"] = 20
		self.gerarNuvemTags["command"] = self.gerarNuvemTagsX
		self.gerarNuvemTags.pack (side=LEFT)
		
		self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
		self.mensagem.pack()

	#Método buscar discurso
	def buscarDiscurso(self):
		string = self.url.get()
		documento = string.split('/')
		if len(documento[-1]) > 0:
			arq = documento[-1]
		else:
			arq = documento[-2]
		self.a = webscrapin01.getDiscurso(string,arq)
		self.mensagem["text"] = "Arquivo salvo em.: "+self.a
		self.url.delete(0, "end")
		self.url.insert(0, "")
	
	#Método sair
	def sairExit(self):
		print("Sistema finalizado manualmente por "+str(webscrapin01.user))
		import sys; sys.exit() 
		
	#Método abrir arquivo
	def abrirArquivo(self):
		print("Diretório do último arquivo gerado.: "+str(self.a))
		print("Diretório local dos arquivos gerados.: "+webscrapin01.script_directory)
		filename = filedialog.askopenfilename(initialdir = webscrapin01.script_directory, 
		                                      title = "Selecione o arquivo", 
		                                      filetypes=(("text files", "*.txt"), 
		                                      ("all files", "*.*")))
		programName = "notepad.exe"
		sp.Popen([programName, filename])
		self.url.insert(0, filename)
		print(filename)
	
	#Método gerar nuvem de tags
	def gerarNuvemTagsX(self):
		print("Gerar nuvem de tags")
		string = self.url.get()
		text = open(string,'r').read()
		cloudtags.gerarNuvemTagss(text)
		self.url.delete(0, "end")
		self.url.insert(0, "")



root = Tk()
root.title('Aplicativo para Geração de Nuvem de Palavras')

Application(root)
root.mainloop()
