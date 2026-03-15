class AspectRatioClosestTarget:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "orientation")
    FUNCTION = "get_target_size"
    CATEGORY = "utils"

    def get_target_size(self, image):
        # ComfyUI image shape is typically [B, H, W, C]
        _, h, w, _ = image.shape
        ratio = w / h

        targets = {
            "portrait": (768, 1344),
            "landscape": (1344, 768),
            "square": (1344, 1344),
        }

        best_name = min(
            targets,
            key=lambda name: abs(ratio - (targets[name][0] / targets[name][1]))
        )

        out_w, out_h = targets[best_name]
        return (out_w, out_h, best_name)


NODE_CLASS_MAPPINGS = {
    "AspectRatioClosestTarget": AspectRatioClosestTarget
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatioClosestTarget": "Aspect Ratio Closest Target"
}
