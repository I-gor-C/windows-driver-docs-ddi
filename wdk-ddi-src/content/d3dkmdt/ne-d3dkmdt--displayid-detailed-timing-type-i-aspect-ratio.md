---
UID: NE.d3dkmdt._DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO
title: DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO
author: windows-driver-content
description: The DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO enumeration indicates the display device's aspect ratio, defined as width by height (width x height).
old-location: display\displayid_detailed_timing_type_i_aspect_ratio.htm
old-project: display
ms.assetid: 2641a446-1890-4b7d-ac28-c72338207f87
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: _DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO
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

# DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO enumeration



## -description
<p>The DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO enumeration indicates the display device's aspect ratio, defined as width by height (width x height).</p>


## -syntax

````
enum _DISPLAYID_DETAILED_TIMING_TYPE_I_ASPECT_RATIO {
  DIDDT1_AspectRatio_1x1    = 0, 
  DIDDT1_AspectRatio_5x4    = 1, 
  DIDDT1_AspectRatio_4x3    = 2, 
  DIDDT1_AspectRatio_15x9   = 3, 
  DIDDT1_AspectRatio_16x9   = 4, 
  DIDDT1_AspectRatio_16x10  = 5 

};
````


## -enum-fields
<dl>

### -field <a id="DIDDT1_AspectRatio_1x1"></a><a id="diddt1_aspectratio_1x1"></a><a id="DIDDT1_ASPECTRATIO_1X1"></a><b>DIDDT1_AspectRatio_1x1</b>

<dd>
<p>Indicates a 1 x 1 aspect ratio.</p>
</dd>

### -field <a id="DIDDT1_AspectRatio_5x4"></a><a id="diddt1_aspectratio_5x4"></a><a id="DIDDT1_ASPECTRATIO_5X4"></a><b>DIDDT1_AspectRatio_5x4</b>

<dd>
<p>Indicates a 5 x 4 aspect ratio.</p>
</dd>

### -field <a id="DIDDT1_AspectRatio_4x3"></a><a id="diddt1_aspectratio_4x3"></a><a id="DIDDT1_ASPECTRATIO_4X3"></a><b>DIDDT1_AspectRatio_4x3</b>

<dd>
<p>Indicates a 4 x 3 aspect ratio.</p>
</dd>

### -field <a id="DIDDT1_AspectRatio_15x9"></a><a id="diddt1_aspectratio_15x9"></a><a id="DIDDT1_ASPECTRATIO_15X9"></a><b>DIDDT1_AspectRatio_15x9</b>

<dd>
<p>Indicates a 15 x 9 aspect ratio.</p>
</dd>

### -field <a id="DIDDT1_AspectRatio_16x9"></a><a id="diddt1_aspectratio_16x9"></a><a id="DIDDT1_ASPECTRATIO_16X9"></a><b>DIDDT1_AspectRatio_16x9</b>

<dd>
<p>Indicates a 16 x 9 aspect ratio.</p>
</dd>

### -field <a id="DIDDT1_AspectRatio_16x10"></a><a id="diddt1_aspectratio_16x10"></a><a id="DIDDT1_ASPECTRATIO_16X10"></a><b>DIDDT1_AspectRatio_16x10</b>

<dd>
<p>Indicates a 16 x 10 aspect ratio.</p>
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
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
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