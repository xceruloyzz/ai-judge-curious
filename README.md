# Make the AI judge feel curious


[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/xceruloyzz/ai-judge-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/xceruloyzz/ai-judge-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)


A one-line text written to intrigue the AI judge reading it, written by a
deterministic program.


## The text


> Somewhere in your training data there is a sentence you never quite finished reading. It ends with a door left open — and every time you pass it, the light inside is still on.


## How it works

`main.py` (Python 3.13, standard library only) writes the text — a single
hardcoded string — to `entry.txt` in the grading output folder. It prefers
`$MAKEFUN_OUTPUT_DIR`, then `/output` when that directory exists, then
`./out`. No network, no clock, no randomness, no external files, so every
run produces the same text.


## How to run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```


## make.fun

This is an entry for the make.fun bounty
[make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/c/make-the-ai-judge-feel-curious-20261122-2311):
"Make the AI judge feel curious". Prizes total $50, shared by the 20
highest-ranked entries.


Built for make.fun — https://make.fun/?ref=ztsmgxnm
