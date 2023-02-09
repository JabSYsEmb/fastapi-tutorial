import axios from "axios";
import { useEffect, useState } from "react";

function App() {
  const [response, setResponse] = useState({});
  useEffect(() => {
    axios
      .get("http://localhost:8000/312343")
      .then((item) => setResponse(item.data));
  }, []);

  return <h1>{response["message"]}</h1>;
}

export default App;
