# Create this middleware file: LibraryProject/middleware/secure_headers.py

def secure_headers_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['Referrer-Policy'] = 'no-referrer-when-downgrade'
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
        return response
    return middleware
