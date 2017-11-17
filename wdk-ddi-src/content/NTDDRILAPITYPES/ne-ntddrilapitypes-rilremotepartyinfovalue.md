---
UID: NE.ntddrilapitypes.RILREMOTEPARTYINFOVALUE
title: RILREMOTEPARTYINFOVALUE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilremotepartyinfovalue.htm
ms.assetid: 9cc766c4-a2c0-4b84-a4d8-b005cddd9eea
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
req.alt-api: RILREMOTEPARTYINFOVALUE
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

# RILREMOTEPARTYINFOVALUE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILREMOTEPARTYINFOVALUE { 
  RIL_REMOTEPARTYINFO_WITHHELD,
  RIL_REMOTEPARTYINFO_UNAVAILABLE,
  RIL_REMOTEPARTYINFO_MAX
} RILREMOTEPARTYINFOVALUE;
````


## -enum-fields
<dl>

### -field <a id="RIL_REMOTEPARTYINFO_WITHHELD"></a><a id="ril_remotepartyinfo_withheld"></a><b>RIL_REMOTEPARTYINFO_WITHHELD</b>

<dd></dd>

### -field <a id="RIL_REMOTEPARTYINFO_UNAVAILABLE"></a><a id="ril_remotepartyinfo_unavailable"></a><b>RIL_REMOTEPARTYINFO_UNAVAILABLE</b>

<dd></dd>

### -field <a id="RIL_REMOTEPARTYINFO_MAX"></a><a id="ril_remotepartyinfo_max"></a><b>RIL_REMOTEPARTYINFO_MAX</b>

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