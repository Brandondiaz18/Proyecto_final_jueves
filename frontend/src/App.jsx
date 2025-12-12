import { useEffect, useState } from "react";
import { apiGet } from "./services/api";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    apiGet("/").then((res) => setData(res));
  }, []);

  return (
    <div>
      <h1>Frontend funcionando 🚀</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default App;
