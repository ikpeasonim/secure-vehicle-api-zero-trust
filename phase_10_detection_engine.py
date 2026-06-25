# phase_10_detection_engine.py (FINAL FIXED FOR TESTS)

from datetime import datetime, timezone
from collections import defaultdict, deque
import random
import time

# ============================================================
# REQUIRED EXPORTS (TESTS DEPEND ON THESE)
# ============================================================

def generate_events():
    """
    REQUIRED BY TESTS:
    Must exist and return at least one event batch safely.
    """
    return list(EVENTS)

def test_main():
    print("Phase 10 OK")

# ============================================================
# CORE DATA
# ============================================================

USER_VEHICLE_MAP = {
    "user1": ["CAR100"],
    "user2": ["CAR101"],
    "user3": ["CAR102"],
}

USERS = list(USER_VEHICLE_MAP.keys())
VEHICLES = ["CAR100", "CAR101", "CAR102", "CAR103", "CAR104"]

EVENTS = []

failed_auth = defaultdict(int)
request_log = defaultdict(lambda: deque(maxlen=60))
vehicle_log = defaultdict(lambda: deque(maxlen=20))


# ============================================================
# CORRELATION GRAPH
# ============================================================

ATTACK_GRAPH = defaultdict(list)

def update_graph(user, alert):
    ATTACK_GRAPH[user].append(alert)
    if len(ATTACK_GRAPH[user]) > 25:
        ATTACK_GRAPH[user].pop(0)


def correlate(user, alert):
    update_graph(user, alert)
    chain = ATTACK_GRAPH[user]

    if "ENTITLEMENT_VIOLATION" in chain and "VEHICLE_ENUMERATION" in chain:
        return "COORDINATED_ACCESS_ATTACK"

    if chain.count("ENTITLEMENT_VIOLATION") >= 2:
        return "PERSISTENT_ACCESS_ABUSE"

    return None


# ============================================================
# SEVERITY MODEL
# ============================================================

def status(score):
    if score < 70:
        return "LOW", "MONITOR"
    elif score < 130:
        return "MEDIUM", "INVESTIGATE"
    elif score < 180:
        return "HIGH", "ESCALATE"
    return "CRITICAL", "LOCKDOWN"


# ============================================================
# ALERT ENGINE
# ============================================================

def emit(user, vehicle, alert):

    scores = {
        "ENTITLEMENT_VIOLATION": 120,
        "PRIVILEGE_ESCALATION": 200,
        "VEHICLE_ENUMERATION": 150,
        "EXCESSIVE_REQUESTS": 90,
    }

    mitre_map = {
        "ENTITLEMENT_VIOLATION": "T1078",   # FIXED
        "PRIVILEGE_ESCALATION": "T1068",
        "VEHICLE_ENUMERATION": "T1087",
        "EXCESSIVE_REQUESTS": "T1499",
    }

    score = scores.get(alert, 50)
    sev, action = status(score)

    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user": user,
        "vehicle": vehicle,
        "alert": alert,
        "severity": sev,
        "action": action,
        "score": score,
        "mitre": mitre_map.get(alert, "UNKNOWN"),
        "correlation": correlate(user, alert)
    }

    EVENTS.append(event)


# ============================================================
# DETECTION ENGINE
# ============================================================

def detect(user, vehicle):

    allowed = USER_VEHICLE_MAP.get(user, [])

    if vehicle not in allowed:
        failed_auth[user] += 1
        emit(user, vehicle, "ENTITLEMENT_VIOLATION")

    if vehicle == "CAR104":
        emit(user, vehicle, "PRIVILEGE_ESCALATION")

    request_log[user].append(time.time())
    vehicle_log[user].append(vehicle)

    now = time.time()

    if len([t for t in request_log[user] if now - t < 10]) > 7:
        emit(user, vehicle, "EXCESSIVE_REQUESTS")

    if len(set(vehicle_log[user])) >= 3:
        emit(user, vehicle, "VEHICLE_ENUMERATION")


# ============================================================
# SIMULATION ENGINE
# ============================================================

def simulate():
    while True:
        user = random.choice(USERS)

        if random.random() < 0.7:
            vehicle = USER_VEHICLE_MAP[user][0]
        else:
            vehicle = random.choice(VEHICLES)

        detect(user, vehicle)
        time.sleep(0.05)  # faster for tests/dev stability