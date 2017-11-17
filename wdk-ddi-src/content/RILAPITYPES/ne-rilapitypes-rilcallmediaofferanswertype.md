---
UID: NE.rilapitypes.RILCALLMEDIAOFFERANSWERTYPE
title: RILCALLMEDIAOFFERANSWERTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediaofferanswertype_2.htm
ms.assetid: 098392dc-f966-44f8-9202-9663b8cabc7e
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
req.alt-api: RILCALLMEDIAOFFERANSWERTYPE
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

# RILCALLMEDIAOFFERANSWERTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>