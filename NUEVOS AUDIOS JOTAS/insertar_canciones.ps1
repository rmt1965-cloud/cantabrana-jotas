# Inserta las 11 canciones nuevas (40-50) en index.html de cantabrana-jotas.
# Ejecutar DESDE la carpeta cantabrana-jotas, en la rama nuevas-canciones.
# Solo contiene caracteres ASCII: las tildes van como \uXXXX, igual que en index.html.

$ErrorActionPreference = 'Stop'

if (-not (Test-Path 'index.html') -or -not (Test-Path 'audio')) {
    Write-Host 'ERROR: no estas en la carpeta cantabrana-jotas (falta index.html o audio). No se ha modificado nada.'
    return
}

$rama = (git branch --show-current)
if ($rama -ne 'nuevas-canciones') {
    Write-Host "ERROR: estas en la rama '$rama', no en 'nuevas-canciones'. No se ha modificado nada."
    return
}

$ruta = (Resolve-Path 'index.html').Path
$enc  = New-Object System.Text.UTF8Encoding($false)
$txt  = [System.IO.File]::ReadAllText($ruta, $enc)
$nl   = if ($txt.Contains("`r`n")) { "`r`n" } else { "`n" }

$bloque = @'
    {a:'Gregorio_Ojeda_Pena_y_Julian_Ojeda_Ojeda--40.mp3',c:'Juli\u00e1n Ojeda Ojeda y Gregorio Ojeda Pe\u00f1a',m:'Cantabrana',t:'YA NO RONDAN LOS CHAVALES'},
    {a:'Julian_Ojeda_Ojeda--41.mp3',c:'Juli\u00e1n Ojeda Ojeda y Gregorio Ojeda Pe\u00f1a',m:'Cantabrana',t:'SOY DEL VALLE (Juli\u00e1n y Gregorio)'},
    {a:'Gregorio_Ojeda_Pena_y_Julian_Ojeda_Ojeda--42.mp3',c:'Juli\u00e1n Ojeda Ojeda y Gregorio Ojeda Pe\u00f1a',m:'Cantabrana',t:'\u00c9CHALA CON FUERZA AL AIRE'},
    {a:'Julian_Ojeda_Ojeda--43.mp3',c:'Juli\u00e1n Ojeda Ojeda',m:'Cantabrana',t:'CANTAR AL MAESTRO'},
    {a:'Julian_Ojeda_Ojeda--44.mp3',c:'Juli\u00e1n Ojeda Ojeda',m:'Cantabrana',t:'O\u00d1A, TERMIN\u00d3N, BENTRETEA Y CANTABRANA (Juli\u00e1n)'},
    {a:'Gregorio_Ojeda_Pena_y_Julian_Ojeda_Ojeda--45.mp3',c:'Gregorio Ojeda Pe\u00f1a y Juli\u00e1n Ojeda Ojeda',m:'Cantabrana',t:'YA NO CANTAN LOS DE ALFARO'},
    {a:'Grupo_Cantabrana--46.mp3',c:'Grupo de Cantabrana',m:'Cantabrana',t:'VIENTO DEL NORTE'},
    {a:'Julian_Ojeda_Ojeda--47.mp3',c:'Juli\u00e1n Ojeda Ojeda',m:'Cantabrana',t:'TE CASAS EN CANTABRANA'},
    {a:'Gregorio_Ojeda_Pena_y_Julian_Ojeda_Ojeda--48.mp3',c:'Juli\u00e1n Ojeda Ojeda y Gregorio Ojeda Pe\u00f1a',m:'Cantabrana',t:'LOS QUE MANDAN\u2026'},
    {a:'Grupo_Cantabrana--49.mp3',c:'Grupo de Cantabrana',m:'Cantabrana',t:'O\u00d1A, TERMIN\u00d3N, BENTRETEA Y CANTABRANA (Grupo Cantabrana)'},
    {a:'Pedro_Felix_Garcia_Linaje--50.mp3',c:'Pedro F\u00e9lix Garc\u00eda Linaje',m:'Cantabrana',t:'YO NAC\u00cd EN CANTABRANA'},
'@
$bloque = ($bloque.TrimEnd() -replace "\r?\n", $nl)

if ($txt.Contains("Grupo_Cantabrana--49.mp3'")) {
    Write-Host 'El bloque ya estaba insertado. No se ha modificado nada.'
    return
}

$m = [regex]::Match($txt, "//\s*\{a:'Salve--37\.mp3'[^\r\n]*")
if (-not $m.Success) {
    Write-Host 'NO se ha encontrado la linea de Salve--37. No se ha modificado nada.'
    return
}

# Copia de seguridad fuera del repositorio
Copy-Item $ruta (Join-Path $env:TEMP 'index.html.copia_antes_de_canciones')

$txt = $txt.Insert($m.Index + $m.Length, $nl + $bloque)
[System.IO.File]::WriteAllText($ruta, $txt, $enc)
Write-Host 'Bloque insertado correctamente.'

# Comprobacion
$txt2 = [System.IO.File]::ReadAllText($ruta, $enc)
$refs = [regex]::Matches($txt2, "(?m)^\s*\{a:'([^']+\.mp3)'") | ForEach-Object { $_.Groups[1].Value } | Sort-Object -Unique
Write-Host "Canciones activas referenciadas en index.html: $($refs.Count)"
$faltan = $refs | Where-Object { -not (Test-Path (Join-Path 'audio' $_)) }
if ($faltan) { $faltan | ForEach-Object { Write-Host "FALTA el archivo: $_" } }
else { Write-Host 'Todos los audios referenciados existen en la carpeta audio.' }
git status --short index.html
