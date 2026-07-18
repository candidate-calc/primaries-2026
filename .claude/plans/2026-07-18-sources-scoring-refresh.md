# Plan: רענון 18.7 — Wikipedia retag, source-framework extension, endorsement research, links, deploy
Maestro plan artifact, 2026-07-18. Vote is 2026-07-20. Total wall-clock budget: ~5.5h. Execute today.
Maestro agent id (resume for checkpoints): ad1c4da1193b88fa0

## OPEN QUESTIONS (relayed to user at start of Phase A; not blocking Phase A)
1. **Research depth.** Deep institutional/endorsement web research for all 51 candidates is a full
   dedicated session; there are 2 days left. Recommendation: mechanical work (retag, sources doc,
   links sections) on all 51 now, deep research only on the current top 13 (קריב, לזימי, רייטן,
   רוזין, פינק, זר קצנשטיין, אביטל, רדמן אבוטבול, שפע, דבוש, לסקי, רגולסקי, אלגרט — per
   04-scoring-method.md ranking; ranks 10–13 sit within 1.1 points of each other, i.e., the real
   decision boundary). Confirm, or name a different cutoff. **Default if no answer by end of
   Phase A: proceed with top 13.**
2. **Rating deltas.** New research findings (endorsements → D5/E2, institutional facts → relevant
   dims, ביסוס changes) will be applied to build_workbook.py and change the published ranking.
   Default: apply them, mirroring 13.7 practice. Tripwire below guards the top-5 order.

## Strategy
Sequence: sources framework first (workers depend on its new tables), then two disjoint-file
tracks in parallel — mechanical pass over the 38 non-top candidates, deep research over the top 13
in 2 waves — then rating application, verification, deploy. One builder touches any given file
exactly once (retag + links + research in a single pass), so no worktree isolation is needed.
Rejected alternatives: (a) deep research on all 51 — doesn't fit the 2-day window and most of it
is below the decision boundary; (b) separate retag and links passes — doubles file touches and
merge risk for no review benefit; (c) editing ביסוס only in .md headers — silently diverges from
the site, which reads ratings-topics.csv, not the headers.

Fact corrections vs. the session's recon: Wikipedia citation tags = 41 in 33 files (not 97; the
other 51 are the header notability lines, untouched). ביסוס and all ratings are authoritative in
research/build_workbook.py (CAND/T/C dicts), regenerated into CSVs+xlsx, then into docs/data.js.

## MANDATORY CLAUSE — paste verbatim into EVERY builder brief that touches a candidate file
> אסור בתכלית: כל לשון תהליכית/מטא בגוף הקובץ. אין לכתוב "הכלל החדש", "לפי הניקוד",
> "המתודולוגיה", "אין שינוי מספרי", "כאמור לעיל", "רענון זה", "לפי ההנחיות", או כל אזכור של
> תהליך המחקר, השיטה או הציונים. בקובץ רק תוכן ענייני על המועמד/ת בתגי `[X/5 — מקור]`
> בסגנון הקיים. מותר: כותרת מדורגת `### רענון 18.7.2026` ומיפוי `→ T3` בסוף שורה, ללא
> הערות סוגריים על ניקוד. עובדה שלא אומתה במקור אמיתי הניתן לבדיקה — משמיטים ומדווחים
> "not found". לעולם לא ממציאים ציטוט או URL. If uncertain: stop and report UNCERTAIN.

Process contract: the only executables are one-shot scripts. `python research/build_workbook.py`
(expect files rewritten, exit 0, <60s) and `python research/build_site_data.py` (expect stdout
`data.js written, 51 candidates, 51 dossiers`, <120s timeout). No servers, nothing to keep alive.

## Steps

### Phase A — framework + mechanical (start immediately)
**1. Rewrite 02-sources.md.** Executor: operator-direct. Budget: 30 min. One file.
   Apply decisions verbatim: (a) שכבה 2 add rows: אוניברסיטאות/מוסדות אקדמיים, משרדי ממשלה,
   צה"ל/דובר צה"ל, גופי רישוי מקצועיים (לשכת עוה"ד, הר"י) — 4-5/5; (b) שכבה 4 add rows:
   הסתדרות, התנועה הקיבוצית, ארגוני מתנדבים, תנועות מחאה, ארגוני פילנתרופיה, with the existing
   COI logic (org the candidate serves praising them ≈3.5/5; dry factual membership record =
   4-5/5 מוסדי); (c) new political-lean table for מכוני מחקר (המכון הישראלי לדמוקרטיה — מרכז;
   מולד — שמאל; קהלת/פורום קהלת — ימין עוין, i.e. 5/5 on hostile ideological criticism of
   on-agenda action, discounted praise — same directional logic as שכבה 3); (d) שכבה 4 note:
   rival-candidate endorsement = 5/5 regardless of channel (organic post, paid/sponsored,
   public broadcast channel); (e) Wikipedia-grounding note in the ביסוס section: זהות עובדה
   באתר חיצוני ובוויקיפדיה שמצטטת אותו ≈ 1.25 מקורות ביסוס, לא 2; ויקיפדיה כמקור סופי נחשבת
   פחות ממקור עצמאי מלא. Done when: all five items present, existing table format/tone kept,
   no other content changed. → **CHECKPOINT 1** (send maestro the diff).

**2. Mechanical pass, 38 non-top candidates.** Executor: builder × 4 in parallel (~9-10 files
   each; needs web access). Budget: 60 min wall-clock. Per file: (i) for each bracketed
   ויקיפדיה tag, open the candidate's he.wikipedia article, trace each tagged fact to a
   footnoted external source; if found, retag to that outlet with its 02-sources.md rating; if
   untraceable, leave the ויקיפדיה tag as-is; the section header stays unless every fact under
   it was retagged; (ii) append `## קישורים נוספים` section with 2-5 links; (iii) do NOT change
   ביסוס, ratings, or דגלים. Also (operator-direct, 2 min): delete the leftover meta-fragment
   `(אין שינוי מספרי — כבר גבוה)` from candidates\03-מורן-זר-קצנשטיין.md line 18.
   → **CHECKPOINT 2**.

### Phase B — deep research, top 13 (gated on Open Q1 default: proceed)
**3. Research wave 1 — ranks 1-6** (קריב, לזימי, רייטן, רוזין, פינק, זר קצנשטיין).
**4. Research wave 2 — ranks 7-13** (אביטל, רדמן, שפע, דבוש, לסקי, רגולסקי, אלגרט).
   Per candidate: retag+links, institutional verification, endorsement sweep (recommended-slate
   posts, Meta Ad Library), think-tank items. Report proposed ביסוס/dim deltas — NOT applied to
   files directly. → **CHECKPOINT 3 after each wave**.

**5. Apply accepted deltas.** Edit build_workbook.py (CAND/T/C dicts) + .md ביסוס headers; run
   build_workbook.py; git diff must show only intended rows. Update collected date + ranking
   table in 04-scoring-method.md if order changed.

### Phase C — verify + deploy
**6. Verification sweep** (spec below) → **CHECKPOINT 4**, before push.
**7. Build + deploy.** build_site_data.py, git commit+push origin main (user-authorized), confirm
   live via WebFetch.

## Tripwires
- Any spot-checked URL fails to load / doesn't support the claimed fact → batch suspect, stop.
- Applying deltas changes top-5 order → report before pushing.
- git diff after build_workbook.py touches unintended rows (esp. פרמטרים sheet) → stop.
- Meta-phrase grep still has hits after one fix pass → stop, list them.
- Any step at 2× budget; builder wanting to restructure sections or edit דגלים.
- Hard deadline: if Phase B not done by 19.7 12:00, deploy what's verified, report the cut.

## Verification spec
1. Meta-phrase sweep over candidates/*.md, expect 0:
   `הכלל החדש|כלל חדש|לפי הניקוד|הניקוד החדש|מתודולוגי|לפי השיטה|השיטה החדשה|אין שינוי מספרי|כאמור לעיל|כמתואר לעיל|לפי ההנחי|בהתאם להנחי|העדכון הנוכחי|רענון זה|התיק עודכן|לפי המשקל|בציון הכללי|כפי שצוין`
2. Pipeline: build_workbook.py then build_site_data.py run clean; stdout ends
   `data.js written, 51 candidates, 51 dossiers`.
3. Verifier (fresh eyes): spot-check 6 files, retag ratings match 02-sources.md, ≥8 URLs load
   and support their facts, קישורים נוספים format consistent, no meta language.
4. Format integrity, all 51: header line regexes intact; ביסוס ∈[1,5] matches build_workbook.py.
5. data.js sanity: contains a string added today, collected=18.7.2026, 51 dossiers.
