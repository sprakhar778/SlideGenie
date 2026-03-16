# SlideGenie - Backend

The backend for SlideGenie is a high-performance, asynchronous REST API powered by FastAPI. It handles the core AI logic, presentation management, and seamless slide-to-PDF conversion.

## Features
- **AI Presentation Generation:** Leverages advanced pipelines (Langchain/Langgraph) to generate slide content and themes seamlessly.
- **Slide Processing & Management:** Robust routing for handling presentation data, layouts, and generated slide codes.
- **High-Quality PDF Export:** Integrated `WeasyPrint` and automated browser tools to accurately render HTML/CSS into presentation-ready PDFs.
- **Scalable Architecture:** Modular design with clearly defined API routers and helpers.

## Tech Stack
- **Framework:** FastAPI
- **Server:** Uvicorn
- **PDF Generation:** WeasyPrint (HTML to PDF layout engine)
- **AI Tooling:** Langchain / Langgraph (Prompts, Chains, Nodes)
- **Python Version:** 3.x (managed via `uv`)

## Setup Guidelines

1. **Environment Setup:**
   Ensure you have Python installed and set up your virtual environment via `uv` or `venv`.
   ```bash
   # If using venv
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install Dependencies:**
   ```bash
   uv sync
   # or depending on your package manager
   pip install -r pyproject.toml
   ```

3. **Configure Environment Variables:**
   Copy `.env.example` to `.env` and fill in the required values (like your AI model API keys).
   ```bash
   cp .env.example .env
   ```

4. **Run the API:**
   ```bash
   python -m src.api.main
   ```
   The API will be available at `http://localhost:8000`. You can access the Swagger UI documentation at `http://localhost:8000/docs`.

## Demo Video
> 🎥 *[]*
