.. meta::
  :description: AMD Life Science toolkit is a collection of open-source software for high-performance data science applications built on the core ROCm platform.
  :keywords: AMD Life Science, life sciences

*********************************
AMD Life Science documentation
*********************************

The AMD Life Science toolkit is an open-source, GPU-accelerated library suite for life science and healthcare applications built on the core ROCm™ platform and optimized for use on AMD GPUs. 

AMD Life Science can be used to accelerate new and existing life science workloads on AMD devices. The suite targets compute-intensive applications that process larger datasets so that you can build pre-processing and post-processing applications for AI models and accelerate existing life science pipelines.

The AMD Life Science libraries provide the following tools for life science acceleration on AMD GPUs:

- **hipCIM**: A GPU imaging library that accelerates and scales image processing on AMD Instinct™ GPUs.
- **MONAI on ROCm**: An open-source framework that brings deep learning for medical imaging to AMD GPU platforms.
- **MONAI Model Zoo**: A collection of MONAI Bundle models with AMD ROCm inference overlays for validated segmentation workloads on AMD Instinct™ GPUs.
- **MONAILabel**: An interactive medical image labeling framework with Early Access AMD GPU support on ROCm.
- **geometric-nn-ops**: A GPU kernel library for geometry-aware neural networks, including triangle operations for protein structure prediction.

These tools are integrated into a comprehensive workflow supporting a variety of life science applications on AMD GPUs.

.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Components

    - `hipCIM <https://rocm.docs.amd.com/projects/hipCIM/en/docs-26.08/>`_
    - `MONAI on ROCm <https://rocm.docs.amd.com/projects/monai/en/docs-26.08/>`_
    - `MONAI Model Zoo on ROCm <https://rocm.docs.amd.com/projects/monai-model-zoo/en/docs-26.08/>`_
    - `MONAILabel <https://rocm.docs.amd.com/projects/monailabel/en/docs-26.08/>`_
    - `geometric-nn-ops <https://rocm.docs.amd.com/projects/geometric-nn-ops/en/docs-26.10/>`_

  .. grid-item-card:: Related content

    - :doc:`contribute/contribution`

For ready-to-run code samples that demonstrate AMD Life Science capabilities on the AMD ROCm platform, see the `AMD Life Science examples <https://github.com/AMD-Ecosystem/lifescience-examples>`_.
