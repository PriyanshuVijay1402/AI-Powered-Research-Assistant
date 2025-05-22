document.getElementById("get-started").addEventListener("click", () => {
  document.getElementById("welcome-screen").style.display = "none";
  document.getElementById("main-app").classList.remove("hidden");
});

// Optional: handle form submission
document.getElementById("research-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const topic = document.getElementById("topic-input").value;
  const resultDiv = document.getElementById("result");
  const resultSection = document.getElementById("result-section");

  resultDiv.textContent = "🔎 Fetching results...";
  resultSection.style.display = "block";

  // Example placeholder call
  const response = await fetch("/generate-report", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_input: topic }),
  });

  const data = await response.text();
  resultDiv.textContent = data;
});
