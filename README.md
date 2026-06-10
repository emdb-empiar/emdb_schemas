# emdb-schemas
EMDB header file schema

## Changelog

This section contains information on changes made for each version change to the EMDB XML schema after version 3.0.0.0.

The format of the information given is:

```text
version number, changes made; additional information
```

```text
3.0.0.1 : 'JEOL CRYOSPECPORTER' enumeration added to the 'specimen_holder_model' element
3.0.1.1 : (1) Changed format for fsc file names; (2) Added organ, tissue, cell, organelle and cellular_location elements to complex natural source; (3) author_type pattern changed to [A-Za-z']+(( |-)[A-Za-z]+)*(Jr|III)?
3.0.1.2 : Changed regex for authors to ([A-Za-z' \-]+ (Jr.?|II|III)?) ?([A-Za-z\-]*)
3.0.1.3 : (1) Allowed for '3rd' and '4th' in authors regex; (2) Allowed chain ids to have up to 2 letters; (3) Increased the EC number range to 7 for proteins
3.0.1.4 : Added 'GATAN K3 (6k x 4k)' and 'GATAN K3 BIOQUANTUM (6k x 4k)' to allowed_film_or_detector_model
3.0.1.5 : Made 'code' and 'country' mandatory for the 'grant_reference_type'
3.0.1.6 : Added enumerations: 1. microscope {"TFS GLACIOS",  "TFS KRIOS"} and 2. specimen_holder_model {"FISCHIONE 2550",  "GATAN ELSA 698 SINGLE TILT LIQUID NITROGEN CRYO TRANSFER HOLDER"}
3.0.1.7 : Added "TFS TALOS" enumeration to microscope
3.0.1.8 : Added (1) "TFS TALOS L120C" and "TFS TALOS F200C" enumerations to microscope; (2) Changed film_material from any token to {"CARBON", "CELLULOSE ACETATE", "FORMVAR", "GOLD", "GRAPHENE", "GRAPHENE OXIDE", "PARLODION"};
(3) Added "NICKEL/TITANIUM" to grid material and "HITACHI H3000 UHVEM" microscope enumerations
3.0.1.9 : (1) Added FEI FALCON IV (4k x 4k) to detectors; (2) Removed max limit to "allowed_acceleration_voltage"; (3) Removed max limit to "allowed_scaning_interval"
3.0.1.10: Removed max limit for "allowed_focus_ion_final_thickness"
3.0.2.0: (1) Added synthetic_source to supramolecules and some macromolecules; (2) Changed name for <supramolecule>_natural_source_type to <supramolecule>_source_type; (3) Added "QCRG Structural Biology Consortium" to author_enums
3.0.2.1: (1) Added 'PDBc' to 'processing_site'; (2) Made 'r_sym', 'overall_phase_error' and 'overall_phase_residual' in 'crystallography_statistics_type' non-mandatory (3) Changed the type of 'phase_error_rejection_criteria' in 'crystallography_statistics_type' from a float to a token; (4) Added a non-mandatory string element 'details' to 'specialist_optics_type'
3.0.2.2: Added 'PDBc' to 'deposition' and 'last_processing' in 'sites'
3.0.2.3: (1) Added "JEOL 1000EES" to the list of microscopes; (2) changed sectioning focused_ion_beam duration to a float
3.0.2.4: Added "FISCHIONE INSTRUMENTS DUAL AXIS TOMOGRAPHY HOLDER" to specimen_holder_model
3.0.2.5: Changed the max limit of allowed_focus_ion_initial_thickness to 100000
3.0.2.6: Added "TFS Tundra" to the list of microscopes; Changed "TFS Tundra" to "TFS TUNDRA"; Changed "applied_symmetry_type" type from token to int
3.0.2.7: Created new type "author_ORCID_type" for storing ORCID; Changed "author" in "author_list" element's type to "author_ORCID_type"; Changed "author_order_type" base type to "author_ORCID_type"
3.0.2.8: (1) Added DIRECT ELECTRON APOLLO (4k x 4k) in allowed_film_or_detector_model; (2) changed minimum value from 5 to 3 in allowed_focus_ion_voltage
3.0.2.9: (1) Changed allowed_focus_ion_voltage (range is now 0.1 to 50); (2) changed allowed_defocus_max (maxInclusive value="50")
3.0.2.10: Allow 1st, 2nd, 3rd and 4th in the author names
3.0.2.11: Added Center for Structural Biology of Infectious Diseases (CSBID)
3.0.3.0: Dictionary change. Five new items to em_3d_fitting_list category which will eventually replace the current three items. (1) accession_code (2) chain_is (3) residue_range (4) source_name (5) type to replace (1) access_code (2)pdbe_chain_id (3)pdb_chain_
residue_range.
3.0.3.1: Changed from mandatory to optional both elements in the startup_model (pdb_model.pdb_id and orthogonal_tilt.number_images).
3.0.3.2: Added TFS FALCON 4i (4k x 4x) to the element film_or_detector_model
3.0.3.3: Changed TFS FALCON 4i (4k x 4k) from TFS FALCON 4i (4k x 4x) in emdb-schema
3.0.4.0: Supports also the extended PDB ids (example: pdb_00001abc)
3.0.5.0: Added an element <other_db_list> in the crossreferences_type
3.0.6.0: Added an element <mask_list> in <interpretation>
3.0.7.0: Attribute synthetically_produced and element details are added to base_source_type
3.0.7.1: Added DECTRIS SINGLA (1k x 1k) in allowed_film_or_detector_model
3.0.7.2: Added "JEOL 1400/HR + YPS FEG" in microscope
3.0.8.0: Removed the element <mask_list> which was added to emdb-schema in v3_0_6_0
3.0.9.0: Added composite_map attribute to element admin
3.0.9.1: Added "DECTRIS ELA (1k x 0.5k)" in allowed_film_or_detector_model
3.0.9.2: Added "GATAN ALPINE (2.3k x 3.2k)" and "GATAN K3 BIOCONTINUUM (6k x 4k)" to allowed_film_or_detector_model
3.0.9.3: Added "DECTRIS ARINA (0.2k x 0.2k)" to allowed_film_or_detector_model and "4D-STEM" to imaging_mode
3.0.9.4: Added "TFS TITAN THEMIS" to microscope
3.0.10.0: Added auditing to data model
3.0.10.1: Added "SILICON DIOXIDE" to film_material
3.0.10.2: Updated enumeration values in revision_group to match the controlled vocabulary list
3.0.10.3: Added "CRYOSOL VITROJET", "SPT LABTECH CHAMELEON", and "ZEISS PLUNGE FREEZER CRYOBOX" to the instrument enumeration list
3.0.11.0: Added type item to em_ctf_correction category and support in ctf_correction_type element; Added objective_aperture, microscope_serial_number and microscope_version items to microscopy; Added em_motion_correction category with items type and details
3.0.11.1: Updated residue_range pattern to allow negative residue numbers: changed from '\d+-\d+' to '[+-]?[0-9]+-[+-]?[0-9]+' to match mmCIF dictionary requirements
3.0.11.2: Added "NOR" to external reference enumerations in emdb_relaxed.xsd
3.0.11.3: Added three new Shuimu Biosciences microscope models: "SHUIMU TOTEM 120S", "SHUIMU TOTEM 200S", and "SHUIMU TOTEM 300S" to microscope enumeration
```
