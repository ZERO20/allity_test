# Rick and Morty API Sync - Módulo Odoo
Módulo de Odoo 18 que permite sincronizar personajes de la serie **Rick and Morty** desde la API pública oficial ([rickandmortyapi.com](https://rickandmortyapi.com/documentation/#get-all-characters)).

## 🚀 Instalación
1. **Copiar el módulo** al directorio `addons` de Odoo 18
2. **Actualizar** la lista de aplicaciones en Odoo
3. **Instalar** el módulo "Rick and Morty API Sync"
4. **Navegar** al menú "Rick and Morty" → "Personajes"

## 📖 Uso

### Sincronización Inicial
1. Ve a **Rick and Morty** → **Personajes**
2. Dar clic en `Sincronizar personajes`
3. Esperar el proceso y visualizar en `Personajes` los registros.

### Odoo
- **Versión**: Odoo 18.0

## 🌐 API Utilizada

- **URL Base**: `https://rickandmortyapi.com/api`
- **Endpoint**: `/character` (obtiene todos los personajes paginados)
- **Documentación**: [rickandmortyapi.com/documentation](https://rickandmortyapi.com/documentation/#get-all-characters)
