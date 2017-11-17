---
UID: NE.rilapitypes.RILCALLMEDIAVIDEOFLAGPARAMMASK
title: RILCALLMEDIAVIDEOFLAGPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediavideoflagparammask_2.htm
ms.assetid: 6f0a8c1f-e3cb-4bcb-a9ec-4d4b7555a314
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
req.alt-api: RILCALLMEDIAVIDEOFLAGPARAMMASK
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

# RILCALLMEDIAVIDEOFLAGPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLMEDIAVIDEOFLAGPARAMMASK { 
  RIL_CALLMEDIAVIDEOFLAG_CAPABILITY_UNKNOWN,
  RIL_CALLMEDIAVIDEOFLAG_PAUSE,
  RIL_CALLMEDIAVIDEOFLAG_TEMPORARILY_UNAVAILABLE,
  RIL_CALLMEDIAVIDEOFLAG_ALL
} RILCALLMEDIAVIDEOFLAGPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLMEDIAVIDEOFLAG_CAPABILITY_UNKNOWN"></a><a id="ril_callmediavideoflag_capability_unknown"></a><b>RIL_CALLMEDIAVIDEOFLAG_CAPABILITY_UNKNOWN</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAVIDEOFLAG_PAUSE"></a><a id="ril_callmediavideoflag_pause"></a><b>RIL_CALLMEDIAVIDEOFLAG_PAUSE</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAVIDEOFLAG_TEMPORARILY_UNAVAILABLE"></a><a id="ril_callmediavideoflag_temporarily_unavailable"></a><b>RIL_CALLMEDIAVIDEOFLAG_TEMPORARILY_UNAVAILABLE</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAVIDEOFLAG_ALL"></a><a id="ril_callmediavideoflag_all"></a><b>RIL_CALLMEDIAVIDEOFLAG_ALL</b>

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