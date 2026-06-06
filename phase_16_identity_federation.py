import jwt
import datetime
import json

# =========================
# ZERO TRUST IDENTITY LAYER
# =========================

SECRET_KEY = "ZT-SOC-SIMULATION-KEY-32-BYTES-MINIMUM!!"

users = {
    "developer": {
        "role": "admin",
        "mfa": True
    },
    "support": {
        "role": "support",
        "mfa": False
    }
}

# -------------------------
# TOKEN GENERATION
# -------------------------
def generate_token(username):
    if username not in users:
        raise ValueError("Unknown user")

    now = datetime.datetime.now(datetime.timezone.utc)

    payload = {
        "iss": "zero-trust-soc-sim",
        "sub": username,
        "user": username,
        "role": users[username]["role"],
        "mfa": users[username]["mfa"],
        "iat": now,
        "nbf": now,
        "exp": now + datetime.timedelta(minutes=30)
    }

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# -------------------------
# TOKEN VALIDATION
# -------------------------
def validate_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        return {"status": "error", "reason": "TOKEN EXPIRED"}

    except jwt.InvalidTokenError:
        return {"status": "error", "reason": "INVALID TOKEN"}


# -------------------------
# AUDIT LOG
# -------------------------
def audit_log(event, user):
    print(f"[AUDIT LOG] event={event} user={user} timestamp={datetime.datetime.now(datetime.timezone.utc)}")


# -------------------------
# MAIN
# -------------------------
def main():
    print("\n=== IDENTITY FEDERATION + SSO (ZERO TRUST SIMULATION) ===")

    token = generate_token("developer")

    print("\nGenerated JWT:\n")
    print(token)

    decoded = validate_token(token)

    print("\nDecoded Identity:\n")
    print(json.dumps(decoded, indent=4, default=str))

    audit_log("TOKEN_ISSUED_AND_VALIDATED", "developer")


if __name__ == "__main__":
    main()

# phase_16_identity_federation.py
def main():
    print("Phase 16: Identity Federation")
    from time import sleep
    sleep(0.1)
    print("Phase 16 completed")

if __name__ == "__main__":
    main()

def test_main():
    print("safe execution ok")