import React, { useState, useEffect } from 'react';
import './App.css';
import  TableComponent from './components/TableComponent'

const SERVER_URL = 'http://127.0.0.1:5000/stats'

const App = () => {
  const [initialData, setInitialData] = useState([])
  const [filter, setFilter] = useState("")

  useEffect(() => {
    async function get_data() {
      await fetch(SERVER_URL).then(res => res.json()).then(data => {
          setInitialData(data)
      })
    }
    get_data()
    const timer = setInterval(() => {
      get_data()
    }, 5000)

    return () => clearInterval(timer)
  }, [])

  if (initialData.length === 0) return <div>fetching data</div>
  return (
    <div className="App">
      <header className="App-header">
        <h3>
          Tweets Statistics
        </h3>
        <input className="search-area" placeholder="Search.." onChange={ e => setFilter(e.target.value)}></input>
      </header>
      <TableComponent data={initialData} filter={filter}></TableComponent>
    </div>
  )
}

export default App;
