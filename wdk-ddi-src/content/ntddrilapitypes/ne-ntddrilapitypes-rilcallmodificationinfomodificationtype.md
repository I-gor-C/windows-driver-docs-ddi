---
UID: NE.ntddrilapitypes.RILCALLMODIFICATIONINFOMODIFICATIONTYPE
title: RILCALLMODIFICATIONINFOMODIFICATIONTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmodificationinfomodificationtype.htm
old-project: netvista
ms.assetid: 37b18047-7818-4e57-b25a-3c958106e215
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
req.alt-api: RILCALLMODIFICATIONINFOMODIFICATIONTYPE
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

# RILCALLMODIFICATIONINFOMODIFICATIONTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLMODIFICATIONINFOMODIFICATIONTYPE { 
  RIL_CALLMODIFICATIONTYPE_BLOCKED,
  RIL_CALLMODIFICATIONTYPE_MODIFIED,
  RIL_CALLMODIFICATIONTYPE_MAX
} RILCALLMODIFICATIONINFOMODIFICATIONTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLMODIFICATIONTYPE_BLOCKED"></a><a id="ril_callmodificationtype_blocked"></a><b>RIL_CALLMODIFICATIONTYPE_BLOCKED</b>

<dd></dd>

### -field <a id="RIL_CALLMODIFICATIONTYPE_MODIFIED"></a><a id="ril_callmodificationtype_modified"></a><b>RIL_CALLMODIFICATIONTYPE_MODIFIED</b>

<dd></dd>

### -field <a id="RIL_CALLMODIFICATIONTYPE_MAX"></a><a id="ril_callmodificationtype_max"></a><b>RIL_CALLMODIFICATIONTYPE_MAX</b>

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