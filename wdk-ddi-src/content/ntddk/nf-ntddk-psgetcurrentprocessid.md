---
UID: NF.ntddk.PsGetCurrentProcessId
title: PsGetCurrentProcessId function
author: windows-driver-content
description: The PsGetCurrentProcessId routine identifies the current thread's process.
old-location: kernel\psgetcurrentprocessid.htm
old-project: kernel
ms.assetid: 9434f740-34c1-4244-813d-3fe9f1ead333
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: PsGetCurrentProcessId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsGetCurrentProcessId
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
---

# PsGetCurrentProcessId function



## -description
The <b>PsGetCurrentProcessId</b> routine identifies the current thread's process. 



## -syntax

````
HANDLE PsGetCurrentProcessId(void);
````


## -parameters


## -returns
<b>PsGetCurrentProcessId</b> returns the process ID of the current thread's process. 

<b>PsGetCurrentProcessId</b> returns the process ID of the current thread's process. 

<b>PsGetCurrentProcessId</b> returns the process ID of the current thread's process. 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.iogetcurrentprocess">IoGetCurrentProcess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559933">PsGetCurrentProcess</a>
</dt>
<dt>
<a href="kernel.psgetcurrentthread">PsGetCurrentThread</a>
</dt>
<dt>
<a href="kernel.psgetcurrentthreadid">PsGetCurrentThreadId</a>
</dt>
<dt>
<a href="kernel.pssetcreateprocessnotifyroutine">PsSetCreateProcessNotifyRoutine</a>
</dt>
<dt>
<a href="kernel.pssetcreatethreadnotifyroutine">PsSetCreateThreadNotifyRoutine</a>
</dt>
<dt>
<a href="kernel.pssetloadimagenotifyroutine">PsSetLoadImageNotifyRoutine</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PsGetCurrentProcessId routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

