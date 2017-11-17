---
UID: NS.d3dkmddi._DXGKARGCB_NOTIFY_INTERRUPT_DATA
title: DXGKARGCB_NOTIFY_INTERRUPT_DATA
author: windows-driver-content
description: The DXGKARGCB_NOTIFY_INTERRUPT_DATA structure describes notification information.
old-location: display\dxgkargcb_notify_interrupt_data.htm
ms.assetid: c71078fb-5666-4038-81a0-de9375bafb5c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARGCB_NOTIFY_INTERRUPT_DATA
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
ms.keywords: DXGKARGCB_NOTIFY_INTERRUPT_DATA, DXGKARGCB_NOTIFY_INTERRUPT_DATA
req.iface: 
---

# DXGKARGCB_NOTIFY_INTERRUPT_DATA structure



## -description
<p>The DXGKARGCB_NOTIFY_INTERRUPT_DATA structure describes notification information.</p>


## -syntax

````
typedef struct _DXGKARGCB_NOTIFY_INTERRUPT_DATA {
  DXGK_INTERRUPT_TYPE                InterruptType;
  union {
    struct {
      UINT SubmissionFenceId;
      UINT NodeOrdinal;
      UINT EngineOrdinal;
    } DmaCompleted;
    struct {
      UINT PreemptionFenceId;
      UINT LastCompletedFenceId;
      UINT NodeOrdinal;
      UINT EngineOrdinal;
    } DmaPreempted;
    struct {
      UINT     FaultedFenceId;
      NTSTATUS Status;
      UINT     NodeOrdinal;
      UINT     EngineOrdinal;
    } DmaFaulted;
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId;
      PHYSICAL_ADDRESS               PhysicalAddress;
      UINT                           PhysicalAdapterMask;
    } CrtcVsync;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId;
    } DisplayOnlyVsync;
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID     VidPnTargetId;
      UINT                               PhysicalAdapterMask;
      UINT                               MultiPlaneOverlayVsyncInfoCount;
      DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO *pMultiPlaneOverlayVsyncInfo;
    } CrtcVsyncWithMultiPlaneOverlay;
    DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS DisplayOnlyPresentProgress;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
    struct {
      D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId;
      DXGK_MIRACAST_CHUNK_INFO       ChunkInfo;
      PVOID                          pPrivateDriverData;
      UINT                           PrivateDataDriverSize;
      NTSTATUS                       Status;
    } MiracastEncodeChunkCompleted;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
    struct {
      UINT                       FaultedFenceId;
      UINT64                     FaultedPrimitiveAPISequenceNumber;
      DXGK_RENDER_PIPELINE_STAGE FaultedPipelineStage;
      UINT                       FaultedBindTableEntry;
      DXGK_PAGE_FAULT_FLAGS      PageFaultFlags;
      D3DGPU_VIRTUAL_ADDRESS     FaultedVirtualAddress;
      UINT                       NodeOrdinal;
      UINT                       EngineOrdinal;
      UINT                       PageTableLevel;
      DXGK_FAULT_ERROR_CODE      FaultErrorCode;
      HANDLE                     FaultedProcessHandle;
    } DmaPageFaulted;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_2)
    D3DDDI_VIDEO_PRESENT_TARGET_ID         VidPnTargetId;
    UINT                                   PhysicalAdapterMask;
    UINT                                   MultiPlaneOverlayVsyncInfoCount;
    DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO2    *pMultiPlaneOverlayVsyncInfo;
    ULONGLONG                              GpuFrequency;
    ULONGLONG                              GpuClockCounter;
#endif 
    struct {
      UINT Reserved[16];
    } Reserved;
  };
  DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS Flags;
} DXGKARGCB_NOTIFY_INTERRUPT_DATA;
````


## -struct-fields
<dl>

### -field <b>InterruptType</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561136">DXGK_INTERRUPT_TYPE</a>-typed value that indicates the type of interrupt that the display miniport driver notifies the GPU scheduler about.</p>
</dd>

### -field <b>DmaCompleted</b>

<dd>
<dl>

### -field <b>SubmissionFenceId</b>

<dd>
<p>[in] The submission identifier of the completed command.</p>
</dd>

### -field <b>NodeOrdinal</b>

<dd>
<p>[in] The zero-based index of the node that generates the notification.</p>
</dd>

### -field <b>EngineOrdinal</b>

<dd>
<p>[in] The zero-based index of the engine, within the node that <b>NodeOrdinal</b> specifies, that generates the notification. For graphics adapters that are not part of a link, you should always set <b>EngineOrdinal</b> to 0. For graphics adapters that are part of a link, set <b>EngineOrdinal</b> to the adapter index of the adapter in the link that the interrupting engine belongs to.</p>
</dd>
</dl>
</dd>

### -field <b>DmaPreempted</b>

<dd>
<dl>

### -field <b>PreemptionFenceId</b>

<dd>
<p>[in] The submission identifier of the preempting request.</p>
</dd>

### -field <b>LastCompletedFenceId</b>

<dd>
<p>[in] The submission identifier of the last completed command before preemption.</p>
</dd>

### -field <b>NodeOrdinal</b>

<dd>
<p>[in] The zero-based index of the node that generates the notification.</p>
</dd>

### -field <b>EngineOrdinal</b>

<dd>
<p>[in] The zero-based index of the engine, within the node that <b>NodeOrdinal</b> specifies, that generates the notification. For graphics adapters that are not part of a link, you should always set <b>EngineOrdinal</b> set to 0. For graphics adapters that are part of a link, set <b>EngineOrdinal</b> to the adapter index of the adapter in the link that the interrupting engine belongs to. The GPU scheduler determines that hardware preempted all commands between the preemption request and the submission that <b>LastCompletedFenceId</b> specifies.</p>
</dd>
</dl>
</dd>

### -field <b>DmaFaulted</b>

<dd>
<dl>

### -field <b>FaultedFenceId</b>

<dd>
<p>[in] The identifier of the faulty command.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>[in] The status of the faulty command.</p>
</dd>

### -field <b>NodeOrdinal</b>

<dd>
<p>[in] The zero-based index of the node that generates the notification.</p>
</dd>

### -field <b>EngineOrdinal</b>

<dd>
<p>[in] The zero-based index of the engine, within the node that <b>NodeOrdinal</b> specifies, that generates the notification. For graphics adapters that are not part of a link, you should always set <b>EngineOrdinal</b> to 0. For graphics adapters that are part of a link, set <b>EngineOrdinal</b> to the adapter index of the adapter in the link that the interrupting engine belongs to. </p>
</dd>
</dl>
</dd>

### -field <b>CrtcVsync</b>

<dd>
<dl>

### -field <b>VidPnTargetId</b>

<dd>
<p>[in] The zero-based identification number of the video present target in a path of a video present network (VidPN) topology. This number represents the video present target where the vertical sync occurs.</p>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>[in] The physical address of the displaying buffer. When monitor visibility is off, the operating system still expects a non-<b>NULL</b> physical address. This address should be set to the physical address that the pixel pipeline would read from if visibility were on.</p>
</dd>

### -field <b>PhysicalAdapterMask</b>

<dd>
<p>[in] The physical adapter mask where the vertical sync occurs. If this member contains a valid value, the driver must also set the <b>ValidPhysicalAdapterMask</b> bit-field flag in the <b>Flags</b> member. </p>
</dd>
</dl>
</dd>

### -field <b>DisplayOnlyVsync</b>

<dd>
<dl>

### -field <b>VidPnTargetId</b>

<dd>
<p>[in] For a display-only driver, the zero-based identification number of the video present target in a path of a video present network (VidPN) topology. This number represents the video present target where the vertical sync occurs.</p>
<p>Supported starting with Windows 8.</p>
</dd>
</dl>
</dd>

### -field <b>CrtcVsyncWithMultiPlaneOverlay</b>

<dd>
<p>Provides VSync notifications for display miniport drivers that support multiplane overlays.</p>
<dl>

### -field <b>VidPnTargetId</b>

<dd>
<p>[in] The zero-based identification number of the video present target in a path of a video present network (VidPN) topology. This number represents the video present target where the vertical sync occurs.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>PhysicalAdapterMask</b>

<dd>
<p>[in] The physical adapter mask where the vertical sync occurs. If this member contains a valid value, the driver must also set the <b>ValidPhysicalAdapterMask</b> bit-field flag in the <b>Flags</b> member.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>MultiPlaneOverlayVsyncInfoCount</b>

<dd>
<p>The number of overlay planes that are available to display.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pMultiPlaneOverlayVsyncInfo</b>

<dd>
<p>[in] A pointer to  a <a href="https://msdn.microsoft.com/library/windows/hardware/hh780309">DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO</a> structure that specifies an overlay plane to display during a VSync interval.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>
</dl>
</dd>

### -field <b>DisplayOnlyPresentProgress</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/hh451245">DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS</a> structure that provides the progress of a kernel mode display-only driver's (KMDOD) present operation.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>MiracastEncodeChunkCompleted</b>

<dd>
<p>Supported by WDDM 1.3 and later display miniport drivers running on Windows 8.1 and later.</p>
<dl>

### -field <b>VidPnTargetId</b>

<dd>
<p>[in] The zero-based identification number of the video present target in a path of a video present network (VidPN) topology. This number represents the video present target where the encoding is being performed.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>ChunkInfo</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/dn322056">DXGK_MIRACAST_CHUNK_INFO</a> encode chunk information structure that the display miniport driver wants to report.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>A pointer to a block of private data that describes this encode chunk. </p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>PrivateDataDriverSize</b>

<dd>
<p>The size, in bytes, of the block of private data in <b>pPrivateDriverData</b>.
This value must not be larger than the <b>MaxChunkPrivateDriverDataSize</b> value that the driver reported in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn322054">DXGK_MIRACAST_CAPS</a> structure.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>A value of type <b>NTSTATUS</b> that indicates whether the encode chunk was successfully added to the queue of chunks. If successful, <b>STATUS_SUCCESS</b> is returned. If any other value is returned, the chunk could not be added to the queue, and all outstanding chunks will be lost.</p>
<p>Supported starting with Windows 8.1.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="STATUS_SUCCESS"></a><a id="status_success"></a><dl>

### -field <b>STATUS_SUCCESS</b>

</dl>
</td>
<td width="60%">
<p>The chunk was successfully added to the queue.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STATUS_INVALID_PARAMETER"></a><a id="status_invalid_parameter"></a><dl>

### -field <b>STATUS_INVALID_PARAMETER</b>

</dl>
</td>
<td width="60%">
<p>Parameters were validated and determined to be incorrect.
</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STATUS_NO_MEMORY"></a><a id="status_no_memory"></a><dl>

### -field <b>STATUS_NO_MEMORY</b>

</dl>
</td>
<td width="60%">
<p>The interrupt-service-routine (ISR) ran out of free encode chunks.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
</dd>

### -field <b>DmaPageFaulted</b>

<dd>
<dl>

### -field <b>FaultedFenceId</b>

<dd>
<p>Submission fence ID of faulted command.</p>
<p>
If the faulted fence cannot be determined reliably, <b>PageFaultFlags</b> should have <b>DXGK_PAGE_FAULT_FENCE_INVALID</b> bit set, and <b>FaultedFenceId</b> should be set to 0.
</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>FaultedPrimitiveAPISequenceNumber</b>

<dd>
<p> When per draw fence write is enabled, this identifies the draw operation that caused the page fault, or <b>DXGK_PRIMITIVE_API_SEQUENCE_NUMBER_UNKNOWN</b> if such information is not available.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>FaultedPipelineStage</b>

<dd>
<p>Render pipeline stage during which the fault was generated, or <b>DXGK_RENDER_PIPELINE_STAGE_UNKNOWN</b> if such information is not available.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>FaultedBindTableEntry</b>

<dd>
<p>A bind table index of a resource being accessed at the time of the fault, or <b>DXGK_BIND_TABLE_ENTRY_UNKNOWN</b> if such information is not available.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>PageFaultFlags</b>

<dd>
<p>Flags described in <a href="https://msdn.microsoft.com/library/windows/hardware/dn906831">DXGK_PAGE_FAULT_FLAGS</a> enumeration specifying the nature of the fault.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>FaultedVirtualAddress</b>

<dd>
<p>GPU virtual address of fault, or <b>D3DGPU_NULL</b> if the fault has another cause. In the latter case, <b>FaultErrorCode</b> field should be used to describe the GPU error.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>NodeOrdinal</b>

<dd>
<p>Node ordinal of the engine generating the notification.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>EngineOrdinal</b>

<dd>
<p>Engine ordinal of the engine generating the notification.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>PageTableLevel</b>

<dd>
<p>Describes page table level that the faulting operation was attempted on.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>FaultErrorCode</b>

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906346">DXGK_FAULT_ERROR_CODE</a> structure describing the error.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>FaultedProcessHandle</b>

<dd>
<p>DirectX graphics kernel process handle of the process that generated page fault, or <b>NULL</b> if the faulted process cannot be determined.</p>
<p>Supported starting with Windows 10.</p>
</dd>
</dl>
</dd>

### -field <b>VidPnTargetId</b>

<dd>
<p>The zero-based identification number of the video present target in a path of a video present network (VidPN) topology. This number represents the video present target where the vertical sync occurs.</p>
</dd>

### -field <b>PhysicalAdapterMask</b>

<dd>
<p>The physical adapter mask where the vertical sync occurs. If this member contains a valid value, the driver must also set the ValidPhysicalAdapterMask bit-field flag in the Flags member.</p>
</dd>

### -field <b>MultiPlaneOverlayVsyncInfoCount</b>

<dd>
<p>The number of overlay planes that are available to display.</p>
</dd>

### -field <b>pMultiPlaneOverlayVsyncInfo</b>

<dd>
<p>A pointer to a DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO2 structure that specifies information for each overlay plane updated by the VSync.</p>
</dd>

### -field <b>GpuFrequency</b>

<dd>
<p>The frequency of the GPU clock counter. </p>
</dd>

### -field <b>GpuClockCounter</b>

<dd>
<p>The GPU clock counter at the time of the VSYNC interrupt. Combined with GpuFrequency, this indicates the time of the VSYNC interrupt. </p>
</dd>

### -field <b>Reserved</b>

<dd>
<dl>

### -field <b>Reserved</b>

<dd>
<p>An array of 32-bit values that are reserved for future use.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff559579">DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS</a> structure that indicates if the display miniport driver provides a physical adapter mask in a call to the <a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a> function.</p>
</dd>
</dl>

## -remarks
<p>Depending on the value in the <b>InterruptType</b> member, the display miniport driver should set the appropriate union member in the DXGKARGCB_NOTIFY_INTERRUPT_DATA structure. For example, for the end of a direct memory access (DMA) buffer fence, which corresponds to a value of DXGK_INTERRUPT_DMA_COMPLETED in <b>InterruptType</b>, the driver must set a value in the <b>SubmissionFenceId</b> member of the <b>DmaCompleted</b> member. This value should be the DMA buffer fence identifier, which the driver's <a href="https://msdn.microsoft.com/de1925ab-e444-4cf6-acd9-8fdab26afcec">DxgkDdiSubmitCommand</a> function assigned to the just completed DMA buffer.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561136">DXGK_INTERRUPT_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn322054">DXGK_MIRACAST_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn322056">DXGK_MIRACAST_CHUNK_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh780309">DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451245">DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559579">DXGKCB_NOTIFY_INTERRUPT_DATA_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7968d26d-0195-463d-8954-e7ebef4f9dea">DxgkCbNotifyInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/de1925ab-e444-4cf6-acd9-8fdab26afcec">DxgkDdiSubmitCommand</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906831">DXGK_PAGE_FAULT_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARGCB_NOTIFY_INTERRUPT_DATA structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
