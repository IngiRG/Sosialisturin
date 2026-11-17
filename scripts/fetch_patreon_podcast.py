#!/usr/bin/env python3
"""Build public podcast listings from Patreon's public (never member-private) RSS."""
import datetime as dt
import email.utils
import html
import json
import os
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

FEED = "https://www.patreon.com/public-rss/16895688?show=2493005"
OUT = Path(__file__).resolve().parents[1] / "src/data/patreon-podcast.json"
NS = {"content": "http://purl.org/rss/1.0/modules/content/"}
def clean(value):
    value = re.sub(r"<[^>]*>", " ", value or "")
    return re.sub(r"\s+", " ", html.unescape(value)).strip()
def main():
    req = urllib.request.Request(FEED, headers={"User-Agent": "SosialisturinPodcastFeed/1.0", "Accept": "application/rss+xml, application/xml, text/xml"})
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            xml = response.read(8_000_000)
        root = ET.fromstring(xml)
        episodes = []
        for item in root.findall("./channel/item"):
            title = clean(item.findtext("title"))
            description = clean(item.findtext("description") or item.findtext("content:encoded", namespaces=NS))[:600]
            url = (item.findtext("link") or "").strip()
            enclosure = item.find("enclosure")
            audio = (enclosure.get("url") or "").strip() if enclosure is not None and (enclosure.get("type") or "").startswith("audio/") else ""
            # Only publicly provided audio is ever embedded.
            if not url.startswith("https://"):
                url = "https://www.patreon.com/sosialisturin"
            if audio and not audio.startswith("https://"):
                audio = ""
            published = item.findtext("pubDate") or ""
            try:
                date = email.utils.parsedate_to_datetime(published).astimezone(dt.timezone.utc).isoformat()
            except (TypeError, ValueError):
                date = "1970-01-01T00:00:00+00:00"
            # Public RSS previews are commonly labelled Preview / Trailer.
            preview = bool(re.search(r"\b(preview|trailer|teaser|hoyr byrjan|forsmak)\b", title + " " + description[:120], re.I))
            episodes.append(dict(title=title, description=description, url=url, audio=audio, date=date, preview=preview))
        if not episodes:
            raise ValueError("Public RSS returned no episodes")
        episodes.sort(key=lambda e: e["date"], reverse=True)
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(episodes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Updated {len(episodes)} public Patreon podcast entries")
    except Exception as exc:
        # Keep last successful snapshot and never break site deployments.
        print(f"WARNING: Patreon feed unavailable; keeping last snapshot: {exc}")
        if not OUT.exists():
            OUT.parent.mkdir(parents=True, exist_ok=True)
            OUT.write_text("[]\n", encoding="utf-8")
if __name__ == "__main__":
    main()
