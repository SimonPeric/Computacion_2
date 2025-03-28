Aquí tienes un **resumen teórico** con los **comandos principales** para estudiar y anotar en tus apuntes. 😊  

---

# **📌 Resumen Teórico: Git y Entrada/Salida en Unix/Linux**

## **1️⃣ ¿Qué es Git y por qué es importante?**  
Git es un **sistema de control de versiones distribuido** que permite gestionar cambios en proyectos de software de manera eficiente.  

🔹 **Diferencias con SVN:**  
- No depende de un servidor central.  
- Permite trabajar sin conexión.  
- Es más rápido y liviano.  
- Maneja ramas (branches) de forma eficiente.  

🔹 **Ventajas de Git:**  
- Permite colaboración en equipo.  
- Guarda un historial completo de cambios.  
- Facilita la recuperación de versiones anteriores.  

### **🖥 Comandos básicos de configuración**  
Verificar si Git está instalado:  
```bash
git --version
```  
Configurar usuario y correo:  
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```  
Ver configuración actual:  
```bash
git config --list
```

---

## **2️⃣ Creación y manejo de un repositorio Git**  
Un **repositorio Git** es un directorio que contiene el historial de versiones de un proyecto.  

🔹 **Tipos de repositorios:**  
- **Local:** En tu computadora.  
- **Remoto:** En servidores como GitHub.  

🔹 **Estructura interna de un repositorio:**  
Cuando se inicia un repositorio, se crea una carpeta oculta `.git`, que almacena la información del control de versiones.  

### **🖥 Comandos para crear un repositorio**  
Crear una carpeta y entrar en ella:  
```bash
mkdir NombreRepositorio
cd NombreRepositorio
```  
Inicializar un repositorio Git:  
```bash
git init
```  
Ver el estado del repositorio:  
```bash
git status
```

---

## **3️⃣ Estructura del repositorio del curso**  
Mantener una estructura organizada facilita el trabajo en equipo. Un buen esquema podría ser:  
```
README.md
/TP_1
/TP_2
/Clases
    /Clase_1
        /Apuntes
        /Ejercicios
        /Resumen_pedagógico
/TRABAJO_FINAL
```  
El archivo `README.md` es importante para describir el proyecto.  

### **🖥 Comandos útiles**  
Crear múltiples carpetas al mismo tiempo:  
```bash
mkdir -p Clases/Clase_1/{Apuntes,Ejercicios,Resumen_pedagógico} TP_1 TP_2 TRABAJO_FINAL
```  
Crear un archivo `README.md` y editarlo:  
```bash
touch README.md
nano README.md
```

---

## **4️⃣ Primer commit y flujo de trabajo en Git**  
Git tiene **tres áreas** donde pueden estar los archivos:  
1. **Working Directory (Directorio de Trabajo):** Archivos en tu carpeta.  
2. **Staging Area (Área de Preparación):** Archivos listos para ser confirmados.  
3. **Local Repository (Repositorio Local):** Cambios guardados permanentemente.  

### **🖥 Comandos clave**  
Añadir archivos al área de staging:  
```bash
git add .
```  
Hacer un commit (confirmar cambios):  
```bash
git commit -m "Primer commit"
```  
Ver historial de commits:  
```bash
git log --oneline
```

---

## **5️⃣ Conexión con un repositorio remoto**  
Un **repositorio remoto** permite compartir el código con otros desarrolladores.  

🔹 **Plataformas populares:**  
- **GitHub**  
- **GitLab**  
- **Bitbucket**  

### **🖥 Comandos clave**  
Añadir un repositorio remoto:  
```bash
git remote add origin https://github.com/usuario/repositorio.git
```  
Verificar repositorios remotos:  
```bash
git remote -v
```  
Subir cambios al repositorio remoto:  
```bash
git push -u origin main
```

---

## **6️⃣ Entrada/Salida en Unix/Linux**  
Unix sigue el **modelo de Entrada/Salida estándar (E/S)**:  
- **stdin (entrada estándar):** Permite ingresar datos (ej. teclado).  
- **stdout (salida estándar):** Muestra datos en la terminal.  
- **stderr (error estándar):** Muestra mensajes de error.  

🔹 **Redirección:**  
- `>` Sobrescribe un archivo.  
- `>>` Agrega al archivo sin sobrescribir.  
- `<` Usa un archivo como entrada.  
- `2>` Redirige errores.  

🔹 **Pipes (`|`)**  
Permiten encadenar comandos:  
```bash
ls -l | grep "archivo"
```  

🔹 **Archivo especial `/dev/null`**  
Descarta cualquier contenido enviado a él:  
```bash
comando > /dev/null 2>&1
```

---

# **📌 Conclusión**  
✅ Git es una herramienta esencial para cualquier desarrollador.  
✅ Organizar bien el repositorio facilita la colaboración.  
✅ Comprender los conceptos de entrada/salida en Unix ayuda a mejorar la eficiencia.  

Este resumen te servirá para estudiar y repasar. ¡Éxitos en la materia! 🚀📚
