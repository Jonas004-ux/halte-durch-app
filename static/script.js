async function loadMessages() {
  const res = await fetch('/get_messages');
  const data = await res.json();
  const feed = document.getElementById('feed');
  if (!feed) return;
  feed.innerHTML = '';
  data.forEach(msg => {
    const div = document.createElement('div');
    div.className = 'message';
    div.innerHTML = `
      <p><strong>${msg.situation}</strong> <span class="time">(${msg.timestamp})</span></p>
      <ul>
        ${msg.responses.map(r => `<li>💬 ${r}</li>`).join('')}
      </ul>
      <form method="POST" action="/post_response/${msg.id}">
        <input name="response" placeholder="Du schaffst das! 💪" required>
        <button class="btn green">Antworten</button>
      </form>
    `;
    feed.appendChild(div);
  });
}

document.addEventListener('DOMContentLoaded', loadMessages);
