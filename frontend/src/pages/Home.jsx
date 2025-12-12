import { useEffect, useState } from "react";
import { apiGet, apiPost } from "../services/api";

const Home = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState("");

  // Cargar todos los TODOs
  const loadTodos = async () => {
    const data = await apiGet("/todos");
    setTodos(data);
  };

  // Crear TODO
  const addTodo = async () => {
    if (!newTodo.trim()) return;
    await apiPost("/todos", { title: newTodo });
    setNewTodo("");
    loadTodos();
  };

  useEffect(() => {
    loadTodos();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Mis TODOs</h1>

      <input
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
        placeholder="Nuevo TODO"
      />
      <button onClick={addTodo}>Agregar</button>

      <ul>
        {todos.map((t) => (
          <li key={t.id}>{t.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
