// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
// import React, { useState, useEffect } from 'react';
// import './App.css';

// function App() {

//   const [searchQuery, setSearchQuery] = useState('');
//   const [output, setOutput] = useState('');

//   const handleSearch = () => {
//     // Here you can implement logic to handle the search query
//     // For simplicity, let's just set the output to the search query
//     setOutput(searchQuery);
//   };

//   return (
//     <div className="App">
//       <div className="header">
//         <h1>Better Playlists</h1>
//       </div>
//       <div className="search-container">
//         <input
//           type="text"
//           placeholder="Enter a playlist to match"
//           value={searchQuery}
//           onChange={(e) => setSearchQuery(e.target.value)}
//         />
//         <button onClick={handleSearch}>Search</button>
//       </div>
//       <div className="output-container">
//         <h2>Output:</h2>
//         <p>{output}</p>
//       </div>
//     </div>
//   );
// }

// export default App;

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [inputList, setInputList] = useState('');
  const [mergeSortTime, setMergeSortTime] = useState('');
  const [quickSortTime, setQuickSortTime] = useState('');
  const [mergeSortedArray, setMergeSortedArray] = useState([]);
  const [quickSortedArray, setQuickSortedArray] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [output, setOutput] = useState('');

  const handleInputChange = (e) => {
    setInputList(e.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post('/sort', { list: inputList });
      setMergeSortTime(response.data.mergeSortTime);
      setQuickSortTime(response.data.quickSortTime);
      setMergeSortedArray(response.data.mergeSortedArray);
      setQuickSortedArray(response.data.quickSortedArray);
    } catch (error) {
      console.error('Error sorting list:', error);
    }
  };

  const handleSearch = () => {
    // Here you can implement logic to handle the search query
    // For simplicity, let's just set the output to the search query
    setOutput(searchQuery);
  };

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        console.log(data)
      }
    )
  }, [])

  return (
    <div className="App">
      <div className="header">
        <h1>Better Playlists</h1>
      </div>
      <div className="search-container">
        <input
          type="text"
          placeholder="Enter a playlist to match"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>
      <div className="output-container">
        <h2>Output:</h2>
        <p>{output}</p>
      </div>
      <div className="sorting-container">
        <h2>Sorting Algorithms</h2>
        <div>
          <label htmlFor="inputList">Input List:</label>
          <input type="text" id="inputList" value={inputList} onChange={handleInputChange} />
          <button onClick={handleSubmit}>Sort</button>
        </div>
        <div>
          <h3>Merge Sort:</h3>
          <p>Time taken: {mergeSortTime}</p>
          <p>Sorted list: {mergeSortedArray.join(', ')}</p>
        </div>
        <div>
          <h3>Quick Sort:</h3>
          <p>Time taken: {quickSortTime}</p>
          <p>Sorted list: {quickSortedArray.join(', ')}</p>
        </div>
      </div>
    </div>
  );
}

export default App;



