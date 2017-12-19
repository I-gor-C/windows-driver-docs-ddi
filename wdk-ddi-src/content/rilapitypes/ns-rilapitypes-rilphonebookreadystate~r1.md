---
UID: NS.RILAPITYPES.RILPHONEBOOKREADYSTATE~R1
title: RILPHONEBOOKREADYSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookreadystate_2.htm
old-project: NetVista
ms.assetid: 2193f73d-c21c-430d-8535-790fdea86366
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RILPHONEBOOKREADYSTATE, *LPRILPHONEBOOKREADYSTATE, RILPHONEBOOKREADYSTATE
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
req.alt-api: RILPHONEBOOKREADYSTATE
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
req.product: Windows 10 or later.
---

# RILPHONEBOOKREADYSTATE structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. 



## -syntax

````
typedef struct _RILPHONEBOOKREADYSTATE {
  DWORD     cbSize;
  HUICCAPP  hUiccApp;
  DWORD     dwStoreLocations;
} RILPHONEBOOKREADYSTATE, RILPHONEBOOKREADYSTATE;
````


## -struct-fields

### -field cbSize


### -field hUiccApp


### -field dwStoreLocations


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>