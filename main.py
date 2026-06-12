from dihook import Dihook

WEBHOOK = Dihook("https://discord.com/api/webhooks/1510197351690797147/n8kgLDQ8LMyirUT4rp7pknfBIny4fDR5d2h0yoOJYgD5gtcbIkPb2G_DbYNeUvQAAwqV")


print(WEBHOOK.send("Hello!", "Dihook"))