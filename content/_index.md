---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        <span style="font-family: 'Century Gothic';">RobotPI Group</span>
      image:
        filename: both.jpg
      text: |
        <br>
        
        **RobotPi** has been a center of excellence for robotics manpulation research, teaching, and practice since its founding in 2021
  
  - block: collection
    content:
      title: |
        <span style="font-family: 'Century Gothic';">Latest News</span>
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: int.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
  
  
---