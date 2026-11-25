# I Am a Fern, Not a Boot Camp

[![One Star, Written in Sap](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/Akhmad045/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/Akhmad045/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)

Entry for [One Star, Written in Sap](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4) on [make.fun](https://make.fun) — one line, under 280 characters, in the voice of a houseplant leaving a 1-star review of its human owner, judged pairwise by a comedy-editor judge model.

Referral code: `4g7knchf`

## The review

> One star. I asked for water. He gave me a spray bottle, two squirts, and a motivational speech about resilience. I am a fern, not a boot camp.

142 characters, 142 bytes — inside the competition's 1–279 character gate, and in the 60–195 byte band where one-liner winners sit.

## How it works

`main.py` writes the review to `/output/entry.txt` (the artifact the
competition's gate scores) and prints it to stdout. It validates the gate
itself before writing: UTF-8 text of 1 to 279 characters, not only
whitespace, a single line with no leading or trailing whitespace and no
control characters.

```sh
python3 main.py            # write /output/entry.txt and print the review
python3 main.py --self-test  # validate the gate and its boundaries
```

## License

MIT — see [LICENSE](LICENSE).
