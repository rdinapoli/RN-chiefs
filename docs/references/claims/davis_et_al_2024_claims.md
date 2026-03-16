# Claims Extraction: Davis et al. 2024

**[OWN WORK]**

**Source**: Davis DS, DiNapoli RJ, Pakarati G, Hunt TL, Lipo CP. 2024. Island-wide characterization of agricultural production challenges the demographic collapse hypothesis for Rapa Nui (Easter Island). *Science Advances* 10, eado1459. https://doi.org/10.1126/sciadv.ado1459

**Type**: Peer-reviewed research article (remote sensing, agricultural extent, population modeling)
**Accessed**: PDF (`davis_et_al_2024.pdf`)
**Extracted**: 2026-03-16

---

## I. Core Argument and Framing

1. "Rapa Nui (Easter Island) is often used as an example of how overexploitation of limited resources resulted in a catastrophic population collapse. A vital component of this narrative is that the rapid rise and fall of pre-contact Rapanui population growth rates was driven by the construction and overexploitation of once extensive rock gardens." (p. 1, abstract)

2. "We show that the extent of this agricultural infrastructure is substantially less than previously claimed and likely could not have supported the large population sizes that have been assumed." (p. 1, abstract)

3. "Our findings indicate that the prevalence of rock gardening is approximately one-fifth of the most conservative previous estimates (26) that Puleston et al. (6) used to estimate population sizes." (p. 2)

**Assessment**: This is the paper's headline finding. If the agricultural base was one-fifth of prior estimates, the carrying capacity calculations that supported population overshoot narratives were based on grossly inflated inputs.

---

## II. Rock Gardening Extent

### Previous estimates vs. new estimates

4. "To date, the only island-wide estimate for ancient rock gardening activity comes from the work of Ladefoged et al. (26). Using near-infrared (NIR) bands from Worldview-2 satellite images, they estimated that between 4.9 and 21.1 km^2 of the island's total 163.6 km^2 area was covered by rock gardens." (p. 1)

5. "However, as Ladefoged et al. (26) report, the accuracy of this estimation is low (Table 1)." (p. 2)

6. Ladefoged et al.'s MLC classifier achieved recall of 0.319-0.337, precision of 0.671-0.753, F1 of 0.443-0.449, overall accuracy of 0.588-0.609, and Kappa coefficients of only 0.17-0.22. (Table 1, p. 3)

7. "The resulting dataset contains a total of 0.76 km^2 of rock gardens across Rapa Nui (Fig. 1)." (p. 3)

8. "Ladefoged et al.'s (26) mulching estimates ranged from 4.3 to 21.1 km^2. Our study estimates indicate that the total area of rock gardening is 0.76 km^2, approximately one-fifth of the most conservative previous estimates." (p. 4)

**Assessment**: The discrepancy is enormous: 0.76 km^2 vs. 4.3-21.1 km^2. This is not a marginal revision but an order-of-magnitude reduction that cascades through all downstream carrying capacity and population models.

### Sources of error in previous estimates

9. "Previous island-wide estimates of rock gardening distribution contain numerous examples of false positives and negatives that were not replicated in this study using SWIR (Fig. 3). Additionally, the urban part of the island could have had rock mulch that has since been destroyed." (p. 6)

10. "The data produced by Ladefoged et al. (26) present numerous cases where areas identified as rock gardens are modern roads, natural lava flows, and vegetation (Fig. 3). Thus, their analysis likely greatly overestimates the amount of ancient rock gardening on Rapa Nui." (p. 2)

11. "The misidentifications in Ladefoged et al.'s (26) analysis are likely due, in part, to the imagery data available at the time from the Worldview-2 satellite. These images provide nine bands of spectral data with wavelengths between 0.45 to 1.04 μm. The NIR bands (0.77 to 1.49 μm) are of particular value for measuring cultivation features as they tend to reflect differences in light absorption due to varying abundance of water. These bands, however, cover a relatively narrow range of the infrared spectrum (i.e., between 0.7 and 1000 μm)." (p. 3)

### Methodological improvement

12. "In all cases, SWIR data perform better than VNIR at identifying rock gardens and classifying the landscape of Rapa Nui. Combining VNIR with SWIR did not improve results." (p. 3)

13. The best-performing model (SWIR, maximum entropy classifier) achieved recall of 0.834, precision of 0.827, F1 of 0.830, overall accuracy of 0.8244, and Kappa coefficient of 0.7865. (Table 2, p. 4)

14. "When examining MaxEnt results for rock gardening classes, specifically, the model attained a true positive rate of over 78% and a true negative rate of over 96%, meaning that there is a low rate of error both for excluding real rock gardening features and from misidentifying other landscape components as rock gardens." (p. 6)

**Assessment**: The new method substantially outperforms the previous one across all metrics. The high true negative rate (>96%) is particularly important: it means the low rock garden estimate is unlikely to be explained by the classifier missing real gardens.

### Spatial distribution of rock gardens

15. "The overall location and density of gardens are similar to those of earlier studies, primarily clustered along coastal regions and largely absent further inland at higher altitudes (Fig. 5)." (p. 6)

16. "Most rock gardens are clustered near the coast, and over 5 km^2 of the cultivated areas are in zones where no rock gardens have been discovered during ground investigations or remote sensing surveys." (p. 6)

---

## III. Agricultural Systems and Food Production

### Rock gardening practices

17. "Rock gardening (sometimes referred to as lithic mulching) is a term for adding rocks to cultivation areas (Fig. 2). The practice of rock gardening can be found worldwide (16-19). On Rapa Nui, rock gardening practices take three different forms (15). First, 'veneer gardens' comprise a layer of fist-sized rocks placed directly on the surface. Second, lithic mulching adds broken rock material into the first 20 to 25 cm of soil. Third, boulder gardens include additional large stones on the surface." (p. 1)

18. "Overall, rock gardening increases productivity in a variety of ways (20). First, placing rocks on the surface can protect plants by generating more turbulent airflow over the garden surface...Second, the disrupted airflow also limits the wind, which can desiccate foliage while providing shade to reduce soil moisture evaporation. Third, by mediating the climate, rock gardening can contribute to the enhancement of nutrient-poor soils by reducing nutrient leaching (15, 22)." (p. 1)

19. "The placement of freshly broken rocks can increase the productivity of the soil by exposing unweathered surfaces and sources of minerals. Given its high surface-to-volume ratio, Stevenson et al. (15) suggest that pulverized rock has the most potential to add nutrients." (p. 1)

### Non-rock-garden food sources

20. "Nearly half of the Rapanui diet consisted of terrestrial foods (24, 25). In this regard, measuring the extent of rock gardens is critical for understanding the island's pre-contact environmental carrying capacity." (p. 1)

21. "Dietary estimates suggest that ~35 to 45% of the Rapanui diet was from marine sources (24). Because of low soil quality and other climatic considerations, additional crops like banana, yams, taro, and sugar cane were not optimal crops for maximizing caloric returns but did serve as a supplement to the Rapanui diet (11, 25). Thus, the impact of these crops on population sizes is likely to have been small, introducing dietary variety but limited increase to carrying capacity." (p. 6)

### Swidden cultivation

22. "Past Rapanui communities initially mitigated problems of the island's poor soil productivity by burning the native palm vegetation (9), a practice common in swidden cultivation. Over time, however, local communities also began to increasingly engage in a cultivation strategy known as 'lithic mulching,' a form of rock gardening (1, 4, 10-14)." (p. 1)

**Assessment**: The sequence from swidden to lithic mulching is important context: rock gardening was an intensification strategy adopted as deforestation proceeded, not the initial agricultural system. This complicates any model that treats rock garden extent as a proxy for total food production.

---

## IV. Population Size Estimates

### Puleston et al. population models

23. "Puleston et al. (6) rely on estimates of sweet potato yields to approximate the pre-European contact population size of Rapa Nui and report that 1 ton/year of sweet potato produces a yield of 2809 kcal/day. Using their reported values for caloric requirements for the population (maximum of 2785 kcal per day per person) and their calculated yields of sweet potato (tons per hectare per year), they conclude that population sizes on Rapa Nui could have exceeded 16,000 [Table 3; also see (6)]." (p. 5)

24. "In contrast, baseline estimates of the population size using our new rock gardening data suggest that population sizes could not have exceeded 4000 (Table 3)." (pp. 5-6)

**Assessment**: The maximum population estimate drops from >16,000 to <4,000, a fourfold reduction, simply by correcting the agricultural extent input. This is not a modeling disagreement; it is a data correction that propagates through any population model that uses rock garden extent as an input.

### Revised carrying capacity estimates

25. "The average carrying capacity of rock gardening calculated in this study is ~2000. If we add 50% to this estimate to account for marine and additional terrestrial foods from nonmulched areas, we arrive at an estimated carrying capacity of ~3000 people. This value matches historical accounts of population size at the time of European arrival in the 18th century (44, 45)." (p. 6)

26. "Nevertheless, the arguments made by previous studies [e.g., (6)] rely on estimates of rock gardening features to model pre-European contact population sizes. Our revised rock gardening estimates use the same logic but conclude that the range of possible population sizes supported by rock gardening infrastructure on Rapa Nui is significantly lower than previous estimates. Our estimates suggest that the maximum population supported by rock gardening is not ~17,000 as claimed through Ladefoged et al.'s (26) rock gardening calculations but just 3901 using our measurements." (p. 6)

**Assessment**: The convergence between the estimated carrying capacity (~3,000) and the contact-era population estimates (~3,000) is a key finding. It removes the supposed gap between carrying capacity and actual population that was the foundation of the Malthusian overshoot narrative.

### Table 3 summary of population estimates (p. 5)

27. Using rock garden area from this study (76 ha), population estimates under various cultivation scenarios range from:
- Continuous, low N: 1,119 individuals
- Continuous, high N: 3,901 individuals
- Shifting (5/5), low N: 912 individuals
- Shifting (5/5), high N: 3,066 individuals
- Shifting (15/3), low N: 716 individuals
- Shifting (15/3), high N: 2,248 individuals

Compared with estimates using Ladefoged et al. (26) rock garden area (3,133.9 ha for continuous; 1,566.9 ha for 5/5 shifting; 522.3 ha for 15/3 shifting), which yielded ranges from 2,955 to 16,089 individuals.

### Limitations of population estimates

28. "It is essential to clarify that these estimates are based solely on sweet potatoes and refer to the population that could, theoretically, have been supported by rock gardening infrastructure alone. However, additional sources of subsistence (like marine foods and other terrestrial crops like bananas, yams, taro, and sugar cane) would have increased the island's carrying capacity." (p. 6)

29. "In addition to the impacts of crops grown outside of rock gardening and mulched areas, varied annual and seasonal growing conditions and changes to the amount of land used for cultivation over time are important considerations when estimating carrying capacity. Thus, further work is needed to model pre-European contact population sizes on Rapa Nui comprehensively and goes beyond this study's scope." (p. 6)

---

## V. The Ecocide/Collapse Narrative

### Direct challenge to Malthusian narrative

30. "Malthusian assumptions are prevalent in a wide range of studies that point to the pre-European contact population size of the island, drawing on previous rock gardening estimates that inflate the land area used for cultivation (6, 46, 49, 54). Recent research has attempted to estimate the pre-European population size on the island using previous evaluations of lithic mulching, with estimates varying widely from ~3000 to more than 17,000 people (6). While an argument for a population size of 17,000 is problematic (5, 55), the overestimation of lithic mulching, as demonstrated by our new estimates, warrants revisiting environmental carrying capacity and population estimates for Rapa Nui (Table 3)." (p. 7)

31. "Despite recent archaeological literature debunking ideas about Malthusian population overshoot, the premise that Rapanui society caused its own demise from unsustainable resource use and uncontrolled population increases has been widely popularized. While many researchers working on the island have shifted their narratives away from the assumptions of a pre-European collapse, the story remains prominent in disciplines such as ecology, paleoecology, and mathematics (49, 54)." (p. 7)

32. "Our results add to a growing body of empirical research showing that Rapa Nui represents a prime example of how an isolated population with limited natural resources created a sustainable subsistence system, maintaining their numbers within the limitations of environmental carrying capacity (55). Contrary to popularized narratives about a runway population size that overexploited natural resources (37, 46), our results suggest that significant demographic increases ('overshoot') did not occur in the past, given the limited extent of agricultural infrastructure." (p. 7)

**Assessment**: This is a strong, direct rebuttal of the ecocide/collapse narrative. The argument is that the agricultural base was never large enough to support the inflated population estimates that the overshoot model requires. If the population never exceeded ~3,000-4,000, there was no overshoot and no resource-driven collapse.

33. "Contrary to popularized narratives about a runway population size that overexploited natural resources (37, 46), our results suggest that significant demographic increases ('overshoot') did not occur in the past, given the limited extent of agricultural infrastructure. Using high-resolution SWIR imagery and machine learning, we detect rock gardens across Rapa Nui's landscape with an accuracy of >80%. On Rapa Nui, our results help refine estimates of agricultural productivity, suggesting that previous estimates were between 5 and 20 times too high." (p. 7)

### Concordance with contact-era population estimates

34. "We demonstrate that the extent of rock gardening cultivation found in the occupied coastal areas comports with estimates of the population from observations made by early European visitors to the island in the 18th century, which is about 3000 (36)." (p. 2)

**Assessment**: The alignment between the new carrying capacity estimate and European contact-era population estimates removes the core premise of the collapse model: that the population once far exceeded what the island could support.

---

## VI. Preservation and Destruction of Rock Gardens

35. "In assessing the extent of rock gardening destruction that urbanization and modern agriculture may have caused, we estimate that ~25 km^2 of the island has been affected. This estimate excludes the Poike Peninsula on the island's eastern side...Of this ~25 km^2, >5 km^2 of the cultivated areas are in zones where no rock gardens have been discovered during ground investigations or remote sensing surveys...Most (~17 km^2) fall within or adjacent to Hanga Roa, the principal modern settlement on Rapa Nui." (p. 4)

36. "Such preservation issues present substantial challenges to archaeologists, and this study is no exception. Using modern (2015 to 2017) satellite observations means that features that have been destroyed are no longer identifiable using these approaches alone, and ground-based analysis is required to verify further or to challenge our conclusions." (p. 6)

37. "Still, we suspect that the destruction is limited as most developed areas would not have had rock gardening infrastructure due to their location on the island (Fig. 4). Most rock gardens are clustered near the coast, and over 5 km^2 of the cultivated areas are in zones where no rock gardens have been discovered during ground investigations or remote sensing surveys." (p. 6)

38. "Nonetheless, our results require careful interpretation, as the total amount of rock gardening features may have been higher than what is reported but have since been destroyed. Furthermore, it is important to emphasize that not all of the rock gardens identified here were necessarily contemporaneous; some of these fields may be older than others, and the total amount of rock gardening infrastructure may have been significantly different or was more limited in extent at different points in the island's history." (p. 6)

**Assessment**: The authors acknowledge the possibility that some rock gardens have been destroyed by modern development, but argue the destruction is likely limited because most developed areas were not in zones where rock gardens were concentrated. The non-contemporaneity point is important: 0.76 km^2 is a cumulative figure across the entire occupation, and the active area at any given time may have been smaller still.

### Temporal non-contemporaneity

39. "Prior estimates of rock gardening infrastructure relied on satellite imagery from 2010 (26), and as such, our results are comparable despite the possible bias caused by the destruction of archaeological features. Furthermore, previous estimates of rock gardening excluded 45 km^2 of land area from analysis due to cloud coverage and urban and agricultural infrastructure. Therefore, we investigated a greater proportion of the island's land mass (due to SWIR's ability to penetrate cloud cover) and greatly improved the accuracy of rock gardening estimates." (p. 7)

---

## VII. Implications for Carrying Capacity Models

40. "Since rock gardening was significantly less prevalent than previously assumed, the island's carrying capacity would also be substantially less than previous claims, even under optimistic assumptions of high productivity." (p. 4)

41. "These estimates are based solely on sweet potatoes and refer to the population that could, theoretically, have been supported by rock gardening infrastructure alone." (p. 6)

42. "Overall, our results are more likely to underestimate small gardens that cannot be seen in the 3.7-m SWIR imagery but are unlikely to have missed other rock gardening features." (p. 6)

---

## VIII. Bearing on Chiefdom Attribution and Political Organization

### Indirect relevance

The paper does not directly address political organization or the chiefdom concept, but its findings undermine the demographic foundations that chiefdom models have been built upon in several ways:

43. The collapse/ecocide narrative is often coupled with the chiefdom model: the standard account holds that chiefly competition drove monument construction, which required deforestation, which led to agricultural intensification through rock gardening, which initially supported population growth, but eventually the system collapsed due to overexploitation. If the agricultural base was never extensive enough to support the large populations this model requires, the entire sequence unravels.

44. Population estimates of 15,000-17,000 have been used to argue for the degree of social complexity and centralized authority needed to manage such a large population on a small island. If the actual population was ~3,000, the organizational demands on political institutions would have been qualitatively different, and the case for chiefly administration of agricultural production weakens considerably.

45. The finding that rock gardens are primarily coastal and not widespread across the island's interior challenges models that posit chiefly territorial control over extensive inland agricultural zones (cf. Stevenson and colleagues' arguments about elite management of agricultural field systems).

---

## IX. Remote Sensing Methodology

46. "Here, we use shortwave infrared (SWIR) satellite imagery and machine learning to generate an island-wide estimate of rock gardening and reevaluate previous population size models for Rapa Nui." (p. 1, abstract)

47. "This study uses archaeological field identifications of rock garden features to train machine learning models to analyze island-wide SWIR data from the Worldview-3 satellite." (p. 2)

48. The SWIR spectrum (1.195-2.365 μm) is "particularly useful for geologic applications because of its ability to distinguish between dry and wet soils, as water is absorbed in the SWIR spectrum, and their reflectance or absorption characteristics can distinguish different minerals." (p. 7)

49. Three machine learning classifiers were tested: maximum entropy (MaxEnt), random forest (RF), and maximum likelihood classification (MLC), using an 80-20 training/validation split. (p. 8)

50. "The results of the maximum entropy model applied to the 3.7-m SWIR imagery were exported to ArcGIS for manual evaluation and cleaning, wherein we assessed the model output and removed any obvious errors by hand to produce an estimate of rock garden distribution. This step required approximately 2 hours of analyst time." (p. 3)

---

## X. Summary of Claims Relevant to Chiefdom Attribution

Davis et al. 2024 does not directly address political organization, but its findings have cascading consequences for the chiefdom-collapse model:

1. **The agricultural base was far smaller than assumed.** Rock garden extent is 0.76 km^2, approximately one-fifth of the most conservative prior estimate and less than 4% of the maximal estimate. All downstream carrying capacity and population models that used the prior estimates require revision.

2. **Population estimates drop dramatically.** Maximum population supportable by rock gardening drops from ~17,000 to ~3,900 (and more realistic scenarios yield ~2,000-3,000). This aligns with contact-era European population estimates of ~3,000.

3. **No evidence of Malthusian overshoot.** If the population never greatly exceeded ~3,000, there was no overshoot, no resource crisis, and no population collapse driven by agricultural overexploitation. The ecocide narrative loses its demographic foundation.

4. **The carrying capacity matched the contact-era population.** This convergence suggests the Rapanui maintained a sustainable subsistence system within environmental limits, rather than exceeding them.

5. **Implications for chiefly agricultural management.** Models positing elite control over extensive agricultural territories are weakened by the finding that the rock garden system was limited and concentrated in coastal areas, not spread across the interior under chiefly administration.

6. **Non-contemporaneity of gardens.** The 0.76 km^2 figure is cumulative; the active cultivated area at any given time may have been smaller, further reducing instantaneous carrying capacity estimates.
