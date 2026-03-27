# Product Mindset for UI Design

Frameworks for thinking like a product designer — aligning visual decisions with user outcomes and business goals. Read this file when scoping requirements, deciding what to prioritize, or asking the right interview questions.

## Table of Contents
1. [Product vs. UI Design Mindset](#1-product-vs-ui-design-mindset)
2. [User Research Fundamentals](#2-user-research-fundamentals)
3. [Metrics & Outcomes](#3-metrics--outcomes)
4. [Prioritization Frameworks](#4-prioritization-frameworks)
5. [MVP Thinking](#5-mvp-thinking)
6. [Product-Led Growth & UI](#6-product-led-growth--ui)
7. [Ask the Right Questions](#7-ask-the-right-questions)

---

## 1. Product vs. UI Design Mindset

| UI Design | Product Design |
|---|---|
| "How does this look?" | "Why does this exist?" |
| Delivers pixels | Delivers outcomes |
| Aesthetic-first | User outcome-first |
| Considers the artifact | Considers the system |

Every visual decision should trace back to a user outcome or business metric. The best UI replication asks: _What is this interface trying to achieve, and does my implementation serve that goal?_

---

## 2. User Research Fundamentals

### Jobs-to-be-Done (JTBD)
Users don't hire products for features — they hire them for progress.
- **Functional job**: "I need to track expenses"
- **Emotional job**: "I want to feel in control of my money"
- **Social job**: "I want to appear financially responsible"

Surface emotional and social jobs via visual hierarchy, copywriting tone, and color psychology.

### The 5 Whys
Ask "why" five times to reach the root problem instead of the surface request.
```
"I want a bigger font" → "I can't read text easily" → "Contrast is too low"
Root cause: #999 on #FFF background — fix contrast, not font size.
```

### Empathy Mapping
| Says | Thinks |
|---|---|
| Explicit feedback | Underlying beliefs |
| **Does** | **Feels** |
| Observable behavior | Emotional state |

Tension between _Says_ vs. _Does_ reveals design opportunities.

---

## 3. Metrics & Outcomes

### North Star Metric
Single metric capturing core product value. UI decisions should optimise for it.
Examples: Spotify — time spent listening; Airbnb — nights booked; Slack — messages sent.

### HEART Framework (Google UX)
| Metric | What to measure |
|---|---|
| Happiness | CSAT, NPS |
| Engagement | Actions per session |
| Adoption | New user activation |
| Retention | Return rate, churn |
| Task Success | Completion rate, error rate |

### Pirate Metrics (AARRR)
Acquisition → Activation → Retention → Revenue → Referral.
**UI most directly impacts Activation** — the first impression and Aha Moment determine whether users ever come back.

### Conversion Funnel UI Priorities
| Stage | Key UI decision |
|---|---|
| Awareness | Hero clarity, value prop above fold |
| Interest | Feature highlights, social proof |
| Desire | Pricing clarity, testimonials |
| Action | CTA prominence, friction reduction |
| Retention | Dashboard usability, notification UX |

---

## 4. Prioritization Frameworks

### MoSCoW
- **Must have**: Without this, the product doesn't work
- **Should have**: Important but not critical for launch
- **Could have**: Nice-to-have if time permits
- **Won't have**: Explicitly deferred

### Effort/Impact Matrix
```
              Low Effort    High Effort
High Impact  [ QUICK WINS ] [ MAJOR PROJECTS ]
Low Impact   [ FILL-INS   ] [ THANKLESS TASKS]
```
Start with quick wins for maximum early visual impact.

### Kano Model (Feature Tiers)
- **Basic needs**: Expected, invisible when met (e.g., page loads)
- **Performance needs**: More = better (speed, clarity)  
- **Delighters**: Unexpected extras (micro-animations, personality)

Ensure basics → optimize performance → sprinkle delighters.

---

## 5. MVP Thinking

### MVP ≠ Bad Product
Build the thinnest slice that demonstrates real value — each iteration should be a working solution.
- ❌ Strip everything until barely functional
- ✅ Ship with 80% feature completeness + 100% core-experience polish

### Feature Completeness vs. Polish
Users forgive missing features. They don't forgive a broken or ugly core experience.
**The core user journey must be polished even at MVP stage.**

### The Aha Moment
The moment users first experience core value. The entire onboarding UI should get users there as fast as possible.
- Slack: "Reply in under 5 minutes to a team message"
- Dropbox: "Store and access a file from two devices"

---

## 6. Product-Led Growth & UI

### Self-Serve Onboarding Best Practices
1. Don't require credit card upfront
2. Show value before asking for effort
3. Empty states should show what's possible (use sample data)
4. Progressive onboarding > upfront tutorial dump
5. Provide "undo" freely — reduce fear of experimentation

### Design as Business Value
Good design directly drives:
- **Conversion rate**: Better CTA placement, clearer value prop
- **Retention**: Reduced confusion, faster time-to-value
- **Support cost reduction**: Self-explanatory UI = fewer tickets
- **Brand equity**: Premium aesthetics command premium pricing

### Design Debt
Ad-hoc spacing, inconsistent components, and undocumented variations compound.
**Remedy**: CSS custom properties (design tokens) + a small shared component set, even for prototypes.

---

## 7. Ask the Right Questions

Use these during the skill's interview phase to surface product context:

### About the User
- Who is the primary user and what do they already know?
- What are they trying to accomplish?
- What's their emotional state when using this? (Stressed? Curious? Transactional?)
- What device do they primarily use?

### About the Context
- Is this a one-time action or a recurring workflow?
- What happens right before and after using this?
- Solo tool or collaborative?

### About the Business
- What is the primary action users should take on this screen?
- What metric defines success?
- Is there a free/premium distinction to communicate?

### About the Design
- Brand guidelines or existing components to follow?
- "Wow first impression" vs. "efficiency after repeated use"?
- What is the one thing the design must get right?

### Red Flag Checks (surface dealbreakers early)
- Accessibility requirements? (WCAG AA/AAA?)
- Performance constraints? (Offline, limited bandwidth?)
- Localization? (RTL languages, long translated strings?)
