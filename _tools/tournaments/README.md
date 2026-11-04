# Tournaments page: how to update it

The Tournaments page (`_pages/tournaments.html`) shows whatever is in
`_data/tournaments.yml`. That file is made from ICCF, so nothing on the page
is typed in by hand. To bring it up to date:

1. **Save your tournaments from ICCF.** In Safari, open any page on
   www.iccf.com (being logged in is fine). Choose **Develop → Show JavaScript
   Console**, click into the bottom line of the console, paste the whole of
   `iccf-snippet.js`, and press Return. After a minute or two it says *Done*,
   and `iccf-events.json` is in Downloads.
   (If there is no Develop menu: Safari → Settings → Advanced → tick
   "Show features for web developers".)

2. **Rebuild the data file.** In VS Code's terminal, in the Chess-Website folder:

   ```
   python3 _tools/tournaments/build.py ~/Downloads/iccf-events.json
   ```

   It prints how many tournaments it found and how many are running.

3. **Check and publish** as usual: branch, commit `_data/tournaments.yml`,
   push, look at the Deploy Preview, merge.

## Good to know

- ICCF blocks scripts that fetch its pages from outside a browser, which is why
  step 1 runs inside Safari.
- `manual.json` holds the tournaments ICCF doesn't know about: the 2021
  Electronic Knights sections played on the US Chess server. Edit it there;
  an entry is skipped once ICCF reports the same section.
- Names ICCF only knows by a code (21VP04, WS/CCE/A/30) are set in `NAMES`
  at the top of `build.py`.
- Annotated games are the pages in `_tournaments/`. The page links them to
  their Electronic Knights section through the `section:` line in each
  page's front matter.
- The downloaded `iccf-events.json` contains your personal ICCF pages; don't
  commit it.
