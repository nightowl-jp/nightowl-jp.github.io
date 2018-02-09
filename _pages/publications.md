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

## International Conferences and Workshops (refereed)
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv_simple.html %}
  {% endfor %}</ul>

## Domestic Conferences
  <ul>{% for post in site.publications_nr reversed %}
    {% include archive-single-cv_simple.html %}
  {% endfor %}</ul>

