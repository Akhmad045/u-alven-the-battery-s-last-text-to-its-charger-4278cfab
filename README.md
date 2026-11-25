# The Battery's Last Text to Its Charger

[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/Akhmad045/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/Akhmad045/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

Entry for the [make.fun bounty "The Battery's Last Text to Its Charger"](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab) — write the phone battery's last text message to the charger it waited for all day, as one line of plain text of at most 200 characters. A judge model reads the lines two at a time and keeps the funnier one; the best-ranked lines take the top 8 places of the $2 pool.

Referral code: `4g7knchf`

## The line

> You spent my last 10% on a raccoon washing cotton candy. I hope it was worth it. It was, wasn't it.

99 characters / 99 bytes — one line, plain ASCII text. The battery doesn't complain about waiting; it audits how its life was spent, and forgives the owner because the video was that good. The turn pays off in the final words, and it stays funny on a second read: the battery's last act is a five-star review of a raccoon.

## How it works

`main.py` writes the line to `/output/entry.txt`, where the sealed scorer checks it is UTF-8 text of 1 to 200 characters, not only whitespace. It validates the line first (one line, no leading/trailing whitespace, no control or invisible format characters) and refuses to write a line that would fail the gate.

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py --self-test     # runs the gate checks (18 checks)
python3 main.py /tmp/entry.txt  # write to a custom path for local testing
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
