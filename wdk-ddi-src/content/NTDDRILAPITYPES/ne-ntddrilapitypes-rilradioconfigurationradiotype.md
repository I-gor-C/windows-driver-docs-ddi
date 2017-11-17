---
UID: NE.ntddrilapitypes.RILRADIOCONFIGURATIONRADIOTYPE
title: RILRADIOCONFIGURATIONRADIOTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradioconfigurationradiotype.htm
ms.assetid: f4efebb4-0258-44f6-bdf0-ff61d3b13792
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
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

### -field <a id="RIL_RADIOTYPE_SINGLE"></a><a id="ril_radiotype_single"></a><b>RIL_RADIOTYPE_SINGLE</b>

<dd></dd>

### -field <a id="RIL_RADIOTYPE_MULTIMODE"></a><a id="ril_radiotype_multimode"></a><b>RIL_RADIOTYPE_MULTIMODE</b>

<dd></dd>

### -field <a id="RIL_RADIOTYPE_1XCSFB"></a><a id="ril_radiotype_1xcsfb"></a><b>RIL_RADIOTYPE_1XCSFB</b>

<dd></dd>

### -field <a id="RIL_RADIOTYPE_SVLTE"></a><a id="ril_radiotype_svlte"></a><b>RIL_RADIOTYPE_SVLTE</b>

<dd></dd>

### -field <a id="RIL_RADIOTYPE_DUALSTANDBY"></a><a id="ril_radiotype_dualstandby"></a><b>RIL_RADIOTYPE_DUALSTANDBY</b>

<dd></dd>

### -field <a id="RIL_RADIOTYPE_DUALACTIVE"></a><a id="ril_radiotype_dualactive"></a><b>RIL_RADIOTYPE_DUALACTIVE</b>

<dd></dd>

### -field <a id="RIL_RADIOTYPE_SGLTE"></a><a id="ril_radiotype_sglte"></a><b>RIL_RADIOTYPE_SGLTE</b>

<dd></dd>

### -field <a id="RIL_RADIOTYPE_SVLTE_DUALACTIVE"></a><a id="ril_radiotype_svlte_dualactive"></a><b>RIL_RADIOTYPE_SVLTE_DUALACTIVE</b>

<dd></dd>

### -field <a id="RIL_RADIOTYPE_SGLTE_DUALACTIVE"></a><a id="ril_radiotype_sglte_dualactive"></a><b>RIL_RADIOTYPE_SGLTE_DUALACTIVE</b>

<dd></dd>

### -field <a id="RIL_RADIOTYPE_SRLTE"></a><a id="ril_radiotype_srlte"></a><b>RIL_RADIOTYPE_SRLTE</b>

<dd></dd>

### -field <a id="RIL_RADIOTYPE_MAX"></a><a id="ril_radiotype_max"></a><b>RIL_RADIOTYPE_MAX</b>

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