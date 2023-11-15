import openai
import time  # Necesario para manejar las pausas entre solicitudes

# Resto del código

openai.api_key = ''

base_de_datos_temporal = {
    "C001": {
        "name": "Introducción a la programación",
        "length": "8 semanas",
        "price": 49.99,
        "modality": "En línea",
        "content": "Conceptos básicos de programación",
        "description": "Aprende los fundamentos de la programación en este curso introductorio.",
        "idInstitution": 1,
        "link": "https://example.com/courses/c001",
        "difficulty": "facil",
    },
    "C002": {
        "name": "Algoritmos avanzados",
        "length": "12 semanas",
        "price": 79.99,
        "modality": "Presencial",
        "content": "Algoritmos avanzados y estructuras de datos",
        "description": "Explora algoritmos avanzados y técnicas de optimización en este curso avanzado.",
        "idInstitution": 2,
        "link": "https://example.com/courses/c002",
        "difficulty": "dificil",
    },
    
}

TIEMPO_ENTRE_SOLICITUDES = 2

def obtener_respuesta_chatgpt(descripcion, nivel):
    prompt = f"Usuario: Quiero aprender sobre {descripcion}. Mi nivel de dificultad es {nivel}."

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
            stop=None
        )

        if response and response.choices and response.choices[0].text:
            return response.choices[0].text.strip()
        else:
            print("La respuesta de OpenAI está vacía.")
            return "No se pudo obtener una respuesta en este momento."

    except openai.error.OpenAIError as e:
        print(f"Error al llamar a la API de OpenAI: {str(e)}")
        return "No se pudo obtener una respuesta en este momento."


cache_respuestas = {}

def obtener_respuesta_chatgpt_cached(descripcion, nivel):

    if (descripcion, nivel) in cache_respuestas:
        return cache_respuestas[(descripcion, nivel)]

    respuesta_chatgpt = obtener_respuesta_chatgpt(descripcion, nivel)

    cache_respuestas[(descripcion, nivel)] = respuesta_chatgpt

    return respuesta_chatgpt

def filtrar_cursos(conjunto_cursos, nivel):
    cursos_recomendados = []

    for curso_id, curso_info in conjunto_cursos.items():
        respuesta_chatgpt = obtener_respuesta_chatgpt_cached(curso_info['description'], nivel)

        curso_recomendado = {
            'nombre': curso_info['name'],
            'tiempo': curso_info['length'],
            'modalidad': curso_info['modality'],
            'precio': curso_info['price'],
            'descripcion': curso_info['description'],
            'dificultad': curso_info['difficulty'],
            'institution': curso_info['idInstitution'],
            'link':curso_info['link'],
            'respuesta_chatgpt': respuesta_chatgpt
        }

        cursos_recomendados.append(curso_recomendado)

    return cursos_recomendados

def powering(conjunto_cursos, nivel):
    cursos=  filtrar_cursos(conjunto_cursos, nivel)
    cursos_finales = {'facil':[],'intermedio':[], 'dificil': []}

    for i in cursos:
        cursos_finales[i['dificultad']].append(i)

    return cursos_finales

descripcion_usuario = input("Ingrese la descripción de lo que quiere aprender: ")
nivel_usuario = input("Ingrese su nivel de dificultad: ")

cursos_recomendados = powering(base_de_datos_temporal, nivel_usuario)



print("Cursos recomendados:")
print(cursos_recomendados)