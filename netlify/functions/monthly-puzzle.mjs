// Rebuild the site early on the 1st and the 15th of each month: the Puzzle of
// the Month is dated the 1st, the game reviews in the blog the 15th.
//
// Puzzles are written ahead, each dated the 1st of its month, and a puzzle
// dated in the future is left out of a build (_plugins/future_puzzles.rb), so
// it appears at the first build after its date. This scheduled function
// starts that build. It runs only on the published site, not on
// Deploy Previews.
//
// Needs an environment variable PUZZLE_BUILD_HOOK holding the URL of a Netlify
// build hook (Project configuration > Build & deploy > Continuous deployment >
// Build hooks). Without it the function does nothing.
export default async () => {
  const hook = Netlify.env.get("PUZZLE_BUILD_HOOK");
  if (!hook) {
    console.log("PUZZLE_BUILD_HOOK is not set, so no rebuild was started.");
    return;
  }
  const response = await fetch(hook, { method: "POST" });
  console.log(`Rebuild requested; the build hook answered ${response.status}.`);
};

// 10:00 UTC on the 1st and the 15th: 2 am in Redmond in winter, 3 am in summer.
export const config = { schedule: "0 10 1,15 * *" };
