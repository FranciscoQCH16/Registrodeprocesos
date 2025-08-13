# Requisitos para la app de reportes B.P.M.

- Aplicación web responsiva (accesible desde móvil y PC)
- Desarrollada en Python con Streamlit
- Pestañas para distintos reportes
- Primer reporte: Verificación de B.P.M.
  - Campos: Nombre de establecimiento, Fecha
  - Tabla editable: Nombre del operario, Cargo, Lavado de manos, Dotación, Utilizan toda la dotación, Uñas cortas limpias y sin esmalte, Accesorios y presentación personal, Observaciones
  - Selectores SI/C/NC para verificación
  - Campos de texto: Responsable, Supervisor, Revisión
- Generación de archivo Excel
- Subida de archivo a Google Drive


## Estructura inicial sugerida
- app.py (principal)
- requirements.txt
- utils/
  - excel.py (generación de Excel)
  - drive.py (subida a Google Drive)
- README.md

## Configuración de Google Drive

1. **Crear un proyecto

## ¿Cómo probar la aplicación localmente?

1. Instala las dependencias (ya sea con `pip install -r requirements.txt` o usando el entorno virtual configurado).
2. Ejecuta la app con:
  ```bash
  streamlit run app.py
  ```
3. Abre el navegador en la dirección que te indique Streamlit (por defecto http://localhost:8501).
4. Llena el formulario, genera el reporte y verifica que se suba correctamente a tu carpeta de Google Drive.

Puedes abrir la app desde tu celular si ambos dispositivos están en la misma red local, usando la IP de tu PC (ejemplo: http://192.168.1.10:8501).
