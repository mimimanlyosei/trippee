# 🎯 Trippee – MVP Tasks

This document outlines the features that make up the **Minimum Viable Product (MVP)** for Trippee. These are the essential tasks required to get a working version of the app that allows route optimisation across IKEA, LEGO, and Ivy locations.

---

## ✅ MVP Objective

Enable users to:
- Find all IKEA, LEGO, and Ivy locations across the UK and Ireland.
- Calculate the shortest or most efficient travel route between them.
- View an estimated travel time for the full route.

---

## 🧱 MVP Core Features

### 📍 1. Data Collection & Parsing
- [ ] Gather and store location data for:
  - [ ] IKEA stores
  - [ ] LEGO stores
  - [ ] Ivy restaurants
- [ ] Clean and structure the data into a standard format (e.g. CSV or JSON)

### 🗺️ 2. Route Optimisation Logic
- [ ] Use a routing algorithm (e.g., greedy TSP or Google Maps API as fallback)
- [ ] Calculate an efficient route through all points
- [ ] Support city-level filtering for faster testing

### 🕒 3. Travel Time Estimation
- [ ] Add estimated travel durations between points
- [ ] Provide a total travel time for the entire route

### 📊 4. Basic Visual Output
- [ ] Print final route in terminal as ordered list
- [ ] Optional: plot route using `matplotlib` or static map image

### 🧪 5. Testing and Validation
- [ ] Write simple unit tests to validate location data parsing
- [ ] Spot-check a few known routes for accuracy

---

## 🚧 Notes
- Aim for working logic before working visuals
- Keep code modular so later features (filters, user input, web app) can plug in easily
- Use GitHub Issues to track each bullet point above

