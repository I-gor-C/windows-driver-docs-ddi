---
UID: NE.ntddrilapitypes.RILCALLHANDOVERPHASE
title: RILCALLHANDOVERPHASE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallhandoverphase.htm
ms.assetid: c97fcbba-a127-4974-bda7-47456c05558f
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
req.alt-api: RILCALLHANDOVERPHASE
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

# RILCALLHANDOVERPHASE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLHANDOVERPHASE { 
  RIL_CALLHANDOVERPHASE_COMPLETED,
  RIL_CALLHANDOVERPHASE_FAILED,
  RIL_CALLHANDOVERPHASE_CANCELLED,
  RIL_CALLHANDOVERPHASE_MAX
} RILCALLHANDOVERPHASE;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLHANDOVERPHASE_COMPLETED"></a><a id="ril_callhandoverphase_completed"></a><b>RIL_CALLHANDOVERPHASE_COMPLETED</b>

<dd></dd>

### -field <a id="RIL_CALLHANDOVERPHASE_FAILED"></a><a id="ril_callhandoverphase_failed"></a><b>RIL_CALLHANDOVERPHASE_FAILED</b>

<dd></dd>

### -field <a id="RIL_CALLHANDOVERPHASE_CANCELLED"></a><a id="ril_callhandoverphase_cancelled"></a><b>RIL_CALLHANDOVERPHASE_CANCELLED</b>

<dd></dd>

### -field <a id="RIL_CALLHANDOVERPHASE_MAX"></a><a id="ril_callhandoverphase_max"></a><b>RIL_CALLHANDOVERPHASE_MAX</b>

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