from dihook import send

WEBHOOK_URL = "https://discord.com/api/webhooks/1510197351690797147/n8kgLDQ8LMyirUT4rp7pknfBIny4fDR5d2h0yoOJYgD5gtcbIkPb2G_DbYNeUvQAAwqV"


print(send(WEBHOOK_URL, "Hello from Webhook!"))