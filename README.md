# SlideGenie 🧞‍♂️

**SlideGenie** is a cutting-edge, AI-powered presentation generation platform. It empowers users to effortlessly turn ideas into beautifully styled, layout-perfect slides and export them seamlessly. 

With a dynamic React frontend and a powerful FastAPI + AI backend, SlideGenie automates the tedious parts of presentation design, from theme creation to layout structuring and PDF exporting.

## 🌟 Key Features
- **AI-Driven Creativity:** Generate complete slide themes and robust layouts directly from your prompts. 
- **Real-Time Editor & Preview:** Instantly preview generated slides in a sandboxed, visually rich editor environment.
- **Pixel-Perfect PDF Export:** Advanced conversion using WeasyPrint to keep your slides' orientation and styling undistorted when exporting to PDF.
- **Interactive "Export Anywhere":** Features a beautiful PDF carousel and layout views for an enhanced management experience.
- **Modern Tech Stack:** Built with speed and scalability in mind using React, TailwindCSS, and FastAPI.

## 🏗️ Project Structure
The repository is split into two main directories:
- [`/frontend`](./frontend/README.md): The React user interface, built with Tailwind CSS, Radix UI, and React Router.
- [`/backend`](./backend/README.md): The FastAPI and Langbase (AI) processing server.

## 🚀 Setup & Installation

### 1. Backend Setup
Navigate into the backend directory, install the Python dependencies, and run the server.
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -e . # or use uv sync
cp .env.example .env
python -m src.api.main
```
The backend will run on `http://localhost:8000`.

### 2. Frontend Setup
Navigate into the frontend directory, install the node dependencies, and start the development server.
```bash
cd frontend
npm install
npm start
```
The frontend will run on `http://localhost:3000`.

## 🎥 Demo Video
> *[]*

---
*Built with ❤️ by the SlideGenie Team.*
