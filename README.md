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

1. **Crear un proyecto en Google Cloud y habilitar la API de Drive**
  - Ve a https://console.cloud.google.com/ y accede con tu cuenta de Google.
  - Crea un nuevo proyecto (o selecciona uno existente).
  - En el menú de la izquierda, ve a “APIs y servicios” > “Biblioteca”.
  - Busca “Google Drive API” y haz clic en “Habilitar”.

2. **Crear una cuenta de servicio y descargar credenciales**
  - En el menú de la izquierda, ve a “APIs y servicios” > “Credenciales”.
  - Haz clic en “Crear credencial” > “Cuenta de servicio”.
  - Ponle un nombre y crea la cuenta.
  - En la sección de permisos, puedes omitir (haz clic en continuar).
  - Una vez creada, haz clic en la cuenta de servicio y luego en “Claves”.
  - Haz clic en “Agregar clave” > “Crear nueva clave” > selecciona “JSON” y descarga el archivo.
  - Renombra el archivo descargado a `credenciales.json` y colócalo en la raíz de tu proyecto.

3. **Compartir la carpeta de Drive con la cuenta de servicio**
  - Crea una carpeta en tu Google Drive donde se subirán los reportes.
  - Haz clic derecho en la carpeta > “Compartir”.
  - Copia el email de la cuenta de servicio (aparece en el archivo JSON, algo como `xxxx@xxxx.iam.gserviceaccount.com`) y agrégalo como colaborador con permisos de editor.
  - Copia el ID de la carpeta (está en la URL de Drive, después de `/folders/`).

4. **Configura el ID de la carpeta en tu proyecto**
  - Abre el archivo `utils/drive.py`.
  - Reemplaza `'TU_FOLDER_ID_AQUI'` por el ID real de tu carpeta de Drive.

---

## ¿Cómo probar la aplicación localmente?

1. Instala las dependencias (ya sea con `pip install -r requirements.txt` o usando el entorno virtual configurado).
2. Ejecuta la app con:
  ```bash
  streamlit run app.py
  ```
3. Abre el navegador en la dirección que te indique Streamlit (por defecto http://localhost:8501).
4. Llena el formulario, genera el reporte y verifica que se suba correctamente a tu carpeta de Google Drive.

Puedes abrir la app desde tu celular si ambos dispositivos están en la misma red local, usando la IP de tu PC (ejemplo: http://192.168.1.10:8501).
