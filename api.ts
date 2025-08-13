// // frontend/src/services/api.ts

export async function askQuestion(question: string) {
  try {
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }),
    });

    if (!response.ok) {
      throw new Error("Failed to fetch answer from backend");
    }

    const data = await response.json();
    return data.answer;
  } catch (error) {
    console.error(error);
    return "Sorry, something went wrong.";
  }
}
// export const askQuestion = async (payload: { question: string; age: number; gender: string }) => {
//   const res = await fetch("http://127.0.0.1:8000/chat", {
//     method: "POST",
//     headers: { "Content-Type": "application/json", accept: "application/json" },
//     body: JSON.stringify(payload),
//   });
//   if (!res.ok) throw new Error(`HTTP ${res.status}`);
//   return res.json(); // { answer: string }
// };
