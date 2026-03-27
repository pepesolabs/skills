# Color Theory & Typography

A deep reference for color systems and typeface selection. Read this file when defining a design's color palette, choosing fonts, or building a type scale.

## Table of Contents
1. [Color Theory Foundations](#1-color-theory-foundations)
2. [Color Systems in UI](#2-color-systems-in-ui)
3. [Curated Palettes by Aesthetic](#3-curated-palettes-by-aesthetic)
4. [Typography Foundations](#4-typography-foundations)
5. [Font Pairings by Aesthetic](#5-font-pairings-by-aesthetic)
6. [Type Scale & Fluid Typography](#6-type-scale--fluid-typography)
7. [CSS Implementation Patterns](#7-css-implementation-patterns)

---

## 1. Color Theory Foundations

### Color Relationships
| Scheme | Definition | Effect |
|---|---|---|
| Monochromatic | One hue, multiple lightness/saturation | Cohesive, calm, sophisticated |
| Analogous | Adjacent hues on wheel (30-60° apart) | Harmonious, natural, peaceful |
| Complementary | Opposite hues (180°) | High contrast, energetic, bold |
| Split-complementary | One hue + two adjacent to its complement | Contrast without tension |
| Triadic | Three hues equidistant (120°) | Vibrant, balanced |
| Tetradic/Square | Four hues at 90° | Rich, complex — hard to manage |

**Safe default**: Monochromatic palette + one complementary accent.

### Color Properties
- **Hue**: The color family (red, blue, green)
- **Saturation**: Intensity/purity (grey → vivid)
- **Lightness**: Bright ↔ dark on the spectrum
- **Chroma** (in OKLCH): Perceived colorfulness (more perceptually uniform than HSL saturation)

### Perceptual Uniformity: OKLCH vs HSL
HSL's "lightness" is not perceptually uniform — two colors at `hsl(X, 100%, 50%)` have wildly different perceived brightness (yellow appears much lighter than blue at the same L value).

**Use `oklch()` for accessible, perceptually consistent palettes**:
```css
--color-primary: oklch(55% 0.2 240);  /* L=55%, C=0.2, H=240° (blue) */
```

### 60-30-10 Rule
Classic interior design principle that applies directly to UI:
- **60%**: Dominant color (usually background) — sets the mood
- **30%**: Secondary color (surfaces, cards, panels)
- **10%**: Accent color (CTAs, links, highlights)

---

## 2. Color Systems in UI

### Semantic Color Tokens
Define colors by intent, not value. This enables theming and consistency:
```css
:root {
  /* Brand */
  --color-primary: #3B4FDD;
  --color-primary-hover: #2D3FAC;

  /* Neutrals */
  --color-bg: #FAFAFA;
  --color-surface: #FFFFFF;
  --color-border: #E5E7EB;
  --color-text: #111827;
  --color-text-muted: #6B7280;

  /* Semantic */
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  --color-info: #3B82F6;
}
```

### Dark Mode Token Strategy
Do NOT simply invert light mode. Redesign for dark:
```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0F0F11;          /* Near black, not pure black */
    --color-surface: #1A1A1F;     /* Slightly lighter than bg */
    --color-border: rgba(255,255,255,0.08);
    --color-text: #F0F0F2;
    --color-text-muted: #8A8A9A;
  }
}
```

### Surface Elevation (Dark Mode)
Simulate depth with surface lightness rather than shadows:
| Elevation | Background |
|---|---|
| Base | `#0F0F11` |
| Surface 1 (cards) | `#1A1A1F` |
| Surface 2 (modals) | `#242429` |
| Surface 3 (tooltips) | `#2E2E35` |

### Opacity Scale for Overlays
```css
--overlay-hover:   rgba(0, 0, 0, 0.04);
--overlay-focus:   rgba(0, 0, 0, 0.08);
--overlay-active:  rgba(0, 0, 0, 0.12);
--overlay-muted:   rgba(0, 0, 0, 0.38);
--overlay-modal:   rgba(0, 0, 0, 0.60);
```

---

## 3. Curated Palettes by Aesthetic

### Neobrutalism
```css
--bg: #FFFBF0; --text: #1A1A1A;
--primary: #FFE14D; --secondary: #FF6B6B;
--accent: #4DFFB4; --border: #1A1A1A;
--shadow: 4px 4px 0 #1A1A1A;
```

### Glassmorphism / Dark Tech
```css
--bg: #0A0A1A; --text: #E8E8F5;
--glass-bg: rgba(255,255,255,0.06);
--glass-border: rgba(255,255,255,0.12);
--accent: #7C6FFF; --glow: rgba(124,111,255,0.4);
```

### Luxury Editorial
```css
--bg: #FAFAF8; --text: #1C1C1C;
--gold: #C9A84C; --muted: #9A9A8E;
--surface: #F2F0EC; --border: #E5E3DE;
```

### Earthy / Biophilic
```css
--bg: #F7F3ED; --text: #2D2416;
--primary: #4A7C59; --secondary: #C16F41;
--accent: #E8C547; --muted: #9E8A74;
--surface: #EDE8DF;
```

### Cyberpunk / Neon Dark
```css
--bg: #050510; --text: #E0E0FF;
--primary: #00D4FF; --secondary: #FF2079;
--accent: #39FF14; 
--glow-blue: 0 0 20px rgba(0,212,255,0.6);
--glow-pink: 0 0 20px rgba(255,32,121,0.6);
```

### Minimal Swiss / Corporate
```css
--bg: #FFFFFF; --text: #000000;
--primary: #0066CC; --muted: #666666;
--border: #DDDDDD; --surface: #F5F5F5;
```

### 70s Vintage
```css
--bg: #F5ECD7; --text: #2C1810;
--primary: #C1440E; --secondary: #5C6B3A;
--accent: #E8A849; --surface: #EDE0C8;
```

---

## 4. Typography Foundations

### Type Classification
| Category | Characteristics | Personality |
|---|---|---|
| Humanist Sans | Calligraphic origins, organic | Friendly, approachable (Inter, Gill Sans) |
| Geometric Sans | Perfect circles/lines | Modern, clean (Futura, Circular, DM Sans) |
| Grotesque Sans | Industrial-era origins | Neutral, robust (Helvetica, Aktiv Grotesk) |
| Old Style Serif | Diagonal stress, bracketed serifs | Classic, trust, readability (Garamond) |
| Modern Serif | Vertical stress, high contrast strokes | Elegant, luxury (Didot, Bodoni) |
| Slab Serif | Heavy, un-bracketed serifs | Bold, confident (Rockwell, Clarendon) |
| Display / Decorative | Expressive, intended for headlines only | Range from playful to extreme |
| Monospace | Fixed-width glyphs | Technical, code, terminal |
| Script / Handwriting | Cursive, flowing or casual | Personal, artisan, informal |

### Type Scale Ratios
| Ratio Name | Value | Character |
|---|---|---|
| Minor Second | 1.067 | Very subtle |
| Major Second | 1.125 | Subtle |
| Minor Third | 1.200 | Gentle |
| Major Third | 1.250 | Common, balanced |
| Perfect Fourth | 1.333 | Classic web scale ← recommended |
| Augmented Fourth | 1.414 | Dramatic |
| Perfect Fifth | 1.500 | Very dramatic |
| Golden Ratio | 1.618 | Maximum drama |

**Recommended starting scale (Perfect Fourth, base 16px)**:
```
xs:  12px  (0.75rem)
sm:  14px  (0.875rem)
md:  16px  (1rem)     ← base
lg:  21px  (1.333rem)
xl:  28px  (1.777rem)
2xl: 37px  (2.369rem)
3xl: 50px  (3.157rem)
4xl: 67px  (4.209rem)
```

---

## 5. Font Pairings by Aesthetic

### Neobrutalism
- **Heading**: Space Grotesk 700 / Syne 800 / Bricolage Grotesque 800
- **Body**: DM Sans 400 / Space Grotesk 400
- **Accent**: Courier Prime (monospace element)

### Glassmorphism / Dark Tech
- **Heading**: Outfit 700 / Plus Jakarta Sans 700
- **Body**: Inter 400 / Outfit 400
- **Code**: JetBrains Mono

### Luxury Editorial
- **Heading**: Cormorant Garamond 300 italic / Playfair Display 400 / Libre Bodoni
- **Body**: Jost 300 / EB Garamond 400 
- **Accent**: Letter-spaced uppercase sans (Jost 600 uppercase)

### 70s / Vintage Organic
- **Heading**: Recoleta / Canela / Freight Display
- **Body**: Libre Baskerville / Source Serif 4
- **Accent**: Script (Dancing Script, Sacramento)

### Swiss / International Style
- **Heading**: Neue Haas Grotesk / Aktiv Grotesk (or free: Be Vietnam Pro)
- **Body**: Same family, lighter weight
- **Rule**: One typeface, multiple weights only

### Terminal / Developer
- **All**: JetBrains Mono / Fira Code / Berkeley Mono (paid)
- **Accent**: Mix proportional for labels (Inter) with monospace for values

### Playful / Kawaii
- **Heading**: Nunito 800 / Fredoka One / Quicksand 700
- **Body**: Nunito 400 / Poppins 400

### Editorial / Magazine
- **Heading**: Fraunces / Newsreader (optical size variable) 
- **Body**: Source Serif 4 / Libre Baskerville
- **Subheading**: Barlow Condensed 600 uppercase

---

## 6. Type Scale & Fluid Typography

### Fluid Type (CSS clamp)
Scale font automatically between two viewport sizes:
```css
/* Syntax: clamp(minimum, preferred, maximum) */
/* Preferred: calc(intercept + slope * 100vw) */

h1 { font-size: clamp(2rem, 5vw + 1rem, 4.5rem); }
h2 { font-size: clamp(1.5rem, 3.5vw + 0.5rem, 3rem); }
p  { font-size: clamp(1rem, 1.5vw + 0.5rem, 1.25rem); }
```

### Line Height Guidelines
| Context | Line Height |
|---|---|
| Display / Headlines | 1.0–1.2 (tight) |
| Subheadings | 1.2–1.4 |
| Body text | 1.5–1.7 (optimal reading) |
| Small/caption text | 1.3–1.5 |
| Code blocks | 1.6–1.8 |

### Letter Spacing Guidelines
| Context | Tracking |
|---|---|
| Display headlines | -0.02em to -0.04em (tight) |
| Body text | 0 (default) |
| Small uppercase labels | 0.08em to 0.15em (wide) |
| Button text | 0.02em to 0.05em |

---

## 7. CSS Implementation Patterns

### Full Design Token System
```css
:root {
  /* Typography */
  --font-display: 'Playfair Display', Georgia, serif;
  --font-body: 'Jost', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Type Scale */
  --text-xs:   0.75rem;
  --text-sm:   0.875rem;
  --text-base: 1rem;
  --text-lg:   1.125rem;
  --text-xl:   1.25rem;
  --text-2xl:  1.5rem;
  --text-3xl:  1.875rem;
  --text-4xl:  2.25rem;
  --text-5xl:  3rem;
  --text-6xl:  3.75rem;

  /* Spacing (8pt grid) */
  --space-1:  0.25rem;   /*  4px */
  --space-2:  0.5rem;    /*  8px */
  --space-3:  0.75rem;   /* 12px */
  --space-4:  1rem;      /* 16px */
  --space-6:  1.5rem;    /* 24px */
  --space-8:  2rem;      /* 32px */
  --space-12: 3rem;      /* 48px */
  --space-16: 4rem;      /* 64px */
  --space-24: 6rem;      /* 96px */

  /* Border Radius */
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   16px;
  --radius-xl:   24px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm:  0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.06);
  --shadow-md:  0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06);
  --shadow-lg:  0 10px 15px rgba(0,0,0,0.08), 0 4px 6px rgba(0,0,0,0.05);
  --shadow-xl:  0 20px 25px rgba(0,0,0,0.1), 0 10px 10px rgba(0,0,0,0.04);
}
```

### Google Fonts Import Template
```html
<!-- Single family with multiple weights -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">

<!-- Two families paired -->
<link href="https://fonts.googleapis.com/css2?
  family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&
  family=Jost:wght@300;400;600&
  display=swap" rel="stylesheet">
```
