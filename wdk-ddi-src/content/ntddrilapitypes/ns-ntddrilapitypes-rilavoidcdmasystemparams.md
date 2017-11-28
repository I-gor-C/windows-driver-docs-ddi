---
UID: NS.ntddrilapitypes.RILAVOIDCDMASYSTEMPARAMS
title: RILAVOIDCDMASYSTEMPARAMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilavoidcdmasystemparams.htm
old-project: netvista
ms.assetid: cf160fb9-8230-4b75-8a4f-d19ef001f54a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILAVOIDCDMASYSTEMPARAMS, RILAVOIDCDMASYSTEMPARAMS, *LPRILAVOIDCDMASYSTEMPARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILAVOIDCDMASYSTEMPARAMS
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

# RILAVOIDCDMASYSTEMPARAMS structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>