---
UID: NF.wdbgexts.GetCurrentThreadAddr
title: GetCurrentThreadAddr
author: windows-driver-content
description: The GetCurrentThreadAddr function returns the location of the system data that describes the current thread.
old-location: debugger\getcurrentthreadaddr.htm
ms.assetid: 0664199b-da65-4b07-958e-d7972b39cefd
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
req.alt-api: GetCurrentThreadAddr
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
ms.keywords: GetCurrentThreadAddr
req.iface: 
req.product: Windows 10 or later.
---

# GetCurrentThreadAddr function



## -description
<p>The <b>GetCurrentThreadAddr</b> function returns the location of the system data that describes the current thread.</p>


## -syntax

````
__inline VOID GetCurrentThreadAddr(
   DWORD    Processor,
   PULONG64 Address
);
````


## -parameters
<dl>

### -param <i>Processor</i> 

<dd>
<p>Specifies the index of the thread whose system data will be returned.</p>
<p>In kernel-mode debugging, this is the index of a virtual thread, which is the index of a processor on the target computer.</p>
</dd>

### -param <i>Address</i> 

<dd>
<p>Receives the location of the system data for the thread.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>In user-mode debugging, <b>GetCurrentThreadAddr</b> returns the location of the thread's Thread Environment Block (TEB).  This is the same location that <a href="https://msdn.microsoft.com/library/windows/hardware/ff549267">GetTebAddress</a> returns.</p>

<p>In kernel-mode debugging, <b>GetCurrentThreadAddr</b> returns the location of the KTHREAD structure of the operating system thread that was executing on the processor when the last event occurred.</p>

<p>For details on the KTHREAD and TEB structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

<p>In user-mode debugging, <b>GetCurrentThreadAddr</b> returns the location of the thread's Thread Environment Block (TEB).  This is the same location that <a href="https://msdn.microsoft.com/library/windows/hardware/ff549267">GetTebAddress</a> returns.</p>

<p>In kernel-mode debugging, <b>GetCurrentThreadAddr</b> returns the location of the KTHREAD structure of the operating system thread that was executing on the processor when the last event occurred.</p>

<p>For details on the KTHREAD and TEB structures, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549267">GetTebAddress</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20GetCurrentThreadAddr function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
