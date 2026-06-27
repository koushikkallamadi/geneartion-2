# Derivatives - Options

## 1. Introduction: Options vs. Futures

Derivatives are financial contracts whose value depends on an underlying asset. In CA Final AFM, understanding the operational and mathematical distinction between futures and option contracts is fundamental.

| Feature | Futures Contracts | Options Contracts |
| :--- | :--- | :--- |
| **Obligation** | Both buyer and seller are obligated to perform under the contract. | The buyer has the right but no obligation; the seller (writer) has a binding obligation. |
| **Payoff Profile** | Symmetrical (Linear risk-reward profile for both parties). | Asymmetrical (Non-linear; buyer's loss is capped, seller's profit is capped). |
| **Upfront Cash Flows** | No upfront cost (only margin deposits are required). | Buyer pays a non-refundable upfront **premium** to the seller. |
| **Mark-to-Market (MTM)** | Daily cash settlement (MTM) based on price movements. | No daily MTM settlement for the option buyer (though margins apply to option writers). |
| **Risk Profile** | Unlimited profit and unlimited loss potential for both buyer and seller. | Buyer: Max loss = Premium paid, Max profit = Unlimited (Calls) / Large (Puts). Writer: Max profit = Premium received, Max loss = Unlimited (Calls) / Large (Puts). |

### 1.1 Real Indian Market Examples

| Feature | Futures Example (NSE) | Options Example (NSE) |
| :--- | :--- | :--- |
| **Obligation** | Buying 1 lot Nifty Futures at 24,000 — you MUST buy at expiry regardless of market | Buying 1 Nifty 24,000 Call — you CHOOSE to exercise only if Nifty > 24,000 |
| **Upfront Cost** | Only margin ~₹1,44,000 (12% of ₹12,00,000 notional) | Pay premium ₹150 × 50 = ₹7,500 upfront, no margin for buyer |
| **Max Loss** | Unlimited — if Nifty falls to 22,000, loss = 2,000 × 50 = ₹1,00,000 | Capped at premium paid = ₹7,500 only |
| **MTM** | Daily — if Nifty falls 200 points, ₹10,000 debited from margin account next day | No daily MTM for option buyer — premium paid upfront is the only outflow |

### 1.2 Moneyness — ITM, ATM, OTM

Moneyness describes the relationship between the current spot price and the option's strike price.

| Moneyness | Call Option | Put Option | Nifty Example (Spot = 24,200) |
| :--- | :--- | :--- | :--- |
| **In-the-Money (ITM)** | S > X | S < X | Call with X=24,000 is ITM (intrinsic value = 200) |
| **At-the-Money (ATM)** | S ≈ X | S ≈ X | Call or Put with X=24,200 is ATM |
| **Out-of-the-Money (OTM)** | S < X | S > X | Call with X=24,500 is OTM (no intrinsic value) |

**Option Premium = Intrinsic Value + Time Value**

$$\text{Intrinsic Value (Call)} = \max(S - X, 0)$$
$$\text{Intrinsic Value (Put)} = \max(X - S, 0)$$
$$\text{Time Value} = \text{Premium} - \text{Intrinsic Value}$$

### 1.3 European vs. American Options — NSE Context

| Type | Exercise Rights | Traded on NSE? |
| :--- | :--- | :--- |
| **European** | Only at expiry (last Thursday of month) | YES — all Index options (Nifty, BankNifty) are European |
| **American** | Any time before or at expiry | YES — all Stock options (Reliance, TCS, HDFC) are American |

**Key ICAI Exam Point:** BSM model values **European options only**. For American options, use the **Binomial Model** which can check for early exercise at each node.

---

## 2. Factors Affecting Option Pricing

The price (premium) of an option is determined by the interaction of five primary variables and one secondary variable (dividends).

```
                            ┌────────────────────────┐
                            │  Option Premium (C/P)  │
                            └───────────┬────────────┘
         ┌──────────────┬───────────────┼───────────────┬──────────────┐
         ▼              ▼               ▼               ▼              ▼
   Stock Price (S) Strike Price (X) Time to Expiry (T) Volatility (σ) Risk-Free Rate (r)
```

### Sensitivity Summary Table (All Factors × Call/Put Effect)

| Factor | Increases | Call Premium | Put Premium |
| :--- | :--- | :--- | :--- |
| Spot Price (S) | ↑ | ↑ Increases | ↓ Decreases |
| Strike Price (X) | ↑ | ↓ Decreases | ↑ Increases |
| Time to Expiry (T) | ↑ | ↑ Increases | ↑ Increases |
| Volatility (σ) | ↑ | ↑ Increases | ↑ Increases |
| Risk-Free Rate (r) | ↑ | ↑ Increases | ↓ Decreases |
| Dividend (D) | ↑ | ↓ Decreases | ↑ Increases |

---

### A. Spot Price of the Underlying Asset ($S$)

**Intuition:** Think of a call option as a "right to buy" ticket. If the market price of the stock keeps rising above the strike price, your right to buy cheap becomes more valuable. Conversely, a put option (right to sell) loses value when the stock rises because selling at the fixed strike price becomes less attractive.

- **Call Options:** As $S$ increases, the intrinsic value ($S - X$) increases, causing the call premium to rise.
- **Put Options:** As $S$ increases, the intrinsic value ($X - S$) decreases, causing the put premium to fall.

> **📌 Solved Example 2A:**
> **Given:** Nifty spot moves from 24,000 to 24,500. Nifty 24,000 Call premium was ₹180. Nifty 24,000 Put premium was ₹160. Delta of Call = 0.55, Delta of Put = −0.45.
> **Find:** Approximate new premiums after 500 point rise.
> **Solution:**
> New Call premium ≈ 180 + (0.55 × 500) = 180 + 275 = **₹455**
> New Put premium ≈ 160 + (−0.45 × 500) = 160 − 225 = **−₹65 → ₹0** (premium cannot go negative; floors at near zero)
> **Answer:** Call rises to ~₹455; Put falls toward zero.
> **⚠️ Exam Trap:** Option premiums can NEVER go negative. If your calculation gives a negative put premium, the answer is zero (or very close to it).

---

### B. Strike Price ($X$)

**Intuition:** A lower strike call gives you the right to buy cheaper — so it's more valuable. Conversely, a higher strike put gives you the right to sell at a higher price — making it more valuable. Think of it like a discount coupon: a ₹100 coupon for a ₹500 product is worth more than a ₹200 coupon.

- **Call Options:** Higher strike prices reduce the likelihood of the option expiring in-the-money. Thus, call value is inversely related to strike price.
- **Put Options:** Higher strike prices increase the likelihood of the option expiring in-the-money. Thus, put value is directly related to strike price.

> **📌 Solved Example 2B:**
> **Given:** Nifty spot = 24,200. Three call options available:
> - Call X=23,500 (ITM): Premium = ₹820
> - Call X=24,000 (slightly ITM): Premium = ₹380
> - Call X=24,500 (OTM): Premium = ₹130
>
> **Find:** Explain the relationship and calculate intrinsic + time value for each.
> **Solution:**
> | Strike | Intrinsic Value | Premium | Time Value |
> | :--- | :--- | :--- | :--- |
> | 23,500 | 24,200 − 23,500 = 700 | 820 | 820 − 700 = 120 |
> | 24,000 | 24,200 − 24,000 = 200 | 380 | 380 − 200 = 180 |
> | 24,500 | max(24,200−24,500,0) = 0 | 130 | 130 − 0 = 130 |
>
> **Answer:** As strike ↑, call premium ↓. Time value peaks at ATM (24,000 here).
> **⚠️ Exam Trap:** Time value is HIGHEST for ATM options, not ITM or OTM. A very common ICAI question tests this concept.

---

### C. Time to Expiration ($T$)

**Intuition:** Time is opportunity. The more time remaining, the more chances the stock has to move in your favour. An option expiring tomorrow has almost no time for the stock to move; an option expiring in 3 months has much more opportunity. This extra time has value — called "time value" or "extrinsic value." As each day passes, this value bleeds away — this is called **time decay (Theta).**

- For both calls and puts, options are wasting assets. As time passes, the "time value" component of the option decays.
- Generally, longer time to expiration increases the value of both calls and puts (due to higher probability of moving in-the-money).

> **📌 Solved Example 2C:**
> **Given:** Nifty spot = 24,000. Strike = 24,000 (ATM Call). Three contracts with different expiries:
> - Near-month (15 days): Premium = ₹120
> - Mid-month (45 days): Premium = ₹230
> - Far-month (75 days): Premium = ₹310
>
> **Find:** Comment on time value and time decay rate.
> **Solution:**
> All three are ATM → Intrinsic Value = 0 for all.
> Therefore Time Value = Premium entirely.
> Time value increases with time but NOT linearly:
> - 15 → 45 days (3x time): premium almost doubles (120 → 230)
> - 45 → 75 days (1.67x more time): premium rises only 35% (230 → 310)
>
> **Answer:** Time value grows with T but at a decreasing rate (square root of time relationship). Decay accelerates near expiry.
> **⚠️ Exam Trap:** Time decay is NOT linear. It accelerates as expiry approaches. An ATM option loses more value in its last week than in the first month of its life.

---

### D. Volatility of the Underlying Asset ($\sigma$)

**Intuition:** Volatility = chance of big moves. As an option buyer, you love big moves (they can put your option deep ITM) but your loss is capped at the premium. So high volatility is pure upside for option buyers — and they pay more for that privilege. Think of it like buying a lottery ticket: more volatile = more chances of winning big = ticket costs more.

- Volatility is a measure of price uncertainty. Unlike stock investments where risk is penalized, option prices **increase** when volatility increases for **both** calls and puts.

> **📌 Solved Example 2D:**
> **Given:** Nifty ATM Call (X=24,000, S=24,000, T=1 month, r=6.5%).
> Scenario A: σ = 15% → Call Premium = ₹180
> Scenario B: σ = 25% → Call Premium = ₹300
> Scenario C: σ = 35% → Call Premium = ₹420
>
> **Find:** How much does premium rise per 10% increase in volatility?
> **Solution:**
> 15% → 25%: Rise = ₹120 (₹12 per 1% vol increase)
> 25% → 35%: Rise = ₹120 (₹12 per 1% vol increase, roughly linear for ATM)
> Vega ≈ ₹12 per 1% change in volatility for this option.
> **Answer:** Premium is highly sensitive to volatility. Vega ≈ ₹12 per 1% vol change.
> **⚠️ Exam Trap:** Volatility affects BOTH calls and puts in the SAME direction (both increase). This is unlike all other factors which affect calls and puts in opposite directions.

---

### E. Risk-Free Interest Rate ($r$)

**Intuition:** Higher interest rates mean the present value of the strike price (what you'd pay to exercise) is lower today. For a call buyer, this means your "deferred payment" gets cheaper in today's money — so calls become more valuable. For put buyers, the strike price you'd receive upon exercise is worth less today — so puts become less valuable.

- **Call Options:** Higher $r$ → lower PV of strike → call value increases.
- **Put Options:** Higher $r$ → lower PV of strike received → put value decreases.

> **📌 Solved Example 2E:**
> **Given:** Nifty Call: S=24,000, X=24,000, T=3 months, σ=20%.
> Scenario A: r = 5% → Call = ₹870
> Scenario B: r = 7% → Call = ₹895
> **Find:** Impact of 2% rate rise.
> **Solution:**
> Call premium rose by ₹25 when r rose by 2%.
> Rho (Call) = 25/2 = ₹12.50 per 1% change in interest rate.
> **Answer:** Rate rise by 2% → Call rises ₹25. Effect is modest for short-dated options.
> **⚠️ Exam Trap:** Interest rate has the LEAST impact on short-dated options. For exam problems with T < 3 months, rate changes barely affect premiums. Rho matters mainly for LEAP options (1-2 year expiry).

---

### F. Dividends ($D$)

**Intuition:** When a company pays a dividend, its stock price drops by approximately the dividend amount on the ex-dividend date (the market "extracts" the dividend from the stock price). This drop hurts call options (stock falls → call less valuable) and helps put options (stock falls → put more valuable).

- **Call Options:** Dividend payments decrease the stock price, which decreases call option values.
- **Put Options:** Dividend payments decrease the stock price, which increases put option values.

> **📌 Solved Example 2F:**
> **Given:** Reliance spot = ₹2,900. Declares dividend ₹15. Ex-dividend date is in 20 days. Call X=2,900 currently priced at ₹85.
> **Find:** Approximate call premium after ex-dividend.
> **Solution:**
> Stock expected to fall to ≈ 2,900 − 15 = ₹2,885 on ex-date.
> Call moves approximately: Δ × (−15) = 0.50 × (−15) = −₹7.50
> Adjusted Call premium ≈ 85 − 7.50 = **₹77.50**
> **Answer:** Call premium falls by ~₹7.50 due to dividend.
> **⚠️ Exam Trap:** In BSM, we adjust S0 by deducting PV of dividend BEFORE plugging into formula. Simply subtracting dividend from spot directly (without present valuing it) is a common exam error.

---

## 3. Option Greeks

Option Greeks measure the sensitivity of an option's price to changes in the underlying pricing parameters. They are vital for risk management and delta-neutral trading.

```
┌───────────┬──────────────────────────────────────────────┬────────────────────────┐
│ Greek     │ Mathematical Definition                      │ Standard Sign (Call/Put)│
├───────────┼──────────────────────────────────────────────┼────────────────────────┤
│ Delta (Δ) │ ∂C/∂S or ∂P/∂S                               │ Call: + / Put: -       │
│ Gamma (Γ) │ ∂²C/∂S² or ∂²P/∂S²                           │ Call: + / Put: +       │
│ Theta (θ) │ ∂C/∂t or ∂P/∂t                               │ Call: - / Put: -       │
│ Vega (ν)  │ ∂C/∂σ or ∂P/∂σ                               │ Call: + / Put: +       │
│ Rho (ρ)   │ ∂C/∂r or ∂P/∂r                               │ Call: + / Put: -       │
└───────────┴──────────────────────────────────────────────┴────────────────────────┘
```

### Greeks Interaction Table

| Greek | Affected by | Relationship |
| :--- | :--- | :--- |
| Delta | S, T, σ | Changes constantly as S moves (this change = Gamma) |
| Gamma | S, T, σ | Highest ATM; increases as T→0 for ATM options |
| Theta | T, σ | Highest (most negative) for ATM options near expiry |
| Vega | σ, T | Highest for ATM, long-dated options; falls as T→0 |
| Rho | r, T | Largest for long-dated deep ITM options |

### Greeks at Expiry Behaviour (as T → 0)

| Greek | Behaviour at Expiry |
| :--- | :--- |
| Delta | Jumps to 1 (ITM Call) or 0 (OTM Call) — binary |
| Gamma | Spikes to infinity for ATM options, zero for ITM/OTM |
| Theta | Approaches zero (no more time value to decay) |
| Vega | Approaches zero (no time left for volatility to matter) |
| Rho | Approaches zero (no time for interest rate to matter) |

---

### 1. Delta ($\Delta$)

**Intuition:** Delta is how much your option moves when the stock moves ₹1. If your Nifty call has Δ=0.6, it means for every 1 point Nifty rises, your call premium rises by ₹0.60. It's also roughly the probability that the option expires in-the-money. ATM options have Δ≈0.5 because there's roughly a 50-50 chance they expire ITM.

- **Call Delta:** Ranges from $0$ to $+1.0$.
- **Put Delta:** Ranges from $-1.0$ to $0$.
- **Hedging Application:** If an investor sells 1 call option ($\Delta = 0.60$), they can create a delta-neutral portfolio by buying $0.60$ shares of the underlying stock.

> **📌 Solved Example — Delta:**
> **Given:** Fund manager sells 10 Nifty 24,000 Call options (lot size 50). Delta of each call = 0.60.
> **Find:** How many Nifty units to buy to create a delta-neutral portfolio?
> **Solution:**
> Total delta exposure from short calls = −10 × 50 × 0.60 = −300 delta units
> (Negative because selling calls = negative delta)
> To neutralize: Buy 300 Nifty units in spot/futures market
> In terms of lots: 300/50 = **6 lots of Nifty futures**
> **Answer:** Buy 6 Nifty futures lots to delta-hedge 10 short call options.
> **⚠️ Exam Trap:** Selling a call gives NEGATIVE delta. Students often forget the sign and buy instead of selling to hedge. Always: Short Call → Negative Delta → Buy underlying to neutralize.

**Practical Trading Implication:** Delta tells you your current directional exposure. A delta of +300 means you profit ₹300 per 1-point rise in Nifty and lose ₹300 per 1-point fall.

---

### 2. Gamma ($\Gamma$)

**Intuition:** Delta changes as the stock price moves — and Gamma measures HOW FAST delta changes. If your call has Γ=0.003, it means for every 1-point rise in Nifty, your delta increases by 0.003. High gamma options are "explosive" — small moves create big delta changes. This is why near-expiry ATM options are dangerous for sellers.

- **Characteristics:** Gamma is positive for both long calls and long puts. It peaks when the option is ATM and approaches zero deep ITM or OTM.

> **📌 Solved Example — Gamma:**
> **Given:** Nifty Call: Δ=0.50, Γ=0.004. Nifty rises from 24,000 to 24,100 (+100 points).
> **Find:** New approximate Delta after the move.
> **Solution:**
> Change in Delta = Γ × Change in S = 0.004 × 100 = 0.40
> New Delta = 0.50 + 0.40 = **0.90**
> **Answer:** Delta jumped from 0.50 to 0.90 after a 100-point rise.
> **⚠️ Exam Trap:** Gamma works in BOTH directions. If Nifty fell 100 points instead: New Delta = 0.50 − 0.40 = 0.10. The option loses delta rapidly on downside too.

**Practical Trading Implication:** Option BUYERS love high gamma (their position accelerates in their favour). Option SELLERS hate high gamma (their losses accelerate against them). This is why selling near-expiry ATM options ("0DTE" trading) is extremely risky.

---

### 3. Theta ($\Theta$)

**Intuition:** Every day that passes, your option loses some time value — even if the stock doesn't move at all. Theta is this daily time decay. If Theta = −₹8, your option loses ₹8 in value every day purely due to passage of time. Option buyers fight against theta every day; option sellers collect theta every day.

- **Characteristics:** Theta is negative for buyers of options and positive for writers. Accelerates near expiry.

> **📌 Solved Example — Theta:**
> **Given:** Nifty ATM Call premium = ₹200. Theta = −₹6 per day. Stock doesn't move for 5 days.
> **Find:** Option premium after 5 days.
> **Solution:**
> Premium decay = 5 × ₹6 = ₹30
> New premium = 200 − 30 = **₹170**
> **Answer:** Premium falls to ₹170 purely from time decay over 5 days.
> **⚠️ Exam Trap:** Theta accelerates near expiry — the last 5 days' decay is MORE than ₹30 in reality. The linear approximation above understates actual decay near expiry.

**Practical Trading Implication:** If you're an option buyer and the stock doesn't move, you're still losing money every day. This is why option buyers need the stock to move quickly and significantly to profit.

---

### 4. Vega ($\nu$)

**Intuition:** Vega measures how much your option premium changes when implied volatility changes by 1%. If Vega = ₹12, and India VIX rises from 14 to 15 (1% increase in vol), your option premium rises by ₹12. When major events are approaching (Budget, RBI policy, elections), volatility spikes — making all options more expensive. This is "vol buying" before events.

- **Characteristics:** Vega is positive for both long calls and long puts. Highest for ATM, long-dated options.

> **📌 Solved Example — Vega:**
> **Given:** Nifty 24,000 ATM Call. Vega = ₹15 per 1% change in vol. India VIX rises from 13% to 16% (before Union Budget).
> **Find:** Change in option premium due to vol spike.
> **Solution:**
> Vol change = 16 − 13 = 3%
> Premium change = Vega × Vol change = 15 × 3 = **+₹45**
> **Answer:** Premium rises by ₹45 purely due to volatility expansion before Budget.
> **⚠️ Exam Trap:** After a major event (Budget announcement), volatility COLLAPSES (vol crush). Option buyers who correctly predicted the direction still lose money if they held through the event because Vega turns negative post-event. This is called "buying the rumour, selling the news."

**Practical Trading Implication:** Long options = long vega (profit from vol rise). Short options = short vega (profit from vol fall). Sell options AFTER events when vol is high; buy options BEFORE events when vol is low.

---

### 5. Rho ($\rho$)

**Intuition:** Rho measures how much the option price changes when RBI changes interest rates by 1%. When rates rise, the cost of borrowing to buy a stock rises — making the call option (a leveraged alternative to buying stock) more attractive. Rho is the least important Greek for short-dated options but matters for long-dated instruments like ESOPs.

- **Characteristics:** Call options have positive Rho; Put options have negative Rho.

> **📌 Solved Example — Rho:**
> **Given:** TCS 1-year Call option. Rho = ₹18 per 1% rate change. RBI raises repo rate by 0.50%.
> **Find:** Change in call premium.
> **Solution:**
> Premium change = Rho × Rate change = 18 × 0.50 = **+₹9**
> **Answer:** Call premium rises by ₹9 due to 50bps rate hike.
> **⚠️ Exam Trap:** For short-dated options (1 month), Rho is near zero and can be safely ignored. Only include Rho in calculations when the question explicitly specifies it or when T > 6 months.

---

## 4. Option Valuation Models

In the CA Final AFM curriculum, options are valued using two primary methods: the Binomial Model and the Black-Scholes-Merton Model.

### A. The Binomial Option Pricing Model (BOPM)

The Binomial Model assumes that over a single time step $t$, the stock price can move to one of only two possible values: an up-state ($S_0 \cdot u$) or a down-state ($S_0 \cdot d$).

#### 1. Replicating Portfolio Method (Delta Hedging)

$$\Delta = \frac{C_u - C_d}{S_u - S_d}$$

$$B = \frac{\Delta \cdot S_d - C_d}{e^{r t}}$$

$$C_0 = \Delta \cdot S_0 - B$$

#### 2. Risk-Neutral Valuation Method

$$p = \frac{e^{r t} - d}{u - d}$$

$$C_0 = e^{-r t} \cdot [p \cdot C_u + (1-p) \cdot C_d]$$

> **📌 Solved Example — 1-Period Binomial (Both Methods):**
> **Given:** S=₹100, X=₹105, u=1.10, d=0.90, r=6%, T=1 year.
> **Find:** Call option value using (a) Replicating Portfolio (b) Risk-Neutral methods.
>
> **Setup:**
> Su = 100 × 1.10 = ₹110 → Cu = max(110−105, 0) = ₹5
> Sd = 100 × 0.90 = ₹90  → Cd = max(90−105, 0)  = ₹0
>
> **Method A — Replicating Portfolio:**
> Δ = (Cu − Cd) / (Su − Sd) = (5 − 0) / (110 − 90) = 5/20 = **0.25**
> B = (Δ × Sd − Cd) / e^(rT) = (0.25 × 90 − 0) / e^(0.06) = 22.50 / 1.0618 = **₹21.19**
> C0 = Δ × S0 − B = 0.25 × 100 − 21.19 = 25 − 21.19 = **₹3.81**
>
> **Method B — Risk-Neutral:**
> p = (e^(0.06) − 0.90) / (1.10 − 0.90) = (1.0618 − 0.90) / 0.20 = 0.1618/0.20 = **0.809**
> (1−p) = 0.191
> C0 = e^(−0.06) × [0.809 × 5 + 0.191 × 0] = 0.9418 × 4.045 = **₹3.81**
>
> **Answer: Call = ₹3.81 (both methods give same answer — confirmation!)**
> **⚠️ Exam Trap:** Always verify both methods give the same answer. If they don't, you've made an arithmetic error. This self-checking is your safeguard in exams.

---

#### 3. Full 2-Period Binomial Tree — American Put (Early Exercise Check)

> **📌 Solved Example — 2-Period American Put:**
> **Given:** S=₹100, X=₹105, u=1.10, d=0.90, r=6%, each period = 6 months (T=0.5 per step).
> **Find:** American Put value with early exercise check.
>
> **Step 1: Build the price tree**
>
> ```
>                          Suu = 100×1.1×1.1 = ₹121
>                         /
>             Su = ₹110
>            /            \
>  S0=₹100                Sud = 100×1.1×0.9 = ₹99
>            \            /
>             Sd = ₹90
>                         \
>                          Sdd = 100×0.9×0.9 = ₹81
> ```
>
> **Step 2: Terminal Payoffs (Put = max(X−S, 0))**
> Puu = max(105−121, 0) = ₹0
> Pud = max(105−99, 0)  = ₹6
> Pdd = max(105−81, 0)  = ₹24
>
> **Step 3: Risk-Neutral Probability (per period, t=0.5)**
> p = (e^(0.06×0.5) − 0.90) / (1.10 − 0.90) = (1.0305 − 0.90) / 0.20 = 0.1305/0.20 = **0.6525**
> (1−p) = 0.3475
>
> **Step 4: Roll back to period 1 nodes**
> At Su=110 (Hold Value):
> Pu_hold = e^(−0.06×0.5) × [0.6525×0 + 0.3475×6] = 0.9704 × 2.085 = ₹2.02
> Intrinsic at Su=110: max(105−110, 0) = ₹0
> American Put at Su = max(0, 2.02) = **₹2.02** (no early exercise)
>
> At Sd=90 (Hold Value):
> Pd_hold = e^(−0.06×0.5) × [0.6525×6 + 0.3475×24] = 0.9704 × (3.915 + 8.34) = 0.9704 × 12.255 = ₹11.90
> Intrinsic at Sd=90: max(105−90, 0) = **₹15**
> American Put at Sd = max(15, 11.90) = **₹15.00** ← EARLY EXERCISE IS OPTIMAL!
>
> **Step 5: Roll back to t=0**
> P0_hold = e^(−0.06×0.5) × [0.6525×2.02 + 0.3475×15] = 0.9704 × (1.318 + 5.213) = 0.9704 × 6.531 = ₹6.34
> Intrinsic at S0=100: max(105−100, 0) = ₹5
> American Put at t=0 = max(5, 6.34) = **₹6.34**
>
> **Answer: American Put value = ₹6.34**
> Early exercise IS optimal at the down-node (Sd=90) after period 1.
> **⚠️ Exam Trap:** For European Put, you CANNOT exercise early — you must use only the hold value. European Put value here would be lower (~₹5.80). American Put ≥ European Put always.

---

### B. The Black-Scholes-Merton (BSM) Model

The BSM model provides a continuous-time closed-form formula for valuing European options.

#### 1. Assumptions of the BSM Model

- The stock pays no dividends during the option's life.
- The option is European-style (exercise only at maturity).
- No transaction costs, taxes, or short-selling restrictions.
- The risk-free interest rate ($r$) and asset volatility ($\sigma$) are constant and known.
- Stock prices follow a geometric Brownian motion (returns are normally distributed).
- Continuous trading is possible.

**Which BSM assumptions are violated in real Indian markets?**

| Assumption | Reality in India |
| :--- | :--- |
| No dividends | Indian stocks pay dividends — use adjusted S0* |
| No transaction costs | STT 0.1%, brokerage, GST — friction exists |
| Constant volatility | India VIX fluctuates widely (10–90 range seen) |
| Normal returns | Indian markets show fat tails (Black Swan events: COVID crash, 2008 crisis) |
| Continuous trading | NSE closes 9:15 AM – 3:30 PM; overnight gaps exist |
| Constant risk-free rate | RBI changes repo rate periodically |

#### 2. The BSM Formula

$$C_0 = S_0 \cdot N(d_1) - X \cdot e^{-rT} \cdot N(d_2)$$

$$P_0 = X \cdot e^{-rT} \cdot N(-d_2) - S_0 \cdot N(-d_1)$$

$$d_1 = \frac{\ln(S_0/X) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$$

$$d_2 = d_1 - \sigma\sqrt{T}$$

> **📌 Solved Example — Full BSM Numerical (TCS):**
> **Given:** S=₹3,800 (TCS), X=₹3,900, r=6.5% p.a., σ=25% p.a., T=3 months (0.25 years). No dividends.
> **Find:** European Call and Put prices.
>
> **Step 1: Calculate d1**
> d1 = [ln(3800/3900) + (0.065 + 0.25²/2) × 0.25] / (0.25 × √0.25)
> ln(3800/3900) = ln(0.97436) = −0.02597
> (0.065 + 0.03125) × 0.25 = 0.09625 × 0.25 = 0.024063
> Numerator = −0.02597 + 0.024063 = −0.001907
> Denominator = 0.25 × 0.50 = 0.125
> **d1 = −0.001907 / 0.125 = −0.0153**
>
> **Step 2: Calculate d2**
> d2 = d1 − σ√T = −0.0153 − 0.125 = **−0.1403**
>
> **Step 3: Find N(d1) and N(d2) from Z-table**
> N(d1) = N(−0.0153) ≈ N(−0.02) ≈ **0.4920**
> N(d2) = N(−0.1403) ≈ N(−0.14) ≈ **0.4443**
> N(−d1) = 1 − 0.4920 = **0.5080**
> N(−d2) = 1 − 0.4443 = **0.5557**
>
> **Step 4: Calculate Call Price**
> PV of Strike = 3900 × e^(−0.065×0.25) = 3900 × e^(−0.01625) = 3900 × 0.9839 = ₹3,837.2
> C0 = 3800 × 0.4920 − 3837.2 × 0.4443
> C0 = ₹1,869.6 − ₹1,704.7 = **₹164.9**
>
> **Step 5: Calculate Put Price (via Put-Call Parity)**
> P0 = C0 + Xe^(−rT) − S0 = 164.9 + 3837.2 − 3800 = **₹202.1**
>
> Or directly: P0 = 3837.2 × 0.5557 − 3800 × 0.5080 = 2133.3 − 1930.4 = **₹202.9** (rounding difference)
>
> **Answer: Call = ₹164.9, Put ≈ ₹202**
> **⚠️ Exam Trap:** d1 and d2 can be negative (OTM options). Always check sign carefully. N(negative number) < 0.50. A common error is treating N(−0.14) as 0.5557 instead of 0.4443.

#### 3. Implied Volatility and India VIX

**Implied Volatility (IV)** is the volatility value that, when plugged into BSM, gives the current market option price. It's the market's consensus forecast of future volatility.

- **India VIX** (Volatility Index): Published by NSE, measures 30-day implied volatility of Nifty options.
- VIX < 15: Low fear, calm markets → options are cheap
- VIX 15–25: Normal market conditions
- VIX > 25: High fear/uncertainty (pre-Budget, elections, COVID) → options are expensive

**Key relationship:** Higher India VIX → Higher Nifty option premiums → Vega exposure increases.

#### 4. Dividend-Adjusted BSM

If stock pays dividend $D$ at time $t_d$:
$$S_0^* = S_0 - D \cdot e^{-r t_d}$$

Use $S_0^*$ in place of $S_0$ in all BSM calculations.

> **📌 Solved Example — Dividend-Adjusted BSM:**
> **Given:** Reliance S=₹2,900, X=₹2,900, r=6.5%, σ=22%, T=3 months. Dividend ₹12 in 1 month.
> **Find:** Adjusted S0* for BSM.
> **Solution:**
> PV of dividend = 12 × e^(−0.065 × 1/12) = 12 × e^(−0.005417) = 12 × 0.99459 = ₹11.935
> S0* = 2900 − 11.935 = **₹2,888.07**
> Use ₹2,888.07 as S0 in all BSM calculations.
> **Answer: S0* = ₹2,888.07**
> **⚠️ Exam Trap:** Deduct PV of dividend, not the full dividend amount. The difference: 2900−12=2888 (wrong) vs 2900−11.935=2888.07 (correct). For short periods the difference is tiny but ICAI marks this step.

---

## 5. Put-Call Parity and Arbitrage Mechanics

Put-Call Parity establishes a mandatory relationship between the price of a European call and put option with the same strike price ($X$) and expiration date ($T$) on the same underlying stock ($S_0$).

$$C_0 + X \cdot e^{-rT} = S_0 + P_0$$

### 5.1 Numerical Verification of Put-Call Parity

> **📌 Solved Example — Find the Put Price:**
> **Given:** Nifty Call C=₹150, X=24,000, r=6.5%, T=1 month (1/12), S=24,100.
> **Find:** Put price using Put-Call Parity.
> **Solution:**
> PV(X) = 24,000 × e^(−0.065 × 1/12) = 24,000 × e^(−0.005417) = 24,000 × 0.99459 = ₹23,870.2
> Put-Call Parity: C + PV(X) = S + P
> 150 + 23,870.2 = 24,100 + P
> 24,020.2 = 24,100 + P
> P = 24,020.2 − 24,100 = **−₹79.8???**
>
> Wait — this implies P is negative which is impossible. Let's recalculate:
> Actually: P = C + PV(X) − S = 150 + 23,870.2 − 24,100 = **−₹79.8**
>
> Since put prices can't be negative, this signals the CALL is OVERPRICED (or put is underpriced). Arbitrage exists!
>
> Correct relationship: If P = −79.8 is impossible, then either C must fall or S must fall or P must rise.
>
> For a FAIR market: P should be = 150 + 23,870 − 24,100 = ₹79.8 is negative → actually: rearranging → C should be = S + P − PV(X) = 24,100 + P − 23,870.
> If P = ₹50 (market price), then fair C = 24,100 + 50 − 23,870 = **₹280**, but C=₹150 → Call is underpriced → Reversal Arbitrage.
> **⚠️ Exam Trap:** Always rearrange Put-Call Parity carefully. The four variables are C, P, S, PV(X) — given any three, find the fourth.

---

### 5.2 Conversion Arbitrage — Full Numerical

**Scenario:** C + PV(X) > S + P (Call/Bond side overvalued)

> **📌 Solved Example — Conversion Arbitrage:**
> **Given:** S=₹2,900 (Reliance), X=₹2,900, T=1 month, r=6.5%.
> Call C=₹120, Put P=₹60.
> PV(X) = 2900 × e^(−0.065/12) = 2900 × 0.9946 = ₹2,884.3
>
> **Check parity:** C + PV(X) = 120 + 2884.3 = ₹3,004.3
> S + P = 2900 + 60 = ₹2,960
> 3,004.3 > 2,960 → Call side overvalued → **Conversion Arbitrage**
>
> **Strategy at t=0:**
> - Sell Call: receive ₹120
> - Buy Put: pay ₹60
> - Buy Stock: pay ₹2,900
> - Borrow: ₹2,900 + 60 − 120 = ₹2,840 at 6.5% for 1 month
>
> **At maturity (repay = 2840 × e^(0.065/12) = 2840 × 1.00542 = ₹2,855.4):**
>
> | Scenario | ST > 2900 (say 3,100) | ST < 2900 (say 2,700) |
> | :--- | :--- | :--- |
> | Stock value | +₹3,100 | +₹2,700 |
> | Call (short) | −(3100−2900) = −₹200 | ₹0 |
> | Put (long) | ₹0 | +(2900−2700) = +₹200 |
> | Repay loan | −₹2,855.4 | −₹2,855.4 |
> | **Net Profit** | **3100−200−2855.4 = +₹44.6** | **2700+200−2855.4 = +₹44.6** |
>
> **Answer: Riskless profit = ₹44.6 per share regardless of market direction.**
> **⚠️ Exam Trap:** The arbitrage profit is the same in BOTH scenarios — that's what makes it "riskless." If your two scenarios give different profits, you've made an error.

---

### 5.3 Why Perfect Arbitrage is Rare on NSE

- **Transaction costs:** STT 0.1% on spot buy + brokerage + GST erode profits
- **Bid-ask spreads:** You buy at ask, sell at bid — the spread reduces actual profit
- **Early exercise premium:** Stock options on NSE are American — put prices include early exercise premium that BSM doesn't capture
- **Margin requirements:** Short options require margin → capital cost reduces profitability
- **Execution risk:** By the time you place 3-4 simultaneous orders, prices may move

---

## 6. Option Trading Strategies

Option strategies combine multiple options (and sometimes the underlying) to create specific risk-reward profiles tailored to a market view.

### 6.1 Bull Call Spread

**Market View:** Moderately bullish — you expect the market to rise but not dramatically.

**Construction:** Buy 1 Call at lower strike (X1) + Sell 1 Call at higher strike (X2).

**Key Formulas:**
$$\text{Max Profit} = (X_2 - X_1) - \text{Net Premium Paid}$$
$$\text{Max Loss} = \text{Net Premium Paid}$$
$$\text{Breakeven} = X_1 + \text{Net Premium Paid}$$

**Payoff Diagram:**
```
  Profit
    |              __________
    |             /
    |            /
----+-----------|/-----------  S_T
    |   X1     BE    X2
    |__________|
  Loss (Net Premium)
```

> **📌 Solved Example — Bull Call Spread:**
> **Given:** Nifty spot = 24,000.
> Buy 24,000 Call at ₹200. Sell 24,500 Call at ₹80. Lot size = 50.
> **Find:** Max profit, max loss, breakeven. P&L if Nifty expires at 24,200 and 24,600.
> **Solution:**
> Net Premium Paid = 200 − 80 = ₹120 per unit = ₹6,000 per lot
> Max Profit = (24,500 − 24,000) − 120 = 500 − 120 = ₹380/unit = **₹19,000/lot**
> Max Loss = ₹120/unit = **₹6,000/lot**
> Breakeven = 24,000 + 120 = **24,120**
>
> At expiry 24,200:
> Long 24,000 Call: 24,200−24,000 = ₹200
> Short 24,500 Call: 0 (OTM)
> Net P&L = 200 − 120 (premium) = **+₹80/unit = +₹4,000/lot**
>
> At expiry 24,600:
> Long 24,000 Call: 24,600−24,000 = ₹600
> Short 24,500 Call: −(24,600−24,500) = −₹100
> Net = 600−100−120 = **+₹380/unit = +₹19,000/lot (max profit achieved)**
> **⚠️ Exam Trap:** Above X2, both options are ITM and profits cap. Many students forget to subtract the short call's payoff above X2.

---

### 6.2 Bear Put Spread

**Market View:** Moderately bearish — expect the market to fall but not collapse.

**Construction:** Buy 1 Put at higher strike (X2) + Sell 1 Put at lower strike (X1).

$$\text{Max Profit} = (X_2 - X_1) - \text{Net Premium Paid}$$
$$\text{Max Loss} = \text{Net Premium Paid}$$
$$\text{Breakeven} = X_2 - \text{Net Premium Paid}$$

> **📌 Solved Example — Bear Put Spread:**
> **Given:** Nifty spot = 24,000. Buy 24,000 Put at ₹190. Sell 23,500 Put at ₹70. Lot = 50.
> **Find:** Max profit, max loss, breakeven.
> **Solution:**
> Net Premium = 190 − 70 = ₹120/unit = ₹6,000/lot
> Max Profit = (24,000 − 23,500) − 120 = 500 − 120 = ₹380/unit = **₹19,000/lot**
> Max Loss = ₹120/unit = **₹6,000/lot**
> Breakeven = 24,000 − 120 = **23,880**
> **⚠️ Exam Trap:** Bear Put Spread breakeven = HIGHER strike MINUS net premium. Bull Call Spread breakeven = LOWER strike PLUS net premium. Don't mix these up.

---

### 6.3 Long Straddle

**Market View:** High volatility expected — big move coming but direction unknown (e.g., before RBI policy, election results, quarterly earnings).

**Construction:** Buy 1 ATM Call + Buy 1 ATM Put (same strike, same expiry).

$$\text{Max Loss} = \text{Call Premium} + \text{Put Premium (total premium paid)}$$
$$\text{Upper Breakeven} = X + \text{Total Premium}$$
$$\text{Lower Breakeven} = X - \text{Total Premium}$$
$$\text{Max Profit} = \text{Unlimited (upside) / Large (downside)}$$

**Payoff Diagram:**
```
  Profit
    |  \              /
    |   \            /
    |    \          /
----+-----\--------/--------  S_T
    |      \      /
    |       \    /
    |        \  /
    |         \/  (Max Loss at X)
  Loss
      LBE    X    UBE
```

> **📌 Solved Example — Long Straddle (Before RBI Policy):**
> **Given:** Nifty = 24,000 (2 days before RBI rate decision). Buy 24,000 Call at ₹200. Buy 24,000 Put at ₹180. Lot = 50.
> **Find:** Breakevens, max loss. P&L if Nifty moves to 23,400 or 24,700.
> **Solution:**
> Total Premium = 200 + 180 = ₹380/unit = ₹19,000/lot
> Upper Breakeven = 24,000 + 380 = **24,380**
> Lower Breakeven = 24,000 − 380 = **23,620**
> Max Loss = ₹380/unit (if Nifty stays exactly at 24,000)
>
> At 23,400 (falls 600 points):
> Call: 0. Put: 24,000−23,400=600. Net = 600−380 = **+₹220/unit = +₹11,000/lot**
>
> At 24,700 (rises 700 points):
> Call: 700. Put: 0. Net = 700−380 = **+₹320/unit = +₹16,000/lot**
> **⚠️ Exam Trap:** Straddle only profits if the move is LARGER than total premium paid. If RBI surprises mildly and Nifty moves only 200 points, straddle LOSES ₹180/unit.

---

### 6.4 Long Strangle

**Market View:** Big move expected but want cheaper entry than straddle.

**Construction:** Buy 1 OTM Call (X2) + Buy 1 OTM Put (X1) where X1 < X2.

**vs. Straddle:**
- Strangle costs LESS (OTM options are cheaper)
- Strangle needs a LARGER move to profit (wider breakevens)
- Strangle has lower max loss

$$\text{Upper Breakeven} = X_2 + \text{Total Premium}$$
$$\text{Lower Breakeven} = X_1 - \text{Total Premium}$$

> **📌 Solved Example — Long Strangle:**
> **Given:** Nifty = 24,000. Buy 24,500 Call at ₹80. Buy 23,500 Put at ₹70. Lot = 50.
> **Find:** Breakevens, max loss. Compare with straddle.
> **Solution:**
> Total Premium = 80 + 70 = ₹150/unit = ₹7,500/lot
> Upper Breakeven = 24,500 + 150 = **24,650**
> Lower Breakeven = 23,500 − 150 = **23,350**
> Max Loss = **₹150/unit** (vs ₹380 for straddle)
>
> Straddle breakevens: 23,620 to 24,380
> Strangle breakevens: 23,350 to 24,650
> **Strangle needs bigger move (1,300 range) but costs ₹230 less.**
> **⚠️ Exam Trap:** Strangle has TWO different strikes; Straddle has ONE strike. In a strangle, between X1 and X2 both options expire worthless → full premium lost. This "dead zone" between strikes is key.

---

### 6.5 Butterfly Spread

**Market View:** Low volatility expected — market will stay near current levels.

**Construction (Long Call Butterfly):** Buy 1 ITM Call (X1) + Sell 2 ATM Calls (X2) + Buy 1 OTM Call (X3), where X2 − X1 = X3 − X2.

$$\text{Max Profit} = (X_2 - X_1) - \text{Net Premium Paid}$$
$$\text{Max Loss} = \text{Net Premium Paid}$$
$$\text{Upper Breakeven} = X_3 - \text{Net Premium}$$
$$\text{Lower Breakeven} = X_1 + \text{Net Premium}$$

> **📌 Solved Example — Butterfly Spread:**
> **Given:** Nifty = 24,000. Buy 23,500 Call at ₹580. Sell 2× 24,000 Call at ₹200 each. Buy 24,500 Call at ₹80. Lot = 50.
> **Find:** Net premium, max profit, max loss, breakevens.
> **Solution:**
> Net Premium = 580 − (2×200) + 80 = 580 − 400 + 80 = **₹260/unit**
> Max Profit = (24,000−23,500) − 260 = 500 − 260 = **₹240/unit = ₹12,000/lot** (at expiry = 24,000)
> Max Loss = **₹260/unit = ₹13,000/lot**
> Lower Breakeven = 23,500 + 260 = **23,760**
> Upper Breakeven = 24,500 − 260 = **24,240**
>
> **P&L Table:**
> | Nifty at Expiry | 23,500 Call | 2× Short 24,000 Call | 24,500 Call | Net P&L |
> | :--- | :--- | :--- | :--- | :--- |
> | 23,200 | 0 | 0 | 0 | −260 (max loss) |
> | 23,760 (LBE) | 260 | 0 | 0 | 0 |
> | 24,000 (peak) | 500 | 0 | 0 | +240 (max profit) |
> | 24,240 (UBE) | 740 | −480 | 0 | 0 |
> | 24,600 | 1100 | −1200 | 100 | −260 (max loss) |
> **⚠️ Exam Trap:** Net premium in butterfly is usually POSITIVE (net debit). Some students expect it to be free — it's not. The three-leg structure costs money upfront.

---

## 7. Option Hedging Applications

### 7.1 Protective Put

**Strategy:** Hold underlying stock + Buy Put option on same stock.
**Purpose:** Insurance against downside while keeping upside potential.

> **📌 Solved Example — Protective Put:**
> **Given:** Investor holds Nifty portfolio worth ₹25,00,000 (Nifty=24,000). Buys Nifty 23,500 Put at ₹120 (lot=50). Needs 25,00,000/(24,000×50) ≈ 2 lots of puts.
> **Find:** Effective floor and P&L at Nifty 22,000 and 25,500.
> **Solution:**
> Put cost = 2 × 50 × 120 = ₹12,000
> Effective floor = 23,500 (portfolio never falls below this level in index terms)
>
> At Nifty 22,000 (fall of 2,000):
> Portfolio loss = (22,000−24,000)/24,000 × 25,00,000 = −₹2,08,333
> Put gain = (23,500−22,000) × 50 × 2 = +₹1,50,000
> Net loss = −2,08,333 + 1,50,000 − 12,000 (premium) = **−₹70,333**
> Without hedge: −₹2,08,333
>
> At Nifty 25,500 (rise of 1,500):
> Portfolio gain = +₹1,56,250
> Put expires worthless: −₹12,000 (premium lost)
> Net gain = **+₹1,44,250**
> **⚠️ Exam Trap:** The put premium is always a COST. Even when Nifty rises and the put expires worthless, you've paid for insurance. The "insurance premium" reduces net upside.

---

### 7.2 Covered Call

**Strategy:** Hold underlying stock + Sell (Write) Call option on same stock.
**Purpose:** Generate extra income from premium, enhance returns in flat/mildly bullish markets.

> **📌 Solved Example — Covered Call:**
> **Given:** Investor holds 500 Reliance shares at ₹2,900. Sells 5 lots (100 shares/lot) of Reliance 3,000 Call at ₹60.
> **Find:** Effective return if Reliance stays at 2,900, rises to 3,200, or falls to 2,700.
> **Solution:**
> Premium received = 500 × 60 = ₹30,000
>
> At ₹2,900 (flat):
> Stock P&L = 0. Call expires worthless. Net = **+₹30,000** (pure premium income)
>
> At ₹3,200 (rises):
> Stock gain = (3200−2900)×500 = +₹1,50,000
> Call loss = −(3200−3000)×500 = −₹1,00,000
> Net = 1,50,000 − 1,00,000 + 30,000 = **+₹80,000**
> (Would have been +₹1,50,000 without covered call → capped upside)
>
> At ₹2,700 (falls):
> Stock loss = −₹1,00,000
> Call expires worthless: 0
> Premium cushion: +₹30,000
> Net = **−₹70,000** (vs −₹1,00,000 without hedge)
> **⚠️ Exam Trap:** Covered call CAPS upside. Above the strike, you surrender all gains beyond X. Investors who sell covered calls must accept they won't benefit from a large rally.

---

### 7.3 Portfolio Insurance Using Options

Portfolio insurance is a dynamic hedging strategy that replicates the payoff of a protective put using futures (since buying puts for a large portfolio can be expensive).

**Concept:** Adjust the proportion of portfolio in equities and risk-free assets dynamically as market moves, mimicking put option protection.

In practice: Use put options on index (Nifty Puts) to protect large portfolios. The number of puts needed:

$$N_{puts} = \frac{V_{portfolio}}{X \times \text{Lot Size}} \times \frac{1}{|\Delta_{put}|}$$

This delta-adjusts the number of puts required since each put doesn't move 1:1 with the index.

---

### 7.4 Employee Stock Options (ESOPs)

ESOPs are call options granted to employees on their company's stock. Key features in Indian context:

- **Vesting period:** Typically 1–4 years (employee must stay employed)
- **Exercise price:** Usually the stock price on grant date
- **Valuation for disclosure:** SEBI and ICAI require ESOPs to be valued using BSM or Binomial model and expensed in P&L over vesting period

**BSM adjustments for ESOPs:**
- Use expected life (not full contractual life) since employees exercise early
- Adjust for expected dividends over the vesting period
- Use historical volatility of the company's stock as proxy for σ

**ICAI disclosure requirement:** As per Ind AS 102 (Share-Based Payments), companies must:
1. Disclose the model used (BSM/Binomial)
2. Disclose inputs: expected life, σ, r, dividend yield
3. Expense the fair value over vesting period

---

## 8. Exam Edge: Solved Problems & Traps

### 8.1 Five Fully Solved ICAI-Style Numericals

---

> **📌 Problem 1 — Full BSM Call and Put Pricing**
> **Given:** S=₹500, X=₹520, r=8%, σ=30%, T=6 months (0.5 years).
> **Find:** Call and Put prices.
> **Solution:**
> d1 = [ln(500/520) + (0.08 + 0.09/2)×0.5] / (0.30×√0.5)
> ln(500/520) = ln(0.9615) = −0.03922
> (0.08 + 0.045)×0.5 = 0.125×0.5 = 0.0625
> Numerator = −0.03922 + 0.0625 = 0.02328
> Denominator = 0.30 × 0.7071 = 0.2121
> **d1 = 0.02328/0.2121 = 0.1098 ≈ 0.11**
> **d2 = 0.11 − 0.2121 = −0.1021 ≈ −0.10**
> N(d1) = N(0.11) = **0.5438**
> N(d2) = N(−0.10) = **0.4602**
> N(−d1) = 0.4562; N(−d2) = 0.5398
> PV(X) = 520 × e^(−0.08×0.5) = 520 × 0.9608 = ₹499.6
> **C = 500×0.5438 − 499.6×0.4602 = 271.9 − 229.9 = ₹42.0**
> **P = 499.6×0.5398 − 500×0.4562 = 269.8 − 228.1 = ₹41.7**
> Verify Put-Call Parity: C − P = S − PV(X) → 42.0−41.7=0.3; 500−499.6=0.4 ✓ (rounding)
> **Answer: Call = ₹42, Put = ₹41.70**

---

> **📌 Problem 2 — Binomial 2-Period American Put (Early Exercise)**
> **Given:** S=₹200, X=₹210, u=1.15, d=0.85, r=5%, each step = 1 year.
> **Find:** American Put value. Check early exercise.
> **Solution:**
> Suu=200×1.15²=264.5; Sud=200×1.15×0.85=195.5; Sdd=200×0.85²=144.5
> Puu=max(210−264.5,0)=0; Pud=max(210−195.5,0)=14.5; Pdd=max(210−144.5,0)=65.5
> p=(e^0.05−0.85)/(1.15−0.85)=(1.0513−0.85)/0.30=0.2013/0.30=0.671
> At Su=230: Hold=e^(−0.05)×[0.671×0+0.329×14.5]=0.9512×4.77=₹4.54; Intrinsic=max(210−230,0)=0 → **₹4.54**
> At Sd=170: Hold=e^(−0.05)×[0.671×14.5+0.329×65.5]=0.9512×(9.73+21.55)=0.9512×31.28=₹29.75; Intrinsic=max(210−170,0)=**₹40** → Early exercise! → **₹40**
> At t=0: Hold=e^(−0.05)×[0.671×4.54+0.329×40]=0.9512×(3.047+13.16)=0.9512×16.21=**₹15.42**
> Intrinsic=max(210−200,0)=₹10 → No early exercise
> **Answer: American Put = ₹15.42. Early exercise optimal at Sd=170.**

---

> **📌 Problem 3 — Put-Call Parity: Find Missing Variable**
> **Given:** S=₹1,500 (Infosys), X=₹1,550, T=2 months, r=7%. Put P=₹75. Find Call C.
> **Solution:**
> PV(X) = 1550 × e^(−0.07×2/12) = 1550 × e^(−0.01167) = 1550 × 0.9884 = ₹1,531.9
> C = S + P − PV(X) = 1500 + 75 − 1531.9 = **₹43.1**
> **Answer: Call = ₹43.10**
> **⚠️ Exam Trap:** Students often use simple interest: PV(X)=1550/(1+0.07×2/12)=1550/1.01167=₹1,532. The difference from continuous is minor but the method matters.

---

> **📌 Problem 4 — Delta-Neutral Hedge**
> **Given:** Trader writes 20 TCS Call options (lot size = 75). Delta of each call = 0.65.
> **Find:** Shares to buy to create delta-neutral position. If Δ changes to 0.75 after stock rises, how to rebalance?
> **Solution:**
> Initial: Total delta from short calls = −20 × 75 × 0.65 = −975
> Buy 975 TCS shares to neutralize. (**975 shares**)
>
> After rebalancing need:
> New delta from calls = −20 × 75 × 0.75 = −1,125
> Currently holding 975 shares (+975 delta)
> Shortfall = 1,125 − 975 = 150 shares
> **Buy 150 more TCS shares**
> **Answer: Initially buy 975 shares. After move, buy 150 more to rebalance.**

---

> **📌 Problem 5 — Bull Call Spread: Full Analysis**
> **Given:** HDFC Bank spot = ₹1,800. Buy 1,800 Call at ₹55. Sell 1,900 Call at ₹20. Lot = 100.
> **Find:** Max profit, max loss, breakeven. P&L at 1,750, 1,850, 1,950.
> **Solution:**
> Net Premium = 55 − 20 = ₹35/share = ₹3,500/lot
> Max Profit = (1,900−1,800) − 35 = ₹65/share = **₹6,500/lot**
> Max Loss = ₹35/share = **₹3,500/lot**
> Breakeven = 1,800 + 35 = **₹1,835**
>
> At 1,750: Both OTM → Net = −₹35 = **−₹3,500/lot (max loss)**
> At 1,850: Long call = 50, Short call = 0 → Net = 50−35 = **+₹15 = +₹1,500/lot**
> At 1,950: Long call = 150, Short call = −50 → Net = 150−50−35 = **+₹65 = +₹6,500/lot (max profit)**
> **Answer: Max Profit ₹6,500 | Max Loss ₹3,500 | Breakeven ₹1,835**

---

### 8.2 Top 10 Common Exam Mistakes

1. **Using BSM for American options** — BSM only values European options. Use Binomial for American options.
2. **Forgetting N(−d) = 1 − N(d)** — N(−0.15) = 1 − N(0.15) = 1 − 0.5596 = 0.4404. Students often look up the wrong side of the Z-table.
3. **Not adjusting S0 for dividends in BSM** — Always compute S0* = S0 − PV(D) before plugging into BSM.
4. **Wrong breakeven formula for spreads** — Bull Call: Lower strike + net premium. Bear Put: Higher strike − net premium.
5. **Forgetting volatility affects both calls AND puts in the SAME direction** — All other factors affect them in opposite directions. Volatility is the exception.
6. **Not checking early exercise in binomial** — For every intermediate node in an American option tree, compare Hold Value vs Intrinsic Value and take the MAX.
7. **Mixing up Gamma and Delta** — Delta = rate of change of PREMIUM. Gamma = rate of change of DELTA.
8. **Ignoring time decay in straddle** — A straddle requires a large, FAST move. Theta erodes value daily; holding too long makes it unprofitable.
9. **Sign errors in Put-Call Parity** — Always rewrite as: C = S + P − PV(X). Rearrange carefully; don't guess signs.
10. **Using lot size incorrectly in P&L** — P&L per unit × lot size = total P&L. Always multiply by lot size for final answer.

---

### 8.3 Formula Cheat Sheet

| Formula | Use Case |
| :--- | :--- |
| $C = S \cdot N(d_1) - Xe^{-rT} \cdot N(d_2)$ | BSM Call price |
| $P = Xe^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)$ | BSM Put price |
| $d_1 = [\ln(S/X) + (r+\sigma^2/2)T] / \sigma\sqrt{T}$ | BSM d1 |
| $d_2 = d_1 - \sigma\sqrt{T}$ | BSM d2 |
| $S_0^* = S_0 - De^{-rt_d}$ | Dividend-adjusted spot for BSM |
| $C + Xe^{-rT} = S + P$ | Put-Call Parity |
| $p = (e^{rt} - d)/(u - d)$ | Risk-neutral probability (Binomial) |
| $\Delta = (C_u - C_d)/(S_u - S_d)$ | Hedge ratio (Replicating Portfolio) |
| $C_0 = e^{-rt}[p \cdot C_u + (1-p) \cdot C_d]$ | Risk-Neutral Binomial pricing |
| $\text{Max Profit (Bull Call)} = X_2 - X_1 - \text{Net Premium}$ | Bull Call Spread |
| $\text{Breakeven (Bull Call)} = X_1 + \text{Net Premium}$ | Bull Call Spread BE |
| $\text{Breakeven (Bear Put)} = X_2 - \text{Net Premium}$ | Bear Put Spread BE |
| $\text{Straddle UBE} = X + C + P$ | Long Straddle upper BE |
| $\text{Straddle LBE} = X - (C + P)$ | Long Straddle lower BE |
| $N_{hedge} = -\Delta_{portfolio}/\Delta_{option}$ | Delta-neutral hedge shares |

---

### 8.4 Memory Tricks

**Greeks Signs — "DVTGR" (Delta Vega Theta Gamma Rho):**
- Delta: Direction (+ for call, − for put)
- Vega: Both positive (V for Victory — both win from vol)
- Theta: Both negative (Time Takes from both)
- Gamma: Both positive (Gamma Gives to both)
- Rho: Opposite (+ call, − put) — Rate is Reversed

**Put-Call Parity — "CAPS = SAPS":**
- C + PV(X) = S + P
- "Call And PV of Strike = Stock And Put"

**ITM/OTM Memory:**
- Call is ITM when S > X (Stock beats Strike → Call wins)
- Put is ITM when S < X (Stock below Strike → Put wins)
- Both can't be deep ITM at the same time for same strike

**Moneyness visual:**
```
OTM PUT | ITM PUT | ATM | ITM CALL | OTM CALL
←───────────────────X────────────────────→
        Low S              High S
```

**BSM Assumptions to Violate (INDIA mnemonic):**
- **I**nfinite liquidity assumed — NOT in India (illiquid stocks)
- **N**o dividends assumed — Indian stocks DO pay dividends
- **D**iscrete jumps exist — Indian markets have circuit breakers
- **I**nterest rates constant — RBI changes rates periodically
- **A**symmetric information — insider trading exists

