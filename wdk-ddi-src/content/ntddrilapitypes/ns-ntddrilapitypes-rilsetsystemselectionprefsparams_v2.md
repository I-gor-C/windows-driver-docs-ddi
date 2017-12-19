---
UID: NS.NTDDRILAPITYPES.RILSETSYSTEMSELECTIONPREFSPARAMS_V2
title: RILSETSYSTEMSELECTIONPREFSPARAMS_V2
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsetsystemselectionprefsparams_v2.htm
old-project: NetVista
ms.assetid: a480f376-c797-4cb8-99b1-bd7f3a3a2656
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILSETSYSTEMSELECTIONPREFSPARAMS_V2, RILSETSYSTEMSELECTIONPREFSPARAMS, LPRILSETSYSTEMSELECTIONPREFSPARAMS_V2, LPRILSETSYSTEMSELECTIONPREFSPARAMS, *LPRILSETSYSTEMSELECTIONPREFSPARAMS, RILSETSYSTEMSELECTIONPREFSPARAMS_V2, *LPRILSETSYSTEMSELECTIONPREFSPARAMS_V2
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
req.alt-api: RILSETSYSTEMSELECTIONPREFSPARAMS_V2
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

# RILSETSYSTEMSELECTIONPREFSPARAMS_V2 structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.



## -syntax

````
typedef struct _RILSETSYSTEMSELECTIONPREFSPARAMS_V2 {
  DWORD                    dwFlags;
  RILSYSTEMSELECTIONPREFS  rilSystemSelectionPrefs;
} RILSETSYSTEMSELECTIONPREFSPARAMS_V2, RILSETSYSTEMSELECTIONPREFSPARAMS_V2;
````


## -struct-fields

### -field dwFlags


### -field rilSystemSelectionPrefs


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