---
UID: NE.ntddrilapitypes.RILCALLMEDIAOFFERANSWERTYPE
title: RILCALLMEDIAOFFERANSWERTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediaofferanswertype.htm
old-project: netvista
ms.assetid: cc0c3fc5-1482-424c-8ca8-c1bfe641bc03
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
req.alt-api: RILCALLMEDIAOFFERANSWERTYPE
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

# RILCALLMEDIAOFFERANSWERTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLMEDIAOFFERANSWERTYPE { 
  RIL_CALLMEDIAOFFERANSWERTYPE_CURRENT,
  RIL_CALLMEDIAOFFERANSWERTYPE_OFFER,
  RIL_CALLMEDIAOFFERANSWERTYPE_ANSWER,
  RIL_CALLMEDIAOFFERANSWERTYPE_PEER_OFFER,
  RIL_CALLMEDIAOFFERANSWERTYPE_PEER_ANSWER,
  RIL_CALLMEDIAOFFERANSWERTYPE_MAX
} RILCALLMEDIAOFFERANSWERTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLMEDIAOFFERANSWERTYPE_CURRENT"></a><a id="ril_callmediaofferanswertype_current"></a><b>RIL_CALLMEDIAOFFERANSWERTYPE_CURRENT</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAOFFERANSWERTYPE_OFFER"></a><a id="ril_callmediaofferanswertype_offer"></a><b>RIL_CALLMEDIAOFFERANSWERTYPE_OFFER</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAOFFERANSWERTYPE_ANSWER"></a><a id="ril_callmediaofferanswertype_answer"></a><b>RIL_CALLMEDIAOFFERANSWERTYPE_ANSWER</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAOFFERANSWERTYPE_PEER_OFFER"></a><a id="ril_callmediaofferanswertype_peer_offer"></a><b>RIL_CALLMEDIAOFFERANSWERTYPE_PEER_OFFER</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAOFFERANSWERTYPE_PEER_ANSWER"></a><a id="ril_callmediaofferanswertype_peer_answer"></a><b>RIL_CALLMEDIAOFFERANSWERTYPE_PEER_ANSWER</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAOFFERANSWERTYPE_MAX"></a><a id="ril_callmediaofferanswertype_max"></a><b>RIL_CALLMEDIAOFFERANSWERTYPE_MAX</b>

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