from graphviz import Digraph

dot = Digraph(comment='Red de Petri para "aprobado"')

# Lugares (círculos)
places = ['Inicio', 'Letra', 'A', 'P', 'R', 'O', 'B', 'A2', 'D', 'O2', 'Fin', 'Error']
for p in places:
    dot.node(p, p, shape='circle' if p not in ['Fin', 'Error'] else 'doublecircle')

# Transiciones (rectángulos)
transitions = [f'T_{i}' for i in range(1, 11)]
for t in transitions:
    dot.node(t, t, shape='box')

# Conexiones (similar al grafo de referencia)
connections = [
    ('Inicio', 'T_1'), ('T_1', 'Letra'), ('Letra', 'T_2'),
    ('T_2', 'A'), ('T_2', 'T_3'), ('T_3', 'Error'),
    ('A', 'T_4'), ('T_4', 'P'), ('P', 'T_5'),
    ('T_5', 'R'), ('R', 'T_6'), ('T_6', 'O'),
    ('O', 'T_7'), ('T_7', 'B'), ('B', 'T_8'),
    ('T_8', 'A2'), ('A2', 'T_9'), ('T_9', 'D'),
    ('D', 'T_10'), ('T_10', 'O2'), ('O2', 'Fin')
]

for src, dst in connections:
    dot.edge(src, dst)

dot.render('red_aprobado_simplificado', format='png', view=True)
