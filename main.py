class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
    
    def indice_hash(self, valor):
        # Calcula o índice usando com o resto
        return valor % self.tamanho
    
    def inserir(self, valor):
        indice =  self.indice_hash(valor)

        #Verifica se o elemento já está inserido na tabela
        if valor in self.tabela:
            print(f'Elemento {valor} já está inserido!\n')
            return
       
        #Verifica se o índice já está ocupado
        while self.tabela[indice] is not None:
            indice = (indice + 1) % self.tamanho
   
        self.tabela[indice] = valor
        return print(f'Elemento {valor} inserido com sucesso!\n')

    def remover(self, valor):
        indice = self.indice_hash(valor)
        
        #Se o valor estiver na posição inicial coloca como none
        if self.tabela[indice] == valor:
            self.tabela[indice] = None
            print(f'Elemento {valor} removido com sucesso!\n')

        else:
            #Se não percorre mais um indice
            indice_inicial = indice
            indice = (indice + 1) % self.tamanho
            
            #Verifica se o indice não é vazio e o indice é diferente do indice inicial 
            while self.tabela[indice] is not None and indice != indice_inicial:
                if self.tabela[indice] == valor:
                    self.tabela[indice] = None
                    return  print(f'Elemento {valor} removido com sucesso!\n')
                indice = (indice + 1) % self.tamanho
            
            print(f'Elemento {valor} não está presente na Tabela Hash\n')
    
    def consulta(self, valor):
        indice = self.indice_hash(valor)
        
        while self.tabela[indice] is not None:
            if self.tabela[indice] == valor:
                return  print(f'Elemento {valor} está presente na Tabela Hash\n')
            indice = (indice + 1) % self.tamanho

        return  print(f'Elemento {valor} não está presente na Tabela Hash\n')
    
    def imprimir(self):
        for indice, elemento in enumerate(self.tabela):
            if elemento is not None:
                print(f'Índice {indice}: {elemento}')
            else:
                print(f'Índice {indice}: Vazio')
        print("\n")

    def uniao(self, conjunto_b):
        conjunto_novo = TabelaHash(self.tamanho)
        
        # Adicionar elementos do conjunto atual ao novo conjunto
        for elemento in self.tabela:
            if elemento is not None:
                conjunto_novo.inserir(elemento)

        # Adicionar elementos do segundo conjunto ao novo conjunto
        for elemento in conjunto_b.tabela:
            if elemento is not None:
                conjunto_novo.inserir(elemento)

        return conjunto_novo

    def interseccao(self, conjunto_b):
        conjunto_novo = TabelaHash(self.tamanho)
        
        for elemento in self.tabela:
            if elemento is not None and elemento in conjunto_b.tabela:
            #verifica se o elemento esta no conjunto b
                conjunto_novo.inserir(elemento)

        return conjunto_novo
    
    def diferenca(self, conjunto_b):
        conjunto_novo = TabelaHash(self.tamanho)
        
        for elemento in self.tabela:
            #verifica se o elemento não está presenta no conjunto b e insere
            if elemento is not None and elemento not in conjunto_b.tabela:
                conjunto_novo.inserir(elemento)

        for elemento in conjunto_b.tabela:
            #verifica se o elemento não está presenta no conjunto atual e insere
            if elemento is not None and elemento not in self.tabela:
                conjunto_novo.inserir(elemento)

        return conjunto_novo    
    

# Uso
#Criando o tamanho da tabela e ambos conjutos
tamanho_da_tabela = 10
conjunto1 = TabelaHash(tamanho_da_tabela)
conjunto2 = TabelaHash(tamanho_da_tabela)


#fazendo operações de inserção, remoção e consulta dos conjuntos
conjunto1.inserir(1)
conjunto1.inserir(2)
conjunto1.inserir(3)
conjunto2.consulta(2)

conjunto2.inserir(3)
conjunto2.inserir(4)
conjunto2.inserir(5)
conjunto2.inserir(6)
conjunto2.remover(6)
conjunto2.consulta(6)


#fazendo união, intersecção e diferença dos conjutos e imprimindo cada
uniao = conjunto1.uniao(conjunto2)
print("União:")
uniao.imprimir()

interseccao = conjunto1.interseccao(conjunto2)
print("Intersecção:")
interseccao.imprimir()

diferenca = conjunto1.diferenca(conjunto2)
print("Diferença:")
diferenca.imprimir()