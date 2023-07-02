# coding: utf-8

class Compilador:

    def openFile(self):
        #Abrir .txt com expressões aritmeticas
        expressoes = open("expressoes.txt")
        linha = [" "]
        imprime = ''
        while linha != '':
            #Ler arquivo linha a Linha .txt
            linha = expressoes.readline().split(' ')
            if (linha == ['']):
                expressoes.close()
                break

            imprime += "O retorno do analizador ["+' '.join(linha[:])+"] e: "'\n'
            imprime += self.analizador_lexico(' '.join(linha[:]))
        return imprime
 
    def writeFile(self,resultado):
        busquedas = open("resultados.txt", "w")
        busquedas.write(resultado)
        busquedas.close()
  

    # O léxico aceita apenas números, operadores e variáveis ​​(em minúsculas)
    def analizador_lexico(self,elementos):
        #Pegar elemento por elemento
        caracteres = elementos.split(' ')
        i = 0
        cont = 0
        imprime = ""
        while i < len(caracteres):
            #Se é numero
            if caracteres[i].isdigit():
                cont += 1
                imprime += caracteres[i]+" E um Lexema mapeado em um token  " + " < id: " +str(cont)+ ">"'\n'

            # Se E um operador (+-*/)
            elif caracteres[i] == "*" or caracteres[i] == "+" or caracteres[i] == "-" or caracteres[i] == "/":
                if(caracteres[i] == "+"):
                    imprime += caracteres[i]+" E um operador de Adicao" + " <" + caracteres[i] + ">"'\n'
                if(caracteres[i] == "-"):
                    imprime += caracteres[i]+" E um operador de Subtracao" + " <" + caracteres[i] + ">"'\n'
                if(caracteres[i] == "*"):
                    imprime += caracteres[i]+" E um operador de Multiplicacao" + " <" + caracteres[i] + ">"'\n' 
                if(caracteres[i] == "/"):
                    imprime += caracteres[i]+" E um operador de Divisao" + " <" + caracteres[i] + ">"'\n'                   
            #Se é uma variavel (minusculas)
            elif caracteres[i].islower():
                cont += 1
                imprime += caracteres[i]+" E um Lexema" + " < id: "+str(cont)+ ">"'\n'
            #Se é um simbolo de atribuição    
            elif caracteres[i] == "=" or caracteres[i] == "+=" or caracteres[i] == "=+":
                imprime += caracteres[i]+" E um simbolo de atribuicao" + " <" + caracteres[i] + ">"'\n'    
            #Se é parentese de    
            elif caracteres[i] == "(" or caracteres[i] == ")" :
                if(caracteres[i] == "("):
                    imprime += caracteres[i]+" E um simbolo de abertura de um parentese" + " <" + caracteres[i] + ">"'\n' 
                if(caracteres[i] == ")"):
                    imprime += caracteres[i]+" E um simbolo de fechamento de um parentese" + " <" + caracteres[i] + ">"'\n'

            elif caracteres[i] == ';':
                imprime += caracteres[i]+"E um delimitador de fim de expressao"+ " <"+ caracteres[i] + ">"'\n'           
            #Não é um Lexema Reconhecido
            else:
                imprime += caracteres[i]+" Nao pertence aos leximas"'\n'
            i += 1       
        return imprime
    
def main():
    compiler = Compilador()
    saida = compiler.openFile()
    compiler.writeFile(saida)

if __name__ == "__main__":
    main()
