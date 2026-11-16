# Puzzles dated in the future stay out of the site until their date.
#
# Jekyll does this by itself for blog posts. For a collection such as
# _puzzles it only skips writing the page: the puzzle would still be listed in
# site.puzzles, so the Puzzles page, search and the sitemap would link to a page
# that isn't there yet. This leaves such puzzles out altogether, unless the build
# runs with --future (Deploy Previews do, see netlify.toml).
Jekyll::Hooks.register :site, :post_read do |site|
  next if site.future

  puzzles = site.collections["puzzles"]
  next unless puzzles

  puzzles.docs.reject! { |doc| doc.date > site.time }
end
