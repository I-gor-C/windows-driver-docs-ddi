---
UID: NE.d3dkmthk.D3DKMT_MULTIPLANE_OVERLAY_FLAGS
title: D3DKMT_MULTIPLANE_OVERLAY_FLAGS
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_multiplane_overlay_flags.htm
old-project: display
ms.assetid: e4199b1a-b339-4b0d-8540-2c582675f24f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_MULTIPLANE_OVERLAY_FLAGS
req.alt-loc: D3dkmthk.h
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

# D3DKMT_MULTIPLANE_OVERLAY_FLAGS enumeration



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef enum D3DKMT_MULTIPLANE_OVERLAY_FLAGS { 
  D3DKMT_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP    = 0x1,
  D3DKMT_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP  = 0x2
} D3DKMT_MULTIPLANE_OVERLAY_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="D3DKMT_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP"></a><a id="d3dkmt_multiplane_overlay_flag_vertical_flip"></a><b>D3DKMT_MULTIPLANE_OVERLAY_FLAG_VERTICAL_FLIP</b>

<dd></dd>

### -field <a id="D3DKMT_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP"></a><a id="d3dkmt_multiplane_overlay_flag_horizontal_flip"></a><b>D3DKMT_MULTIPLANE_OVERLAY_FLAG_HORIZONTAL_FLIP</b>

<dd></dd>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>