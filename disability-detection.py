# --------------------------------------------------------------------------
import os

# Preguntas divididas por dominios
domains = {
     "Cognición": [
        "¿Tiene dificultades para recordar eventos recientes?",
        "¿Se siente confundido con frecuencia en entornos nuevos o poco familiares?",
        "¿Tiene dificultades para concentrarse en tareas durante períodos prolongados?",
        "¿Tiene problemas para comprender información compleja?",
        "¿Olvida frecuentemente realizar tareas importantes?",
        "¿Tiene problemas para resolver problemas o tomar decisiones?",
        "¿Se siente desorientado en lugares familiares?",
        "¿Tiene dificultades para planificar actividades cotidianas?",
        "¿Tiene problemas para seguir instrucciones múltiples?",
        "¿Se distrae fácilmente incluso en entornos tranquilos?"
    ],
    "Movilidad": [
        "¿Tiene dificultades para caminar largas distancias?",
        "¿Tiene problemas para subir o bajar escaleras sin ayuda?",
        "¿Tiene dificultades para levantarse de una silla sin apoyo?",
        "¿Tiene problemas para agacharse o arrodillarse?",
        "¿Experimenta dolor al moverse o caminar?",
        "¿Tiene problemas para mantenerse de pie durante largos períodos?",
        "¿Usa dispositivos de asistencia para moverse, como bastones o sillas de ruedas?",
        "¿Tiene dificultad para moverse en espacios reducidos?",
        "¿Se siente inseguro al caminar en superficies irregulares?",
        "¿Evita actividades físicas debido a limitaciones de movilidad?"
    ],
    "Cuidado personal": [
        "¿Tiene dificultades para bañarse sin ayuda?",
        "¿Tiene problemas para vestirse de manera independiente?",
        "¿Necesita ayuda para alimentarse?",
        "¿Tiene problemas para realizar tareas de higiene personal?",
        "¿Requiere asistencia para usar el baño?",
        "¿Tiene dificultades para lavarse los dientes o peinarse?",
        "¿Tiene problemas para preparar sus comidas diarias?",
        "¿Necesita ayuda para mantener su espacio personal limpio?",
        "¿Tiene problemas para recordar tomar medicamentos?",
        "¿Evita actividades de cuidado personal debido a dolor o limitaciones físicas?"
    ],
    "Relaciones": [
        "¿Tiene dificultades para mantener amistades?",
        "¿Se siente incomprendido por sus emociones en público?",
        "¿Tiene problemas para iniciar conversaciones?",
        "¿Evita eventos sociales debido a ansiedad?",
        "¿Se siente rechazado en entornos grupales?",
        "¿Tiene problemas para trabajar con otros en equipo?",
        "¿Siente que su discapacidad afecta su relación familiar?",
        "¿Tiene problemas para expresar sus necesidades emocionales?",
        "¿Evita interacciones debido al miedo al juicio social?",
        "¿Tiene dificultades para relacionarse con compañeros de trabajo o estudio?"
    ],
    "Actividades de la vida diaria": [
        "¿Tiene problemas para realizar compras en el mercado?",
        "¿Tiene dificultades para realizar tareas domésticas?",
        "¿Necesita ayuda para administrar sus finanzas personales?",
        "¿Tiene problemas para leer o escribir documentos?",
        "¿Tiene dificultades para usar dispositivos electrónicos?",
        "¿Evita salir solo por miedo a caídas o desorientación?",
        "¿Tiene problemas para manejar situaciones de emergencia?",
        "¿Se siente incapaz de participar en actividades recreativas?",
        "¿Tiene dificultades para mantener un horario regular?",
        "¿Evita actividades al aire libre debido a limitaciones físicas o psicológicas?"
    ],
    "Participación": [
        "¿Tiene problemas para participar en actividades comunitarias?",
        "¿Siente que su discapacidad afecta su trabajo o estudios?",
        "¿Evita lugares concurridos por estrés o ansiedad?",
        "¿Tiene dificultades para participar en eventos familiares?",
        "¿Se siente excluido en entornos grupales?",
        "¿Evita viajar debido a problemas de movilidad?",
        "¿Tiene problemas para contribuir en proyectos comunitarios?",
        "¿Siente que su discapacidad limita sus oportunidades de desarrollo?",
        "¿Se siente incapaz de expresar sus opiniones en público?",
        "¿Evita actividades sociales por miedo al juicio?"
    ],

    # Seccion para detectar discapacidad fisica
    "Fisica": [
        "¿Tiene dificultades para caminar largas distancias?",
        "¿Tiene problemas para subir o bajar escaleras sin ayuda?",
        "¿Tiene dificultades para levantarse de una silla sin apoyo?",
        "¿Tiene problemas para agacharse o arrodillarse?",
        "¿Experimenta dolor al moverse o caminar?",
        "¿Tiene problemas para mantenerse de pie durante largos períodos?",
        "¿Usa dispositivos de asistencia para moverse, como bastones o sillas de ruedas?",
        "¿Tiene dificultad para moverse en espacios reducidos?",
        "¿Se siente inseguro al caminar en superficies irregulares?",
        "¿Evita actividades físicas debido a limitaciones de movilidad?"
    ],

    # Seccion para detectar discapacidad Visual
    "Visual": [
        "¿Tiene dificultades para leer textos pequeños o lejanos?",
        "¿Tiene problemas para reconocer rostros familiares?",
        "¿Experimenta visión borrosa o doble con frecuencia?",
        "¿Tiene dificultades para ver en entornos con poca luz?",
        "¿Necesita lentes correctivos para actividades diarias?",
        "¿Tiene problemas para seguir objetos en movimiento?",
        "¿Siente fatiga visual después de actividades prolongadas?",
        "¿Tiene dificultades para leer señales o carteles?",
        "¿Evita actividades visuales como la lectura o el cine?",
        "¿Tiene problemas para identificar colores o contrastes?"
    ],

    # Seccion para detectar discapacidad Auditiva
    "Auditiva": [
        "¿Tiene dificultades para escuchar conversaciones en entornos ruidosos?",
        "¿Tiene problemas para entender el habla clara o lentamente?",
        "¿Experimenta zumbidos o pitidos en los oídos?",
        "¿Necesita aumentar el volumen de la televisión o la radio?",
        "¿Tiene dificultades para seguir instrucciones verbales?",
        "¿Siente que los demás le hablan en voz baja?",
        "¿Tiene problemas para mantener conversaciones telefónicas?",
        "¿Evita eventos sociales debido a problemas de audición?",
        "¿Tiene dificultades para localizar la fuente de sonidos?",
        "¿Experimenta dolor o malestar en los oídos con frecuencia?"
    ],

    # Seccion para detectar discapacidad Cognitiva (Intelectual)
    "Cognitiva": [
        "¿Tiene dificultades para recordar eventos recientes?",
        "¿Se siente confundido con frecuencia en entornos nuevos o poco familiares?",
        "¿Tiene dificultades para concentrarse en tareas durante períodos prolongados?",
        "¿Tiene problemas para comprender información compleja?",
        "¿Olvida frecuentemente realizar tareas importantes?",
        "¿Tiene problemas para resolver problemas o tomar decisiones?",
        "¿Se siente desorientado en lugares familiares?",
        "¿Tiene dificultades para planificar actividades cotidianas?",
        "¿Tiene problemas para seguir instrucciones múltiples?",
        "¿Se distrae fácilmente incluso en entornos tranquilos?"
    ],

    # Seccion para detectar discapacidad Psicosocial (Mental)
    "Psicosocial": [
        "¿Tiene dificultades para mantener amistades?",
        "¿Se siente incomprendido por sus emociones en público?",
        "¿Tiene problemas para iniciar conversaciones?",
        "¿Evita eventos sociales debido a ansiedad?",
        "¿Se siente rechazado en entornos grupales?",
        "¿Tiene problemas para trabajar con otros en equipo?",
        "¿Siente que su discapacidad afecta su relación familiar?",
        "¿Tiene problemas para expresar sus necesidades emocionales?",
        "¿Evita interacciones debido al miedo al juicio social?",
        "¿Tiene dificultades para relacionarse con compañeros de trabajo o estudio?"
    ],

    # Seccion para detectar discapacidad Sordoceguera
    "Sordoceguera": [
        "¿Tiene dificultades para comunicarse con otros de manera efectiva?",
        "¿Necesita asistencia para realizar tareas cotidianas?",
        "¿Tiene problemas para identificar objetos o personas sin ayuda?",
        "¿Siente que su discapacidad afecta su independencia?",
        "¿Tiene dificultades para navegar en entornos desconocidos?",
        "¿Requiere apoyo para actividades de la vida diaria?",
        "¿Tiene problemas para acceder a información visual o auditiva?",
        "¿Evita situaciones nuevas o desconocidas debido a su discapacidad?",
        "¿Siente que su discapacidad limita su participación social?",
        "¿Tiene dificultades para expresar sus necesidades o deseos?"
    ],

    # Seccion para detectar discapacidad Multiple
    "Multiple": [
        "¿Tiene dificultades para realizar tareas cotidianas sin ayuda?",
        "¿Necesita asistencia para moverse o comunicarse?",
        "¿Tiene problemas para mantener relaciones interpersonales?",
        "¿Siente que su discapacidad afecta su calidad de vida?",
        "¿Tiene dificultades para acceder a servicios de apoyo?",
        "¿Requiere apoyo para actividades de la vida diaria?",
        "¿Tiene problemas para participar en eventos sociales o comunitarios?",
        "¿Evita situaciones nuevas o desconocidas debido a su discapacidad?",
        "¿Siente que su discapacidad limita su independencia?",
        "¿Tiene dificultades para expresar sus necesidades o deseos?"
    ]
}

options = [
    "1. Nunca",
    "2. Raramente",
    "3. A veces",
    "4. Frecuentemente",
    "5. Siempre"
]

# Ponderaciones para las respuestas
input_to_score = {
    1: 0.0,  # Nunca
    2: 0.53,  # Raramente
    3: 1.03,  # A veces
    4: 1.54,  # Frecuentemente
    5: 2.08   # Siempre
}

# Mapeo de dominios a tipos de discapacidad
domain_to_disability = {
    "Cognición": "Discapacidad Cognitiva",
    "Movilidad": "Discapacidad Física",
    "Cuidado personal": "Discapacidad Física",
    "Relaciones": "Discapacidad Psicosocial",
    "Actividades de la vida diaria": "Discapacidad Física",
    "Participación": "Discapacidad Psicosocial",
    "Fisica": "Discapacidad Física",
    "Visual": "Discapacidad Visual",
    "Auditiva": "Discapacidad Auditiva",
    "Cognitiva": "Discapacidad Cognitiva",
    "Psicosocial": "Discapacidad Psicosocial",
    "Sordoceguera": "Discapacidad Sordoceguera",
    "Multiple": "Discapacidad Múltiple"
}

# Ajustar umbral para clasificar como discapacidad
disability_threshold = 1.5

# Función para determinar discapacidad según puntajes ponderados promedios
def determine_disability(scores):
    disabilities = {}
    for domain, score in scores.items():
        if score >= disability_threshold:
            disability = domain_to_disability[domain]
            if disability in disabilities:
                disabilities[disability] = (disabilities[disability] + score) / 2
            else:
                disabilities[disability] = score
    return disabilities


# Ejecución del cuestionario
def run_questionnaire():
    scores = {domain: 0.0 for domain in domains}
    print("Responda las siguientes preguntas con las opciones:")
    for domain, questions in domains.items():
        print(f"\n--- {domain} ---")
        for question in questions:
            print(question)
            for option in options:
                print(option)
            while True:
                try:
                    response = int(input("Ingrese su respuesta (1-5): "))
                    if response in input_to_score:
                        scores[domain] += input_to_score[response]
                        break
                    else:
                        print("Respuesta inválida. Por favor, ingrese un número entre 1 y 5.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
    return scores

# Iniciar el cuestionario y mostrar resultados
scores = run_questionnaire()
disabilities = determine_disability(scores)

# Imprimir puntuaciones por dominio
print("\n--- Puntuaciones por Dominio ---")
for domain, score in scores.items():
    print(f"{domain}: {score:.2f}")

print("\n--- Resultados ---")
if disabilities:
    print("Se detectaron las siguientes posibles discapacidades:")
    for disability, score in disabilities.items():
        print(f"- {disability} (Puntaje promedio: {score:.2f})")
else:
    print("No se detectaron discapacidades significativas.")