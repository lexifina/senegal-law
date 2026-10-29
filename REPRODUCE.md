# How this repository was made (Senegal)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Journal officiel de la République du Sénégal (jo.gouv.sn), via the Internet Archive | <http://www.jo.gouv.sn/spip.php?article6663> | 2026-10-28 | Official legislation; the site read "© Copyrights Gouvernement du Sénégal" and states no licence |
| Conseil constitutionnel du Sénégal | <https://conseilconstitutionnel.sn/la-loi-organique/> | 2026-10-28 | Official legislation; the site reads "© Copyright 2026. tous droits réservés" |
| Commission de Protection des Données Personnelles (cdp.sn), via the Internet Archive | <http://www.cdp.sn/sites/default/files/protection.pdf> | 2026-10-29 | Official authority; no licence stated |
| Vie Publique Sénégal (www.vie-publique.sn) | <https://www.vie-publique.sn> | 2026-10-29 | Civic publisher; Content-Signal use=reference |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `donnees-personnelles` | Loi n° 2008-12 du 25 janvier 2008 portant sur la Protection des données à caractère personnel | 1 | 2008-05-07 to 2008-05-07 |
| `conseil-constitutionnel` | Loi organique n° 2016-23 du 14 juillet 2016 relative au Conseil constitutionnel | 1 | 2016-07-19 to 2016-07-19 |

The build made 2 commits:

| Commits | Kind |
| ---: | --- |
| 2 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futur`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (Africa/Dakar) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Loi n° 70-14 du 6 février 1970, art. 2: laws become executory in the Cap-Vert region (Dakar) on the 3rd day after the Journal officiel that prints them is deposited with the Secrétariat général de la Présidence, extended by any Sunday or public holiday before that day. Replaced for laws published from 20 March 2021 by Loi n° 2021-21 du 2 mars 2021, art. 10: in force « un jour franc à compter de leur publication au Journal officiel ». https://www.vie-publique.sn/docs/03ff08a9-aad5-46ed-b92c-db9e89e5ef53/loi-n-70-014-du-06-fevrier-1970.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `7de9fabf2f0fa707e085f2658e51fca769afcd7c0552338e833143bd7ff600c2` (89482 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

2 versions of 2 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Phase 1 is Loi 2008-12 (data protection) and Loi organique 2016-23 (Conseil constitutionnel): the two core texts with a complete official text layer. The Code pénal (Loi 65-60) is only available as image scans (cdp.sn code_penal.pdf, vie-publique), so it is left out (no OCR).
- The Constitution of 2001 is not built yet. Its only consolidation (Conseil constitutionnel, la-constitution, à jour of Loi constitutionnelle 2018-14) interleaves about 100 editorial notes and « » change markers inside the paragraphs of the text, with no clean copy to check a de-annotation against; LC 2019-10 (JO 7181) and LC 2021-41 (JO 7483) have been collected. Vie-publique.sn also lists a "Loi n° 11/2024 portant révision de la Constitution" (14 décembre 2024) published only as a 2-page image scan, whose status could not be settled.
- Loi 2008-12 is taken from the Journal officiel web edition (JO n° 6406 du samedi 3 mai 2008, spip.php?article6663), the official publication. Its text was compared article by article with the CDP's PDF (protection.pdf, the same file vie-publique serves): 13 articles differ: art. 2: JO "oeuvre" / CDP "œuvre"; JO "oeuvre" / CDP "œuvre" | art. 3: JO "oeuvre" / CDP "œuvre" | art. 4: JO "sous-traitant," / CDP "sous- traitant," | art. 7: JO "vice-président" / CDP "vice- président"; JO "oeuvre" / CDP "œuvre" | art. 22: JO "oeuvre" / CDP "œuvre" | art. 25: JO "oeuvre" / CDP "œuvre" | art. 39: JO "oeuvre" / CDP "œuvre" | art. 42: JO "oeuvre" / CDP "œuvre" | art. 45: JO "oeuvre" / CDP "œuvre" | art. 52: JO "sous-traitant," / CDP "sous- traitant," | art. 53: JO "œuvre" / CDP "oeuvre" | art. 60: JO "oeuvre" / CDP "œuvre" | art. 78: JO "Les modalités d'application de la présente loi seront prises par décret." / CDP "". The JO wording is kept (the CDP PDF lacks the last sentence of art. 78 and splits two words at line ends), except two transcription slips of the web edition, corrected from the CDP copy: art. 16: ") elle reçoit les formalités" read as "a) elle reçoit les formalités"; art. 57: "taritements" read as "traitements".
- Loi organique 2016-23 is taken from the Conseil constitutionnel's own page, which gives the law as promulgated (JORS NS 6946 du 15 juillet 2016, pp. 927-930) with no later amendment noted.
- In-force dates follow Loi n° 70-14 art. 2 (both acts were published before Loi 2021-21 took over): the 3rd day after the JO's deposit at the Secrétariat général de la Présidence, plus one day for each Sunday before it. The deposit receipts for JO 6406 and JORS 6946 were not found, so the deposit is taken to be the issue date: Loi 2008-12 (JO 3 May 2008, a Saturday) is dated 2008-05-07; LO 2016-23 (JORS 15 July 2016, a Friday) is dated 2016-07-19. Public holidays are not modelled; none fell in those windows that we know of. Loi 70-14 was amended by Loi 71-07 (21 January 1971), which was not available to check.
- Loi 70-14 is read from the text layer the publisher (Direction des relations avec les institutions, via vie-publique.sn) put on its scan; it is cited only for the rule and no legal text in the record comes from it.
- The exposé des motifs, chapter and section headings, the enacting formula, the executory formula ("sera exécutée comme loi de l'État") and the signatures are left out; each article is one file, one paragraph or list item per line.
- Today's text: no amending law to either act was found. The CDP's law page (captured 2025-01-24) and vie-publique.sn (retrieved 2026-10-29) still give Loi 2008-12 as the data protection law; the Conseil constitutionnel still publishes Loi organique 2016-23 unamended (retrieved 2026-10-28). A 2026 constitutional revision (loi n° 18/2026) that would have replaced the Conseil by a Cour constitutionnelle was declared unconstitutional (décision n° 6/C/2026 du 9 juillet 2026) and never took effect.
- Only Internet Archive copies are used.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: no model wrote or transcribed legal text; parsing is rule-based.
