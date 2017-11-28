---
UID: NF.wdbgexts.GetFieldValue
title: GetFieldValue
author: windows-driver-content
description: The GetFieldValue macro is a thin wrapper around the GetFieldData function. It is provided as a convenience for reading the value of a member in a structure.
old-location: debugger\getfieldvalue.htm
old-project: debugger
ms.assetid: 4655bac3-997e-43d9-b628-b4292ae5509d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetFieldValue
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
req.alt-api: GetFieldValue
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

# GetFieldValue function



## -description
<p>The <b>GetFieldValue</b> macro is a thin wrapper around the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546743">GetFieldData</a> function.  It is provided as a convenience for reading the value of a member in a structure.</p>


## -syntax

````
__inline ULONG GetFieldValue(
   ULONG64 Addr,
   LPCSTR  Type,
   LPCSTR  Field,
   PVOID   OutValue
);
````


## -parameters
<dl>

### -param <i>Addr</i> 

<dd>
<p>Specifies the address of the structure in the target's memory.</p>
</dd>

### -param <i>Type</i> 

<dd>
<p>Specifies the name of the type of the structure.  This can be qualified with a module name, for example, <b>mymodule!mystruct</b>.</p>
</dd>

### -param <i>Field</i> 

<dd>
<p>Specifies the name of the member in the structure.  Submembers can be specified by using a period-separated path, for example, "myfield.mysubfield".</p>
</dd>

### -param <i>OutValue</i> 

<dd>
<p>Specifies the object into which the member's value is read.</p>
</dd>
</dl>

## -returns
<p>If the function succeeds, the return value is zero. Otherwise, the return value is an <a href="https://msdn.microsoft.com/41d64bbc-cefe-4665-b054-e6bd135ccd20">IG_DUMP_SYMBOL_INFO error code</a>. 
	  </p>

## -remarks
<p>The parameters provided to this macro are the same as those provided to the <b>GetFieldData</b> function except that instead of providing a pointer to a buffer and its size, the variable to hold the returned value can be provided directly.</p>

<p>The parameters provided to this macro are the same as those provided to the <b>GetFieldData</b> function except that instead of providing a pointer to a buffer and its size, the variable to hold the returned value can be provided directly.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546743">GetFieldData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20GetFieldValue function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
