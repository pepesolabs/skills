---
name: ui-style-replicator
description: Build frontend interfaces by analyzing reference UI images and interviewing the user about requirements. Use when the user provides a reference image or design mock and wants to replicate or adapt its style.
---

# UI Style Replicator

## Overview
This skill guides the process of replicating or adapting a UI design from a reference image provided by the user. It transforms a visual reference into a production-ready frontend implementation through a systematic process of analysis, user interview, and strategic coding.

**Use this skill when:**
- The user provides a screenshot, mock, or design image and asks to "build this".
- The user wants to mimic a specific style (e.g., "neobrutalism", "glassmorphism") seen in a reference.

## Workflow

Follow this four-phase process strictly:

### Phase 1: Visual Analysis (Deep Dive)
Before writing any code or asking questions, perform a comprehensive visual audit of the provided reference image(s). If no image is active or visible, ask the user to upload it.

**Analyze & Output the following details:**
1.  **Aesthetic Style**: Identify the core design language (e.g., Neobrutalism, Swiss Design, Glassmorphism, Material, Apple-esque).
2.  **Color Palette**: Extract primary, secondary, and accent colors. efficient use of whitespace/darkspace.
3.  **Typography**: Analyze font categories (Grotesque Sans, Serif, Monospace), weights, and hierarchy.
4.  **Layout & Grid**: Identify the structural patterns (bento grid, card-based, split-screen, sidebar navigation).
5.  **Visual Elements**: Note distinct UI details (border-radius, shadows, border thickness, texture, gradients).
6.  **Micro-Interactions (Inferred)**: Hypothesize likely hover states or animations based on the style.

### Phase 2: Strategic Interview
Do **NOT** start building immediately. You must align on the user's specific interpretation and requirements. Use the analysis from Phase 1 to inform these questions.

**Ask these 4-5 focused questions:**
1.  **Target Audience & Vibe**: "Who is this for? Should we lean more playful/casual or serious/professional than the reference?"
2.  **Deviation Check**: "Are there specific elements in the reference you *dislike* or want to change?"
3.  **Responsiveness**: "Is this primarily for mobile, desktop, or responsive web?"
4.  **Tech Stack Preference**: "Confirming: React + Tailwind? Or HTML/CSS? Any specific libraries (e.g., Framer Motion, shadcn/ui)?"
5.  **Functionality**: "Is this a static mockup or do you need specific functional interactivity (mock data, state)?"

*Wait for User Response.*

### Phase 3: Synthesis & Proposal
Once the user responds, synthesize their answers with your initial analysis.

1.  **Restate the Plan**: "I will build a [Component/Page] using [Tech Stack]. We will target a [Style Name] aesthetic, featuring [Key characteristic 1] and [Key characteristic 2]."
2.  **Confirm Assets/Libraries**: List any specific tools you will use (e.g., "I'll use `lucide-react` for icons and a custom `font-family` configuration in Tailwind.").

### Phase 4: Implementation
Proceed to build the frontend.

**Design Guidelines:**
-   **Pixel Perfection vs. Spirit**: Aim to capture the *spirit* and *polish* of the reference. If the reference is blurry, make professional design decisions to "clean it up".
-   **Variables & Tokens**: Start by defining CSS variables or Tailwind config for the analyzed color palette.
-   **Components**: Break the UI into logical components.
-   **Polish**: Add the inferred micro-interactions (hover states, transitions).
-   **Content**: Use realistic mock data that matches the context (no Lorem Ipsum if possible - use context-relevant text).

**Reference Check**:
-   Does the border radius match?
-   Is the whitespace generous enough? (Most AI implementations are too dense).
-   Are the shadows accurate?

### Final Output
Present the code in clear, copy-pasteable blocks (e.g., `index.tsx`, `globals.css`, `tailwind.config.js`).
