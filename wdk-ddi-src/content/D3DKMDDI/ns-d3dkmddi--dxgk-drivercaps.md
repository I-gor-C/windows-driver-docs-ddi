---
UID: NS.d3dkmddi._DXGK_DRIVERCAPS
title: DXGK_DRIVERCAPS
author: windows-driver-content
description: The DXGK_DRIVERCAPS structure describes capabilities of a display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_drivercaps.htm
ms.assetid: 1ee8eb02-066c-4a54-b31a-cd6644cbce06
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DRIVERCAPS
req.alt-loc: d3dkmddi.h
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
ms.keywords: DXGK_DRIVERCAPS, DXGK_DRIVERCAPS
req.iface: 
---

# DXGK_DRIVERCAPS structure



## -description
<p>The DXGK_DRIVERCAPS structure describes capabilities of a display miniport driver that the driver provides through a call to its <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function.</p>


## -syntax

````
typedef struct _DXGK_DRIVERCAPS {
  PHYSICAL_ADDRESS        HighestAcceptableAddress;
  UINT                    MaxAllocationListSlotId;
  SIZE_T                  ApertureSegmentCommitLimit;
  UINT                    MaxPointerWidth;
  UINT                    MaxPointerHeight;
  DXGK_POINTERFLAGS       PointerCaps;
  UINT                    InterruptMessageNumber;
  UINT                    NumberOfSwizzlingRanges;
  UINT                    MaxOverlays;
  union {
    DXGK_GAMMARAMPCAPS      GammaRampCaps;
    DXGK_COLORTRANSFORMCAPS ColorTransformCaps;
  };
  DXGK_PRESENTATIONCAPS   PresentationCaps;
  UINT                    MaxQueuedFlipOnVSync;
  DXGK_FLIPCAPS           FlipCaps;
  DXGK_VIDSCHCAPS         SchedulingCaps;
  DXGK_VIDMMCAPS          MemoryManagementCaps;
  DXGK_GPUENGINETOPOLOGY  GpuEngineTopology;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN7)
  DXGK_WDDMVERSION        WDDMVersion;
  DXGK_VIRTUALADDRESSCAPS VirtualAddressCaps;
  DXGK_DMABUFFERCAPS      DmaBufferCaps;
#endif 
#if DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8
  D3DKMDT_PREEMPTION_CAPS PreemptionCaps;
  BOOLEAN                 SupportNonVGA;
  BOOLEAN                 SupportSmoothRotation;
  BOOLEAN                 SupportPerEngineTDR;
  BOOLEAN                 SupportDirectFlip;
  BOOLEAN                 SupportMultiPlaneOverlay;
  BOOLEAN                 SupportRuntimePowerManagement;
  BOOLEAN                 SupportSurpriseRemovalInHibernation;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  BOOLEAN                 HybridDiscrete;
  UINT                    MaxOverlayPlanes;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_1)
  BOOLEAN                 SupportMultiPlaneOverlayImmediateFlip;
  BOOLEAN                 CursorScaledWithMultiPlaneOverlayPlane0;
  uint                    MaxQueuedMultiPlaneOverlayFlipVSync;
} DXGK_DRIVERCAPS;
````


## -struct-fields
<dl>

### -field <b>HighestAcceptableAddress</b>

<dd>
<p>[out] A PHYSICAL_ADDRESS data type (which is defined as LARGE_INTEGER) that indicates the highest acceptable physical address of system memory (RAM) to use.</p>
</dd>

### -field <b>MaxAllocationListSlotId</b>

<dd>
<p>[out] The maximum number of allocation-list slot identifiers. An allocation-list slot represents where an allocation is directed in direct memory access (DMA) buffering. </p>
</dd>

### -field <b>ApertureSegmentCommitLimit</b>

<dd>
<p>[out] The maximum number of bytes of physical memory that the display miniport driver supports for mapping into an aperture segment. The video memory manager will not map more physical memory into an aperture segment than the limit that <b>ApertureSegmentCommitLimit</b> specifies. </p>
</dd>

### -field <b>MaxPointerWidth</b>

<dd>
<p>[out] The maximum width of the mouse pointer, in pixels.</p>
</dd>

### -field <b>MaxPointerHeight</b>

<dd>
<p>[out] The maximum height of the mouse pointer, in scan lines.</p>
</dd>

### -field <b>PointerCaps</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561995">DXGK_POINTERFLAGS</a> structure that identifies the mouse pointer capabilities, in bit-field flags, that the driver can support.</p>
</dd>

### -field <b>InterruptMessageNumber</b>

<dd>
<p>[out] The message number that is used if message-signaled interrupts are used and the driver calls the <a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a> function from the interrupt handler corresponding to a fixed message number. </p>
</dd>

### -field <b>NumberOfSwizzlingRanges</b>

<dd>
<p>[out] The number of swizzling ranges that the driver can support. </p>
</dd>

### -field <b>MaxOverlays</b>

<dd>
<p>[out] The maximum number of overlays that the driver can support.</p>
</dd>

### -field <b>GammaRampCaps</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561071">DXGK_GAMMARAMPCAPS</a> structure that identifies the gamma-ramp capabilities, in bit-field flags, that the driver can support.</p>
</dd>

### -field <b>ColorTransformCaps</b>

<dd>
<p>Flags to describe gamma and colorspace transform capabilities of the display pipelines.</p>
<div class="alert"><b>Note</b>  This field replaces the GammaRampCaps in the pre-WDDM 2.2 version of this structure.</div>
<div> </div>
</dd>

### -field <b>PresentationCaps</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a> structure that identifies the presentation capabilities, in bit-field flags, that the driver can support.</p>
</dd>

### -field <b>MaxQueuedFlipOnVSync</b>

<dd>
<p>[out] The number of flips that can be queued and pending at the graphics hardware. Each flip is latched to a digital-to-analog converter (DAC) at every VSync interrupt, in order, as the graphics hardware queues the flip.</p>
</dd>

### -field <b>FlipCaps</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561069">DXGK_FLIPCAPS</a> structure that identifies the flipping capabilities, in bit-field flags, that the driver can support.</p>
</dd>

### -field <b>SchedulingCaps</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562863">DXGK_VIDSCHCAPS</a> structure that identifies the graphics processing unit (GPU) scheduling capabilities, in bit-field flags, that the driver can support.</p>
</dd>

### -field <b>MemoryManagementCaps</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562072">DXGK_VIDMMCAPS</a> structure that identifies the video memory management capabilities that the driver can support.</p>
</dd>

### -field <b>GpuEngineTopology</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561121">DXGK_GPUENGINETOPOLOGY</a> structure that describes the GPU-engine topology that the driver can support.</p>
</dd>

### -field <b>WDDMVersion</b>

<dd>
<p>[out] If a driver supports Windows 7 or later features (DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7), this member is reserved and should be set to zero.</p>
<div class="alert"><b>Note</b>  <p class="note">If a driver does not support Windows 7 or later features (DXGKDDI_INTERFACE_VERSION &lt; DXGKDDI_INTERFACE_VERSION_WIN7), and you want to compile the driver
with the Windows 7 WDK (Version 7600), set this member to DXGKDDI_WDDMv1.</p>
<p class="note">If a driver does not support Windows 7 or later features (DXGKDDI_INTERFACE_VERSION &lt; DXGKDDI_INTERFACE_VERSION_WIN7), and you want to compile the driver
with the Windows 8 WDK, set this member to DXGKDDI_WDDMv1_2.</p>
</div>
<div> </div>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>VirtualAddressCaps</b>

<dd>
<p>[out] This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>DmaBufferCaps</b>

<dd>
<p>[out] This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>PreemptionCaps</b>

<dd>
<p>[out] A <a href="https://msdn.microsoft.com/library/windows/hardware/hh439334">D3DKMDT_PREEMPTION_CAPS</a> structure that describes the capabilities for the preemption of GPU graphics requests that the driver supports.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>SupportNonVGA</b>

<dd>
<p>[out] If <b>TRUE</b>, the driver supports resetting the  display device and releasing ownership of the current  power-on self-test (POST)  device by using the <a href="https://msdn.microsoft.com/6AF170BF-C422-4340-8935-31A4D4F3EFA5">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>SupportSmoothRotation</b>

<dd>
<p>[out] If <b>TRUE</b>, the driver supports updating path rotation on the adapter by using the <a href="https://msdn.microsoft.com/3bf5ebf7-8113-4ab2-beb1-1a52df25ac37">DxgkDdiUpdateActiveVidPnPresentPath</a> function, while not requiring a new VidPN to be created and set.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>SupportPerEngineTDR</b>

<dd>
<p>[out] If <b>TRUE</b>, the driver supports resetting individual GPU engines.</p>
<p>If this member is set, the display miniport driver must implement the <a href="https://msdn.microsoft.com/42040ffc-40a3-4794-805c-7a165c47c8c9">DxgkDdiQueryDependentEngineGroup</a>, <a href="https://msdn.microsoft.com/87c99fcb-d25a-41b1-a1f3-9cf9ab7b141e">DxgkDdiQueryEngineStatus</a>, and <a href="https://msdn.microsoft.com/9c2097b2-5742-422c-a650-7efff2484970">DxgkDdiResetEngine</a> functions.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>SupportDirectFlip</b>

<dd>
<p>[out] If <b>TRUE</b>, the driver supports the creation and opening of shared managed primary allocations. A value of <b>TRUE</b> also indicates the following:</p>
<ul>
<li>The display miniport driver guarantees that when the <a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a> function is called, the driver does not allow video memory to be flipped to an incompatible allocation.</li>
<li>The user mode driver validates Direct Flip resources before the Desktop Windows Manager (DWM) uses them.</li>
</ul>
<p>Only the DWM can flip video memory to Direct Flip resources. The DWM validates these resources using the user-mode <a href="https://msdn.microsoft.com/BB909041-0194-4828-ACA2-E3F6B1974DBB">CheckDirectFlipSupport</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>SupportMultiPlaneOverlay</b>

<dd>
<p>[out] If <b>TRUE</b>, the display miniport driver supports multiplane overlays, and the driver should also set a value for the <b>MaxOverlayPlanes</b> member. If <b>FALSE</b>, the DirectX graphics kernel subsystem will not call multiplane overlay functions.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>SupportRuntimePowerManagement</b>

<dd>
<p>[out] If <b>TRUE</b>, the display miniport driver supports run-time power management.</p>
<p>If this member is set, the display miniport driver must implement the <a href="https://msdn.microsoft.com/C68CC6F1-83D6-43D9-93F3-99E3A990C7D7">DxgkDdiSetPowerComponentFState</a> and <a href="https://msdn.microsoft.com/56535128-3107-4fb5-b0e1-2e913c386cc2">DxgkDdiPowerRuntimeControlRequest</a> functions.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>SupportSurpriseRemovalInHibernation</b>

<dd>
<p>[out] If <b>TRUE</b>, the display miniport driver supports cleaning up software resources after an external display device in hibernation mode is disconnected from the system.</p>
<p>If this member is set, the display miniport driver must implement the <a href="https://msdn.microsoft.com/4e6403e7-7463-479a-8be9-4136287b375e">DxgkDdiNotifySurpriseRemoval</a> function with the <i>RemovalType</i> parameter set to <b>DxgkRemovalHibernation</b>.</p>
<p>For more information, see <a href="https://msdn.microsoft.com/ECBB0AA7-50C2-41C8-9DC6-6EEFC5CEEB15">Using cross-adapter resources in a hybrid system</a>.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>HybridDiscrete</b>

<dd>
<p>[out] If <b>TRUE</b>, the display miniport driver is a discrete GPU in a <a href="display.using_cross-adapter_resources_in_a_hybrid_system#definition_of_a_hybrid_system#definition_of_a_hybrid_system">hybrid system</a>.</p>
<p>If this member is set, the display miniport driver should:<ul>
<li>support WDDM 1.3</li>
<li>support cross-adapter resources</li>
<li>have no display outputs</li>
</ul>
</p>
<p>For more information, see <a href="https://msdn.microsoft.com/ECBB0AA7-50C2-41C8-9DC6-6EEFC5CEEB15">Using cross-adapter resources in a hybrid system</a>.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>MaxOverlayPlanes</b>

<dd>
<p>[out] If <b>SupportRuntimePowerManagement</b> is <b>TRUE</b>, the display miniport driver should set <b>MaxOverlayPlanes</b> to the maximum number of overlay planes that can be simultaneously displayed on a single output, including the primary surface, that it can support. If the number of available planes will change when the operating mode changes, the driver should use a number that reflects the best-case scenario.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>SupportMultiPlaneOverlayImmediateFlip</b>

<dd>
<p>[out] If TRUE, the display miniport driver supports immediate flips to a multiplane overlay plane as long as the only value changing is the physical address to be displayed. </p>
</dd>

### -field <b>CursorScaledWithMultiPlaneOverlayPlane0</b>

<dd>
<p>[out] If TRUE, the display hardware will always apply the same scaling factor to the hardware cursor as is applied to plane 0 when per plane multiplane overlay stretching is applied.</p>
</dd>

### -field <b>MaxQueuedMultiPlaneOverlayFlipVSync</b>

<dd>
<p>[out] Indicates the maximum number of updates to a single plane can be made within a single VSYNC period, where the most recent update overrides the previous update.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/BB909041-0194-4828-ACA2-E3F6B1974DBB">CheckDirectFlipSupport</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439334">D3DKMDT_PREEMPTION_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561069">DXGK_FLIPCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561071">DXGK_GAMMARAMPCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561121">DXGK_GPUENGINETOPOLOGY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561995">DXGK_POINTERFLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562004">DXGK_PRESENTATIONCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562072">DXGK_VIDMMCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562863">DXGK_VIDSCHCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557621">DXGKARG_QUERYADAPTERINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4e6403e7-7463-479a-8be9-4136287b375e">DxgkDdiNotifySurpriseRemoval</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/56535128-3107-4fb5-b0e1-2e913c386cc2">DxgkDdiPowerRuntimeControlRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/42040ffc-40a3-4794-805c-7a165c47c8c9">DxgkDdiQueryDependentEngineGroup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/87c99fcb-d25a-41b1-a1f3-9cf9ab7b141e">DxgkDdiQueryEngineStatus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9c2097b2-5742-422c-a650-7efff2484970">DxgkDdiResetEngine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/C68CC6F1-83D6-43D9-93F3-99E3A990C7D7">DxgkDdiSetPowerComponentFState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6AF170BF-C422-4340-8935-31A4D4F3EFA5">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3bf5ebf7-8113-4ab2-beb1-1a52df25ac37">DxgkDdiUpdateActiveVidPnPresentPath</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_DRIVERCAPS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
