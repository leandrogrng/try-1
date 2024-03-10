import { useState } from 'react'
import './App.css'
import BarChart from './components/BarChart';
import {UserData} from './Data'

function App() {
  const [userData, setUserData] = useState({
    labels: UserData.map((data) => data.timestamp_seconds),
    datasets: [
      {
        label: 'Water temperature',
        data: UserData.map((data) => data.temperature_celsius),
      }
    ]
  });

  return (
    <div className = 'App'>
      <h1>Water Temperature</h1>
      <BarChart chartData = {userData}/>
    </div>
  )
}

export default App;
