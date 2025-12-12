import { useEffect, useState } from "react";
import { apiGet, apiPost, apiPut, apiDelete } from "./services/api";
import TodoForm from "./components/TodoForm";
import TodoItem from "./components/TodoItem";

function App() {
  const [todos, setTodos] = useState([]);

  const loadTodos = async () => {
    const data = await apiGet("/api/todos");
    setTodos(data);
  };

  useEffect(() => {
    loadTodos();
  }, []);

  const createTodo = async (title) => {
    await apiPost("/api/todos/", { title });
    loadTodos();
  };

  const updateTodo = async (id, title) => {
    await apiPut(`/api/todos/${id}`, { title });
    loadTodos();
  };

  const deleteTodo = async (id) => {
    await apiDelete(`/api/todos/${id}`);
    loadTodos();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Gestor de Tareas ✔️</h1>

      <TodoForm onCreate={createTodo} />

      <h2>Lista de tareas</h2>

      {todos.length === 0 ? (
        <p>No hay tareas todavía.</p>
      ) : (
        <ul>
          {todos.map((t) => (
            <TodoItem
              key={t.id}
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
