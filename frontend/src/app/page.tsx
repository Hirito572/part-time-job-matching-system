
"use client";

import { useEffect, useState } from "react";

interface ApiResponse {
  status: string;
  message: string;
}

export default function Home() {
  const [apiData, setApiData] = useState<ApiResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("http://localhost:8000/api/health/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("API request failed");
        }
        return response.json();
      })
      .then((data: ApiResponse) => setApiData(data))
      .catch(() => setError("Backend API-тай холбогдож чадсангүй."));
  }, []);

  return (
    <main className="min-h-screen flex flex-col items-center justify-center gap-4 p-8">
      <h1 className="text-3xl font-bold">
        Part-Time Job Matching System
      </h1>

      <h2 className="text-xl">Backend API Connection</h2>

      {apiData && (
        <div className="rounded-lg border p-6">
          <p>Status: {apiData.status}</p>
          <p>Message: {apiData.message}</p>
        </div>
      )}

      {error && <p className="text-red-500">{error}</p>}

      {!apiData && !error && <p>Connecting to backend...</p>}
      <p>Docker Layer Caching Test</p>
    </main>
  );
}
