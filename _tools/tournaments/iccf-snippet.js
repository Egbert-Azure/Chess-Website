// Saves all your ICCF tournaments (running and finished) into one file,
// iccf-events.json, in Downloads. Paste it into Safari's JavaScript console
// while you are on any page of www.iccf.com (see README.md).
// It only reads ICCF pages, one per second, and sends nothing anywhere.
(async () => {
  const pause = () => new Promise((r) => setTimeout(r, 1000));
  const get = async (url) => {
    try {
      const res = await fetch(url, { credentials: "include" });
      return res.ok ? await res.text() : `HTTP ${res.status}`;
    } catch (e) {
      return `ERROR ${e}`;
    }
  };
  // "My events": the running list, then the finished list, page by page
  // (ICCF switches and pages that list with form postbacks)
  const postback = async (html, target, arg) => {
    const fields = new FormData(new DOMParser().parseFromString(html, "text/html").getElementById("form1"));
    fields.set("__EVENTTARGET", target);
    fields.set("__EVENTARGUMENT", arg);
    fields.set("ctl00$ContentPlaceHolder1$chkFinished", "on");
    const res = await fetch("/myevents", { method: "POST", body: new URLSearchParams(fields), credentials: "include" });
    return res.text();
  };
  const pages = { myevents: await get("/myevents") };
  let list = await postback(pages.myevents, "ctl00$ContentPlaceHolder1$chkFinished", "");
  pages.myevents_finished_1 = list;
  for (let page = 2; list.includes(`Page$${page}`) && page < 20; page += 1) {
    await pause();
    list = await postback(list, "ctl00$ContentPlaceHolder1$MxDataGrid1", `Page$${page}`);
    pages[`myevents_finished_${page}`] = list;
  }
  const lists = Object.keys(pages).filter((k) => k.startsWith("myevents")).map((k) => pages[k]).join("");

  const ids = [...new Set([...lists.matchAll(/event\?id=(\d+)/g)].map((m) => Number(m[1])))]
    .sort((a, b) => a - b);
  console.log(`Found ${ids.length} tournaments.`);
  let n = 0;
  for (const id of ids) {
    n += 1;
    const html = await get(`/event?id=${id}`);
    pages[`event-${id}`] = html;
    console.log(`${n} of ${ids.length}: tournament ${id} ${html.startsWith("HTTP") || html.startsWith("ERROR") ? html : "ok"}`);
    let k = 0;
    for (const m of html.matchAll(/href="([^"]*pgn[^"]*)"/gi)) {
      k += 1;
      pages[`event-${id}-games-${k}`] = await get(new URL(m[1].replace(/&amp;/g, "&"), location.href).href);
      await pause();
    }
    await pause();
  }
  const link = document.createElement("a");
  link.href = URL.createObjectURL(new Blob([JSON.stringify(pages)], { type: "application/json" }));
  link.download = "iccf-events.json";
  document.body.append(link);
  link.click();
  link.remove();
  console.log("Done: iccf-events.json is in your Downloads folder.");
})();
