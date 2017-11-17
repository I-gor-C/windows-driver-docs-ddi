---
UID: NE.d3dkmdt._DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE
title: DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE
author: windows-driver-content
description: The DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE enumeration indicates the display device's frame scanning mode.
old-location: display\displayid_detailed_timing_type_i_scanning_mode.htm
ms.assetid: 8a5d3fba-ffd5-4fbc-973a-d5bfec6bb6e3
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
req.alt-api: _DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE
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

# DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE enumeration



## -description
<p>The DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE enumeration indicates the display device's frame scanning mode.</p>


## -syntax

````
enum _DISPLAYID_DETAILED_TIMING_TYPE_I_SCANNING_MODE {
  DIDDT1_Progressive  = 0, 
  DIDDT1_Interlaced   = 1 

};
````


## -enum-fields
<dl>

### -field <a id="DIDDT1_Progressive"></a><a id="diddt1_progressive"></a><a id="DIDDT1_PROGRESSIVE"></a><b>DIDDT1_Progressive</b>

<dd>
<p>Indicates a progressive scanning mode.</p>
</dd>

### -field <a id="DIDDT1_Interlaced"></a><a id="diddt1_interlaced"></a><a id="DIDDT1_INTERLACED"></a><b>DIDDT1_Interlaced</b>

<dd>
<p>Indicates an interlaced scanning mode.</p>
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