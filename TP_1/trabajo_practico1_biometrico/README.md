Trabajo práctico 1 - Sistema Concurrente de Análisis Biométrico

Archivos:
- main.py: Ejecuta generador, analizadores y verificador. Produce blockchain.json
- verificar_cadena.py: Verifica integridad de blockchain.json y genera reporte.txt
- blockchain.json: Se genera al ejecutar main.py
- reporte.txt: Generado por verificar_cadena.py

Requisitos:
- Python 3.9+
- Dependencias: numpy 

Ejecución:
1) Ejecutar el sistema y generar la cadena:
   $ python3 main.py

   (espera 60s mientras genera 60 muestras; puedes interrumpir con Ctrl+C que intenta parada limpia)

2) Verificar la cadena y obtener reporte:
   $ python3 verificar_cadena.py

Salida:
- blockchain.json se actualiza cada bloque.
- reporte.txt contiene: total de bloques, bloques con alerta y promedios.

Notas:
- Los analizadores envían resultados a una cola compartida; el verificador agrupa por timestamp.
- Cada analizador envia "FIN" cuando termina; el verificador finaliza cuando recibe los 3 "FIN".
- Si quieres cambiar la duración de la prueba, modifica la constante SAMPLES en main.py.

Justificación:

En este proyecto se utilizan pipes en lugar de FIFOs debido a la naturaleza de la comunicación entre procesos que se requiere:

    Comunicación estrictamente entre procesos emparentados
    Los pipes están pensados para pasar datos entre un proceso padre y sus hijos. En este proyecto, todos los procesos que intercambian información se generan dentro de la misma jerarquía, por lo que no es necesario que otros procesos externos puedan acceder a la tubería.

    Menor sobrecarga y simplicidad
    Los pipes no requieren crear un archivo especial en el sistema de archivos (como sí lo hacen las FIFOs), lo que simplifica la implementación y evita operaciones adicionales de apertura y borrado del recurso.

    Mayor seguridad y control del flujo
    Al ser anónimos, los pipes desaparecen automáticamente cuando todos los procesos que los usan cierran sus extremos, evitando fugas o accesos no deseados por parte de otros procesos que podrían abrir una FIFO en el sistema.

    Velocidad y temporalidad de los datos
    En esta aplicación los datos son efímeros y no necesitan persistir en el sistema. Las FIFOs, al ser con nombre, permiten conexiones persistentes en el tiempo, pero eso no aporta beneficios en este caso y sí añade complejidad innecesaria.

En resumen, se usan pipes porque la comunicación es inmediata, temporal, privada y limitada a procesos relacionados, lo que encaja perfectamente con sus características y evita la sobrecarga que tendría usar FIFOs.
