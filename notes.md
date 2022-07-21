---
title: "PHD 101: A Computer Science PhD Handbook"
linktitle: "PHD 101"
summary: "A collection of guides for navigating a PhD in Computer Science."
date: 2022-06-29T00:00:00-07:00
lastmod: 2022-06-29T00:00:00-07:00
type: book    # Do not modify.
weight: 1     # Page position in course.

draft: false  # Is this a draft? true/false
toc: true     # Show table of contents? true/false

tags: []
categories: ["teaching"]
---

<div class="media stream-item">
  <div class="media-body">
    <h5 class="article-title mb-0 mt-0">
      <a href="/course/phd101/">PHD 101: A Computer Science PhD Handbook</a>
    </h5>
    <div class="article-style">
      A collection of guides for navigating a PhD in Computer Science.
    </div>
  </div>
</div>

## Random Thoughts

Is everything in academia amenable to a process/workflow structure? Should I design the course around those things?
- In some senses, yes, everything from digital communication to writing papers to program committees to travelling are processes. But there are ideals/virtues/goals/principles that stand above these things.
- At the highest level of each workflow, the intro should state (1) what you'll get by following the workflow, and (2) any preliminaries/account setup/etc. you need first.


## Planning the Course

### Audiences

- "Specialists" are senior graduate students, postdocs, and established faculty&mdash;especially those from within mathematics and computer science.
- "Nonspecialists" include prospective/junior graduate students, especially those from outside mathematics and computer science, and individuals who are curious about PhDs but have no current intention of pursuing one. This category technically includes everyone else as well, though their likelihood of reading this material is low.
- "Primary readers", in this case, overlap heavily with the defined parts of the above two categories. The emphasis on "secondary readers" for this project is about how relevant information will be later in time and to those who just stumble across it.

It's worth identifying what is specific to computer science theory vs. computer science generally vs. STEM vs. any PhD. Be conservative but hopeful in what's being recommended here.

### Purpose

What must be different after this material is read?

- Individuals considering pursuing a PhD (in computer science) will understand what a PhD is/isn't, enhancing their discernment.
- Junior PhD students will have a set of tools, references, and examples to jumpstart their research and writing workflows.
- PhD students will be able to navigate opaque academic processes and their various roles.

### Fractal Structures

- (optional) Context: why the need is pressing/important
- Need: why something needs to be done at all
- Task: what was undertaken to address the need
- Object: what the present document does/covers
- Findings: what the work done yielded or revealed
- Conclusion: what the findings mean for the audience
- (optional) Perspectives: what the future holds, beyond this work


## Content

Each workflow/process we discuss has three components:
1. We always start with the *problem/task* the workflow performs.
2. Then we identify *principles* of good solutions.
3. We conclude with possible software *solutions* for the problem/task that adhere to our desired principles.

### Writing a Research Paper

The opening introduction should explain what's here. In particular, what are the deliverables/outcomes? A formatted and polished manuscript, intended for either a journal or conference, and an arXiv version.

#### Having Ideas

Writing is the process of communicating thoughts and ideas, not having the thoughts and ideas in the first place (through writing can catalyze structure and further thinking). Before research or writing begins, we first need an interesting research idea to write about.

This is one of the hardest skills in academia, and ability to form interesting ideas is often used as a marker of when a PhD student is ready to graduate. So how do we have ideas?
- Read the literature, both for breadth (high-profile, interesting papers&mdash;like in a reading group/seminar) and depth (have one or two areas closely related to your "expertise" that you're keeping up with).
- Related to the above: popular science books can be good ways of getting the gist of other fields without having to go deep. As a CS person, I've found this particularly useful for biology and physics. Books often lay out more interesting and sweeping theories than papers, too, since they're not necessarily making truth claims and have the space to work with (e.g., Gelenter).
- Talk to people (collaborators, conference attendees, authors of papers you like). Ask them about challenges/big problems in their (sub)field.
- Have life experiences outside academia/your area of study (especially important for interdisciplinary connections). Travel. Volunteer. Join a club. Get involved in politics/advocacy. Do things. For people thinking about but not yet committed to PhD, what about doing a summer in Alaska or backpacking in a new country (privileged, but valuable)? International students coming to the US are ahead, already gaining the experience of self-reliance and adaptability to new cultures and experiences.

It's important to understand that since a PhD is an apprenticeship and a process, your ideas don't *have* to be about the thing you care about most in the world (related to pressures to "make a difference"), especially at the start. This is a noble goal, but as a PhD student you're *learning* how to have ideas in tandem with mastering content about the ideas you're having/being given. There's always room to pivot later&mdash;a strong ability to ideate is what's important.

#### Managing Literature

Problem: literature search/reading/notetaking/creating bibliographies.

Principles: discovery, searchability/recall, organization, persistence, consistency. As always, leave syntactic formatting to a computer.

Software Solution(s): Google Scholar (and to a lesser extent, ResearchGate, arXiv, etc.) + Zotero (possibly with bibliographic help from DBLP, Google Scholar, and publisher sites) + BibTeX.

This step in writing/research ensures a few things:
- You'll have an easier time writing related work.
- You establish credibility and connection to relevant fields.
- You don't replicate what's already been done (a good way to get rejected is to have a weak novelty claim) or position yourself to get scooped.
- You'll get inspired by interesting methods/data visualizations/etc. as well as get turned off by bad/annoying ways of presenting information.

#### Clarifying Purpose

At this point, you've (a) had an idea and (b) read, taken notes on, and organized related literature.

Now identify purpose (see Jean-luc, Effective written documents > Planning the document); specifically, we can write the foreword ("the before") for the eventual paper:
- (optional) Context: why the need is pressing/important
- Need: why something needs to be done at all
- Task: what was undertaken to address the need
- Object: what the present document does/covers

These can and should be informed by what you read in the literature. There needs to be a real "gap" between what exists (the literature) and what we hope for.

We will return to the summary ("the after") once we've performed our research.

It may at this point be useful to clarify the types of publications (research article, brief announcement, review/survey, perspective, etc.?)

#### Conducting Research

This should be a separate section, based on whether it's modeling, simulation, proofs, etc., but the point is that this is where the work is done. Any experiments, results, etc. should be in support of the purpose.

#### Communicating Findings

Now that you have results, complete the purpose statement with a summary ("the after", see Jean-luc, Effective written documents > Planning the document).
- Findings: what the work done yielded or revealed
- Conclusion: what the findings mean for the audience
- (optional) Perspectives: what the future holds, beyond this work

Verify that your findings satisfactorily address the need from your foreword.

#### Identifying a Venue

This matters at this point in the process because (a) it determines the audience, (b) it may determine a deadline, and (c) it may affect length limitations.

TODO: If it doesn't fit well anywhere else, this may be a good place to talk about tiers of conferences/journals, how to figure that out, academic "communities", and example conferences and journals are for my lab areas specifically.

Explain the need to track venue pairs for deadlines, as there are a lot of them. Can discuss schema, but maybe not systems (I'm not terribly happy with the Trello or Airtable solutions I have so far).

#### Drafting the Manuscript

Read Jean-luc's chapter on drafting written documents.

This is where we need to talk about Overleaf vs. git vs. etc. for managing manuscripts.

Deep Dive: LaTeX/BibTeX lessons and best practices.

Draft the manuscript in a basic 'article' document class. In the first draft, focus on *clarity* and *accuracy*. Then revise a second draft focused on *conciseness*. If it's been some time between the initial literature search and this point in time, check the literature again and integrate anything important before moving on to revisions.

#### Revising the Manuscript

Read Jean-luc's chapter on revising written documents.

TODO: Decide on a good workflow for revisions.

TODO: Anything from Jean-luc worth saying here?

#### Formatting the Manuscript

We use LaTeX to easily format and structure manuscripts.

Discuss the main formats (article, ACM, Springer, IEEE, LIPIcs, etc.), where they're appropriate, and what to use for arXiv.
- Discuss any idiosyncracies with corresponding LaTeX templates (always read the manual!).

The arXiv version has looser length requirements, but should still tell a concise and compelling story. "Formatting" for our purposes may also involve cutting the paper down to size if length limitations apply.

#### Submitting the Manuscript

Discuss submission to digital repositories (arXiv, SocArXiv, biorXiv), conferences (EasyChair, HotCRP), and journals (usually Editorial Manager).

Don't stress or worry or even think hard about your manuscript until decisions. Take a break. Work on other things.

Give a brief overview of what's happening in review for conferences and journals, but leave the details to the reviewing workflow (link to it). Estimate the time for reviews (conferences will tell you a decisions date, journals won't). Talk about reasonable times to reach out to the editor for signs of life.

####


### Publicizing Your Research

TODO: Websites, Twitter, institutional news articles, research profiles (Google Scholar, ResearchGate), etc.


### Communicating Digitally

Task: effective electronic communication.

Principles: efficiency, clarity, availability, organization, persistence.

Software Solution(s):
- Email: Focus is on features as opposed to a single client/provider: tags vs. folders, signatures, clear communication (see Jean-luc), archive/delete. Discuss pros/cons of using institutional email. Can mention the "just use email" project, though I'm in some disagreement there.
- Pairwise messaging: Signal > Whatsapp > iMessage and other platform-specific issues.
- Group messaging: Zulip > Discord ~ Slack > Teams.
- Video conferencing: Zoom is defacto, Teams is okay. Various privacy-focused/open-source alternatives exist.


### Time & Project Management

**NOTE**: while somewhat disjoint, this and project management seem related to communicating digitally in that they're all loosely coupled, relating to the communication/connectivity parts of research and courses.

Task:

Principles:

Software Solution(s):
- Calendar: Again focus on features instead of apps: tags/categorization, invitation etiquette, good naming, time zone checking, bonus for availability.
- Project Tracking: Kanban boards, e.g., Trello/Airtable/MS Planner/open source alternative.


### Preparing a CV

Task: collecting items, writing, and formatting a CV.

Principles: completeness, readability, easy maintenance.

Software Solution(s): LaTeX + CV theme + BibTeX. Certain customizations around auto-generated BibTeX lists of publications, presentations, and poster lists using multibib and nocite. Link to Zotero for "My Publications".
