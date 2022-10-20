---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

## Thesis
  <ul>{% for post in site.publications_thesis reversed %}
    {% include archive-single-cv_simple.html %}
  {% endfor %}</ul>

## Journals (refereed)
  <ul>{% for post in site.publications_jn reversed %}
    {% include archive-single-cv_simple.html %}
  {% endfor %}</ul>

## International Conferences and Workshops (refereed)
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv_simple.html %}
  {% endfor %}</ul>

## Non-refereed papers
  <ul>{% for post in site.publications_nr reversed %}
    {% include archive-single-cv_simple.html %}
  {% endfor %}</ul>

## Talks and Presentations
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
