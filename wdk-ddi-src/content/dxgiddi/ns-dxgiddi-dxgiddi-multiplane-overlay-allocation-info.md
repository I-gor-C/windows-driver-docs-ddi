---
UID: NS.dxgiddi.DXGIDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO
title: DXGIDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO
author: windows-driver-content
description: Specifies info about a multiplane overlay allocation.
old-location: display\dxgiddi_multiplane_overlay_allocation_info.htm
old-project: display
ms.assetid: 2736b955-1b25-4ded-a75a-19a1c47f61ee
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGIDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO, DXGIDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGIDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO
req.alt-loc: Dxgiddi.h
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

# DXGIDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO structure



## -description
<p>Specifies info about a multiplane overlay allocation.</p>


## -syntax

````
typedef struct DXGIDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO {
  D3DKMT_HANDLE PresentAllocation;
  UINT          SubResourceIndex;
} DXGIDDI_MULTIPLANE_OVERLAY_ALLOCATION_INFO;
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>