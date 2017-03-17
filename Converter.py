#coding: utf-8

import socket
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class ConversorIPv6(object):
    def __init__(self):
    
        builder = Gtk.Builder() #Instancia do Gtk
        builder.add_from_file("Converter.glade") #Função para carregar o arquivo
    
    
    	#Widget da janela principal
        self.window = builder.get_object("window1")

		#Widget campo da url    
        self.url_entry = builder.get_object("text_url_entry")

        #Widget textview dos ipv6
        self.ipv6_text = builder.get_object("ip_view")
    
    	#Widget de abertura do arquivo txt
        self.arquivos = builder.get_object("file_button")

        #Filtro do widger de arquivo
        filter = Gtk.FileFilter()
    	filter.set_name("Text")
    	filter.add_pattern("*.txt")
    	self.arquivos.add_filter(filter)
    	
    	#Obtendo o widget about com as informaçoes do programa
        self.about = builder.get_object("about_dialog")
        
    	#Exibindo a janela principal do programa
        self.window.show()
    
    	#Conectando os sinais(listeners) dos elementos
        builder.connect_signals({"Gtk_main_quit": Gtk.main_quit,
                            #Encerra o programa

                            "on_obter_ipv6_clicked": self.obter_ipv6,
                            #Botao para obter ipv6

                            "on_text_url_entry_activate": self.obter_ipv6,
                            #Ao clicar enter no campo, ele funciona como o botao

                            "on_about_activate": self.about_window,
                            #Botão ajuda
                                })
  
    def obterDominios(self, filename, ips):
    	arq = open(filename, 'r')

    	for linha in arq:
    		try:
    			ip = socket.getaddrinfo(linha.strip(), None, socket.AF_INET6)[0][4][0]
    		except:
    			ip = 'Dominio não encontrado'
    		ips.append(ip + '\n')

	
	#Funções do listener(sinais)
    def obter_ipv6(self, widget):
        
    	textbuffer = self.ipv6_text.get_buffer()
    	#Campo maior onde se encontrarão os ips

    	ips = []
    	#lista onde serão armazenados os dominios convertidos para ip

    	filename = self.arquivos.get_filename()
    	#Obtém o nome do arquivo do botão

        dominio = self.url_entry.get_text()
        #obtem o valor dentro do campo de texto de URL

        if dominio and dominio != 'Insira o URL aqui:':

	        try:
	        	ip = socket.getaddrinfo(dominio, None, socket.AF_INET6)[0][4][0] + '\n'
	        except:
	        	ip = 'Dominio não encontrado\n'
	    	ips.append(ip)
   
    	if filename != None:
    		self.obterDominios(filename, ips)

    	str_ips = ''

    	for i in ips:
   			str_ips += str(i)

    	textbuffer.set_text(str_ips)


        
    def about_window(self, widget):
        
        #Executando a Janela
        self.about.run()

        #Fechando a Janela
        self.about.hide()
        
if __name__ == "__main__":
    #Cria a instância do programa
    app = ConversorIPv6()
    
    #Função para manter a janela principal aberta
    Gtk.main() 