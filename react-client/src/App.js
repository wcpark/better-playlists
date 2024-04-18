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
import React, { useState } from 'react';
import './App.css';

function App() {
  const [searchQuery, setSearchQuery] = useState('');
  const [output, setOutput] = useState('');

  const handleSearch = () => {
    // Here you can implement logic to handle the search query
    // For simplicity, let's just set the output to the search query
    setOutput(searchQuery);
  };

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
    </div>
  );
}

export default App;
