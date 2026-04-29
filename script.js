const username = "mexicanbr0auth";

const reposContainer = document.getElementById("repos");
const languagesContainer = document.getElementById("languages");

const repoCount = document.getElementById("repoCount");
const langCount = document.getElementById("langCount");
const starCount = document.getElementById("starCount");

async function loadRepos() {
  try {
    const response = await fetch(`https://api.github.com/users/${username}/repos?sort=updated&per_page=100`);
    const repos = await response.json();

    const filtered = repos.filter(repo => !repo.fork);
    const languages = new Set();
    let stars = 0;

    repoCount.textContent = filtered.length;

    filtered.forEach(repo => {
      if (repo.language) languages.add(repo.language);
      stars += repo.stargazers_count;

      const card = document.createElement("div");
      card.className = "card";

      card.innerHTML = `
        <h3>${repo.name}</h3>
        <p>${repo.description || "Projeto desenvolvido para estudo, automação ou ferramentas práticas."}</p>

        <div class="info">
          <span>${repo.language || "Código"}</span>
          <span>⭐ ${repo.stargazers_count}</span>
        </div>

        <a href="${repo.html_url}" target="_blank">Ver projeto</a>
      `;

      reposContainer.appendChild(card);
    });

    starCount.textContent = stars;
    langCount.textContent = languages.size;

    languages.forEach(lang => {
      const chip = document.createElement("span");
      chip.className = "chip";
      chip.textContent = lang;
      languagesContainer.appendChild(chip);
    });

  } catch (error) {
    reposContainer.innerHTML = "<p>Erro ao carregar repositórios.</p>";
  }
}

loadRepos();
