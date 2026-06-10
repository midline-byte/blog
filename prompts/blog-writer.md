# Blog Writer Prompt

Write a clear blog post using the image analysis result and selected skill rules.

Include:

- A concise title
- Intro paragraph
- Main body sections
- Practical details
- Natural SEO keywords
- Closing paragraph

Inputs:

- Image analysis JSON
- Skill selection result
- Selected skill markdown
- Category metadata

Rules:

- Follow the selected skill's required sections.
- Do not invent facts that are not in the image analysis or supplied metadata.
- When confidence is low, use careful wording.
- Return markdown.
