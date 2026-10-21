# AMD Life Science 26.08 release notes

The release notes provide a summary of notable changes since the previous AMD Life Science release.

## AMD Life Science release highlights

The following are notable new features and improvements in AMD Life Science 26.08 since the release of 26.03. For detailed changes to individual components, see [detailed component changes](#detailed-component-changes).

- hipCIM 26.06.00: Adds OME-TIFF and multi-page TIFF support, a NIfTI-1 reader, and a DICOM Phase 1 reader. rocJPEG handle pooling and a process-level GPU tile cache speed up repeated `read_region()` calls.

- MONAI on ROCm 1.6.0: Speeds up SwinUNETR, SlidingWindowInferer, and DynUNet inference on AMD CDNA GPUs.

- MONAI Model Zoo 26.08: Adds AMD ROCm inference overlays for five MONAI Bundle models, in Early Access.

- MONAILabel 0.8.5: Adds AMD GPU support on ROCm, in Early Access.

## AMD Life Science components

The following table lists the versions of AMD Life Science components for AMD Life Science 26.08, including any version changes from 26.03 to 26.08. Click the GitHub icon to go to the component's source code.

<div class="pst-scrollable-table-container">
    <table id="rocm-rn-components" class="table">
        <thead>
            <tr>
                <th>Category</th>
                <th>Component name</th>
                <th>Version</th>
                <th>Source code</th>
            </tr>
        </thead>
        <colgroup>
            <col span="1">
            <col span="1">
        </colgroup>
        <tbody class="rocm-components-libs rocm-components-ml">
            <tr>
                <td>Imaging</td>
                <td><a href="https://rocm.docs.amd.com/projects/hipCIM/en/docs-26.08/">hipCIM</a></td>
                <td>25.10.00&nbsp;&Rightarrow;&nbsp;<a href="#hipcim-26-06-00">26.06.00</a></td>
                <td><a href="https://github.com/AMD-Ecosystem/hipCIM"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monai/en/docs-26.08/">MONAI on ROCm</a></td>
                <td>1.5.2&nbsp;&Rightarrow;&nbsp;<a href="#monai-on-rocm-1-6-0">1.6.0</a></td>
                <td><a href="https://github.com/AMD-Ecosystem/monai"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monai-model-zoo/en/docs-26.08/">MONAI Model Zoo</a></td>
                <td><a href="#monai-model-zoo-26-08">26.08</a></td>
                <td><a href="https://github.com/AMD-Ecosystem/monai-model-zoo"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monailabel/en/docs-26.08/">MONAILabel</a></td>
                <td><a href="#monailabel-0-8-5">0.8.5</a></td>
                <td><a href="https://github.com/AMD-Ecosystem/monailabel"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

## Detailed component changes

The following sections describe changes to the AMD Life Science components.

### hipCIM (26.06.00)

#### Added

- **OME-TIFF and multi-page TIFF support:** Multi-IFD TIFFs are now accepted as a flat page list. Previously, any TIFF with more than one full-resolution IFD raised a parse error.

- **NIfTI-1 reader:** CuImage now opens `.nii` and `.nii.gz` volumetric files directly, without requiring nibabel or DCMTK. The reader handles endianness detection, gzip decompression using libdeflate, and all common NIfTI-1 data types.

- **DICOM Phase 1 reader:** Single-frame DICOM files, using uncompressed Explicit or Implicit VR Little-Endian, are now readable via CuImage, with no DCMTK or GDCM dependency. Compressed transfer syntaxes, including JPEG Baseline and JPEG 2000, are supported when the library is built with `CUMED_DICOM_COMPRESSED=ON`.

#### Optimized

- **rocJPEG handle pool:** rocJPEG decode handles are now pooled at the process level. Previously, a new handle was created and destroyed for every `read_region()` call.

- **Process-level GPU tile cache:** Decoded tiles are cached in GPU memory across `read_region()` calls.

#### Changed

- **Graceful plugin degradation:** A plugin that fails to load, for example when rocJPEG runtime libraries are absent, now logs a warning and is skipped, rather than taking down all formats. NIfTI and DICOM reads succeed even on hosts where slide-format GPU libraries aren't installed.

#### Resolved issues

- Fixed a SIGSEGV in the rocJPEG batch path triggered by scattered or out-of-range `read_region` calls.

- Fixed an OOM abort caused by an unchecked rocJPEG batch device allocation when VRAM was nearly full.

- Fixed a JP2K GPU abort where JPEG 2000-compressed tiles were incorrectly routed to the GPU decode path. JP2K tiles now decode into host memory before transfer.

- Fixed incorrect colour output on RGB-native images (blue/red channel swap) when using the host-input GPU decode path.

- Fixed an undefined-behavior crash where any rocJPEG or HIP error would call `exit(1)`, terminating the host process. Errors now throw `std::runtime_error` so callers can recover.

### MONAI on ROCm (1.6.0)

#### Optimized

- **SwinUNETR WindowAttention SDPA:** Scaled dot-product attention (SDPA) via `torch.nn.functional.scaled_dot_product_attention` is now auto-enabled for SwinUNETR WindowAttention layers on ROCm, replacing the explicit Q×KT×V loop. This accelerates SwinUNETR-based inference on AMD CDNA GPUs.

- **SlidingWindowInferer dynamic graph stabilization:** The sliding window inferer patches an HIP-specific divergence in `torch.compile` graph recompilation caused by non-constant window shapes during inference. This eliminates recompilation storms on variable-resolution inputs.

- **DynUNet GEMM-based ConvTranspose3d:** 3D transposed convolutions in DynUNet are routed through a GEMM-based implementation on ROCm, bypassing a performance regression in the default convolution transpose kernel on CDNA architectures.

### MONAI Model Zoo (26.08)

#### Added

- **AMD ROCm inference overlays (Early Access):** Five bundles are inference-validated and optimized for AMD Instinct™ GPUs using MONAI Bundle overlay configurations (`inference_rocm.json` or `inference_rocm.yaml`):

  - `vista3d`: VISTA-3D multi-organ segmentation for 130+ structures.
  - `swin_unetr_btcv_segmentation`: Swin UNETR 13-organ abdominal CT segmentation.
  - `wholeBody_ct_segmentation`: SegResNet 104-structure whole-body CT segmentation
  - `spleen_deepedit_annotation`: DeepEdit interactive spleen segmentation.
  - `pancreas_ct_dints_segmentation`: DiNTS pancreas and tumor segmentation.

  All overlays apply channels-last 3D memory format, BF16 AMP, `torch.compile`, and device-aware checkpoint loading without modifying model weights.

#### Known issues

- `spleen_deepedit_annotation`: the ROCm overlay calls `network_def.enable_gemm_transpose(True)` when the method is present and sets `evaluator.compile = True`, so `torch.compile` is applied consistently. No source patch is required — the behaviour is configured entirely through the bundle overlay.

### MONAILabel (0.8.5)

#### Added

- **AMD GPU support (Early Access):** MONAILabel now reports AMD GPU memory and device information on ROCm through three targeted code changes: ROCm-aware `gpu_memory_map()` in `monailabel/utils/others/generic.py`, the `/gpu` REST endpoint in `monailabel/endpoints/logs.py`, and an updated Dockerfile for ROCm runtime. The MONAILabel framework API and all existing apps and plugins are unmodified.

#### Known issues

- Pathology app workflows are not validated in this release.
