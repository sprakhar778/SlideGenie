import axios from 'axios';

// Get API URL from localStorage or use default
const getApiUrl = () => {
  return localStorage.getItem('slidegenie_api_url') || 'https://uncarbonated-divisibly-charlee.ngrok-free.dev';
};

// Set API URL
export const setApiUrl = (url) => {
  localStorage.setItem('slidegenie_api_url', url);
};

// Create axios instance with dynamic baseURL
const createApi = () => {
  return axios.create({
    baseURL: getApiUrl(),
    timeout: 120000,
    headers: {
      'ngrok-skip-browser-warning': 'true', // Skip ngrok browser warning
    },
  });
};

// ── Presentation Management ──────────────────────────────────

export const createPresentation = async (topic, content) => {
  const api = createApi();
  const response = await api.post('/create-presentation', { topic, content });
  return response.data;
};

export const getPresentation = async (presentationId) => {
  const api = createApi();
  const response = await api.get(`/presentations/${encodeURIComponent(presentationId)}`);
  return response.data;
};

export const deletePresentation = async (presentationId) => {
  const api = createApi();
  const response = await api.delete(`/presentations/${encodeURIComponent(presentationId)}`);
  return response.data;
};

// ── Theme Management ─────────────────────────────────────────

export const getTheme = async (presentationId) => {
  const api = createApi();
  const response = await api.get(`/presentation-theme/${encodeURIComponent(presentationId)}`);
  return response.data;
};

export const updateTheme = async (presentationId, themeInfo) => {
  const api = createApi();
  const response = await api.post(`/presentation-theme/${encodeURIComponent(presentationId)}`, {
    theme_info: themeInfo,
  });
  return response.data;
};

// ── Slides Data Management ───────────────────────────────────

export const getSlidesData = async (presentationId) => {
  const api = createApi();
  const response = await api.get(`/presentation-data/${encodeURIComponent(presentationId)}`);
  return response.data;
};

export const getSlideData = async (presentationId, slideIndex) => {
  const api = createApi();
  const response = await api.get(
    `/presentation-data/${encodeURIComponent(presentationId)}/slide/${slideIndex}`
  );
  return response.data;
};

export const updateSlideData = async (presentationId, slideIndex, content, description) => {
  const api = createApi();
  const response = await api.post(
    `/presentation-data/${encodeURIComponent(presentationId)}/slide/${slideIndex}`,
    { content, description }
  );
  return response.data;
};

// ── Layout Management ────────────────────────────────────────

export const getLayouts = async (presentationId) => {
  const api = createApi();
  const response = await api.get(`/presentation-layout/${encodeURIComponent(presentationId)}`);
  return response.data;
};

export const getSlideLayout = async (presentationId, slideIndex) => {
  const api = createApi();
  const response = await api.get(
    `/presentation-layout/${encodeURIComponent(presentationId)}/slide/${slideIndex}`
  );
  return response.data;
};

export const regenerateSlideLayout = async (presentationId, slideIndex) => {
  const api = createApi();
  const response = await api.post(
    `/presentation-layout/${encodeURIComponent(presentationId)}/slide/${slideIndex}/regenerate`
  );
  return response.data;
};

// ── Slide Code Streaming ─────────────────────────────────────

export const streamSlides = async (presentationId, onChunk, onDone, onError) => {
  const apiUrl = getApiUrl();
  
  try {
    const response = await fetch(
      `${apiUrl}/presentation-slides/${encodeURIComponent(presentationId)}`,
      {
        headers: {
          'ngrok-skip-browser-warning': 'true',
        },
      }
    );
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = '';
    
    while (true) {
      const { done, value } = await reader.read();
      
      if (done) {
        onDone();
        break;
      }
      
      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split('\n');
      buffer = lines.pop() || '';
      
      for (const line of lines) {
        if (line.trim()) {
          try {
            const chunk = JSON.parse(line);
            onChunk(chunk);
          } catch (e) {
            console.warn('Failed to parse chunk:', line);
          }
        }
      }
    }
  } catch (error) {
    onError(error);
  }
};

export const regenerateSlideCode = async (presentationId, slideIndex, userInput, onChunk, onDone, onError) => {
  const apiUrl = getApiUrl();
  
  try {
    const response = await fetch(
      `${apiUrl}/presentation-slides/${encodeURIComponent(presentationId)}/slide/${slideIndex}/edit`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'ngrok-skip-browser-warning': 'true',
        },
        body: JSON.stringify({ user_input: userInput }),
      }
    );
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = '';
    
    while (true) {
      const { done, value } = await reader.read();
      
      if (done) {
        onDone();
        break;
      }
      
      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split('\n');
      buffer = lines.pop() || '';
      
      for (const line of lines) {
        if (line.trim()) {
          try {
            const chunk = JSON.parse(line);
            onChunk(chunk);
          } catch (e) {
            console.warn('Failed to parse chunk:', line);
          }
        }
      }
    }
  } catch (error) {
    onError(error);
  }
};

// ── PDF Download ─────────────────────────────────────────────

export const downloadPresentationPDF = async (presentationId) => {
  const api = createApi();
  const response = await api.get(`/presentations/${encodeURIComponent(presentationId)}/download`, {
    responseType: 'blob'
  });
  return response;
};

// ── Health Check ─────────────────────────────────────────────

export const healthCheck = async () => {
  const api = createApi();
  const response = await api.get('/health');
  return response.data;
};

// Export getApiUrl for display purposes
export { getApiUrl };
