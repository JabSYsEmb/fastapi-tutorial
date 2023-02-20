import { useEffect } from "react";
import axios from "axios";

function App() {
  useEffect(() => {
    axios
      .get("http://backend.colasloth.com/api/v1/items")
      .then((res) => res.data)
      .then((data) => console.log(data));
  }, []);
  return <h1>Gello</h1>;
}

export default App;
