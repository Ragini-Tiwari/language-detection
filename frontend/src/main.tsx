import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'

// Grab the root element from index.html
const container = document.getElementById('root') as HTMLElement
const root = createRoot(container)

// Render the App component inside root
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
