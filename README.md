# Dupla_LucasAvelar_MatheusSantos_Grafos

Repositório com soluções de problemas de grafos do LeetCode.

## Estrutura do Repositório

```
/
  README.md
  problems/
    leetcode_269_alien_dictionary.py
    leetcode_847_shortest_path_visiting_all_nodes.py
    leetcode_2127_maximum_employees_meeting.py
```

## Problemas

### LeetCode 269 - Alien Dictionary
- **Tema:** Ordenação Topológica (Topological Sort)
- **Descrição:** Determina a ordem das letras em um dicionário alienígena
- **Abordagem:** Algoritmo de Kahn (BFS) para ordenação topológica

### LeetCode 847 - Shortest Path Visiting All Nodes
- **Tema:** BFS com máscara de bits
- **Descrição:** Encontra o caminho mais curto que visita todos os nós de um grafo
- **Abordagem:** BFS com estados representados por (nó atual, máscara de visitados)

### LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
- **Tema:** Detecção de ciclos em grafos funcionais
- **Descrição:** Encontra o número máximo de funcionários que podem ser convidados para uma reunião
- **Abordagem:** Detecção de ciclos + extensão de cadeias

## Como Executar

```bash
python3 problems/leetcode_269_alien_dictionary.py
python3 problems/leetcode_847_shortest_path_visiting_all_nodes.py
python3 problems/leetcode_2127_maximum_employees_meeting.py
```