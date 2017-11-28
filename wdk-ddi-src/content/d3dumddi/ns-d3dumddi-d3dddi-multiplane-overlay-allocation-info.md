---
UID: NS.d3dumddi.D3DDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO
title: D3DDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO
author: windows-driver-content
description: Specifies info about a multiplane overlay allocation.
old-location: display\d3dddi_multiplane_allocation_info.htm
old-project: display
ms.assetid: ce3610ab-a927-45e7-8ceb-3f38b5f50f00
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO, D3DDDI_MULTIPLANE_ALLOCATION_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_MULTIPLANE_ALLOCATION_INFO
req.alt-loc: D3dumddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# D3DDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO structure



## -description
<p>Specifies info about a multiplane overlay allocation.</p>


## -syntax

````
typedef struct D3DDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO {
  D3DKMT_HANDLE PresentAllocation;
  UINT          SubResourceIndex;
} D3DDDI_MULTIPLANE_ALLOCATION_INFO;
````


## -struct-fields
<dl>

### -field <b>PresentAllocation</b>

<dd>
<p>[in] A handle to the multiplane overlay allocation.</p>
</dd>

### -field <b>SubResourceIndex</b>

<dd>
<p>[in] The zero-based index into the resource which the handle in the <b>PresentAllocation</b> member specifies. This index indicates the display surface.</p>
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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>