---
UID: NS.D3DKMDDI._DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO
title: _DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO
author: windows-driver-content
description: Specifies an overlay plane to display during a VSync interval.
old-location: display\dxgk_multiplane_overlay_vsync_info.htm
old-project: display
ms.assetid: b3e93b4d-7d0a-4862-a405-2bf7f78244ef
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO, DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO
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
---

# _DXGK_MULTIPLANE_OVERLAY_VSYNC_INFO structure



## -description
Specifies an overlay plane to display during a VSync interval.


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

### -field LayerIndex

The zero-based index of the overlay plane to display. The top plane (in the z-direction) has index zero. The planes' index values must be sequential from top to bottom.

### -field Enabled

Indicates if the overlay plane specified by <b>LayerIndex</b> is enabled for display.

### -field PhysicalAddress

[in] A <b>PHYSICAL_ADDRESS</b> data type (which is defined as <b>LARGE_INTEGER</b>) that indicates the physical address within the segment where the data is read.

### -field PlaneAttributes

A structure of type <a href="display.dxgk_multiplane_overlay_attributes">DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES</a>  that specifies overlay plane attributes.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012 R2
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>