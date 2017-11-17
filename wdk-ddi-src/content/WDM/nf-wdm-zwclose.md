---
UID: NF.wdm.ZwClose
title: ZwClose
author: windows-driver-content
description: The ZwClose routine closes an object handle.
old-location: kernel\zwclose.htm
ms.assetid: 35f335db-416b-4a17-b84c-d440b34ed199
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwClose,NtClose
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlZwPassive, PowerIrpDDis, ZwRegistryCreate, ZwRegistryOpen, HwStorPortProhibitedDDIs, ZwRegistryCreate(storport), ZwRegistryOpen(storport)
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
ms.keywords: ZwClose
req.iface: 
req.product: Windows 10 or later.
---

# ZwClose function



## -description
<p>The <b>ZwClose</b> routine closes an object handle. </p>


## -syntax

````
NTSTATUS ZwClose(
  _In_ HANDLE Handle
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Handle to an object of any type. </p>
</dd>
</dl>

## -returns
<p><b>ZwClose</b> returns STATUS_SUCCESS on success, or the appropriate NTSTATUS error code on failure. In particular, it returns STATUS_INVALID_HANDLE if <i>Handle</i> is not a valid handle, or STATUS_HANDLE_NOT_CLOSABLE if the calling thread does not have permission to close the handle.</p>

## -remarks
<p><b>ZwClose</b> is a generic routine that operates on any type of object.</p>

<p>Closing an open object handle causes that handle to become invalid. The system also decrements the handle count for the object and checks whether the object can be deleted. The system does not actually delete the object until all of the object's handles are closed and no referenced pointers remain.</p>

<p>A driver must close every handle that it opens as soon as the handle is no longer required. Kernel handles, which are those that are opened by a system thread or by specifying the OBJ_KERNEL_HANDLE flag, can be closed only when the previous processor mode is <b>KernelMode</b>. This requirement applies both to system threads and to dispatch routines for IRPs that were issued from kernel mode. (For more information about the previous processor mode, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545288">ExGetPreviousMode</a>.) For example, a handle that <a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a> returns to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine cannot subsequently be closed by the same driver's <a href="wdkgloss.d#wdkgloss.dispatch_routine#wdkgloss.dispatch_routine"><i>dispatch routines</i></a>. A <b>DriverEntry</b> routine runs in a system process, whereas dispatch routines usually run either in the context of the thread issuing the current I/O request, or, for lower-level drivers, in an arbitrary thread context.</p>

<p>A nonkernel handle can be closed only if one of two conditions is met: The previous processor mode is <b>KernelMode</b>, or the calling thread has sufficient permission to close the handle. An example of the latter occurs when the calling thread is the one that created the handle.</p>

<p>Callers of <b>ZwClose</b> should not assume that this routine automatically waits for all I/O to complete prior to returning. </p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

<p><b>ZwClose</b> is a generic routine that operates on any type of object.</p>

<p>Closing an open object handle causes that handle to become invalid. The system also decrements the handle count for the object and checks whether the object can be deleted. The system does not actually delete the object until all of the object's handles are closed and no referenced pointers remain.</p>

<p>A driver must close every handle that it opens as soon as the handle is no longer required. Kernel handles, which are those that are opened by a system thread or by specifying the OBJ_KERNEL_HANDLE flag, can be closed only when the previous processor mode is <b>KernelMode</b>. This requirement applies both to system threads and to dispatch routines for IRPs that were issued from kernel mode. (For more information about the previous processor mode, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545288">ExGetPreviousMode</a>.) For example, a handle that <a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a> returns to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine cannot subsequently be closed by the same driver's <a href="wdkgloss.d#wdkgloss.dispatch_routine#wdkgloss.dispatch_routine"><i>dispatch routines</i></a>. A <b>DriverEntry</b> routine runs in a system process, whereas dispatch routines usually run either in the context of the thread issuing the current I/O request, or, for lower-level drivers, in an arbitrary thread context.</p>

<p>A nonkernel handle can be closed only if one of two conditions is met: The previous processor mode is <b>KernelMode</b>, or the calling thread has sufficient permission to close the handle. An example of the latter occurs when the calling thread is the one that created the handle.</p>

<p>Callers of <b>ZwClose</b> should not assume that this routine automatically waits for all I/O to complete prior to returning. </p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

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
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547897">IrqlZwPassive</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556228">ZwRegistryCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556231">ZwRegistryOpen</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="https://msdn.microsoft.com/38CCE6AA-BA42-4305-B193-CB1B1C0F105B">ZwRegistryCreate(storport)</a>, <a href="https://msdn.microsoft.com/E423616B-C990-4D26-ABB4-6061BF3B6A21">ZwRegistryOpen(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566421">ZwCreateDirectoryObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566425">ZwCreateKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567014">ZwOpenKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567029">ZwOpenSection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwClose routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
