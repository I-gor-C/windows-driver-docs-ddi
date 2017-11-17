---
UID: NF.ntddk.KeSetBasePriorityThread
title: KeSetBasePriorityThread
author: windows-driver-content
description: The KeSetBasePriorityThread routine sets the run-time priority, relative to the current process, for a given thread.
old-location: kernel\kesetbaseprioritythread.htm
ms.assetid: 7070070c-a953-4120-bddf-c1a7f080ef50
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeSetBasePriorityThread
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
req.irql: PASSIVE_LEVEL
ms.keywords: KeSetBasePriorityThread
req.iface: 
---

# KeSetBasePriorityThread function



## -description
<p>The <b>KeSetBasePriorityThread</b> routine sets the run-time priority, relative to the current process, for a given thread.</p>


## -syntax

````
LONG KeSetBasePriorityThread(
  _Inout_ PKTHREAD Thread,
  _In_    LONG     Increment
);
````


## -parameters
<dl>

### -param <i>Thread</i> [in, out]

<dd>
<p>Pointer to a dispatcher object of type KTHREAD. </p>
</dd>

### -param <i>Increment</i> [in]

<dd>
<p>Specifies the value to be added to the base priority of the process for the <i>Thread</i>.</p>
</dd>
</dl>

## -returns
<p><b>KeSetBasePriorityThread</b> returns the previous base priority increment of the given thread. The previous base priority increment is defined as the difference between the specified thread's old base priority and the base priority of the thread's process.</p>

## -remarks
<p>The new base priority is computed by adding the given <i>Increment</i>, which can be a negative value, to the base priority of the specified thread's process. The resultant value is stored as the base priority of the specified thread.</p>

<p>Drivers that set up device-dedicated threads with variable priority attributes can call this routine to set such a thread's priority relative to the system process in which the thread is created.</p>

<p>The new base priority is restricted to the priority class of the given thread's process. Therefore, the base priority is not allowed to cross over from a variable priority class to a real-time priority class or vice versa. </p>

<p>The new base priority is computed by adding the given <i>Increment</i>, which can be a negative value, to the base priority of the specified thread's process. The resultant value is stored as the base priority of the specified thread.</p>

<p>Drivers that set up device-dedicated threads with variable priority attributes can call this routine to set such a thread's priority relative to the system process in which the thread is created.</p>

<p>The new base priority is restricted to the priority class of the given thread's process. Therefore, the base priority is not allowed to cross over from a variable priority class to a real-time priority class or vice versa. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552084">KeGetCurrentThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553062">KeQueryPriorityThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553265">KeSetPriorityThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeSetBasePriorityThread routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
