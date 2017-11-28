---
UID: NE.ntddrilapitypes.RILNITZINFOPARAMMASK
title: RILNITZINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilnitzinfoparammask.htm
old-project: netvista
ms.assetid: bdf1505f-2a84-48a3-9534-df83237ab7bb
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: RILNITZINFOPARAMMASK
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

# RILNITZINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILNITZINFOPARAMMASK { 
  RIL_PARAM_NITZ_TIMEZONEOFFSET,
  RIL_PARAM_NITZ_DAYLIGHTSAVINGOFFSET,
  RIL_PARAM_NITZ_SYSTEMTIME,
  RIL_PARAM_NITZ_SYSTEMTYPE,
  RIL_PARAM_NITZ_ALL
} RILNITZINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_NITZ_TIMEZONEOFFSET"></a><a id="ril_param_nitz_timezoneoffset"></a><b>RIL_PARAM_NITZ_TIMEZONEOFFSET</b>

<dd></dd>

### -field <a id="RIL_PARAM_NITZ_DAYLIGHTSAVINGOFFSET"></a><a id="ril_param_nitz_daylightsavingoffset"></a><b>RIL_PARAM_NITZ_DAYLIGHTSAVINGOFFSET</b>

<dd></dd>

### -field <a id="RIL_PARAM_NITZ_SYSTEMTIME"></a><a id="ril_param_nitz_systemtime"></a><b>RIL_PARAM_NITZ_SYSTEMTIME</b>

<dd></dd>

### -field <a id="RIL_PARAM_NITZ_SYSTEMTYPE"></a><a id="ril_param_nitz_systemtype"></a><b>RIL_PARAM_NITZ_SYSTEMTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_NITZ_ALL"></a><a id="ril_param_nitz_all"></a><b>RIL_PARAM_NITZ_ALL</b>

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