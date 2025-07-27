# ✅ Enforce HTTPS across the site
SECURE_SSL_REDIRECT = True  # 🚀 Automatically redirects all HTTP -> HTTPS

# ✅ HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# ✅ Secure Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ✅ Secure Headers
X_FRAME_OPTIONS = "DENY"  # 🛡️ Protect against clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # 🚫 No MIME sniffing
SECURE_BROWSER_XSS_FILTER = True  # 🧼 XSS protection (some browsers)

# ✅ Production only (update this!)
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Optionally, if you’re not running `DEBUG = False` yet, flip it:
DEBUG = False
