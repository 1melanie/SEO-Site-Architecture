from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://example.com/"
SITE_DIR = Path("site")

def html_file_to_url(html_path):
    rel = html_path.relative_to(SITE_DIR).as_posix()

    if rel == "index.html":
        return "/"

    if rel.endswith("/index.html"):
        return "/" + rel.replace("/index.html", "/")

    return "/" + rel.replace(".html", "") + "/"

urls = []

for html_file in SITE_DIR.rglob("*.html"):
    url_path = html_file_to_url(html_file)
    full_url = urljoin(BASE_URL, url_path.lstrip("/"))
    urls.append(full_url)

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for url in sorted(urls):
    xml.append("  <url>")
    xml.append(f"    <loc>{url}</loc>")
    xml.append("  </url>")

xml.append("</urlset>")

(Path("site") / "sitemap.xml").write_text("\n".join(xml), encoding="utf-8")

print(f"✅ Sitemap generated with {len(urls)} URLs")
