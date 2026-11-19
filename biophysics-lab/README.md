# Confocal vs. Airyscan: Resolution Limits in Fluorescence Microscopy

*Biophysics lab project, FSU Jena · summer 2025 · with Agnese and Zineb · supervisor: Dr. K. Reglinski*

📄 **[Full lab report (PDF, German)](report.pdf)**

<p align="center">
  <img src="figures/cell3_confocal.png" width="45%" alt="HEK cells, confocal image: mitochondria in red, peroxisomes in green"/>
  <img src="figures/cell3_airyscan.png" width="45%" alt="The same HEK cells imaged with Airyscan: sharper, more separated green peroxisomes"/>
</p>
<p align="center"><em>The same cells, imaged twice. Left: confocal. Right: Airyscan. Red: mitochondria, green: peroxisomes.</em></p>

## The idea
A light microscope cannot show details much smaller than about half the wavelength of light (the **Abbe limit**, roughly 200–250 nm for a confocal microscope). Two tiny structures closer than that blur into one spot.

- A **confocal microscope** scans a focused laser across the sample and uses a pinhole to block out-of-focus light, giving sharp optical sections.
- **Airyscan** replaces the pinhole with an array of 32 detectors that each see a slightly different part of the blurred spot (the Airy disk). Combining them computationally pushes the resolution beyond the classical confocal limit.

Our question: **how much better is Airyscan in practice?**

## What we did
- Used human cells (HEK) and stained two organelles by **immunofluorescence**: mitochondria (anti-TOM20, AbStar Red) and peroxisomes (anti-PMP70, Alexa 488). This involved fixing, permeabilising, blocking and two rounds of antibody incubation.
- Imaged the same cells with a **Zeiss confocal microscope** and its **Airyscan** detector, including z-stacks and close-ups.
- Peroxisomes are smaller than the resolution limit, so their image is essentially the microscope's **point spread function (PSF)**: ideal test objects.

## How we analysed it
- Drew **line profiles** across single peroxisomes in Fiji and fitted a **Gaussian** to each profile.
- Resolution from the width of the fit: **FWHM = 2√(2 ln 2)·d**.
- Repeated this for **20 peroxisomes** in each mode and compared mean, spread and best value; also applied the **Rayleigh criterion**.
- Plotted measured intensity and fit in Python ([`analysis/peroxisome_line_profile.py`](analysis/peroxisome_line_profile.py)).

<p align="center">
  <img src="figures/peroxisome_line.png" width="40%" alt="A single peroxisome with the measured line profile drawn across it"/>
  <img src="figures/peroxisome_line_profile.png" width="50%" alt="Intensity along the line with Gaussian fit"/>
</p>

## Results

| Criterion | Confocal | Airyscan | Improvement |
|---|---|---|---|
| FWHM (mean of 20 peroxisomes) | 314 nm | **235 nm** | 1.33× |
| Rayleigh criterion | 287 nm | **183 nm** | 1.57× |

Airyscan resolves noticeably finer detail: peroxisomes appear as clearly separated dots, and mitochondria show more structure.

<p align="center">
  <img src="figures/cell3_airyscan_closeup.png" width="40%" alt="Airyscan close-up of mitochondria and peroxisomes"/>
  <img src="figures/cell4_confocal.png" width="40%" alt="Another HEK cell with a mitochondrial network in red and peroxisomes in green"/>
</p>

## Files
- `report.pdf`: the full lab report (German)
- `analysis/`: Python script and the exported Fiji line profile with Gaussian fit
- `figures/`: fluorescence images and the line-profile plot
