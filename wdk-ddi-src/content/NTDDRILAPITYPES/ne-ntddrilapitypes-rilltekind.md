---
UID: NE.ntddrilapitypes.RILLTEKIND
title: RILLTEKIND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilltekind.htm
ms.assetid: e7457252-0ca9-4cea-bc06-283573e49331
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
req.alt-api: RILLTEKIND
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

# RILLTEKIND enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILLTEKIND { 
  RIL_LTEKIND_FDD,
  RIL_LTEKIND_TDD,
  RIL_LTEKIND_RESERVED,
  RIL_LTEKIND_UNKNOWN_CA,
  RIL_LTEKIND_FDD_CA,
  RIL_LTEKIND_TDD_CA,
  RIL_LTEKIND_MAX
} RILLTEKIND;
````


## -enum-fields
<dl>

### -field <a id="RIL_LTEKIND_FDD"></a><a id="ril_ltekind_fdd"></a><b>RIL_LTEKIND_FDD</b>

<dd></dd>

### -field <a id="RIL_LTEKIND_TDD"></a><a id="ril_ltekind_tdd"></a><b>RIL_LTEKIND_TDD</b>

<dd></dd>

### -field <a id="RIL_LTEKIND_RESERVED"></a><a id="ril_ltekind_reserved"></a><b>RIL_LTEKIND_RESERVED</b>

<dd></dd>

### -field <a id="RIL_LTEKIND_UNKNOWN_CA"></a><a id="ril_ltekind_unknown_ca"></a><b>RIL_LTEKIND_UNKNOWN_CA</b>

<dd></dd>

### -field <a id="RIL_LTEKIND_FDD_CA"></a><a id="ril_ltekind_fdd_ca"></a><b>RIL_LTEKIND_FDD_CA</b>

<dd></dd>

### -field <a id="RIL_LTEKIND_TDD_CA"></a><a id="ril_ltekind_tdd_ca"></a><b>RIL_LTEKIND_TDD_CA</b>

<dd></dd>

### -field <a id="RIL_LTEKIND_MAX"></a><a id="ril_ltekind_max"></a><b>RIL_LTEKIND_MAX</b>

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