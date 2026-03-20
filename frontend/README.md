# SlideGenie - Frontend

The frontend for SlideGenie is a modern, responsive React application built to provide an intuitive interface for AI-powered presentation generation.

## Features
- **Interactive Editor:** Real-time slide preview using iframes.
- **Theme Generation:** Seamless integration with backend AI to generate and preview beautiful themes.
- **Layout Management:** Advanced layout selection and preview experience.
- **Export Anywhere:** View and export presentation slides with a built-in PDF Carousel.
- **Responsive Design:** Polished UI components built with Radix UI and styled with Tailwind CSS.

## Tech Stack
- **Framework:** React 18
- **Routing:** React Router DOM
- **Styling:** Tailwind CSS, Radix UI Primitives
- **Form Validation:** React Hook Form + Zod
- **Animations/UI:** Embla Carousel, Recharts, Sonner (Toasts)
- **Build Tool:** Craco (Create React App Configuration Override)

## Setup Guidelines

1. **Install Dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

2. **Start Development Server:**
   ```bash
   npm start
   # or
   yarn start
   ```

3. **Build for Production:**
   ```bash
   npm run build
   ```
## Environment Variables

To run this project, you need to configure environment variables.

1. **Create a `.env` file** in the root of the `frontend` folder:

```bash
cp .env.example .env
```

2. **Open the `.env` file** and add your API key:

```env
REACT_APP_UNSPLASH_API_KEY=your_unsplash_api_key_here
```

3. **Get an Unsplash API Key:**

* Go to: https://unsplash.com/developers
* Create an application
* Copy the **Access Key**
* Paste it into your `.env` file

4. **Restart the development server** after updating `.env`:

```bash
npm start
```

> ⚠️ Note: Environment variables must start with `REACT_APP_` to be accessible in a React (CRA-based) project.



