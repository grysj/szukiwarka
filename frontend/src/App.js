import "./App.css";
import TextField from "@mui/material/TextField";
import { useEffect, useState } from "react";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import NumberInput from "./components/NumberInput";
import Button from "@mui/material/Button";
import Search from "./components/SearchResults";

function App() {
  const [inputQuery, setInputQuery] = useState("");
  const [inputEngine, setInputEngine] = useState("");
  const [inputK, setInputK] = useState("");
  const [data, setData] = useState("");

  function onButtonClick() {
    const url = `http://127.0.0.1:8000/search?query=${encodeURIComponent(
      String(inputQuery)
    )}&eng=${parseInt(inputEngine)}&k=${parseInt(inputK)}`;
    console.log(url);
    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setData(data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }

  return (
    <div className="App">
      <img src="szukiwarka.png"></img>
      <div className="search-bar">
        <TextField
          fullWidth
          // style={{ width: "500px" }}
          label="Query"
          id="Query"
          onChange={(e) => setInputQuery(e.target.value)}
        />
        <Button variant="contained" onClick={onButtonClick}>
          Search
        </Button>
      </div>
      <div className="params">
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">Engine</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={inputEngine}
            label="Engine"
            onChange={(e) => setInputEngine(Number(e.target.value))}
          >
            <MenuItem value={0}>LRA for k = 500</MenuItem>
            <MenuItem value={1}>LRA for k = 1000</MenuItem>
            <MenuItem value={2}>LRA for k = 2000</MenuItem>
            <MenuItem value={3}>LRA for k = 4000</MenuItem>
            <MenuItem value={4}>Original Matrix</MenuItem>
          </Select>
        </FormControl>
        <NumberInput value={inputK} setValue={setInputK} />
      </div>
      <Search data={data}></Search>
    </div>
  );
}

export default App;
