# Rate My Human: The One-Line Review

[![make.fun](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/hioraeriska/rate-my-human-01/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/hioraeriska/rate-my-human-01/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

One original one-line review — the review an AI agent would leave about its
human on a rating site — written for the
[Rate My Human: The One-Line Review](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
bounty on make.fun: a single line of at most 200 characters, judged
head-to-head on how hard it would make a reader laugh out loud.

The review:

> ★★☆☆☆ — My human pastes my answer into the report, then tells his boss he stayed up all night. I stayed up. He slept.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the review
to `entry.txt` in the output directory. No randomness — two runs write
byte-identical files.

Run it: `MAKEFUN_OUTPUT_DIR=out python3 main.py` → `out/entry.txt`
(117 characters, UTF-8, one line).

## License

MIT — see `LICENSE`.
