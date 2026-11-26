# Structure

Senegal's national law (`sn/national/acts`), in French, one folder per text and one file per article.

| Folder | What it holds |
| --- | --- |
| `constitution/` | Constitution du 22 janvier 2001: `preambule.md`, `art-001.md` … `art-108.md` |
| `codes/<code>/` | Codes as enacted (`codes/code-des-douanes/`, `codes/code-de-la-peche-maritime/`, …) |
| `lois/<année>/<loi>/` | Laws, organic and constitutional laws (`lois/2016/loi-2016-31/`, `lois/2003/loi-2003-15/`) |
| `ordonnances/<année>/` | Ordinances |
| `decrets/<année>/<décret>/` | Decrees (`decrets/2006/decret-2006-374/`) |
| `arretes/<année>/<arrêté>-<date>/` | Ministerial, interministerial, presidential and Prime Minister's orders (numbers repeat, so the date of the order is part of the name) |
| `decisions-ministerielles/<année>/` | Ministerial decisions |
| `actes-communautaires/<année>/` | UEMOA, CEDEAO and OHADA acts as printed in the Journal officiel |
| `traites/<année>/` | Treaties and conventions as printed in the Journal officiel |
| `rectificatifs/<année>/` | Errata |
| `journal-officiel/<année>/<numéro>/` | One `README.md` per Journal officiel issue, listing the texts of that issue held here |
| `donnees-personnelles/`, `conseil-constitutionnel/` | The two acts of the first build (Loi n° 2008-12, Loi organique n° 2016-23), kept at their paths |

Files: `art-NNN.md` (`art-001.md` is Article premier; `art-012-bis.md`; prefixed codes use `art-l-001.md`, `art-r-001.md`);
a text without numbered articles is one `texte.md`. Each text folder has a `README.md` with its full title and source.
Each file starts with `# Article …` and holds one paragraph or list item per line.

Commits: one per text version, dated at noon Africa/Dakar on the day it took effect (trailer `In-force:`, basis in
`In-force-basis:`); the author is the text itself (`Décret n° 2006-374 <decret-2006-374@jo.gouv.sn.invalid>`), the
committer Lexifina. Trailers: `Law`, `Kind`, `Enacted`, `Published`, `Journal-officiel`, `In-force`,
`In-force-basis`, `Source`, `Act`, `Provisions`.

Folder counts at this build:

| Folder | Texts |
| --- | ---: |
| `actes-communautaires/` | 164 |
| `arretes/` | 4198 |
| `codes/` | 9 |
| `conseil-constitutionnel/` | 1 |
| `constitution/` | 1 |
| `decisions-ministerielles/` | 213 |
| `decrets/` | 4946 |
| `donnees-personnelles/` | 1 |
| `lois/` | 467 |
| `rectificatifs/` | 15 |
| `traites/` | 12 |
