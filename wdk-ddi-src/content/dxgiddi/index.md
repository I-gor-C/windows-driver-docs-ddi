# Dxgiddi.h header


This header is used by Display. For more information, see
- [Display](../_display/index.md)

Dxgiddi.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PFNDDXGIDDI_PRESENTCB callback](nc-dxgiddi-pfnddxgiddi-presentcb.md) | The pfnPresentCbDXGI function copies content from a source allocation to a destination allocation. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [DXGI1_1_DDI_BASE_FUNCTIONS structure](ns-dxgiddi-dxgi1-1-ddi-base-functions.md) | The DXGI1_1_DDI_BASE_FUNCTIONS structure contains pointers to functions that the user-mode display driver can implement to perform low-level tasks like presenting rendered frames to an output, controlling gamma, getting notifications regarding shared and GDI interoperable surfaces, and managing a full-screen transition. |
| [DXGI1_2_DDI_BASE_FUNCTIONS structure](ns-dxgiddi-dxgi1-2-ddi-base-functions.md) | Contains pointers to functions that a Windows Display Driver Model (WDDM) 1.2 and later user-mode display driver can implement to perform low-level tasks like presenting rendered frames to an output, controlling gamma, getting notifications regarding shared and Windows Graphics Device Interface (GDI) interoperable surfaces, and managing a full-screen transition. |
| [DXGI1_3_DDI_BASE_FUNCTIONS structure](ns-dxgiddi-dxgi1-3-ddi-base-functions.md) | Contains pointers to functions that a Windows Display Driver Model (WDDM) 1.3 and later user-mode display driver can implement to perform low-level tasks like presenting rendered frames to an output, controlling gamma, getting notifications regarding shared and Windows Graphics Device Interface (GDI) interoperable surfaces, and managing a full-screen transition. |
| [DXGIDDICB_PRESENT structure](ns-dxgiddi-dxgiddicb-present.md) | The DXGIDDICB_PRESENT structure describes allocations that content is copied to and from. |
| [DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY structure](ns-dxgiddi-dxgiddicb-present-multiplane-overlay.md) | Describes multiplane overlay allocations that content is copied to and from. |
| [DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY1 structure](ns-dxgiddi-dxgiddicb-present-multiplane-overlay1.md) | Describes multiplane overlay allocations, private driver data, and context information for each multiplane overlay plane. |
| [DXGIDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO structure](ns-dxgiddi-dxgiddi-multiplane-overlay-allocation-info.md) | Specifies info about a multiplane overlay allocation. |
| [DXGI_DDI_ARG_BLT structure](ns-dxgiddi-dxgi-ddi-arg-blt.md) | The DXGI_DDI_ARG_BLT structure describes the parameters of a bit-block transfer (bitblt). |
| [DXGI_DDI_ARG_BLT1 structure](ns-dxgiddi-dxgi-ddi-arg-blt1.md) | Describes the parameters of a bit-block transfer (bitblt) that include specifications for a source rectangle. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [DXGI_DDI_ARG_BLT_FLAGS structure](ns-dxgiddi-dxgi-ddi-arg-blt-flags.md) | The DXGI_DDI_ARG_BLT_FLAGS structure identifies the type of bit-block transfer (bitblt) to perform. |
| [DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT structure](ns-dxgiddi--dxgi-ddi-arg-checkmultiplaneoverlaysupport.md) | Used in a call to the pfnCheckMultiPlaneOverlaySupport (DXGI) function to check details on hardware support for multiplane overlays. |
| [DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT structure](ns-dxgiddi--dxgi-ddi-arg-checkpresentdurationsupport.md) | Used in a call to the pfnCheckPresentDurationSupport(DXGI) function to check details on hardware device support for seamlessly switching to a new monitor refresh rate. |
| [DXGI_DDI_ARG_GETMULTIPLANEOVERLAYCAPS structure](ns-dxgiddi--dxgi-ddi-arg-getmultiplaneoverlaycaps.md) | Used in a call to the pfnGetMultiPlaneOverlayCaps function to get overlay plane capabilities. |
| [DXGI_DDI_ARG_GETMULTIPLANEOVERLAYGROUPCAPS structure](ns-dxgiddi--dxgi-ddi-arg-getmultiplaneoverlaygroupcaps.md) | Used in a call to the pfnGetMultiplaneOverlayGroupCaps function to get a group of overlay plane capabilities. |
| [DXGI_DDI_ARG_GET_GAMMA_CONTROL_CAPS structure](ns-dxgiddi-dxgi-ddi-arg-get-gamma-control-caps.md) | The DXGI_DDI_ARG_GET_GAMMA_CONTROL_CAPS structure contains gamma capabilities. |
| [DXGI_DDI_ARG_OFFERRESOURCES structure](ns-dxgiddi--dxgi-ddi-arg-offerresources.md) | Describes video memory resources that the user-mode display driver offers for reuse. Used with the pfnOfferResources function. Used with the pfnReclaimResources function by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [DXGI_DDI_ARG_PRESENT structure](ns-dxgiddi-dxgi-ddi-arg-present.md) | The DXGI_DDI_ARG_PRESENT structure describes a resource to display. |
| [DXGI_DDI_ARG_PRESENT1 structure](ns-dxgiddi-dxgi-ddi-arg-present1.md) | Describes a resource to display. Used with the pfnPresent1(DXGI) function by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers. |
| [DXGI_DDI_ARG_PRESENTMULTIPLANEOVERLAY structure](ns-dxgiddi--dxgi-ddi-arg-presentmultiplaneoverlay.md) | Specifies a multiplane overlay resource to display. |
| [DXGI_DDI_ARG_PRESENTSURFACE structure](ns-dxgiddi-dxgi-ddi-arg-presentsurface.md) | Describes a surface to display. |
| [DXGI_DDI_ARG_QUERYRESOURCERESIDENCY structure](ns-dxgiddi-dxgi-ddi-arg-queryresourceresidency.md) | The DXGI_DDI_ARG_QUERYRESOURCERESIDENCY structure describes the residency status of a list of resources. |
| [DXGI_DDI_ARG_RECLAIMRESOURCES structure](ns-dxgiddi--dxgi-ddi-arg-reclaimresources.md) | Describes video memory resources that are to be reclaimed and that the user-mode display driver previously offered for reuse. Used with the pfnReclaimResources function by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers. |
| [DXGI_DDI_ARG_RESOLVESHAREDRESOURCE structure](ns-dxgiddi-dxgi-ddi-arg-resolvesharedresource.md) | The DXGI_DDI_ARG_RESOLVESHAREDRESOURCE structure describes the parameters that the user-mode display driver's ResolveSharedResourceDXGI function uses to synchronize a shared surface or a GDI interoperable surface. |
| [DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES structure](ns-dxgiddi-dxgi-ddi-arg-rotate-resource-identities.md) | Describes a list of resources to rotate. |
| [DXGI_DDI_ARG_SETDISPLAYMODE structure](ns-dxgiddi-dxgi-ddi-arg-setdisplaymode.md) | The DXGI_DDI_ARG_SETDISPLAYMODE structure describes parameters for setting the display mode. |
| [DXGI_DDI_ARG_SETRESOURCEPRIORITY structure](ns-dxgiddi-dxgi-ddi-arg-setresourcepriority.md) | The DXGI_DDI_ARG_SETRESOURCEPRIORITY structure describes parameters for setting the priority level of a resource. |
| [DXGI_DDI_BASE_ARGS structure](ns-dxgiddi-dxgi-ddi-base-args.md) | The DXGI_DDI_BASE_ARGS structure contains Microsoft DirectX Graphics Infrastructure (DXGI) basic device driver interface (DDI) device creation arguments. |
| [DXGI_DDI_BASE_CALLBACKS structure](ns-dxgiddi-dxgi-ddi-base-callbacks.md) | The DXGI_DDI_BASE_CALLBACKS structure contains pointers to Microsoft Direct3D 10 runtime callback functions that the user-mode display driver can use. |
| [DXGI_DDI_BASE_FUNCTIONS structure](ns-dxgiddi-dxgi-ddi-base-functions.md) | The DXGI_DDI_BASE_FUNCTIONS structure contains functions that the user-mode display driver can implement to perform low-level tasks like presenting rendered frames to an output, controlling gamma, and managing a full-screen transition. |
| [DXGI_DDI_CHECK_MULTIPLANEOVERLAYSUPPORT_PLANE_INFO structure](ns-dxgiddi-dxgi-ddi-check-multiplaneoverlaysupport-plane-info.md) | Specifies the support attributes that the hardware provides for multiplane overlays. |
| [DXGI_DDI_MODE_DESC structure](ns-dxgiddi-dxgi-ddi-mode-desc.md) | The DXGI_DDI_MODE_DESC structure describes a display mode. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_ATTRIBUTES structure](ns-dxgiddi-dxgi-ddi-multiplane-overlay-attributes.md) | Used by the user-mode display driver to specify overlay plane attributes. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_CAPS structure](ns-dxgiddi-dxgi-ddi-multiplane-overlay-caps.md) | Used by the user-mode display driver to specify overlay plane capabilities. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_GROUP_CAPS structure](ns-dxgiddi-dxgi-ddi-multiplane-overlay-group-caps.md) | Used by the user-mode display driver to specify groups of overlay plane capabilities. |
| [DXGI_DDI_PRESENT_FLAGS structure](ns-dxgiddi-dxgi-ddi-present-flags.md) | Identifies how to perform a present operation. |
| [DXGI_DDI_PRESENT_MULTIPLANE_OVERLAY structure](ns-dxgiddi--dxgi-ddi-present-multiplane-overlay.md) | Specifies overlay planes to display. |
| [DXGI_DDI_PRIMARY_DESC structure](ns-dxgiddi-dxgi-ddi-primary-desc.md) | Describes a resource that is used as a primary (that is, a resource that is scanned out to the display). |
| [DXGI_DDI_RATIONAL structure](ns-dxgiddi-dxgi-ddi-rational.md) | The DXGI_DDI_RATIONAL structure describes a fractional value that represents vertical and horizontal frequencies of a display mode (that is, vertical sync and horizontal sync). |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [DXGI_DDI_FLIP_INTERVAL_TYPE enumeration](ne-dxgiddi-dxgi-ddi-flip-interval-type.md) | The DXGI_DDI_FLIP_INTERVAL_TYPE enumeration type contains values that identify the type of flip that occurs in present operations. |
| [DXGI_DDI_MODE_ROTATION enumeration](ne-dxgiddi-dxgi-ddi-mode-rotation.md) | The DXGI_DDI_MODE_ROTATION enumeration type contains values that identify the orientation of the display. |
| [DXGI_DDI_MODE_SCALING enumeration](ne-dxgiddi-dxgi-ddi-mode-scaling.md) | The DXGI_DDI_MODE_SCALING enumeration type contains values that identify the scaling support for a display. |
| [DXGI_DDI_MODE_SCANLINE_ORDER enumeration](ne-dxgiddi-dxgi-ddi-mode-scanline-order.md) | The DXGI_DDI_MODE_SCANLINE_ORDER enumeration type contains values that identify how scan lines are ordered in a display mode. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_BLEND enumeration](ne-dxgiddi-dxgi-ddi-multiplane-overlay-blend.md) | Identifies a blend operation to be performed on an overlay plane. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_FEATURE_CAPS enumeration](ne-dxgiddi-dxgi-ddi-multiplane-overlay-feature-caps.md) | Identifies overlay capabilities. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_FLAGS enumeration](ne-dxgiddi-dxgi-ddi-multiplane-overlay-flags.md) | Identifies a flip operation to be performed on an overlay plane. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_CAPS enumeration](ne-dxgiddi-dxgi-ddi-multiplane-overlay-stereo-caps.md) | Reserved for system use. Do not use it in your driver. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE enumeration](ne-dxgiddi-dxgi-ddi-multiplane-overlay-stereo-flip-mode.md) | Identifies the overlay plane's stereo flip mode. Only the DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE value is supported. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT enumeration](ne-dxgiddi-dxgi-ddi-multiplane-overlay-stereo-format.md) | Identifies the overlay plane's stereo presentation format. Only the DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO value is supported. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_STRETCH_QUALITY enumeration](ne-dxgiddi-dxgi-ddi-multiplane-overlay-stretch-quality.md) | Identifies filtering processes that the hardware should perform when it stretches or shrinks multiplane overlay data. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT enumeration](ne-dxgiddi-dxgi-ddi-multiplane-overlay-video-frame-format.md) | Identifies the overlay plane's video frame format. Only the DXGI_DDI_MULIIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE value is supported. |
| [DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS enumeration](ne-dxgiddi-dxgi-ddi-multiplane-overlay-ycbcr-flags.md) | Identifies YUV range and conversion info that describes a multiplane overlay. |
