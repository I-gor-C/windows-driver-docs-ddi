---
UID: NE.rilapitypes.RILUICCLOCKSTATELOCKSTATE
title: RILUICCLOCKSTATELOCKSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluicclockstatelockstate_2.htm
ms.assetid: e97ef5bc-e3da-46ca-b593-59dc93e9cb8e
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
req.alt-api: RILUICCLOCKSTATELOCKSTATE
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

# RILUICCLOCKSTATELOCKSTATE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILUICCLOCKSTATELOCKSTATE { 
  RIL_UICCLOCKSTATE_VERIFIED,
  RIL_UICCLOCKSTATE_ENABLED,
  RIL_UICCLOCKSTATE_BLOCKED,
  RIL_UICCLOCKSTATE_ALL
} RILUICCLOCKSTATELOCKSTATE;
````


## -enum-fields
<dl>

### -field <a id="RIL_UICCLOCKSTATE_VERIFIED"></a><a id="ril_uicclockstate_verified"></a><b>RIL_UICCLOCKSTATE_VERIFIED</b>

<dd></dd>

### -field <a id="RIL_UICCLOCKSTATE_ENABLED"></a><a id="ril_uicclockstate_enabled"></a><b>RIL_UICCLOCKSTATE_ENABLED</b>

<dd></dd>

### -field <a id="RIL_UICCLOCKSTATE_BLOCKED"></a><a id="ril_uicclockstate_blocked"></a><b>RIL_UICCLOCKSTATE_BLOCKED</b>

<dd></dd>

### -field <a id="RIL_UICCLOCKSTATE_ALL"></a><a id="ril_uicclockstate_all"></a><b>RIL_UICCLOCKSTATE_ALL</b>

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