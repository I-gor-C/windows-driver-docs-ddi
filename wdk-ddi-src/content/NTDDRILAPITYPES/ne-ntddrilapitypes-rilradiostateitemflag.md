---
UID: NE.ntddrilapitypes.RILRADIOSTATEITEMFLAG
title: RILRADIOSTATEITEMFLAG
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradiostateitemflag.htm
ms.assetid: dcbd0b16-4960-4cc1-b76b-6d971ba6a192
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
req.alt-api: RILRADIOSTATEITEMFLAG
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

# RILRADIOSTATEITEMFLAG enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILRADIOSTATEITEMFLAG { 
  RIL_RADIOSTATE_ITEMFLAG_USE_UINTVAL,
  RIL_RADIOSTATE_ITEMFLAG_USE_WSZVAL,
  RIL_RADIOSTATE_ITEMFLAG_USE_INTARRAY,
  RIL_RADIOSTATE_ITEMFLAG_USE_UINTARRAY,
  RIL_RADIOSTATE_ITEMFLAG_USE_BYTEARRAY,
  RIL_RADIOSTATE_ITEMFLAG_USE_MAX
} RILRADIOSTATEITEMFLAG;
````


## -enum-fields
<dl>

### -field <a id="RIL_RADIOSTATE_ITEMFLAG_USE_UINTVAL"></a><a id="ril_radiostate_itemflag_use_uintval"></a><b>RIL_RADIOSTATE_ITEMFLAG_USE_UINTVAL</b>

<dd></dd>

### -field <a id="RIL_RADIOSTATE_ITEMFLAG_USE_WSZVAL"></a><a id="ril_radiostate_itemflag_use_wszval"></a><b>RIL_RADIOSTATE_ITEMFLAG_USE_WSZVAL</b>

<dd></dd>

### -field <a id="RIL_RADIOSTATE_ITEMFLAG_USE_INTARRAY"></a><a id="ril_radiostate_itemflag_use_intarray"></a><b>RIL_RADIOSTATE_ITEMFLAG_USE_INTARRAY</b>

<dd></dd>

### -field <a id="RIL_RADIOSTATE_ITEMFLAG_USE_UINTARRAY"></a><a id="ril_radiostate_itemflag_use_uintarray"></a><b>RIL_RADIOSTATE_ITEMFLAG_USE_UINTARRAY</b>

<dd></dd>

### -field <a id="RIL_RADIOSTATE_ITEMFLAG_USE_BYTEARRAY"></a><a id="ril_radiostate_itemflag_use_bytearray"></a><b>RIL_RADIOSTATE_ITEMFLAG_USE_BYTEARRAY</b>

<dd></dd>

### -field <a id="RIL_RADIOSTATE_ITEMFLAG_USE_MAX"></a><a id="ril_radiostate_itemflag_use_max"></a><b>RIL_RADIOSTATE_ITEMFLAG_USE_MAX</b>

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