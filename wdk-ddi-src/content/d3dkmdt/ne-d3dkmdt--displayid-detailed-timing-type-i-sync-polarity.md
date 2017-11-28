---
UID: NE.d3dkmdt._DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY
title: DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY
author: windows-driver-content
description: The DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY enumeration indicates the display device's sync polarity (whether the sync signal is positive or negative).
old-location: display\displayid_detailed_timing_type_i_sync_polarity.htm
old-project: display
ms.assetid: 6563d4f7-3750-49c1-80f5-14a839e70cb7
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
req.alt-api: _DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY
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

# DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY enumeration



## -description
<p>The DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY enumeration indicates the display device's sync polarity (whether the sync signal is positive or negative).</p>


## -syntax

````
enum _DISPLAYID_DETAILED_TIMING_TYPE_I_SYNC_POLARITY {
  DIDDT1_Sync_Positive  = 0, 
  DIDDT1_Sync_Negative  = 1 

};
````


## -enum-fields
<dl>

### -field <a id="DIDDT1_Sync_Positive"></a><a id="diddt1_sync_positive"></a><a id="DIDDT1_SYNC_POSITIVE"></a><b>DIDDT1_Sync_Positive</b>

<dd>
<p>Indicates that the sync polarity is positive.</p>
</dd>

### -field <a id="DIDDT1_Sync_Negative"></a><a id="diddt1_sync_negative"></a><a id="DIDDT1_SYNC_NEGATIVE"></a><b>DIDDT1_Sync_Negative</b>

<dd>
<p>Indicates that the sync polarity is negative.</p>
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