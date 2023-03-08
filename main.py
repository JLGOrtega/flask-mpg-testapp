import os
from flask import Flask, request, jsonify, render_template
import pickle
import time


app = Flask(__name__)



chistes = ["¿Por qué los programadores prefieren los gatos? Porque tienen purr-ogramación en su ADN.",    
"¿Por qué los programadores odian el mar? Porque siempre devuelve un 404.",    
"¿Por qué los programadores prefieren el café frío? Porque no les gusta el Java caliente.",    
"¿Qué hace un servidor en un bar? Sirve a los clientes.",    
"¿Cómo se llama un programador sin café? Des-cafe-inado.",    
"¿Por qué los programadores no pueden trabajar en el exterior? Porque les da sol-syntax.",    
"¿Por qué los programadores prefieren el cielo? Porque no tienen bugs.",    
"¿Cómo se llama un programador que siempre está concentrado? Un foca, porque está en su shell.",    
"¿Por qué los programadores no pueden confiar en el átomo? Porque conforma todo.",    
"¿Qué es un objeto en la programación? Algo que una vez que se tira a la basura, se queda ahí para siempre."]

chistes += ["¿Por qué los programadores prefieren la oscuridad? Porque la luz atrae a los bugs.",    
"¿Qué es un grupo de programadores llamado? Un error 404, porque no se encontraron.",
    "¿Por qué los programadores siempre confunden Halloween con Navidad? Porque Oct 31 equals Dec 25.",    
    "¿Por qué los programadores no pueden comer en paz? Porque siempre hay alguien que les dice que sus platos tienen errores de sintaxis.",    
    "¿Qué le dijo un programador a otro programador cuando le pidió ayuda? Me encantaría, pero estoy ocupado resolviendo mis propios problemas.",    
    "¿Por qué los programadores no pueden jugar fútbol? Porque siempre intentan crear una nueva lógica de juego.",    
    "¿Por qué los programadores nunca se bañan? Porque siempre quieren actualizar algo.",    
    "¿Cómo se llama el estilo de programación que nunca funciona? Copy-paste.",    
    "¿Por qué los programadores son malos en los juegos de azar? Porque siempre esperan a que se actualicen las probabilidades.",    
    "¿Por qué los programadores no pueden tener citas? Porque siempre buscan la perfección en su pareja."]

import random

@app.route('/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        if "title" in request.form:
            title = request.form['title']
            content = request.form['content']

            if title.lower() in ["pelu"]:
                messages = [{'title': 'Pelu!',
                            'content': 'Menuda vaina marico!'},
                            {'title': 'Un chiste',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["dami", "damo"]:
                messages = [{'title': 'Vamo DAMOOOO!!!',
                            'content': 'El Damo SAAAAAPEEE'},
                            {'title': 'Un chiste inimputable',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["quiq", "enri", "puço", "kike"]:
                messages = [{'title': 'PUÇOL!',
                            'content': 'Caaarol, eres tuuuu!'},
                            {'title': 'Un chistaco pa pusol',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["quiq", "enri", "puço", "kike"]:
                messages = [{'title': 'PUÇOL!',
                            'content': 'Caaarol, eres tuuuu!'},
                            {'title': 'Un chistaco pa pusol',
                            'content': random.choice(chistes)}
                            ]

            elif title.lower() in ["carr", "javi"]:
                messages = [{'title': 'Damian J. Carras',
                            'content': 'Mi botella de agua se quedo en Mestalla!'},
                            {'title': 'Javi, pa que no te enfades con el VCF',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["yera"]:
                messages = [{'title': 'Torrent',
                            'content': 'Bon poble i...'},
                            {'title': 'Tigre, maquina, pegaso!',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["fabr", "digi", "giov"]:
                messages = [{'title': 'Ma coooooomo???',
                            'content': 'Ahora os enseñare mi hundir la flota para que lloreis, mataos'},
                            {'title': 'Pesto, pizza, provolone!',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["bea", "beat", "bea ", "amat"]:
                messages = [{'title': 'Buaaaaaaah!',
                            'content': 'Esto en derecho no pasaba!!'},
                            {'title': 'Flipas! Como va esto!?! No hay videos??',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["yari"]:
                messages = [{'title': 'Arroz con huevo y tomate en españa se llama: ARROZ A LA CUBANA!!!',
                            'content': 'Como te quedas?!?!?!'},
                            {'title': 'Para que te animes mientras se mejoran tus peques: ',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["adri"]:
                messages = [{'title': 'Adri, je bent de beste student ter wereld',
                            'content': 'we missen je!!!'},
                            {'title': 'Para que se te amenice la estancia hasta que vuelvas a Utrecht',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["guil"]:
                messages = [{'title': 'Ese Guille como mola!!',
                            'content': 'Se merece una ola!!!! UEEEE'},
                            {'title': 'Ahi va un horripilante chiste de chatgpt: ',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["guil"]:
                messages = [{'title': 'Ese Guille como mola!!',
                            'content': 'Se merece una ola!!!! UEEEE'},
                            {'title': 'Ahi va un horripilante chiste de chatgpt: ',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["selv"]:
                messages = [{'title': 'Selvie!!!',
                            'content': 'Tienes nombre de hacerte una foto a ti misma! 📸'},
                            {'title': 'Sorry!!! 😅 Si el chiste de arriba te parecio malo, aqui va otro: ',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["rube"]:
                messages = [{'title': 'OK, la broma ya valio...',
                            'content': 'Amigo, Ruben! Donde esta toda la comida que le habias prometido al profe?!?!?!'},
                            {'title': '... Tengo hambre',
                            'content': random.choice(chistes)}
                            ]
            elif title.lower() in ["dieg"]:
                messages = [{'title': 'Tacooooo!!',
                            'content': 'Taco taco, burrito burritooo! https://www.youtube.com/watch?v=bQKDlNTEl6w'},
                            {'title': 'Wei, pinche, pendejooo!!',
                            'content': random.choice(chistes)}
                            ]
            else:
                messages = [{'title': 'Exta si!!',
                            'content': 'Exta noooooo!!!'},
                            {'title': 'Esta me gusta me la como yoooo!! HUHA!',
                            'content': random.choice(chistes)}
                            ]
            time.sleep(4)
            return render_template('index.html', messages=messages)

    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
