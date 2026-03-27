---
name: ui-style-replicator
description: Replicate, adapt, or design-from-scratch frontend UIs with deep aesthetic intelligence. Use when the user provides a reference image, screenshot, or design mock and wants to build it — or when they describe a design style (e.g. "neobrutalism", "glassmorphism", "luxury editorial") and want a UI built in that aesthetic. Also use when the user asks to make an existing UI look like a specific design or improve its visual quality significantly.
---

# UI Style Replicator

Transforms visual references and style descriptions into production-ready frontend implementations. Follows a four-phase workflow: deep visual analysis → strategic user interview → synthesis → implementation.

## Bundled References

Load these files **only when they are relevant** to the current task:

| File | When to load |
|---|---|
| `references/design-themes.md` | Identifying or selecting an aesthetic (Neobrutalism, Glassmorphism, etc.) |
| `references/design-patterns.md` | Choosing layout, navigation, components, or animation patterns |
| `references/design-thinking.md` | Making strategic design decisions, evaluating quality, or applying design principles |
| `references/product-mindset.md` | Scoping requirements, aligning design with user outcomes, running the interview phase |
| `references/color-typography.md` | Selecting a color palette, building a type scale, or choosing font pairings |

**Load `design-themes.md` and `color-typography.md` for almost every task.** The others are situational.

## Scripts

- **`scripts/extract_palette.py`**: Extract dominant colors from a reference image.
  Usage: `python3 scripts/extract_palette.py <image_path> [--colors N] [--format css|json|table]`
  Run this when the user provides an image and color extraction would save analysis time.
  Requires: `pip install Pillow colorthief` (colorthief optional, Pillow alone works).

---

## Workflow: Four Phases

### Phase 1: Visual Analysis

Before writing any code or asking questions, perform a comprehensive visual audit of the reference image. If no image is provided and they describe a style, skip to Phase 2.

**Optionally run `extract_palette.py`** on the reference image to get precise hex values.

**Analyze and output:**
1. **Aesthetic Style** — Name the design language. Use `references/design-themes.md` to identify it precisely (e.g., "late-stage Neobrutalism with Memphis accents").
2. **Color Palette** — Extract primary, secondary, accent, and neutral colors. Note whitespace vs. darkspace usage.
3. **Typography** — Font categories (grotesque sans, serif, mono), weights used, and typographic hierarchy.
4. **Layout & Grid** — Structural patterns (bento, split-screen, sidebar, masonry). See `references/design-patterns.md`.
5. **Visual Details** — Border-radius values, shadow style, border weight, gradients, textures, depth.
6. **Inferred Micro-Interactions** — Hypothesize hover states, transitions, and animations based on the aesthetic.

### Phase 2: Strategic Interview

**Do NOT start building yet.** Align on requirements. Keep questions to 4–5. Use `references/product-mindset.md` to ask product-aware questions.

**Core questions to adapt:**
1. **Purpose & Audience** — "Who is this for? What's the primary action users should take?"
2. **Deviation Check** — "Anything in the reference you dislike or want changed?"
3. **Vibe/Tone** — "Should this lean more [X] or [Y]? More playful or professional than the reference?"
4. **Tech Stack** — "Confirming: React + Tailwind? Or vanilla HTML/CSS? Any specific libraries?"
5. **Scope** — "Static mockup or functional with interactive state/data?"

*Wait for user response before building.*

### Phase 3: Synthesis & Proposal

Synthesize Phase 1 analysis + Phase 2 answers into a clear implementation plan:
1. **Restate the plan**: "I will build a [Component/Page] using [Tech Stack], targeting a [Style Name] aesthetic with [key design choices]."
2. **Confirm tokens**: List the color variables, fonts, and key CSS patterns you'll use.
3. **Flag any trade-offs**: e.g., "The reference uses a commercial font — I'll substitute [X] which captures the same feel."

### Phase 4: Implementation

**Design guidelines:**

- **Color tokens first**: Define all CSS custom properties (`--color-*`, `--font-*`, `--radius-*`, `--shadow-*`) before any component code. Reference `references/color-typography.md`.
- **Capture spirit, not pixels**: If the reference is blurry or low-res, make confident professional judgments to "complete" the design.
- **Components over monoliths**: Break the UI into logical, named components.
- **Realistic content**: Use context-appropriate mock data — no Lorem Ipsum.
- **Polish the details**: Hover states, focus states, transitions. The small things separate great from mediocre.
- **Accessibility baseline**: Sufficient color contrast, visible focus indicators, semantic HTML. See `references/design-thinking.md` § 7.

**Reference Quality Checklist (before finalizing):**
- [ ] Does the border radius match the reference's personality (sharp, rounded, pill)?
- [ ] Is the whitespace generous enough? (Most AI implementations are too dense)
- [ ] Do the shadows match — soft/diffuse vs. hard/offset?
- [ ] Is the typography hierarchy clear at a glance?
- [ ] Do interactive elements have visible hover/active states?
- [ ] Is the color palette cohesive — 60/30/10 rule applied?

**Final output format**: Provide clear, copy-pasteable code blocks labeled by file (`index.html`, `styles.css`, `App.tsx`, `globals.css`, etc.).
