# UI/UX Design Patterns

Reference for structural and interaction patterns. Read this file when analyzing layout structure, component composition, or planning an implementation architecture.

## Table of Contents
1. [Layout Patterns](#1-layout-patterns)
2. [Navigation Patterns](#2-navigation-patterns)
3. [Content Patterns](#3-content-patterns)
4. [Interaction Patterns](#4-interaction-patterns)
5. [Form Patterns](#5-form-patterns)
6. [Animation Patterns](#6-animation-patterns)
7. [Data Display Patterns](#7-data-display-patterns)
8. [Responsive Patterns](#8-responsive-patterns)

---

## 1. Layout Patterns

### Bento Grid
- **When**: Dashboard/marketing pages with varied content blocks
- **Structure**: CSS Grid with `grid-template-areas`, cells of different sizes
- **Signature**: Mixed-size cards with consistent gap, rounded corners, subtle bg differentiation
- **Modern use**: Apple product pages, Linear, Vercel dashboards

```css
.bento {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto;
  gap: 1rem;
}
.bento .featured { grid-column: span 2; }
```

### Split-Screen / Hero Split
- **When**: Landing pages, login pages, feature showcases
- **Structure**: Two equal (50/50) or weighted (60/40) columns; one content, one visual
- **Tip**: The visual column often contains animation or video loop

### Sidebar + Main
- **When**: App dashboards, admin panels, documentation
- **Variants**: Fixed sidebar (app-like), collapsible sidebar (responsive), icon-only collapsed
- **Pattern**: `display: flex` with nav `width: 240-280px`, main `flex: 1`

### Masonry / Pinterest Layout
- **When**: Media-heavy grids (images, cards of varying heights)
- **Implementation**: CSS `columns` property or CSS Grid with `grid-row: span N`
- **Gotcha**: Pure CSS masonry doesn't maintain source order well; use JS for strict order

### Full-Bleed Hero
- **When**: Marketing pages, cinematic entrances
- **Pattern**: `width: 100vw; min-height: 100vh` or `100dvh`; background fills viewport
- **Content**: Centered via `display: grid; place-items: center`

### Sticky Scroll Narrative
- **When**: Storytelling pages, scroll-based reveals, product explanations
- **Pattern**: Wrapper `height: N * 100vh`; inner content `position: sticky; top: 0`
- **Use with**: IntersectionObserver or scroll-driven animations

### Card Grid
- **When**: Listings, catalogs, feature showcases
- **Variants**: Fixed column grid, auto-fill responsive grid, masonry
- **Standard responsive**: `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`

---

## 2. Navigation Patterns

### Top Navigation Bar
- **Content**: Logo + nav links + actions (search, CTA, avatar)
- **Sticky variant**: `position: sticky; top: 0; backdrop-filter: blur(8px); z-index: 100`
- **Transparent-to-solid**: Animate on scroll, transitioning background and shadow

### Tab Navigation
- **When**: Segmented views of related content (not separate pages)
- **Accessibility**: Use `role="tablist"`, `role="tab"`, `aria-selected`
- **Variants**: Underline tabs, pill tabs (filled), icon + label tabs

### Drawer / Off-Canvas Menu
- **When**: Mobile navigation, secondary panels
- **Pattern**: `transform: translateX(-100%)` → `translateX(0)` on open
- **Best practice**: Use `inert` attribute on background content when open

### Breadcrumb
- **When**: Deep navigation hierarchies, file systems, e-commerce categories
- **Pattern**: `Home / Category / Subcategory / Current`
- **Styling tip**: Use `>` or `/` separator with subtle color-fade toward current page

### Command Palette (⌘K)
- **When**: Power user apps, developer tools, complex nav
- **Pattern**: Modal with search input + filtered results, keyboard-navigable
- **Libraries**: cmdk, kbar (React)

### Floating Action Button (FAB)
- **When**: Mobile-primary apps, single dominant action
- **Position**: `position: fixed; bottom: 1.5rem; right: 1.5rem`
- **Expand variant**: Click to reveal related sub-actions (speed dial)

---

## 3. Content Patterns

### Feature Grid / Bento Feature
- **Structure**: Grid of cards, each highlighting one feature
- **Anatomy**: Icon + headline + 1-2 line description
- **Design tip**: Vary card sizes for hierarchy; use subtle bg, icon color as accent

### Testimonial / Social Proof
- **Variants**: Single quote prominently, carousel of quotes, grid of small cards
- **Elements**: Avatar, name, role/company, star rating (optional), quote text
- **Design tip**: Avatars + names feel more human than logos alone

### Pricing Table
- **Structure**: 2-4 columns; toggle monthly/annual; highlight recommended plan
- **Pattern**: Middle card `scale(1.05)`, contrasting background, "Popular" badge

### FAQ Accordion
- **Pattern**: `<details>/<summary>` HTML or CSS-only `max-height` transition
- **Best practice**: Smooth height animation: `transition: max-height 0.3s ease`

### Timeline
- **When**: History, changelog, process steps
- **CSS**: Vertical line (`::before` pseudo-element on parent) + dot at each step
- **Horizontal variant**: Stepper for multi-step forms/onboarding

### Progress / Stats
- **Variants**: Circular progress (SVG stroke-dasharray), horizontal bar, stacked bar
- **Animated reveal**: Animate progress value on IntersectionObserver trigger

### Hero CTA
- **Elements**: Eyebrow text (optional uppercase label) + H1 + subtext + primary CTA + secondary CTA (or "no credit card" social proof)
- **Text sizing**: H1 typically `3rem`–`6rem` on desktop; fluid: `clamp(2rem, 6vw, 5rem)`

---

## 4. Interaction Patterns

### Hover State Hierarchy
- **Level 1 (subtle)**: Background color shift, `opacity: 0.8`, slight `translateY(-2px)`
- **Level 2 (moderate)**: Shadow appears/grows, border color change, icon reveals
- **Level 3 (expressive)**: Scale transform, full color swap, slide-in text

### Tooltip
- **Pattern**: Show on hover/focus, `position: absolute` relative to trigger
- **Accessibility**: `role="tooltip"`, linked via `aria-describedby`
- **Avoid**: Tooltips on primary actions or on mobile (hover doesn't exist)

### Modal / Dialog
- **Pattern**: `<dialog>` element (native) or ARIA role="dialog" with focus trap
- **Open animation**: Fade + scale from 95% to 100%; backdrop fade-in
- **Close**: Escape key, backdrop click, explicit close button

### Toast / Snackbar
- **Position**: Bottom-center (mobile), top-right (desktop)
- **Duration**: 3-5 seconds; pause on hover
- **Variants**: Success (green), Error (red), Info (blue), Warning (amber)
- **Library**: Sonner (React), hot-toast

### Infinite Scroll vs. Pagination
- **Infinite scroll**: Good for social feeds, media galleries (content without destination)
- **Pagination**: Good for search results, tables, sequential content with page permalinks
- **Hybrid**: "Load More" button balances both

### Drag & Drop
- **Native**: HTML5 Drag and Drop API (complex, limited styling)
- **Library**: dnd-kit (React), SortableJS
- **Visual feedback**: Ghost/clone of dragged item, drop zone highlight, animation on drop

---

## 5. Form Patterns

### Floating Label
- **Pattern**: Label sits inside field; flies to top on focus or when value exists
- **CSS technique**: `placeholder-shown` selector or JS class-toggle
- **Accessibility note**: Always paired with real `<label>` (not just placeholder)

### Inline Validation
- **Pattern**: Validate on blur; show error immediately below field
- **UX rule**: Never validate while typing (too aggressive); validate on blur or submit

### Multi-Step Form / Wizard
- **Pattern**: Progress indicator at top, one section visible at time
- **State**: Keep all data in memory; only submit on final step
- **Navigation**: Forward + backward arrows; allow clicking completed steps

### Search with Autocomplete
- **Pattern**: Input triggers debounced API call; results in dropdown
- **Keyboard**: Arrow keys navigate list; Enter selects; Escape closes
- **ARIA**: `role="combobox"` on input, `role="listbox"` on dropdown

---

## 6. Animation Patterns

### Page Load / Entrance Sequence
- **Strategy**: Stagger reveals with `animation-delay` increments (50-100ms per element)
- **Common sequence**: Nav → Hero text → Hero image → Below-fold content
```css
.hero-title { animation: fadeUp 0.6s ease both; }
.hero-sub   { animation: fadeUp 0.6s ease 0.1s both; }
.hero-cta   { animation: fadeUp 0.6s ease 0.2s both; }
```

### Scroll-Triggered Reveal
- **Implementation**: IntersectionObserver adds `.visible` class
- **CSS**: `opacity: 0; transform: translateY(20px)` → transitions to visible state
- **Scroll-driven animation API**: New CSS `animation-timeline: scroll()` for native approach

### Micro-interaction on Action
- **Button click**: Brief `scale(0.97)` then back; or ripple effect
- **Toggle switch**: `transform: translateX` on thumb
- **Checkbox**: SVG checkmark draw animation (`stroke-dashoffset` transition)

### Loading States
- **Skeleton screens**: Preferred over spinners for content-heavy pages
- **Pulse animation**: `@keyframes pulse { 0%, 100% { opacity: 1 } 50% { opacity: 0.4 } }`
- **Spinner**: Reserve for quick operations (<2s); provide progress for long operations

### Number/Value Counter
- **Pattern**: Animate from 0 to target value on scroll-reveal
- **Implementation**: `requestAnimationFrame` loop incrementing displayed value

---

## 7. Data Display Patterns

### Data Table
- **Structure**: `<table>` with `<thead>`, sortable columns, row hover states
- **Features**: Sorting (click header), filtering (search above), pagination below
- **Responsive**: Horizontal scroll on mobile; prioritize columns; collapse to cards

### Chart Selection Guide
| Data type | Best chart |
|---|---|
| Part-to-whole | Pie / Donut (≤5 segments) |
| Trend over time | Line chart |
| Comparison between items | Bar / Column chart |
| Distribution | Histogram / Box plot |
| Correlation | Scatter plot |
| Hierarchy | Treemap / Sunburst |
| Geographic | Choropleth map |

### KPI Card / Stat Block
- **Elements**: Label + large number + trend indicator (▲/▼ % change) + sparkline (optional)
- **Color coding**: Green for positive, red for negative, neutral grey for flat
- **Size**: Prominent enough to read at a glance; typically 3-4 per row

### Feed / Activity Stream
- **Pattern**: Reverse chronological list; timestamp, actor, action, object
- **Visual**: Avatar on left, text content on right, faint timestamp
- **Infinite scroll**: Appropriate here

---

## 8. Responsive Patterns

### Mobile-First Breakpoints
```css
/* Mobile first (no media query = mobile) */
/* Small tablet */
@media (min-width: 640px) { }
/* Tablet / large phone landscape */
@media (min-width: 768px) { }
/* Desktop */
@media (min-width: 1024px) { }
/* Large desktop */
@media (min-width: 1280px) { }
```

### Container Query (Component-level responsive)
```css
.card-wrapper { container-type: inline-size; }
@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

### Fluid Typography
```css
/* Scales smoothly between viewport widths */
font-size: clamp(1.25rem, 3vw + 0.5rem, 2.5rem);
```

### Touch Target Sizes
- Minimum: `44×44px` (Apple HIG) / `48×48dp` (Material)
- Comfortable: `48×48px` with at least `8px` gap between targets

### Navigation Transforms
- **Desktop**: Horizontal nav bar
- **Tablet**: Same or collapsed to icon-only
- **Mobile**: Hamburger → Drawer, or Bottom Tab Bar (native app feel)
