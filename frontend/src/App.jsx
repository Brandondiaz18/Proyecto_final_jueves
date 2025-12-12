import { useEffect, useState } from "react";
import { apiGet, apiPost, apiPut, apiDelete } from "./services/api";
import TodoForm from "./components/TodoForm";
import TodoItem from "./components/TodoItem";

function App() {
  const [todos, setTodos] = useState([]);
  const [error, setError] = useState(null);

  // cargar lista
  const loadTodos = async () => {
    try {
      const data = await apiGet("/todos"); // <--- CORREGIDO
      if (!Array.isArray(data)) {
        throw new Error("Respuesta del servidor no es una lista");
      }
      setTodos(data);
      setError(null);
    } catch (err) {
      console.error("Error cargando tareas:", err);
      setError("No se pudieron cargar las tareas. Ver consola.");
    }
  };

  useEffect(() => {
    loadTodos();
  }, []);

  // crear
  const createTodo = async (title) => {
    await apiPost("/todos", { title });
    loadTodos();
  };

  // actualizar
  const updateTodo = async (id, title) => {
    await apiPut(`/todos/${id}`, { title });
    loadTodos();
  };

  // borrar
  const deleteTodo = async (id) => {
    await apiDelete(`/todos/${id}`);
    loadTodos();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Gestor de Tareas ✔️</h1>

      {error && (
        <p style={{ color: "red", fontWeight: "bold" }}>
          {error}
        </p>
      )}

      <TodoForm onCreate={createTodo} />

      <h2>Lista de tareas</h2>

      {todos.length === 0 ? (
        <p>No hay tareas todavía.</p>
      ) : (
        <ul>
          {todos.map((t) => (
            <TodoItem
              key={t._id || t.id}
              todo={t}
              onUpdate={updateTodo}
              onDelete={deleteTodo}
            />
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
