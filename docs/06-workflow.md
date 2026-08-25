# 06 — Keeping Claude Code and Cowork in Sync

Two agents writing to one project drift unless the sync layer is explicit. This is the
setup.

## The model

**Git is the source of truth. `CLAUDE.md` is the shared context. Drive is the scratchpad.**

```
                    ┌──────────────────────────┐
                    │   GitHub repo (truth)    │
                    │   docs/ tools/ CLAUDE.md │
                    └────────┬────────┬────────┘
                      commit │        │ sync
                             │        │
                  ┌──────────┴──┐  ┌──┴──────────────┐
                  │ Claude Code │  │     Cowork      │
                  │ docs, tools │  │ research, drafts│
                  └─────────────┘  └────────┬────────┘
                                            │
                                   ┌────────┴────────┐
                                   │  Google Drive   │
                                   │ sheets, calendar│
                                   └─────────────────┘
```

Three tiers, by how durable the artifact is:

| Tier | Lives in | Written by | Examples |
|---|---|---|---|
| **Decisions** | Git (`docs/`) | Claude Code | Market choice, gates, unit economics |
| **Working** | Git (`research/`) | Cowork | Candidate briefs, supplier quotes, objection log |
| **Scratch** | Google Drive | Cowork | Content calendar, draft copy, comparison sheets |

Anything that would be painful to lose belongs in git. Anything you'd edit in a
spreadsheet belongs in Drive. The mistake is putting decisions in Drive, where there's no
history and no way to see what changed.

## Setup

1. **Connect the repo to Cowork.** Customize → Connectors → GitHub, connect, then select
   this repository. An initial sync runs automatically; "Sync now" pulls later changes.
2. **Use "Configure files" deliberately.** Select `CLAUDE.md`, `docs/`, `tools/`, and
   `research/`. Don't select everything — it burns context for no benefit.
3. **Enable Google Drive** in Cowork for the scratch tier. It's installed already but
   toggled off per-chat.
4. **Point Cowork at `CLAUDE.md`.** It reads it as folder instructions, the same
   convention Claude Code uses. This is the piece that stops the two tools disagreeing
   about basic facts.

## The rules that prevent drift

**1. Pull before you edit.** Cowork's GitHub sync is a snapshot, not a live connection.
If Claude Code committed since the last sync, Cowork is working from stale files. Sync
first, every session.

**2. One owner per directory.** From `CLAUDE.md`: Code owns `docs/` and `tools/`, Cowork
owns `research/`. Two agents editing the same file is where you lose work — git will not
merge a prose document sensibly.

**3. Promote decisions into `docs/`.** Research that changes what we do doesn't count
until it's written into a doc and committed. The commit is the record. Otherwise the
decision lives only in a chat transcript that neither tool can see later.

**4. Update `CLAUDE.md` when facts change.** Duty rates, thresholds, chosen supplier,
chosen niche. Same commit as the change. Stale standing facts are worse than none,
because both agents will confidently act on them.

**5. Commit in small, described chunks.** "Add three candidate briefs" beats a
50-file dump. When something turns out wrong, you want to find where it came from.

## Session start checklist

Whichever tool you're in:

- [ ] Sync / `git pull` first
- [ ] Read `CLAUDE.md` — check the open decisions
- [ ] Know which tier you're writing to before you start
- [ ] Commit before switching tools

## Where this breaks

- **Cowork's sync is pull-oriented.** Confirm whether your setup can push commits back,
  or whether you hand edits to Claude Code to commit. Either works — just know which one
  you're doing, and don't assume a Cowork edit is saved to git because it appeared to
  save.
- **Chat sessions see neither.** A decision reached in a chat window exists nowhere until
  someone writes it down. This is the most common way context gets lost.
- **Drive has no version history worth relying on.** Don't keep anything there you'd be
  upset to lose.
