# Reference Index

Master lookup table for all sources. Entries are added as papers are processed through the pipeline.

## Tag Vocabulary

Controlled tags for consistent classification:

- `chiefdom-attribution`: Sources that attribute chiefdom status to Rapa Nui
- `contact-era`: European contact-era accounts (1722-1862)
- `post-slave-raid-ethnography`: Sources recorded after 1862-1863 slave raids
- `polynesian-analogy`: Sources using comparative Polynesian models
- `collective-action`: Sources on collective action and cooperative production
- `archaeological-evidence`: Sources presenting archaeological data from Rapa Nui
- `epistemology`: Sources on archaeological epistemology, analogy, equifinality
- `settlement-patterns`: Sources on settlement distribution and organization
- `monument-production`: Sources on ahu/moai construction, transport, and quarry organization
- `mortuary-evidence`: Sources on burial practices and differential treatment
- `political-authority`: Sources discussing political organization, leadership, authority
- `decolonial`: Sources on decolonial critique and indigenous knowledge
- `own-work`: Published work by the authors
- `critique`: Sources critiquing chiefdom/neoevolutionary frameworks
- `equifinality`: Sources on equifinality in archaeological interpretation
- `circularity`: Sources relevant to demonstrating the circular inferential chain
- `data-quality`: Sources on archaeological data quality and resolution

## Entry Format

Each entry follows this format:

```
## {Author} {Year}
**File**: `{filename}.pdf`
**Tags**: tag1, tag2, tag3
**Pipeline**: claims / summary / evidence / index
**Notes**: [one-line relevance note]
```

---

## Roggeveen 1722 (Corney 1903 translation)
**File**: `european_accounts/01_roggeveen_1722/Easter Island Expeditions_Part 1 (Dutch).pdf`
**Tags**: contact-era, political-authority, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: Primary account of first European contact. One observation of directive authority in crisis context; no evidence of institutional chieftainship.

## Bouman 1722 (von Saher 1994 translation)
**File**: `european_accounts/01_roggeveen_1722/vonSaher-1994-The Complete Journal of Captain Cornelis Bouman...pdf`
**Tags**: contact-era, political-authority
**Pipeline**: claims / summary / evidence / index
**Notes**: Full journal translation. Most detailed behavioral description of the feathered "chief" and threat-submission sequence.

## Von Saher 1990-1993 (Roggeveen/Bouman journal details)
**File**: `european_accounts/01_roggeveen_1722/vonSaher-1990-*.pdf`, `vonSaher-1993-*.pdf`
**Tags**: contact-era, political-authority
**Pipeline**: claims / summary / index
**Notes**: Additional journal details and reliability assessment of all Roggeveen expedition narratives.

## Jakubowska 2012 (Behrens analysis)
**File**: `european_accounts/01_roggeveen_1722/RNJ_26_1_Jakubowska.pdf`
**Tags**: contact-era, data-quality
**Pipeline**: claims / summary / index
**Notes**: Demonstrates unreliability of Behrens' published narrative; two editions produce "two realities."

## González 1770 (Corney 1903 translation)
**File**: `european_accounts/02_gonzalez_1770/Easter Island Expeditions_Part 2 (Spain).pdf`, `Part 3 (Peru-Cook).pdf`
**Tags**: contact-era, political-authority, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: Spanish annexation expedition. No chiefly authority observed; annexation "chiefs" are editorial impositions. Age-graded differentiation only.

## Jakubowska 2014 (Spanish expedition translation analysis)
**File**: `european_accounts/02_gonzalez_1770/Z.Jakubowska2014-TheSpanishexpeditiontoEasterIsland1770...pdf`
**Tags**: contact-era, data-quality, circularity
**Pipeline**: claims / summary / index
**Notes**: Critical. Demonstrates Corney mistranslated *hombres mayores* ("elderly men") as "principal men," systematically inflating age into political authority.

## Cook 1774 (Cook 1846 direct + von Saher and Jakubowska)
**File**: `european_accounts/03_cook_1774/` (multiple files); Cook 1846 OCR: `cook_1846_easter_island_ocr.txt`
**Tags**: contact-era, political-authority, polynesian-analogy, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: Most important contact-era evidence. Cook's own narrative now directly accessed (1846 compiled ed., OCR'd). Cook "confess[ed] myself quite ignorant" of chiefly authority. Named ariki (Ko Toheetai) in Forster accounts; Cook's inland party independently identified a "chief" but described no commanding behavior. Quarry confirmed by Cook via Wales, resolving Forster discrepancy.

## Forster c.1775-1786 (*Memoire sur Waihou*)
**File**: `european_accounts/03_cook_1774/Jakubowska-2014-Still More to Discover...pdf`
**Tags**: contact-era, political-authority
**Pipeline**: claims / summary / index
**Notes**: Full Forster manuscript. Dual purpose: scientific report and Enlightenment political manifesto. Caution required on political descriptions.

## La Pérouse 1786 (1799 Milet-Mureau translation)
**File**: `european_accounts/04_laperouse_1786/LaPerouse-1786-EasterIsland.pdf`, `La Perouse - A Voyage Around the World.pdf`
**Tags**: contact-era, political-authority, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: Most detailed contact-era account. Active search for chiefs yielded negative results. "All conditions are equal"; "no need of a chief." Explicit methodological disclaimer.

## Richards 2008 (*Easter Island 1793 to 1861*)
**File**: `european_accounts/05_post_laperouse_1793-1862/Easter Island 1793-1861- book.pdf`
**Tags**: contact-era, political-authority
**Pipeline**: claims / summary / evidence / index
**Notes**: 79 visits compiled. HMS Blossom (1825) observers explicitly tested and rejected chief hypothesis. No visitor 1793-1862 provides clear evidence of centralized authority.

---

## Eyraud 1864 (Altman 2004 translation + Altman et al. 2003)
**File**: `post_slave_raid/altman_2004/Altman-2004-EarlyVisitorsToEasterIsland-1864-1877-Part1.pdf`, `Altman-2003-EyraudSojourn.pdf`
**Tags**: post-slave-raid-ethnography, political-authority, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: First European to live on the island (9 months, 1864). One year post-raids. Authority described as personal influence, not institutional hierarchy. Collective boat-building without chiefly command. Population ~1,200.

## Roussel 1869 (Altman 2004 translation)
**File**: `post_slave_raid/altman_2004/Altman-2004-EarlyVisitorsToEasterIsland-1864-1877-Part2.pdf`, `Part3.pdf`
**Tags**: post-slave-raid-ethnography, political-authority, chiefdom-attribution, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: Most ethnographically detailed early post-raid source. Records king list (22 generations), four social classes (ariki, ivi atua, matatoa, kio), first-fruits ceremony. Critical: Roussel admits royal authority "had passed completely into the hands of the matatoa." King list disagrees with Thomson and Jaussen lists. Population ~650.

## Loti/Viaud 1872 (Altman 2004 translation)
**File**: `post_slave_raid/altman_2004/Altman-2004-EarlyVisitorsToEasterIsland-1864-1877-Part3.pdf`
**Tags**: post-slave-raid-ethnography, political-authority
**Pipeline**: claims / summary / evidence / index
**Notes**: French naval cadet, 5 days. Literary account. Only informal "old chief" observed. Population ~100, concentrated at Hanga Roa. Most of island deserted. Dutrou-Bornier's commercial operation dominates.

## Pinart 1877 (Altman 2004 translation)
**File**: `post_slave_raid/altman_2004/Altman-2004-EarlyVisitorsToEasterIsland-1864-1877-Part4.pdf`, `Part5.pdf`
**Tags**: post-slave-raid-ethnography, political-authority, archaeological-evidence, settlement-patterns, monument-production
**Pipeline**: claims / summary / evidence / index
**Notes**: Trained French ethnographer, 6 days. Population at nadir: 111 people (26 women). Only authority is Dutrou-Bornier's widow as "regent." No traditional political structure survives. Best early archaeological descriptions of ahu and Rano Raraku. Islanders had "retained no memory at all" of earlier inhabitants.

## Altman 2004 (*Early Visitors to Easter Island 1864-1877*)
**File**: `post_slave_raid/altman_2004/` (Parts 1-5)
**Tags**: post-slave-raid-ethnography, data-quality
**Pipeline**: index
**Notes**: Compilation volume. Translations from French by Ann M. Altman. Editorial introduction by Georgia Lee. Endnotes provide valuable corrections and context. Appendix: ship arrivals list 1722-1879 (from McCall 1990).

## Geiseler 1883 (*Die Oster-Insel*)
**File**: `post_slave_raid/geiseler_1883/Geiseler_1883_German.pdf`
**Tags**: post-slave-raid-ethnography, political-authority, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: SMS Hyäne visit, September 19-23, 1882. German original (Fraktur OCR); English translation (Ayres & Ayres 1995) not yet in repo. Population 150. Political collapse total: no king, "old chief" without power, every man his own master. Former regime described as "almost despotic" with succession to BROTHER (contradicts Thomson and Roussel). Kings served as priests. CRITICAL: Salmon served as translator here AND for Thomson (1886), so convergence may reflect Salmon's framework. Rongorongo known only to kings and chiefs.

## Routledge 1919 (*The Mystery of Easter Island*)
**File**: `post_slave_raid/routledge_1919/Routledge_1919.pdf`
**Tags**: post-slave-raid-ethnography, political-authority, chiefdom-attribution, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: Most extensive early ethnography; Katherine Routledge, Mana Expedition, 17 months (1914-1915). Population ~250. First account NOT filtered through Salmon. "No chiefs nor any form of government" except Miru (p. 224). Ariki-mau explicitly "neither a leader in war, nor the fount of justice, nor even a priest" (p. 242); unable to compel his own servant; captured and enslaved. Tangata manu: food gifts "the sole practical advantage of victory" (p. 264). Ao system rotated clan dominance annually. Matatoa/matakio as rotating statuses, not permanent classes. No king list provided; genealogies contradictory. No kio class, no priests, no tribute, no redistribution.

## Thompson 1891 (*Te Pito te Henua, or Easter Island*)
**File**: `post_slave_raid/thompson_1891/Thompson_1891.pdf`
**Tags**: post-slave-raid-ethnography, political-authority, chiefdom-attribution, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: Most extensive 19th-century account. Paymaster Thomson, USS Mohican, 12 days in December 1886. Population 155. "Government" section describes "arbitrary monarchy" but simultaneously states no tax, no great homage, independent clans. King list of 57 names irreconcilable with Roussel's 22 (only ~12 overlap). Tangata manu: "no especial authority" vested in winner, contradicting Roussel. Primary source for the "arbitrary monarchy" framing later absorbed into chiefdom models. Traditions filtered through Salmon as translator; Ure Vaeiko could not actually read tablets.

## Altman n.d. (*Escape from Easter Island*)
**File**: `post_slave_raid/altman_2004/Altman-nd-EscapeFromEasterIsland.pdf`
**Tags**: (book review, not processed)
**Pipeline**: index only
**Notes**: Book review of Mieth & Bork ecology book. Not a primary source; filed but not processed through pipeline.
