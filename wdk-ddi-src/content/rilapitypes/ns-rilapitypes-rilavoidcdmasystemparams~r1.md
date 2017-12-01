---
UID: NS.rilapitypes.RILAVOIDCDMASYSTEMPARAMS~r1
title: RILAVOIDCDMASYSTEMPARAMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilavoidcdmasystemparams_2.htm
old-project: netvista
ms.assetid: bd938bd9-479a-434c-91d6-93ec76ebe5d6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILAVOIDCDMASYSTEMPARAMS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILAVOIDCDMASYSTEMPARAMS
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

# RILAVOIDCDMASYSTEMPARAMS structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILAVOIDCDMASYSTEMPARAMS {
  DWORD                       dwExecutor;
  RILCDMAAVOIDANCEREQUESTYPE  dwAvoidanceReqType;
} RILAVOIDCDMASYSTEMPARAMS, RILAVOIDCDMASYSTEMPARAMS;
````


## -struct-fields
<dl>

### -field <b>dwExecutor</b>

<dd></dd>

### -field <b>dwAvoidanceReqType</b>

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