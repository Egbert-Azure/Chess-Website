# Puzzles and annotated games dated in the future stay out of the site until
# their date.
#
# Jekyll does this by itself for blog posts. For a collection such as
# _puzzles or _tournaments it only skips writing the page: the page would
# still be listed in site.puzzles or site.tournaments, so the Puzzles page, the
# Tournaments page, search and the sitemap would link to a page that isn't there
# yet. This leaves such pages out altogether, unless the build runs with
# --future (Deploy Previews do, see netlify.toml).
Jekyll::Hooks.register :site, :post_read do |site|
  next if site.future

  %w[puzzles tournaments].each do |name|
    collection = site.collections[name]
    next unless collection

    collection.docs.reject! { |doc| doc.date > site.time }
  end
end
