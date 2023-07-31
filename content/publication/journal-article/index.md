---
title: Complex In-Hand Manipulation via Compliance-Enabled Finger Gaiting and
  Multi-Modal Planning
publication_types:
  - "2"
authors:
  - Andrew S. Morgan
  - Kaiyu Hang
  - Bowen Wen
  - Kostas Bekris
  - and Aaron M. Dollar
publication_short: RAL
abstract: Constraining contacts to remain fixed on an object during manipulation
  limits the potential workspace size, as motion is subject to the hand's
  kinematic topology. Finger gating is one way to alleviate such restraints. It
  allows contacts to be freely broken and remade so as to operate on different
  manipulation manifolds. This capability, however, has traditionally been
  difficult or impossible to practically realize. A finger gating system must
  simultaneously plan for and control forces on the object while maintaining
  stability during contact switching. This work alleviates the traditional
  requirement by taking advantage of system compliance, allowing the hand to
  more easily switch contacts while maintaining a stable grasp. Our method
  achieves complete SO(3) finger gating control of grasped objects against
  gravity by developing a manipulation planner that operates via orthogonal safe
  modes of a compliant, underactuated hand absent of tactile sensors or joint
  encoders. During manipulation, a low-latency 6D pose object tracker provides
  feedback via vision, allowing the planner to update its plan online so as to
  adaptively recover from trajectory deviations. The efficacy of this method is
  showcased by manipulating both convex and non-convex objects on a real robot.
  Its robustness is evaluated via perturbation rejection and long trajectory
  goals. To the best of the authors' knowledge, this is the first work that has
  autonomously achieved full SO(3) control of objects within-hand via finger
  gating and without a support surface, elucidating a valuable step towards
  realizing true robot in-hand manipulation capabilities.
draft: false
featured: false
tags:
  - Source Themes
slides: null
url_pdf: http://arxiv.org/pdf/1512.04133v1
image:
  caption: "Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)"
  focal_point: ""
  preview_only: false
summary: This work presents a method for achieving complete SO(3) finger gating
  control of grasped objects against gravity, using a manipulation planner that
  operates via orthogonal safe modes of a compliant, underactuated hand absent
  of tactile sensors or joint encoders. The method takes advantage of system
  compliance to allow the hand to more easily switch contacts while maintaining
  a stable grasp, and uses a low-latency 6D pose object tracker for online
  feedback and adaptive recovery from trajectory deviations. The method is
  demonstrated on a real robot manipulating both convex and non-convex objects,
  and represents a valuable step towards realizing true robot in-hand
  manipulation capabilities.
url_dataset: ""
url_project: ""
url_source: ""
url_video: ""
author_notes: []
doi: ""
publication: IEEE Robotics and Automation Letters, 2022
projects: []
date: 2022-03-04T01:00:00.000Z
url_slides: ""
publishDate: 2017-01-01T00:00:00.000Z
url_poster: ""
url_code: ""
---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

Supplementary notes can be added here, including [code and math](https://wowchemy.com/docs/content/writing-markdown-latex/).
