#!/usr/bin/env python3
"""PS-SHA∞ — Persistent Sovereign Hash-chain (Amundson Framework)"""
import hashlib, json, time

class PSSHAInfiniteJournal:
    def __init__(self):
        self.chain = []
        self.head_hash = "0" * 64  # genesis

    def append(self, action, entity, details, agent="system"):
        entry = {
            "index": len(self.chain),
            "timestamp": time.time(),
            "agent": agent,
            "action": action,
            "entity": entity,
            "details": details,
            "prev_hash": self.head_hash,
        }
        entry["hash"] = hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest()
        self.chain.append(entry)
        self.head_hash = entry["hash"]
        return entry

    def verify_head(self):
        if not self.chain: return True
        last = self.chain[-1]
        expected = hashlib.sha256(json.dumps({k:v for k,v in last.items() if k != "hash"}, sort_keys=True).encode()).hexdigest()
        return expected == last["hash"]

    def verify_full_chain(self):
        for i, entry in enumerate(self.chain):
            if i > 0 and entry["prev_hash"] != self.chain[i-1]["hash"]:
                return False, f"Broken link at index {i}"
            check = {k:v for k,v in entry.items() if k != "hash"}
            if hashlib.sha256(json.dumps(check, sort_keys=True).encode()).hexdigest() != entry["hash"]:
                return False, f"Invalid hash at index {i}"
        return True, "Chain valid"

    def __len__(self): return len(self.chain)

class TrinaryEngine:
    """Trinary logic with Creative Energy Formula K(t) = C(t) * e^(λ*contradiction)"""
    import math
    
    def evaluate_trinary(self, value, threshold=0.5):
        """Returns +1 (true), 0 (undetermined), -1 (false)"""
        if value > threshold: return 1
        if value < -threshold: return -1
        return 0
    
    def creative_energy(self, C_t, lambda_val, contradiction):
        """K(t) = C(t) * e^(λ * |contradiction|)"""
        import math
        return C_t * math.exp(lambda_val * abs(contradiction))
    
    def z_equilibrium(self, y, x, w):
        """Z := yx - w. |Z| → 0 is equilibrium."""
        return y * x - w

if __name__ == "__main__":
    j = PSSHAInfiniteJournal()
    j.append("init", "test", "PS-SHA∞ test")
    j.append("compute", "G(5)", "2.0093878601")
    j.append("verify", "chain", "integrity check")
    print(f"Chain length: {len(j)}")
    print(f"Head valid: {j.verify_head()}")
    valid, msg = j.verify_full_chain()
    print(f"Full chain: {msg}")
    
    t = TrinaryEngine()
    print(f"Trinary(0.8): {t.evaluate_trinary(0.8)}")
    print(f"Trinary(0.0): {t.evaluate_trinary(0.0)}")
    print(f"Trinary(-0.9): {t.evaluate_trinary(-0.9)}")
    print(f"K(t) at C=1,λ=0.5,contradiction=2: {t.creative_energy(1, 0.5, 2):.4f}")
    print(f"Z(3,4,12) = {t.z_equilibrium(3,4,12)} (equilibrium)")
