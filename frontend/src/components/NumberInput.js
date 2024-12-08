import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";

const NumberInput = ({ value, setValue }) => {
  const [error, setError] = useState("");

  const handleChange = (event) => {
    const newValue = event.target.value;
    if (newValue === "" || (newValue > 0 && newValue < 50)) {
      setValue(Number(newValue));
      setError("");
    } else {
      setError("Value must be between 0 and 100");
    }
  };

  return (
    <Box>
      <TextField
        label="Number of results"
        type="number"
        value={value}
        onChange={handleChange}
        variant="outlined"
        sx={{ width: "300px" }}
        error={!!error}
        helperText={error}
        inputProps={{ min: 0, max: 100 }}
      />
    </Box>
  );
};

export default NumberInput;
