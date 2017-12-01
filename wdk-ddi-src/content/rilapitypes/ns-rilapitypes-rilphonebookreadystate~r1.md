---
UID: NS.rilapitypes.RILPHONEBOOKREADYSTATE~r1
title: RILPHONEBOOKREADYSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookreadystate_2.htm
old-project: netvista
ms.assetid: 2193f73d-c21c-430d-8535-790fdea86366
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILPHONEBOOKREADYSTATE,
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
req.iface: 
req.product: Windows 10 or later.
---

# RILPHONEBOOKREADYSTATE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILPHONEBOOKREADYSTATE {
  DWORD     cbSize;
  HUICCAPP  hUiccApp;
  DWORD     dwStoreLocations;
} RILPHONEBOOKREADYSTATE, RILPHONEBOOKREADYSTATE;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>hUiccApp</b>

<dd></dd>

### -field <b>dwStoreLocations</b>

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