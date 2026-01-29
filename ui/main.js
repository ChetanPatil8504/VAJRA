async function checkVajraStatus() {
  try {
    const response = await fetch("http://127.0.0.1:5000/status");
    const data = await response.json();

    console.log("VAJRA STATUS:", data);

    const title = document.querySelector("h1");
    const subtitle = document.querySelector("p");

    title.textContent = data.assistant;
    subtitle.textContent = data.message;
  } catch (error) {
    console.error("Failed to connect to VAJRA brain", error);
  }
}

// Call backend when UI loads
checkVajraStatus();
