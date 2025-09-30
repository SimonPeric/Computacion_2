📚 Resumen teórico de la clase
1. Pipes vs FIFOs

Pipes:

Son canales de comunicación entre procesos relacionados (por ejemplo, padre-hijo).

Se crean con pipe() en C o con objetos como multiprocessing.Pipe en Python.

Son temporales: existen solo mientras los procesos involucrados estén en ejecución.

No tienen un nombre en el sistema de archivos.

Útiles para comunicación rápida dentro de un mismo programa o entre procesos muy ligados.

FIFOs (Named Pipes):

Funcionan como pipes, pero son persistentes y tienen un nombre en el sistema de archivos.

Se crean con mkfifo en la terminal o os.mkfifo() en Python.

Permiten que procesos no relacionados (ejecutados en momentos distintos) se comuniquen.

Persisten hasta que se eliminen manualmente.

2. Problemas comunes con FIFOs

Bloqueo (deadlock o espera indefinida):

Un proceso queda esperando porque el otro extremo no abre el FIFO.

Ejemplo: abrir en modo lectura sin que nadie lo abra en escritura.

Prevención:

Abrir el FIFO en modo no bloqueante (O_NONBLOCK).

Asegurar que el otro proceso abra su extremo antes de hacer operaciones.

Mantener una lógica clara de quién envía y quién recibe.

3. Motivos para usar un diseño específico

En el contexto de tu trabajo:

Evitar bloqueos → Configurando el flujo para que el FIFO siempre tenga datos o cierre correctamente.

Comunicación dirigida → Cada proceso sabe qué debe enviar y recibir.

Distribución de datos → Asegurar que cada destinatario reciba exactamente lo que le corresponde.

4. Comunicación entre procesos en Python

Pipes: con multiprocessing.Pipe(), crean un canal entre dos procesos.

Queues: con multiprocessing.Queue(), permiten pasar mensajes a múltiples procesos de forma segura.

FIFOs: con os.mkfifo() y operaciones de lectura/escritura estándar (open, read, write).
