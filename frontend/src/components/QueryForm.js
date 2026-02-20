import { useState } from "react";
import axios from "axios";

export default function QueryForm() {
  const [question, setQuestion] = useState("");
  const [crop, setCrop] = useState("");
  const [location, setLocation] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    const res = await axios.post("http://127.0.0.1:8000/query/", {
      question,
      crop,
      location,
    });

    setResponse(res.data.answer);
  };

  return (
    <div className="bg-white shadow-xl rounded-2xl p-8 w-[600px]">
      <h1 className="text-3xl font-bold text-green-700 mb-6 text-center">
        🌾 KrishiSahay AI
      </h1>

      <input
        className="w-full border p-2 rounded mb-3"
        placeholder="Crop"
        onChange={(e) => setCrop(e.target.value)}
      />

      <input
        className="w-full border p-2 rounded mb-3"
        placeholder="Location"
        onChange={(e) => setLocation(e.target.value)}
      />

      <textarea
        className="w-full border p-2 rounded mb-3"
        placeholder="Ask your farming question..."
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        onClick={handleSubmit}
        className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700"
      >
        Get Advice
      </button>

      {response && (
        <div className="mt-6 p-4 bg-green-50 rounded">
          <h2 className="font-bold mb-2">AI Recommendation:</h2>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}