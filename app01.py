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
		global b
		self.a = ""
		self.b = "black"

		self.nomeLabel = Label(root, text="Colar URL aqui.: ")
		self.nomeLabel.grid(row=0,column=0,sticky='e')
		
		self.url = Entry(root,width=100)
		self.url.focus_set()
		self.url.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=9)

		self.fundoNuvem = Label(root,text="Escolher Tema.: ")
		self.fundoNuvem.grid(row=1,column=1,sticky='w')
		
		self.opcaoUM = Radiobutton(root,text="Dia",variable=var,value=1,command=self.sel)
		self.opcaoUM.grid(row=2,column=1, sticky='w')
		
		self.opcaoDois = Radiobutton(root,text="Noite",variable=var,value=2,command=self.sel)
		self.opcaoDois.grid(row=2,column=2, sticky='w')

		self.buscar = Button(root, text="Download",command=self.buscarDiscurso)
		self.buscar.grid(row=0,column=10,sticky='e'+'w',padx=2,pady=2)
		
		self.recuperarArquivo = Button(root, text="Abrir",command=self.abrirArquivo)
		self.recuperarArquivo.grid(row=1,column=10,sticky='e'+'w',padx=2)
		
		self.gerarNuvemTags = Button(root, text="Gerar Nuvem de Tags",command=self.gerarNuvemTagsX)
		self.gerarNuvemTags.grid(row=2,column=10,sticky='e'+'w',padx=2)
		
		self.sair = Button(root, text="Sair",command=self.sairExit)
		self.sair.grid(row=3,column=10,sticky='e'+'w',padx=2)
		
		self.mensagem = Label(root, text="")
		self.mensagem.grid(row=3,column=1,sticky='e'+'w',columnspan=9)
		
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
		text = open(string,'r', encoding="utf-8", errors="ignore").read()
		cloudtags.gerarNuvemTagss(text,self.b)
		self.url.delete(0, "end")
		self.url.insert(0, "")
	
	def sel(self):
		 self.b = var.get()


root = Tk()
var = IntVar()
root.title("Gerador de Nuvem de Palavras")
Application(root)
root.mainloop()
