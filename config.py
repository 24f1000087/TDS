# ==========================================
# MASTER CONFIGURATION CHEAT SHEET
# Filled in with your assigned values from the Exam Portal
# ==========================================

# 1. Your IITM Email
EMAIL = "24f1000087@ds.study.iitm.ac.in"

# 2. Q1: CORS Allowed Origin
Q1_ALLOWED_ORIGIN = "https://dash-xl9rpc.example.com"

# 3. Q2: OAuth JWKS (Issuer, Audience, and Public Key)
ISSUER = "https://idp.exam.local"
AUDIENCE = "tds-ab19wtp5.apps.exam.local"
PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2okOHspNjgA+2rTLbeuY
cxiP/hG8C6Sb9iwg3yiLAA4HCnpITcbWCSelbvbYGuc3EbNy4xFyf5Cbj5DHJMID
EkryOgyd2giIIIBOUBj8S63uGcnRpOBh9NFatfNwheKuzsPuVNldu6A9cNteNpXc
WyJjG2axVfmq7i6SuKr1JoWYG7xTTAvKPujSl4OtsQfO3h5NepzdfXpr28oNnzfW
ed+zclR6BcmNNo/WVfJ4xyCLSf0BCOgdTgW6PdaChd1l9VDetJZVEgC5tkyvXsfI
SI6iyrYbKR0NEBSqq4XkadEjsCs4F1RncsS4LlgniT7GlkL9Mce3b0wGLs9/7ZIX
dQIDAQAB
-----END PUBLIC KEY-----"""

# 4. Q3: 12-Factor Config — the four layers, lowest to highest precedence.
# These feed a real merge function in main.py (not hardcoded final values),
# so it still works correctly no matter what the grader overrides via ?set=.
Q3_DEFAULTS = {
    "port": 8000,
    "workers": 1,
    "debug": False,
    "log_level": "info",
    "api_key": "default-secret-000",
}
Q3_YAML_LAYER = {  # simulates config.development.yaml
    "workers": 2,
    "log_level": "error",
    "api_key": "key-zhb541skc0",
}
Q3_DOTENV_LAYER = {  # simulates .env file (raw string values, pre-normalization)
    "NUM_WORKERS": "7",
    "APP_DEBUG": "true",
    "APP_API_KEY": "key-dp3oeh26p7",
}
Q3_OS_ENV_FALLBACK = {  # simulates OS-level env vars (APP_* prefix)
    "APP_PORT": "8352",
    "APP_WORKERS": "10",
    "APP_DEBUG": "false",
    "APP_LOG_LEVEL": "warning",
}

# 5. Q5: Analytics API key
Q5_API_KEY = "ak_57funeff2rapi8rd8qdvmx4q"

# 6. Q9: Idempotency & Rate Limit
Q9_TOTAL_ORDERS = 57
Q9_RATE_LIMIT = 20

# 7. Q10: Middleware Rate Limit
Q10_ALLOWED_ORIGIN = "https://app-omrefp.example.com"
Q10_RATE_LIMIT = 12

# ==========================================
# FIXED VARIABLES (Do not change these)
# ==========================================
EXAM_PORTAL_ORIGIN = "https://exam.sanand.workers.dev"
