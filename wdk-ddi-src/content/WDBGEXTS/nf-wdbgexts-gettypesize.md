---
UID: NF.wdbgexts.GetTypeSize
title: GetTypeSize
author: windows-driver-content
description: The GetTypeSize function returns the size in the target's memory of an instance of the specified type.
old-location: debugger\gettypesize.htm
ms.assetid: 5532799d-5c3b-41ba-ab62-dca9c9d9eb56
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetTypeSize
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
ms.keywords: GetTypeSize
req.iface: 
req.product: Windows 10 or later.
---

# GetTypeSize function



## -description
<p>The <b>GetTypeSize</b> function returns the size in the target's memory of an instance of the specified type.</p>


## -syntax

````
__inline ULONG GetTypeSize(
  _In_ LPCSTR Type
);
````


## -parameters
<dl>

### -param <i>Type</i> [in]

<dd>
<p>Specifies the type to return the size of.</p>
</dd>
</dl>

## -returns
<p>This function returns the size of an instance of the specified type.</p>

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