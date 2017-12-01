---
UID: NF.wdm.ProbeForRead
title: ProbeForRead
author: windows-driver-content
description: The ProbeForRead routine checks that a user-mode buffer actually resides in the user portion of the address space, and is correctly aligned.
old-location: kernel\probeforread.htm
old-project: kernel
ms.assetid: 86b09f5c-6527-447e-b383-b97d45a57ce7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ProbeForRead
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProbeForRead
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlExApcLte2, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ProbeForRead function



## -description
<p>The <b>ProbeForRead</b> routine checks that a user-mode buffer actually resides in the user portion of the address space, and is correctly aligned. </p>


## -syntax

````
VOID ProbeForRead(
  _In_ PVOID  Address,
  _In_ SIZE_T Length,
  _In_ ULONG  Alignment
);
````


## -parameters
<dl>

### -param <i>Address</i> [in]

<dd>
<p>Specifies the beginning of the user-mode buffer.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the length, in bytes, of the user-mode buffer.</p>
</dd>

### -param <i>Alignment</i> [in]

<dd>
<p>Specifies the required alignment, in bytes, of the beginning of the user-mode buffer.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If the specified range of memory is not within the user-mode address range, <b>ProbeForRead</b> raises the STATUS_ACCESS_VIOLATION exception. If the beginning of the address range is not aligned on the byte boundary that is specified by <i>Alignment</i>, <b>ProbeForRead</b> raises the STATUS_DATATYPE_MISALIGNMENT exception.</p>

<p>Kernel-mode drivers must use <b>ProbeForRead</b> to validate read access to buffers that are allocated in user space. It is most commonly used during METHOD_NEITHER I/O to validate the user buffer pointed to by <b>Irp -&gt; UserBuffer</b>.</p>

<p>Drivers must call <b>ProbeForRead</b> inside a <b>try/except</b> block. If the routine raises an exception, the driver should complete the IRP with the appropriate error. Note that subsequent accesses by the driver to the user-mode buffer must also be encapsulated within a <b>try/except</b> block: a malicious application could have another thread deleting, substituting, or changing the protection of user address ranges at any time (even after or during a call to <b>ProbeForRead</b> or <b>ProbeForWrite</b>). For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546823">Handling Exceptions</a>.</p>

<p>Do not use this routine on kernel-mode addresses; it will raise an exception.</p>

<p>If <b>Irp-&gt;RequestorMode</b> = <b>KernelMode</b>, the <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> and <b>Irp-&gt;UserBuffer</b> fields do not contain user-mode addresses, and a call to <b>ProbeForRead</b> to probe a buffer pointed to by either field will raise an exception.</p>

<p>If <i>Length</i> = 0, <b>ProbeForRead</b> does no checking of the address. In this case, the routine does not raise an exception for an address that is misaligned or is outside the range of valid user addresses.</p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqlexapclte2">IrqlExApcLte2</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-probeforwrite.md">ProbeForWrite</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ProbeForRead routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
