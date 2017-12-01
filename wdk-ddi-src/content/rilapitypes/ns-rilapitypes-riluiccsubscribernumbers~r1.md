---
UID: NS.rilapitypes.RILUICCSUBSCRIBERNUMBERS~r1
title: RILUICCSUBSCRIBERNUMBERS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccsubscribernumbers_2.htm
old-project: netvista
ms.assetid: e1a097b5-ce13-4070-a6f6-4b461ac086de
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILUICCSUBSCRIBERNUMBERS,
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
req.alt-api: RILUICCSUBSCRIBERNUMBERS
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

# RILUICCSUBSCRIBERNUMBERS structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILUICCSUBSCRIBERNUMBERS {
  DWORD                 cbSize;
  DWORD                 dwNumSubscribers;
  RILSUBSCRIBERINFO [1] rsiInfo;
} RILUICCSUBSCRIBERNUMBERS, RILUICCSUBSCRIBERNUMBERS;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwNumSubscribers</b>

<dd></dd>

### -field <b>rsiInfo</b>

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