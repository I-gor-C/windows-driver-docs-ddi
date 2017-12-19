---
UID: NS.NTDDRILAPITYPES.RILGETCALLWAITINGSETTINGSPARAMS
title: RILGETCALLWAITINGSETTINGSPARAMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilgetcallwaitingsettingsparams.htm
old-project: NetVista
ms.assetid: b257ef88-a474-4443-8fbf-91759066a536
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILGETCALLWAITINGSETTINGSPARAMS, RILGETCALLWAITINGSETTINGSPARAMS, *LPRILGETCALLWAITINGSETTINGSPARAMS, LPRILGETCALLWAITINGSETTINGSPARAMS
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
req.alt-api: RILGETCALLWAITINGSETTINGSPARAMS
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
---

# RILGETCALLWAITINGSETTINGSPARAMS structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILGETCALLWAITINGSETTINGSPARAMS {
  DWORD  dwExecutor;
  BOOL   fAllClasses;
  DWORD  dwInfoClasses;
} RILGETCALLWAITINGSETTINGSPARAMS, RILGETCALLWAITINGSETTINGSPARAMS;
````


## -struct-fields

### -field dwExecutor


### -field fAllClasses


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