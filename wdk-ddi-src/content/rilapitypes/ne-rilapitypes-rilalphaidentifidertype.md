---
UID: NE.rilapitypes.RILALPHAIDENTIFIDERTYPE
title: RILALPHAIDENTIFIDERTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilalphaidentifidertype_2.htm
old-project: netvista
ms.assetid: 25e65540-b221-453a-95ff-ec2b96857475
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: RILALPHAIDENTIFIDERTYPE
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

# RILALPHAIDENTIFIDERTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILALPHAIDENTIFIDERTYPE { 
  RIL_ALPHAIDENTIFIERTYPE_PRESENT,
  RIL_ALPHAIDENTIFIERTYPE_NOTPRESENT,
  RIL_ALPHAIDENTIFIERTYPE_MAX
} RILALPHAIDENTIFIDERTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_ALPHAIDENTIFIERTYPE_PRESENT"></a><a id="ril_alphaidentifiertype_present"></a><b>RIL_ALPHAIDENTIFIERTYPE_PRESENT</b>

<dd></dd>

### -field <a id="RIL_ALPHAIDENTIFIERTYPE_NOTPRESENT"></a><a id="ril_alphaidentifiertype_notpresent"></a><b>RIL_ALPHAIDENTIFIERTYPE_NOTPRESENT</b>

<dd></dd>

### -field <a id="RIL_ALPHAIDENTIFIERTYPE_MAX"></a><a id="ril_alphaidentifiertype_max"></a><b>RIL_ALPHAIDENTIFIERTYPE_MAX</b>

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