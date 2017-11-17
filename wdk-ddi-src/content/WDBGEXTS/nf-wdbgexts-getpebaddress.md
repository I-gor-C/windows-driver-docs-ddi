---
UID: NF.wdbgexts.GetPebAddress
title: GetPebAddress
author: windows-driver-content
description: The GetPebAddress function returns the address of the process environment block (PEB) for a system process.
old-location: debugger\getpebaddress.htm
ms.assetid: 314eb897-a441-41c7-8b74-a853de70e066
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
req.alt-api: GetPebAddress
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
ms.keywords: GetPebAddress
req.iface: 
req.product: Windows 10 or later.
---

# GetPebAddress function



## -description
<p>The <b>GetPebAddress</b> function returns the address of the process environment block (PEB) for a system process.</p>


## -syntax

````
__inline VOID GetPebAddress(
   ULONG64    CurrentThread,
   PULONGLONG Address
);
````


## -parameters
<dl>

### -param <i>CurrentThread</i> 

<dd>
<p>Specifies an operating system thread whose PEB's address will be returned.</p>
<p>In kernel-mode debugging, this is the location of the KTHREAD structure, which is returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff545889">GetCurrentThreadAddr</a>.  If <i>CurrentThread</i> is <b>NULL</b>, the PEB for the current process is returned.</p>
<p>In user-mode debugging, <i>CurrentThread</i> is ignored.</p>
</dd>

### -param <i>Address</i> 

<dd>
<p>Receives the address of the PEB for the current operating system process or, in kernel-mode debugging, when <i>CurrentThread</i> is not <b>NULL</b>, for the system process that contains the thread that is specified by <i>CurrentThread</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>In user-mode debugging, the PEB for the current thread is returned.</p>

<p>In kernel-mode debugging, if <i>CurrentThread</i> is <b>NULL</b>, the PEB for the operating system process in which the last event occurred is returned.</p>

<p>In user-mode debugging, the PEB for the current thread is returned.</p>

<p>In kernel-mode debugging, if <i>CurrentThread</i> is <b>NULL</b>, the PEB for the operating system process in which the last event occurred is returned.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545889">GetCurrentThreadAddr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549267">GetTebAddress</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20GetPebAddress function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
