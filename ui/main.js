const vajraContainer = document.getElementById("vajra-container");
const vajraText = document.querySelector(".vajra-text");

function setState(state, message) {
  vajraContainer.className = state;
  if (message) vajraText.textContent = message;
}

/* TEMP DEMO FLOW (for testing UI only) */
setState("idle", "Friday is ready");

setTimeout(() => {
  setState("listening", "Listening…");
}, 2000);

setTimeout(() => {
  setState("thinking", "Thinking…");
}, 4500);

setTimeout(() => {
  setState("responding", "Done.");
}, 7000);

setTimeout(() => {
  setState("idle", "Friday is ready");
}, 9000);
