"""Senegal: the shared curl cache from scripts/africa-law/peachjam.py, with Senegal's host delays.

Every request goes through peachjam.Cache (sha256-named files in .cache/, every request logged to
.cache/requests.jsonl, archive.org spacing shared by every process on this machine). Government hosts are read at
1 request per second (africa-law/FANOUT.md); archive.org at 1 per 3 s.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "africa-law"))
import peachjam  # noqa: E402  (read-only shared adapter)

for host in ("conseilconstitutionnel.sn", "www.conseilconstitutionnel.sn", "www.cdp.sn", "cdp.sn",
             "www.jo.gouv.sn", "jo.gouv.sn", "www.sec.gouv.sn", "sec.gouv.sn", "www.justice.gouv.sn",
             "www.assemblee-nationale.sn", "www.presidence.sn", "www.sgg.gouv.sn", "www.primature.sn"):
    peachjam.CRAWL_DELAY.setdefault(host, 1.0)

WAYBACK = peachjam.WAYBACK


def cache(offline: bool = False) -> peachjam.Cache:
    return peachjam.Cache(HERE, offline=offline)


def raw(ts: str, orig: str) -> str:
    """The Wayback raw (`id_`) form of a capture."""
    return f"{WAYBACK}/web/{ts}id_/{orig}"


def get(url: str, offline: bool = False) -> bytes:
    return cache(offline).get(url)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for u in sys.argv[1:]:
        b = get(u)
        print(u, len(b), cache().path(u))
