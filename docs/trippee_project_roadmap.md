# 🚀 Trippee Project Roadmap

This roadmap outlines the planned phases of development for **Trippee**, from initial MVP through to later feature enhancements and framework integrations.

---

## 🧭 Intro

**Trippee** is a route planning project that optimises travel between IKEA, LEGO, and Ivy locations across the UK and Ireland. It serves as both a portfolio piece and a practical tool to demonstrate backend skills using Python and Flask (and later Django).

---

## ✅ Phase 1 – Minimum Viable Product (MVP)

**Objective:** Build a foundational backend system that reads, processes, and visualises travel data between IKEA, LEGO, and Ivy locations.

### Core Deliverables:
- [ ] Parse and clean location data (CSV or JSON)
- [ ] Implement route logic in pseudocode and Python
- [ ] Generate basic route outputs (terminal or JSON)
- [ ] Visualise route using matplotlib or similar
- [ ] Document MVP features and usage

### Optional Enhancements:
- [ ] Flask-based location viewer (`/trippee-flask/`)
- [ ] Flask REST API (`/api/locations`, `/api/route-plan`)

🏷️ Labels used: `MVP`, `feature`, `data`, `testing`, `flask`, `framework-sprint`

---

## 🚧 Phase 2 – Iteration & Rebuild

**Objective:** Expand and restructure MVP features using Django to improve scalability, reinforce learning, and support richer feature sets.

### Planned Refactors:
- [ ] Set up Django project structure (`/trippee-django/`)
- [ ] Rebuild location viewer using Django templates
- [ ] Define models for locations and user trips
- [ ] Integrate database (SQLite or PostgreSQL)
- [ ] Document Django architecture and migration process

🏷️ Labels used: `framework-rebuild`, `django`, `learning`, `phase-2`

---

## 🔮 Future Enhancements

Features that may be explored after the MVP to deepen learning or broaden project scope.

- [ ] Add user-generated trip planning via forms
- [ ] Use APIs (e.g. Google Maps, OpenRouteService) for live routing
- [ ] Export trip data (PDF, JSON, map image)
- [ ] Build frontend interface (e.g. Streamlit, Flask UI, or React)
- [ ] Deploy to public platform (Heroku, Render, Vercel, Railway)

🏷️ Labels used: `enhancement`, `research`, `infrastructure`, `visualisation`

---

## 🗺️ Timeline & Progress Tracker

This section outlines a flexible development schedule to help pace the project. Actual timelines may vary to accommodate deeper learning or tech pivots.

### 🔹 Milestone Walkthrough

Here’s a high-level view of how Trippee’s MVP will unfold.

- **29 May 2025** – Project Start (Sprint Kick-off)
- **Week 1:** Core setup – repo, folder structure, CSV integration
- **Week 2:** Flask API – build /api/locations with query filters
- **Week 3:** Flask Viewer – form-based location viewer (template + POST logic)
- **Week 4:** Route logic MVP – create trip route output (simple or mock)
- **Week 5:** Polish & deploy to host platform (Render, Heroku, etc.)
- **Week 6+:** Begin Django migration (rebuild viewer feature in Django)

### 🔹 Timeline Table

| Phase               | Focus                             | Estimated Time       | Actual Time         |
|---------------------|------------------------------------|----------------------|----------------------|
| Project Kickoff     | Planning, GitHub setup, labels     | 29 May 2025          | 29 May 2025          |
| Core Setup          | Folder structure, clean datasets   | 30 May – 1 June      |                      |
| Flask Foundations   | Flask app, routing, templates      | Week 1 (Est. 2–8 Jun) |                      |
| Flask Viewer        | Location viewer, city filters      | Week 2               |                      |
| Route Logic         | Trip day routing logic (basic)     | Week 3               |                      |
| Flask Polish & Deploy | Testing, polish, deploy MVP     | Week 4               |                      |
| Django Migration    | Rebuild 1 feature in Django        | Week 5–6+            |                      |

---

## 🧩 Roadmap Notes & Priorities

- MVP will be built in Flask first
- Django will be used post-MVP to rebuild core features
- Timeline is adaptive and learning-driven — not deadline-bound
- All commits should follow `#issue_number` format and reference GitHub issues

---

This roadmap is a living document and will evolve with the project. Each step builds toward deployment while showcasing a growing backend skillset. 💪
