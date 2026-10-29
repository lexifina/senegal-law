# Senegal: law history in git

The law of Senegal as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph, `git log` lists every change to an article, and `tools/en_vigueur_au.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `sn/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `donnees-personnelles/` | Loi n° 2008-12 du 25 janvier 2008 portant sur la Protection des données à caractère personnel | 1 | As published in the Journal officiel n° 6406 of 3 May 2008, in force 7 May 2008; no amending law found |
| `conseil-constitutionnel/` | Loi organique n° 2016-23 du 14 juillet 2016 relative au Conseil constitutionnel | 1 | As published in the JORS numéro spécial 6946 of 15 July 2016, in force 19 July 2016; no amending law found |

The per-act `README.md` in each folder lists every provision, how often it changed and when.

**Why these two acts, and why one version each.** The Journal officiel website (jo.gouv.sn) has been offline since about 2019, and no official site publishes dated versions of Senegalese law. The two acts here have a complete official text with a machine-readable text layer, and neither has been amended, so one version each is the whole history. Loi 2008-12 is read from the Internet Archive's copy of the Journal officiel's own web edition. Loi organique 2016-23 is read from the Conseil constitutionnel's site.

**Not included yet**

- **The Constitution of 2001.** Its only consolidation, the Conseil constitutionnel's (current to Loi constitutionnelle 2018-14), mixes about 100 editorial notes and « » change markers into the paragraphs of the text. No clean copy exists to check a de-annotated text against. The later revisions (LC 2019-10, LC 2021-41) are in hand. A "Loi n° 11/2024 portant révision de la Constitution" listed by vie-publique.sn is published only as an image scan, and its status is not settled.
- **The Code pénal (Loi 65-60).** It is available only as image scans, and this record does not transcribe images (no OCR).

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 33 of the data protection law say on 1 January 2020? | `python tools/en_vigueur_au.py 2020-01-01 donnees-personnelles 33` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2020-01-01T23:59:59Z" main -- donnees-personnelles/art-033.md):donnees-personnelles/art-033.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2020-01-01T23:59:59Z" main -- donnees-personnelles/art-033.md; git show "$($r):donnees-personnelles/art-033.md"` |
| Which law wrote each paragraph of an article? | `git blame conseil-constitutionnel/art-004.md` |
| Every change to an article, word by word | `git log -p --word-diff donnees-personnelles/art-016.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one law changed | `git show law/loi-2008-12` (tags `law/<key>` mark each law's commit) |
| A whole act on a date | `python tools/en_vigueur_au.py 2017-01-01 conseil-constitutionnel` |
| Which law gave a provision its wording on a date | `python tools/en_vigueur_au.py --law 2021-01-01 conseil-constitutionnel 22` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Africa/Dakar (UTC), on the day the change took effect**. The day is also in the `In-force:` trailer, which the tools read. The promulgation date is the `Enacted:` trailer and the Journal officiel date is the `Published:` trailer.
- **The rule for these two acts is Loi n° 70-14 du 6 février 1970, art. 2.** A law becomes executory in the Cap-Vert region (Dakar) on the 3rd day after the Journal officiel that prints it is deposited with the Secrétariat général de la Présidence. Each Sunday or public holiday before that day adds a day. The deposit receipts for these two issues were not found, so the deposit is taken as the issue's own date:
  - Loi 2008-12 appeared in JO n° 6406 of Saturday 3 May 2008. Sunday 4 May falls before the 3rd day, so it took effect on 7 May 2008.
  - Loi organique 2016-23 appeared in JORS numéro spécial 6946 of Friday 15 July 2016. Sunday 17 July falls before the 3rd day, so it took effect on 19 July 2016.
- Public holidays are not modelled; none is known to fall in those windows. Loi 70-14 was later amended by Loi 71-07, which could not be checked.
- **Laws published from 20 March 2021** follow Loi n° 2021-21 du 2 mars 2021, art. 10: they take effect "un jour franc à compter de leur publication au Journal officiel". No act in this record falls under that rule yet.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a law that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- **Loi 2008-12 against a second official copy.** The Journal officiel text was compared article by article with the PDF that the Commission de Protection des Données Personnelles (CDP) publishes. Vie-publique.sn serves the same file. All 78 articles agree apart from spelling ("oeuvre"/"œuvre") and two words the PDF splits at line ends. The PDF also lacks the last sentence of art. 78, which the Journal officiel prints and which is kept. Two transcription slips in the Journal officiel's web edition are corrected from the CDP copy: a missing "a" before item a) of art. 16, and "taritements" for "traitements" in art. 57. Both are listed in REPRODUCE.md.
- **Nothing dropped.** Every word of each law's body, from the enacting formula to the signature, is in a provision file except the chapter and section headings and the article numbers.
- **Today's text.** No amending law was found for either act. The CDP's law page (captured 24 January 2025) and vie-publique.sn (October 2026) still give Loi 2008-12 as the data protection law. The Conseil constitutionnel still publishes Loi organique 2016-23 without amendments (October 2026). A 2026 constitutional revision (loi n° 18/2026) would have replaced the Conseil with a Cour constitutionnelle, but décision n° 6/C/2026 of 9 July 2026 declared it unconstitutional, and it never took effect.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change. Its e-mail address cannot exist, so `git blame` and `git log --author` name laws. The committer is always Lexifina.

- Each act's first commit is the act as enacted, credited to the act itself (Loi n° 2008-12, Loi organique n° 2016-23).
- Blame credits whole lines (one paragraph per line). Use `git log -p --word-diff` to see exactly which words a change made.

## What it does not show

- **Only two acts.** The Constitution, the codes and other laws are not in this record yet (see above).
- **Headings** (Chapitre, Section, Titre) are left out; each file starts with "# Article N". The exposé des motifs, the enacting formula, the executory formula ("sera exécutée comme loi de l'État") and the signatures are left out too.
- **Deposit dates.** The in-force days use each issue's printed date as the deposit date (see Dates).
- **No OCR.** Texts published only as scanned images are not included.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

The Journal officiel and the CDP are read through Internet Archive captures, with the capture timestamps pinned in Lexifina's code.

## Sources

| Source | What it gives | Used for |
| --- | --- | --- |
| [Journal officiel de la République du Sénégal](http://www.jo.gouv.sn) (Internet Archive copy) | The official web edition, one page per published text, about 2001 to 2018 | Loi 2008-12 (JO n° 6406, 3 May 2008) |
| [Conseil constitutionnel](https://conseilconstitutionnel.sn/la-loi-organique/) | Loi organique 2016-23 as promulgated, and its consolidation of the Constitution | Loi organique 2016-23 |
| [Commission de Protection des Données Personnelles](https://www.cdp.sn) (Internet Archive copy) | Its PDF of Loi 2008-12 and its law page | Checking Loi 2008-12 and that it is still the law |
| [Vie Publique Sénégal](https://www.vie-publique.sn) | Journal officiel issues and laws as PDFs, from a civic publisher | Loi 70-14 and Loi 2021-21 (the in-force rules), and checking for later laws; no legal text in this record comes from it |

The Journal officiel site is offline (checked 28 October 2026) and has no consolidated text. The Secrétariat général du Gouvernement (sgg.gouv.sn) does not resolve, and the Assemblée nationale's site does not answer.

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

See [LICENSE](LICENSE). Texts: Journal officiel de la République du Sénégal (jo.gouv.sn, via the Internet Archive) and Conseil constitutionnel du Sénégal (https://conseilconstitutionnel.sn), official texts of the Republic of Senegal, reproduced with that attribution. Lexifina's arrangement, messages, tables and tools are CC0.

This repository is not legal advice.

## En français

Ce dépôt retrace dans git l'histoire de deux textes sénégalais : un fichier par article, un commit par loi à la date de son entrée en vigueur, et la loi à l'origine du texte comme auteur du commit. Il contient la loi n° 2008-12 du 25 janvier 2008 portant sur la protection des données à caractère personnel, telle que publiée au Journal officiel n° 6406 du 3 mai 2008 (en vigueur le 7 mai 2008), et la loi organique n° 2016-23 du 14 juillet 2016 relative au Conseil constitutionnel, telle que publiée au JORS numéro spécial 6946 du 15 juillet 2016 (en vigueur le 19 juillet 2016). Les dates d'entrée en vigueur suivent l'article 2 de la loi n° 70-14 du 6 février 1970 : le troisième jour suivant le dépôt du Journal officiel, prorogé d'un jour par dimanche. Aucune loi modificative de ces deux textes n'a été trouvée. La Constitution et le Code pénal n'y figurent pas encore : la seule consolidation de la Constitution mêle au texte les notes éditoriales du Conseil constitutionnel, et le Code pénal n'est disponible qu'en images numérisées. `python tools/en_vigueur_au.py 2020-01-01 donnees-personnelles 33` affiche l'article 33 tel qu'il était en vigueur à cette date, et `git blame donnees-personnelles/art-033.md` nomme la loi à l'origine de chaque alinéa. Ce dépôt ne constitue pas un avis juridique.
