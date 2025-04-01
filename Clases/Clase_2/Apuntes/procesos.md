# Resumen Teórico: Procesos en Sistemas Operativos

## ¿Qué es un proceso?
Un **proceso** es un programa en ejecución. Se compone de:
- **Código** (instrucciones del programa).
- **Datos** (variables, estructuras de datos, etc.).
- **Pila** (stack: manejo de llamadas a funciones y variables locales).
- **Heap** (memoria dinámica).
- **Registros y contexto de ejecución**.

## Creación de Procesos en Linux
En sistemas UNIX/Linux, un nuevo proceso se crea mediante la llamada al sistema `fork()`, que genera un **proceso hijo** idéntico al padre.

### Ejemplo en Python:
```python
import os

pid = os.fork()
if pid == 0:
    print(f"Soy el proceso hijo, PID: {os.getpid()}")
else:
    print(f"Soy el proceso padre, PID: {os.getpid()}, hijo: {pid}")
```

## Procesos Zombi y Huérfanos
### Proceso Zombi
Un **proceso zombi** es un proceso hijo que ha terminado su ejecución pero su entrada en la tabla de procesos aún no ha sido eliminada porque el padre no ha leído su estado de terminación con `wait()`.

#### Cómo Crear un Zombi en Python:
```python
import os, time

pid = os.fork()
if pid > 0:
    print(f"Proceso padre (PID {os.getpid()}) creado, hijo PID {pid}")
    time.sleep(10)  # Simula un padre que no recoge el estado del hijo
else:
    print(f"Proceso hijo (PID {os.getpid()}) terminado")
    exit(0)
```

### Proceso Huérfano
Un **proceso huérfano** es un proceso cuyo padre ha terminado antes que él. El proceso huérfano es adoptado por `init` o `systemd`.

#### Cómo Crear un Huérfano en Python:
```python
import os, time

pid = os.fork()
if pid > 0:
    print(f"Proceso padre (PID {os.getpid()}) terminando")
else:
    time.sleep(5)  # Simula una ejecución más larga
    print(f"Proceso huérfano (PID {os.getpid()}), adoptado por init/systemd")
```

## Visualización de Procesos
Podemos inspeccionar los procesos en ejecución con:
```sh
ps aux | grep <PID>
ps -o pid,ppid,cmd -u $USER
```

## Terminación de Procesos
Los procesos pueden terminar de varias maneras:
1. **Salida normal:** `exit(0)`.
2. **Señales del sistema:** `kill -9 <PID>`.
3. **El padre llama `wait()` para eliminar al hijo de la tabla de procesos.**

#### Manejo de `wait()` en Python:
```python
import os
pid = os.fork()
if pid > 0:
    os.wait()  # Espera a que el hijo termine
    print("El proceso hijo ha terminado correctamente.")
else:
    print("Proceso hijo ejecutando.")
    exit(0)
```

---
Este resumen cubre los conceptos clave sobre la gestión de procesos en sistemas operativos UNIX/Linux, con ejemplos prácticos en C y Python. ¡Buena suerte con tu estudio! 🚀

