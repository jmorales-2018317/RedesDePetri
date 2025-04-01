from graphviz import Digraph
import os

def crear_diagrama_base():
    """Crea el diagrama base de la Red de Petri para el semáforo"""
    dot = Digraph(comment='Red de Petri para Semáforo', format='png')
    dot.attr(rankdir='LR', size='8,5')
    
    # Configuración nodos
    dot.attr('node', shape='circle', width='1.5', fixedsize='true')
    
    # Plazas 
    dot.node('P_R1', 'P_R1\nRojo1', style='filled', fillcolor='red', fontcolor='white')
    dot.node('P_G1', 'P_G1\nVerde1', style='filled', fillcolor='green')
    dot.node('P_Y1', 'P_Y1\nAmarillo1', style='filled', fillcolor='yellow')
    dot.node('P_R2', 'P_R2\nRojo2', style='filled', fillcolor='red', fontcolor='white')
    dot.node('P_G2', 'P_G2\nVerde2', style='filled', fillcolor='green')
    dot.node('P_Y2', 'P_Y2\nAmarillo2', style='filled', fillcolor='yellow')
    
    # Transiciones
    dot.attr('node', shape='rectangle', width='1', height='0.5', fixedsize='true', fillcolor='lightgray', style='filled')
    dot.node('T_1', 'T_1')
    dot.node('T_2', 'T_2')
    dot.node('T_3', 'T_3')
    dot.node('T_4', 'T_4')
    dot.node('T_5', 'T_5')
    dot.node('T_6', 'T_6')
    
    # Arcos
    dot.edge('P_R1', 'T_1')
    dot.edge('T_1', 'P_G1')
    dot.edge('P_G1', 'T_2')
    dot.edge('T_2', 'P_Y1')
    dot.edge('P_Y1', 'T_3')
    dot.edge('T_3', 'P_R1')
    
    dot.edge('P_R2', 'T_4')
    dot.edge('T_4', 'P_G2')
    dot.edge('P_G2', 'T_5')
    dot.edge('T_5', 'P_Y2')
    dot.edge('P_Y2', 'T_6')
    dot.edge('T_6', 'P_R2')
    
    # Reglas de sincronización (líneas punteadas)
    dot.edge('P_G1', 'P_R2', style='dotted', dir='none')
    dot.edge('P_G2', 'P_R1', style='dotted', dir='none')
    
    return dot

def generar_diagramas_completos():
    """Genera los 7 diagramas requeridos"""
    # Crear directorio de salida si no existe
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # 1. Diagrama base sin tokens
    dot_base = crear_diagrama_base()
    dot_base.render('output/semaforo_base', view=False)
    print("Diagrama base generado: semaforo_base.png")
    
    # Diccionario con los colores de cada plaza
    colores_plazas = {
        'P_R1': 'red',
        'P_G1': 'green',
        'P_Y1': 'yellow',
        'P_R2': 'red',
        'P_G2': 'green',
        'P_Y2': 'yellow'
    }
    
    # Función para crear diagramas con tokens
    def crear_diagrama_con_tokens(nombre_archivo, plazas_con_tokens):
        dot = Digraph(comment='Red de Petri para Semáforo', format='png')
        dot.attr(rankdir='LR', size='8,5')
        
        # Recrear todas las plazas
        for plaza in ['P_R1', 'P_G1', 'P_Y1', 'P_R2', 'P_G2', 'P_Y2']:
            dot.node(plaza, 
                    f'{plaza}\n{"Rojo" if "R" in plaza else "Verde" if "G" in plaza else "Amarillo"}{plaza[-1]}',
                    style='filled',
                    fillcolor=colores_plazas[plaza],
                    fontcolor='white' if 'R' in plaza else 'black',
                    xlabel='●' if plaza in plazas_con_tokens else '')
        
        # Recrear todas las transiciones
        dot.attr('node', shape='rectangle', width='1', height='0.5', fixedsize='true', fillcolor='lightgray', style='filled')
        for transicion in ['T_1', 'T_2', 'T_3', 'T_4', 'T_5', 'T_6']:
            dot.node(transicion, transicion)
        
        # Recrear todos los arcos
        dot.edge('P_R1', 'T_1')
        dot.edge('T_1', 'P_G1')
        dot.edge('P_G1', 'T_2')
        dot.edge('T_2', 'P_Y1')
        dot.edge('P_Y1', 'T_3')
        dot.edge('T_3', 'P_R1')
        
        dot.edge('P_R2', 'T_4')
        dot.edge('T_4', 'P_G2')
        dot.edge('P_G2', 'T_5')
        dot.edge('T_5', 'P_Y2')
        dot.edge('P_Y2', 'T_6')
        dot.edge('T_6', 'P_R2')
        
        # Reglas de sincronización
        dot.edge('P_G1', 'P_R2', style='dotted', dir='none')
        dot.edge('P_G2', 'P_R1', style='dotted', dir='none')
        
        dot.render(f'output/{nombre_archivo}', view=False)
        print(f"Diagrama generado: {nombre_archivo}.png")
    
    # Generar los diagramas con tokens
    crear_diagrama_con_tokens('semaforo_inicial', ['P_R1', 'P_R2'])
    crear_diagrama_con_tokens('semaforo_t1', ['P_G1', 'P_R2'])
    crear_diagrama_con_tokens('semaforo_t2', ['P_Y1', 'P_R2'])
    crear_diagrama_con_tokens('semaforo_t3', ['P_R1', 'P_R2'])
    crear_diagrama_con_tokens('semaforo_t4', ['P_R1', 'P_G2'])
    crear_diagrama_con_tokens('semaforo_t5', ['P_R1', 'P_Y2'])
    crear_diagrama_con_tokens('semaforo_t6', ['P_R1', 'P_R2'])

if __name__ == '__main__':
    generar_diagramas_completos()
    print("¡Todos los diagramas han sido generados exitosamente en la carpeta 'output'!")
