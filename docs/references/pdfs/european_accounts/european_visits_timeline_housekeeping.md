# European Visits to Easter Island (Rapa Nui) Before the Slave Raids

## 1. Roggeveen Expedition (1722) - Dutch
- **Date:** April 5, 1722 (Easter Sunday)
- **Ships:** Arend, Thienhoven, Afrikaansche Galei
- **Accounts:**
  - Jacob Roggeveen (commander) - official log/journal
  - Carl Friedrich Behrens (German soldier) - narrative published 1737
  - Cornelis Bouman (captain of the Thienhoven) - log
- **Notes:** First recorded European contact. Stayed approximately one week. Crew killed ~12 islanders shortly after landing. All moai reported standing.

## 2. González de Ahedo Expedition (1770) - Spanish
- **Date:** November 15-20, 1770
- **Ships:** San Lorenzo (ship of the line), Santa Rosalia (frigate)
- **Sent by:** Viceroy of Peru, Manuel de Amat
- **Accounts:**
  - Felipe González de Ahedo (commander) - ship log/journal
  - Pilot Hervé (pilot of the San Lorenzo) - narrative/derrota
  - Francisco Antonio de Agüera Infanzón (pilot of the Santa Rosalia) - journal
  - Additional officers' logs and reports from the expedition
- **Notes:** Claimed the island for Spain as "Isla de San Carlos." Spent five days. Erected three crosses on Poike. Created a Rapanui-Spanish dictionary of 88 words. Produced detailed coastal survey/map (likely by pilots Hervé and Agüera). All moai still standing. Primary source compilation: Bolton Glanvill Corney (ed./trans.), published by Hakluyt Society in 1908. Spanish originals compiled by Francisco Mellén Blanco (1986).

## 3. Cook Expedition (1774) - British
- **Date:** Mid-March 1774 (second voyage, HMS Resolution)
- **Accounts:**
  - James Cook (commander) - official voyage account (published 1777)
  - Georg Forster - *A Voyage Round the World* (published 1777, six weeks before Cook's account)
  - Johann Reinhold Forster (naturalist) - *Observations Made During a Voyage Round the World* (published 1778); also kept a detailed journal/manuscript
- **Notes:** Cook was ill during the visit and could not walk far. A small group explored the island. Reported some moai already toppled. No sign of the Spanish crosses. Botanist described it as "a poor land." Had a Tahitian interpreter (Hitihiti) who could partially understand the language.

## 4. La Pérouse Expedition (1786) - French
- **Date:** April 9-10, 1786
- **Ships:** La Boussole, L'Astrolabe
- **Accounts:**
  - Jean-François de Galaup, comte de La Pérouse (commander) - journal (published posthumously 1797, edited by M. L. A. Milet-Mureau)
  - M. Rollin (surgeon of La Boussole) - dissertation on inhabitants of Easter Island
  - Barthélemy de Lesseps (interpreter/officer on L'Astrolabe) - carried expedition records overland from Kamchatka to Paris; published his own travel account (1790)
- **Notes:** Spent approximately 11 hours on the island. Made a detailed map. Described the island as one-tenth cultivated, population ~2,000. Attempted to introduce domestic animals (hogs, goats, sheep) and plant seeds. Gardener declared "three days' work a year" would suffice to support the population. Confirmed existence of underground caves.

## 5. Post-La Pérouse Visits Before the Slave Raids (1793-1862)

By the 19th century, Easter Island became a common resupply stop. Rhys Richards (2008) documented 79 visits involving contacts ashore before the 1862 slave raids, of which 56 were by whaling ships.

### Notable visits:
- **1805** - American sealing ship *Nancy* (from New London). Kidnapped 22 islanders (12 men, 10 women) to use as seal-hunting labor. Captives jumped overboard three days out; crew shot at them. This event poisoned subsequent interactions with Europeans.
- **1806** - *Kaahou-Manou* (turned away by hostile islanders)
- **1816** - Otto von Kotzebue (Russian) on the brig *Rurik*. Met with hostility at Anakena. Wrote a published account: *A Voyage of Discovery* (1821). Learned from Alexander Adams at the Sandwich Islands about the 1805 Nancy incident, which explained the islanders' hostility.
- **1825** - Captain Frederick William Beechey (British) on HMS *Blossom*. Similar hostile reception. Published account of the visit.
- **1822-1862** - 51 American whaling ships visited, trading knives, nails, hoop iron, and whale-pot scraps for sweet potatoes, yams, bananas, and sugar cane.
- **1837** - Chilean schooner *Colo-Colo* under Leoncio Señoret (no report filed or found)
- Other brief visitors: Lisiansky, Amasa Delano, and many others whose journals provide limited information.

### Key reference for this period:
- Richards, Rhys. 2008. *Easter Island 1793 to 1861: Observations by Early Visitors Before the Slave Raids.* Los Osos: Easter Island Foundation.

---

## 6. Peruvian Slave Raids (1862-1863)
- **December 1862:** Eight Peruvian ships arrived. ~1,400+ Rapanui kidnapped (roughly one-third to one-half of the population), including the king, his son, and the ritual priests/wise men who could read rongorongo. Most died in Peru from disease and harsh labor. A handful were eventually returned, bringing smallpox, which devastated the remaining population.

---
---

# INSTRUCTIONS FOR CLAUDE CODE: PDF Source Inventory and Deduplication

## Context
There is a folder of PDFs containing primary and secondary source accounts from the European visits listed above. The goal is to build a clean, deduplicated reference library of these sources for a research project.

## Task

### Step 1: Inventory the folder
- Go through every PDF in the designated folder.
- For each file, identify:
  - **What it is:** Which expedition/visit does it relate to? Which specific account or author?
  - **Type:** Is it a primary source (original journal/log/narrative), a translated compilation (e.g., the Corney 1908 Hakluyt volume), a secondary source discussing the visits, or something else?
  - **Completeness:** Is this a full/complete version of the source, or a partial extract/chapter/excerpt?
  - **Quality:** Is the OCR clean and readable, or is it rough/garbled? Are there missing pages, scan artifacts, or other issues?
  - **Language:** Original language or translation? If translation, by whom?

### Step 2: Identify duplicates and overlaps
- Flag cases where multiple PDFs cover the same source material. For example:
  - Two different scans of the same Corney 1908 volume
  - A PDF with just one chapter/account that is also contained in a larger compiled volume
  - Different editions or translations of the same original text
- For each set of duplicates/overlaps, recommend which version to keep and why (better OCR, more complete, better translation, etc.)

### Step 3: Assess coverage against the timeline above
- Cross-reference the PDFs against the full list of known accounts in the timeline.
- Flag what is **present and accounted for**.
- Flag what is **missing entirely** (i.e., a known account with no corresponding PDF).
- Flag what is **partially covered** (e.g., we have an excerpt but not the full account).

### Step 4: Create an output document
- Produce a markdown file (e.g., `source_inventory.md`) with:
  1. **Complete inventory table** listing every PDF with the metadata from Step 1
  2. **Duplicate report** identifying overlapping files with keep/remove recommendations
  3. **Coverage assessment** mapped to each expedition, showing what we have vs. what we are missing
  4. **Recommended actions** (files to remove, sources still needed, etc.)

### Step 5: Organize the folder
- Do NOT delete anything without confirmation.
- Propose a folder structure organized by expedition/visit (e.g., `01_Roggeveen_1722/`, `02_Gonzalez_1770/`, etc.)
- If confirmed, move files into the proposed structure, placing the "best" version of each source at the top level and putting duplicates/lesser versions into a `duplicates/` subfolder within each expedition folder.

## Notes
- When in doubt about whether something is a duplicate, keep it and flag it for manual review.
- Some PDFs may contain multiple accounts bundled together (e.g., the Corney volume has both Roggeveen and González material). Note this in the inventory rather than trying to split them.
- Pay attention to the 19th century sources. The Richards (2008) volume is the key compiled reference for the post-La Pérouse period, but there may also be individual ship logs or extracts.
- The inventory should be thorough enough that someone can look at it and immediately know what is in the folder without opening any files.
