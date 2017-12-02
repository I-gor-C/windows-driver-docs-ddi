---
UID: NS.d3dkmddi._DXGK_STANDARD_COLORIMETRY_FLAGS
title: DXGK_STANDARD_COLORIMETRY_FLAGS
author: windows-driver-content
description: Flags describing standard colorimetry and related support.
old-location: display\dxgk_standard_colorimetry_flags.htm
old-project: display
ms.assetid: 473C5D7B-8FDD-49E2-981A-00ECCA67671A
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_STANDARD_COLORIMETRY_FLAGS, DXGK_STANDARD_COLORIMETRY_FLAGS, *PDXGK_STANDARD_COLORIMETRY_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_STANDARD_COLORIMETRY_FLAGS
req.alt-loc: d3dkmddi.h
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

# DXGK_STANDARD_COLORIMETRY_FLAGS structure



## -description
<p>Flags describing standard colorimetry and related support.</p>


## -syntax

````
typedef union _DXGK_STANDARD_COLORIMETRY_FLAGS {
  struct {
    UINT BT2020YCC  :1;
    UINT BT2020RGB  :1;
    UINT ST2084  :1;
    UINT Reserved  :29;
  };
  ULONG Value;
} DXGK_STANDARD_COLORIMETRY_FLAGS, *PDXGK_STANDARD_COLORIMETRY_FLAGS;
````


## -struct-fields
<dl>

### -field BT2020YCC

<dd>
<p>Flag which indicates device support for the color space defined by BT.2020 using a YCC signal format.</p>
</dd>

### -field BT2020RGB

<dd>
<p>Flag which indicates device support for the color space defined by BT.2020 using an RGB signal format.</p>
</dd>

### -field ST2084

<dd>
<p>Flag which indicates device support for the ST.2084 EOTF.</p>
</dd>

### -field Reserved

<dd>
<p>This value is reserved for system use.</p>
</dd>

### -field Value

<dd>
<p>The combined value that is operated on.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>