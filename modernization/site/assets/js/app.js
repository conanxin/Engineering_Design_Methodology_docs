document.addEventListener('DOMContentLoaded', function() {
  // Flow step interaction (existing)
  const flowSteps = document.querySelectorAll('.flow-step');
  const explanationBox = document.getElementById('flow-explanation');

  if (explanationBox) {
    flowSteps.forEach(step => {
      step.addEventListener('click', function() {
        const title = this.textContent;
        explanationBox.innerHTML = `<strong>${title}</strong><p>此阶段是工程设计流程的核心环节。</p>`;
        explanationBox.style.display = 'block';
      });
    });
  }

  // Global search (homepage)
  const globalSearch = document.getElementById('global-search');
  const searchResults = document.getElementById('search-results');

  if (globalSearch && searchResults) {
    globalSearch.addEventListener('input', async function() {
      const q = this.value.toLowerCase().trim();
      if (!q) {
        searchResults.innerHTML = '';
        return;
      }

      const files = ['chapters', 'concepts', 'checklists', 'workflows', 'cases'];
      let resultsHTML = '';

      for (const file of files) {
        try {
          const res = await fetch(`data/${file}.json`);
          const data = await res.json();
          let matches = [];

          if (file === 'chapters') {
            matches = data.filter(item => 
              item.title.toLowerCase().includes(q) || 
              (item.summary && item.summary.toLowerCase().includes(q))
            );
          } else if (file === 'concepts') {
            matches = data.filter(item => 
              item.term.toLowerCase().includes(q) || 
              item.definition.toLowerCase().includes(q)
            );
          } else if (file === 'cases') {
            matches = data.filter(item => 
              item.title.toLowerCase().includes(q) || 
              item.scenario.toLowerCase().includes(q)
            );
          }

          if (matches.length > 0) {
            resultsHTML += `<h4>${file}</h4>`;
            matches.slice(0, 3).forEach(m => {
              const title = m.title || m.term || m.scenario || 'Untitled';
              const link = m.page_url ? m.page_url : '#';
              resultsHTML += `<div class="search-result-item"><a href="${link}">${title}</a></div>`;
            });
          }
        } catch (e) {}
      }

      searchResults.innerHTML = resultsHTML || '<p>未找到匹配结果</p>';
    });
  }

  // Copy template buttons
  document.querySelectorAll('.copy-template').forEach(btn => {
    btn.addEventListener('click', async function() {
      const templateName = this.dataset.template;
      const pre = this.parentElement.querySelector('pre');
      if (!pre) return;

      const text = pre.textContent;
      try {
        await navigator.clipboard.writeText(text);
        const original = this.textContent;
        this.textContent = '已复制！';
        setTimeout(() => { this.textContent = original; }, 1500);
      } catch (e) {
        alert('请手动复制：\n' + text);
      }
    });
  });

  // Load chapters grid on homepage
  const chaptersGrid = document.getElementById('chapters-grid');
  if (chaptersGrid) {
    fetch('data/chapters.json')
      .then(r => r.json())
      .then(data => {
        chaptersGrid.innerHTML = data.map(ch => `
          <div class="card">
            <strong>Unit ${ch.id}</strong><br>
            <small>${ch.title}</small>
            <p>${ch.summary || ch.role}</p>
            <a href="${ch.page_url}" class="btn">进入章节</a>
          </div>
        `).join('');
      });
  }

  // Load concepts on concepts.html
  if (window.location.pathname.includes('concepts.html')) {
    loadConcepts();
  }
});

async function loadConcepts() {
  const container = document.getElementById('concepts-grid');
  if (!container) return;

  const searchInput = document.getElementById('concept-search');
  
  const res = await fetch('data/concepts.json');
  const concepts = await res.json();

  function render(filtered) {
    container.innerHTML = filtered.map(c => `
      <div class="card">
        <h3>${c.term}</h3>
        <p>${c.definition}</p>
        <small>章节：${c.chapter} | 现代映射：${c.modern_mapping}</small>
        <p><em>Agent 提示：${c.agent_prompt_hint}</em></p>
      </div>
    `).join('');
  }

  render(concepts);

  if (searchInput) {
    searchInput.addEventListener('input', () => {
      const q = searchInput.value.toLowerCase();
      const filtered = concepts.filter(c => 
        c.term.toLowerCase().includes(q) || 
        c.definition.toLowerCase().includes(q)
      );
      render(filtered);
    });
  }
}
// Phase 2C additions
document.addEventListener('DOMContentLoaded', function() {
  // Back to top button
  const backToTop = document.createElement('button');
  backToTop.className = 'back-to-top';
  backToTop.innerHTML = '↑';
  backToTop.setAttribute('aria-label', '返回顶部');
  document.body.appendChild(backToTop);

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTop.classList.add('visible');
    } else {
      backToTop.classList.remove('visible');
    }
  });

  backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // Mobile menu toggle
  const nav = document.querySelector('.site-nav');
  if (nav) {
    const menuBtn = document.createElement('button');
    menuBtn.className = 'mobile-menu-btn';
    menuBtn.innerHTML = '☰';
    menuBtn.setAttribute('aria-label', '打开菜单');
    
    const navLinks = nav.querySelector('.nav-links') || nav;
    nav.insertBefore(menuBtn, navLinks);
    
    menuBtn.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });
  }

  // Generate simple page TOC for long pages
  const tocContainer = document.querySelector('.page-toc');
  if (tocContainer) {
    const headings = document.querySelectorAll('h2, h3');
    if (headings.length > 0) {
      const ul = document.createElement('ul');
      headings.forEach((h, i) => {
        if (!h.id) h.id = 'section-' + i;
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.textContent;
        li.appendChild(a);
        ul.appendChild(li);
      });
      tocContainer.appendChild(ul);
    }
  }
});
