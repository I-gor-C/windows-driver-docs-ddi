---
UID: NS.d3dkmddi._DXGK_PAGETABLEUPDATEADDRESS
title: DXGK_PAGETABLEUPDATEADDRESS
author: windows-driver-content
description: DXGK_PAGETABLEUPDATEADDRESS contains the address of a page table to update. The member containing the address is defined as part of a DxgkDdiBuildPagingBuffer operation in the DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE structure.
old-location: display\dxgk_pagetableupdateaddress.htm
old-project: display
ms.assetid: 39013276-C76A-4E31-80DD-26C17A020BD6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_PAGETABLEUPDATEADDRESS, DXGK_PAGETABLEUPDATEADDRESS
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
req.alt-api: DXGK_PAGETABLEUPDATEADDRESS
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

# DXGK_PAGETABLEUPDATEADDRESS structure



## -description
<p><b>DXGK_PAGETABLEUPDATEADDRESS</b> contains the address of a page table to update. The member containing the address is defined as part of a <a href="display.dxgkddibuildpagingbuffer">DxgkDdiBuildPagingBuffer</a> operation in the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-buildpagingbuffer-updatepagetable.md">DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE</a> structure.</p>


## -syntax

````
typedef struct _DXGK_PAGETABLEUPDATEADDRESS {
  union {
    PVOID                   CpuVirtual;
    D3DGPU_PHYSICAL_ADDRESS GpuPhysical;
    D3DGPU_VIRTUAL_ADDRESS  GpuVirtual;
  };
} DXGK_PAGETABLEUPDATEADDRESS;
````


## -struct-fields
<dl>

### -field <b>CpuVirtual</b>

<dd>
<p>The CPU virtual address of the page table to update.</p>
</dd>

### -field <b>GpuPhysical</b>

<dd>
<p>The GPU physical address of the page table to update.</p>
</dd>

### -field <b>GpuVirtual</b>

<dd>
<p>The GPU virtual address of the page table to update.</p>
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
<a href="display.dxgkddibuildpagingbuffer">DxgkDdiBuildPagingBuffer</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-buildpagingbuffer-updatepagetable.md">DXGK_BUILDPAGINGBUFFER_UPDATEPAGETABLE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_PAGETABLEUPDATEADDRESS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
