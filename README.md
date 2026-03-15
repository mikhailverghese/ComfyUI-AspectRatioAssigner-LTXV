# ComfyUI-AspectRatioAssigner-LTXV

A simple ComfyUI custom node that reads an input image's aspect ratio and selects the closest target resolution from:

- Portrait: 768 x 1344
- Landscape: 1344 x 768
- Square: 1344 x 1344

## Node

**Aspect Ratio Closest Target**

### Inputs
- `image` (IMAGE)

### Outputs
- `width` (INT)
- `height` (INT)
- `orientation` (STRING)

## Installation

Clone into your ComfyUI custom_nodes folder:

```bash
cd /workspace/ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/ComfyUI-AspectRatioTarget.git
