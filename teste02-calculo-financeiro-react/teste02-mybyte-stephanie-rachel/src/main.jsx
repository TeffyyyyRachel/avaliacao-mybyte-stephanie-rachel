import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App frase="teste"/>
    <App frase="teste 02"/>
    <App frase="Consegui!"/>
  </StrictMode>,
)
