document.addEventListener('DOMContentLoaded', function() {
  const flowSteps = document.querySelectorAll('.flow-step');
  const explanationBox = document.getElementById('flow-explanation');

  if (!explanationBox) return;

  flowSteps.forEach(step => {
    step.addEventListener('click', function() {
      const title = this.querySelector('strong').textContent;
      const desc = this.dataset.explanation || '此阶段是工程设计流程的核心环节。';
      explanationBox.innerHTML = `<strong>${title}</strong><p>${desc}</p>`;
      explanationBox.style.display = 'block';
    });
  });
});