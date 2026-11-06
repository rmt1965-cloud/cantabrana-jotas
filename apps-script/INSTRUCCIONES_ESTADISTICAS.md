# Puesta en marcha del módulo de estadísticas (10 minutos)

1. Entra en https://sheets.google.com con tu cuenta y crea una hoja nueva: "Cantabrana estadísticas".
2. Menú Extensiones > Apps Script. Borra el código que haya y pega TODO el contenido de Code.gs.
3. En la primera línea de configuración cambia `CAMBIA-ESTA-CLAVE` por tu clave (mínimo 10 caracteres). Solo tú la sabrás.
4. Arriba, elige la función `configurar` y pulsa Ejecutar. Acepta los permisos (Avanzado > Ir a proyecto). Se crea la pestaña "Eventos".
5. Implementar > Nueva implementación > Tipo: Aplicación web.
   - Ejecutar como: Yo
   - Quién tiene acceso: Cualquier usuario
   Pulsa Implementar y copia la URL que termina en /exec.
6. Abre `stats-config.js` y pega la URL entre las comillas: window.CANT_STATS_URL='https://script.google.com/macros/s/.../exec';
7. Publica con git (add, commit, push).
8. Tu panel: https://rmt1965-cloud.github.io/cantabrana-jotas/estadisticas.html  (te pedirá la clave).

Si cambias Code.gs más adelante: Implementar > Administrar implementaciones > Editar > Versión nueva (la URL no cambia).
