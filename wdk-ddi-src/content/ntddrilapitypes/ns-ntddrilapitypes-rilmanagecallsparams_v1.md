---
UID: NS.NTDDRILAPITYPES.RILMANAGECALLSPARAMS_V1
title: RILMANAGECALLSPARAMS_V1
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmanagecallsparams_v1.htm
old-project: NetVista
ms.assetid: 7e89e417-59aa-4bcd-a6a9-0eaaa6a7a776
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILMANAGECALLSPARAMS_V1, *LPRILMANAGECALLSPARAMS_V1, LPRILMANAGECALLSPARAMS_V1, RILMANAGECALLSPARAMS_V1
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
req.alt-api: RILMANAGECALLSPARAMS_V1
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

# RILMANAGECALLSPARAMS_V1 structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILMANAGECALLSPARAMS_V1 {
  DWORD                       dwExecutor;
  RILMANAGECALLPARAMSCOMMAND  dwCommand;
  DWORD                       dwID;
} RILMANAGECALLSPARAMS_V1, RILMANAGECALLSPARAMS_V1;
````


## -struct-fields

### -field dwExecutor


### -field dwCommand


### -field dwID


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