---
UID: NE.rilapitypes.RILCALLMODIFICATIONINFOMODIFICATIONTYPE
title: RILCALLMODIFICATIONINFOMODIFICATIONTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmodificationinfomodificationtype_2.htm
old-project: netvista
ms.assetid: e73abe84-1688-40f1-9b8c-e4e34cc87b78
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
req.alt-api: RILCALLMODIFICATIONINFOMODIFICATIONTYPE
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

# RILCALLMODIFICATIONINFOMODIFICATIONTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>