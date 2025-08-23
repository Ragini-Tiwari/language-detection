import { useState } from "react";
import {
  PieChart, Pie, Cell, Tooltip,
  BarChart, Bar, XAxis, YAxis, CartesianGrid,
} from "recharts";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const analyzeText = async () => {
    setLoading(true);
    setResult(null);
    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  const COLORS = ["#00C49F", "#FFBB28", "#FF4444"];

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold mb-6 flex items-center gap-2">
        🤖 Language & Sentiment Analyzer
      </h1>

      <div className="flex gap-10 w-full max-w-6xl">
        {/* Left: Input + Results */}
        <div className="flex-1">
          <textarea
            className="w-full p-4 rounded-lg text-black"
            rows={5}
            placeholder="Type your text here..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />

          <button
            onClick={analyzeText}
            className="mt-4 px-6 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg"
            disabled={loading}
          >
            {loading ? "Analyzing..." : "Analyze"}
          </button>

          {result && (
            <div className="mt-6 grid gap-6">
              {/* Language */}
              <div className="p-4 bg-gray-800 rounded-lg">
                <h2 className="font-semibold text-lg">🌐 Language</h2>
                <p>
                  {result.language} (
                  {(result.confidence * 100).toFixed(2)}%)
                </p>
                {/* Bar Chart */}
                <BarChart
                  width={400}
                  height={200}
                  data={[
                    { name: result.language, score: result.confidence * 100 },
                  ]}
                >
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="score" fill="#8884d8" />
                </BarChart>
              </div>

              {/* Sentiment */}
              <div className="p-4 bg-gray-800 rounded-lg">
                <h2 className="font-semibold text-lg">😊 Sentiment</h2>
                <p>{result.sentiment}</p>
                {/* Pie Chart */}
                <PieChart width={400} height={250}>
                  <Pie
                    data={[
                      { name: "Positive", value: result.sentiment === "positive" ? 1 : 0 },
                      { name: "Neutral", value: result.sentiment === "neutral" ? 1 : 0 },
                      { name: "Negative", value: result.sentiment === "negative" ? 1 : 0 },
                    ]}
                    cx="50%"
                    cy="50%"
                    outerRadius={80}
                    dataKey="value"
                    label
                  >
                    {COLORS.map((c, i) => (
                      <Cell key={i} fill={c} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </div>

              {/* Toxicity */}
              <div className="p-4 bg-gray-800 rounded-lg">
                <h2 className="font-semibold text-lg">⚠️ Toxicity</h2>
                <p>
                  {result.toxicity.label} (
                  {(result.toxicity.score * 100).toFixed(2)}%)
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Right: Robot Girl Avatar */}
        <div className="flex flex-col items-center justify-center">
          <img
          src="/robotgirl.png"   // ✅ no ./public, just the root path
          alt="AI Robot Girl"
          className="w-64 h-64 object-contain animate-bounce"
  />
          <p className="mt-2 text-sm text-gray-300">Your AI Assistant 🤖💬</p>
        </div>
      </div>
    </div>
  );
}

export default App;
