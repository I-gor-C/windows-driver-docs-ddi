---
UID: NS:ntddrilapitypes.RILREMOVECALLFORWARDINGPARAMS
title: RILREMOVECALLFORWARDINGPARAMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilremovecallforwardingparams.htm
old-project: netvista
ms.assetid: f6eaaa56-8444-496b-8b14-63bb2368d6ba
ms.author: windowsdriverdev
ms.date: 1/8/2018
ms.keywords: RILREMOVECALLFORWARDINGPARAMS, *LPRILREMOVECALLFORWARDINGPARAMS, RILREMOVECALLFORWARDINGPARAMS
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
req.alt-api: RILREMOVECALLFORWARDINGPARAMS
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
req.typenames: *LPRILREMOVECALLFORWARDINGPARAMS, RILREMOVECALLFORWARDINGPARAMS
---

# RILREMOVECALLFORWARDINGPARAMS structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILREMOVECALLFORWARDINGPARAMS {
  DWORD                            dwExecutor;
  RILCALLFORWARDINGSETTINGSREASON  dwReason;
  DWORD                            dwInfoClasses;
} RILREMOVECALLFORWARDINGPARAMS, RILREMOVECALLFORWARDINGPARAMS;
````


## -struct-fields

### -field dwExecutor


### -field dwReason


### -field dwInfoClasses


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>