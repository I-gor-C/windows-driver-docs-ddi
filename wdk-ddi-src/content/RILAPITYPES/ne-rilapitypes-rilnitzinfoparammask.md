---
UID: NE.rilapitypes.RILNITZINFOPARAMMASK
title: RILNITZINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilnitzinfoparammask_2.htm
ms.assetid: c9ee5373-53eb-4356-8969-4d7bfea13779
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILNITZINFOPARAMMASK
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILNITZINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>