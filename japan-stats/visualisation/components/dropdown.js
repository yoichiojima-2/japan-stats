import { useState } from "react";

const DropDown = ({ options, onFilterChange }) => {
  const [selectedValue, setSelectedValue] = useState(options[0] || "")

  const handleChange = (event) => {
    setSelectedValue(event.target.value);
    onFilterChange(event.target.value);
  }

  return (
    <select value={selectedValue} onChange={handleChange}>
      {options.map(opt => (
        <option key={opt} value={opt}>{opt}</option>
      ))}
    </select>
  );
}

export default DropDown