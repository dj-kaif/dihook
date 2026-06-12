# Dihook

> A lightweight Python library for sending Discord webhook messages.

[![Version](https://img.shields.io/badge/version-v1.0.0--beta-blue)](https://github.com/dj-kaif/dihook/releases)
[![PyPI](https://img.shields.io/pypi/v/dihook)](https://pypi.org/project/dihook)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/dj-kaif/webhook.py?style=social)](https://github.com/dj-kaif/dihook)


**dihook** makes it simple to send Discord webhook messages from any Python script — without unnecessary boilerplate.

---

## Features

- Send Discord webhook messages
- Simple Python interface
- Lightweight and easy to use
- Minimal dependencies
- Built for scripts, bots, and automation

---

## Installation

### From PyPI

```bash
pip install dihook
```

### From GitHub (latest)

```bash
pip install git+https://github.com/dj-kaif/dihook.git
```

---

## Quick Start

```python
from dihook import Dihook

WEBHOOK = Dihook("YOUR_WEBHOOK_URL")

WEBHOOK.send("Hello from Dihook 🚀")
print(WEBHOOK.send("This will print a success message in your terminal."))
```

---

## Roadmap

### v1.2.0 *(planned)*

- [ ] Discord embed support
- [ ] More usage examples
- [ ] Better documentation
- [ ] Improved error handling
- [ ] Better developer experience

---

## Contributing

Contributions are welcome!

### How to contribute

1. Fork the repository
2. Clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/dihook.git
```

3. Create a new branch

```bash
git checkout -b feature-name
```

4. Make your changes
5. Test your changes
6. Open a pull request

### Guidelines

- Keep code clean and readable
- Follow existing project style
- Do not add unnecessary dependencies
- Do not break existing features
- Keep pull requests focused on one change

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact & Support

- 🐛 **Bugs & feature requests:** [Open an issue](https://github.com/dj-kaif/dihook/issues)
- 💬 **Discord:** [dj.kaif](https://discord.com/users/1237644967422459996)
- 📦 **PyPI:** [pypi.org/project/dihook](https://pypi.org/project/dihook)

If Dihook saves you time, consider ⭐ **[starring the repo](https://github.com/dj-kaif/dihook)** — it really helps!
