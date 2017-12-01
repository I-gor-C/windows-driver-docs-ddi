---
UID: NS.rilapitypes.RILEMERGENCYNUMBER~r1
title: RILEMERGENCYNUMBER
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilemergencynumber_2.htm
old-project: netvista
ms.assetid: 70759d23-b5ab-4c51-b73f-32021b9ae6fb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILEMERGENCYNUMBER,
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
req.alt-api: RILEMERGENCYNUMBER
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

# RILEMERGENCYNUMBER structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILEMERGENCYNUMBER {
  DWORD                             cbSize;
  DWORD                             dwParams;
  DWORD                             dwExecutor;
  HUICCAPP                          hUiccApp;
  DWORD                             dwCategory;
  WCHAR [MAXLENGTH_EMERGENCYNUMBER] wszEmergencyNumber;
} RILEMERGENCYNUMBER, RILEMERGENCYNUMBER;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwExecutor</b>

<dd></dd>

### -field <b>hUiccApp</b>

<dd></dd>

### -field <b>dwCategory</b>

<dd></dd>

### -field <b>wszEmergencyNumber</b>

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