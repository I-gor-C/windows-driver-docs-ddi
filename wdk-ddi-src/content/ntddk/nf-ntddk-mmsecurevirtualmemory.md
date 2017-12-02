---
UID: NF.ntddk.MmSecureVirtualMemory
title: MmSecureVirtualMemory
author: windows-driver-content
description: The MmSecureVirtualMemory routine secures a user-space memory address range so that it cannot be freed and its protection type cannot be made more restrictive.
old-location: kernel\mmsecurevirtualmemory.htm
old-project: kernel
ms.assetid: e5c2d5d5-550e-42e5-b86a-f17e361925dc
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: MmSecureVirtualMemory
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
req.alt-api: MmSecureVirtualMemory
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlMmApcLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <=APC_LEVEL
req.iface: 
---

# MmSecureVirtualMemory function



## -description
<p>The <b>MmSecureVirtualMemory</b> routine secures a user-space memory address range so that it cannot be freed and its protection type cannot be made more restrictive.</p>


## -syntax

````
HANDLE MmSecureVirtualMemory(
  _In_ PVOID  Address,
  _In_ SIZE_T Size,
  _In_ ULONG  ProbeMode
);
````


## -parameters
<dl>

### -param Address [in]

<dd>
<p>The beginning of the user virtual address range to secure.</p>
</dd>

### -param Size [in]

<dd>
<p>The size, in bytes, of the virtual address range to secure.</p>
</dd>

### -param ProbeMode [in]

<dd>
<p>The most restrictive protection type that is allowed. Use PAGE_READWRITE to specify that address range must remain both readable and writable, or use PAGE_READONLY to specify the address range must only remain readable.</p>
</dd>
</dl>

## -returns
<p>On success, <b>MmSecureVirtualMemory</b> returns an opaque pointer value that the driver passes to the <a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a> routine to unsecure the memory address range. If the routine is unable to secure the memory address range, it returns <b>NULL</b>.</p>

## -remarks
<p><b>MmSecureVirtualMemory</b> can be used to avoid certain race conditions on user-mode buffers. For example, if a driver checks to see if the buffer is writable, but then the originating user-mode process changes the buffer to be read-only before the driver can write to the buffer, then a race condition can result. A driver that uses <b>MmSecureVirtualMemory</b> is guaranteed that if the requested protection mode is available, it cannot be changed until the driver calls <a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a>. The routine also protects against the originating user-mode process freeing the buffer. Here are a few guidelines about calling those routines:<ul>
<li>
<p>If a driver calls <b>MmSecureVirtualMemory</b> and does not call <a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a>, the memory is automatically unsecured when the process terminates.</p>
</li>
<li>
<p>If the driver calls <a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a>, it must call it in the context of the process in which the memory was originally secured, and before that process terminates.</p>
</li>
<li>
<p>Typically drivers need to reference the process when they secure the memory, then later call <a href="..\ntifs\nf-ntifs-kestackattachprocess.md">KeStackAttachProcess</a> to switch to the context of that process before calling <a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a>.</p>
</li>
<li>
<p>To detect process termination drivers can use <a href="..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutine.md">PsSetCreateProcessNotifyRoutine</a>. Alternatively, the process can submit an IRP with a cancel routine that is invoked by the I/O manager when the process is exiting. In the cancel routine the driver can attach to the process and call <a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a>.</p>
</li>
</ul>
</p>

<p>If a driver calls <b>MmSecureVirtualMemory</b> and does not call <a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a>, the memory is automatically unsecured when the process terminates.</p>

<p>If the driver calls <a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a>, it must call it in the context of the process in which the memory was originally secured, and before that process terminates.</p>

<p>Typically drivers need to reference the process when they secure the memory, then later call <a href="..\ntifs\nf-ntifs-kestackattachprocess.md">KeStackAttachProcess</a> to switch to the context of that process before calling <a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a>.</p>

<p>To detect process termination drivers can use <a href="..\ntddk\nf-ntddk-pssetcreateprocessnotifyroutine.md">PsSetCreateProcessNotifyRoutine</a>. Alternatively, the process can submit an IRP with a cancel routine that is invoked by the I/O manager when the process is exiting. In the cancel routine the driver can attach to the process and call <a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a>.</p>

<p>While calling <b>MmSecureVirtualMemory</b> on an address range prevents the address range from being freed or from having its protection changed, it does not protect against other types of raised exceptions. (For example, it does not protect against an exception raised when the system finds a bad disk block in the page file.)  Therefore, drivers must still wrap any memory accesses in a <b>try/except</b> block. Therefore, we recommend that drivers do not use this function. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546823">Handling Exceptions</a>. </p>

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
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqlmmapclte">IrqlMmApcLte</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-mmunsecurevirtualmemory.md">MmUnsecureVirtualMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmSecureVirtualMemory routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
