---
layout: page
title: Puzzles
permalink: /puzzles/
image: '/images/puzzle.jpg'
tags: [weekly-puzzles, game-of-the-week]
description: "Puzzle of the Month: one position from my own correspondence games on the 1st of every month, each with exactly one move that works."
---
<div style="text-align: left; font-size: smaller;">
Photo by <a href="https://unsplash.com/@edge2edgemedia?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Edge2Edge Media</a> on <a href="https://unsplash.com/photos/black-puzzle-piece-on-white-paper-x21KgBfOd_4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
</div>

{%- comment -%}
  All puzzles live in _puzzles. The monthly ones have layout: puzzle (see
  _tools/puzzles); the weekly puzzles of 2023–2024 don't. A puzzle dated in the
  future is left out of the site until its date (_plugins/future_puzzles.rb).
{%- endcomment -%}
{% assign puzzles = site.puzzles | sort: "date" | reverse %}
{% assign monthly = puzzles | where: "layout", "puzzle" %}

## Puzzle of the Month

Every month a position from one of my own finished correspondence games, with the story behind it. Each has exactly one move that works. Some I found, some my opponents found against me.

{% if monthly.size > 0 -%}
<ol class="puzzle-list">
{%- for p in monthly %}
  <li><a href="{{ p.url | relative_url }}"><span class="puzzle-list__month">{{ p.date | date: "%B %Y" }}</span><span class="puzzle-list__title">{{ p.title }}</span><span class="puzzle-list__task">{{ p.puzzle.task }}</span></a></li>
{%- endfor %}
</ol>
{%- else -%}
The first one appears on 1 December 2026.
{%- endif %}

## Weekly puzzles, 2023–2024

The weekly series that came before, with positions and games from my own play and from the masters.

<ul>
{%- for p in puzzles %}{% if p.layout == "puzzle" %}{% continue %}{% endif %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a> ({{ p.date | date: "%-d %B %Y" }}){% if p.description %}: {{ p.description | escape }}{% endif %}</li>
{%- endfor %}
</ul>
