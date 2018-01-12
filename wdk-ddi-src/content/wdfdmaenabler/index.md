---
UID: NA:wdfdmaenabler
---

# Wdfdmaenabler.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfdmaenabler.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFDMAENABLERCONFIGURESYSTEMPROFILE function](nc-wdfdmaenabler-pfn_wdfdmaenablerconfiguresystemprofile.md) | The WdfDmaEnablerConfigureSystemProfile method configures the hardware-specific settings for a system-mode DMA enabler and completes the resource initialization. |
| [PFN_WDFDMAENABLERCREATE function](nc-wdfdmaenabler-pfn_wdfdmaenablercreate.md) | The WdfDmaEnablerCreate method creates a DMA enabler object. |
| [PFN_WDFDMAENABLERGETFRAGMENTLENGTH function](nc-wdfdmaenabler-pfn_wdfdmaenablergetfragmentlength.md) | The WdfDmaEnablerGetFragmentLength method returns the maximum transfer length that the operating system supports for a single DMA transfer. |
| [PFN_WDFDMAENABLERGETMAXIMUMLENGTH function](nc-wdfdmaenabler-pfn_wdfdmaenablergetmaximumlength.md) | The WdfDmaEnablerGetMaximumLength method returns the maximum transfer length, for a single DMA transfer, that a device supports. |
| [PFN_WDFDMAENABLERGETMAXIMUMSCATTERGATHERELEMENTS function](nc-wdfdmaenabler-pfn_wdfdmaenablergetmaximumscattergatherelements.md) | The WdfDmaEnablerGetMaximumScatterGatherElements method returns the maximum number of scatter/gather elements that the device and driver support, for a specified DMA enabler object. |
| [PFN_WDFDMAENABLERSETMAXIMUMSCATTERGATHERELEMENTS function](nc-wdfdmaenabler-pfn_wdfdmaenablersetmaximumscattergatherelements.md) | The WdfDmaEnablerSetMaximumScatterGatherElements method sets the maximum number of scatter/gather elements that a device supports, for a specified DMA enabler object. |
| [PFN_WDFDMAENABLERWDMGETDMAADAPTER function](nc-wdfdmaenabler-pfn_wdfdmaenablerwdmgetdmaadapter.md) | The WdfDmaEnablerWdmGetDmaAdapter method returns a pointer to a WDM DMA_ADAPTER structure that is associated with a DMA enabler object. |
| [WDF_DMA_ENABLER_CONFIG_INIT function](nf-wdfdmaenabler-wdf_dma_enabler_config_init.md) | The WDF_DMA_ENABLER_CONFIG_INIT function initializes a driver's WDF_DMA_ENABLER_CONFIG structure. |
| [WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT function](nf-wdfdmaenabler-wdf_dma_system_profile_config_init.md) | The WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT function initializes a driver's WDF_DMA_SYSTEM_PROFILE_CONFIG structure. |
| [WdfDmaEnablerConfigureSystemProfile function](nf-wdfdmaenabler-wdfdmaenablerconfiguresystemprofile.md) | The WdfDmaEnablerConfigureSystemProfile method configures the hardware-specific settings for a system-mode DMA enabler and completes the resource initialization. |
| [WdfDmaEnablerCreate function](nf-wdfdmaenabler-wdfdmaenablercreate.md) | The WdfDmaEnablerCreate method creates a DMA enabler object. |
| [WdfDmaEnablerGetFragmentLength function](nf-wdfdmaenabler-wdfdmaenablergetfragmentlength.md) | The WdfDmaEnablerGetFragmentLength method returns the maximum transfer length that the operating system supports for a single DMA transfer. |
| [WdfDmaEnablerGetMaximumLength function](nf-wdfdmaenabler-wdfdmaenablergetmaximumlength.md) | The WdfDmaEnablerGetMaximumLength method returns the maximum transfer length, for a single DMA transfer, that a device supports. |
| [WdfDmaEnablerGetMaximumScatterGatherElements function](nf-wdfdmaenabler-wdfdmaenablergetmaximumscattergatherelements.md) | The WdfDmaEnablerGetMaximumScatterGatherElements method returns the maximum number of scatter/gather elements that the device and driver support, for a specified DMA enabler object. |
| [WdfDmaEnablerSetMaximumScatterGatherElements function](nf-wdfdmaenabler-wdfdmaenablersetmaximumscattergatherelements.md) | The WdfDmaEnablerSetMaximumScatterGatherElements method sets the maximum number of scatter/gather elements that a device supports, for a specified DMA enabler object. |
| [WdfDmaEnablerWdmGetDmaAdapter function](nf-wdfdmaenabler-wdfdmaenablerwdmgetdmaadapter.md) | The WdfDmaEnablerWdmGetDmaAdapter method returns a pointer to a WDM DMA_ADAPTER structure that is associated with a DMA enabler object. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_WDF_DMA_ENABLER_CONFIG structure](ns-wdfdmaenabler-_wdf_dma_enabler_config.md) | The WDF_DMA_ENABLER_CONFIG structure supplies characteristics for a DMA enabler object. |
| [_WDF_DMA_SYSTEM_PROFILE_CONFIG structure](ns-wdfdmaenabler-_wdf_dma_system_profile_config.md) | The WDF_DMA_SYSTEM_PROFILE_CONFIG structure describes the hardware-specific settings related to a system-mode DMA enabler. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_WDF_DMA_DIRECTION enumeration](ne-wdfdmaenabler-_wdf_dma_direction.md) | The WDF_DMA_DIRECTION enumeration defines the direction of a DMA transfer. |
| [_WDF_DMA_ENABLER_CONFIG_FLAGS enumeration](ne-wdfdmaenabler-_wdf_dma_enabler_config_flags.md) | The WDF_DMA_ENABLER_CONFIG_FLAGS enumeration type defines flags that are used in a driver's WDF_DMA_ENABLER_CONFIG structure. |
| [_WDF_DMA_PROFILE enumeration](ne-wdfdmaenabler-_wdf_dma_profile.md) | The WDF_DMA_PROFILE enumeration identifies the types of bus-master or system-mode DMA operations that devices can support. |
