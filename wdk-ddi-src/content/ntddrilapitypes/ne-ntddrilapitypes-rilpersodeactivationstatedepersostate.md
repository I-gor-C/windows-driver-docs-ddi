---
UID: NE.ntddrilapitypes.RILPERSODEACTIVATIONSTATEDEPERSOSTATE
title: RILPERSODEACTIVATIONSTATEDEPERSOSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpersodeactivationstatedepersostate.htm
old-project: netvista
ms.assetid: 81147a47-b5aa-4f00-812d-2c6cf9d5ab8b
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
req.alt-api: RILPERSODEACTIVATIONSTATEDEPERSOSTATE
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

# RILPERSODEACTIVATIONSTATEDEPERSOSTATE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>