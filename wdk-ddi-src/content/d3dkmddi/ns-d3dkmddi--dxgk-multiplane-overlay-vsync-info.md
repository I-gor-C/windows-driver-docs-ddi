---
UID: NS.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO
title: DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO
author: windows-driver-content
description: Specifies an overlay plane to display during a VSync interval.
old-location: display\dxgk_multiplane_overlay_vsync_info.htm
old-project: display
ms.assetid: b3e93b4d-7d0a-4862-a405-2bf7f78244ef
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO, DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO
req.alt-loc: D3dkmddi.h
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

# DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO structure



## -description
<p>Specifies an overlay plane to display during a VSync interval.</p>


## -syntax

````
typedef struct _DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO {
  DWORD                              LayerIndex;
  BOOL                               Enabled;
  PHYSICAL_ADDRESS                   PhysicalAddress;
  DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES PlaneAttributes;
} DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO;
````


## -struct-fields
<dl>

### -field <b>LayerIndex</b>

<dd>
<p>The zero-based index of the overlay plane to display. The top plane (in the z-direction) has index zero. The planes' index values must be sequential from top to bottom.</p>
</dd>

### -field <b>Enabled</b>

<dd>
<p>Indicates if the overlay plane specified by <b>LayerIndex</b> is enabled for display.</p>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>[in] A <b>PHYSICAL_ADDRESS</b> data type (which is defined as <b>LARGE_INTEGER</b>) that indicates the physical address within the segment where the data is read.</p>
</dd>

### -field <b>PlaneAttributes</b>

<dd>
<p>A structure of type <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-attributes.md">DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES</a>  that specifies overlay plane attributes.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>