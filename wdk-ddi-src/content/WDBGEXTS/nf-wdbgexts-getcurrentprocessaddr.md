---
UID: NF.wdbgexts.GetCurrentProcessAddr
title: GetCurrentProcessAddr
author: windows-driver-content
description: The GetCurrentProcessAddr function returns the location of the system data that describes the current process.
old-location: debugger\getcurrentprocessaddr.htm
ms.assetid: 31fada1c-53eb-4e55-bf5f-bf852a8df3ad
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
req.alt-api: GetCurrentProcessAddr
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
ms.keywords: GetCurrentProcessAddr
req.iface: 
req.product: Windows 10 or later.
---

# GetCurrentProcessAddr function



## -description
<p>The <b>GetCurrentProcessAddr</b> function returns the location of the system data that describes the current process.</p>


## -syntax

````
__inline VOID GetCurrentProcessAddr(
   DWORD    Processor,
   ULONG64  CurrentThread,
   PULONG64 Address
);
````


## -parameters
<dl>

### -param <i>Processor</i> 

<dd>
<p>Specifies the index of the processor or virtual thread that was running the current thread when the last event occurred.  <i>Processor</i> is only used in kernel-mode debugging; and, only if <i>CurrentThread</i> is <b>NULL</b>.</p>
</dd>

### -param <i>CurrentThread</i> 

<dd>
<p>Specifies the location of the system data for the current thread.  This is the location returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff545889">GetCurrentThreadAddr</a>.</p>
<p>In kernel-mode debugging, <i>CurrentThread</i> can be <b>NULL</b>, in which case <i>Processor</i> is used instead.</p>
</dd>

### -param <i>Address</i> 

<dd>
<p>Receives the location of the system data that describes the current process.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>In user-mode debugging, <b>GetCurrentProcessAddr</b> returns the location of the process's Process Environment Block (PEB).  This is the same location that <a href="https://msdn.microsoft.com/library/windows/hardware/ff548122">GetPebAddress</a> returns.</p>

<p>In kernel-mode debugging, <b>GetCurrentProcessAddr</b> returns the location of the KPROCESS structure of the current process.</p>

<p>For details on the KPROCESS and PEB structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

<p>In user-mode debugging, <b>GetCurrentProcessAddr</b> returns the location of the process's Process Environment Block (PEB).  This is the same location that <a href="https://msdn.microsoft.com/library/windows/hardware/ff548122">GetPebAddress</a> returns.</p>

<p>In kernel-mode debugging, <b>GetCurrentProcessAddr</b> returns the location of the KPROCESS structure of the current process.</p>

<p>For details on the KPROCESS and PEB structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548122">GetPebAddress</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20GetCurrentProcessAddr function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
