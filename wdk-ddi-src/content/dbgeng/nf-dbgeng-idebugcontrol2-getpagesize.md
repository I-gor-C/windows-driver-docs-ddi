---
UID: NF.dbgeng.IDebugControl2.GetPageSize
title: IDebugControl2::GetPageSize
author: windows-driver-content
description: The GetPageSize method returns the page size for the effective processor mode.
old-location: debugger\getpagesize.htm
old-project: debugger
ms.assetid: 26f11dfb-3fc3-4804-a294-2dfc674b4a73
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl2, GetPageSize, IDebugControl2::GetPageSize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.GetPageSize,IDebugControl2.GetPageSize,IDebugControl3.GetPageSize
req.alt-loc: dbgeng.h
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
req.iface: IDebugControl2
---

# IDebugControl2::GetPageSize method



## -description
<p>The <b>GetPageSize</b> method returns the page size for the effective processor mode.</p>


## -syntax

````
HRESULT GetPageSize(
  [out] PULONG Size
);
````


## -parameters
<dl>

### -param <i>Size</i> [out]

<dd>
<p>Receives the page size.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>