---
UID: NE.rilapitypes.RILMSGCLASS
title: RILMSGCLASS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgclass_2.htm
ms.assetid: 95818f9a-9053-4fb3-8bcb-6e318ed6bae5
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
req.alt-api: RILMSGCLASS
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

# RILMSGCLASS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILMSGCLASS { 
  RIL_MSGCLASS_INCOMING,
  RIL_MSGCLASS_OUTGOING,
  RIL_MSGCLASS_BROADCAST,
  RIL_MSGCLASS_ALL
} RILMSGCLASS;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGCLASS_INCOMING"></a><a id="ril_msgclass_incoming"></a><b>RIL_MSGCLASS_INCOMING</b>

<dd></dd>

### -field <a id="RIL_MSGCLASS_OUTGOING"></a><a id="ril_msgclass_outgoing"></a><b>RIL_MSGCLASS_OUTGOING</b>

<dd></dd>

### -field <a id="RIL_MSGCLASS_BROADCAST"></a><a id="ril_msgclass_broadcast"></a><b>RIL_MSGCLASS_BROADCAST</b>

<dd></dd>

### -field <a id="RIL_MSGCLASS_ALL"></a><a id="ril_msgclass_all"></a><b>RIL_MSGCLASS_ALL</b>

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