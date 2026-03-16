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

## Métraux 1937 ("The Kings of Easter Island")
**File**: `post_slave_raid/metraux_1937/Metraux_1937.pdf`
**Tags**: post-slave-raid-ethnography, political-authority, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: Focused article on kingship. Independent confirmation that ariki-mau had no political power. "Certainly not a ruler or civilian chief." Strongest source assessment of all post-raid ethnographers, directly evaluating Roussel, Thomson, and Geiseler. Dismisses Roussel's claim of ancient absolute power as "entirely gratuitous assumption." Documents food flowing through king to tangata-honui (elite-to-elite, not downward redistribution).

## Métraux 1937 ("Easter Island Sanctuaries")
**File**: `post_slave_raid/metraux_1937_sanctuaries/Metraux_1937_Sanctuaries.pdf`
**Tags**: archaeological-evidence, monument-production, settlement-patterns
**Pipeline**: claims / summary / evidence / index
**Notes**: Most detailed analytical study of ahu architecture, typology, and construction from the early 20th century. Four-type ahu classification, construction techniques, distribution patterns. Comprehensive treatment of statue transport with Polynesian parallels. Walking statues legend dismissed as myth; Roussel's alternative (each tribe dragging its family gods to its district) implies decentralized, clan-level organization. Contains NO claims of chiefly command over monument construction. Significant absence from the ethnographer who wrote the most detailed ahu study.

## Métraux 1940 (*Ethnology of Easter Island*)
**File**: `post_slave_raid/metraux_1940/Metraux_1940.pdf`
**Tags**: post-slave-raid-ethnography, political-authority, chiefdom-attribution, circularity, monument-production
**Pipeline**: claims / summary / evidence / index
**Notes**: Most comprehensive ethnographic monograph on Easter Island (Bishop Museum Bulletin 160, 463 pages). Confirms 1937 article: ariki-mau "certainly not a ruler or civilian chief" (p. 136). King list comparison (Table 2, pp. 88-93) shows only 7 names common to all four independently recorded lists; shared names are tribal eponyms, not historical individuals. Roussel's four-class hierarchy "only superficially exact"; matatoa identified as "actual rulers of the tribes"; kio were war captives, not hereditary caste. Stone image significance: "no direct evidence that they were ever worshipped"; "tribal pride and competitive instinct" as motivation. Bird cult: tangata manu coexisted with but separate from ariki-mau; privileges limited to marauding and food extraction.

## Métraux 1957 (*Easter Island: A Stone-Age Civilization of the Pacific*)
**File**: `post_slave_raid/metraux_1957/Metraux_1957.pdf`
**Tags**: post-slave-raid-ethnography, political-authority, monument-production
**Pipeline**: claims / summary / evidence / index
**Notes**: Popular synthesis of the 1940 monograph. Contains Métraux's clearest formulations: ariki-mau political authority "not clear"; matatoa had "much stronger" political position than Polynesian warriors elsewhere (caudillo analogy); statue transport organized by "heads of lineages" through competitive feast sponsorship ("immense pleasure party"); statues became "noa—profane" without active ritual. No evolution toward chiefdom model between 1940 and 1957.

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

---

## McCoy 1976 (*Easter Island Settlement Patterns*)
**File**: `mccoy_1976.pdf`
**Tags**: settlement-patterns, chiefdom-attribution, archaeological-evidence, circularity
**Pipeline**: claims / summary / evidence / index
**Notes**: First comprehensive settlement pattern analysis for Rapa Nui. Often miscited as applying chiefdom framework; McCoy actually concluded chiefdom development was "retarded" by warrior class ascendancy (p. 145). Explicitly projects ethnohistoric data back in time as interpretive baseline (p. 70), documenting the circularity this paper identifies. Describes ranked society under stress, not a consolidated chiefdom. Notable: Sahlins himself treated Easter Island as an exception to his model (p. 152). Anticipates DiNapoli et al. 2019 freshwater-settlement finding (p. 142).

## Robinson & Stevenson 2017 ("The Cult of the Birdman: religious change at 'Orongo, Rapa Nui")
**File**: `robinson_stevenson_2017.pdf`
**Tags**: archaeological-evidence, political-authority, contact-era, circularity
**Pipeline**: claims / summary / index
**Notes**: Reassesses 'Orongo chronology using radiocarbon and obsidian hydration data. Conventional date of c. AD 1540 for stone house construction rests on unreliable bulk charcoal; revised timeline places peak activity at AD 1795 and hypothesized house construction c. AD 1800. Birdman Cult formalization is a contact-period phenomenon. Paramountcy "has not been discovered archaeologically or reported in the ethnohistoric oral history" (p. 90). Causal chain from ecological stress to cult emergence acknowledged as lacking empirical support. Relies on Metraux 1940 (post-slave-raid) for political characterization without critical assessment.

## Pollard et al. 2010 ("*Te Miro o'one*: the archaeology of contact on Rapa Nui")
**File**: `pollard_et_al_2010.pdf`
**Tags**: contact-era, archaeological-evidence, political-authority, circularity
**Pipeline**: claims / summary / index
**Notes**: Archaeology of European contact, 1722-1868. Key claims: birdman cult (*tangata manu*) replaced hereditary chiefly authority with performative warrior-leadership (p. 566); 'Orongo chronology insecure, stone structures potentially post-contact (p. 567); moai toppling may be contact-driven, triggered by Gonzalez 1770 visit (p. 569); geographic differentiation in rock art suggests competing groups, not unified polity (p. 574); total European contact before 1795 was approximately two weeks over 80 years (p. 567). Does not present new data but reinterprets existing material within contact-archaeology framework.

## DiNapoli et al. 2019 ("Rapa Nui monument (*ahu*) locations explained by freshwater sources")
**File**: `dinapoli_et_al_2019.pdf`
**Tags**: own-work, archaeological-evidence, settlement-patterns, collective-action
**Pipeline**: claims / summary / index
**Notes**: First formal spatial analysis of ahu placement relative to subsistence resources. Point-process modeling demonstrates ahu locations are most parsimoniously explained by proximity to freshwater sources (coastal groundwater seeps) and the coastline. Rock mulch gardens do not predict ahu locations; marine resource correlation is spurious once coastline and freshwater are accounted for. Challenges Kirch's marine-control and Stevenson's agricultural-territory interpretations. Framed through community-level costly signaling theory, not chiefly command. Monument construction did not require large labor forces.

## DiNapoli et al. 2020 ("A model-based approach to the tempo of 'collapse': The case of Rapa Nui")
**File**: `dinapoli_et_al_2020.pdf`
**Tags**: own-work, archaeological-evidence, monument-production, data-quality, critique
**Pipeline**: claims / summary / index
**Notes**: First formal Bayesian chronological model for ahu construction timing using tempo plots (Dye 2016). Integrates radiocarbon dates from 11 platform ahu with architectural stratigraphy. Central finding: ahu construction began early 14th to mid-15th centuries AD and continued at a steady rate through European contact in 1722 and into the post-contact era. No evidence for pre-contact cessation. Provides "important falsifying evidence that directly challenges core components of Rapa Nui's collapse narrative." Previous chronologies based on ad hoc SPD interpretation, not formal models. Tempo shows rapid onset then steady activity, not escalating competition followed by collapse. Construction framed as group-level community activity, not chiefly command.

## Mulrooney 2013 ("An island-wide assessment of the chronology of settlement and land use on Rapa Nui")
**File**: `mulrooney_2013.pdf`
**Tags**: archaeological-evidence, settlement-patterns, data-quality, critique
**Pipeline**: claims / summary / index
**Notes**: First island-wide radiocarbon chronology assessment for Rapa Nui (313 dates from archaeological contexts). Central finding: settlement and land use show continuity, not collapse. Inland agricultural areas (1-3.5 km from coast) were not abandoned prior to European contact, contradicting the collapse scenario tied to the "breakdown of the chiefly economy." Demonstrates calibration curve effects can mimic cultural disruption. Documents severe coastal sampling bias (72.8% of dates within 500 m of coast). Previous chronological models (including Stevenson's "Chiefdom Integration" phase) built on uncritically assessed dates. Settlement by at least AD 1200, broadly consistent with late colonization model.

## Lipo et al. 2013 ("The 'Walking' Megalithic Statues of Easter Island")
**File**: `lipo_et_al_2013.pdf`
**Tags**: own-work, monument-production, collective-action, archaeological-evidence
**Pipeline**: claims / summary / index
**Notes**: Walking moai experiment. Demonstrates vertical transport of a 4.35-ton scaled replica by 18 people with three ropes. Archaeological analysis of 62 road moai shows systematic shape differences from ahu moai consistent with engineering for vertical transport. Concave road cross-sections rule out rollers. Directly undermines the claim that moai transport required large labor forces under chiefly command: "activities by small-scale social groups rather than the product of laborers unified under a powerful centralized chiefdom" (p. 2866). No timber required; severs deforestation link. Scaling argument: larger moai proportionally easier to walk.

## Lipo et al. 2025 ("Megalithic statue (*moai*) production on Rapa Nui (Easter Island, Chile)")
**File**: `lipo_et_al_2025.pdf`
**Tags**: own-work, monument-production, collective-action, archaeological-evidence
**Pipeline**: claims / summary / index
**Notes**: First comprehensive 3D photogrammetric documentation of Rano Raraku quarry (11,686 UAV images, sub-cm resolution). Identifies 30 distinct quarrying foci with redundant production features and varied carving methods (face-outline, block, lateral), consistent with contemporaneous operation by multiple autonomous groups. Physical constraints limited active carvers to 4-6 per moai. Workshop boundaries follow natural bedrock features, not imposed barriers: no evidence of restricted access or centralized management. Standardized moai forms coexisted with organizational autonomy, demonstrating cultural convergence through horizontal information sharing without hierarchical oversight. Extends evidence for decentralized, clan-based organization from settlement, transport, and lithic patterns to the island's primary production center. "These findings challenge assumptions that monumentality requires hierarchical control" (p. 1).

## Davis et al. 2024 ("Island-wide characterization of agricultural production challenges the demographic collapse hypothesis for Rapa Nui")
**File**: `davis_et_al_2024.pdf`
**Tags**: own-work, archaeological-evidence, settlement-patterns, critique
**Pipeline**: claims / summary / index
**Notes**: SWIR satellite imagery and machine learning classification of rock garden extent. Rock gardens cover 0.76 km^2, approximately one-fifth of the most conservative prior estimate (Ladefoged et al. 2013). Maximum population supportable by rock gardening drops from ~17,000 to ~3,900; average carrying capacity ~2,000, rising to ~3,000 with marine and non-mulched foods. Matches contact-era population estimate of ~3,000. Directly challenges Malthusian overshoot/ecocide narrative: agricultural base was never extensive enough to support the large populations the collapse model requires. Rock gardens concentrated in coastal areas, not spread across interior under chiefly administration.

## Haoa Cardinali et al. 2017 (eds.) (*Cultural and Environmental Change on Rapa Nui*)
**File**: `haoa_et_al_2017.pdf`
**Tags**: archaeological-evidence, settlement-patterns, contact-era, political-authority, monument-production, circularity
**Pipeline**: claims / summary / index
**Notes**: Routledge edited volume (11 chapters). Key chapters: Boersema (Ch. 8) systematically reviews all four 18th-century expedition accounts and finds no evidence of collapse, warfare, or starvation; Richards (Ch. 9) documents prosperous whaling-era trade (1805-1862) and references to "King" and "chiefs"; Vogt and Kuhlem (Ch. 6) interpret Ava Ranga Uka A Toroke Hau as elite-controlled ritual complex (using Metraux 1940 analogy); Lee et al. (Ch. 7) assume chiefly command of monument construction as premise for pukao analysis; editors' reflections (Ch. 11) explicitly acknowledge collapse framework shapes interpretation of Orongo, ana kionga, and mata'a without adequate evidence.

## Moreno-Mayar et al. 2024 ("Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas")
**File**: `moreno-mayar_et_al_2024.pdf`
**Tags**: archaeological-evidence, data-quality, critique
**Pipeline**: claims / summary / index
**Notes**: First high-quality ancient whole-genome data from Rapa Nui (15 individuals, 0.4-25.6x, 1670-1950 CE). Multiple genomic analyses (HapNe-LD, coalescent simulations, ROH distributions) reject a 1600s population collapse. Population grew steadily from founding bottleneck through European contact. Contact-era estimates of 1,500-3,000 consistent with gradual growth, not post-collapse remnant. ~10% Native American admixture in both ancient and modern Rapanui dated to 1250-1430 CE (pre-European). No European admixture in ancient individuals. Late colonization (~1200-1250 CE) confirmed by independent genetic evidence. Directly undermines ecocide narrative; indirectly challenges demographic basis for chiefdom attribution.
