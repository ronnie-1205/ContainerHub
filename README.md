# 🧭 Container Dashboard

A minimal, dark-themed **Streamlit dashboard** for easily accessing services running on your local Docker containers — no more remembering random ports. Designed to be accessed securely using **Tailscale**, with auto-refreshing links and a simple login screen.

> 💡 **Note:** You don't need to use Tailscale for this to work. The dashboard simply uses the URLs from your `links.json` file. You can use `localhost`, your LAN IP, a domain name, or a reverse proxy like NGINX — anything that lets your device reach the services.

---

## 📦 Features

- ✅ Clean Streamlit interface in **dark mode**
- ✅ Display container service links as clickable buttons
- ✅ JSON-driven, hot-reloadable link list
- ✅ Login screen with hardcoded credentials
- ✅ Responsive layout (mobile friendly)
- ✅ Access from anywhere via **Tailscale**
- ✅ Fully containerized with `docker-compose`

---

## 📁 Project Structure

```
dashboard/
├── data/
│   └── links.json         # Store your link buttons here (editable JSON)
├── app.py                 # Streamlit app
├── requirements.txt       # Python dependencies
└── docker-compose.yml     # Docker config (no Dockerfile needed)
```

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/container-dashboard.git
cd container-dashboard
```

### 2. Edit `data/links.json`

Example:

```json
{
  "Grafana": "http://localhost:3000",
  "Portainer": "http://localhost:9000",
  "Ollama API": "http://localhost:11434"
}
```

### 3. Start the dashboard

```bash
docker-compose up -d
```

This runs the dashboard at:

```
http://localhost:8501
```

> ✅ Make sure port `8501` is open if accessing remotely or via Tailscale.

---

## 🌐 Access Remotely with Tailscale

This dashboard is designed to be accessed from other devices via [Tailscale](https://tailscale.com/).

### Option 1: Basic Access (Tailscale IP)

On your mobile or another device in the tailnet:

```
http://100.x.x.x:8501
```

### Option 2: Friendly `.ts.net` Hostname (with MagicDNS)

Ensure:
- MagicDNS is enabled in your Tailscale admin panel
- DNS override is enabled in your mobile's Tailscale app

Then access:

```
http://your-hostname.ts.net:8501
```

### Option 3: Clean HTTPS with `tailscale serve`

Run this on the host:

```bash
tailscale serve --https /dashboard=http://localhost:8501
```

Now access via:

```
https://your-hostname.ts.net/dashboard
```

No ports, no DNS hassle, and fully HTTPS.

---

## 🔐 Login Credentials

Hardcoded in `app.py` (you can change these):

```python
USERNAME = "admin"
PASSWORD = "password"
```

---

## 🛠 Requirements (if running locally)

If you prefer not to use Docker:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📄 License

MIT — free to use and modify.

---

## ✨ Credits

Made with ❤️ using [Streamlit](https://streamlit.io), [Docker](https://docker.com), and [Tailscale](https://tailscale.com).
