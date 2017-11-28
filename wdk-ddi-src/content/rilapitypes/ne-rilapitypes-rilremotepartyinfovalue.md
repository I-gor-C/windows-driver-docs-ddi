---
UID: NE.rilapitypes.RILREMOTEPARTYINFOVALUE
title: RILREMOTEPARTYINFOVALUE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilremotepartyinfovalue_2.htm
old-project: netvista
ms.assetid: bdea158f-6ee5-4e59-be50-efd8027a8645
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILREMOTEPARTYINFOVALUE
req.alt-loc: rilapitypes.h
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
req.product: Windows 10 or later.
---

# RILREMOTEPARTYINFOVALUE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>