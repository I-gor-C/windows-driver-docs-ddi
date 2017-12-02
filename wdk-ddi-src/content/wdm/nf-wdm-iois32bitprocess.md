---
UID: NF.wdm.IoIs32bitProcess
title: IoIs32bitProcess
author: windows-driver-content
description: The IoIs32bitProcess routine checks whether the originator of the current I/O request is a 32-bit user-mode application.
old-location: kernel\iois32bitprocess.htm
old-project: kernel
ms.assetid: a2de12d5-ed9e-42ac-b3e8-a3a567e4ab4a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoIs32bitProcess
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in 64-bit versions of Microsoft Windows XP and later 64-bit versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoIs32bitProcess
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoIs32bitProcess function



## -description
<p>The <b>IoIs32bitProcess</b> routine checks whether the originator of the current I/O request is a 32-bit user-mode application.</p>


## -syntax

````
BOOLEAN IoIs32bitProcess(
  _In_opt_ PIRP Irp
);
````


## -parameters
<dl>

### -param Irp [in, optional]

<dd>
<p>Optional pointer to the IRP containing the current I/O request. Note that this must be the original IRP that was issued by the I/O manager. If the caller is a fast I/O dispatch routine (and thus there is no IRP), the caller should set this parameter to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>IoIs32bitProcess</b> returns <b>TRUE</b> if the originator of the current I/O request is a 32-bit user-mode process. Otherwise, it returns <b>FALSE</b>. </p>

## -remarks
<p>Drivers call <b>IoIs32bitProcess</b> to determine whether an I/O request is likely to contain data elements that need to be converted, or "thunked," before they can be used in a 64-bit driver.</p>

<p>If the <i>Irp</i> parameter is <b>NULL</b>, and the caller is running in the context of a user-mode process, <b>IoIs32bitProcess</b> returns <b>TRUE</b> if this process is a 32-bit process.</p>

<p>If the <i>Irp</i> parameter is not <b>NULL</b>, it must point to an IRP that was issued by the I/O manager on behalf of a user-mode process. <b>IoIs32bitProcess</b> cannot be used to check driver-allocated IRPs. Driver-allocated IRPs, as well as kernel-mode drivers, are assumed to be 64-bit-ready.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559923">Programming Issues for 64-Bit Drivers</a>.</p>

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
<p>Available in 64-bit versions of Microsoft Windows XP and later 64-bit versions of the Windows operating system.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>