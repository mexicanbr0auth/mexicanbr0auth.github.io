const CONFIG = {
  username: "mexicanbr0auth",
  maxRepos: 100
};

const state = {
  repos: [],
  languages: new Set()
};

const els = {
  repos: document.getElementById("repos"),
  languages: document.getElementById("languages"),
  repoCount: document.getElementById("repoCount"),
  langCount: document.getElementById("langCount"),
  starCount: document.getElementById("starCount"),
  searchInput: document.getElementById("searchInput"),
  languageFilter: document.getElementById("languageFilter")
};

function fallbackDescription(repo) {
  const name = repo.name.toLowerCase();

  if (name.includes("bot")) return "Bot desenvolvido para automação, APIs e integração com serviços externos.";
  if (name.includes("crypto") || name.includes("cotacao")) return "Ferramenta voltada para criptomoedas, cotações e monitoramento de mercado.";
  if (name.includes("termux")) return "Projeto focado em Linux/Android, Termux e automação em ambiente mobile.";
  if (name.includes("site") || name.includes("github.io")) return "Projeto web publicado com GitHub Pages.";
  
  return "Projeto criado para estudo, desenvolvimento prático e construção de ferramentas úteis.";
}

function normalizeRepo(repo) {
  return {
    name: repo.name,
    description: repo.description || fallbackDescription(repo),
    language: repo.language || "Outro",
    stars: repo.stargazers_count || 0,
    forks: repo.forks_count || 0,
    url: repo.html_url,
    updated: new Date(repo.updated_at).toLocaleDateString("pt-BR")
  };
}

function renderStats() {
  const totalStars = state.repos.reduce((acc, repo) => acc + repo.stars, 0);

  els.repoCount.textContent = state.repos.length;
  els.langCount.textContent = state.languages.size;
  els.starCount.textContent = totalStars;
}

function renderLanguages() {
  els.languages.innerHTML = "";

  [...state.languages].sort().forEach(language => {
    const chip = document.createElement("span");
    chip.className = "chip";
    chip.textContent = language;
    els.languages.appendChild(chip);

    const option = document.createElement("option");
    option.value = language;
    option.textContent = language;
    els.languageFilter.appendChild(option);
  });
}

function renderRepos() {
  const search = els.searchInput.value.toLowerCase();
  const selectedLanguage = els.languageFilter.value;

  const filtered = state.repos.filter(repo => {
    const matchesSearch =
      repo.name.toLowerCase().includes(search) ||
      repo.description.toLowerCase().includes(search);

    const matchesLanguage =
      selectedLanguage === "all" || repo.language === selectedLanguage;

    return matchesSearch && matchesLanguage;
  });

  els.repos.innerHTML = "";

  if (!filtered.length) {
    els.repos.innerHTML = `<div class="empty">Nenhum projeto encontrado.</div>`;
    return;
  }

  filtered.forEach(repo => {
    const card = document.createElement("article");
    card.className = "project-card";

    card.innerHTML = `
      <h3>${repo.name}</h3>
      <p>${repo.description}</p>

      <div class="project-meta">
        <span>${repo.language}</span>
        <span>⭐ ${repo.stars}</span>
        <span>⑂ ${repo.forks}</span>
      </div>

      <small>Atualizado em ${repo.updated}</small>
      <br>
      <a href="${repo.url}" target="_blank" rel="noopener noreferrer">Abrir projeto</a>
    `;

    els.repos.appendChild(card);
  });
}

async function loadGitHubRepos() {
  els.repos.innerHTML = `<div class="loading">Carregando projetos do GitHub...</div>`;

  try {
    const url = `https://api.github.com/users/${CONFIG.username}/repos?sort=updated&per_page=${CONFIG.maxRepos}`;
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error("Erro ao acessar API do GitHub");
    }

    const data = await response.json();

    state.repos = data
      .filter(repo => !repo.fork)
      .map(normalizeRepo)
      .sort((a, b) => b.stars - a.stars);

    state.repos.forEach(repo => state.languages.add(repo.language));

    renderStats();
    renderLanguages();
    renderRepos();

  } catch (error) {
    els.repos.innerHTML = `
      <div class="empty">
        Não foi possível carregar os repositórios agora.
      </div>
    `;
  }
}

els.searchInput.addEventListener("input", renderRepos);
els.languageFilter.addEventListener("change", renderRepos);

loadGitHubRepos();
