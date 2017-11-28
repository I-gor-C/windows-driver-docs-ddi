---
UID: NE.ntddrilapitypes.RILIMSSUBSCRIBETYPE
title: RILIMSSUBSCRIBETYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimssubscribetype.htm
old-project: netvista
ms.assetid: 347b42c1-7585-471c-af42-44218da48fa3
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
req.alt-api: RILIMSSUBSCRIBETYPE
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

# RILIMSSUBSCRIBETYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILIMSSUBSCRIBETYPE { 
  RIL_IMSSUBSCRIBETYPE_MWI,
  RIL_IMSSUBSCRIBETYPE_CONFERENCE,
  RIL_IMSSUBSCRIBETYPE_MAX
} RILIMSSUBSCRIBETYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_IMSSUBSCRIBETYPE_MWI"></a><a id="ril_imssubscribetype_mwi"></a><b>RIL_IMSSUBSCRIBETYPE_MWI</b>

<dd></dd>

### -field <a id="RIL_IMSSUBSCRIBETYPE_CONFERENCE"></a><a id="ril_imssubscribetype_conference"></a><b>RIL_IMSSUBSCRIBETYPE_CONFERENCE</b>

<dd></dd>

### -field <a id="RIL_IMSSUBSCRIBETYPE_MAX"></a><a id="ril_imssubscribetype_max"></a><b>RIL_IMSSUBSCRIBETYPE_MAX</b>

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