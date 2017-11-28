---
UID: NS.rilapitypes.RILMANAGECALLSPARAMS_V2~r1
title: RILMANAGECALLSPARAMS_V2
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmanagecallsparams_v2_2.htm
old-project: netvista
ms.assetid: 6da5ba7b-60d5-4f98-b75b-67956b9a85f8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILMANAGECALLSPARAMS_V2,
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
req.alt-api: RILMANAGECALLSPARAMS_V2
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

# RILMANAGECALLSPARAMS_V2 structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILMANAGECALLSPARAMS_V2 {
  DWORD                       dwExecutor;
  RILMANAGECALLPARAMSCOMMAND  dwCommand;
  DWORD                       dwID;
  BOOL                        fHasOfferAnswer;
  RILCALLMEDIAOFFERANSWERSET  rcmOfferAnswer;
} RILMANAGECALLSPARAMS_V2, RILMANAGECALLSPARAMS_V2;
````


## -struct-fields
<dl>

### -field <b>dwExecutor</b>

<dd></dd>

### -field <b>dwCommand</b>

<dd></dd>

### -field <b>dwID</b>

<dd></dd>

### -field <b>fHasOfferAnswer</b>

<dd></dd>

### -field <b>rcmOfferAnswer</b>

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