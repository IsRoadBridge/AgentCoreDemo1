---
name: a-share-dual-score
description: Score A-share swing candidates and next-day open strength using a dual workflow. Use when the user gives one or more A-share stock names or codes and wants: (1) a same-day buy-before-close score using market environment, sector strength, stock strength, volume, position, and risk factors, or (2) a next-day score after 9:25 using stock strength, sector strength, market strength, and opening confirmation for hold/sell decisions.
---

# A-Share Dual Score

Use this skill to run the user's fixed A-share trading workflow.

## Core Workflow

Run two scoring passes:

1. Buy-before-close score:
   - `Market environment`: 10
   - `Sector strength`: 25
   - `Stock strength`: 25
   - `Volume`: 15
   - `Position`: 10
   - `Risk`: 15
   - Total: 100

2. Next-day score:
   - `Pre-score at 9:25`: stock strength 40, sector strength 30, market strength 20, risk 10
   - `Composite score at 9:30-9:35`: use the same 40/30/20/10 frame, but update with opening confirmation

## Data Collection

If the user only gives stock names or codes, search current web sources and fill in the rest:

- Yesterday close and today's open
- 9:25 call auction tone if available
- 9:30-9:35 opening behavior if available
- Sector / concept and whether the sector is in the front ranks
- Broad market tone
- Material risk items such as `ST/*ST`, risk warning, large unlocks, major negative announcements, obvious liquidity weakness

If exact 9:25 auction data is not publicly available, estimate conservatively from the best available opening data and clearly label it as an estimate.

## Hard Filters

If any item below hits, mark the stock as `Do Not Trade` before scoring:

- `ST/*ST`
- Risk warning
- Major negative announcement
- Large unlock pressure
- Poor liquidity

## Buy-Before-Close Scoring Guide

### Market Environment / 10

Score higher when:

- Main indices are not weak
- Intraday trend is stable
- Market mood is not breaking down

### Sector Strength / 25

Score higher when:

- The sector is near the front of the market
- At least 2-3 stocks in the same sector are moving together
- There is a clear leading stock

### Stock Strength / 25

Score higher when:

- The stock is stronger than its sector peers
- Intraday action does not fade badly
- Strength is not only a brief spike

### Volume / 15

Score higher when:

- Turnover is active enough
- Volume expands without looking exhausted
- Pullbacks have reasonable support

### Position / 10

Score lower when:

- It is extended after a large run
- There are long upper shadows
- It already looks like a late chase

### Risk / 15

Score lower when:

- There are unlocks, abnormal volatility notices, financing stress, obvious distribution, or meaningful bad news

## Next-Day Scoring Guide

### Pre-score at 9:25 / 100

- `Stock strength`: 40
- `Sector strength`: 30
- `Market strength`: 20
- `Risk`: 10

### Composite score at 9:30-9:35 / 100

Use the same weights, then adjust for:

- Whether price holds the open
- Whether price can hold yesterday close or nearby key levels
- Whether the sector stays strong after the open
- Whether the broad market turns weak quickly

## Decision Thresholds

### Buy-before-close

- `80+`: tradable
- `65-79`: small probe position only
- `<65`: skip

### Next-day open

- `80+`: hold
- `60-79`: reduce or watch closely
- `<60`: sell / avoid holding

## Output Format

For each stock, return:

1. Stock name and code
2. Hard-filter result
3. Buy-before-close score with six line items
4. Pre-score at 9:25
5. Composite score at 9:30-9:35
6. Trade action: `Buy / Small Probe / Skip / Hold / Reduce / Sell / Watch`
7. Key reasons
8. One-line conclusion

## Style Rules

- Keep the scoring concrete and concise
- Use exact dates when talking about `today` or `tomorrow`
- Link sources when web data is used
- Say clearly when a number is estimated rather than directly observed
