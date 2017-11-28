---
UID: NF.wdbgexts.GetSetSympath
title: GetSetSympath
author: windows-driver-content
description: The GetSetSympath function can be used to either get or set the symbol search path.
old-location: debugger\getsetsympath.htm
old-project: debugger
ms.assetid: 2c7392c2-49c8-4b27-addc-0200eabbe87e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetSetSympath
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
req.alt-api: GetSetSympath
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

# GetSetSympath function



## -description
<p>The <b>GetSetSympath</b> function can be used to either get or set the symbol search path. </p>


## -syntax

````
__inline VOID GetSetSympath(
  _In_      PSTR Arg,
  _Out_opt_ PSTR Result,
  _In_      int  Length
);
````


## -parameters
<dl>

### -param <i>Arg</i> [in]

<dd>
<p>Specifies the new search path. If this argument is <b>NULL</b> or the string is empty, the search path is not set and the current setting is returned in <i>Result</i>.</p>
</dd>

### -param <i>Result</i> [out, optional]

<dd>
<p>Optional. If <i>Arg</i> is <b>NULL</b>, <b>GetSetSympath</b> stores the current search path in the buffer pointed to by <i>Result</i>.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the size of the buffer for storing the result.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When the symbol path is changed, a call to <b>ReloadSymbols</b> is made implicitly.</p>

<p>When the symbol path is changed, a call to <b>ReloadSymbols</b> is made implicitly.</p>

<p>When the symbol path is changed, a call to <b>ReloadSymbols</b> is made implicitly.</p>

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