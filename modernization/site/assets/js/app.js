document.addEventListener('DOMContentLoaded', function() {
  // Flow step explanations (homepage)
  const flowSteps = document.querySelectorAll('.flow-step');
  const explanationBox = document.getElementById('flow-explanation');

  if (explanationBox) {
    flowSteps.forEach(step => {
      step.addEventListener('click', function() {
        const title = this.querySelector('strong').textContent;
        const desc = this.dataset.explanation || '此阶段是工程设计流程的核心环节。';
        explanationBox.innerHTML = `<strong>${title}</strong><p>${desc}</p>`;
        explanationBox.style.display = 'block';
      });
    });
  }

  // Chapter card accessibility enhancement
  const chapterCards = document.querySelectorAll('.card-grid .card');
  chapterCards.forEach(card => {
    card.setAttribute('tabindex', '0');
    card.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        const link = card.getAttribute('href');
        if (link) window.location.href = link;
      }
    });
  });
});