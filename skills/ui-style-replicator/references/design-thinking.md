# Design Thinking

Frameworks, principles, and mental models for making design decisions. Read this file when making strategic design choices, understanding user needs, or evaluating design quality.

## Table of Contents
1. [Core Design Thinking Frameworks](#1-core-design-thinking-frameworks)
2. [Design Principles](#2-design-principles)
3. [Visual Hierarchy & Attention](#3-visual-hierarchy--attention)
4. [Gestalt Principles](#4-gestalt-principles)
5. [Cognitive Load & Usability](#5-cognitive-load--usability)
6. [Emotional Design](#6-emotional-design)
7. [Accessibility as Design Quality](#7-accessibility-as-design-quality)
8. [Decision Frameworks for UI](#8-decision-frameworks-for-ui)

---

## 1. Core Design Thinking Frameworks

### Double Diamond (Design Council)
Four phases — Discover, Define, Develop, Deliver:
1. **Discover** (diverge): Research, observe, gather user insights without judgment
2. **Define** (converge): Synthesize into problem statement (Point of View, HMW questions)
3. **Develop** (diverge): Ideate, prototype, explore many solutions
4. **Deliver** (converge): Test, refine, ship

**Application**: When replicating a UI, you're in the Deliver phase — but ask Define-phase questions to ensure the implementation solves the right problem.

### Jobs To Be Done (JTBD)
Users don't hire products for features — they hire them to make progress in a situation.
- **Functional job**: "I need to track my expenses"
- **Emotional job**: "I want to feel in control of my money"
- **Social job**: "I want to appear financially responsible to my partner"

**Application**: When choosing what to emphasize in the UI — surface the emotional and social job via visual hierarchy, tone of copy, and color psychology.

### Design Sprint (Google Ventures)
5-day structured process: Map → Sketch → Decide → Prototype → Test
- **Key insight**: Build just enough to learn. A realistic-looking prototype ≠ production code.

### Human-Centered Design (IDEO/d.school)
Three lenses for viable solutions:
1. **Desirability**: Do people want this? (User research)
2. **Feasibility**: Can we build it? (Technical)
3. **Viability**: Should we build it? (Business)

**Sweet spot**: Innovative design lives at the intersection of all three.

---

## 2. Design Principles

### Dieter Rams' 10 Principles of Good Design
1. Innovative
2. Makes a product useful
3. Is aesthetic
4. Makes a product understandable
5. Unobtrusive
6. Honest
7. Long-lasting
8. Thorough down to the last detail
9. Environmentally friendly
10. **As little design as possible** ← most quoted

**UI application**: Remove elements until functionality breaks. Then add one back.

### Don Norman's Principles (The Design of Everyday Things)
- **Affordance**: Make it obvious what can be done (buttons look clickable, links look tappable)
- **Signifier**: Use visual cues to signal where actions happen
- **Feedback**: Every action must produce a response (state change, animation, confirmation)
- **Mapping**: Controls should relate spatially/logically to their effect
- **Constraints**: Prevent errors by limiting wrong options
- **Conceptual Model**: The UI should match users' mental model of the system

### Jakob's Law
Users spend most time on OTHER sites. They expect your site to work like sites they already know.
**Implication**: Innovate on value, not on convention. Use standard patterns unless you have a compelling reason not to.

### Hick's Law
Decision time increases logarithmically with the number of choices.
**Application**: Limit navigation items, reduce form fields, progressive disclosure over information dumps.

### Fitts' Law
Time to click a target is a function of distance and target size.
**Application**: Primary CTAs should be large and close to the user's starting position (e.g., bottom of mobile screens).

---

## 3. Visual Hierarchy & Attention

### F-Pattern (Reading Pattern)
Eye-tracking studies show users scan in an F-shape on text-heavy pages:
- First horizontal scan across the top
- Second shorter horizontal scan
- Vertical scan down the left side

**Design response**: Put key information in F-pattern hotspots. Don't rely on right-side content for critical info on text pages.

### Z-Pattern (Scanning Pattern)
On sparse, image-forward pages (landing pages), eyes flow in a Z:
- Top-left → Top-right → Diagonal to bottom-left → Bottom-right

**Design response**: Logo top-left, nav top-right, feature image diagonal midpoint, CTA bottom-right.

### Hierarchy Through Scale
Establish clear size ratios — don't use more than 4-5 distinct sizes:
```
Display (72-96px): Page hero, one per screen
H1 (48-64px): Section headline
H2 (32-40px): Subsection
Body (16-18px): Reading text
Caption (12-14px): Metadata, labels
```

### Visual Weight
Elements "weigh" more when they are: larger, darker, more saturated, isolated, textured, or at the top of the page. Use weight to direct attention.

### The 3-Second Test
A new user should understand: (1) what the product does, (2) who it's for, and (3) what to do next — within 3 seconds of landing.

---

## 4. Gestalt Principles

### Proximity
Elements close together appear related. Use spacing to communicate group membership.
**Application**: Card padding should pull elements inside together; gap between cards separates them.

### Similarity
Elements that look alike (color, shape, size) appear to belong together.
**Application**: All interactive elements should share a common visual language (e.g., all links are the same blue).

### Continuity
The eye follows smooth paths, even across gaps.
**Application**: Aligned elements feel connected. Misalignment implies separation.

### Closure
The mind completes incomplete shapes.
**Application**: Partial images (cropped) + progress bars + skeleton loaders all use closure.

### Figure-Ground
We perceive objects either as "figure" (focus) or "ground" (background).
**Application**: Dialogs create new figure; backdrop creates ground. Don't clutter ground.

### Common Fate
Elements that move together appear related.
**Application**: Animate related items together (same easing, same delay offset).

---

## 5. Cognitive Load & Usability

### Three Types of Cognitive Load
1. **Intrinsic**: Complexity inherent to the task (can't be reduced, only managed)
2. **Extraneous**: Load added by bad design (must be eliminated)
3. **Germane**: Load that builds useful understanding (optimize for)

**Design goal**: Minimize extraneous, maximize germane, make intrinsic bearable.

### Progressive Disclosure
Show only what's needed for the next decision. Reveal complexity on demand.
**Pattern hierarchy**: Overview → Detail → Edit → Advanced

### Error Prevention > Error Recovery
Design to prevent mistakes first:
- Confirm destructive actions (delete dialog)
- Inline validation before form submission
- Disable unavailable options (don't hide them — grey them with tooltip why)
- Default to safe options

### Recognition Over Recall
Users should recognize what to do, not remember it.
**Application**: Visible navigation (not hidden), icon + label (not icon alone for unfamiliar actions), placeholder text as format hint.

### Miller's Law
Working memory holds approximately 7±2 items.
**Application**: Don't put more than 7 items in a nav, a list without grouping, or a form section.

---

## 6. Emotional Design

### Three Levels (Don Norman)
1. **Visceral**: First impression — aesthetics, sensory appeal ("I want this")
2. **Behavioral**: Using it — does it work? Is it effortless?
3. **Reflective**: After use — does it align with my identity? Do I tell others about it?

**Application**: Most AI-generated UI fails at visceral level. The style replicator skill specifically targets visceral excellence.

### Delight vs. Satisfaction
- **Satisfaction**: The product does what I expected
- **Delight**: The product exceeded expectation in a meaningful moment

Delight comes from: surprising micro-animations, witty empty states, unexpected visual richness, and moments of warmth in an otherwise functional interface.

### Color Psychology Quick Reference
| Color | Psychological Association | Common Use |
|---|---|---|
| Blue | Trust, calm, reliability | Finance, health, enterprise |
| Green | Growth, success, nature | Finance (positive), health, sustainability |
| Red | Urgency, energy, danger | Error states, CTAs for impulse purchases |
| Orange | Warmth, enthusiasm, creativity | Community, casual brands |
| Purple | Luxury, creativity, mystery | Beauty, premium, creative tools |
| Yellow | Optimism, attention, caution | Warnings, highlight, friendly brands |
| Black | Power, elegance, sophistication | Luxury, premium, tech |
| White | Clarity, simplicity, cleanliness | Healthcare, tech, minimalist brands |

---

## 7. Accessibility as Design Quality

Accessibility is not a compliance checklist — it's quality design.

### WCAG Contrast Requirements
- Body text: **4.5:1** contrast ratio against background
- Large text (18px+ or 14px+ bold): **3:1**
- Interactive elements (borders, icons): **3:1**
- **Tool**: Use `oklch` or check via browser DevTools Accessibility panel

### Focus States
Every interactive element must have a visible focus indicator.
```css
:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
```

### Semantic HTML Hierarchy
- One `<h1>` per page
- `<h2>` for major sections, `<h3>` for subsections
- `<button>` for actions, `<a>` for navigation
- `<nav>`, `<main>`, `<aside>`, `<footer>` as landmarks

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 8. Decision Frameworks for UI

### The CRAP Principles (Robin Williams)
- **Contrast**: Make different things look VERY different
- **Repetition**: Repeat visual elements to create unity
- **Alignment**: Every element aligned to something
- **Proximity**: Group related items, separate unrelated items

### The Aesthetic-Usability Effect
Attractive interfaces are perceived as more usable. Users are more tolerant of issues in beautiful products.
**Implication**: Investing in visual polish directly improves perceived quality.

### Goodhart's Law Applied to Design
When a design metric becomes a target, it ceases to be a good metric.
**Example**: Optimizing for "time on site" can make a confusing site look successful. Always trace metrics back to user outcomes.

### The MAYA Principle (Raymond Loewy)
"Most Advanced Yet Acceptable" — the ideal design is the most advanced the audience can accept.
**Application**: Push aesthetics as far as the target audience can embrace. Too conservative = boring. Too radical = rejected.

### Card Sorting Mental Model
Before designing information architecture, ask: "How would users categorize these items?" The resulting structure should mirror user mental models, not internal org structure.
