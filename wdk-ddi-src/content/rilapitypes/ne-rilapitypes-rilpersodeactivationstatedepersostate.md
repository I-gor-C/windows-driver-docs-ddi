---
UID: NE.rilapitypes.RILPERSODEACTIVATIONSTATEDEPERSOSTATE
title: RILPERSODEACTIVATIONSTATEDEPERSOSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpersodeactivationstatedepersostate_2.htm
old-project: netvista
ms.assetid: e01aa9fb-a35e-41d4-994b-8a166372caaf
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: RILPERSODEACTIVATIONSTATEDEPERSOSTATE
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

# RILPERSODEACTIVATIONSTATEDEPERSOSTATE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILPERSODEACTIVATIONSTATEDEPERSOSTATE { 
  RIL_DEPERSOSTATE_CK_REQUIRED,
  RIL_DEPERSOSTATE_PUK_REQUIRED,
  RIL_DEPERSOSTATE_PUK_BLOCKED,
  RIL_DEPERSOSTATE_MAX
} RILPERSODEACTIVATIONSTATEDEPERSOSTATE;
````


## -enum-fields
<dl>

### -field <a id="RIL_DEPERSOSTATE_CK_REQUIRED"></a><a id="ril_depersostate_ck_required"></a><b>RIL_DEPERSOSTATE_CK_REQUIRED</b>

<dd></dd>

### -field <a id="RIL_DEPERSOSTATE_PUK_REQUIRED"></a><a id="ril_depersostate_puk_required"></a><b>RIL_DEPERSOSTATE_PUK_REQUIRED</b>

<dd></dd>

### -field <a id="RIL_DEPERSOSTATE_PUK_BLOCKED"></a><a id="ril_depersostate_puk_blocked"></a><b>RIL_DEPERSOSTATE_PUK_BLOCKED</b>

<dd></dd>

### -field <a id="RIL_DEPERSOSTATE_MAX"></a><a id="ril_depersostate_max"></a><b>RIL_DEPERSOSTATE_MAX</b>

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