const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api';
const API_TOKEN = import.meta.env.VITE_API_TOKEN || '';

async function request(path, options = {}) {
  const headers = {
    'Content-Type': 'application/json',
    ...(options.headers || {}),
  };
  if (API_TOKEN) {
    headers.Authorization = `Bearer ${API_TOKEN}`;
  }

  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...options,
    headers,
  });

  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(payload.detail || `Request failed: ${response.status}`);
  }
  return payload;
}

export function getHealth() {
  return request('/health/');
}

export function getChirpConfig() {
  return request('/chirp-config/');
}

export function enrollUser(payload) {
  return request('/enroll/', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export function verifyUser(payload) {
  return request('/verify/', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export function getMetrics() {
  return request('/metrics/');
}
