import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [isConn, setIsConn] = useState(() => false);

  useEffect(() => {
    axios
      .get("http://backend.colasloth.com/api/v1/items")
      .then((res) => res.data)
      .then((data) => data && setIsConn(true));
  }, []);
  return (
    <div className="app-div">
      <h1>
        The Frontend{" "}
        <span className={isConn ? "green" : "red"}>
          {isConn ? "is" : "is not"} connected
        </span>{" "}
        to the backend
      </h1>
    </div>
  );
}

export default App;
