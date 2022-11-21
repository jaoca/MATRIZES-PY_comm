def crie_matriz(n_linhas, n_colunas, valor):
    ''' (int, int, valor) -> matriz

    Cria e retorna uma matriz com n_linhas e n_colunas
    em que cada elemento dentro do desenho é igual ao valor.
    '''
    aresta=24 #tamanho das arestas do quadrado,min 3
    linha=4 #começo da linha do quadrado
    coluna=5 #começo da coluna do quadrado
    altura=12
    inicio=10 #inicio da forma
    maxc=aresta+inicio #coluna maxima
    maxt=inicio+(aresta/2)
    maxa=aresta+altura
    #i=coluna atual
    #j=linha atual
    adicao=0 #variavel para o somatorio
    matriz = [] # lista vazia
    for i in range(n_linhas): 
        linha = [] 
        for j in range(n_colunas): #espaço sem desenho
            if i < altura: 
                if ((j+i<maxt) or (j-i>maxt+1)):
                    linha.append(0)
                else:
                    linha.append(1)
            elif i>=altura and i < maxa: #quadrado
                if (j <= inicio) or (j > maxc):
                    linha.append(0) #fora do desenho
                else:
                    linha.append(valor) #dentro do desenho
                    adicao=adicao+valor #parte do calculo do somatorio
                    
            else:
                    linha.append(0)
        matriz.append(linha)
        
    for o in range (n_linhas): 
        print(matriz[o]) #printa toda a matriz
    print("Resultado da somatório:",adicao) #printa o resultado do somatorio
    
    


    return matriz
#-----------------------
A = crie_matriz(43,43,1) #exagerei com os comentarios?