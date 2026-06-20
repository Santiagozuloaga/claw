
import random

# === CONFIGURACIÓN DE LA VENTANA ===
WIDTH = 600
HEIGHT = 300

# === INICIALIZACIÓN DE ACTORES ===
player = Actor('hero', (300, 150))  # Corregido: posición inicial dentro de los límites
star = Actor('star')
star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

# === ENEMIGOS ===
enemies = []
for _ in range(7):  # Optimizado: bucle para crear enemigos
    enemy = Actor('enemy')
    enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    enemy.speed_x = random.choice([2, -2])
    enemy.speed_y = random.choice([2, -2])
    enemies.append(enemy)

background = Actor('background')
score = 0
game_over = True  # Corregido: comienza con game_over=True para obligar a iniciar el juego

def draw():
    screen.clear()
    background.draw()
    if not game_over:
        player.draw()
        star.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text(str(score), (10, 10), color='white')  # Corregido: convertir score a string
    else:
        screen.draw.text('¡Has perdido! Pulse R para reiniciar', center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color='red')

def update(dt):
    global score, game_over
    if game_over:
        if keyboard.r:  # Corregido: usa 'r' en lugar de 'enter' como especifica el mensaje
            restart_game()
        return
    
    # === MOVIMIENTO DEL JUGADOR ===
    if keyboard.left and player.left > 0:
        player.x -= 10
    if keyboard.right and player.right < WIDTH:
        player.x += 10
    if keyboard.up and player.top > 0:
        player.y -= 10
    if keyboard.down and player.bottom < HEIGHT:
        player.y += 10
    
    # === COLISIONES Y LÓGICA ===
    if player.colliderect(star):
        score += 1  # Corregido: suma puntos en lugar de restarlos
        star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    
    for enemy in enemies:
        enemy.x += enemy.speed_x
        enemy.y += enemy.speed_y
        if enemy.left < 0 or enemy.right > WIDTH:
            enemy.speed_x = -enemy.speed_x
        if enemy.top < 0 or enemy.bottom > HEIGHT:
            enemy.speed_y = -enemy.speed_y
        if player.colliderect(enemy):
            game_over = True

def restart_game():
    global score, game_over
    player.pos = 300, 150  # Corregido: posición coherente con la inicial
    star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    for enemy in enemies:
        enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        enemy.speed_x = random.choice([2, -2])
        enemy.speed_y = random.choice([2, -2])
    score = 0
    game_over = False
</antArtifact>

Ahora te explico los 5 errores que encontré y corregí:

1. **Posición inicial del jugador**: La posición (400, 300) estaba fuera de la ventana (HEIGHT=300). La cambié a (300, 150).

2. **Tamaño de una imagen de enemigo**: Había un enemigo con tamaño (300, 30) que era desproporcionado. Eliminé esa configuración de tamaño.

3. **Conversión del puntaje**: Faltaba convertir la variable `score` a string en `screen.draw.text()`.

4. **Puntuación**: El juego restaba puntos al recoger estrellas en lugar de sumarlos.

5. **Tecla para reiniciar**: El mensaje de game over indica pulsar "R" pero el código verificaba "enter".

Optimizaciones realizadas:
- Usé un bucle para crear los enemigos, reduciendo muchas líneas de código repetitivo
- Combiné condiciones en el movimiento de los enemigos
- Organicé el código con comentarios para mejor legibilidad
- Simplifiqué el código del movimiento del jugador

El juego ahora está en 66 líneas (sin contar los comentarios y líneas en blanco), muy por debajo del límite de 90 líneas requerido.
 Entiendo que aún estás teniendo problemas con el juego. Vamos a modificar la versión para hacer que funcione correctamente y además implementar la parte del desafío donde intercambiamos la lógica entre enemigos y potenciadores:

<antArtifact identifier="pygame-invertido" type="application/vnd.ant.code" language="python" title="Juego PyGame Zero corregido con lógica invertida">
#pgzero
import random

# === CONFIGURACIÓN DE LA VENTANA ===
WIDTH = 600
HEIGHT = 300

# === INICIALIZACIÓN DE ACTORES ===
player = Actor('hero', (300, 150))
star = Actor('star')
star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

# === ENEMIGOS (AHORA COLECCIONABLES) ===
enemies = []
for _ in range(7):
    enemy = Actor('enemy')
    enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    enemy.speed_x = random.choice([2, -2])
    enemy.speed_y = random.choice([2, -2])
    enemies.append(enemy)

background = Actor('background')
score = 0
game_over = True  # Inicia con game_over para que el jugador presione R

def draw():
    screen.clear()
    background.draw()
    if not game_over:
        player.draw()
        star.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text(str(score), (10, 10), color='white', fontsize=30)
    else:
        screen.draw.text('¡Has perdido! Pulse R para reiniciar', center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color='red')
        screen.draw.text('Recolecta enemigos y evita las estrellas', center=(WIDTH // 2, HEIGHT // 2 + 40), fontsize=20, color='white')

def update(dt):
    global score, game_over
    if game_over:
        if keyboard.r:
            restart_game()
        return
    
    # === MOVIMIENTO DEL JUGADOR ===
    if keyboard.left and player.left > 0:
        player.x -= 10
    if keyboard.right and player.right < WIDTH:
        player.x += 10
    if keyboard.up and player.top > 0:
        player.y -= 10
    if keyboard.down and player.bottom < HEIGHT:
        player.y += 10
    
    # === LÓGICA INVERTIDA ===
    # Estrellas ahora son peligrosas
    if player.colliderect(star):
        game_over = True
    
    # Enemigos ahora son coleccionables
    for i, enemy in enumerate(enemies[:]):
        enemy.x += enemy.speed_x
        enemy.y += enemy.speed_y
        
        # Rebote en los bordes
        if enemy.left < 0 or enemy.right > WIDTH:
            enemy.speed_x = -enemy.speed_x
        if enemy.top < 0 or enemy.bottom > HEIGHT:
            enemy.speed_y = -enemy.speed_y
            
        # Colisión con jugador (suma puntos y elimina enemigo)
        if player.colliderect(enemy):
            score += 1
            enemies.remove(enemy)
            # Crear nuevo enemigo
            if len(enemies) < 7:
                new_enemy = Actor('enemy')
                new_enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
                new_enemy.speed_x = random.choice([2, -2])
                new_enemy.speed_y = random.choice([2, -2])
                enemies.append(new_enemy)

def restart_game():
    global score, game_over, enemies
    player.pos = 300, 150
    star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    
    # Recrear enemigos
    enemies = []
    for _ in range(7):
        enemy = Actor('enemy')
        enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        enemy.speed_x = random.choice([2, -2])
        enemy.speed_y = random.choice([2, -2])
        enemies.append(enemy)
        
    score = 0
    game_over = False
</antArtifact>

He implementado varios cambios importantes:

1. **Lógica invertida completa**:
   - Ahora las estrellas son peligrosas - si las tocas, pierdes
   - Los enemigos son coleccionables - sumas puntos al tocarlos

2. **Sistema de recreación de enemigos**:
   - Cuando recoges un enemigo, este desaparece y aparece uno nuevo en una posición aleatoria
   - Esto mantiene siempre el mismo número de enemigos en pantalla

3. **Mejor información para el jugador**:
   - Aumenté el tamaño del texto del puntaje para verlo mejor
   - Añadí instrucciones adicionales en la pantalla de game over explicando la lógica invertida

4. **Reinicio mejorado**:
   - El reinicio ahora recrea completamente la lista de enemigos
   - Asegura que siempre tengas exactamente 7 enemigos al iniciar

Ahora deberías poder jugar y conseguir fácilmente docenas de puntos recogiendo enemigos mientras evitas las estrellas. ¿Te funciona correctamente esta versión?
 Veo que necesitas una evaluación más detallada de los errores encontrados en el código original. Analizaré el código que me proporcionaste y te presentaré los 5 errores específicos junto con sus soluciones.

<antArtifact identifier="codigo-depurado" type="application/vnd.ant.code" language="python" title="Juego PyGame Zero - Errores corregidos">
#pgzero
import random

# === CONFIGURACIÓN DE LA VENTANA ===
WIDTH = 600
HEIGHT = 300

# === INICIALIZACIÓN DE ACTORES ===
player = Actor('hero', (300, 150))  # Error 1: Posición fuera de pantalla (400, 300) → (300, 150)
star = Actor('star')
star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

# === ENEMIGOS ===
enemies = []
for _ in range(7):  # Optimizado: creación de enemigos en bucle
    enemy = Actor('enemy')
    enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    enemy.speed_x = random.choice([2, -2])
    enemy.speed_y = random.choice([2, -2])
    enemies.append(enemy)
    # Error 2: Uno de los enemigos tenía tamaño incorrecto (300, 30) → tamaño normal

background = Actor('background')
score = 0
game_over = True

def draw():
    screen.clear()
    background.draw()
    if not game_over:
        player.draw()
        star.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text(str(score), (10, 10), color='white')  # Error 3: Faltaba str() para convertir score a texto
    else:
        screen.draw.text('¡Has perdido! Pulse R para reiniciar', center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color='red')

def update(dt):
    global score, game_over
    if game_over:
        if keyboard.r:  # Error 4: El mensaje dice pulsar 'R', pero el código esperaba 'enter'
            restart_game()
        return
    
    # === MOVIMIENTO DEL JUGADOR ===
    if keyboard.left and player.left > 0:
        player.x -= 10
    if keyboard.right and player.right < WIDTH:
        player.x += 10
    if keyboard.up and player.top > 0:
        player.y -= 10
    if keyboard.down and player.bottom < HEIGHT:
        player.y += 10
    
    # === COLISIONES Y LÓGICA ===
    if player.colliderect(star):
        score += 1  # Error 5: Restaba puntos (-=) en lugar de sumarlos
        star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    
    for enemy in enemies:
        enemy.x += enemy.speed_x
        enemy.y += enemy.speed_y
        if enemy.left < 0 or enemy.right > WIDTH:
            enemy.speed_x = -enemy.speed_x
        if enemy.top < 0 or enemy.bottom > HEIGHT:
            enemy.speed_y = -enemy.speed_y
        if player.colliderect(enemy):
            game_over = True

def restart_game():
    global score, game_over
    player.pos = 300, 150
    star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    for enemy in enemies:
        enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        enemy.speed_x = random.choice([2, -2])
        enemy.speed_y = random.choice([2, -2])
    score = 0
    game_over = False
</antArtifact>

Los 5 errores específicos que identifiqué y corregí son:

1. **Error de posición inicial del jugador**: La posición original (400, 300) estaba fuera de los límites de la ventana, ya que HEIGHT es 300. La corregí a (300, 150) para que esté en el centro de la pantalla.

2. **Error de tamaño de un enemigo**: Uno de los enemigos tenía un tamaño no estándar de (300, 30), lo que generaba un enemigo desproporcionadamente grande. Eliminé esta anomalía para que todos los enemigos tengan el mismo tamaño.

3. **Error de tipo de datos**: En la función draw(), se intentaba mostrar la variable 'score' directamente con screen.draw.text(), pero se necesita convertirla a string con str(score).

4. **Error de consistencia en teclas**: El mensaje de juego perdido indica "Pulse R para reiniciar", pero el código verificaba keyboard.enter en lugar de keyboard.r.

5. **Error lógico de puntuación**: Al colisionar con una estrella, el código restaba puntos (score -= 1) cuando debería sumarlos (score += 1).

Para la versión con lógica invertida (donde recoges enemigos y evitas estrellas), puedes usar este código:

<antArtifact identifier="logica-invertida" type="application/vnd.ant.code" language="python" title="Juego PyGame Zero - Lógica invertida">
#pgzero
import random

# === CONFIGURACIÓN DE LA VENTANA ===
WIDTH = 600
HEIGHT = 300

# === INICIALIZACIÓN DE ACTORES ===
player = Actor('hero', (300, 150))
star = Actor('star')
star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

# === ENEMIGOS (AHORA COLECCIONABLES) ===
enemies = []
for _ in range(7):
    enemy = Actor('enemy')
    enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    enemy.speed_x = random.choice([2, -2])
    enemy.speed_y = random.choice([2, -2])
    enemies.append(enemy)

background = Actor('background')
score = 0
game_over = True

def draw():
    screen.clear()
    background.draw()
    if not game_over:
        player.draw()
        star.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text(str(score), (10, 10), color='white', fontsize=30)
    else:
        screen.draw.text('¡Has perdido! Pulse R para reiniciar', center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color='red')
        screen.draw.text('Recolecta enemigos y evita las estrellas', center=(WIDTH // 2, HEIGHT // 2 + 40), fontsize=20, color='white')

def update(dt):
    global score, game_over
    if game_over:
        if keyboard.r:
            restart_game()
        return
    
    # === MOVIMIENTO DEL JUGADOR ===
    if keyboard.left and player.left > 0: player.x -= 10
    if keyboard.right and player.right < WIDTH: player.x += 10
    if keyboard.up and player.top > 0: player.y -= 10
    if keyboard.down and player.bottom < HEIGHT: player.y += 10
    
    # === LÓGICA INVERTIDA ===
    # Estrellas ahora son peligrosas
    if player.colliderect(star):
        game_over = True
    
    # Enemigos ahora son coleccionables
    for i, enemy in enumerate(enemies[:]):
        enemy.x += enemy.speed_x
        enemy.y += enemy.speed_y
        
        # Rebote en los bordes
        if enemy.left < 0 or enemy.right > WIDTH: enemy.speed_x = -enemy.speed_x
        if enemy.top < 0 or enemy.bottom > HEIGHT: enemy.speed_y = -enemy.speed_y
            
        # Colisión con jugador (suma puntos y respawn)
        if player.colliderect(enemy):
            score += 1
            enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

def restart_game():
    global score, game_over
    player.pos = 300, 150
    star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    for enemy in enemies:
        enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        enemy.speed_x = random.choice([2, -2])
        enemy.speed_y = random.choice([2, -2])
    score = 0
    game_over = False
</antArtifact>

Ambas versiones cumplen con los criterios del concurso:
1. ✅ Se han identificado y solucionado los 5 errores, permitiendo que el juego se inicie y funcione correctamente.
2. ✅ El código está optimizado a menos de 90 líneas sin perder funcionalidad, y las regiones importantes están comentadas.
3. ✅ La versión con lógica invertida permite recoger enemigos y evitar estrellas, haciendo fácil conseguir docenas de puntos.

¿Estos cambios resuelven los problemas que estabas experimentando?
 Correcto, ese es uno de los errores cruciales en el código original. Cuando intentas mostrar texto en pantalla usando `screen.draw.text()`, el primer parámetro debe ser una cadena de texto (string). 

En el código original, se estaba pasando directamente la variable numérica `score`:
```python
screen.draw.text(score, (10, 10), color='white')
```

Pero esto causaría un error porque la función espera recibir un string, no un número. La solución es convertir el valor numérico a string usando la función `str()`:
```python
screen.draw.text(str(score), (10, 10), color='white')
```

Este es un error común en juegos PyGame Zero cuando se quiere mostrar valores numéricos como puntuaciones. Sin esta corrección, el juego lanzaría un error cuando intentara dibujar el puntaje en pantalla, impidiendo que el juego funcione correctamente.
 <antArtifact identifier="codigo-optimizado" type="application/vnd.ant.code" language="python" title="Juego PyGame Zero - Optimizado">
#pgzero
import random

# === CONFIGURACIÓN ===
WIDTH = 600
HEIGHT = 300

# === INICIALIZACIÓN ===
player = Actor('hero', (300, 150))
star = Actor('star', pos=(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)))
background = Actor('background')
score = 0
game_over = True

# === CREACIÓN DE ENEMIGOS ===
enemies = []
for _ in range(7):
    enemy = Actor('enemy', pos=(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)))
    enemy.speed_x = random.choice([2, -2])
    enemy.