# PLAN ARTIFACT — Full deep-research pass, all 51 candidates + Facebook/Ad Library component
# Engagement: Conductor Mode B (planned lane) | Maestro: Fable 5 | Date: 2026-07-18 | Voting: 2026-07-20

## STRATEGY

Two components, deliberately split by executor capability:

1. **Text deep research (39 remaining files)** — builders (Opus), one builder per file, no
   re-touches, spawned in waves. This repeats the proven 18.7 treatment.
2. **Facebook/Ad Library research (all 51 candidates)** — OPERATOR-DIRECT, serial, in the
   main session only. Rationale: the logged-in Chrome connection is bound to your session;
   parallel agents sharing one authenticated browser on the user's PERSONAL Facebook account
   is an account-safety hazard (automation flags) and an unverifiable-access gamble. Never
   hand browser work to a subagent in this engagement.

**Sequencing**: Facebook sweep for the 39 runs BEFORE their builder waves, so each builder
brief carries that candidate's FB findings verbatim and every file is touched exactly once.
The 12 already-done candidates get FB last, as operator-direct appends to their existing
רענון sections (serial edits = no merge risk).

**Decision — FB scope is all 51, not just the 39**: the FB component was never run for
anyone, including the top 12; slate posts are inherently multi-candidate evidence; and the
user's complaint was precisely about tiering candidates. Decided, not open.

**Decision — section label stays `### רענון 18.7.2026`** for all new sections even if work
finishes 19.7: it is a pass label matching the 12 existing files, and the verification grep
depends on uniformity. FB findings for the 12 go under their existing section as
`#### פייסבוק וספריית המודעות`; for the 39 the builder folds FB findings into the new section.

Rejected alternatives: (a) builders doing their own FB browsing — access unverified, account
risk, parallel-browser chaos; (b) one mega-builder for many files — loses the no-re-touch
merge safety that worked on 13.7/18.7; (c) FB after all text work — would force a second
touch on all 39 files.

**Verified baseline facts** (do not re-derive): 12 files have the רענון heading; 39 lack it,
including 23-הדס-רגולסקי.md (Ragolsky = the "#23 gap"; handoff's "all 13" claim was false).
36/51 files already have `## קישורים נוספים` — the 15 without: 08, 12, 14, 16, 17, 19, 20,
24, 30, 31, 36, 39, 40, 42, 44. Meta-language grep baseline across candidates/ = 0 matches.
"Last updated" date = docs/index.html line 155. Git clean except docs build artifacts.

**No process contracts needed**: nothing long-running launches. build_workbook.py and
build_site_data.py are run-to-exit scripts (<1 min, natural termination). No app server.

## STEPS

1. **Working files setup** (operator, 10 min). Create research/fb-findings-2026-07.md
   (FB findings log, one section per candidate: URLs, post dates, quotes, ad-library hits,
   or explicit "לא נמצא") and research/deltas-2026-07-18.md (accumulated ביסוס/T/C delta
   proposals — NOTHING gets applied to build_workbook.py until CP4).
   Done-when: both files exist with headers.

2. **Facebook pilot — 3 candidates** (operator, 45 min). Kariv (richest presence — stress
   test) + 2 from the 39 (pick one Arab-sector candidate, e.g. עלי סלאלחה — tests
   name-search in Arabic/Hebrew). Per candidate, fixed protocol, 8-min timebox: (a) find
   public candidate page/profile, scan recent public posts for endorsements/slate posts;
   (b) search Ad Library (facebook.com/ads/library, Israel, political ads) by candidate
   name; (c) log every finding with URL + date, or "לא נמצא". Public content only — never
   the personal feed, messages, groups, or friend lists.
   Done-when: 3 sections in fb-findings with real URLs or explicit not-found. → CHECKPOINT 1.

3. **FB sweep, remaining 37 of the 39** (operator, 4h). Same protocol, 6-min timebox each,
   in ranked order (highest-scored first) so a forced descope sacrifices the least. Also log
   any slate post naming MULTIPLE candidates in a dedicated "slates" section — it is
   evidence for every named candidate. Batch of ~12, short break between batches (account
   safety: human-paced browsing, no rapid-fire).
   Done-when: all 39 have fb-findings sections.

4. **Builder waves — 39 files, one builder per file, waves of 6** (builder ×39, ~3.5h total,
   ≤30 min/wave). Spawn each wave in one message (parallel). Review every report before the
   next wave: written ACCEPT/REJECT per builder. Brief template (self-contained, per file):
   - Goal: deep-research refresh of <file> per the 18.7 treatment.
   - Context: source rules in 02-sources.md (read it); scoring dims in 04-scoring-method.md.
     PASTE the candidate's fb-findings section verbatim. State whether the file already has
     `## קישורים נוספים` (24 of the 39 do — EXTEND it, never duplicate; 15 lack it — append).
   - Work: verify institutional facts (Knesset/courts/registries) via web; endorsement
     sweep; retag citations per 02-sources.md; add/extend קישורים נוספים (2-5 links, NEVER
     Wikipedia); write `### רענון 18.7.2026` section incl. FB findings.
   - Constraints: NEVER fabricate a citation/URL/fact — write "לא נמצא"; absolute
     meta-language ban (list the banned phrases); citation format [X/5 — מקור]; edit ONLY
     this one .md file — ביסוס/dimension changes are PROPOSED in the report, never applied;
     do not touch build_workbook.py, CSVs, xlsx, docs/.
   - Report: what changed, proposed deltas (CAND/T/C, with evidence), not-founds.
   - "If uncertain: stop and report UNCERTAIN. Do not guess."
   After each wave: run the meta-grep on the 6 files; append accepted deltas to
   deltas-2026-07-18.md. Failed brief → improve once, retry; second failure → escalate to
   maestro with the report. → CHECKPOINT 2 after wave 1; CHECKPOINT 3 after wave 4 (~24 files).

5. **FB sweep + appends, the 12 done candidates** (operator, 1.5h). Kariv already piloted.
   Same protocol for the other 11; operator directly Edits each of the 12 files, appending
   `#### פייסבוק וספריית המודעות` under the existing רענון section (substantive findings or
   one-line "לא נמצא", same citation format, same meta-language ban). Late-discovered slate
   posts naming candidates from the 39: append a line to those files too (serial, safe).
   Done-when: all 51 files carry FB content or explicit not-found.

6. **Delta review and central application** (operator, 1h). Consolidate
   deltas-2026-07-18.md → CHECKPOINT 4 (maestro reviews the full delta list BEFORE any edit
   to build_workbook.py). After my verdict: apply approved deltas to CAND/T/C dicts only,
   sync each changed ביסוס into the matching .md header line (`**ביסוס תיק: X/5**`), run
   build_workbook.py then build_site_data.py, confirm stdout ends
   "data.js written, 51 candidates, 51 dossiers". Note the new top-8 vs old.

7. **Verification** (verifier + operator, 1h). Spawn verifier with the spec below (spec and
   file list, not builder conclusions). In parallel, operator does the FB spot-check (spec
   item 7 — verifier has no FB login). Then bump docs/index.html:155 date, commit.
   → CHECKPOINT 5 (final): verifier report + FB spot-check → maestro close verdict.
   Pushing live/deploy remains the user's call.

## CHECKPOINTS (report to maestro; do not proceed past one without a verdict)

- **CP1** after step 2: minutes per candidate (actual), tool failures, findings sample with
  real URLs, any Facebook friction (captcha, warnings, rate limits). Gate: FB approach
  viable at ~6 min/candidate, or descope proposal.
- **CP2** after builder wave 1: verbatim רענון section from 1 file, meta-grep output for the
  6, delta proposals from the wave, ACCEPT/REJECT lines. Gate: quality before scaling.
- **CP3** after wave 4: files done count, FB sweep status, cumulative deltas, wall-clock vs
  budget. Pulse check.
- **CP4** after step 6 consolidation, BEFORE editing build_workbook.py: full delta list with
  evidence pointers. I approve/trim. Flag any candidate newly entering top-8 (floor-of-1
  mechanic makes big first-evidence swings — expected, but the user votes on this).
- **CP5** final: verifier report verbatim, FB spot-check results, build output tail, new
  ranking top-13.

## TRIPWIRES (unscheduled report, stop the affected work)

- Facebook shows a security checkpoint, captcha, "unusual activity" warning, or any
  automation flag → STOP all FB work immediately, report. Personal account at stake.
- FB averaging >12 min/candidate over any 5 consecutive → report with descope options
  (Ad-Library-only, or ranked top-N cutoff).
- Operator or wave-review finds a cited URL that doesn't resolve or doesn't say what's
  claimed → REJECT that report; on a second fabrication across any builders → report to me.
- Meta-grep >0 after a wave → fix before next wave; recurring pattern → report.
- Any builder edits anything beyond its one .md file → reject outright, report.
- Any step at 2× budget; total wall-clock projecting past 2026-07-19 evening (voting is
  20.7 — an unfinished-but-consistent state beats a complete-but-late one).

## VERIFICATION SPEC (final green; items 1-6, 8 = verifier; item 7 = operator)

1. Meta-language grep (exact pattern below) across candidates/*.md → 0 matches:
   הכלל החדש|כלל חדש|לפי הניקוד|הניקוד החדש|מתודולוגי|לפי השיטה|השיטה החדשה|אין שינוי מספרי|כאמור לעיל|כמתואר לעיל|לפי ההנחי|בהתאם להנחי|העדכון הנוכחי|רענון זה|התיק עודכן|לפי המשקל|בציון הכללי|כפי שצוין
2. All 51 files contain `### רענון 18.7.2026`; exactly one `## קישורים נוספים` per file
   (2-5 links); no wikipedia.org URL inside any קישורים נוספים section.
3. All 51 files contain FB content (findings or explicit לא נמצא).
4. ביסוס cross-check: CAND dict in research/build_workbook.py vs the
   `**ביסוס תיק: X/5**` header line in every .md — zero mismatches (scriptable).
5. Fresh build: build_workbook.py + build_site_data.py run clean, stdout ends
   "data.js written, 51 candidates, 51 dossiers".
6. Spot-check 6 files (4 random from the 39, 1 from the 12, 1 top-5): sections substantive,
   citations tagged [X/5 — מקור]; verifier fetches 2-3 non-Facebook cited URLs per file and
   confirms they resolve and support the claim.
7. FB authenticity (OPERATOR, browser): re-open 5 randomly chosen cited FB post URLs + 3 Ad
   Library claims; confirm each matches the text written in the file. Report alongside CP5.
8. docs/index.html:155 date updated to actual completion date.
   Green = all eight pass. Any builder fix after the verifier run → re-run verifier on the
   affected items or list them UNVERIFIED.

## OPEN QUESTIONS (for the user, non-blocking to start)

- Time budget: total ≈ 11h across 18-19.7. If the user cannot fund that, the pre-designed
  descope is FB in ranked order with a top-N cutoff (steps 3/5 shrink; everything else
  stands). Ask only if CP1/CP3 show the budget breaking.
- Publish: commit is in-plan; pushing the site live before voting is the user's decision.

## AMENDMENT (post-CP1, following user push-back on shortcuts + operator's
## unauthenticated-access discovery) — ADJUST verdict, appended verbatim

VERDICT: ADJUST (steps 1, 2b, 4, 6, 7, the checkpoints, and the verification spec all
survive intact, so this is an amendment, not a replacement artifact.)

The prior handoff conflated "JS-gated" (WebFetch can't render) with "login-gated" (needs
auth); operator's unauthenticated reproduction of the exact slate ad (Library ID
1275064378171547) plus a fully-rendered Kariv page is sufficient evidence. The serial
constraint existed solely to protect the user's personal account; with zero-auth access
there is nothing to protect, and parallelism is safe. One discipline survives: **nothing
that touches the authenticated Chrome session ever goes to a subagent** — it stays
operator-only, reserved for the residual login-gated pages the operator's caveat predicts.

STEP 3a (NEW — FB-scout pilot, 1 scout, 20 min): spawn ONE scout with the brief below for
2 candidates from the remaining 25. Purpose: verify subagents can actually drive the
unauthenticated browser tool (unproven), and calibrate Haiku judgment quality on the
noise-filtering. → CHECKPOINT 1b: scout's raw report + operator's ACCEPT/REJECT + merged
fb-findings diff. Gate: tool works, findings carry real URLs, false-positive rule applied.
If Haiku quality fails, retry the pilot once at a higher tier before falling back to serial.

STEP 3b (REPLACES remainder of steps 3+5 research): waves of 4 scouts × 3 candidates each
(budget 30 min/scout), covering the 23 remaining step-3 candidates then the 11 step-5
candidates (Kariv done) — ~3 waves. Ranked order within waves preserved (descope insurance).
  Scout brief (self-contained, per batch): Goal: FB/Ad Library findings for <names>.
  Protocol per candidate, 8-min cap: (a) public candidate Page via unauthenticated browser
  — recent public posts, endorsements, slate posts; (b) Ad Library keyword+advertiser
  search, date-filtered 1.1.2026–today, top 30 results max. Log per finding: URL, date,
  VERBATIM text snippet, Library ID for ads. Exclusion rule (paste verbatim from
  fb-findings): mass-tagging media/watchdog ads naming many politicians are NOT
  endorsements. Self-reported claims → tag "עדות עצמית — טרם אומת". Hit a login wall →
  log "login-gated, needs operator" and move on. NEVER invent a URL/post; nothing found =
  "לא נמצא". If uncertain: log UNCERTAIN. Report findings as text — do NOT write to any
  file.
STEP 3c (operator, after each wave): review each scout report against its brief (written
ACCEPT/REJECT), merge into fb-findings-2026-07.md yourself — operator is the sole writer
of that file. Sweep any "login-gated" leftovers serially in the authenticated Chrome at
the end (operator-only, human-paced).
Step-5 file appends to the 12 .md files remain operator-direct as planned.

TRIPWIRE (new): a scout reporting findings without URLs/verbatim snippets, or 2+
fabrication-suspect entries across waves → stop fan-out, report to maestro.

Budget: pilot 20 min + 3 waves ≈ 2h — recovers the schedule without cutting a single
corner, which is what the user actually asked for.

Decided: scouts report back, operator merges — single-writer, review-at-merge, no
concurrent-write risk. Prioritization matters much less under parallelism; keep ranked
order only for wave assembly. Wave size 4×3 — wide enough to finish FB research in ~2
hours, small enough that a bad wave is reviewable and cheap to redo.

## Corrections carried forward from maestro's verification pass

- True remaining set is 39 files including `23-הדס-רגולסקי.md`
  (absolute path `C:\Users\avaknin\Projects\Primaries\candidates\23-הדס-רגולסקי.md`).
- 24 of those 39 already have a קישורים נוספים section to extend rather than create.
- Hardcoded "last updated" date is at
  `C:\Users\avaknin\Projects\Primaries\docs\index.html` line 155, not 145.
- Maestro agentId for resuming this planning engagement at checkpoints: a7cf4a25c9e01b0d0
