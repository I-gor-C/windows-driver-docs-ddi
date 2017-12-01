---
UID: NS.ntddrilapitypes.RILPHONEBOOKREADYSTATE
title: RILPHONEBOOKREADYSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookreadystate.htm
old-project: netvista
ms.assetid: cd71234b-4b46-4b7b-953b-32e6f014af03
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILPHONEBOOKREADYSTATE, RILPHONEBOOKREADYSTATE, *LPRILPHONEBOOKREADYSTATE
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
req.alt-api: RILPHONEBOOKREADYSTATE
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

# RILPHONEBOOKREADYSTATE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>