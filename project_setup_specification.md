# RN-CHIEF: Project Setup Specification

## Instructions for Claude Code

This is the master specification for the RN-CHIEF (Rapa Nui Chiefdom Attribution: A Critical Evaluation) project. Read this entire document before doing anything. It contains:

1. What this project is and what we are trying to accomplish
2. What files already exist in the repo
3. Instructions for creating files that do not yet exist
4. The reference processing pipeline and research workflow
5. Task priorities

---

# Part I: Project Overview

## What This Paper Does

The paper evaluates the chiefdom attribution for Rapa Nui (Easter Island): the claim, embedded in the literature since Sahlins (1958) and operationalized archaeologically through Kirch (1984, 2010) and McCoy (1976), that prehistoric Rapa Nui society was organized as a Polynesian chiefdom characterized by hereditary rank, centralized redistribution, and chiefly direction of monument production.

We show that this attribution rests on a five-step circular inferential chain that was never independently grounded in the archaeological record, and that the archaeological evidence, when analyzed on its own terms, is better explained by collective action and cooperative production without centralized chiefly command.

Target journal: *Journal of Archaeological Method and Theory* or *Journal of Anthropological Archaeology* (finalize with co-author before submission)

## The Paper's Argument

The paper evaluates the chiefdom attribution through four converging arguments:

1. **The contact-era accounts are insufficient.** European observers at contact (Roggeveen 1722, González 1770, Cook 1774, La Pérouse 1786) recorded a politically complex and contested situation using European categories. The accounts are thinner and less consistent on hereditary chiefly authority than the literature assumes. They cannot support the inference of a classic Polynesian redistributive chiefdom.

2. **The post-slave-raid ethnographic sources are compromised.** The sources that most clearly describe Rapa Nui "traditional" political organization (Thompson 1891, Routledge 1919, Métraux 1940, Englert) were recorded after the 1862-1863 slave raids and successive epidemics that reduced the population from roughly 3,000 to fewer than 200. The political forms they describe cannot straightforwardly represent pre-contact prehistoric organization.

3. **The Polynesian analogy is not warranted.** The chiefdom framework was imported from comparative Polynesian ethnology (Sahlins 1958, Kirch 1984) built primarily on Hawaii, Tonga, and Samoa. Rapa Nui's distinctive isolation, resource base, and demographic trajectory make the structural analogy questionable. Applying the Hawaiian or Tongan model to Rapa Nui requires assumptions of historical continuity and structural homology that have not been demonstrated.

4. **The archaeological evidence does not require the chiefdom model.** The material signatures attributed to chiefly command (moai production, ahu construction, monumental scale, settlement patterns) are equally consistent with, and in several respects better explained by, collective action without centralized authority. Published work provides positive evidence for decentralized cooperative production.

The five-step circularity that unifies these arguments:

1. European observers record political arrangements at contact using European categories, and post-slave-raid ethnographers record a recovery-period society
2. Those accounts are treated as descriptions of "traditional" pre-contact society, collapsing post-contact disruption and centuries of change into a timeless ethnographic present
3. Polynesian chiefdom models (built from other islands) generate expectations about what Rapa Nui's archaeological record should contain
4. The expectations are framed at a level of generality that the record always satisfies (there are ahu, moai, differential site elaboration)
5. The archaeological evidence is presented as independent confirmation of the chiefdom model, but the model was never derived from that evidence in the first place

## Relationship to the *Current Anthropology* Paper

The CA paper makes a general epistemological argument about the chiefdom concept across anthropological archaeology. It requires a concrete demonstration for at least one region where the argument can be made in full. This paper provides that demonstration. The CA paper can then point here rather than developing the Rapa Nui case within its word limits. When the CA paper reaches journals, reviewers who want to attack the Rapa Nui evidence will need to engage with this paper, which gives the CA argument structural protection.

## Key Figures in the Debate

- **Patrick Kirch**: Primary architect of the Polynesian chiefdom comparative framework and its application to Rapa Nui. *Evolution of the Polynesian Chiefdoms* (1984) and *How Chiefs Became Kings* (2010) are the primary targets of the analogy critique
- **Patrick McCoy**: 1970s fieldwork on Rapa Nui (McCoy 1976). The primary archaeological application of chiefdom models to Rapa Nui's material record
- **Marshall Sahlins**: The comparative Polynesian ethnology on which Kirch's framework draws (Sahlins 1958, 1963)
- **Katherine Routledge**: 1914-1915 expedition; *The Mystery of Easter Island* (1919). Influential source recorded 50+ years after the slave raids
- **Alfred Métraux**: *Ethnology of Easter Island* (1940). The most systematic mid-20th-century ethnographic synthesis; recorded ~75 years after the slave raids
- **William Thomson**: 1886 Smithsonian expedition; earliest systematic ethnographic account; recorded ~25 years after the slave raids
- **Carl Lipo**: Co-author. Extensive published work on Rapa Nui settlement, moai transport, monument production, and collective action
- **Robert DiNapoli**: Co-author (lead). Published work on Rapa Nui chronology, ahu-freshwater correlation, demographic modeling, and population resilience

## Claude Code's Role

Claude Code's primary role is research assistance: extracting claims from source PDFs, tracking how the chiefdom attribution was constructed and perpetuated across publications, compiling the evidence base, and helping draft manuscript prose. This is a research and writing project, not a computational one.

---

# Part II: What Already Exists in the Repo

At initialization, the following working documents should be present. Read each before doing anything else.

## Pre-existing Working Documents (`docs/working/`)

### `chiefdom_bibliography_final_consolidated.md`

A comprehensive annotated bibliography of the chiefdom literature organized into 10 thematic sections: (I) foundational neoevolutionary frameworks, (II) critiques of the chiefdom concept, (III) collective action alternatives, (IV) regional case studies, (V) recent works 2020-2026, (VI) epistemological foundations, (VII) the ethnohistoric projection problem, (VIII) sociology of knowledge, (IX) the decolonial critique, (X) models calibrated to data. This is the primary research base for both this paper and the CA paper. Use it to identify what has already been assessed and what sources are most relevant to the Rapa Nui-specific argument.

### `chiefdom_argument_outline.md`

A detailed argument outline for the broader CA paper, organized into ten sections mirroring the bibliography. This contains the general epistemological argument (empirical sufficiency, equifinality, five-step circularity, sociology of knowledge, decolonial critique) that this paper will demonstrate specifically for Rapa Nui. Use it to understand the theoretical scaffolding; the Rapa Nui paper applies these arguments to a specific case rather than making them in the abstract.

### `chiefdom_CA_strategy_and_outline.md`

The strategy memo and revised outline for the *Current Anthropology* paper. Contains the five-movement structure for the CA paper and notes on anticipated objections, tone, and commentator suggestions. Useful for understanding where the Rapa Nui paper fits in the larger project and what the CA paper will need from it.

**Important**: These working documents are UNVERIFIED at the level of specific page citations. Claims drawn from them for manuscript prose must be checked against primary sources. Tag any such claims `[UNVERIFIED: {description}]` until verified.

---

# Part III: Files to Create on First Run

## Task 1: Copy or Confirm `CLAUDE.md`

`CLAUDE.md` should already be in the repo root. Do not overwrite it.

## Task 2: Create `README.md`

Create `README.md` in the repo root containing:

- Project title: "RN-CHIEF: The Chiefdom Attribution on Rapa Nui: A Critical Evaluation"
- One paragraph: the attribution under review (the claim that prehistoric Rapa Nui society was a Polynesian redistributive chiefdom, established through Sahlins, Kirch, and McCoy)
- One paragraph: the argument (the attribution rests on a circular inferential chain combining insufficient contact accounts, compromised post-slave-raid ethnography, and an unwarranted Polynesian analogy; the archaeological evidence is better explained by collective action)
- The full directory structure tree after setup
- Authors: [user name] and Carl P. Lipo, Department of Anthropology, Binghamton University
- Target journal: *Journal of Archaeological Method and Theory* or *Journal of Anthropological Archaeology* (TBD)

## Task 3: Create Directories

Create the following directories:

```
docs/references/summaries/
docs/references/claims/
docs/evidence/
docs/manuscript/
docs/working/        (may already exist; do not overwrite contents)
R/
figures/
```

## Task 4: Create `docs/references/INDEX.md`

Master lookup table for all sources. Entries added as papers are processed through the pipeline. Header should describe the tag vocabulary. Controlled tags include at minimum:

`chiefdom-attribution`, `contact-era`, `post-slave-raid-ethnography`, `polynesian-analogy`, `collective-action`, `archaeological-evidence`, `epistemology`, `settlement-patterns`, `monument-production`, `mortuary-evidence`, `political-authority`, `decolonial`, `own-work`, `critique`, `equifinality`, `circularity`, `data-quality`

Each entry format:

```
## {Author} {Year}
**File**: `{filename}.pdf`
**Tags**: tag1, tag2, tag3
**Pipeline**: claims / summary / evidence / index [mark each complete as processing proceeds]
**Notes**: [one-line relevance note]
```

## Task 5: Create `docs/references/crosscheck_log.md`

Running log of verification checks. Every claim in the manuscript that attributes a specific statement to a published source must be verified here before submission.

**Mandatory pre-submission checklist** (all 10 must have entries before submission):

1. All direct quotes verified against source PDFs with page numbers
2. All claims attributed to contact-era accounts verified against primary sources with page numbers
3. All claims attributed to Thompson 1891, Routledge 1919, Métraux 1940, and Englert verified with page numbers
4. All claims attributed to Kirch 1984 and Kirch 2010 verified with page numbers; chapter and page
5. All claims attributed to own published work verified against published versions
6. No claim attributes to a source something the source does not actually say
7. All `[CITE-CHECK]` flags in manuscript resolved
8. All `[UNVERIFIED]` flags in working documents resolved or excluded from manuscript prose
9. Page numbers from postprints/preprints converted to published versions where available
10. Tone check: no passage reads as attacking researchers personally rather than evaluating evidence

## Task 6: Create `docs/references/reference_inventory.md`

Acquisition status and version tracking. Updates as PDFs are acquired.

Header section: acquisition date, notes on postprint vs. published status.

Table format:

| Filename | Title/Author | Version | Acquired | Claims | Summary | Notes |
|----------|-------------|---------|----------|--------|---------|-------|
| `kirch_1984_ch7-8.pdf` | Kirch 1984, Ch 7-8 | photocopy/scan | no | no | no | Chapters TBD |

Postprint policy: if only a postprint or preprint is available, flag with `[POSTPRINT]` in the notes column. Before submission, verify page numbers against the published version and record the conversion in the crosscheck log.

## Task 7: Create `docs/references/summary_template.md`

Template file for structured paper summaries. Contents:

```markdown
# Summary: {Author} {Year}

**Full citation**: 
**PDF filename**: 
**Date summarized**: 
**Pipeline status**: claims / summary / evidence / index

---

## Relevance to Argument

[1-2 sentences: how this source relates to the chiefdom attribution argument. Which of the five steps of the circularity does it address? Does it support or complicate our argument?]

## Key Claims

[List each claim relevant to our argument, with evidence strength rating]

| Claim | Page | Type | Strength | Notes |
|-------|------|------|----------|-------|
| [claim statement] | [p. X] | empirical / interpretive / speculative | strong / moderate / weak | [brief note] |

Claim types:
- **empirical**: direct observation or measurement reported by the author
- **interpretive**: inference from empirical data; not directly observable
- **speculative**: acknowledged by the author as tentative, or basis unclear
- **methodological**: claim about how to conduct or interpret research

Strength ratings apply to how well the evidence cited actually supports the claim, not to whether we agree with the claim.

## Data Presented

[What datasets, measurements, or primary observations does this source contribute? Note sample sizes, methods, geographic scope.]

## Methodological Notes

[Any concerns about methods, dating, sample size, analogical leaps, or dependency on other sources.]

## Connections to Other Sources

[Which sources does this one depend on? Which sources cite or respond to this one? Does this source corroborate or conflict with others in the collection?]

## Post-Slave-Raid Dependency

[If this source is Thompson, Routledge, Métraux, or Englert, or if it depends substantially on those sources: note which claims carry [POST-RAID] status and why.]

## Verification Notes

[Any discrepancies found between claims file and PDF; any page number corrections; any cases where the source does not say what is attributed to it.]
```

## Task 8: Create `docs/references/claims_template.md`

Template file for systematic claims extraction. Contents:

```markdown
# Claims Extraction: {Author} {Year}

**Full citation**: 
**PDF filename**: 
**PDF version**: [published / postprint / preprint / scan -- note page number reliability]
**Date extracted**: 
**Extractor**: Claude Code

---

## Claims

### Claim {N}

**Statement**: [Quote or close paraphrase of the claim as the source states it]
**Page**: [p. X or pp. X-Y]
**Type**: empirical / interpretive / speculative / methodological
**Evidence cited by author**: [what does the author cite in support of this claim?]
**Depends on**: [does this claim require other claims or sources to be reliable?]
**Independent archaeological support**: [is there independent evidence from the archaeological record for this claim, or does it rest on analogy/ethnography?]
**Counter-evidence**: [any evidence that contradicts or complicates this claim]
**[POST-RAID]**: yes / no / partial [flag if derived from Thompson, Routledge, Métraux, or Englert]
**First appearance**: [is this claim original to this source, or does it appear in earlier literature? If earlier, cite where]
**Notes**: [anything else relevant]

---

[Repeat for each claim]

---

## Claim Hardening Tracking

[For sources that appear in multiple editions or versions, or that are cited as establishing claims later treated as settled: note where language has hardened from tentative to assertive, or where qualifications present in an earlier source have been dropped in later citations.]

## Summary Assessment

[2-3 sentences: what does this source contribute to the chiefdom attribution? What does it contribute to our critique?]
```

## Task 9: Create Evidence Compilation Files

Create five files in `docs/evidence/`. Each should begin with the key questions it addresses and the anticipated sources, then leave structured space for evidence to be compiled as PDFs are processed.

### `docs/evidence/contact_accounts_evidence.md`

Key questions:
- What do Roggeveen (1722), González (1770), Cook (1774), and La Pérouse (1786) actually record about political authority, hereditary rank, and redistribution?
- Are the political leaders described consistent with hereditary chiefly authority, or could they be situational leaders, intermediaries, or individuals who emerged from the contact situation itself?
- What don't the accounts describe that chiefdom models would predict (redistribution networks, tribute, ranked genealogies, chiefly control over production)?
- Where do accounts conflict with each other or with later ethnographic descriptions?
- What political disruption had already occurred before each systematic visit?

Anticipated sources: European accounts collection (Corney 1903 for Roggeveen, González, Cook; La Pérouse 1799 English translation), Richards 2018, Boersema 2018, Pollard et al. 2010.

### `docs/evidence/ethnographic_sources_evidence.md`

Key questions:
- When were Thompson (1891), Routledge (1919), Métraux (1940), and Englert recorded relative to the 1862-1863 slave raids and subsequent epidemics?
- What is known about the demographic recovery process and the surviving population's composition and knowledge?
- What specifically do these sources say about hereditary rank, the ariki mau, mata group organization, and chiefly authority? How consistent are they with each other?
- Which chiefdom-supporting claims in the archaeological literature depend primarily on these sources?
- What do these sources describe that is consistent with post-collapse political reorganization rather than pre-contact tradition?

Anticipated sources: Thompson 1891, Routledge 1919, Métraux 1940, Englert (relevant edition), haoa_et_al_2017 (Boersema ch. 8, Richards ch. 9).

### `docs/evidence/polynesian_analogy_evidence.md`

Key questions:
- What is the structural basis of the Polynesian chiefdom comparative model (Sahlins 1958, Kirch 1984)?
- On what island cases was the model primarily built, and what are the evidential bases for those cases?
- How specifically was this model applied to Rapa Nui by Kirch (1984, 2010) and McCoy (1976)?
- What assumptions of historical continuity and structural homology are required for the analogy to hold?
- What features of Rapa Nui's history and ecology distinguish it from the islands on which the model was built?
- Does Kirch himself acknowledge limits on applying the model to Rapa Nui?
- Are there parallel critiques of the Polynesian chiefdom model from within Pacific archaeology (Dye 2010 for Hawaii; Kolb 1994)?

Anticipated sources: Sahlins 1958, Sahlins 1963, Kirch 1984, Kirch 2010, Kirch and Green 2001, McCoy 1976, Valeri 1985, Dye 2010, Kolb 1994.

### `docs/evidence/archaeological_record_evidence.md`

Key questions:
- What is the direct archaeological evidence for hereditary rank on Rapa Nui (differential mortuary treatment, elite residential compounds, prestige goods, evidence of tribute)?
- What does the spatial distribution of ahu tell us about political territories vs. resource-centered organization (DiNapoli et al. 2019)?
- What does the ahu construction chronology show about the tempo and character of monument production (DiNapoli et al. 2020)?
- What does the quarry production evidence show about centralized vs. decentralized organization (Lipo et al. 2025)?
- What does the moai transport evidence show (Hunt and Lipo 2011, Lipo et al. 2013)?
- What do settlement patterns show about population distribution, internal differentiation, and change over time?
- How do collective action frameworks generate different expectations from chiefly-command frameworks, and which better fits the record?

Anticipated sources: DiNapoli et al. 2019, 2020, 2021 (sustainability), Lipo et al. 2013, 2025, Hunt and Lipo 2011, McCoy 1976, Mulrooney 2013, Davis et al. 2024, Moreno-Mayar et al. 2024.

### `docs/evidence/circularity_demonstration.md`

Key questions:
- Can we document each of the five steps of the circularity for Rapa Nui specifically?
- Step 1: What were political conditions at contact? What European categories did observers bring? What disruption had already occurred?
- Step 2: Who made the move of treating these accounts as "traditional" or "prehistoric" evidence, and when? Cite specific passages.
- Step 3: Which specific publications introduced the Polynesian chiefdom expectations for Rapa Nui's archaeological record?
- Step 4: Which specific archaeological features were cited as confirming the chiefdom model? What alternative explanations were not considered?
- Step 5: Where in the literature is this presented as independent archaeological confirmation?
- Has any published analysis evaluated the archaeological record independently of the ethnohistoric framework and reached different conclusions?

Anticipated sources: All of the above. Key passages needed from Kirch 1984, McCoy 1976, Sahlins 1958 (the analogy introduction), Routledge 1919 (the source of many chiefdom-supporting claims), Fabian 1983, Stahl 1993, Wobst 1978.

## Task 10: Create `figures_plan.md`

Create in the repo root. Track figure specifications and status.

```markdown
# Figures Plan

## Figure Status

| Fig | Description | R script | Output | Status |
|-----|-------------|----------|--------|--------|
| 1 | [Map: Rapa Nui with ahu locations, colored by size/complexity] | R/fig1_ahu_map.R | figures/fig1_ahu_map.png | planned |
| 2 | [Inferential chain diagram: five steps of circularity] | R/fig2_circularity.R | figures/fig2_circularity.png | planned |
| 3 | [Timeline: contact accounts, slave raids, ethnographic sources, archaeological publications] | R/fig3_timeline.R | figures/fig3_timeline.png | planned |

## Figure Notes

[Add notes on data sources, design decisions, and revision history as figures are created]
```

## Task 11: Create Manuscript Skeleton

Create `docs/manuscript/MAIN_TEXT_V1.md` with the structure below. The abstract goes at the top once drafted. Leave section bodies empty for now.

**Title**: The Chiefdom on Rapa Nui: Circularity, Analogy, and the Epistemology of Political Attribution

**Abstract**: [Draft after sections complete]

**1. Introduction**
The chiefdom concept has organized interpretation of Rapa Nui archaeology since the mid-20th century. Frame the problem: every major category of evidence (monument production, settlement patterns, mortuary differentiation) has been read through a chiefly-command lens imported from comparative Polynesian ethnology. The paper's purpose: demonstrate through systematic evaluation that the attribution rests on a five-step circular inferential chain, and that the archaeological evidence analyzed independently is better explained by collective action.

**2. The Chiefdom Attribution: Origins and Development**
Trace the attribution: Sahlins's comparative Polynesian stratification model (1958), Kirch's evolutionary chiefdom framework (1984, 2010), McCoy's archaeological application (1976), and subsequent research operating within rather than testing the framework. Show that the label was imported before systematic archaeological analysis, not derived from it.

**3. Contact-Era Accounts: What European Observers Actually Recorded**
Systematic evaluation: Roggeveen (1722), González (1770), Cook (1774), La Pérouse (1786). What they recorded on political authority; what they did not record; the political conditions at each moment of contact; how subsequent researchers read more into these accounts than they contain.

**4. Post-Slave-Raid Ethnographic Sources and Their Limits**
Thompson (1891), Routledge (1919), Métraux (1940), Englert. The demographic catastrophe of 1862-1877. Which claims about hereditary rank, ariki mau, and political organization depend on these sources, and why that dependency is epistemologically problematic.

**5. The Polynesian Analogy Problem**
The structural analogy from Hawaii, Tonga, and Samoa. What assumptions of continuity and homology it requires. Features of Rapa Nui's history and ecology that undermine the analogy. Parallel critiques of the Polynesian chiefdom model in Pacific archaeology.

**6. The Archaeological Record Without the Chiefdom Lens**
Evidence for the material signatures of chiefly command: monument production, ahu distribution, settlement patterns, mortuary differentiation. Collective action explanations as an alternative. Specific evidence (quarry organization, ahu-freshwater correlation, moai transport) that supports decentralized cooperative production.

**7. Discussion**
The five-step circularity as a unified account of how the attribution was constructed and perpetuated. The epistemological standard: what evidence would actually be required to support the chiefdom attribution. Why the available evidence, combined with the circularity of what is invoked, warrants abandoning the attribution. Implications for how comparative ethnological frameworks are used as archaeological interpretive tools.

**8. Conclusions**
The chiefdom label has done organizational work in Rapa Nui research, but the evidentiary foundation was circular from the start. The path forward is not a single replacement model but an epistemological standard: do not claim more than the evidence can demonstrate.

## Task 12: Create `status.md`

Create in the repo root. This is a living document that Claude Code updates after completing any significant task. Match the RN-IIM format exactly.

**Current Phase** section: which phase is active and what the next task is.

**PDF Inventory** section: organize by priority group (Priority 1, Priority 2, etc.), each as a table with columns `| Filename | Version | Pipeline |`. The Version column records what version of the PDF is in hand (publisher, CSIC postprint, archive.org scan, user provided, etc.). The Pipeline column records pipeline status as a single value: `pending` / `claims` / `summary` / `complete` / `reference only`. Initialize all as `pending`. Example format:

```
### Priority 1: Core chiefdom-attribution sources

| Filename | Version | Pipeline |
|----------|---------|----------|
| `kirch_1984_relevant_chs.pdf` | | pending |
| `kirch_2010_relevant_chs.pdf` | | pending |
| `mccoy_1976.pdf` | | pending |
```

**Evidence File Status** table: `| File | Status | Lines | Sources Incorporated |`

**Manuscript Status** table: `| Section | Status |` with status values: not started / outline only / draft in progress / draft complete / crosschecked.

**Pre-Submission Checklist**: the 10-item list from `crosscheck_log.md`, with checkbox status.

**Blockers and Open Questions**: anything preventing progress or requiring user input.

**Change Log**: append-only table `| Date | Description |`.

---

# Part IV: The Reference Processing Pipeline

Each source goes through four stages. Templates are in `docs/references/`.

## Stage 1: Claims Extraction

Read the PDF. Create `docs/references/claims/{author}_{year}_claims.md` using the claims template. For each claim relevant to political authority, hereditary rank, redistribution, chiefly command, the Polynesian analogy, monument production, or the chiefdom attribution on Rapa Nui:

- State the claim as the source states it (quote or close paraphrase with page number)
- Classify: empirical / interpretive / speculative / methodological
- Note what evidence the author cites in support
- Note whether the claim depends on other claims or sources
- Note whether there is independent archaeological support, or whether the claim rests on analogy or ethnographic projection
- Note counter-evidence
- Flag `[POST-RAID]` if claim derives from Thompson, Routledge, Métraux, or Englert
- Note whether this claim appears in earlier sources (and whether language has hardened)

For contact-era accounts specifically: distinguish with care between what the observer directly recorded (behaviors, objects, persons) and what they interpreted (ranks, functions, authority structures). Many chiefdom-supporting claims in the literature rest on interpretations layered onto accounts that do not use the language they are interpreted as containing.

## Stage 2: Structured Summary

Create `docs/references/summaries/{author}_{year}.md` using the summary template. Synthesize the claims extraction into an assessment of the source's contribution, methodology, and relationship to the chiefdom attribution.

## Stage 3: Evidence Integration

Update the relevant evidence compilation files in `docs/evidence/`. If a source provides archaeological data, add it. If a source makes a chiefdom attribution claim, add the claim and note whether the cited evidence actually supports it. If a source provides counter-evidence or an alternative explanation, add that.

## Stage 4: INDEX Update

Add the paper to `docs/references/INDEX.md` with appropriate tags and pipeline status.

---

# Part V: PDF Acquisition

Use `download_papers.py` (see `reference_acquisition_guide.md`) for automated acquisition. Always check for open access before using EZproxy. Report all acquisition failures so the user can supply PDFs manually.

Save to `docs/references/pdfs/` using standardized filenames.

## Check Before Downloading: Transferable PDFs from RN-IIM

**Ask the user first.** Many needed PDFs were already acquired in the companion RN-IIM project. Do not download what is already in hand. Check for the following:

| RN-IIM Filename | Status in CHIEF |
|-----------------|-----------------|
| `european_accounts/` directory (Corney 1903 PDFs for Roggeveen, González, Cook; La Pérouse 1799) | Reuse as-is; already processed for settlement/freshwater questions, needs NEW claims extraction focused on political authority |
| `routledge_1919.pdf` | Transfer; needs NEW claims extraction focused on political organization |
| `metraux_1940.pdf` | Transfer if acquired; needs NEW claims extraction |
| `mccoy_1976.pdf` | Transfer; needs NEW claims extraction focused on chiefdom attribution |
| `dinapoli_et_al_2019.pdf` | Transfer; summary sufficient |
| `dinapoli_et_al_2020.pdf` | Transfer; summary sufficient |
| `dinapoli_et_al_sustainability_2021.pdf` | Transfer; summary sufficient |
| `lipo_et_al_2013.pdf` | Transfer; summary sufficient |
| `lipo_et_al_2025.pdf` | Transfer; summary sufficient |
| `moreno-mayar_et_al_2024.pdf` | Transfer; summary sufficient |
| `davis_et_al_2024.pdf` | Transfer; summary sufficient |
| `mulrooney_2013.pdf` | Transfer; summary sufficient |
| `haoa_et_al_2017.pdf` (Routledge book) | Transfer; Boersema (Ch. 8) and Richards (Ch. 9) already processed; other chapters may need review |
| `pollard_et_al_2010.pdf` | Transfer; Birdman cult / contact-period politics |
| `robinson_stevenson_2017.pdf` | Transfer; contact-period Orongo |

**Important note on re-processing**: PDFs from RN-IIM were processed with different research questions in mind (settlement patterns, freshwater access, chronology). Even if a PDF is already in hand, it will need NEW claims extraction focused on the questions this paper asks: political authority, hereditary rank, redistribution, the chiefdom attribution, and the evidence base for and against it.

## Priority 1: Core Chiefdom-Attribution Sources

These are the primary targets of the critique and must be fully processed through claims extraction.

| Paper | Filename | Access note |
|-------|----------|-------------|
| Kirch, P.V. 1984. *The Evolution of the Polynesian Chiefdoms*. Cambridge University Press. | `kirch_1984_relevant_chs.pdf` | Book; ask user about physical/digital access. Priority chapters: Ch 7-8 or equivalent chapters on archaeological correlates and Easter Island |
| Kirch, P.V. 2010. *How Chiefs Became Kings*. University of California Press. | `kirch_2010_relevant_chs.pdf` | Book; ask user. Priority: introduction, comparative framework, Eastern Polynesia/Rapa Nui coverage |
| McCoy, M.D. 1976. *Easter Island Settlement Patterns in the Late Prehistoric and Protohistoric Periods*. Easter Island Committee, Bishop Museum. | `mccoy_1976.pdf` | May transfer from RN-IIM |
| Sahlins, M.D. 1958. *Social Stratification in Polynesia*. University of Washington Press. | `sahlins_1958_relevant_chs.pdf` | Book; ask user. Priority: introduction and comparative stratification chapters |
| Sahlins, M.D. 1963. "Poor Man, Rich Man, Big-Man, Chief." *CSSH* 5(3): 285-303. | `sahlins_1963.pdf` | JSTOR |

## Priority 2: Contact-Era and Ethnographic Primary Sources

Claims extraction with special attention to observation vs. interpretation.

| Paper | Filename | Access note |
|-------|----------|-------------|
| European accounts (Roggeveen 1722, González 1770, Cook 1774, via Corney 1903) | from `european_accounts/` | Transfer from RN-IIM |
| La Pérouse 1786 (English translation, 1799) | from `european_accounts/` | Transfer from RN-IIM |
| Thompson, W.J. 1891. "Te Pito te Henua." *Annual Report of the Smithsonian Institution* 1889: 447-552. | `thompson_1891.pdf` | Public domain; HathiTrust or Smithsonian digital collections |
| Routledge, K. 1919. *The Mystery of Easter Island*. Sifton, Praed & Co. | `routledge_1919.pdf` | Transfer from RN-IIM |
| Métraux, A. 1940. *Ethnology of Easter Island*. Bishop Museum Press. | `metraux_1940.pdf` | Transfer if acquired from RN-IIM; otherwise HathiTrust (lending) or ILL |
| Englert, S. 1948. *La Tierra de Hotu Matu'a*. [English edition as available] | `englert_1948.pdf` | Ask user; may require ILL |

## Priority 3: Own Published Archaeological Work

Positive evidence for collective action; summary-level processing is sufficient since these are our own papers.

| Paper | Filename |
|-------|----------|
| DiNapoli et al. 2019. Ahu-freshwater. *PLOS ONE* 14(1): e0210409. | `dinapoli_et_al_2019.pdf` |
| DiNapoli et al. 2020. Ahu construction tempo. *Journal of Archaeological Science* | `dinapoli_et_al_2020.pdf` |
| DiNapoli et al. 2021. "Triumph of the Commons." *Sustainability* 13(21): 11798. | `dinapoli_et_al_2021_sustainability.pdf` |
| Lipo, C.P. et al. 2013. Walking moai. *Journal of Archaeological Science* 40(6): 2859-2866. | `lipo_et_al_2013.pdf` |
| Lipo et al. 2025. Megalithic statue production. *PLOS ONE* | `lipo_et_al_2025.pdf` |
| Hunt, T.L. and Lipo, C.P. 2011. *The Statues That Walked*. Free Press. | `hunt_lipo_2011_relevant_chs.pdf` |
| Moreno-Mayar et al. 2024. *Nature* | `moreno-mayar_et_al_2024.pdf` |
| Davis et al. 2024. *Science Advances* | `davis_et_al_2024.pdf` |
| Mulrooney, M. 2013. Island-wide radiocarbon chronology. | `mulrooney_2013.pdf` |
| DiNapoli et al. 2021. JPA (warfare). | `dinapoli_et_al_2021_jpa.pdf` |

## Priority 4: Comparative and Critical Literature

Summary-level processing is sufficient for most of these.

| Paper | Filename | Access note |
|-------|----------|-------------|
| Kirch, P.V. and Green, R.C. 2001. *Hawaiki, Ancestral Polynesia*. Cambridge University Press. | `kirch_green_2001_relevant_chs.pdf` | Book; ask user |
| Valeri, V. 1985. *Kingship and Sacrifice*. University of Chicago Press. | `valeri_1985_relevant_chs.pdf` | Book; ask user |
| Dye, T.S. 2010. "Social Transformation in Old Hawai'i." *American Antiquity* 75(4): 727-741. | `dye_2010.pdf` | JSTOR |
| Kolb, M.J. 1994. "Monumentality and the Rise of Religious Authority in Precontact Hawai'i." *Current Anthropology* 35(5): 521-547. | `kolb_1994.pdf` | JSTOR |
| McCoy, M.D. 2006. "Landscapes of War." *American Antiquity* 71(2): 285-314. | `mccoy_2006.pdf` | JSTOR |
| Earle, T.K. 1997. *How Chiefs Come to Power*. Stanford University Press. | `earle_1997_relevant_chs.pdf` | Book; ask user |
| Pauketat, T.R. 2007. *Chiefdoms and Other Archaeological Delusions*. AltaMira. | `pauketat_2007_relevant_chs.pdf` | Book; ask user |
| Feinman, G.M. and Neitzel, J. 1984. "Too Many Types." *AMTA* 7: 39-102. | `feinman_neitzel_1984.pdf` | Check Unpaywall |
| Blanton, R.E. and Fargher, L.F. 2008. *Collective Action in the Formation of Pre-Modern States*. Springer. | `blanton_fargher_2008_relevant_chs.pdf` | Book; ask user |
| Fabian, J. 1983. *Time and the Other*. Columbia University Press. | `fabian_1983_relevant_chs.pdf` | Book; ask user |

## Priority 5: Epistemological Foundations

Summaries only; no full claims extraction needed.

| Paper | Filename | Access note |
|-------|----------|-------------|
| Wobst, H.M. 1978. "The Archaeo-Ethnology of Hunter-Gatherers." *American Antiquity* 43(2): 303-309. | `wobst_1978.pdf` | JSTOR |
| Wylie, A. 1985. "The Reaction Against Analogy." *AMTA* 8: 63-111. | `wylie_1985.pdf` | Check Unpaywall/JSTOR |
| Stahl, A.B. 1993. "Concepts of Time." *American Antiquity* 58(2): 235-260. | `stahl_1993.pdf` | JSTOR |
| Lyman, R.L. and O'Brien, M.J. 2001. "The Direct Historical Approach." *JAMT* 8(4): 303-342. | `lyman_obrien_2001.pdf` | Check Unpaywall |
| Rogers, A.R. 2000. "On Equifinality in Faunal Analysis." *American Antiquity* 65(4): 709-723. | `rogers_2000.pdf` | JSTOR |
| Perreault, C. 2019. *The Quality of the Archaeological Record*. University of Chicago Press. | `perreault_2019_relevant_chs.pdf` | Book; ask user |

---

# Part VI: Task Priority

## Phase 1: Foundation (do first)

1. **Set up the repo.** Create directories and files per Part III. Read the three pre-existing working documents before creating anything.

2. **Ask the user about PDF transfers.** Confirm which RN-IIM PDFs are available. Copy confirmed PDFs to `docs/references/pdfs/`. Initialize `reference_inventory.md` with transfer status.

3. **Ask the user about book access.** Kirch 1984, Kirch 2010, Sahlins 1958 are the highest-priority books. Ask before attempting automated download.

4. **Download remaining PDFs.** Start with open access (Thompson 1891 via HathiTrust, PLOS ONE papers), then JSTOR (Sahlins 1963, Dye 2010, Kolb 1994, Wobst 1978, Stahl 1993, Rogers 2000), then EZproxy for remaining journal articles. Report all failures.

5. **Process the european_accounts collection for political authority claims.** This collection was processed in RN-IIM for settlement and freshwater questions. New claims extraction is needed, focused explicitly on: language of political authority, descriptions of hereditary rank, any mention of redistribution or tribute, what the observers could and could not have known. Create new claims files; do not overwrite RN-IIM versions.

6. **Process Routledge 1919 for political organization claims.** Similarly, new extraction focused on: what she describes about ariki mau, mata groups, hereditary rank, succession, the basis of her knowledge (informants, direct observation, inference), and how far into the post-slave-raid recovery period her observations reach.

## Phase 2: Build the Evidence Base

7. **Process Kirch 1984** (relevant chapters). Full claims extraction: the Polynesian chiefdom model's structure, how it is applied to Rapa Nui, what archaeological evidence Kirch cites for the Rapa Nui case specifically, and where he depends on Métraux/Routledge vs. archaeology.

8. **Process Kirch 2010** (relevant chapters). Claims extraction with attention to how Kirch handles Rapa Nui relative to his Hawaiian case, and whether he acknowledges limits on the analogy.

9. **Process McCoy 1976.** Full claims extraction: the primary archaeological application of chiefdom models to Rapa Nui's material record. This is the key source that operationalized the ethnographic/comparative claims archaeologically.

10. **Process Métraux 1940 and Thompson 1891** for political organization claims. New extraction focused on political authority, with `[POST-RAID]` flagging throughout.

11. **Compile evidence files.** Build all five files in `docs/evidence/` from processed sources.

## Phase 3: Complete the Source Base and Begin Drafting

12. **Process comparative literature** (Sahlins 1958, Kirch and Green 2001, Dye 2010, Kolb 1994). Summaries and relevant claims.

13. **Process epistemological foundations** (Wobst, Wylie, Stahl, Lyman and O'Brien). Summaries only.

14. **Draft Sections 3-5** (contact accounts, ethnographic sources, Polynesian analogy).

15. **Draft Section 6** (archaeological record without the chiefdom lens).

16. **Draft Sections 2, 7, 8** (attribution history, discussion, conclusions).

17. **Draft Introduction and Abstract.**

## Phase 4: Revision and Verification

18. Crosscheck all claims against the mandatory pre-submission checklist.
19. Co-author review with Carl Lipo.
20. Final verification pass.

---

# Part VII: What Claude Code Should Do on First Run

1. Read this file (`project_setup_specification.md`) in full.
2. Read `CLAUDE.md` for project instructions and persona.
3. Read the three pre-existing working documents in `docs/working/`: `chiefdom_bibliography_final_consolidated.md`, `chiefdom_argument_outline.md`, and `chiefdom_CA_strategy_and_outline.md`.
4. **Ask the user two questions before downloading anything:**
   a. Which PDFs from the RN-IIM project are available to transfer? (List the transferable PDFs from Part V.)
   b. What physical or institutional ebook access is available for the priority books (Kirch 1984, Kirch 2010, Sahlins 1958)? These are not available via standard DOI/EZproxy download and require institutional catalog, physical copy, or ILL.
5. Execute Part III tasks: create directories and all specified files.
6. Initialize `papers_config.json` for download (see `reference_acquisition_guide.md`).
7. Copy transferred PDFs. Download remaining PDFs per Part V. Update `status.md` and `reference_inventory.md` after each batch.
8. Begin Phase 1 processing tasks.

**Critical constraint**: Do not begin drafting manuscript prose until the contact accounts, Routledge, Métraux/Thompson, Kirch (1984 and 2010), and McCoy (1976) have all been processed through claims extraction with page numbers. The manuscript must be built on verified claims, not on working document summaries.
