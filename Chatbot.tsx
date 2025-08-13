// import React, { useState } from "react";
// import { askQuestion } from "../services/api";

// const Chatbot = () => {
//   const [question, setQuestion] = useState("");
//   const [answer, setAnswer] = useState("");

//   const handleAsk = async () => {
//     if (!question) return;
//     const response = await askQuestion(question);
//     setAnswer(response);
//   };

//   return (
//     <div style={{ padding: "20px" }}>
//       <h2>Symptom Chatbot</h2>
//       <input
//         type="text"
//         value={question}
//         onChange={(e) => setQuestion(e.target.value)}
//         placeholder="Type your question..."
//         style={{ width: "300px", padding: "5px" }}
//       />
//       <button onClick={handleAsk} style={{ marginLeft: "10px" }}>
//         Ask
//       </button>
//       <div style={{ marginTop: "20px" }}>
//         <strong>Bot:</strong> {answer}
//       </div>
//     </div>
//   );
// };

// export default Chatbot;

import React, { useState } from "react";

const chatbotData = [
{"instruction": "What is abdominal pain?", "response": "Abdominal pain is discomfort or pain that occurs anywhere between the chest and groin."},
  {"instruction": "What causes sudden severe abdominal pain?", "response": "Sudden severe abdominal pain may be caused by appendicitis, bowel obstruction, or a ruptured ulcer and needs urgent medical attention."},
  {"instruction": "Can stress cause abdominal pain?", "response": "Yes, stress can lead to abdominal pain by affecting gut motility and increasing sensitivity to pain."},
  {"instruction": "How is abdominal pain diagnosed?", "response": "Diagnosis may involve physical examination, blood tests, imaging like ultrasound or CT scan, and sometimes endoscopy."},
  {"instruction": "What treatments are available for abdominal pain?", "response": "Treatment depends on the cause and may include medications, lifestyle changes, or surgery."},
  {"instruction": "Is abdominal pain always a sign of something serious?", "response": "Not always; it can be due to minor issues like indigestion, but persistent or severe pain should be evaluated by a doctor."},
  {"instruction": "What symptoms along with abdominal pain indicate an emergency?", "response": "Symptoms like high fever, persistent vomiting, blood in stool, chest pain, or difficulty breathing along with abdominal pain require immediate medical care."},
  {"instruction": "What is abdominal pain?", "response": "Abdominal pain is discomfort or pain that occurs anywhere between the chest and groin."},
{"instruction": "What causes sudden severe abdominal pain?", "response": "Sudden severe abdominal pain may be caused by appendicitis, bowel obstruction, or a ruptured ulcer and needs urgent medical attention."},
{"instruction": "Can stress cause abdominal pain?", "response": "Yes, stress can lead to abdominal pain by affecting gut motility and increasing sensitivity to pain."},
{"instruction": "How is abdominal pain diagnosed?", "response": "Diagnosis may involve physical examination, blood tests, imaging like ultrasound or CT scan, and sometimes endoscopy."},
{"instruction": "What treatments are available for abdominal pain?", "response": "Treatment depends on the cause and may include medications, lifestyle changes, or surgery."},
{"instruction": "Is abdominal pain always a sign of something serious?", "response": "Not always; it can be due to minor issues like indigestion, but persistent or severe pain should be evaluated by a doctor."},
{"instruction": "What symptoms along with abdominal pain indicate an emergency?", "response": "Symptoms like high fever, persistent vomiting, blood in stool, chest pain, or difficulty breathing along with abdominal pain require immediate medical care."},
{"instruction": "Can diet affect abdominal pain?", "response": "Yes, certain foods can trigger or worsen abdominal pain, especially in conditions like irritable bowel syndrome."},
{"instruction": "What home remedies help with mild abdominal pain?", "response": "Rest, hydration, applying heat, and avoiding solid food for a few hours may help mild abdominal pain."},
{"instruction": "When should I seek emergency care for abdominal pain?", "response": "Seek emergency care if pain is sudden and severe, accompanied by dizziness, fainting, or if you cannot pass stool or gas."},
{"instruction": "What is functional abdominal pain?", "response": "Functional abdominal pain is chronic pain without a clear physical cause, often related to how the brain and gut communicate."},
{"instruction": "Can abdominal pain be a symptom of COVID-19?", "response": "Yes, some COVID-19 patients report abdominal pain along with other symptoms like fever and cough."},
{"instruction": "What are some common causes of abdominal pain in children?", "response": "Common causes include constipation, gastroenteritis, and sometimes appendicitis."},
{"instruction": "How do gallstones cause abdominal pain?", "response": "Gallstones can block bile ducts, causing intense pain in the upper right abdomen."},
{"instruction": "Can medications cause abdominal pain?", "response": "Certain medications, such as NSAIDs or antibiotics, can irritate the stomach and cause abdominal pain."},
{"instruction": "How long does abdominal pain usually last?", "response": "Duration varies; it can be minutes to hours in minor cases, but persistent pain over days needs medical evaluation."},
{"instruction": "What lifestyle changes help prevent abdominal pain?", "response": "Eating a balanced diet, regular exercise, avoiding smoking and excessive alcohol can help prevent abdominal pain."},
{"instruction": "Can abdominal pain be related to menstrual cycle?", "response": "Yes, many women experience abdominal pain related to their menstrual cycle due to hormonal changes."},
{"instruction": "What diagnostic tests are used for chronic abdominal pain?", "response": "Tests may include blood work, stool tests, imaging, endoscopy, and sometimes specialized tests like manometry."},
{"instruction": "How can irritable bowel syndrome cause abdominal pain?", "response": "IBS causes abdominal pain through abnormal muscle contractions and increased sensitivity of the intestines."},
{ "instruction": "Hi", "response": "Hi! How can I assist you?" },
  { "instruction": "How are you?", "response": "I’m doing well, thank you! How about you?" },
  { "instruction": "Good morning", "response": "Good morning! How can I assist you today?" },
  { "instruction": "Good evening", "response": "Good evening! What can I help you with?" },
  { "instruction": "Thanks", "response": "You're welcome! Let me know if you have any questions." },
  { "instruction": "Bye", "response": "Goodbye! Take care!" }
];

function Chatbot() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = () => {
    // find the answer from dataset
    const item = chatbotData.find(q => q.instruction.toLowerCase() === question.trim().toLowerCase());
    if (item) {
      setAnswer(item.response);
    } else {
      setAnswer("I'm sorry, I don't have information on that topic yet.");
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "500px", margin: "auto" }}>
      <h2>Symptom Chatbot</h2>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a question..."
        style={{ width: "100%", padding: "10px", marginBottom: "10px" }}
      />
      <button onClick={handleAsk} style={{ padding: "10px 20px" }}>Ask</button>
      <div style={{ marginTop: "20px", minHeight: "50px", border: "1px solid #ccc", padding: "10px" }}>
        <strong>Bot:</strong> {answer}
      </div>
    </div>
  );
}

export default Chatbot;


