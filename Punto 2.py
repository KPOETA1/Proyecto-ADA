import sys

# Clase Arbol Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.number_of_words = 0
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):  # word: str
        current = self.root  # nodo actual
        for c in word:  # para cada caracter en la palabra
            if c not in current.children:  # si no existe el caracter en el nodo actual
                current.children[c] = TrieNode()  # se crea un nuevo nodo
            current = current.children[c]  # se mueve al nodo hijo
            current.number_of_words += 1
        current.isEnd = True  # se marca como final de la palabra
    

    def getWords(self, prefix):  # prefix: str
        current = self.root  # nodo actual
        current.number_of_words += 1
        for c in prefix:  # para cada caracter en el prefijo
            if c not in current.children:  # si no existe el caracter en el nodo actual
                return []  # retorna una lista vacia
            current = current.children[c]  # se mueve al nodo hijo
        # retorna la lista de palabras
        return self.getWordsAux(current, prefix)
    
    # funcion para buscar segun la palabra cual es el prefijo mas grande
    def getPrefix(self, word):
        current = self.root
        prefix = ""
        for c in word:
            if c not in current.children:
                return prefix
            current = current.children[c]
            prefix += c
        return prefix
    
    def getBiggestWord(self, word):
        current = self.root
        prefix = self.getPrefix(word)

        for c in prefix:
            current = current.children[c]
        
        #print(current.number_of_words)
        if current.number_of_words > 1:
            count = 1
            letter = ""
            for c in current.children:
                if current.children[c].number_of_words > count:
                    count = current.children[c].number_of_words
                    letter = c
            prefix += letter

        #print (prefix)
        words = self.getWords(prefix)
        shortest = self.getShortestWord(words)
        #return self.getShortestWord(words)
        return shortest


    def getShortestWord(self, words):
        words.sort()
        shortest = words[0]
        for word in words:
            if len(word) < len(shortest):
                shortest = word
        return shortest

    # Funcion recursiva para obtener las palabras
    def getWordsAux(self, node, prefix):    # node: TrieNode, prefix: str
        if node.isEnd:  # si es el final de la palabra
            return [prefix]  # retorna la palabra
        words = []  # lista de palabras
        for c in node.children:  # para cada hijo del nodo
            words += self.getWordsAux(node.children[c], prefix + c)
        return words  # retorna la lista de palabras
    
    # contador de palabras con el mismo prefijo countPrefix
    def countPrefix(self, prefix):
        current = self.root
        for c in prefix:
            current = current.children[c]
        return current.number_of_words

def main():
    trie = Trie()  # crear arbol trie

    # insertar lista de palabras
    with open('PROYECTO/Proyecto-ADA/input.txt', 'r') as f:  # abre el archivo de texto
        instructions = []   # lista de instrucciones
        lines = f.read().splitlines()  # lee las lineas del archivo
        for line in lines:
            # se agrega la instruccion a la lista
            instructions.append(line.split(" "))

    for instruction in instructions[1:]:  # para cada instruccion
        query_type = int(instruction[0])  # tipo de instruccion
        word = instruction[1]  # palabra

        if query_type == 1:  # si es de tipo 1
            trie.insert(word)  # se inserta la palabra
        elif query_type == 2:  # si es de tipo 2
            # for i in trie.getWords(word): 
            #     print(i)
            #escribe en el archivo de salida
            with open('PROYECTO/Proyecto-ADA/output.txt', 'a') as f:
                f.write(str(trie.getBiggestWord(word)) + "\n")
            #print(trie.getBiggestWord(word))

if __name__ == "__main__":
    main()