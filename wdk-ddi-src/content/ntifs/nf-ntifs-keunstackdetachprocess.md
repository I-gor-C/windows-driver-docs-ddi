---
UID: NF.ntifs.KeUnstackDetachProcess
title: KeUnstackDetachProcess function
author: windows-driver-content
description: The KeUnstackDetachProcess routine detaches the current thread from the address space of a process and restores the previous attach state.
old-location: ifsk\keunstackdetachprocess.htm
old-project: ifsk
ms.assetid: 3dd5b8f7-d8f8-4c02-80d1-76d0dbe06cd3
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: KeUnstackDetachProcess
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
req.alt-api: KeUnstackDetachProcess
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
---

# KeUnstackDetachProcess function



## -description
The <b>KeUnstackDetachProcess</b> routine detaches the current thread from the address space of a process and restores the previous attach state. 



## -syntax

````
VOID KeUnstackDetachProcess(
  _In_ PRKAPC_STATE ApcState
);
````


## -parameters

### -param ApcState [in]

Opaque pointer to a KAPC_STATE structure that was returned from a previous call to <a href="ifsk.kestackattachprocess">KeStackAttachProcess</a>. 


## -returns
None


## -remarks
Every successful call to <a href="ifsk.kestackattachprocess">KeStackAttachProcess</a> must be matched by a subsequent call to <b>KeUnstackDetachProcess</b>. 


<div class="alert"><b>Note</b>  Attaching a thread to a different process can prevent asynchronous I/O operations from completing and can potentially cause deadlocks. In general, the lines of code between the call to 
     <a href="ifsk.kestackattachprocess">KeStackAttachProcess</a>
      and the call to 
     <b>KeUnstackDetachProcess</b>
      should be very simple and should not call complex routines or send IRPs to other drivers.</div>
<div> </div>


For more information about using system threads and managing synchronization within a nonarbitrary thread context, see <a href="kernel.driver_threads__dispatcher_objects__and_resources">Driver Threads, Dispatcher Objects, and Resources</a>. 


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
This routine is available on Microsoft Windows 2000 and later. 

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
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
&lt; DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.iogetcurrentprocess">IoGetCurrentProcess</a>
</dt>
<dt>
<a href="ifsk.iogetrequestorprocess">IoGetRequestorProcess</a>
</dt>
<dt>
<a href="ifsk.iothreadtoprocess">IoThreadToProcess</a>
</dt>
<dt>
<a href="kernel.kegetcurrentirql">KeGetCurrentIrql</a>
</dt>
<dt>
<a href="kernel.kegetcurrentthread">KeGetCurrentThread</a>
</dt>
<dt>
<a href="ifsk.kestackattachprocess">KeStackAttachProcess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559933">PsGetCurrentProcess</a>
</dt>
<dt>
<a href="kernel.psgetcurrentthread">PsGetCurrentThread</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20KeUnstackDetachProcess routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

