import { API_URL } from "../config";

export const apiGet = async (endpoint) => {
  const response = await fetch(`${API_URL}${endpoint}`);
  return response.json();
};

export const apiPost = async (endpoint, data) => {
  const response = await fetch(`${API_URL}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return response.json();
};

export const apiPut = async (endpoint, data) => {
  const response = await fetch(`${API_URL}${endpoint}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return response.json();
};

export const apiDelete = async (endpoint) => {
  const response = await fetch(`${API_URL}${endpoint}`, {
    method: "DELETE",
  });
  return response.json();
};
