// Senior Chess Improver: search, topic filter, comments and chess boards.

const slug = (value) =>
  String(value || "")
    .toLowerCase()
    .replace(/\+/g, " ")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");

/* ---------- Search ---------- */
(function search() {
  const panel = document.getElementById("search");
  const openButton = document.querySelector("[data-search-open]");
  const input = document.querySelector("[data-search-input]");
  const status = document.querySelector("[data-search-status]");
  const results = document.querySelector("[data-search-results]");
  const closeButton = document.querySelector("[data-search-close]");
  if (!panel || !openButton || !input) return;

  let entries = null;

  async function load() {
    if (entries) return entries;
    try {
      const response = await fetch(input.dataset.searchSrc);
      entries = await response.json();
    } catch (error) {
      entries = [];
      status.textContent = "Search couldn’t load. Reload the page and try again.";
    }
    return entries;
  }

  function open() {
    panel.hidden = false;
    openButton.setAttribute("aria-expanded", "true");
    input.focus();
    load();
  }

  function close() {
    panel.hidden = true;
    openButton.setAttribute("aria-expanded", "false");
    openButton.focus();
  }

  function render(query) {
    results.innerHTML = "";
    const words = query.toLowerCase().split(/\s+/).filter(Boolean);
    if (!words.length || !entries) {
      status.textContent = "";
      return;
    }
    const matches = entries.filter((entry) => {
      const haystack = [entry.title, entry.description, (entry.tags || []).join(" ")]
        .join(" ")
        .toLowerCase();
      return words.every((word) => haystack.includes(word));
    });
    status.textContent = matches.length
      ? `${matches.length} ${matches.length === 1 ? "post" : "posts"} found`
      : "No posts match. Try a shorter word or a tag such as ICCF.";
    for (const entry of matches.slice(0, 30)) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = entry.url;
      link.textContent = entry.title;
      const meta = document.createElement("span");
      meta.textContent = entry.date || "";
      item.append(link, meta);
      results.append(item);
    }
  }

  openButton.addEventListener("click", () => (panel.hidden ? open() : close()));
  closeButton.addEventListener("click", close);
  input.addEventListener("input", async () => {
    await load();
    render(input.value);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !panel.hidden) close();
    const typing = /input|textarea|select/i.test(document.activeElement?.tagName || "");
    if (event.key === "/" && panel.hidden && !typing) {
      event.preventDefault();
      open();
    }
  });
})();

/* ---------- Topics page: ?tag=name shows one topic ---------- */
(function topics() {
  const sections = document.querySelectorAll("[data-tag-section]");
  if (!sections.length) return;

  // Tags merged in the 2026 clean-up, so older links still land.
  const aliases = {
    "tournament": "tournaments",
    "opening": "openings",
    "21en9": "21en09",
    "megadatabase": "mega-database",
    "ultracorr23": "ultracorr",
    "chess-strategy": "strategy",
    "chessnutair": "chessnut-air",
  };

  const params = new URLSearchParams(window.location.search);
  let wanted = slug(params.get("tag"));
  wanted = aliases[wanted] || wanted;
  const target = wanted && document.querySelector(`[data-tag-section="${CSS.escape(wanted)}"]`);

  sections.forEach((section) => {
    section.hidden = Boolean(target) ? section !== target : true;
  });
  if (target) {
    const link = document.querySelector(`[data-tag-link="${CSS.escape(wanted)}"]`);
    if (link) link.setAttribute("aria-current", "true");
    const intro = document.querySelector("[data-tags-intro]");
    if (intro) intro.textContent = "Posts on this topic. All topics are listed below.";
    const chips = document.querySelector(".topics--page .chips");
    if (chips) chips.before(target);
  }
})();

/* ---------- Disqus comments, loaded when the reader gets near them ---------- */
(function comments() {
  const thread = document.getElementById("disqus_thread");
  if (!thread || !thread.dataset.disqus) return;
  const load = () => {
    window.disqus_config = function () {
      this.page.url = window.location.href.split("?")[0].split("#")[0];
    };
    const script = document.createElement("script");
    script.src = `https://${thread.dataset.disqus}.disqus.com/embed.js`;
    script.setAttribute("data-timestamp", String(Date.now()));
    script.async = true;
    document.body.append(script);
  };
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      if (entries.some((entry) => entry.isIntersecting)) {
        observer.disconnect();
        load();
      }
    }, { rootMargin: "300px" });
    observer.observe(thread);
  } else {
    load();
  }
})();

/* ---------- Chess boards ----------
   In a post, paste a game as a fenced code block marked pgn:
     ```pgn
     [White "Schroeer, Egbert"] ...
     1. e4 e5 2. Nf3 ...
     ```
   or a position as  <div class="board" data-fen="FEN"></div>
   Add data-orientation="black" to show the board from Black's side. */
(async function boards() {
  const blocks = [];
  document.querySelectorAll(".language-pgn").forEach((node) => {
    if (node.closest(".language-pgn") !== node) return;
    const outer = node.closest("div.language-pgn, pre") || node;
    if (blocks.some((block) => block.el === outer)) return;
    blocks.push({ el: outer, pgn: node.textContent.trim() });
  });
  document.querySelectorAll(".board[data-fen], .board[data-pgn]").forEach((el) => {
    blocks.push({ el, pgn: el.dataset.pgn || "*", fen: el.dataset.fen, orientation: el.dataset.orientation });
  });
  if (!blocks.length) return;

  const base = new URL("../lpv/", import.meta.url);
  for (const file of ["chessground.base.css", "chessground.cburnett.css", "lichess-pgn-viewer.css"]) {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = new URL(file, base).href;
    document.head.prepend(link);
  }

  let Viewer;
  try {
    Viewer = (await import(new URL("lichess-pgn-viewer.min.js", base).href)).default;
  } catch (error) {
    return; // Leave the PGN text in place if the viewer can't load.
  }

  for (const block of blocks) {
    const holder = document.createElement("div");
    holder.className = "board";
    const mount = document.createElement("div");
    holder.append(mount);
    block.el.replaceWith(holder);

    const isPosition = Boolean(block.fen);
    const sideToMove = isPosition && block.fen.split(" ")[1] === "b" ? "Black" : "White";
    Viewer(mount, {
      pgn: block.pgn,
      fen: block.fen || undefined,
      orientation: block.orientation || undefined,
      showPlayers: isPosition ? false : "auto",
      showMoves: isPosition ? false : "auto",
      showControls: !isPosition,
      showClocks: false,
      scrollToMove: false,
      lichess: false,
      menu: { getPgn: { enabled: !isPosition }, practiceWithComputer: { enabled: false }, analysisBoard: { enabled: false } },
    });

    if (isPosition) {
      const note = document.createElement("p");
      note.className = "board-note";
      const analyse = document.createElement("a");
      analyse.href = `https://lichess.org/analysis/standard/${block.fen.replace(/ /g, "_")}`;
      analyse.rel = "noopener";
      analyse.textContent = "Try it on an analysis board";
      note.append(`${sideToMove} to move. `, analyse);
      holder.after(note);
    }
  }
})();
