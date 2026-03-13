# Reference Acquisition Guide for Claude Code

This guide tells Claude Code how to acquire PDFs of academic references using `download_papers.py`. The script handles institutional proxy authentication (EZproxy), publisher-specific PDF extraction for 8 major publishers, open access pre-checks, and print-to-PDF fallback. The script and a starter `papers_config.json` are both in the repo root.

## Prerequisites

1. **Chrome or Chromium** installed (the script auto-detects common paths)
2. **Python 3.8+** with these packages:
   - `selenium` (required for EZproxy downloads)
   - `requests` (required for open access pre-check)
   - `chromedriver` matching installed Chrome version

Setup:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install selenium requests
# Install chromedriver:
pip install chromedriver-autoinstaller
```

3. **`download_papers.py`** in the project root (copy from RN-IIM if not present)
4. **Institutional proxy access**: Binghamton EZproxy at `https://login.proxy.binghamton.edu/login?url=`

---

## Step 0: Check for Transferable PDFs First

Before downloading anything, ask the user which PDFs from the RN-IIM project are available to transfer. Many papers needed for this project were already acquired there. See the transfer table in `project_setup_specification.md` Part V.

Once confirmed, copy those PDFs to `docs/references/pdfs/` and mark them in `reference_inventory.md` as "transferred from RN-IIM."

---

## Step 1: Initialize the Config

If no config exists yet:
```bash
python3 download_papers.py init --config papers_config.json
```

Edit the config to set the correct `output_dir` and `ezproxy_base`:

```json
{
  "ezproxy_base": "https://login.proxy.binghamton.edu/login?url=",
  "output_dir": "docs/references/pdfs",
  "min_valid_size_bytes": 10000,
  "papers": []
}
```

If a config already exists:
```bash
python3 download_papers.py status --config papers_config.json
```

---

## Step 2: Resolve DOIs

For each reference, resolve the DOI using the CrossRef API (no authentication required):

```bash
curl -s "https://api.crossref.org/works?query.bibliographic=AUTHOR+YEAR+TITLE_KEYWORDS&rows=3" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for item in data['message']['items'][:3]:
    title = item.get('title', [''])[0]
    doi = item.get('DOI', '')
    print(f'{doi}  {title}')
"
```

Replace `AUTHOR+YEAR+TITLE_KEYWORDS` with URL-encoded search terms. Pick the correct match.

For journal articles, the DOI is usually available on the journal website or via Google Scholar. For book chapters, DOIs may exist for Cambridge Books Online, Springer, and similar platforms. For pre-DOI publications (Thompson 1891, Routledge 1919, Métraux 1940), skip this step and go to Step 3.

---

## Step 3: Check for Open Access Availability

For each DOI, check in this order:

**Unpaywall** (best source, no auth required):
```bash
curl -s "https://api.unpaywall.org/v2/DOI_HERE?email=user@binghamton.edu" | python3 -c "
import sys, json
data = json.load(sys.stdin)
oa = data.get('best_oa_location', {}) or {}
if oa.get('url_for_pdf'):
    print('OA PDF:', oa['url_for_pdf'])
elif oa.get('url'):
    print('OA landing:', oa['url'])
else:
    print('Not open access via Unpaywall')
print('OA status:', data.get('oa_status', 'unknown'))
"
```

**Semantic Scholar**:
```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/DOI:DOI_HERE?fields=openAccessPdf,externalIds" | python3 -c "
import sys, json
data = json.load(sys.stdin)
pdf = data.get('openAccessPdf') or {}
if pdf.get('url'):
    print('OA PDF:', pdf['url'])
else:
    print('Not available via Semantic Scholar')
"
```

**PubMed Central** (for biomedical papers):
```bash
curl -s "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=DOI_HERE&format=json" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for rec in data.get('records', []):
    pmcid = rec.get('pmcid', '')
    if pmcid:
        print(f'PMC PDF: https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/')
    else:
        print('No PMC version')
"
```

**For public domain texts** (Thompson 1891, Routledge 1919, and any pre-1928 publication):

Check these in order:
1. HathiTrust Digital Library: https://catalog.hathitrust.org (search by author and title; full view available for public domain)
2. Internet Archive: https://archive.org (search; download as PDF)
3. Smithsonian Institution Digital Library: https://library.si.edu (for Thompson 1891 specifically -- it appeared in the Smithsonian Annual Report)

For Thompson 1891:
```bash
# Try Internet Archive directly
curl -L "https://archive.org/download/annualreportofbo1889smit/annualreportofbo1889smit.pdf" \
  -o docs/references/pdfs/thompson_1891.pdf
```

For Routledge 1919 (if not transferred from RN-IIM):
```bash
curl -L "https://archive.org/download/mysteryofeaste00rout/mysteryofeaste00rout.pdf" \
  -o docs/references/pdfs/routledge_1919.pdf
```

---

## Step 4: Build the Config

Add each paper using the `add` subcommand or by editing `papers_config.json` directly:

```bash
# Paper with DOI only (will use EZproxy)
python3 download_papers.py add --config papers_config.json \
    --filename sahlins_1963.pdf \
    --doi 10.1017/S0010417500002115

# Paper with DOI and OA URL (tries OA first)
python3 download_papers.py add --config papers_config.json \
    --filename dye_2010.pdf \
    --doi 10.7183/0002-7316.75.4.727 \
    --oa-url "https://www.jstor.org/stable/pdf/20622605.pdf"

# Paper without DOI (direct URL)
python3 download_papers.py add --config papers_config.json \
    --filename thompson_1891.pdf \
    --url "https://archive.org/download/annualreportofbo1889smit/annualreportofbo1889smit.pdf"
```

JSON format for direct editing:
```json
{
  "filename": "sahlins_1963.pdf",
  "doi": "10.1017/S0010417500002115",
  "url": null,
  "oa_url": null,
  "status": "pending",
  "note": ""
}
```

---

## Step 5: Run a Dry Run

Before downloading:
```bash
python3 download_papers.py download --config papers_config.json --dry-run
```

---

## Step 6: Download

```bash
python3 download_papers.py download --config papers_config.json
```

The script:
1. Tries OA URLs first via `requests` (no browser needed)
2. Opens Chrome for EZproxy login
3. Waits for authentication (up to 5 minutes)
4. Downloads each paper, trying publisher-specific extraction then print-to-PDF fallback
5. Updates `status` and `note` in the config after each paper

Keep browser visible for debugging:
```bash
python3 download_papers.py download --config papers_config.json --headed
```

Download only specific papers:
```bash
python3 download_papers.py download --config papers_config.json --only "kirch"
```

---

## Step 7: Verify Downloads

```bash
python3 download_papers.py status --config papers_config.json
```

Validate PDFs programmatically:
```python
import os
from pathlib import Path

output_dir = Path("docs/references/pdfs")
for pdf in sorted(output_dir.rglob("*.pdf")):
    size = pdf.stat().st_size
    with open(pdf, "rb") as f:
        magic = f.read(4)
    valid = magic == b"%PDF" and size > 10000
    status = "OK" if valid else "BAD"
    print(f"  [{status}] {pdf.name} ({size:,} bytes)")
```

Report any `BAD` results before beginning claims extraction.

---

## Step 8: Report Results and Update Tracking

After each acquisition batch:
1. Update `papers_config.json` status fields (the script does this automatically)
2. Update `reference_inventory.md` with acquisition results and postprint/published notes
3. Update `status.md` PDF Inventory table
4. Report to the user: how many acquired, which failed, suggested alternatives for failures

---

## Handling Failures by Failure Mode

| Failure | Cause | Fix |
|---------|-------|-----|
| "session expired" | EZproxy cookie timed out mid-run | Re-run; script prompts for login again |
| "could not download" | Publisher not supported or page structure changed | Try manually in browser; use `--only` to retry |
| "navigation error" | Network issue or bad URL | Verify DOI/URL is correct |
| "no DOI or URL" | Missing identifier in config | Add DOI or URL to the config entry |
| File too small (<10KB) | Downloaded HTML or abstract instead of PDF | May be abstract-only; try different URL or check journal access |
| Book chapters | Not available via DOI/EZproxy | Ask user about institutional ebook access; flag for ILL |
| Archive.org lending | 403 Forbidden | Requires borrowing login; manual download needed |

---

## Supported Publishers

`download_papers.py` has publisher-specific PDF extractors for:

1. **ScienceDirect (Elsevier)** -- constructs `/pdfft` download URL from PII
2. **Wiley** -- constructs `/pdfdirect/` URL from DOI
3. **Nature** -- appends `.pdf` to article URL
4. **Springer** -- constructs `/content/pdf/` URL from DOI
5. **JSTOR** -- constructs `/stable/pdf/` URL from stable ID
6. **Taylor & Francis** -- constructs `/doi/pdf/` URL from DOI
7. **Cell Press** -- constructs `/action/showPdf` URL from PII
8. **UChicago Press** -- constructs `/doi/pdf/` URL from DOI

For other publishers, the script falls back to scanning the page for PDF links, then print-to-PDF capture.

---

## File Naming Conventions

- Single author: `smith_2024.pdf`
- Two authors: `smith_jones_2024.pdf`
- Three or more: `smith_et_al_2024.pdf`
- Books (relevant chapters only): `kirch_1984_relevant_chs.pdf`
- Specific chapters if downloaded separately: `kirch_1984_ch7.pdf`
- Disambiguation: `mccoy_1976.pdf`, `mccoy_2006.pdf`
- Transferred from RN-IIM: use same filename; note in `reference_inventory.md`

The european_accounts collection uses a subdirectory structure. Preserve it if transferring:

```
docs/references/pdfs/
  european_accounts/
    01_roggeveen_1722/
    02_gonzalez_1770/
    03_cook_1774/
    04_laperouse_1786/
    05_post_laperouse_1793-1862/
```

---

## Priority Download Order

1. **Transfer from RN-IIM** (no download needed; user confirms availability)
2. **Public domain** (Thompson 1891, Routledge 1919 if not transferred; HathiTrust/archive.org)
3. **Gold OA journal articles** (PLOS ONE, Frontiers, MDPI; download directly)
4. **JSTOR** (Sahlins 1963, Dye 2010, Kolb 1994, Wobst 1978, Stahl 1993, Rogers 2000; via EZproxy)
5. **Other journal articles via EZproxy** (Wylie 1985, Lyman and O'Brien 2001, Feinman and Neitzel 1984)
6. **Books** (ask user first; attempt institutional ebook access or ILL)

---

## Batch Processing Notes

- The script saves status after each paper; interrupted runs resume by re-running
- Papers already on disk (valid file size) are automatically skipped
- Use `--only` to retry specific failed papers
- EZproxy sessions may expire mid-run for large batches; re-run to pick up where it left off
- The script waits 2 seconds between papers; this is sufficient for most publishers
- Update `reference_inventory.md` and `status.md` after each batch

---

## Troubleshooting

**Chrome won't launch**: Ensure Chrome is installed and no other instance is running on the debug port.

**ChromeDriver version mismatch**: `pip install chromedriver-autoinstaller` usually resolves this.

**All papers fail with "session expired"**: The EZproxy session was not established. Re-run and complete login in the Chrome window.

**Downloads are HTML pages, not PDFs**: Publisher page structure may have changed. Try the EZproxy URL manually in Chrome. If that works, the script's publisher extractor may need updating.

**Books return abstract-only or preview pages**: Book chapters require institutional ebook subscription. Flag for ILL and report to user.
