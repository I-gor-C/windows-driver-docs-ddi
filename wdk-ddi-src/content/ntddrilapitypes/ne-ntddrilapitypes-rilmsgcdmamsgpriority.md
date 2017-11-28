---
UID: NE.ntddrilapitypes.RILMSGCDMAMSGPRIORITY
title: RILMSGCDMAMSGPRIORITY
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmamsgpriority.htm
old-project: netvista
ms.assetid: aec67cd5-9ac9-41da-b5e6-a4e416923afb
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
req.alt-api: RILMSGCDMAMSGPRIORITY
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

# RILMSGCDMAMSGPRIORITY enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGCDMAMSGPRIORITY { 
  RIL_MSGPRIORITY_HIGH,
  RIL_MSGPRIORITY_URGENT,
  RIL_MSGPRIORITY_EMERGENCY,
  RIL_MSGPRIORITY_MAX
} RILMSGCDMAMSGPRIORITY;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGPRIORITY_HIGH"></a><a id="ril_msgpriority_high"></a><b>RIL_MSGPRIORITY_HIGH</b>

<dd></dd>

### -field <a id="RIL_MSGPRIORITY_URGENT"></a><a id="ril_msgpriority_urgent"></a><b>RIL_MSGPRIORITY_URGENT</b>

<dd></dd>

### -field <a id="RIL_MSGPRIORITY_EMERGENCY"></a><a id="ril_msgpriority_emergency"></a><b>RIL_MSGPRIORITY_EMERGENCY</b>

<dd></dd>

### -field <a id="RIL_MSGPRIORITY_MAX"></a><a id="ril_msgpriority_max"></a><b>RIL_MSGPRIORITY_MAX</b>

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