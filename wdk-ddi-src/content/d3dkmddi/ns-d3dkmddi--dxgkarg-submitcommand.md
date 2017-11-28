---
UID: NS.d3dkmddi._DXGKARG_SUBMITCOMMAND
title: DXGKARG_SUBMITCOMMAND
author: windows-driver-content
description: The DXGKARG_SUBMITCOMMAND structure describes the direct memory access (DMA) buffer that a display miniport driver submits to the hardware command execution unit.
old-location: display\dxgkarg_submitcommand.htm
old-project: display
ms.assetid: f0b5c7aa-855e-419a-ac27-c9f4edefd648
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_SUBMITCOMMAND, DXGKARG_SUBMITCOMMAND
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_SUBMITCOMMAND
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
req.iface: 
---

# DXGKARG_SUBMITCOMMAND structure



## -description
<p>The DXGKARG_SUBMITCOMMAND structure describes the direct memory access (DMA) buffer that a display miniport driver submits to the hardware command execution unit.</p>


## -syntax

````
typedef struct _DXGKARG_SUBMITCOMMAND {
  union {
    HANDLE hDevice;
    HANDLE hContext;
  };
  UINT                           DmaBufferSegmentId;
  PHYSICAL_ADDRESS               DmaBufferPhysicalAddress;
  UINT                           DmaBufferSize;
  UINT                           DmaBufferSubmissionStartOffset;
  UINT                           DmaBufferSubmissionEndOffset;
  VOID                           *pDmaBufferPrivateData;
  UINT                           DmaBufferPrivateDataSize;
  UINT                           DmaBufferPrivateDataSubmissionStartOffset;
  UINT                           DmaBufferPrivateDataSubmissionEndOffset;
  UINT                           SubmissionFenceId;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  D3DDDI_FLIPINTERVAL_TYPE       FlipInterval;
  DXGK_SUBMITCOMMANDFLAGS        Flags;
  UINT                           EngineOrdinal;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN7)
  D3DGPU_VIRTUAL_ADDRESS         DmaBufferVirtualAddress;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  UINT                           NodeOrdinal;
#endif 
} DXGKARG_SUBMITCOMMAND;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] If the driver is not multiple-engine aware (that is, the driver does not support context creation), a handle to the display device (graphics context) that the submission request originated from. A device handle is supplied to the driver's <a href="display.dxgkddisubmitcommand">DxgkDdiSubmitCommand</a> function in the union that DXGKARG_SUBMITCOMMAND contains.</p>
<p>For some paging operations, <b>hDevice</b> is <b>NULL</b> (for example, paging operations that evict the content of the entire frame buffer during power management). Paging operations are indicated by the <b>Paging</b> bit-field flag in the <b>Flags</b> member. </p>
</dd>

### -field <b>hContext</b>

<dd>
<p>[in] If the driver is multiple-engine aware (that is, the driver supports context creation), a handle to the device context that the submission request originated from. A context handle is supplied to the driver's <a href="display.dxgkddisubmitcommand">DxgkDdiSubmitCommand</a> function in the union that DXGKARG_SUBMITCOMMAND contains. </p>
<p>For some paging operations, <b>hContext</b> is <b>NULL</b> (for example, paging operations that evict the content of the entire frame buffer during power management). Paging operations are indicated by the <b>Paging</b> bit-field flag in the <b>Flags</b> member.</p>
</dd>

### -field <b>DmaBufferSegmentId</b>

<dd>
<p>[in] The identifier of the memory segment that the DMA buffer was paged in. </p>
<p>The identifier can be zero if the driver indicated not to map the DMA buffer into the segment by setting the <b>DmaBufferSegmentSet</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561019">DXGK_CONTEXTINFO</a> structure to 0 in a call to the driver's <a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a> function. If <b>DmaBufferSegmentId</b> is zero, the DMA buffer was allocated as a contiguous block of system memory.  </p>
</dd>

### -field <b>DmaBufferPhysicalAddress</b>

<dd>
<p>[in] A PHYSICAL_ADDRESS data type (which is defined as LARGE_INTEGER) that indicates the physical address where the DMA buffer was paged in. </p>
<p>If <b>DmaBufferSegmentId</b> is zero, <b>DmaBufferPhysicalAddress</b> is the physical address in system memory where the DMA buffer is located. </p>
<p>If <b>DmaBufferSegmentId</b> is nonzero, <b>DmaBufferPhysicalAddress</b> is the segment physical address for the DMA buffer (that is, DXGK_SEGMENTDESCRIPTOR.BaseAddress + DmaBuffer.SegmentOffset). </p>
<p>Note that <b>DmaBufferPhysicalAddress</b> always refers to the beginning of the DMA buffer even though the driver might be required to patch or submit a section of the DMA buffer that does not include the beginning of the DMA buffer (that is, if the <b>DmaBufferSubmissionStartOffset</b> member is nonzero). </p>
</dd>

### -field <b>DmaBufferSize</b>

<dd>
<p>[in] The size, in bytes, of the DMA buffer.</p>
<p>Note that <b>DmaBufferSize</b> represents the entire length of the DMA buffer; however, the request to patch or submit might refer to only a portion of the DMA buffer. </p>
</dd>

### -field <b>DmaBufferSubmissionStartOffset</b>

<dd>
<p>[in] The offset, in bytes, from the beginning of the DMA buffer to the start of the portion of the DMA buffer that requires patching or submitting. The offset that is received at patch time matches the offset that is received at submission time. </p>
</dd>

### -field <b>DmaBufferSubmissionEndOffset</b>

<dd>
<p>[in] The offset, in bytes, from the beginning of the DMA buffer to the end of the portion of the DMA buffer that requires patching or submitting. The offset that is received at patch time matches the offset that is received at submission time. </p>
</dd>

### -field <b>pDmaBufferPrivateData</b>

<dd>
<p>[in] A pointer to the driver-resident private data that is associated with the DMA buffer that was filled during the <a href="display.dxgkddirender">DxgkDdiRender</a>, <a href="display.dxgkddipresent">DxgkDdiPresent</a>, or <a href="display.dxgkddipatch">DxgkDdiPatch</a> function. </p>
<p>For paging operations, a single paging buffer is used for multiple independent submissions. In that scenario, the driver can indicate--by returning the appropriate private driver data pointer in a call to its <a href="display.dxgkddibuildpagingbuffer">DxgkDdiBuildPagingBuffer</a> function--to have either a single driver private data range for all of the submissions or one for each submission. </p>
</dd>

### -field <b>DmaBufferPrivateDataSize</b>

<dd>
<p>[in] The size, in byte,s of the private driver data that <b>pDmaBufferPrivateData</b> points to.</p>
<p>Note that <b>DmaBufferPrivateDataSize</b> represents the entire length of the private driver data buffer; however, the portion that is associated with the current submission might be smaller. </p>
</dd>

### -field <b>DmaBufferPrivateDataSubmissionStartOffset</b>

<dd>
<p>[in] The offset, in bytes, from the beginning of the DMA buffer private data that <b>pDmaBufferPrivateData</b> specifies to the start of the portion of the private data that is associated with the current submission. <b>DmaBufferPrivateDataSubmissionStartOffset</b> is always zero for a nonpaging request. </p>
</dd>

### -field <b>DmaBufferPrivateDataSubmissionEndOffset</b>

<dd>
<p>[in] The offset, in bytes, from the beginning of the DMA buffer private data that <b>pDmaBufferPrivateData</b> specifies to the end of the portion of the private data that is associated with the current submission. </p>
</dd>

### -field <b>SubmissionFenceId</b>

<dd>
<p>[in] A unique identifier that the driver can write into the fence command in the ring buffer, which is the buffer where DMA buffers are queued for the graphics processing unit (GPU) to run. For more information about these types of identifiers, see <a href="https://msdn.microsoft.com/0ec8a4eb-c441-47ae-b5de-d86e6065ffd4">Supplying Fence Identifiers</a>.</p>
</dd>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology for a flip operation. This member is valid only when the <b>Flip</b> or <b>FlipWithNoWait</b> bit-field flag is set in the <b>Flags</b> member. </p>
</dd>

### -field <b>FlipInterval</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>-typed value that indicates the flip interval (that is, if the flip occurs after zero, one, two, three, or four vertical syncs). <b>FlipInterval</b> is valid only if the <b>Flip</b> bit-field flag is set (that is, <b>TRUE</b>) in the <b>Flags</b> member.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562058">DXGK_SUBMITCOMMANDFLAGS</a> structure that identifies information about the DMA buffer to submit.</p>
</dd>

### -field <b>EngineOrdinal</b>

<dd>
<p>[in] Reserved for future use.</p>
</dd>

### -field <b>DmaBufferVirtualAddress</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>NodeOrdinal</b>

<dd>
<p>The zero-based index of the node that the context is created for. Identifies the node when the context is <b>NULL</b>.</p>
<p>Supported starting with Windows 8.</p>
</dd>
</dl>

## -remarks
<p>The display miniport driver's <a href="display.dxgkddisubmitcommand">DxgkDdiSubmitCommand</a> function must be aware that multiple processes can access the device object that the <b>hDevice</b> member specifies at the same time.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561019">DXGK_CONTEXTINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562058">DXGK_SUBMITCOMMANDFLAGS</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-notify-dpc.md">DxgkCbNotifyDpc</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-notify-interrupt.md">DxgkCbNotifyInterrupt</a>
</dt>
<dt>
<a href="display.dxgkddibuildpagingbuffer">DxgkDdiBuildPagingBuffer</a>
</dt>
<dt>
<a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a>
</dt>
<dt>
<a href="display.dxgkddipatch">DxgkDdiPatch</a>
</dt>
<dt>
<a href="display.dxgkddipresent">DxgkDdiPresent</a>
</dt>
<dt>
<a href="display.dxgkddirender">DxgkDdiRender</a>
</dt>
<dt>
<a href="display.dxgkddisubmitcommand">DxgkDdiSubmitCommand</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_SUBMITCOMMAND structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
