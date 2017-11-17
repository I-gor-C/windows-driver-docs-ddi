---
UID: NE.rilapitypes.RILMSGCDMAMSGSTATUSTYPE
title: RILMSGCDMAMSGSTATUSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmamsgstatustype_2.htm
ms.assetid: 315ca5af-103e-4c00-8dd7-10aa21bfa8a2
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
req.alt-api: RILMSGCDMAMSGSTATUSTYPE
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

# RILMSGCDMAMSGSTATUSTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>