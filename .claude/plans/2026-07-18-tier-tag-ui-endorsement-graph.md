# PLAN ARTIFACT — Primaries beta: tier-tag UI + anchor/endorsement graph
# Save verbatim. Execute steps in order. Report at each checkpoint (CP) and on any tripwire.
# Production (docs/index.html, docs/data.js, primaries-scoring.xlsx, README.md) is NEVER modified. All new files are additive.
# Authored by: maestro planning engagement (agentId abff3a97e2abfc9f2), 2026-07-18.

## STRATEGY

Build the redesigned calculator as a parallel app at docs/beta/ (own index.html + own data.js),
served by the existing GitHub Pages setup at https://candidate-calc.github.io/primaries-2026/beta/.
Develop on branch `beta-ui`; push to main only at the deploy step (additive files only).

Key design decisions (made, not options):
1. ENDORSEMENT FORMULA — keep the researched D5/E2 scalars untouched (they encode broader credit incl.
   media/orgs, reliability-weighted, calibrated). Add a separate ADDITIVE bonus term from the attributed
   peer-endorsement graph; the anchor-doubling applies to that term's edges. Rejected alternative:
   recomputing D5/E2 from the graph — it would silently re-rank all 51 candidates two days before the
   vote and cannot absorb non-peer credit already baked into those scalars.
2. EXCEL — primaries-scoring.xlsx is NOT touched. Beta's defaults (tier assignments) are defined in the
   beta build script; the xlsx stays source of truth for the production slider app. If beta is ever
   promoted, updating the xlsx is a separate future task.
3. LOCALSTORAGE — beta uses NEW key 'primaries-params-v2'. MANDATORY: beta shares the browser origin with
   production; reusing 'primaries-params-v1' would corrupt production users' saved slider state.
   No migration from v1 (tier model is not losslessly derivable from slider values): invalid/absent v2
   state → fresh defaults, wrapped in try/catch exactly like the current load().
4. TOUCH — buttons (X / arrows) are the primary interaction, custom Pointer-Events drag is the
   enhancement (pointerdown+setPointerCapture+elementFromPoint; drag starts immediately with mouse,
   after a 150ms press-hold on touch so page scroll still works). No HTML5 DnD, no library.
   Rejected: HTML5 draggable (broken on mobile), sortable libs (no-build constraint).
5. FACEBOOK — no live scraping. research/fb-findings-2026-07.md + dossiers suffice (verified by scouts).
   Known coverage limits to state in the beta method note: 7 candidates' FB pages were login-gated;
   ~740 ad-library results unscanned for #47, ~80 for #03. The graph is "what the saved research shows",
   not exhaustive.

## ENDORSEMENT FORMULA (exact)

Edge record: {from, to, kind, r, quote, src}   from/to ∈ 1..51, from≠to, r = reliability 1-5.
kind base-weights B: endorse=1.0, partner=0.8, list=0.6, event=0.4
  (endorse = explicit recommendation/praise of a named candidate; partner = declared mutual
   partnership/cross-support statement; list = membership in a named recommended list, edge from the
   list's funder/publisher to each member; event = joint appearance/tour/campaign event.)
Mutual items ("↔") become two directed edges. Edges from non-candidates (Golan, Zandberg) are EXCLUDED.
Edge weight: w = B[kind] * (r/5). Dedupe: per (from,to) pair keep only the max-w edge.
Per candidate j: E_j = Σ over kept edges (i→j) of w_ij * (i anchored ? 2 : 1)
Build-time constant: EREF = max_j E_j with no anchors (stored in beta data.js as D.endorseRef).
Bonus: bonus_j = 0.2 * min(E_j / EREF, 2)          // MU=0.2 constant in JS, commented
F' = F + bonus_j   (F per existing calcOne); score = max(0,(F'-1)/4*100).
Effect size: up to +5 points unanchored, up to +10 when a candidate's endorsers are anchored — visible
but never dominant. Anchored candidates themselves: displayed score forced to 100, pinned to top
(anchored group sorted by F' among themselves, then everyone else by F'). Top-8 green highlight = first
8 rows as today. If anchors > 8, show a red warning next to the table title ("שיריינתם יותר מ-8").
Tier→weight mapping: top tier→10, middle→1, bottom→0, applied to wT/wC; everything else in calcOne
(alpha, gamma, lam, beta, advanced sliders) unchanged.

## STEPS

S1. Curate the endorsement graph → research/endorsements.json      [operator-direct, 60 min]
    Using APPENDIX A below as the worklist: open each referenced file location (line numbers are
    pointers — re-find the quote by grep if drifted), confirm attribution, and write one JSON array of
    edge records per the schema above. Include the three named lists in Appendix A2 as kind=list edges
    from the funder/publisher to each member (funder→own list: skip self-edge). The Rozin "נבחרת" list
    is supporter-authored but amplified by her official page — include with r=3. Joint events → kind=event.
    Set r from the dossier's [n/5] tag; if absent use 3.
    Done when: JSON parses; every edge has all 6 fields; all ids in 1..51; no self-edges; ≥40 edges
    pre-dedup; both פורום דב (8 members) and נבחרת (10 members) lists present; each quote ≥5 words
    copied verbatim from source.

S2. Beta build script → research/build_beta_data.py + docs/beta/data.js      [builder, 30 min]
    Brief the builder: copy build_site_data.py logic; output to docs/beta/data.js ONLY; delete/skip the
    README-mutation block (lines 81-93 of the original) and the xlsx copy (line 107); add to the data
    dict: 'endorse': edges loaded from research/endorsements.json (validated: ids 1..51, no self-edges),
    'endorseRef': EREF computed per formula above, 'defaults' extended with
    'tierT': [1,2,2,1,1,1,1,1,1,1] and 'tierC': [1,2,2,1,2]  (index order = D.topics/D.traits;
    2=top,1=middle,0=bottom; matches: topics top = דמוקרטיה ומשפט, דת ומדינה ושוויון בנטל; traits top =
    חריצות וביצוע, אומץ ציבורי, מקצועיות וניסיון). Keep wT/wC in defaults too (harmless; beta derives
    live values from tiers).
    Done when: script runs clean; docs/beta/data.js exists with 51 candidates + endorse edges (count
    matches post-dedup expectation) + endorseRef>0; `git status` shows docs/data.js, README.md,
    primaries-scoring.xlsx all unmodified.

S3a. Beta UI shell + tier-tag widget → docs/beta/index.html      [builder, 2 h]     → CP2
    Start from a copy of docs/index.html. Changes in this step:
    - <script src> paths stay relative to beta/ (copy data.js reference as-is — beta/data.js sits
      beside it; marked.min.js: reference ../marked.min.js; photos already load as photos/NN.jpg —
      change candidate photo base to ../photos/). Add <meta name="robots" content="noindex"> and a
      visible "גרסת בטא — לבדיקה" badge in the header. LS_KEY = 'primaries-params-v2'.
    - Remove sliderRow usage for sl-topics/sl-traits ONLY (advanced <details> sliders stay as-is).
    - Two widgets (topics card, traits card), each = three stacked boxes with titles, top to bottom:
      "החשובים ביותר" / "נכללים" / "לא חשובים" (add tiny .note hints: "משקל מלא" / "נלקח בחשבון" /
      "לא נספר" — words, never numbers, on the hint line only).
    - Tag DOM (RTL — first child renders RIGHTMOST):
        top box tag:    <button class="mv" data-act="down">▼</button><span>label</span><button class="mv x" data-act="drop">✕</button>
        middle box tag: <button class="mv" data-act="up">▲</button><span>label</span><button class="mv x" data-act="drop">✕</button>
        bottom box tag: <button class="mv" data-act="up">▲</button><span>label</span><button class="mv" data-act="top">⏫</button>
      i.e. screen-RIGHT = single-step arrow (▲ promote / ▼ demote from top), screen-LEFT = jump to
      extreme (✕ to bottom / ⏫ to top). This matches the user's screen-relative spec — verify visually
      in CP2 evidence (screenshot showing a middle tag with ▲ at right edge, ✕ at left edge).
    - CSS (uses existing vars): .tierbox{min-height:46px;border-radius:10px;padding:8px;display:flex;
      flex-wrap:wrap;gap:6px;align-content:flex-start} .tier-top{background:var(--top);border:2px solid
      var(--accent2)} .tier-mid{background:var(--bg);border:1px solid var(--line)}
      .tier-low{background:#eceff1;border:1px dashed var(--line)} .tier-low .tag{opacity:.55;
      filter:grayscale(.6)} .tier-top .tag{background:var(--accent2);color:#fff;border-color:
      var(--accent2);font-weight:600} .tag{display:inline-flex;align-items:center;gap:2px;
      border-radius:16px;padding:2px 4px;background:#fff;border:1px solid var(--line);font-size:.8rem;
      min-height:32px;user-select:none;cursor:grab;touch-action:none} .tag .mv{min-width:26px;
      min-height:26px;border:0;background:transparent;cursor:pointer;font-size:.7rem;opacity:.7}
      .tag .x{color:var(--bad)} empty box → ::after placeholder hint in muted .7rem. Mobile (@media
      max-width:900px): tag font .68rem, .mv 22px, tierbox padding 5px, use SHORT_TOPICS/SHORT_TRAITS
      labels (reuse existing maps + narrowMQ rebuild listener).
    - Behavior: buttons move tags between tiers, update state.tierT/tierC, derive wT/wC (2→10,1→1,0→0),
      save(), render(). Tags keep D.topics/D.traits index order within each box. Reset button restores
      default tiers + advanced sliders + clears anchors.
    - Pointer-drag enhancement per Strategy §4: dragging clone follows pointer, boxes highlight
      (outline: 2px solid var(--accent)) when a drop would land, elementFromPoint targets .tierbox.
      Buttons excluded from drag start.
    - State shape v2: {tierT:[10], tierC:[5], anchors:[], alpha, gamma, lam, beta}. load(): if parsed
      object lacks tierT → return null (fresh defaults).
    Done when: local page (process contract below) renders both widgets with correct defaults; button
    moves re-rank the table live; drag works with mouse; state survives reload; docs/index.html
    untouched per git status.

S3b. Anchor toggle + endorsement scoring in docs/beta/index.html      [builder, 90 min]     → CP3
    - New first table column (narrow: 30px desktop / 24px mobile — mobile table is table-layout:fixed,
      set explicit th width like existing th:first-child rule): per-row toggle button, inline SVG
      bookmark (outline stroke var(--muted) when off; filled var(--accent2) when on), aria-pressed,
      title="שריון — הצבעה בטוחה". Clicking must NOT trigger the row's detail-row/dossier click
      (stopPropagation).
    - Anchored row: class .anchored → background #fdf3d8 (distinct from top8 green), 3px solid #d4a017
      inline-start border, score cell shows 100. Detail row adds line: "ציון מחושב ללא שריון: X.X".
    - Scoring per ENDORSEMENT FORMULA section verbatim (dedupe map precomputed once at load from
      D.endorse). Sort: anchored (by F') then rest (by F'). anchors>8 → warning in #warn span.
    - Note under table gains one sentence explaining שריון and that peer-support from anchored
      candidates counts double.
    - OPTIONAL (only if S3a+S3b under budget): in the detail row and dossier chips block, add
      "נתמך/ת ע"י: <names>" from incoming kept edges, marking doubled ones. Skip freely if tight.
    Done when: locally — anchoring any candidate pins them at top with score 100 and gold styling;
    anchoring #31 (מסאלחה) visibly raises פורום דב members (#47,#38,#51,#46,#41,#07,#45); un-anchoring
    restores; anchors persist across reload; hand-computation check for ONE candidate matches (pick
    #7: compute E_7, bonus, F' by hand from the JSON and compare console value).

S4. Local verification      [verifier, 45 min]     → CP3 evidence
    Give the verifier the VERIFICATION SPEC below + file list (docs/beta/index.html, docs/beta/data.js,
    research/endorsements.json) — not the builder's summary.
    Process contract:
      Start: powershell: cd C:\Users\avaknin\Projects\Primaries\docs; python -m http.server 8123
      Readiness: HTTP 200 from http://localhost:8123/beta/index.html (poll, ≤30s)
      Timeout: kill after 15 min of testing
      Stop: terminate the python process (Stop-Process / Ctrl+C); never wait for natural exit.

S5. Deploy + live verification      [operator-direct then verifier, 30 + 30 min]     → CP4
    Merge/push beta-ui to main. Pre-push gate: `git diff main --stat` (or diff of the merge) shows ONLY
    additions: docs/beta/*, research/endorsements.json, research/build_beta_data.py. Any modification to
    docs/index.html, docs/data.js, README.md, primaries-scoring.xlsx → TRIPWIRE, do not push.
    After push: wait for Pages build (poll the URL, up to ~5 min), then verifier runs the VERIFICATION
    SPEC against https://candidate-calc.github.io/primaries-2026/beta/ (desktop + 375px viewports) AND
    confirms https://candidate-calc.github.io/primaries-2026/ still shows the OLD slider UI with
    data updated 18.7.2026. Deliverable to user: the beta URL.

## CHECKPOINTS
CP1 after S1+S2: report edge counts per kind, 5 sample edges verbatim, EREF value, git status output.
CP2 after S3a: report screenshots (desktop + 375px) of both widgets, default-tier confirmation,
    one before/after ranking change from a tag move, LS key name used.
CP3 after S3b+S4: verifier's full pass/fail table vs the VERIFICATION SPEC, the #7 hand-computation,
    the מסאלחה-anchor delta numbers.
CP4 after S5: live beta URL checks + production-unchanged evidence. I return the final verdict.

## TRIPWIRES (report immediately, don't proceed)
- S1 yields <30 edges post-verification, or >20% of Appendix A items fail re-verification at source.
- Any step requires modifying docs/index.html, docs/data.js, README.md, or the xlsx.
- Drag implementation exceeds 2× its share of budget → ship buttons-only, mark drag UNVERIFIED/dropped,
  report at next checkpoint (buttons are the contract; drag is enhancement).
- GitHub Pages does not serve docs/beta/ after 10 min (unlikely; if so, try adding docs/.nojekyll — but
  that touches docs/, so report first).
- Any step at 2× wall-clock budget; any scope growth (e.g. redesigning advanced sliders).

## VERIFICATION SPEC (S4 locally, S5 live; both desktop ~1280px and mobile 375px viewports)
Green means ALL of:
1. Defaults: topics top tier = exactly {דמוקרטיה ומשפט, דת ומדינה ושוויון בנטל}; traits top = exactly
   {חריצות וביצוע, אומץ ציבורי, מקצועיות וניסיון}; bottom tiers empty; ranking table populated.
2. Buttons: on a middle-tier tag, ▲ (screen-right) moves to top, ✕ (screen-left) to bottom; top-tier ▼
   demotes, ✕ drops to bottom; bottom-tier ▲ to middle, ⏫ to top. Every move re-ranks instantly.
   No numbers visible on any tag.
3. Weight semantics: move ALL topics except ביטחון וחטופים to "לא חשוב" and ביטחון to top → ranking
   reorders to security-heavy candidates; #warn shows nothing until a whole group is zeroed (zero all
   topics → warning appears, no crash/NaN).
4. Drag (desktop): mouse-drag a tag between boxes works, target box highlights. Mobile viewport:
   buttons fully usable with touch/tap; page still scrolls normally.
5. Persistence: change tiers + anchor someone → reload → state intact under 'primaries-params-v2';
   with production open in same browser, its 'primaries-params-v1' state is untouched. Reset restores
   defaults and clears anchors. Corrupt v2 JSON by hand → page loads with defaults, no crash.
6. Anchor: toggle → row pinned first, score 100, gold styling, bookmark filled; detail row shows the
   un-anchored computed score; >8 anchors → warning. Anchor #31 → each פורום דב member's score strictly
   increases vs. un-anchored state (record one before/after pair numerically).
7. Formula audit: for candidate #7, hand-compute E, bonus, F', score from research/endorsements.json
   + current weights and match the displayed score to ±0.1.
8. Mobile 375px: no horizontal overflow anywhere on the rank tab; tags fit the 140px column with short
   labels; all buttons ≥22px tap targets.
9. (S5 only) Production URL unchanged: old slider UI renders, header shows 18.7.2026 data stamp;
   git log shows no commit touched the four protected files.

## OPEN QUESTIONS (none blocking — proceed unless user objects)
- Endorsement transparency in dossiers ("נתמך/ת ע"י") is included only as the optional item in S3b.
- MU=0.2 endorsement-bonus strength is my calibration call (max ±5-10 pts); user can ask to retune at CP4.

## APPENDIX A — endorsement worklist (from scout sweep; verify each at source before writing JSON)
A1. Dossier-attributed items (file NN-*.md : approx line | from→to | kind hint):
04:23-27 #04↔#14 partner(סביבה); #04+#18+#48 event; #04+#01+#15+#44+#45 event; #04+#47+#46+#49 list/event(רשימת סביבה)
06:20 #06↔#47 event(מודעת מפלגה) · 07:21 פורום דב (see A2)
11:21 #30↔#11 partner(5/5 ברית) · 11:22 #28→#11 endorse · 11:23 #26→#11 list(נבחרת)
22:21 #22+#20+#21 event · 26:21-22 נבחרת (A2); #26↔#31 event
28:24 #28↔#50 partner · 29:23 #29↔#34 event · 29:24 ערב רדיקל event: #47,#38,#51,#29,#02,#33
31:26-29 #31+#21 event; #31↔#26 event; #31↔#33 partner(תודה הדדית); #31+#20+#21+#22 event
38:24-30 #18→#38 endorse(5/5); #38↔#20 partner(מטה משותף); #34→#38 endorse; #15→#38 endorse; #38↔#47 partner
47:27-39 #47↔#23 endorse; #47↔#10 endorse; #47→#29 endorse(4.5); #47+#26+#38+#28 partner(תודה הדדית);
         #47→#33 endorse; #47↔#15 partner(מטה פריפריות); #47↔#46 event; 48:28 #48→#28 endorse
50:23-25 #10↔#50 partner(5/5); #50↔#06 partner; #28→#50 endorse
51:22-23 #51↔#47 endorse(5/5); #51↔#38 event(5/5); #51↔#46 partner
02:25-26 #02+#39+#15 event; #02↔#35 event
fb-findings-2026-07.md extras (by line): 182-186 #35→#49 endorse(5/5); 325-331 #10↔#50 partner(5/5);
349-354 #30↔#11 partner(5/5); 427-431 #18↔#41 partner; 68-72 #47→#51,#38→#51 endorse(5/5);
73-76 #04+#18+#48 event
EXCLUDE (non-candidates): תמר זנדברג→#29, יאיר גולן→#38/#28.
A2. Named lists (kind=list edges from publisher to each member, no self-edge):
- פורום דב [r=5, funder #31 מסאלחה, Library ID 1794969478545053] → members: #31,#47,#38,#51,#46,#41,#07,#45
- נבחרת/"התקווה" [r=3, supporter-authored, amplified by #26 רוזין official page] → #47,#33,#38,#09,#28,#50,#11,#26,#46,#49
- ערב "רדיקל — בית לרעיונות" [r=3, party event, Library ID 1066874269101706] → treat as kind=event mutual
  among participants #47,#38,#51,#29,#02,#33 (party-published, so no single candidate publisher).
A3. Candidates with NO found endorsement data (bonus=0, expected): #08,#12,#13,#16,#19 and others absent above.
