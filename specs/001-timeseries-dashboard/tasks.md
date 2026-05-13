---

description: "Task list for TimeSeries Insight Dashboard implementation"
---

# Tasks: TimeSeries Insight Dashboard

**Input**: Design documents from `specs/001-timeseries-dashboard/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions
- Size: S (Small), M (Medium), L (Large)

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Project initialization and basic structure

- [ ] T001 [P] Create backend directory structure in backend/src/
- [ ] T002 [P] Create static directory with empty index.html
- [ ] T003 [P] Create .env file with CSV_PATH configuration
- [ ] T004 Create requirements.txt with dependencies (fastapi, pandas, numpy, scipy, uvicorn, python-dotenv, pytest, pytest-cov)
- [ ] T005 [P] Create initial main.py with FastAPI app and static file serving

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 [P] Create CSV generator service in backend/src/services/csv_generator.py (S) - generates 1 year hourly random-walk data
- [ ] T007 [P] Create CSV loader service in backend/src/services/csv_loader.py (M) - reads CSV, validates timestamp, handles missing values
- [ ] T008 [P] Create statistics module in backend/src/statistics/__init__.py (L) - pure functions: mean, median, std, min, max, count, skewness, kurtosis, linear regression, rolling average, anomaly detection (z-score > 2)
- [ ] T009 [P] Create .env configuration loader in backend/src/config.py (S)
- [ ] T010 [P] Create git integration service in backend/src/services/git_integration.py (M) - subprocess for git add/commit

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - View Time Series Data (Priority: P1) 🎯 MVP

**Goal**: Display CSV data on a line chart with column selection dropdown

**Independent Test**: Can load CSV (or auto-generated sample), view chart, select columns

### Tests for User Story 1

> **NOTE: Statistics module tests - target 70% coverage**

- [ ] T011 [P] [US1] Unit tests for statistics module in tests/statistics/test_stats.py (L)

### Implementation for User Story 1

- [ ] T012 [P] [US1] Create GET /columns endpoint in backend/src/routes/data.py (S)
- [ ] T013 [P] [US1] Create GET /data endpoint in backend/src/routes/data.py (M)
- [ ] T014 [US1] Integrate CSV loader with main.py (S) - T012 depends on T006, T007
- [ ] T015 [P] [US1] Download Chart.js and save to static/chart.min.js (S)
- [ ] T016 [US1] Implement column dropdown in index.html (M)
- [ ] T017 [US1] Implement basic line chart in index.html with Chart.js (M) - depends on T015

**Checkpoint**: User Story 1 should be fully functional - CSV loads, chart displays, column selection works

---

## Phase 4: User Story 2 - Filter Data by Date Range (Priority: P1)

**Goal**: Filter displayed data by start/end date

**Independent Test**: Can select date range and see filtered data in chart

### Implementation for User Story 2

- [ ] T018 [P] [US2] Add date range query params to GET /data endpoint (M) - depends on T013
- [ ] T019 [US2] Implement date range picker UI in index.html (M) - T019 depends on T016
- [ ] T020 [US2] Connect date picker to fetch new data on change (S) - T020 depends on T019

**Checkpoint**: User Stories 1 AND 2 work together - data displays with date filtering

---

## Phase 5: User Story 3 - Analyze Data with Statistics (Priority: P1)

**Goal**: Display statistical metrics in sidebar

**Independent Test**: Statistics sidebar shows all 14 metrics

### Implementation for User Story 3

- [ ] T021 [P] [US3] Create GET /stats endpoint in backend/src/routes/stats.py (L) - returns mean, median, std, min, max, count, skewness, kurtosis, regression slope, R², anomaly count
- [ ] T022 [US3] Implement stats sidebar UI in index.html (M) - T022 depends on T016
- [ ] T023 [US3] Connect stats endpoint to sidebar display (S) - T023 depends on T021, T022

**Checkpoint**: User Stories 1, 2, AND 3 work together - chart, filter, and stats all functional

---

## Phase 6: User Story 4 - Toggle Moving Averages (Priority: P2)

**Goal**: Toggle 7-period and 30-period moving averages on chart

**Independent Test**: Moving average lines appear/disappear on chart

### Implementation for User Story 4

- [ ] T024 [P] [US4] Add rolling average calculation to backend (S) - add to statistics module
- [ ] T025 [US4] Add moving average toggle checkboxes in index.html (S) - T025 depends on T016
- [ ] T026 [US4] Add moving average data to GET /data response (S) - T026 depends on T013
- [ ] T027 [US4] Render moving average lines on Chart.js chart (M) - T027 depends on T017

**Checkpoint**: User Story 4 adds moving average visualization

---

## Phase 7: User Story 5 - Visualize Anomalies and Trends (Priority: P2)

**Goal**: Show anomaly points in red, display regression trend line

**Independent Test**: Anomalies highlighted in red, trend line visible

### Implementation for User Story 5

- [ ] T028 [P] [US5] Add anomaly detection to backend (S) - z-score > 2
- [ ] T029 [US5] Add anomaly data points to GET /data response (S) - T029 depends on T013
- [ ] T030 [US5] Add regression trend line data to GET /data response (S) - T030 depends on T013
- [ ] T031 [US5] Render anomaly points as red markers in Chart.js (M) - T031 depends on T017
- [ ] T032 [US5] Render regression trend line in Chart.js (S) - T032 depends on T017

**Checkpoint**: User Story 5 adds anomaly and trend visualization

---

## Phase 8: User Story 6 - Save and Download Snapshots (Priority: P3)

**Goal**: Save current view as CSV, auto-git-commit, show history with download

**Independent Test**: Can save snapshot, view history, download past snapshots

### Implementation for User Story 6

- [ ] T033 [P] [US6] Create POST /snapshot endpoint in backend/src/routes/snapshot.py (L)
- [ ] T034 [P] [US6] Create GET /snapshots endpoint in backend/src/routes/snapshot.py (M)
- [ ] T035 [US6] Integrate git subprocess in POST /snapshot (M) - T035 depends on T010, T033
- [ ] T036 [US6] Add snapshot button UI in index.html (S)
- [ ] T037 [US6] Add snapshot history panel UI in index.html (M)
- [ ] T038 [US6] Connect snapshot button to POST endpoint (S) - T038 depends on T036, T033
- [ ] T039 [US6] Connect history panel to GET /snapshots endpoint (S) - T039 depends on T037, T034
- [ ] T040 [US6] Add download functionality for snapshots in index.html (S)

**Checkpoint**: All user stories complete - full dashboard functional

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T041 [P] Run pytest with coverage and verify 70% on statistics module (S)
- [ ] T042 [P] Add chart zoom/pan functionality with Chart.js (M)
- [ ] T043 [P] Add hover tooltips to chart (S)
- [ ] T044 Verify all acceptance scenarios from spec.md pass (M)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 6 (P6)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit tests for statistics module in tests/statistics/test_stats.py"

# Launch all implementation tasks for User Story 1 together:
Task: "Create GET /columns endpoint in backend/src/routes/data.py"
Task: "Create GET /data endpoint in backend/src/routes/data.py"
Task: "Download Chart.js and save to static/chart.min.js"
Task: "Implement column dropdown in index.html"
Task: "Implement basic line chart in index.html with Chart.js"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Add User Story 6 → Test independently → Deploy/Demo
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group (per Constitution: atomic commits)
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence