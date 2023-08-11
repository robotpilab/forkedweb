---
title: Manipulation for self-Identification, and self-Identification for better
  manipulation
publication_types:
  - "2"
authors:
  - Kaiyu Hang
  - Walter G. Bircher
  - Andrew S. Morgan
  - Aaron M. Dollar
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
summary: The process of modeling a series of hand-object parameters is crucial
  for precise and controllable robotic in-hand manipulation because it enables
  the mapping from the hand’s actuation input to the object’s motion to be
  ob-tained. Without assuming that most of these model parameters are known a
  priori or can be easily estimated by sensors, we focus on equipping robots
  with the ability to actively self-identify necessary model parameters using
  minimal sensing. Here, we derive algorithms, on the basis of the concept of
  virtual linkage-based representations (VLRs), to self-identify the underlying
  mechanics of hand-object systems via exploratory manipulation actions and
  probabilistic reasoning and, in turn, show that the self-identified VLR can
  enable the control of precise in-hand ma-nipulation. To validate our
  framework, we instantiated the proposed system on a Yale Model O hand without
  joint
  encoders  or  tactile  sensors.  The  passive  adaptability  of  the  underactuated  hand  greatly  facilitates  the  self-identification  process,
  because they naturally secure stable hand-object interactions during random
  exploration. Relying solely on an in-hand camera, our system can effectively
  self-identify the VLRs, even when some fingers are replaced with novel
  designs. In addition, we show in-hand manipulation applications of
  handwriting, marble maze playing, and cup stacking to demonstrate the
  effectiveness of the VLR in precise in-hand manipulation control.
url_dataset: ""
url_project: ""
url_source: ""
url_video: ""
author_notes: []
doi: ""
publication: IEEE Robotics and Automation Letters, 2022
projects: []
date: 2023-08-11T18:51:24.401Z
url_slides: ""
publishDate: 2017-01-01T00:00:00.000Z
url_poster: ""
url_code: ""
---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

Supplementary notes can be added here, including [code and math](https://wowchemy.com/docs/content/writing-markdown-latex/).
