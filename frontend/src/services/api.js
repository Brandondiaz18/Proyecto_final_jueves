import { API_URL } from "../config";

export const apiGet = async (endpoint) => {
  const response = await fetch(`${API_URL}/api${endpoint}`);
  return response.json();
};


export const apiPost = async (endpoint, data) => {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  return res.json();
};

export const apiPut = async (endpoint, data) => {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  return res.json();
};

export const apiDelete = async (endpoint) => {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: "DELETE"
  });
  return res.json();
};
