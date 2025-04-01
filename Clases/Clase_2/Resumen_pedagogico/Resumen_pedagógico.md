📌 Resumen de lo aprendido

✅ Comprendiste qué son los procesos zombis y cómo se generan cuando un proceso hijo finaliza, pero su padre no llama a wait().

✅ Identificaste procesos zombis en tu sistema usando ps y verificaste su estado con el indicador Z.

✅ Eliminaste un proceso zombi al forzar la finalización de su proceso padre y comprobaste que desapareció.

✅ Aprendiste qué son los procesos huérfanos y cómo init/systemd los adopta cuando su padre muere.

✅ Observaste que un proceso puede pasar de zombi a huérfano, pero no al revés.

✅ Diferencias clave:

    Zombi: Terminado, pero su entrada sigue en la tabla de procesos.

    Huérfano: Sigue ejecutándose, pero su padre ya no existe.

✅ Aplicaste comandos como ps aux | grep <PID>, kill -9 <PID> y wait() para gestionar estos procesos.

✅ Experimentaste con la terminación de procesos y validaste los cambios con herramientas de monitoreo.

🔥 ¡Dominaste los conceptos fundamentales de procesos zombis y huérfanos con pruebas prácticas en la terminal! 🚀
