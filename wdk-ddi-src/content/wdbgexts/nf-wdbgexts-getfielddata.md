---
UID: NF.wdbgexts.GetFieldData
title: GetFieldData
author: windows-driver-content
description: The GetFieldData function returns the value of a member in a structure.
old-location: debugger\getfielddata.htm
old-project: debugger
ms.assetid: e60c2288-fe25-4da5-9b17-6e95a30e7c1c
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: GetFieldData
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
req.alt-api: GetFieldData
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

# GetFieldData function



## -description
<p>The <b>GetFieldData</b> function returns the value of a member in a structure.</p>


## -syntax

````
__inline ULONG GetFieldData(
  _In_  ULONG64 TypeAddress,
  _In_  LPCSTR  Type,
  _In_  LPCSTR  Field,
  _In_  ULONG   OutSize,
  _Out_ PVOID   pOutValue
);
````


## -parameters
<dl>

### -param <i>TypeAddress</i> [in]

<dd>
<p>Specifies the address of the structure in the target's memory.</p>
</dd>

### -param <i>Type</i> [in]

<dd>
<p>Specifies the name of the type of the structure.  This can be qualified with a module name, for example, <b>mymodule!mystruct</b>.</p>
</dd>

### -param <i>Field</i> [in]

<dd>
<p>Specifies the name of the member in the structure whose value will be returned.  Submembers can be specified by using a period-separated path, for example, "myfield.mysubfield".</p>
<p>If the size of the structure pointed to by <i>TypeAddress</i> is less than 8 bytes, <i>Field</i> can be <b>NULL</b>; in this case, the entire structure is copied to <i>pOutValue</i>.</p>
</dd>

### -param <i>OutSize</i> [in]

<dd>
<p>Specifies the size, in bytes, of the buffer <i>pOutValue</i>.</p>
<p>If <i>OutSize</i> is smaller than the size of the value returned, an error message is printed and an exception is raised; if the exception is handled or ignored, the return value is zero. In this case, the data beyond the end of the buffer referred to by <i>pOutValue</i> might be overwritten.</p>
</dd>

### -param <i>pOutValue</i> [out]

<dd>
<p>Receives the value of the member.  Or, the value of the type, if <i>Field</i> is <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>If the function succeeds, the return value is zero. Otherwise, the return value is an <a href="https://msdn.microsoft.com/41d64bbc-cefe-4665-b054-e6bd135ccd20">IG_DUMP_SYMBOL_INFO error code</a>. 
</p>

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