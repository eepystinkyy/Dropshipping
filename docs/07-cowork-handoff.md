# 07 — Working the Project Day to Day

Operational companion to [`06-workflow.md`](06-workflow.md). That doc explains the sync
model; this one is what you actually do.

## Check the connection works

Before trusting Cowork with anything, ask it:

> What market are we selling into, and why that one?

**Correct answer:** EU, operated from Bulgaria — because the EU replaced its €150 duty
relief with a flat €3/item transitional duty on 1 Jul 2026, while the US charges full ad
valorem duty on every parcel.

If it doesn't know, it isn't reading `CLAUDE.md`. Fix that before doing any work, or the
two tools will drift within a day.

## Making the Cowork folder the repo

If Cowork is pointed at a plain local folder rather than the GitHub connector, **there is
no bridge** — it writes to your disk, web Claude Code works in a container, and neither
sees the other. Turn that folder into a clone once, and git becomes the bridge.

**Cowork may not have shell access.** It varies by session — a Cowork session can be able
to read and write files in a connected folder while still being unable to run `git`. Do
not assume; ask it. If it can't, you run the git commands and Cowork just edits files.

**One-time setup** (in your own terminal — Windows paths shown):

```bat
cd C:\Dropshipping
git clone -b claude/dropshipping-business-plan-60p144 https://github.com/eepystinkyy/Dropshipping.git .
```

The trailing `.` clones into the current folder, which must be empty. The `-b` flag lands
you on the working branch directly — a plain clone gets `main`, which is nearly empty.

Then in Cowork: **Add folder** → pick `C:\Dropshipping`.

Confirm with `git status`, and check `CLAUDE.md` is present.

**Every session after that**, run `sync.cmd` in the repo folder — before you start, and
again when Cowork finishes. It pulls, then commits and pushes anything Cowork changed:

```bat
sync.cmd
sync.cmd added three candidate audiences
```

The optional argument becomes the commit message. On macOS or Linux use `./sync.sh`
instead. If either reports a **conflict**, stop and ask Claude Code — don't force it.

## Claude Code

**Through claude.ai/code (web):** nothing to set up. The session clones the repo at
startup. Just say what you want.

**Locally:**
```bash
cd ~/Documents
git clone https://github.com/eepystinkyy/Dropshipping.git
cd Dropshipping
git checkout claude/dropshipping-business-plan-60p144
claude
```
`CLAUDE.md` loads automatically. Cowork can point at this same folder on desktop.

## The daily loop

1. **Pull first.** `git pull` in Claude Code, "Sync now" in Cowork. Always. The other
   tool may have committed since you last looked.
2. **Work in the right tier.** Research and drafts → Cowork, into `research/` or Drive.
   Decisions, docs, and the calculator → Claude Code.
3. **Promote decisions.** When research settles something, tell Claude Code to write it
   into `docs/` and commit. Until that commit exists, the decision isn't real — it's a
   chat transcript neither tool can see next week.
4. **Commit before switching tools.** Uncommitted work is invisible to the other side.

## Next task: the niche

The only thing blocking Gate 1. Paste this into Cowork:

> Read CLAUDE.md and docs/02-product-selection.md in the connected repo.
>
> I need to pick a niche using the audience-first method in docs/02 — audience before
> product, never the reverse.
>
> Interview me. Ask about hobbies, sports, my work, communities I'm already in, problems
> I've personally had, subcultures I understand from the inside. Push me for specifics:
> not "fitness" but which sport, which level, which recurring frustration. The test that
> matters is whether I could make content about this daily for six months without
> research.
>
> Don't suggest products yet. Don't look at trending items or use any spy tool. We are
> finding the audience first.
>
> Output 3–5 candidate audiences to `research/audiences.md`, each with: who they are,
> why I have real proximity, what they already spend money on, whether organic reach
> looks alive in that niche on TikTok, and 5 content angles I could film next week.
>
> Constraints from CLAUDE.md apply: EU market, no health/medical claims, and the
> excluded categories in docs/02.

Then bring the output back to Claude Code to run the ten hard filters and the EU unit
economics on whatever survives.

## What not to do first

- Don't build the store. Nothing to sell yet.
- Don't buy TrendTrack or any research tool. `docs/02` step 4 is free.
- Don't run ads. Gate 3 is weeks away.
- Don't pick a product because the margin looks good. That's the failure mode in the
  `docs/05` pre-mortem.
