---
UID: NF.wdbgexts.IsPtr64
title: IsPtr64
author: windows-driver-content
description: The IsPtr64 function determines if the target uses 64-bit pointers.
old-location: debugger\isptr64.htm
old-project: debugger
ms.assetid: 0474a8dc-e2e3-4c84-8058-6229bf0e9d62
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IsPtr64
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IsPtr64
req.alt-loc: wdbgexts.h
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

# IsPtr64 function



## -description
<p>The <b>IsPtr64</b> function determines if the target uses 64-bit pointers.</p>


## -syntax

````
ULONG IsPtr64(void);
````


## -parameters


## -returns
<p>The function returns <b>TRUE</b> if the target uses 64-bit pointers; <b>FALSE</b>, otherwise.</p>

<p>The function returns <b>TRUE</b> if the target uses 64-bit pointers; <b>FALSE</b>, otherwise.</p>

<p>The function returns <b>TRUE</b> if the target uses 64-bit pointers; <b>FALSE</b>, otherwise.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdbgexts.h (include Wdbgexts.h, Wdbgexts.h, or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>