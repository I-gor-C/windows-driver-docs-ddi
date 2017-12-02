---
UID: NE.d3dkmdt._D3DKMDT_MONITOR_ORIENTATION
title: D3DKMDT_MONITOR_ORIENTATION
author: windows-driver-content
description: The D3DKMDT_MONITOR_ORIENTATION enumeration is used to describe the orientation (rotation angle) of a connected external display device.
old-location: display\d3dkmdt_monitor_orientation.htm
old-project: display
ms.assetid: 16e7d91c-04de-4a8c-97c2-c500d0d3697d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_MONITOR_ORIENTATION
req.alt-loc: d3dkmdt.h
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

# D3DKMDT_MONITOR_ORIENTATION enumeration



## -description
<p>The D3DKMDT_MONITOR_ORIENTATION enumeration is used to describe the orientation (rotation angle) of a connected external display device.</p>


## -syntax

````
typedef enum _D3DKMDT_MONITOR_ORIENTATION { 
  D3DKMDT_MO_UNINITIALIZED  = 0,
  D3DKMDT_MO_0DEG           = 1,
  D3DKMDT_MO_90DEG          = 2,
  D3DKMDT_MO_180DEG         = 3,
  D3DKMDT_MO_270DEG         = 4
} D3DKMDT_MONITOR_ORIENTATION;
````


## -enum-fields
<dl>

### -field D3DKMDT_MO_UNINITIALIZED

<dd>
<p>Indicates that a variable of type D3DKMDT_MONITOR_ORIENTATION has not yet been assigned a meaningful value.</p>
</dd>

### -field D3DKMDT_MO_0DEG

<dd>
<p>Indicates that the display device has not been rotated from its default orientation.</p>
</dd>

### -field D3DKMDT_MO_90DEG

<dd>
<p>Indicates that the display device has been rotated 90 degrees clockwise from its default orientation.</p>
</dd>

### -field D3DKMDT_MO_180DEG

<dd>
<p>Indicates that the display device has been rotated 180 degrees clockwise from its default orientation.</p>
</dd>

### -field D3DKMDT_MO_270DEG

<dd>
<p>Indicates that the display device has been rotated 270 degrees clockwise from its default orientation.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>