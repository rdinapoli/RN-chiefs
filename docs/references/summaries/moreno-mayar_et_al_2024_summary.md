# Summary: Moreno-Mayar et al. 2024

**Source**: Moreno-Mayar JV, Sousa da Mota B, Higham T, Klemm S, Gorman Edmunds M, Stenderup J, Iraeta-Orbegozo M, Laborde V, Heyer E, Torres Hochstetter F, Friess M, Allentoft ME, Schroeder H, Delaneau O, Malaspinas A-S. 2024. Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas. *Nature* 633: 389-397. https://doi.org/10.1038/s41586-024-07881-4

---

## Overview

This paper presents the first high-quality ancient whole-genome data from Rapa Nui. The authors sequenced 15 ancient individuals (0.4-25.6x coverage) from petrous bone and teeth held at the Museum national d'Histoire naturelle in Paris, collected by Alphonse Pinart in 1877 (11 individuals) and Alfred Metraux in 1934-1935 (4 individuals). Radiocarbon dates place these individuals between 1670 and 1950 CE, but museum collection dates confirm they predate the 1860s Peruvian slave raids and subsequent demographic catastrophe. The study addresses two contested questions: whether Rapa Nui experienced a self-inflicted population collapse in the 1600s (the ecocide theory), and whether Polynesian ancestors of the Rapanui had pre-European contact with Native Americans.

The central findings are: (1) the genomic data reject a scenario of severe population collapse in the 1600s, instead supporting steady population growth from initial colonization through European contact; (2) all ancient and present-day Rapanui carry approximately 10% Native American ancestry from a single admixture event estimated at 1250-1430 CE, predating European arrival; and (3) European-like ancestry is present in modern but absent from ancient Rapanui, confirming the ancient sample represents the pre-contact gene pool.

## Methods

The study employs multiple analytical frameworks:

- **Effective population size reconstruction** using HapNe-LD (linkage disequilibrium-based) to infer population size trajectories over the last 100 generations.
- **Coalescent simulations** using msprime to model population histories with two bottlenecks (founding and proposed collapse) across a grid of timing, strength, and growth rate parameters, comparing simulated and observed HapNe-LD curves.
- **ROH analysis** using hapROH and PLINK to characterize the distribution of runs of homozygosity, distinguishing between chronically small populations (many short ROH) and recently bottlenecked ones (long ROH).
- **ADMIXTURE analysis** and f-statistics to determine ancestry proportions and genetic affinities.
- **IBD sharing** to assess relatedness and population affinities.
- **ALDER, DATES, and local ancestry inference** to date and characterize the Native American admixture event.
- **Bayesian modeling** integrating genetic admixture dates with radiocarbon dates to estimate the timing of trans-Pacific contact.

Community engagement with the Rapanui community (CODEIPA and CAMN) was conducted throughout the study, with both commissions voting in favor of the research.

## Key Findings

### No evidence for 1600s population collapse

The HapNe-LD effective population size curve shows a decreasing population size reaching a minimum approximately 28 generations (about 800 years) before the ancient individuals' births, corresponding to the founding bottleneck, followed by steady increase. No second decline is detected. Coalescent simulations across a parameter grid reject models with a strong or intermediate second bottleneck (Sb2 <= 50%, P < 10^-5). The SROH distribution likewise does not match strong bottleneck scenarios (Sb2 <= 0.2). The authors conclude: "These results do not support a major population collapse on Rapa Nui after its initial peopling and before the 1800s. Rather, they suggest that the island was home to a small population whose effective size steadily increased after initial peopling of the island until the 1860s" (p. 393).

### ROH pattern: chronically small, not recently collapsed

Ancient Rapanui carry extensive ROH compared to continental populations (average 198 cM vs. 25 cM for Eurasia), but these are predominantly short (<12 cM, 80% of total). Long ROH, which would indicate recent severe inbreeding from a population crash, are absent. This pattern is diagnostic of a population that has been small for many generations, not one that recently collapsed from a larger size.

### Population trajectory consistent with contact-era estimates

The contact-era population estimates of 1,500-3,000 are shown to be compatible with steady growth from a small founding population under pre-industrial growth rates, without requiring a prior larger population that collapsed. The effective population size remained low throughout the past 1,000 years while increasing monotonically.

### Native American admixture: pre-European, single event

All 15 ancient and 8 present-day Rapanui carry approximately 10% (6-12.4%) Native American-like ancestry. European-like ancestry is absent from ancient individuals but present in modern Rapanui. Using Bayesian modeling integrating genetic and radiocarbon data, the admixture is dated to 1246-1425 CE (95.4%), overlapping with the most recent colonization estimates (1150-1280 CE). The Native American source population is most closely related to Pacific Coast South Americans (Central Andean Highlands), not North Americans or populations east of the Andes.

### Colonization timing

The genetic evidence is consistent with colonization around 1250 CE, overlapping with current archaeological estimates (1150-1280 CE). The admixture event may have occurred shortly after or around the time of initial peopling.

### Low inbreeding, no close kin

No first- or second-degree relatives were found among the 15 ancient individuals. Inbreeding coefficients were <0.01 for all pairs. One pair of third- to fourth-degree relatives was detected. These patterns are consistent with a small but not critically endangered population that maintained kin-avoidance norms in mating.

## Relevance to the Chiefdom and Collapse Questions

### What it demonstrates

1. **The ecocide collapse narrative lacks genomic support.** The proposed population crash from 15,000 to 1,500-3,000 in the 1600s is rejected by multiple independent genomic analyses. The population grew steadily from colonization through European contact. This removes the demographic catastrophe that anchors the standard narrative of chiefdom rise, overexploitation, and societal collapse (Diamond 2005; Kirch 2017).

2. **The contact-era population was probably not a collapsed remnant.** If 1,500-3,000 represents normal growth from a small founding population, then the entire explanatory apparatus built around explaining a population decline (resource overexploitation, warfare, famine, moai-building madness) is addressing a problem that may not have existed.

3. **A chronically small population complicates chiefdom attributions.** While effective population size does not translate directly to census size, the consistently low Ne throughout Rapa Nui's history raises questions about the demographic base required for the redistributive chiefdom organization attributed to the island. Complex chiefdoms in the comparative Polynesian literature (Hawaii, Tonga) operated with substantially larger populations.

4. **Late colonization is confirmed by an independent data source.** Genetic evidence supports colonization around 1200-1250 CE, consistent with Hunt and Lipo (2006) and DiNapoli et al. (2021). The compressed chronology (roughly 500 years from colonization to European contact) further constrains the time available for developing the elaborate political hierarchy attributed to Rapa Nui.

5. **Pre-contact genetic isolation.** After the single early admixture event with Native Americans, the Rapanui population appears genetically isolated for centuries before European contact. This isolation, combined with Rapa Nui's distinctive ecology, weakens the basis for assuming that political developments tracked those of better-connected Polynesian societies.

### What it does not demonstrate

1. **The paper does not address political organization.** It is a population genetics study. It makes no claims about chiefdoms, social hierarchy, leadership, or governance.

2. **It cannot determine census population size.** The relationship between effective and census population size is complex and the authors explicitly decline to translate Ne into census numbers. A population of 3,000 or even 1,500 could in principle support some form of hierarchical organization.

3. **It does not deny environmental change.** Deforestation and ecological transformation are not disputed. The paper rejects only the claim that these changes caused a demographic collapse. Advocates of the chiefdom model could argue that political organization changed (from chiefdom to something else) without a population crash, though this would require abandoning the standard ecocide framing.

4. **The ROH and Ne analyses provide trajectory information, not absolute numbers.** The finding is about the shape of the population history curve (no collapse), not about the precise population count at any given time.

5. **The Native American admixture, while dated to pre-European times, does not resolve the direction or mechanism of contact.** Whether Polynesian voyagers reached South America, South Americans reached Polynesia, or both, remains undetermined.

## Relationship to Other Sources in This Project

- **DiNapoli et al. 2021 (Nat. Commun.)**: The population resilience finding from Bayesian radiocarbon modeling is independently confirmed by the genomic data. Both approaches reject the collapse scenario and support steady growth.

- **Hunt and Lipo 2006/2011**: The late colonization date and the rejection of the ecocide narrative are consistent with Hunt and Lipo's longstanding critique. The genomic data provide an independent biological line of evidence supporting their position.

- **Diamond 2005; Kirch 2017**: The ecocide narrative that structures these accounts is directly challenged. The proposed population collapse from 15,000 to a few thousand, which these authors attribute to resource overexploitation under chiefly mismanagement, finds no support in the genomic record.

- **Contact-era accounts (Roggeveen 1722, Cook 1774, La Perouse 1786)**: The contact-era population estimates of 1,500-3,000 are reinterpreted as reflecting normal population levels, not a post-collapse remnant. This means these accounts may be describing a population at or near its historical peak, not one that had recently crashed.

- **Post-slave-raid sources (Thompson 1891, Routledge 1919, Metraux 1940)**: The paper confirms that the 1860s slave raids and epidemics were the real demographic catastrophe, reducing the population to approximately 110. The ancient genomes predate this event and are uncontaminated by it. This reinforces the distinction between the well-documented post-1860s collapse and the hypothesized (and now genomically unsupported) pre-contact collapse.

- **Mulrooney 2013**: The settlement continuity finding from radiocarbon analysis is complementary. Where Mulrooney showed no evidence of inland abandonment (predicted by the collapse model), Moreno-Mayar et al. show no evidence of population decline. Together, these independent lines of evidence converge on the same conclusion: the 1600s collapse did not occur.
