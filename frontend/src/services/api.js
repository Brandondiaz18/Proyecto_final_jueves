import { API_URL } from "../config";

export const apiGet = async (endpoint) => {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: "GET",
    headers: { "Content-Type": "application/json" }
  });
  return res.json();
};

export const apiPost = async (endpoint, data) => {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
};

export const apiPut = async (endpoint, data) => {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
};

export const apiDelete = async (endpoint) => {
  const res = await fetch(`${API_URL}${endpoint}`, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" }
  });
  return res.json();
};
