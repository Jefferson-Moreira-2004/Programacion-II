>[!Importante]
><h1>Flappy Bird Videojuego</h1>
<h2>Descripción del Código</h2>
<p>Este es un juego clásico de Flappy Bird implementado en Python utilizando la biblioteca <strong>pygame</strong>.
 El objetivo del juego es controlar un pájaro y evitar las tuberías que aparecen en pantalla, ganando puntos al pasar entre ellas sin chocar.</p>
<h3>Variables</h3>
<ul>
    <li><strong>Pantalla:</strong> Se configura para ser de 600x650 píxeles.</li>
    <li><strong>Colores:</strong> Se definen colores básicos como blanco y verde para los obstáculos.</li>
    <li><strong>Pájaro:</strong> El pájaro tiene un tamaño de 50x50 píxeles y es de color amarillo.</li>
    <li><strong>Tuberías:</strong> Las tuberías tienen un ancho fijo de 70 píxeles, y su altura es aleatoria dentro de un rango específico.</li>
</ul>

<h3>Funcionalidad</h3>
<ul>
    <li><strong>Movimiento del pájaro:</strong> El pájaro se mueve hacia abajo por la gravedad y puede ser impulsado hacia arriba al presionar la barra espaciadora.</li>
    <li><strong>Tuberías:</strong> Las tuberías se desplazan de derecha a izquierda y nuevas tuberías aparecen de forma aleatoria cuando una ya ha salido de la pantalla.</li>
    <li><strong>Colisiones:</strong> El juego termina si el pájaro toca una tubería o se sale de los límites de la pantalla.</li>
    <li><strong>Puntuación:</strong> Se muestra la puntuación en la parte superior de la pantalla, la cual aumenta cada vez que el pájaro pasa entre dos tuberías.</li>
</ul>
<h2>Funciones Principales</h2>
<ul>
    <li><strong>mostrar_puntuacion():</strong> Dibuja la puntuación actual en la pantalla.</li>
    <li><strong>main():</strong> La función principal donde ocurre la lógica del juego: control de eventos, movimiento del pájaro y las tuberías, detección de colisiones, y actualización de la pantalla.</li>
</ul>
<h2>Instrucciones</h2>
<ol>
    <li>Ejecuta el archivo Python.</li>
    <li>Usa la barra espaciadora (Space) para hacer que el pájaro salte.</li>
    <li>El objetivo es evitar que el pájaro toque el suelo, el techo o las tuberías.</li>
    <li>Cada vez que el pájaro pase entre las tuberías, obtendrás un punto.</li>
</ol>
<h2>Requisitos</h2>
<ul>
    <li>Python 3.x</li>
    <li>Pygame</li>
</ul>

<h2>Instalación de Pygame</h2>
<p>Si no tienes Pygame instalado, puedes hacerlo ejecutando el siguiente comando en CMD:</p>
<pre><code>pip install pygame</code></pre>
<h2>Animación y Captura de la aplicación🤩</h2>
<img scr="https://github.com/user-attachments/assets/d27c3fa8-fcd4-4f85-9c04-1a3a9cb517e9" width="100">

