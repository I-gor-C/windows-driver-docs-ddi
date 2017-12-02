---
UID: NE.ntddrilapitypes.RILRADIOCONFIGURATIONRADIOTYPE
title: RILRADIOCONFIGURATIONRADIOTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradioconfigurationradiotype.htm
old-project: netvista
ms.assetid: f4efebb4-0258-44f6-bdf0-ff61d3b13792
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILRADIOCONFIGURATIONRADIOTYPE
req.alt-loc: ntddrilapitypes.h
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

# RILRADIOCONFIGURATIONRADIOTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILRADIOCONFIGURATIONRADIOTYPE { 
  RIL_RADIOTYPE_SINGLE,
  RIL_RADIOTYPE_MULTIMODE,
  RIL_RADIOTYPE_1XCSFB,
  RIL_RADIOTYPE_SVLTE,
  RIL_RADIOTYPE_DUALSTANDBY,
  RIL_RADIOTYPE_DUALACTIVE,
  RIL_RADIOTYPE_SGLTE,
  RIL_RADIOTYPE_SVLTE_DUALACTIVE,
  RIL_RADIOTYPE_SGLTE_DUALACTIVE,
  RIL_RADIOTYPE_SRLTE,
  RIL_RADIOTYPE_MAX
} RILRADIOCONFIGURATIONRADIOTYPE;
````


## -enum-fields
<dl>

### -field RIL_RADIOTYPE_SINGLE

<dd></dd>

### -field RIL_RADIOTYPE_MULTIMODE

<dd></dd>

### -field RIL_RADIOTYPE_1XCSFB

<dd></dd>

### -field RIL_RADIOTYPE_SVLTE

<dd></dd>

### -field RIL_RADIOTYPE_DUALSTANDBY

<dd></dd>

### -field RIL_RADIOTYPE_DUALACTIVE

<dd></dd>

### -field RIL_RADIOTYPE_SGLTE

<dd></dd>

### -field RIL_RADIOTYPE_SVLTE_DUALACTIVE

<dd></dd>

### -field RIL_RADIOTYPE_SGLTE_DUALACTIVE

<dd></dd>

### -field RIL_RADIOTYPE_SRLTE

<dd></dd>

### -field RIL_RADIOTYPE_MAX

<dd></dd>
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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>