# Rick and Morty API Sync - Módulo Odoo

## 📋 Descripción

Módulo de Odoo 18 que permite sincronizar personajes de la serie **Rick and Morty** desde la API pública oficial ([rickandmortyapi.com](https://rickandmortyapi.com/documentation/#get-all-characters)).

## ✨ Características Principales

### 🎭 Gestión de Personajes
- **Modelo simple** con los datos esenciales de los personajes
- **Descarga automática** de imágenes desde la API
- **Sincronización completa** de todos los personajes (826 personajes)
- **Actualización** de personajes existentes en futuras sincronizaciones

### 📊 Campos del Modelo
- **ID**: ID único del personaje en la API
- **Nombre**: Nombre del personaje
- **Imagen**: Imagen del personaje descargada automáticamente

### 🖥️ Vistas Disponibles
- **Vista Kanban**: Tarjetas visuales con imágenes, nombre e ID
- **Vista Lista**: Tabla simple con imagen, ID y nombre
- **Vista Formulario**: Vista detallada del personaje

### 🔄 Sincronización
- **Botón "Sincronizar"** en la vista lista para obtener todos los personajes
- **Acción del servidor** configurable desde el menú de acción
- **Prevención de duplicados** usando el ID de la API
- **Manejo de errores** con notificaciones informativas

## 🚀 Instalación

1. **Copiar el módulo** al directorio `addons` de Odoo 18
2. **Actualizar** la lista de aplicaciones en Odoo
3. **Instalar** el módulo "Rick and Morty API Sync"
4. **Navegar** al menú "Rick and Morty" → "Personajes"

## 📖 Uso

### Sincronización Inicial
1. Ve a **Rick and Morty** → **Personajes**
2. En la vista lista, haz clic en **"Acción"** → **"Sincronizar Personajes de Rick and Morty"**
3. El proceso descargará todos los 826 personajes con sus imágenes
4. Recibirás una notificación con el resumen de la sincronización

### Funcionalidades Adicionales
- **Búsqueda**: Por nombre e ID del personaje

## 🔧 Dependencias Técnicas

### Odoo
- **Versión**: Odoo 18.0
- **Módulos**: `base` (incluido en el core)

### Python
- **requests**: Para realizar llamadas HTTP a la API
- **base64**: Para codificar imágenes (incluido en Python)

## 🌐 API Utilizada

- **URL Base**: `https://rickandmortyapi.com/api`
- **Endpoint**: `/character` (obtiene todos los personajes paginados)
- **Documentación**: [rickandmortyapi.com/documentation](https://rickandmortyapi.com/documentation/#get-all-characters)

## 📁 Estructura del Módulo

```
rick_and_morty_api_sync/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── rick_morty_character.py
├── views/
│   └── rick_morty_character_views.xml
├── security/
│   └── ir.model.access.csv
└── README.md
```

## 🛠️ Funcionalidades Técnicas

### Modelo Principal: `rick.morty.character`
```python
# Campos principales
- name: Nombre del personaje
- api_id: ID único de la API
- image: Imagen en binario
```

### Métodos Principales
- `action_sync_characters()`: Sincronización completa desde la API
- `_prepare_character_data()`: Procesamiento de datos de la API

## 🔒 Permisos y Seguridad
- **Usuarios normales**: Lectura, escritura, creación y eliminación
- **Usuarios públicos**: Solo lectura
- **Configuración**: `security/ir.model.access.csv`

## 📝 Notas de Desarrollo

### Manejo de Errores
- **Timeouts**: 30 segundos para la API, 10 segundos para imágenes
- **Notificaciones**: Mensajes informativos de éxito y error
- **Logging**: Registro detallado de operaciones y errores

### Optimizaciones
- **Prevención de duplicados** usando `api_id`
- **Actualización inteligente** de registros existentes
- **Paginación automática** para obtener todos los personajes
- **Descarga asíncrona** de imágenes

## 🐛 Solución de Problemas

### Error de Conexión
Si hay problemas de conexión a la API:
1. Verificar conexión a internet
2. Revisar que `https://rickandmortyapi.com` esté accesible
3. Verificar logs de Odoo para detalles del error

### Imágenes No Cargan
Si las imágenes no se descargan:
1. Verificar permisos de escritura en Odoo
2. Volver a ejecutar la sincronización
3. Revisar configuración de firewall/proxy

## 📈 Estadísticas de la API
- **Personajes totales**: 826
- **Páginas**: ~42 (20 personajes por página)
- **Especies**: Diversas (Humanos, Aliens, etc.)
- **Estados**: Vivo, Muerto, Desconocido

## 🎯 Casos de Uso
- **Fans de Rick and Morty**: Base de datos personal de personajes
- **Desarrolladores**: Ejemplo de integración con APIs externas
- **Análisis de datos**: Estadísticas sobre personajes de la serie
- **Aprendizaje**: Referencia para módulos de Odoo con APIs

---

**Autor**: Allity  
**Versión**: 18.0.1.0.0  
**Licencia**: LGPL-3 