---
UID: NE.ntddrilapitypes.RILMSGCDMAMSGSTATUSTYPE
title: RILMSGCDMAMSGSTATUSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmamsgstatustype.htm
old-project: netvista
ms.assetid: 60365fd7-3897-4948-a251-098e5a91c959
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: RILMSGCDMAMSGSTATUSTYPE
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

# RILMSGCDMAMSGSTATUSTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGCDMAMSGSTATUSTYPE { 
  RIL_MSGSTATUSTYPE_DELIVERYACK,
  RIL_MSGSTATUSTYPE_USERACK,
  RIL_MSGSTATUSTYPE_READACK,
  RIL_MSGSTATUSTYPE_MAX
} RILMSGCDMAMSGSTATUSTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGSTATUSTYPE_DELIVERYACK"></a><a id="ril_msgstatustype_deliveryack"></a><b>RIL_MSGSTATUSTYPE_DELIVERYACK</b>

<dd></dd>

### -field <a id="RIL_MSGSTATUSTYPE_USERACK"></a><a id="ril_msgstatustype_userack"></a><b>RIL_MSGSTATUSTYPE_USERACK</b>

<dd></dd>

### -field <a id="RIL_MSGSTATUSTYPE_READACK"></a><a id="ril_msgstatustype_readack"></a><b>RIL_MSGSTATUSTYPE_READACK</b>

<dd></dd>

### -field <a id="RIL_MSGSTATUSTYPE_MAX"></a><a id="ril_msgstatustype_max"></a><b>RIL_MSGSTATUSTYPE_MAX</b>

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