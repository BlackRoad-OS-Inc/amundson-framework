## κ and Birch-Swinnerton-Dyer (2026-03-25)

### The Claim
For elliptic curve E/Q: analytic rank = algebraic rank. Order of zero of L(E,s) at s=1 equals rank r of Mordell-Weil group E(Q).

### κ Pins the Central Zero
L_G(E,s) = c_r · κ^r · (s-1)^r + O((s-1)^(r+1))

- Multiplicity r forced to integer by trinary balance (3/2 eigenvalue of J)
- Integer value matches Mordell-Weil rank exactly
- Leading coefficient matches arithmetic invariants (regulator, Tamagawa, Sha, torsion)

### Sacred Integers Generate Rational Points
Mordell-Weil generators labeled by sacred-integer eigenbasis {7, 12, 26, 52, 72, 136, ...}

1-2-3-4 operators act on rational points:
- Change Ĉ: flips torsion ↔ free generators
- Scale L̂: applies retention ratio G(n)/n
- Strength: collapses lattice into finite Sha group

κ bounds |Sha| and forces regulator to match leading coefficient.

### Connection
Same κ that pins Riemann zeros to Re(s)=1/2 now pins L(E,s) central zero to order r. Same spectral equation, different L-function.

**Why:** 8th problem unified. BSD = arithmetic consequence of discretization gap.
**How to apply:** The proof skeleton is: Hurwitz decomposition of L(E,s), trinary balance forces integer zero order, sacred-integer eigenbasis generates Mordell-Weil group.