# AMD Life Science 26.10 release notes

The release notes provide a summary of notable changes since the previous AMD Life Science release.

## Release highlights

The following are notable new features and improvements in AMD Life Science 26.10 since the 26.08 release. For detailed changes to individual components, see [detailed component changelogs](#detailed-component-changelogs).

### geometric-nn-ops 0.1.0

This is the first release of geometric-nn-ops. geometric-nn-ops is a library of Triton GPU kernels for protein structure prediction models such as OpenFold3. The same kernel source runs on AMD GPUs with ROCm.

- **Fused triangle attention:** `triangle_attention` has native Triton forward and backward passes. It supports an optional pair bias and a boolean key mask. It runs bf16, fp16, and fp32. `dynamic=True` avoids recompiling for each sequence length. `use_exp2=True` selects a base-2 exponential softmax.

- **Triangle multiplicative update:** `triangle_multiplicative_update` has a fused Triton forward pass and a `cuequivariance`-compatible signature. When gradients are needed, it switches to a differentiable PyTorch implementation.

- **Attention with pair bias:** `attention_pair_bias` implements Algorithm 24 from the AlphaFold 3 paper in PyTorch. The interface matches `cuequivariance` 0.9, and it can cache the projected pair bias.

- **fp32 precision control:** The Triton kernels follow `torch.backends.cuda.matmul.fp32_precision`. With `"tf32"`, they use a matmul that is at least TF32-accurate, for example XF32 MFMA on AMD CDNA3.

- **Removed bias arguments:** `attention_pair_bias` no longer accepts `ln_z_bias` or `proj_z_bias`. The softmax cancels these parameters, so they can't affect the output.

- **Drop-in replacement for `cuequivariance_ops_torch`:** The `hipequivariance-ops-torch` package lets unmodified `cuequivariance_torch` 0.9.1 code run on AMD GPUs. The shim translates tensor layouts and output ranks to match `cuequivariance`.

- **Installation guards:** Importing the shim raises an error if `cuequivariance-ops-torch` wheels are also installed. It warns if the installed `cuequivariance-torch` version isn't 0.9.1.

## AMD Life Science components

The following table lists the versions of AMD Life Science components for AMD Life Science 26.10. Click the GitHub icon to go to the component's source code.

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
                <td>26.06.00</td>
                <td><a href="https://github.com/AMD-Ecosystem/hipCIM"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monai/en/docs-26.08/">MONAI on ROCm</a></td>
                <td>1.6.0</td>
                <td><a href="https://github.com/AMD-Ecosystem/monai"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monai-model-zoo/en/docs-26.08/">MONAI Model Zoo</a></td>
                <td>26.08</td>
                <td><a href="https://github.com/AMD-Ecosystem/monai-model-zoo"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://rocm.docs.amd.com/projects/monailabel/en/docs-26.08/">MONAILabel</a></td>
                <td>0.8.5</td>
                <td><a href="https://github.com/AMD-Ecosystem/monailabel"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td>AI/ML</td>
                <td><a href="https://advanced-micro-devices-demo--26.com.readthedocs.build/projects/geometric-nn-ops/en/26/">geometric-nn-ops</a></td>
                <td>0.1.0</td>
                <td><a href="https://github.com/ROCm/geometric-nn-ops"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

## Detailed component changelogs

The following are changes specific to the AMD Life Science components.

### geometric-nn-ops 0.1.0

#### Resolved issues

These changes are in the triangle attention kernel originally contributed to OpenFold3.

- Fixed NaN output in fp16 when a whole tile of keys was masked.

- Fixed incorrect gradients for fully masked rows in the backward pass.
