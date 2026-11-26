# How this repository was made (Senegal)

Build of 2026-11-26: 10027 texts, 64915 provision files, in force 1981 to 2018. Layout: see [STRUCTURE.md](STRUCTURE.md).

## Sources

| Source | Address | Use |
| --- | --- | --- |
| Journal officiel de la République du Sénégal, web edition (jo.gouv.sn), via the Internet Archive | <http://www.jo.gouv.sn/spip.php?articleN> | The Constitution of 2001; the texts the site published, 2001 to 2018, as published (HTML) |
| Vie Publique Sénégal | <https://www.vie-publique.sn/documents> | Laws, ordinances and decrees whose PDF is born-digital; the Code des douanes (Loi n° 2014-10) |
| Conseil constitutionnel | <https://conseilconstitutionnel.sn/la-loi-organique/> | Loi organique n° 2016-23 (first build) |

jo.gouv.sn has not answered since about 2019 (connection times out; checked again 2026-11-26), so its pages are read
from Internet Archive captures (one capture per page, via the shared archive.org client, one request in flight for
the machine). vie-publique.sn was read at up to 5 requests in flight; its robots.txt allows the document pages.

## How each text is dated

- Journal officiel texts: Loi n° 70-14 du 6 février 1970, art. 2: in force on the 3rd day after the Journal officiel
  that prints the text, extended by each Sunday in that window (the issue date stands for the deposit date; public
  holidays are not modelled). Texts the JO prints "selon la procédure d'urgence" are dated on the issue day. From
  20 March 2021, Loi n° 2021-21 art. 10 (one clear day after publication).
- The Constitution of 2001: the day of its promulgation, 22 January 2001 (its art. 108).
- Codes from the JO site's "Code" heading and vie-publique.sn texts: those sources give no Journal officiel issue, so
  the commit is dated on the day of the law or decree, and `In-force-basis` says so.

## What was left out

- No OCR. Pages and PDFs whose text is an image (scans, or scans with a machine-read text layer) are held and listed.
- Notices (annonces, récépissés, land-registry notices, election results, staff movements) are not legal texts.
- Exposés des motifs, rapports de présentation, visas, headings, signatures and the executory formula.
- Decisions of the Conseil constitutionnel (case law) go to the separate repository senegal-caselaw.
- The Constitution is held as enacted in 2001; its revisions are held as enacted in `lois/` (2003 to 2016), not yet
  applied to the articles. The Conseil constitutionnel's consolidated text interleaves editorial notes and quotation
  marks with the text, with no clean copy to check a de-annotation against.
- The Cour suprême's site (coursupreme.sn) refuses automated requests (HTTP 403); it was not read.

Held from the Journal officiel archive (by reason):
- 132: notice or unclassified
- 85: no Journal officiel date
- 73: decision
- 17: code text
- 17: empty
- 10: continuation/annex page
- 1: text partly or wholly in images

Held from vie-publique.sn (by reason):
- 1645: scanned
- 368: no number in title
- 1: odd number 1933-68
- 1: odd number 2030-80
- 1: no articles found
- 1: odd number 1949-94
- 1: odd number 001-2023

Codes held:
- spip article38: heading reads 'LOI 96-03 du 26 février 1996 portant Code de l'environnement' but the L-numbered text (L1-L110) is that of Loi n° 2001-01 du 15 janvier 2001; reference unsettled
- spip article2557: no law reference in heading: ['REPUBLIQUE DU SENEGAL']
- spip article7747: no law reference in heading: ['LOI N° 98-05 DU 08 janvier 1998 portant sur le Code pétrolier.']

## Decisions made by hand

- jo.gouv.sn's "Code" page for the Code de l'environnement is headed "LOI 96-03 du 26 février 1996" while its
  L-numbered text (L1 to L110) is that of Loi n° 2001-01 du 15 janvier 2001: held until settled.
- The "Code forestier" page is headed "LOI n° 98-164" but holds R.-numbered articles, the regulatory part: recorded
  as Décret n° 98-164.
- Where the web edition lost an article number ("Art. - …"), the article takes the next number; up to two missing
  numbers are allowed between articles; a repeated or out-of-sequence number is kept as text of the current article
  (quoted amendments).
- The JO site's "Le Code minier" page holds Décret n° 2004-647 du 17 mai 2004 (application decree of the Code minier,
  Loi n° 2003-36), not the Code itself: built first under `codes/code-minier/`, moved to
  `decrets/2004/decret-2004-647/` by the documentation commit.
- The JO site's Code de la sécurité sociale page is headed "LOI N° 73-37 du 31 Juillet 1993"; the law is of
  31 July 1973. Its commit is dated 1993-07-31 as the page reads; the true date is 1973-07-31.
- Codes held: Code des marchés publics page (no law reference in its heading), Code pétrolier (Loi n° 98-05; heading
  not parsed), Code de l'environnement (see above).
- When two JO pages carry the same text number, the second is kept with the suffix `-jo<page id>`.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code under Lexifina's direction.
No model wrote, translated or corrected legal text; parsing is rule-based.
