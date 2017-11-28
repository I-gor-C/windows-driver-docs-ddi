---
UID: NE.rilapitypes.RILTDSCDMAKIND
title: RILTDSCDMAKIND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riltdscdmakind_2.htm
old-project: netvista
ms.assetid: ff6c4459-dd3e-43f6-aa41-a2e82221394e
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
req.alt-api: RILTDSCDMAKIND
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

# RILTDSCDMAKIND enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILTDSCDMAKIND { 
  RIL_TDSCDMAKIND_HSDPA,
  RIL_TDSCDMAKIND_HSUPA,
  RIL_TDSCDMAKIND_HSPAPLUS,
  RIL_TDSCDMAKIND_DC_HSPAPLUS,
  RIL_TDSCDMAKIND_MAX
} RILTDSCDMAKIND;
````


## -enum-fields
<dl>

### -field <a id="RIL_TDSCDMAKIND_HSDPA"></a><a id="ril_tdscdmakind_hsdpa"></a><b>RIL_TDSCDMAKIND_HSDPA</b>

<dd></dd>

### -field <a id="RIL_TDSCDMAKIND_HSUPA"></a><a id="ril_tdscdmakind_hsupa"></a><b>RIL_TDSCDMAKIND_HSUPA</b>

<dd></dd>

### -field <a id="RIL_TDSCDMAKIND_HSPAPLUS"></a><a id="ril_tdscdmakind_hspaplus"></a><b>RIL_TDSCDMAKIND_HSPAPLUS</b>

<dd></dd>

### -field <a id="RIL_TDSCDMAKIND_DC_HSPAPLUS"></a><a id="ril_tdscdmakind_dc_hspaplus"></a><b>RIL_TDSCDMAKIND_DC_HSPAPLUS</b>

<dd></dd>

### -field <a id="RIL_TDSCDMAKIND_MAX"></a><a id="ril_tdscdmakind_max"></a><b>RIL_TDSCDMAKIND_MAX</b>

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