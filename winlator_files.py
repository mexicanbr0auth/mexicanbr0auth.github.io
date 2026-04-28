<!DOCTYPE html><html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Winlator Bionic WCP Downloader</title>
  <style>
    :root {
      --bg: #0f172a;
      --bg2: #111827;
      --card: #1e293b;
      --card2: #020617;
      --text: #e5e7eb;
      --muted: #94a3b8;
      --primary: #7c3aed;
      --primary2: #22d3ee;
      --border: rgba(148, 163, 184, 0.18);
      --ok: #22c55e;
    }* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  background:
    radial-gradient(circle at top left, rgba(124, 58, 237, 0.28), transparent 35%),
    radial-gradient(circle at top right, rgba(34, 211, 238, 0.18), transparent 30%),
    var(--bg);
  color: var(--text);
  min-height: 100vh;
}

header {
  padding: 34px 18px 24px;
  text-align: center;
}

header h1 {
  margin: 0;
  font-size: clamp(2rem, 6vw, 4rem);
  letter-spacing: -1px;
  background: linear-gradient(90deg, #a78bfa, #22d3ee);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

header p {
  margin: 12px auto 0;
  color: var(--muted);
  max-width: 760px;
  line-height: 1.6;
}

.wrap {
  width: min(1180px, calc(100% - 28px));
  margin: 0 auto 40px;
}

.panel {
  background: rgba(15, 23, 42, 0.72);
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 16px;
  backdrop-filter: blur(14px);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.22);
  position: sticky;
  top: 10px;
  z-index: 5;
}

.controls {
  display: grid;
  grid-template-columns: 1fr 210px 170px;
  gap: 12px;
}

input, select, button {
  width: 100%;
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 13px 14px;
  background: rgba(2, 6, 23, 0.72);
  color: var(--text);
  outline: none;
  font-size: 15px;
}

input:focus, select:focus {
  border-color: rgba(34, 211, 238, 0.6);
}

button {
  cursor: pointer;
  background: linear-gradient(135deg, var(--primary), var(--primary2));
  border: none;
  font-weight: bold;
  transition: transform 0.15s ease, opacity 0.15s ease;
}

button:hover {
  transform: translateY(-1px);
  opacity: 0.95;
}

.stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin: 16px 0 22px;
}

.stat {
  background: rgba(30, 41, 59, 0.72);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 14px;
}

.stat strong {
  display: block;
  font-size: 24px;
}

.stat span {
  color: var(--muted);
  font-size: 13px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 14px;
}

.card {
  background: linear-gradient(180deg, rgba(30, 41, 59, 0.92), rgba(2, 6, 23, 0.84));
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 16px;
  min-height: 190px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: 0 18px 38px rgba(0, 0, 0, 0.18);
}

.type {
  width: fit-content;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(124, 58, 237, 0.18);
  border: 1px solid rgba(124, 58, 237, 0.38);
  color: #ddd6fe;
  font-size: 12px;
  font-weight: bold;
}

.name {
  font-weight: bold;
  font-size: 17px;
  line-height: 1.35;
  word-break: break-word;
}

.url {
  color: var(--muted);
  font-size: 12px;
  line-height: 1.4;
  word-break: break-all;
  flex: 1;
}

.actions {
  display: grid;
  grid-template-columns: 1fr 42px;
  gap: 8px;
}

.download {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  color: white;
  background: linear-gradient(135deg, var(--primary), var(--primary2));
  border-radius: 14px;
  padding: 12px;
  font-weight: bold;
  font-size: 14px;
}

.copy {
  padding: 0;
  border-radius: 14px;
  background: rgba(148, 163, 184, 0.14);
  border: 1px solid var(--border);
}

.empty, .loading {
  text-align: center;
  color: var(--muted);
  padding: 30px;
}

footer {
  color: var(--muted);
  text-align: center;
  padding: 22px;
  font-size: 13px;
}

@media (max-width: 760px) {
  .controls, .stats {
    grid-template-columns: 1fr;
  }

  .panel {
    position: static;
  }
}

  </style>
</head>
<body>
  <header>
    <h1>WCP Downloader</h1>
    <p>Baixe builds de Box64, DXVK, FEXCore, Proton, VKD3D, WOWBox64 e Wine direto do repositório Winlator Bionic Nightly.</p>
  </header>  <main class="wrap">
    <section class="panel">
      <div class="controls">
        <input id="search" placeholder="Pesquisar: dxvk, proton, wine, arm64ec..." />
        <select id="typeFilter">
          <option value="all">Todos os tipos</option>
        </select>
        <button id="reloadBtn">Atualizar lista</button>
      </div>
    </section><section class="stats" id="stats"></section>
<section id="list" class="grid"><div class="loading">Carregando lista...</div></section>

  </main>  <footer>
    Fonte: content.json do GitHub. Os botões apontam para os downloads originais.
  </footer>  <script>
    const JSON_URL = "https://raw.githubusercontent.com/Xnick417x/Winlator-Bionic-Nightly-wcp/refs/heads/main/content.json";

    const list = document.getElementById("list");
    const search = document.getElementById("search");
    const typeFilter = document.getElementById("typeFilter");
    const stats = document.getElementById("stats");
    const reloadBtn = document.getElementById("reloadBtn");

    let packages = [];

    async function loadData() {
      list.innerHTML = '<div class="loading">Carregando lista...</div>';

      try {
        const res = await fetch(JSON_URL, { cache: "no-store" });
        if (!res.ok) throw new Error("Falha ao carregar JSON");

        packages = await res.json();
        buildTypeOptions();
        render();
      } catch (err) {
        list.innerHTML = `
          <div class="empty">
            Não consegui carregar o JSON remoto.<br><br>
            Dica: abra por um servidor local, não direto pelo arquivo.<br>
            Exemplo: <b>python -m http.server 8080</b>
          </div>
        `;
      }
    }

    function buildTypeOptions() {
      const selected = typeFilter.value;
      const types = [...new Set(packages.map(item => item.type))].sort();

      typeFilter.innerHTML = '<option value="all">Todos os tipos</option>';
      for (const type of types) {
        const option = document.createElement("option");
        option.value = type;
        option.textContent = type;
        typeFilter.appendChild(option);
      }

      typeFilter.value = types.includes(selected) ? selected : "all";
    }

    function renderStats(filtered) {
      const total = packages.length;
      const showing = filtered.length;
      const types = new Set(packages.map(item => item.type)).size;
      const latest = packages[0]?.verName || "N/A";

      stats.innerHTML = `
        <div class="stat"><strong>${total}</strong><span>Total de arquivos</span></div>
        <div class="stat"><strong>${showing}</strong><span>Exibindo agora</span></div>
        <div class="stat"><strong>${types}</strong><span>Categorias</span></div>
        <div class="stat"><strong>${latest}</strong><span>Primeiro da lista</span></div>
      `;
    }

    function render() {
      const term = search.value.toLowerCase().trim();
      const type = typeFilter.value;

      const filtered = packages.filter(item => {
        const text = `${item.type} ${item.verName} ${item.remoteUrl}`.toLowerCase();
        const matchSearch = !term || text.includes(term);
        const matchType = type === "all" || item.type === type;
        return matchSearch && matchType;
      });

      renderStats(filtered);

      if (!filtered.length) {
        list.innerHTML = '<div class="empty">Nada encontrado.</div>';
        return;
      }

      list.innerHTML = filtered.map(item => `
        <article class="card">
          <div class="type">${escapeHtml(item.type)}</div>
          <div class="name">${escapeHtml(item.verName)}</div>
          <div class="url">${escapeHtml(item.remoteUrl)}</div>
          <div class="actions">
            <a class="download" href="${item.remoteUrl}" download>Baixar</a>
            <button class="copy" onclick="copyUrl('${encodeURIComponent(item.remoteUrl)}')" title="Copiar URL">📋</button>
          </div>
        </article>
      `).join("");
    }

    function escapeHtml(text) {
      return String(text)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
    }

    async function copyUrl(encodedUrl) {
      const url = decodeURIComponent(encodedUrl);
      await navigator.clipboard.writeText(url);
      alert("URL copiada!");
    }

    search.addEventListener("input", render);
    typeFilter.addEventListener("change", render);
    reloadBtn.addEventListener("click", loadData);

    loadData();
  </script></body>
</html>
