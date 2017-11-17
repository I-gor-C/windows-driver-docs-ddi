---
UID: NE.d3dkmdt._DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE
title: DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE
author: windows-driver-content
description: The DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE enumeration indicates the display device's stereo vision mode.
old-location: display\displayid_detailed_timing_type_i_stereo_mode.htm
ms.assetid: 7e40ddf4-0098-4ea6-ab93-17515849b6cd
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: _DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE
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
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE enumeration



## -description
<p>The DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE enumeration indicates the display device's stereo vision mode.</p>


## -syntax

````
enum _DISPLAYID_DETAILED_TIMING_TYPE_I_STEREO_MODE {
  DIDDT1_Monoscopic  = 0, 
  DIDDT1_Stereo      = 1, 
  DIDDT1_Dependent   = 2 

};
````


## -enum-fields
<dl>

### -field <a id="DIDDT1_Monoscopic"></a><a id="diddt1_monoscopic"></a><a id="DIDDT1_MONOSCOPIC"></a><b>DIDDT1_Monoscopic</b>

<dd>
<p>Indicates monoscopic mode (no stereo vision).</p>
</dd>

### -field <a id="DIDDT1_Stereo"></a><a id="diddt1_stereo"></a><a id="DIDDT1_STEREO"></a><b>DIDDT1_Stereo</b>

<dd>
<p>Indicates stereo mode.</p>
</dd>

### -field <a id="DIDDT1_Dependent"></a><a id="diddt1_dependent"></a><a id="DIDDT1_DEPENDENT"></a><b>DIDDT1_Dependent</b>

<dd>
<p>Indicates that the mode depends upon user action.</p>
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