---
UID: NF.ntifs.KeStackAttachProcess
title: KeStackAttachProcess
author: windows-driver-content
description: The KeStackAttachProcess routine attaches the current thread to the address space of the target process.
old-location: ifsk\kestackattachprocess.htm
old-project: ifsk
ms.assetid: 52ac1410-8f8f-405a-9c81-a534c3cfbf51
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: KeStackAttachProcess
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeStackAttachProcess
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
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# KeStackAttachProcess function



## -description
<p>The <b>KeStackAttachProcess</b> routine attaches the current thread to the address space of the target process.</p>


## -syntax

````
VOID KeStackAttachProcess(
  _Inout_ PRKPROCESS   Process,
  _Out_   PRKAPC_STATE ApcState
);
````


## -parameters
<dl>

### -param <i>Process</i> [in, out]

<dd>
<p>Pointer to the target process object. This parameter can be a PEPROCESS pointer returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff549177">IoGetCurrentProcess</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff559933">PsGetCurrentProcess</a>. </p>
</dd>

### -param <i>ApcState</i> [out]

<dd>
<p>An opaque pointer to a KAPC_STATE structure. The caller must allocate storage for this structure either from nonpaged pool or from the caller's own thread stack. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>KeStackAttachProcess</b> attaches the current thread to the address space of the process pointed to by the <i>Process</i> parameter. If the current thread was already attached to another process, the <i>ApcState</i> parameter receives the current APC state before <b>KeStackAttachProcess</b> attaches to the new process. </p>

<p>Every call to <b>KeStackAttachProcess</b> must be matched by a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549677">KeUnstackDetachProcess</a>. </p>

<p>
<div class="alert"><b>Note</b>  
     Attaching a thread to a different process can prevent asynchronous I/O operations from completing and can potentially cause deadlocks. In general, the lines of code between the call to 
     <b>KeStackAttachProcess</b>
      and the call to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549677">KeUnstackDetachProcess</a>
      should be very simple and should not call complex routines or send IRPs to other drivers. 
    </div>
<div> </div>
</p>

<p>For more information about using system threads and managing synchronization within a nonarbitrary thread context, see <a href="kernel.driver_threads__dispatcher_objects__and_resources">Driver Threads, Dispatcher Objects, and Resources</a>. </p>

<p><b>KeStackAttachProcess</b> attaches the current thread to the address space of the process pointed to by the <i>Process</i> parameter. If the current thread was already attached to another process, the <i>ApcState</i> parameter receives the current APC state before <b>KeStackAttachProcess</b> attaches to the new process. </p>

<p>Every call to <b>KeStackAttachProcess</b> must be matched by a subsequent call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549677">KeUnstackDetachProcess</a>. </p>

<p>
<div class="alert"><b>Note</b>  
     Attaching a thread to a different process can prevent asynchronous I/O operations from completing and can potentially cause deadlocks. In general, the lines of code between the call to 
     <b>KeStackAttachProcess</b>
      and the call to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549677">KeUnstackDetachProcess</a>
      should be very simple and should not call complex routines or send IRPs to other drivers. 
    </div>
<div> </div>
</p>

<p>For more information about using system threads and managing synchronization within a nonarbitrary thread context, see <a href="kernel.driver_threads__dispatcher_objects__and_resources">Driver Threads, Dispatcher Objects, and Resources</a>. </p>

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
<p>This routine is available on Microsoft Windows 2000 and later. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549177">IoGetCurrentProcess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548385">IoGetRequestorProcess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548549">IoThreadToProcess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552054">KeGetCurrentIrql</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552084">KeGetCurrentThread</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549677">KeUnstackDetachProcess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559933">PsGetCurrentProcess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559936">PsGetCurrentThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20KeStackAttachProcess routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
