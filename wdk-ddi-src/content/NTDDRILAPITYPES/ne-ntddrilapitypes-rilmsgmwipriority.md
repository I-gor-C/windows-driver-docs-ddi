---
UID: NE.ntddrilapitypes.RILMSGMWIPRIORITY
title: RILMSGMWIPRIORITY
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgmwipriority.htm
ms.assetid: a974af39-a4a6-44f2-9010-e612f50c83df
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
req.alt-api: RILMSGMWIPRIORITY
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

# RILMSGMWIPRIORITY enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGMWIPRIORITY { 
  RIL_MSGMWIPRIORITY_LOW,
  RIL_MSGMWIPRIORITY_NORMAL,
  RIL_MSGMWIPRIORITY_URGENT,
  RIL_MSGMWIPRIORITY_EMERGENCY,
  RIL_MSGMWIPRIORITY_MAX
} RILMSGMWIPRIORITY;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGMWIPRIORITY_LOW"></a><a id="ril_msgmwipriority_low"></a><b>RIL_MSGMWIPRIORITY_LOW</b>

<dd></dd>

### -field <a id="RIL_MSGMWIPRIORITY_NORMAL"></a><a id="ril_msgmwipriority_normal"></a><b>RIL_MSGMWIPRIORITY_NORMAL</b>

<dd></dd>

### -field <a id="RIL_MSGMWIPRIORITY_URGENT"></a><a id="ril_msgmwipriority_urgent"></a><b>RIL_MSGMWIPRIORITY_URGENT</b>

<dd></dd>

### -field <a id="RIL_MSGMWIPRIORITY_EMERGENCY"></a><a id="ril_msgmwipriority_emergency"></a><b>RIL_MSGMWIPRIORITY_EMERGENCY</b>

<dd></dd>

### -field <a id="RIL_MSGMWIPRIORITY_MAX"></a><a id="ril_msgmwipriority_max"></a><b>RIL_MSGMWIPRIORITY_MAX</b>

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