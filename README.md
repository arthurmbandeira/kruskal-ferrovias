# Algoritmo de Kruskal
#### Aplicação: geração de uma árvore geradora mínima para conectar cidades do Estado do Paraná através de ferrovias

## Execução
O programa está implementado em Python 3 e deve ser executado da seguinte forma:
```bash
$ ./main.py -f entradas/<arquivo_de_entrada.txt>
```
ou
```python
$ python3 main.py -f entradas/<arquivo_de_entrada.txt>
```


O arquivo de entrada deve estar no formato:
```
3 # numero de vertices
3 # numero de arestas
A B 1 # vertice, vertice, peso da aresta
A C 2
B C 3
```

Exemplos encontram-se na pasta `entradas`

Para gerar as imagens, a ferramenta `graphviz` foi utilizada. O comando para geração das imagens de saída é:
```
$ dot -Tpng ../<arquivo.dot> > <imagem_de_saida.png>
```
