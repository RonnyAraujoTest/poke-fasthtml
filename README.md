
# 🚀 Pokedex FastHTML

Una recreación fiel de la Pokedex original migrada de React/Next.js a **FastHTML**. Utiliza **HTMX** para actualizaciones de estado asíncronas y **Python** para la lógica del servidor.

## 📜 Créditos y Referencias 
Este proyecto es una migración a **FastHTML** basada en el trabajo original de [Nombre de tu Amigo]. 
* **Proyecto Original:** [Nombre del Repo de tu amigo]
* **Autor Original:** [@treblig-punisher](https://github.com/treblig-punisher)
* **Repositorio Base:** https://github.com/treblig-punisher/pokedex-nextjs ¡Gracias por permitirme usar tu diseño como base para aprender FastHTML!

## 🧪 Tecnologías utilizadas

-   **FastHTML**: Framework principal de Python.
    
-   **HTMX**: Para la interactividad sin recargar la página.
    
-   **PokeAPI**: Fuente de datos de los Pokémon.
    
-   **CSS Custom Properties**: Para el diseño temático.

## 🛠️ Instalación y Configuración

Sigue estos pasos para correr el proyecto localmente:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/tu-usuario/tu-pokedex.git](https://github.com/tu-usuario/tu-pokedex.git)
cd tu-pokedex
```

### 2. Configurar el entorno
Crea un entorno virtual e instala las dependencias:
```bash
python -m venv .venv
# En Windows:
source .venv/Scripts/activate
# En Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Variables de entorno
Crea un archivo `.env` basado en el ejemplo:
```bash
cp .env.example .env
```

### 4. Ejecutar la aplicación
```bash
python main.py
```
La aplicación estará disponible en `http://localhost:5000`
