# Matrix Rain - Deployment Guide

## Files in Root Directory

These files must be in the root for deployment:
- index.html
- pyscript.toml
- CNAME
- src/matrix_rain/matrix.py (referenced by pyscript.toml)

## GitHub Pages Deployment

### Step 1: Prepare Repository

```bash
# Make sure CNAME file is in root
echo "rain.kahdev.me" > CNAME

# Commit everything
git add .
git commit -m "Add matrix rain visualizer"
git push origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repo: https://github.com/khesse-757/matrix-rain
2. Click Settings
3. Scroll to Pages (left sidebar)
4. Under "Source":
   - Select "Deploy from a branch"
   - Branch: main
   - Folder: / (root)
5. Click Save

GitHub will build and deploy. Wait a few minutes.

### Step 3: Configure DNS in Cloudflare

1. Log into Cloudflare
2. Select your domain: kahdev.me
3. Go to DNS > Records
4. Add a CNAME record:
   - Type: CNAME
   - Name: rain
   - Target: khesse-757.github.io
   - Proxy status: Proxied (orange cloud)
   - TTL: Auto
5. Save

### Step 4: Verify

Wait 5-10 minutes for DNS to propagate, then visit:
https://rain.kahdev.me

## Local Testing

### Python HTTP Server

```bash
# From project root
python3 -m http.server 8000

# Open browser to http://localhost:8000
```

### Docker

```bash
# Build and run the container
docker compose up

# Or run in background
docker compose up -d

# View logs
docker compose logs -f

# Stop the container
docker compose down
```

Then open http://localhost:8000

The Docker setup:
- Installs all Python dependencies from pyproject.toml
- Creates isolated environment
- Serves the PyScript app on port 8000
- Auto-reloads when you edit files (via volume mounts)

## Troubleshooting

**GitHub Pages shows 404:**
- Check that index.html is in root
- Check that GitHub Pages is enabled
- Wait 5 minutes and try again

**Custom domain not working:**
- Verify CNAME file exists in root
- Check Cloudflare DNS has CNAME record
- Wait 10 minutes for DNS propagation
- Check SSL certificate is active

**PyScript not loading:**
- Open browser console (F12)
- Check for errors
- Verify pyscript.toml path is correct
- Verify matrix.py exists at src/matrix_rain/matrix.py

**Matrix effect not showing:**
- Check browser console for JavaScript errors
- Try different browser
- Clear cache and reload

**Docker not working:**
- Make sure Docker is running
- Check port 8000 isn't already in use
- Try: `docker compose down` then `docker compose up --build`