---
UID: NS.d3dkmddi._DXGKARG_SUBMITCOMMANDVIRTUAL
title: DXGKARG_SUBMITCOMMANDVIRTUAL
author: windows-driver-content
description: DXGKARG_SUBMITCOMMANDVIRTUAL is used to submit a direct memory access (DMA) buffer to a context that supports virtual addressing with the DxgkDdiSubmitCommandVirtualdevice driver interface (DDI).
old-location: display\dxgkarg_submitcommandvirtual.htm
old-project: display
ms.assetid: 7BBB4BEC-82F1-44B9-A0C2-1073517A4116
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_SUBMITCOMMANDVIRTUAL, DXGKARG_SUBMITCOMMANDVIRTUAL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_SUBMITCOMMANDVIRTUAL
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

# DXGKARG_SUBMITCOMMANDVIRTUAL structure



## -description
<p><b>DXGKARG_SUBMITCOMMANDVIRTUAL</b> is used to submit a direct memory access (DMA) buffer to a context that supports virtual addressing with the  <a href="display.dxgkddisubmitcommandvirtual">DxgkDdiSubmitCommandVirtual</a>device driver interface (DDI).

</p>


## -syntax

````
typedef struct _DXGKARG_SUBMITCOMMANDVIRTUAL {
  HANDLE                         hContext;
  D3DGPU_VIRTUAL_ADDRESS         DmaBufferVirtualAddress;
  UINT                           DmaBufferSize;
  VOID                           *pDmaBufferPrivateData;
  UINT                           DmaBufferPrivateDataSize;
  UINT                           DmaBufferUmdPrivateDataSize;
  UINT                           SubmissionFenceId;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  D3DDDI_FLIPINTERVAL_TYPE       FlipInterval;
  DXGK_SUBMITCOMMANDFLAGS        Flags;
  UINT                           EngineOrdinal;
  UINT                           NodeOrdinal;
} DXGKARG_SUBMITCOMMANDVIRTUAL;
````


## -struct-fields
<dl>

### -field <b>hContext</b>

<dd>
<p>The handle returned from <a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a>.</p>
</dd>

### -field <b>DmaBufferVirtualAddress</b>

<dd>
<p>The virtual address for the DMA buffer in the context of the submitting process.</p>
</dd>

### -field <b>DmaBufferSize</b>

<dd>
<p>The size of the DMA buffer in bytes.</p>
</dd>

### -field <b>pDmaBufferPrivateData</b>

<dd>
<p>A pointer to the driver-private data buffer.</p>
</dd>

### -field <b>DmaBufferPrivateDataSize</b>

<dd>
<p>The size of the driver-private data buffer in bytes.</p>
</dd>

### -field <b>DmaBufferUmdPrivateDataSize</b>

<dd>
<p>Size of the private driver data, in bytes, that was set by the user mode driver in <b>SubmitCommandCb</b>. When <b>SubmitCommandCb</b> is called, the DirectX graphics kernel allocates a buffer for the private driver data with the size equal to <a href="https://msdn.microsoft.com/library/windows/hardware/ff561019">DXGK_CONTEXTINFO</a>::<b>DmaBufferPrivateDataSize</b>. This size was reported by the kernel mode driver in the <a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a> call. The DirectX graphics kernel copies the driver private data from the <b>SubmitCommandCb</b> to the allocated buffer.</p>
</dd>

### -field <b>SubmissionFenceId</b>

<dd>
<p>A unique identifier that the driver can write into the fence command in the ring buffer, which is the buffer where DMA buffers are queued for the GPU to run. For more information about these types of identifiers, see <a href="https://msdn.microsoft.com/0ec8a4eb-c441-47ae-b5de-d86e6065ffd4">Supplying Fence Identifiers</a>.</p>
</dd>

### -field <b>VidPnSourceId</b>

<dd>
<p>The zero-based identification number of the video present source in a path of a video present network (VidPN) topology for a flip operation. This member is valid only when the <b>Flip</b> or <b>FlipWithNoWait</b> bit-field flag is set in the <b>Flags</b> member.</p>
</dd>

### -field <b>FlipInterval</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>-typed value that indicates the flip interval (that is, if the flip occurs after zero, one, two, three, or four vertical syncs). <b>FlipInterval</b> is valid only if the <b>Flip</b> bit-field flag is set (that is, <b>TRUE</b>) in the <b>Flags</b> member.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562058">DXGK_SUBMITCOMMANDFLAGS</a> structure that identifies information about the DMA buffer to submit.</p>
</dd>

### -field <b>EngineOrdinal</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>NodeOrdinal</b>

<dd>
<p>The zero-based index of the node that the context is created for. Identifies the node when the context is <b>NULL</b>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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
<a href="display.dxgkddisubmitcommandvirtual">DxgkDdiSubmitCommandVirtual</a>
</dt>
<dt>
<a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561019">DXGK_CONTEXTINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0ec8a4eb-c441-47ae-b5de-d86e6065ffd4">Supplying Fence Identifiers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544549">D3DDDI_FLIPINTERVAL_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_SUBMITCOMMANDVIRTUAL structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
