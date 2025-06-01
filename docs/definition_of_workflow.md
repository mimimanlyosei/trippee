# 🧭 Definition of Workflow – Trippee

This document outlines how work is tracked and progressed through the Trippee project using GitHub Issues and a Kanban-style board.

## 📋 Project Board Setup
We use the GitHub Projects Kanban board template, with the following columns:

- **Backlog**: A holding area for ideas and tasks. Tickets stay here until they have a full breakdown.
- **Ready**: Once a ticket has a clear markdown breakdown, it is moved here.
- **To Do**: Tickets are moved here once they have been prioritised for active development.
- **In Progress**: Active work is underway.
- **Testing**: Tickets that require verification, testing, or bug checks.
- **In Review**: Work that needs a second look or feedback before completion.
- **Done**: Completed, tested, and verified tickets.

---

## 📌 Issue Lifecycle

1. **Create the Issue**  
   - Add a meaningful title.
   - Include a short description and any relevant context.

2. **Break It Down**  
   - Add a checklist in markdown to clearly define subtasks.
   - Once breakdown is added, move the issue to **Ready**.

3. **Prioritise**  
   - Prioritised Ready issues are moved to **To Do**.

4. **Development Cycle**  
   - Move issue to **In Progress** when work begins.
   - When finished, move to **Testing** or **In Review** depending on what’s needed.
   - Once tested/reviewed, move to **Done**.

---

## 🏷️ Labels

Issues are tagged with labels to provide context and aid filtering:

- **Core labels**: `MVP`, `feature`, `bug`, `validation`, `testing`, `documentation`, `planning`, `infrastructure`
- **Framework sprint labels**: `framework-sprint`, `flask`, `django`, `framework-rebuild`, `learning`, `api`, `phase-2`

These labels help group issues by purpose, phase, and technical focus. They also identify items driven by Mimi’s personal learning plan (e.g., Flask/Django tasks).

---

## 🔁 Commits

Each commit should:
- Be descriptive (what, why)
- Reference the related issue using `#issue_number`  
  Example:
  ```bash
  git commit -m "Add route visualisation script #8"
  ```

---

## 📁 Where Work Lives

- `/scripts`: Python scripts and logic
- `/data`: Raw and cleaned datasets
- `/notebooks`: Jupyter notebooks for EDA or quick tests
- `/docs`: Planning, workflow, and roadmap documentation
- `/trippee-flask/`: Flask framework implementation (optional UI/API for MVP)
- `/trippee-django/`: Django experiments and feature rebuilds (used for Phase 2 learning)

---
