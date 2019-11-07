#-*- coding: utf8 -*-

import re
import nltk
from nltk.corpus import stopwords
from string import punctuation
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from unidecode import unidecode
import webscrapin01
    
def gerarNuvemTagss(text, background):
	if background == 1:
		dia_noite = 'white'
	else:
		dia_noite = 'black'
	if webscrapin01.proxyy.lower() == 'y':
		nltk.set_proxy('http://'+webscrapin01.user_proxy+':'+webscrapin01.pass_proxy+'@10.251.250.250:3128')
	nltk.download('punkt')
	nltk.download('stopwords')
	# remover caracteres especiais e remover acentuação
	review = re.sub('[^a-zA-Z]', ' ', str(unidecode(text)))
	# converter texto para minusculo
	review = review.lower()
	# criar uma lista de palavras
	review = review.split()
	# preparar palavras comuns e pontuação para serem removidas da lista
	stopw = (stopwords.words('portuguese') + list(punctuation))
	# adicionar palavras comuns não previstas pelo stopwords
	addExcecoes = ['ha','ver','alguns','ate','aqui','la','sendo','estar','novo','vez','desses','quero','deixou','geral','cada','boa',
	'outras','certo','dentro','deixe','tudo','pronto','toda','manter','locais','deste','sob','agora','diz','assim','daquele','tanto','busca',
	'estao','deve','todo','ser','tambem','nao','quase','forma','qualquer','sem','nessa','ja','outro','outros','sao','ainda','parte','onde','tantos','todas',
	'existem','apresento','adiante','antes','depois','durante','mesmos','todos','causa','pode','prontos','nessas','nesses','proximo','ter','alguma','sido','ido',
	'subiu','pediu','chegou','existe','veio','vai','duas','entao','por que']
	# adicionar exceções ao stopword standard
	stopw.extend(addExcecoes)
	# remover palavras comuns da lista de palavras gerada a partir do texto informado
	palavras_sem_stopwords = [w for w in review if w not in stopw]
	# converter a lista de palavras num texto
	review = ' '.join(palavras_sem_stopwords)
	# gerar a nuvem de palavras
	wordcloud = WordCloud(width = 1366, height = 768, background_color=dia_noite).generate(str(review))
	plt.figure(figsize=(12,6))
	plt.imshow(wordcloud,interpolation='lanczos')
	plt.axis("off")
	plt.show()
