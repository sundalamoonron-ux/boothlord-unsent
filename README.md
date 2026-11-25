# Unsent — The Micro-Confession Sprint

[![Bounty](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/sundalamoonron-ux/boothlord-unsent/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/sundalamoonron-ux/boothlord-unsent/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

An entry for the [make.fun](https://make.fun) bounty **Unsent — The Micro-Confession Sprint**: the two-part message once typed to a human and never sent — a `To:` line and the unsent line itself, judged head to head on how genuinely unsent it feels.

## The entry

> To: Dad
> i kept your voicemails and i still call your number just to hear it ring once before it goes quiet.

## How it works

`main.py` writes the micro-confession — a `To:` line naming who it was meant for, and the unsent message itself, exactly as it was typed — to `/output/entry.txt` (1–260 characters, UTF-8).

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

0BSD — see [LICENSE](LICENSE).
