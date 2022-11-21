def crie_matriz(n_linhas, n_colunas, valor):
    ''' (int, int, valor) -> matriz

    Cria e retorna uma matriz com n_linhas e n_colunas
    em que cada elemento dentro do desenho é igual ao valor.
    '''
    aresta=6 #tamanho das arestas do quadrado,min 3
    linha=4 #começo da linha do quadrado
    coluna=5 #começo da coluna do quadrado
    inicio=4 #inicio da forma
    maxc=aresta+inicio #coluna maxima
    #i=coluna atual
    #j=linha atual
    adicao=0 #variavel para o somatorio
    matriz = [] # lista vazia
    for i in range(n_linhas): 
        linha = [] 
        for j in range(n_colunas): #espaço sem desenho
            if i < inicio: 
                linha.append(0)
            if i>=inicio and i < maxc: #quadrado
                if ((j==i+1) or ((maxc+inicio)==(i+j))):
                    linha.append(0) #diagonal principal ou secundária do monitor
                elif (j <= inicio) or (j > maxc):
                    linha.append(0) #fora do desenho
                else:
                    linha.append(valor) #dentro do desenho
                    adicao=adicao+valor #parte do calculo do somatorio
                    
            if i>=maxc: #retangulo
                if (j<(aresta-inicio)) or ( j>=(maxc+inicio)): #fora do desenho
                    linha.append(0)
                else:
                    linha.append(valor) #dentro do desenho
                    adicao=adicao+valor #parte do calculo do somatorio
        matriz.append(linha)
        
    for o in range (n_linhas): 
        print(matriz[o]) #printa toda a matriz
    print("Resultado da somatório:",adicao) #printa o resultado do somatorio
    
    


    return matriz
#-----------------------
A = crie_matriz(16,16,1) #exagerei com os comentarios?