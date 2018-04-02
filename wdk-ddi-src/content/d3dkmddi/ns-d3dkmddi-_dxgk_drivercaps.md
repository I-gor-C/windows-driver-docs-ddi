---
UID: NS:d3dkmddi._DXGK_DRIVERCAPS
title: "_DXGK_DRIVERCAPS"
author: windows-driver-content
description: The DXGK_DRIVERCAPS structure describes capabilities of a display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_drivercaps.htm
old-project: display
ms.assetid: 1ee8eb02-066c-4a54-b31a-cd6644cbce06
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_DRIVERCAPS, DXGK_DRIVERCAPS structure [Display Devices], DmStructs_4a8b7d02-5b36-4a4b-980f-edfc96b4efd3.xml, _DXGK_DRIVERCAPS, d3dkmddi/DXGK_DRIVERCAPS, display.dxgk_drivercaps
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_DRIVERCAPS
product: Windows
targetos: Windows
req.typenames: DXGK_DRIVERCAPS
---

# _DXGK_DRIVERCAPS structure
The DXGK_DRIVERCAPS structure describes capabilities of a display miniport driver that the driver provides through a call to its <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function.

## Syntax
```
typedef struct _DXGK_DRIVERCAPS {
  PHYSICAL_ADDRESS                   HighestAcceptableAddress;
  UINT                               MaxAllocationListSlotId;
  SIZE_T                             ApertureSegmentCommitLimit;
  UINT                               MaxPointerWidth;
  UINT                               MaxPointerHeight;
  DXGK_POINTERFLAGS                  PointerCaps;
  UINT                               InterruptMessageNumber;
  UINT                               NumberOfSwizzlingRanges;
  UINT                               MaxOverlays;
  union {
    DXGK_COLORTRANSFORMCAPS ColorTransformCaps;
    DXGK_GAMMARAMPCAPS      GammaRampCaps;
  };
  DXGK_PRESENTATIONCAPS              PresentationCaps;
  UINT                               MaxQueuedFlipOnVSync;
  DXGK_FLIPCAPS                      FlipCaps;
  DXGK_VIDSCHCAPS                    SchedulingCaps;
  DXGK_VIDMMCAPS                     MemoryManagementCaps;
  DXGK_GPUENGINETOPOLOGY             GpuEngineTopology;
  DXGK_WDDMVERSION                   WDDMVersion;
  DXGK_VIRTUALADDRESSCAPS_DEPRECATED Reserved;
  DXGK_DMABUFFERCAPS_DEPRECATED      Reserved1;
  D3DKMDT_PREEMPTION_CAPS            PreemptionCaps;
  BOOLEAN                            SupportNonVGA;
  BOOLEAN                            SupportSmoothRotation;
  BOOLEAN                            SupportPerEngineTDR;
  BOOLEAN                            SupportDirectFlip;
  BOOLEAN                            SupportMultiPlaneOverlay;
  BOOLEAN                            SupportRuntimePowerManagement;
  BOOLEAN                            SupportSurpriseRemovalInHibernation;
  BOOLEAN                            HybridDiscrete;
  UINT                               MaxOverlayPlanes;
  BOOLEAN                            HybridIntegrated;
  D3DGPU_VIRTUAL_ADDRESS             InternalGpuVirtualAddressRangeStart;
  D3DGPU_VIRTUAL_ADDRESS             InternalGpuVirtualAddressRangeEnd;
  BOOLEAN                            SupportSurpriseRemoval;
  BOOLEAN                            SupportMultiPlaneOverlayImmediateFlip;
  BOOLEAN                            CursorScaledWithMultiPlaneOverlayPlane0;
  BOOLEAN                            HybridAcpiChainingRequired;
  UINT                               MaxQueuedMultiPlaneOverlayFlipVSync;
} DXGK_DRIVERCAPS;
```

## Members


`HighestAcceptableAddress`

[out] A PHYSICAL_ADDRESS data type (which is defined as LARGE_INTEGER) that indicates the highest acceptable physical address of system memory (RAM) to use.

`MaxAllocationListSlotId`

[out] The maximum number of allocation-list slot identifiers. An allocation-list slot represents where an allocation is directed in direct memory access (DMA) buffering.

`ApertureSegmentCommitLimit`

[out] The maximum number of bytes of physical memory that the display miniport driver supports for mapping into an aperture segment. The video memory manager will not map more physical memory into an aperture segment than the limit that <b>ApertureSegmentCommitLimit</b> specifies.

`MaxPointerWidth`

[out] The maximum width of the mouse pointer, in pixels.

`MaxPointerHeight`

[out] The maximum height of the mouse pointer, in scan lines.

`PointerCaps`

[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561995">DXGK_POINTERFLAGS</a> structure that identifies the mouse pointer capabilities, in bit-field flags, that the driver can support.

`InterruptMessageNumber`

[out] The message number that is used if message-signaled interrupts are used and the driver calls the <a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a> function from the interrupt handler corresponding to a fixed message number.

`NumberOfSwizzlingRanges`

[out] The number of swizzling ranges that the driver can support.

`MaxOverlays`

[out] The maximum number of overlays that the driver can support.

`PresentationCaps`

[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a> structure that identifies the presentation capabilities, in bit-field flags, that the driver can support.

`MaxQueuedFlipOnVSync`

[out] The number of flips that can be queued and pending at the graphics hardware. Each flip is latched to a digital-to-analog converter (DAC) at every VSync interrupt, in order, as the graphics hardware queues the flip.

`FlipCaps`

[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561069">DXGK_FLIPCAPS</a> structure that identifies the flipping capabilities, in bit-field flags, that the driver can support.

`SchedulingCaps`

[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562863">DXGK_VIDSCHCAPS</a> structure that identifies the graphics processing unit (GPU) scheduling capabilities, in bit-field flags, that the driver can support.

`MemoryManagementCaps`

[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562072">DXGK_VIDMMCAPS</a> structure that identifies the video memory management capabilities that the driver can support.

`GpuEngineTopology`

[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561121">DXGK_GPUENGINETOPOLOGY</a> structure that describes the GPU-engine topology that the driver can support.

`WDDMVersion`

[out] If a driver supports Windows 7 or later features (DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7), this member is reserved and should be set to zero.

<div class="alert"><b>Note</b>  <p class="note">If a driver does not support Windows 7 or later features (DXGKDDI_INTERFACE_VERSION &lt; DXGKDDI_INTERFACE_VERSION_WIN7), and you want to compile the driver
with the Windows 7 WDK (Version 7600), set this member to DXGKDDI_WDDMv1.

<p class="note">If a driver does not support Windows 7 or later features (DXGKDDI_INTERFACE_VERSION &lt; DXGKDDI_INTERFACE_VERSION_WIN7), and you want to compile the driver
with the Windows 8 WDK, set this member to DXGKDDI_WDDMv1_2.

</div>
<div> </div>
Supported starting with Windows 7.

`Reserved`



`Reserved1`



`PreemptionCaps`

[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/hh439334">D3DKMDT_PREEMPTION_CAPS</a> structure that describes the capabilities for the preemption of GPU graphics requests that the driver supports.

Supported starting with Windows 8.

`SupportNonVGA`

[out] If <b>TRUE</b>, the driver supports resetting the  display device and releasing ownership of the current  power-on self-test (POST)  device by using the <a href="https://msdn.microsoft.com/6AF170BF-C422-4340-8935-31A4D4F3EFA5">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a> function.

Supported starting with Windows 8.

`SupportSmoothRotation`

[out] If <b>TRUE</b>, the driver supports updating path rotation on the adapter by using the <a href="https://msdn.microsoft.com/3bf5ebf7-8113-4ab2-beb1-1a52df25ac37">DxgkDdiUpdateActiveVidPnPresentPath</a> function, while not requiring a new VidPN to be created and set.

Supported starting with Windows 8.

`SupportPerEngineTDR`

[out] If <b>TRUE</b>, the driver supports resetting individual GPU engines.

If this member is set, the display miniport driver must implement the <a href="https://msdn.microsoft.com/42040ffc-40a3-4794-805c-7a165c47c8c9">DxgkDdiQueryDependentEngineGroup</a>, <a href="https://msdn.microsoft.com/87c99fcb-d25a-41b1-a1f3-9cf9ab7b141e">DxgkDdiQueryEngineStatus</a>, and <a href="https://msdn.microsoft.com/9c2097b2-5742-422c-a650-7efff2484970">DxgkDdiResetEngine</a> functions.

Supported starting with Windows 8.

`SupportDirectFlip`

[out] If <b>TRUE</b>, the driver supports the creation and opening of shared managed primary allocations. A value of <b>TRUE</b> also indicates the following:

<ul>
<li>The display miniport driver guarantees that when the <a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a> function is called, the driver does not allow video memory to be flipped to an incompatible allocation.</li>
<li>The user mode driver validates Direct Flip resources before the Desktop Windows Manager (DWM) uses them.</li>
</ul>
Only the DWM can flip video memory to Direct Flip resources. The DWM validates these resources using the user-mode <a href="https://msdn.microsoft.com/BB909041-0194-4828-ACA2-E3F6B1974DBB">CheckDirectFlipSupport</a> function.

Supported starting with Windows 8.

`SupportMultiPlaneOverlay`

[out] If <b>TRUE</b>, the display miniport driver supports multiplane overlays, and the driver should also set a value for the <b>MaxOverlayPlanes</b> member. If <b>FALSE</b>, the DirectX graphics kernel subsystem will not call multiplane overlay functions.

Supported starting with Windows 8.1.

`SupportRuntimePowerManagement`

[out] If <b>TRUE</b>, the display miniport driver supports run-time power management.

If this member is set, the display miniport driver must implement the <a href="https://msdn.microsoft.com/C68CC6F1-83D6-43D9-93F3-99E3A990C7D7">DxgkDdiSetPowerComponentFState</a> and <a href="https://msdn.microsoft.com/56535128-3107-4fb5-b0e1-2e913c386cc2">DxgkDdiPowerRuntimeControlRequest</a> functions.

Supported starting with Windows 8.

`SupportSurpriseRemovalInHibernation`

[out] If <b>TRUE</b>, the display miniport driver supports cleaning up software resources after an external display device in hibernation mode is disconnected from the system.

If this member is set, the display miniport driver must implement the <a href="https://msdn.microsoft.com/4e6403e7-7463-479a-8be9-4136287b375e">DxgkDdiNotifySurpriseRemoval</a> function with the <i>RemovalType</i> parameter set to <b>DxgkRemovalHibernation</b>.

For more information, see <a href="https://msdn.microsoft.com/ECBB0AA7-50C2-41C8-9DC6-6EEFC5CEEB15">Using cross-adapter resources in a hybrid system</a>.

Supported starting with Windows 8.

`HybridDiscrete`

[out] If <b>TRUE</b>, the display miniport driver is a discrete GPU in a <a href="https://msdn.microsoft.com/ECBB0AA7-50C2-41C8-9DC6-6EEFC5CEEB15">hybrid system</a>.

If this member is set, the display miniport driver should:<ul>
<li>support WDDM 1.3</li>
<li>support cross-adapter resources</li>
<li>have no display outputs</li>
</ul>


For more information, see <a href="https://msdn.microsoft.com/ECBB0AA7-50C2-41C8-9DC6-6EEFC5CEEB15">Using cross-adapter resources in a hybrid system</a>.

Supported starting with Windows 8.1.

`MaxOverlayPlanes`

[out] If <b>SupportRuntimePowerManagement</b> is <b>TRUE</b>, the display miniport driver should set <b>MaxOverlayPlanes</b> to the maximum number of overlay planes that can be simultaneously displayed on a single output, including the primary surface, that it can support. If the number of available planes will change when the operating mode changes, the driver should use a number that reflects the best-case scenario.

Supported starting with Windows 8.1.

`HybridIntegrated`



`InternalGpuVirtualAddressRangeStart`



`InternalGpuVirtualAddressRangeEnd`



`SupportSurpriseRemoval`



`SupportMultiPlaneOverlayImmediateFlip`

[out] If TRUE, the display miniport driver supports immediate flips to a multiplane overlay plane as long as the only value changing is the physical address to be displayed.

`CursorScaledWithMultiPlaneOverlayPlane0`

[out] If TRUE, the display hardware will always apply the same scaling factor to the hardware cursor as is applied to plane 0 when per plane multiplane overlay stretching is applied.

`HybridAcpiChainingRequired`



`MaxQueuedMultiPlaneOverlayFlipVSync`

[out] Indicates the maximum number of updates to a single plane can be made within a single VSYNC period, where the most recent update overrides the previous update.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/BB909041-0194-4828-ACA2-E3F6B1974DBB">CheckDirectFlipSupport</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439334">D3DKMDT_PREEMPTION_CAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557621">DXGKARG_QUERYADAPTERINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561069">DXGK_FLIPCAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561071">DXGK_GAMMARAMPCAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561121">DXGK_GPUENGINETOPOLOGY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561995">DXGK_POINTERFLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562072">DXGK_VIDMMCAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562863">DXGK_VIDSCHCAPS</a>



<a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a>



<a href="https://msdn.microsoft.com/4e6403e7-7463-479a-8be9-4136287b375e">DxgkDdiNotifySurpriseRemoval</a>



<a href="https://msdn.microsoft.com/56535128-3107-4fb5-b0e1-2e913c386cc2">DxgkDdiPowerRuntimeControlRequest</a>



<a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a>



<a href="https://msdn.microsoft.com/42040ffc-40a3-4794-805c-7a165c47c8c9">DxgkDdiQueryDependentEngineGroup</a>



<a href="https://msdn.microsoft.com/87c99fcb-d25a-41b1-a1f3-9cf9ab7b141e">DxgkDdiQueryEngineStatus</a>



<a href="https://msdn.microsoft.com/9c2097b2-5742-422c-a650-7efff2484970">DxgkDdiResetEngine</a>



<a href="https://msdn.microsoft.com/C68CC6F1-83D6-43D9-93F3-99E3A990C7D7">DxgkDdiSetPowerComponentFState</a>



<a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a>



<a href="https://msdn.microsoft.com/6AF170BF-C422-4340-8935-31A4D4F3EFA5">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a>



<a href="https://msdn.microsoft.com/3bf5ebf7-8113-4ab2-beb1-1a52df25ac37">DxgkDdiUpdateActiveVidPnPresentPath</a>