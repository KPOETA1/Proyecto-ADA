import sys
from timeit import default_timer as timer

# Clase Arbol Trie
# en caso de empate se retorna la palabra mayor palabra lexicograficamente

# funcion para obtener el valor maximo de un diccionario
def getMaxValue(d):
    for key in d:
        d[key] = d[key].number_of_words
    sortedDict = dict(sorted(d.items()))
    return max(sortedDict, key=d.get)

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

    # funcion para obtener las palabras con un prefijo
    def getWords(self, prefix):  # prefix: str
        current = self.root  # nodo actual
        current.number_of_words += 1
        for c in prefix:  # para cada caracter en el prefijo
            if c not in current.children:  # si no existe el caracter en el nodo actual
                return []  # retorna una lista vacia
            current = current.children[c]  # se mueve al nodo hijo
        # retorna la lista de palabras
        return self.getWordsAux(current, prefix)

     # Funcion recursiva para obtener las palabras
    def getWordsAux(self, node, prefix):    # node: TrieNode, prefix: str
        if node.isEnd:  # si es el final de la palabra
            return [prefix]  # retorna la palabra
        words = []  # lista de palabras
        for c in node.children:  # para cada hijo del nodo
            words += self.getWordsAux(node.children[c], prefix + c)
        return words  # retorna la lista de palabras

    # funcion para obtener el prefijo de una palabra
    def getPrefix(self, word):
        current = self.root
        prefix = ""
        for c in word:
            if c not in current.children:
                return prefix
            current = current.children[c]
            prefix += c
        return prefix

    # funcion para contar el numero de palabras con un prefijo
    def countPrefix(self, prefix):
        current = self.root
        for c in prefix:
            current = current.children[c]
        return current.number_of_words

    # funcion para recorrer el arbol
    def recorrerArbol(self, prefix):
        current = self.root
        for c in prefix:
            current = current.children[c]
            # si hay empate se retorna la palabra mayor lexicograficamente
        if not current.isEnd:
            prefix += getMaxValue(current.children.copy())
            return self.recorrerArbol(prefix)
        else:
            return prefix

    # funcion para obtener la palabra mas grande
    def getBiggestWord(self, word):
        current = self.root
        prefix = self.getPrefix(word)

        prefix = self.recorrerArbol(prefix)
        
        words = self.getWords(prefix)
        shortest = self.getShortestWord(words)
        # return self.getShortestWord(words)
        return shortest

    # funcion para obtener la palabra mas corta
    def getShortestWord(self, words):
        words.sort()
        shortest = words[0]
        for word in words:
            if len(word) < len(shortest):
                shortest = word
        return shortest


def resolver():
    trie = Trie()  # crear arbol trie

    # insertar lista de palabras
    with open('input.txt', 'r') as f:  # abre el archivo de texto
        instructions = []   # lista de instrucciones

        lines = f.read().splitlines()  # lee las lineas del archivo
        for line in lines:
            # se agrega la instruccion a la lista
            instructions.append(line.split(" "))

    path = 'output.txt'

    try:
        with open(path, 'r+') as f:
            f.truncate()
    except IOError:
        print('Failure')

    file = open('output.txt', 'w')  # abre el archivo de salida
    for instruction in instructions[1:]:  # para cada instruccion
        query_type = int(instruction[0])  # tipo de instruccion
        word = instruction[1]  # palabra

        if query_type == 1:  # si es de tipo 1
            trie.insert(word)  # se inserta la palabra
        elif query_type == 2:  # si es de tipo 2
            # escribe en el archivo de salida
            file.write(str(trie.getBiggestWord(word)) + "\n")


#analisis de la complejidad
#el algoritmo tiene una complejidad de O(n) donde n es el numero de palabras ya que se recorre la lista de palabras una sola vez