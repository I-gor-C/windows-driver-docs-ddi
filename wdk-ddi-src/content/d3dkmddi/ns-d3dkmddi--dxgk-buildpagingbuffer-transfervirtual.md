---
UID: NS.d3dkmddi._DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL
title: DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL
author: windows-driver-content
description: DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL is used as part of an allocation transfer operation.
old-location: display\dxgk_buildpagingbuffer_transfervirtual.htm
old-project: display
ms.assetid: D4427E44-204F-490C-9EE7-BBC4906E5920
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL, DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL
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
req.alt-api: DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL
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

# DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL structure



## -description
<p><b>DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL</b> is used as part of an allocation transfer operation.</p>


## -syntax

````
typedef struct _DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL {
  HANDLE                         hAllocation;
  UINT64                         AllocationOffsetInBytes;
  UINT64                         TransferSizeInBytes;
  D3DGPU_VIRTUAL_ADDRESS         SourceVirtualAddress;
  D3DGPU_VIRTUAL_ADDRESS         DestinationVirtualAddress;
  D3DGPU_VIRTUAL_ADDRESS         SourcePageTable;
  DXGK_MEMORY_TRANSFER_DIRECTION TransferDirection;
  DXGK_TRANSFERVIRTUALFLAGS      Flags;
  D3DGPU_VIRTUAL_ADDRESS         DestinationPageTable;
} DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL;
````


## -struct-fields
<dl>

### -field <b>hAllocation</b>

<dd>
<p>Kernel mode driver handle of the transferred allocation content. The handle is returned from <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>. The allocation properties are needed to perform special transfers (as swizzle, de-swizzle, etc.).</p>
</dd>

### -field <b>AllocationOffsetInBytes</b>

<dd>
<p>The offset in bytes from the start of the allocation being transferred. The offset should not be added to <b>SourceVirtualAddress</b> or <b>DesinationVirtualAddress</b>.</p>
</dd>

### -field <b>TransferSizeInBytes</b>

<dd>
<p>The number of bytes to transfer.</p>
</dd>

### -field <b>SourceVirtualAddress</b>

<dd>
<p>The virtual address of the source in the context of the paging process. </p>
</dd>

### -field <b>DestinationVirtualAddress</b>

<dd>
<p>The virtual address of the destination in the context of the paging process.</p>
</dd>

### -field <b>SourcePageTable</b>

<dd>
<p>The GPU virtual address of the page table that is used to map the <b>SourceVirtualAddress</b> address. </p>
<div class="alert"><b>Note</b>  The address is valid only when the <b>DXGK_GPUMMUCAPS.LegacyBehaviors.SourcePageTableVaInTransfer</b> cap is set.</div>
<div> </div>
</dd>

### -field <b>TransferDirection</b>

<dd>
<p>The <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-memory-transfer-direction.md">DXGK_MEMORY_TRANSFER_DIRECTION</a> structure describing the operation.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-transfervirtualflags.md">DXGK_TRANSFERVIRTUALFLAGS</a> structure describing the operation.</p>
</dd>

### -field <b>DestinationPageTable</b>

<dd>
<p>The GPU virtual address of the page table that  is used to map the <b>DestinationVirtualAddress</b> address. The address is valid only when the <b>DXGK_GPUMMUCAPS.LegacyBehaviors.SourcePageTableVaInTransfer</b> cap is set.</p>
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
<a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-memory-transfer-direction.md">DXGK_MEMORY_TRANSFER_DIRECTION</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-transfervirtualflags.md">DXGK_TRANSFERVIRTUALFLAGS</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-buildpagingbuffer.md">DXGKARG_BUILDPAGINGBUFFER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BUILDPAGINGBUFFER_TRANSFERVIRTUAL structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
