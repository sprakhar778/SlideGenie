# SlideGenie API Reference

All API endpoints are available under `http://localhost:8000`.

## 1. Presentation Management
Endpoints for creating, reading, and deleting presentations.

- **POST** `/create-presentation`
    - **Summary:** Create a new presentation
    - **Description:** Initializes presentation state with user topic and content. Returns a presentation ID.
- **GET** `/presentations/{presentation_id}`
    - **Summary:** Get full presentation state
    - **Description:** Returns the complete internal state of the presentation.
- **DELETE** `/presentations/{presentation_id}`
    - **Summary:** Delete a presentation
    - **Description:** Permanently deletes the saved presentation JSON file.

---

## 2. Theme Management
Endpoints for generating and updating a presentation theme.

- **GET** `/presentation-theme/{presentation_id}`
    - **Summary:** Generate or get theme
    - **Description:** Generates a presentation theme based on topic and content.
- **POST** `/presentation-theme/{presentation_id}`
    - **Summary:** Update theme
    - **Description:** Manually overrides the theme information for a presentation.

---

## 3. Slides Data Management
Endpoints for generating and editing structured slide data.

- **GET** `/presentation-data/{presentation_id}`
    - **Summary:** Generate or get all slides data
    - **Description:** Generates structured slide data (slide_type, content, description) for all slides.
- **GET** `/presentation-data/{presentation_id}/slide/{slide_index}`
    - **Summary:** Get a single slide's data
    - **Description:** Returns the slide data for a specific slide by index.
- **POST** `/presentation-data/{presentation_id}/slide/{slide_index}`
    - **Summary:** Update a single slide's data
    - **Description:** Manually update the content and/or description of a specific slide by index.

---

## 4. Slide Layout Management
Endpoints for assigning and regenerating slide layouts.

- **GET** `/presentation-layout/{presentation_id}`
    - **Summary:** Generate or get layout for all slides
    - **Description:** Assigns a layout template to every slide based on its slide_type.
- **GET** `/presentation-layout/{presentation_id}/slide/{slide_index}`
    - **Summary:** Get layout for a single slide
    - **Description:** Returns the assigned layout for a specific slide by index.
- **POST** `/presentation-layout/{presentation_id}/slide/{slide_index}/regenerate`
    - **Summary:** Regenerate layout for a single slide
    - **Description:** Force-regenerates the layout for a specific slide.

---

## 5. Slide Code Generation
Streaming endpoint for generating slide HTML code.

- **GET** `/presentation-slides/{presentation_id}`
    - **Summary:** Stream slide HTML for all slides
    - **Description:** Streams HTML code for each slide as NDJSON.

---

## 6. Utility
Health-check and miscellaneous utility endpoints.

- **GET** `/health`
    - **Summary:** Health check
    - **Description:** Returns service health status.
