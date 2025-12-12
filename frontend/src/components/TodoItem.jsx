import { useState } from "react";

function TodoItem({ todo, onUpdate, onDelete }) {
  const [editing, setEditing] = useState(false);
  const [title, setTitle] = useState(todo.title);

  const saveEdit = () => {
    onUpdate(todo._id || todo.id, title);
    setEditing(false);
  };

  return (
    <li style={{ marginBottom: "10px" }}>
      {editing ? (
        <>
          <input
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            style={{ padding: "5px" }}
          />
          <button onClick={saveEdit} style={{ marginLeft: "5px" }}>
            ✔️
          </button>
        </>
      ) : (
        <>
          {todo.title}

          <button
            onClick={() => setEditing(true)}
            style={{ marginLeft: "10px" }}
          >
            ✏️
          </button>

          <button
            onClick={() => onDelete(todo._id || todo.id)}
            style={{ marginLeft: "10px", color: "red" }}
          >
            🗑️
          </button>
        </>
      )}
    </li>
  );
}

export default TodoItem;
