import os

# Preguntas divididas por dominios
domains = {
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
}

options = [
    "1. Nunca",
    "2. Raramente",
    "3. A veces",
    "4. Frecuentemente",
    "5. Siempre"
]

# Mapeo de dominios a tipos de discapacidad según la Clasificación Internacional del Funcionamiento, de la Discapacidad y de la Salud (CIF)

# Dominios segun las preguntas
domain_to_disability = {
    'Fisica': "Discapacidad Física",
    'Visual': "Discapacidad Visual",
    'Auditiva': "Discapacidad Auditiva",
    'Cognitiva': "Discapacidad Cognitiva",
    'Psicosocial': "Discapacidad Psicosocial",
    'Sordoceguera': "Discapacidad Sensorial",
}

# Mapeo de la entrada del usuario a los nuevos puntajes
input_to_score = {
    1: 0.00,  # Nunca
    2: 0.55,  # Raramente
    3: 1.05,  # A veces
    4: 1.55,  # Frecuentemente
    5: 2.55   # Siempre
}

# Determinar el umbral para la discapacidad
threshold = 8.50

# Función para determinar si hay o no discapacidad y que tipo y si es discapacidad multiple y que severidad segun la CIF
def determine_disability(scores):
    # Verificar si la puntuación total supera el umbral
    total_score = sum(scores.values())
    if total_score < threshold:
        return "No hay discapacidad"

    # Determinar el dominio con mayor puntuación
    max_domain = max(scores, key=scores.get)
    disability = domain_to_disability[max_domain]

    # Verificar si hay discapacidad múltiple con otros dominios significativos
    significant_domains = [domain for domain, score in scores.items() if score >= threshold]
    if len(significant_domains) > 1:
        disability = "Discapacidad Múltiple"

    # Determinar la severidad de la discapacidad según la puntuación total por dominio
    if total_score < 20.00:
        severity = "Leve"
    elif total_score < 30.00:
        severity = "Moderada"
    else:
        severity = "Severa"

    return f"{disability} {severity}"



# Programa principal con datos predefinidos
def main():
    # Datos del paciente con discapacidad psicosocial
    name = "Jesús David Silva Rangel"
    id_number = "1004898027"
    answers = []
    scores = {domain: 0 for domain in domains}

    # Respuestas predefinidas que indican discapacidad psicosocial
    # Asignamos puntajes altos en los dominios relacionados con discapacidad psicosocial
    predefined_answers = {
        'Fisica': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'Visual': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'Auditiva': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'Cognitiva': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'Psicosocial': [3, 4, 5, 2, 2, 3, 1, 3, 4, 3],
        'Sordoceguera': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    }

    for domain, questions in domains.items():
        print(f"\n--- {domain} ---")
        for i, question in enumerate(questions):
            print(f"\n{question}")
            print("\n".join(options))  # Mostrar opciones
            # Usar respuestas predefinidas
            answer = predefined_answers[domain][i]
            print(f"Respuesta seleccionada: {answer}")
            score_value = input_to_score[answer]
            scores[domain] += score_value
            answers.append(score_value)

    # Imprimir datos del paciente
    print("\n--- Datos del Paciente ---")
    print(f"\nNombre: {name}")
    print(f"Número de Identificación: {id_number}")

    # Determinar el tipo de discapacidad
    print("\n--- Resultados ---")
    disability_result = determine_disability(scores)
    print(f"\nDiagnóstico automático: {disability_result}")


    # Imprimir puntuaciones por dominio
    print("\n--- Puntuaciones por Dominio ---")
    for domain, score in scores.items():
        print(f"{domain}: {score:.2f}")

if __name__ == "__main__":
    main()



# Datos de discapacidad psicosocial
    """ predefined_answers = {
        "Cuidado personal": [4, 4, 3, 3, 5, 4, 3, 4, 3, 5],
        "Relaciones": [5, 4, 4, 5, 3, 4, 5, 5, 4, 5],
        "Actividades de la vida diaria": [4, 3, 5, 4, 5, 3, 4, 5, 4, 5],
        "Participación": [5, 4, 5, 5, 4, 5, 4, 5, 5, 5],
        "Cognición": [2, 2, 1, 1, 2, 1, 1, 2, 2, 1],
        "Movilidad": [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
        'Fisica': [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
        'Visual': [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
        'Auditiva': [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
        'Cognitiva': [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
        'Psicosocial': [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
        'Sordoceguera': [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
        'Multiple': [1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
    } 
    
    
    domains = {
    "Cognición": [
        "¿Experimenta dificultad para recordar información reciente?",
        "¿Se siente confundido en entornos nuevos o poco familiares?",
        "¿Tiene dificultades para concentrarse en tareas prolongadas?",
        "¿Encuentra complicado comprender información compleja?",
        "¿Olvida realizar tareas planificadas?",
        "¿Tiene problemas para resolver problemas o tomar decisiones?",
        "¿Se desorienta en lugares que antes le eran familiares?",
        "¿Le resulta difícil planificar actividades cotidianas?",
        "¿Tiene dificultades para seguir instrucciones con múltiples pasos?",
        "¿Se distrae fácilmente incluso en entornos tranquilos?"
    ],
    "Movilidad": [
        "¿Presenta dificultades para caminar distancias habituales?",
        "¿Tiene problemas al subir o bajar escaleras sin apoyo?",
        "¿Le cuesta levantarse de una silla sin asistencia?",
        "¿Encuentra difícil agacharse o arrodillarse?",
        "¿Experimenta dolor al realizar movimientos cotidianos?",
        "¿Le resulta complicado mantenerse de pie por períodos prolongados?",
        "¿Utiliza dispositivos de apoyo para desplazarse, como bastones o sillas de ruedas?",
        "¿Tiene dificultad para moverse en espacios reducidos o concurridos?",
        "¿Se siente inseguro al caminar sobre superficies irregulares?",
        "¿Evita actividades físicas debido a limitaciones en su movilidad?"
    ],
    "Cuidado personal": [
        "¿Requiere asistencia para realizar su aseo personal?",
        "¿Tiene dificultades para vestirse de forma independiente?",
        "¿Necesita ayuda para alimentarse adecuadamente?",
        "¿Encuentra desafíos al mantener su higiene diaria?",
        "¿Requiere apoyo para utilizar las instalaciones sanitarias?",
        "¿Le cuesta realizar tareas como cepillarse los dientes o peinarse?",
        "¿Tiene problemas para preparar sus comidas diarias por sí mismo?",
        "¿Necesita ayuda para mantener la limpieza de su entorno personal?",
        "¿Olvida tomar sus medicamentos de manera regular?",
        "¿Evita actividades de cuidado personal debido a dolor o limitaciones físicas?"
    ],
    "Relaciones": [
        "¿Tiene dificultades para establecer y mantener relaciones de amistad?",
        "¿Se siente incomprendido en la expresión de sus emociones?",
        "¿Le resulta complicado iniciar conversaciones con otras personas?",
        "¿Evita situaciones sociales por ansiedad o incomodidad?",
        "¿Percibe rechazo o aislamiento en entornos grupales?",
        "¿Tiene problemas para colaborar efectivamente en trabajos en equipo?",
        "¿Considera que su condición afecta las relaciones con su familia?",
        "¿Le resulta difícil comunicar sus necesidades emocionales?",
        "¿Evita interacciones sociales por temor al juicio o crítica?",
        "¿Encuentra problemas para relacionarse con compañeros de trabajo o estudio?"
    ],
    "Actividades de la vida diaria": [
        "¿Tiene problemas para realizar compras o trámites cotidianos?",
        "¿Encuentra dificultades al llevar a cabo tareas domésticas básicas?",
        "¿Necesita apoyo para manejar sus finanzas personales?",
        "¿Tiene problemas para leer, escribir o entender documentos importantes?",
        "¿Le resulta complicado utilizar dispositivos electrónicos o tecnológicos?",
        "¿Evita salir solo debido a preocupaciones por su seguridad?",
        "¿Siente inseguridad al enfrentar situaciones de emergencia?",
        "¿Se ve limitado para participar en actividades recreativas que antes disfrutaba?",
        "¿Tiene dificultades para mantener una rutina diaria organizada?",
        "¿Evita actividades al aire libre por razones físicas o emocionales?"
    ],
    "Participación": [
        "¿Encuentra obstáculos para involucrarse en actividades comunitarias?",
        "¿Percibe que su condición impacta en su desempeño laboral o académico?",
        "¿Evita lugares concurridos debido al estrés o ansiedad que le generan?",
        "¿Tiene dificultades para asistir y participar en eventos familiares?",
        "¿Se siente excluido o aislado en entornos sociales?",
        "¿Limita sus viajes o desplazamientos por dificultades físicas o de acceso?",
        "¿Encuentra impedimentos para contribuir en proyectos comunitarios o voluntarios?",
        "¿Siente que su condición reduce sus oportunidades de crecimiento personal?",
        "¿Le resulta difícil expresar sus opiniones o ideas en público?",
        "¿Evita actividades sociales por temor a la interacción con otros?"
    ],
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
    "Auditiva": [
        "¿Tiene dificultades para escuchar conversaciones en entornos ruidosos?",
        "¿Le cuesta entender el habla incluso cuando es clara y lenta?",
        "¿Experimenta zumbidos o pitidos en los oídos?",
        "¿Necesita aumentar el volumen de dispositivos auditivos?",
        "¿Tiene problemas para seguir instrucciones verbales?",
        "¿Siente que los demás le hablan en voz baja o susurrando?",
        "¿Tiene problemas para mantener conversaciones telefónicas?",
        "¿Evita eventos sociales debido a problemas de audición?",
        "¿Tiene dificultades para localizar la fuente de sonidos?",
        "¿Experimenta dolor o malestar en los oídos con frecuencia?"
    ],
    "Sordoceguera": [
        "¿Tiene dificultades para comunicarse con otros de manera efectiva debido a limitaciones visuales y auditivas?",
        "¿Necesita asistencia para realizar tareas cotidianas debido a limitaciones sensoriales?",
        "¿Tiene problemas para identificar objetos o personas sin ayuda?",
        "¿Siente que su discapacidad afecta significativamente su independencia?",
        "¿Tiene dificultades para navegar en entornos desconocidos?",
        "¿Requiere apoyo para actividades de la vida diaria debido a limitaciones sensoriales?",
        "¿Tiene problemas para acceder a información visual y auditiva?",
        "¿Evita situaciones nuevas o desconocidas debido a su discapacidad sensorial?",
        "¿Siente que su condición limita su participación social?",
        "¿Tiene dificultades para expresar sus necesidades o deseos?"
    ]
}
    
    """