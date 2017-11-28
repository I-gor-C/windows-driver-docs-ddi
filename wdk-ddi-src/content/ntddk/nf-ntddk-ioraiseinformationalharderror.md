---
UID: NF.ntddk.IoRaiseInformationalHardError
title: IoRaiseInformationalHardError
author: windows-driver-content
description: The IoRaiseInformationalHardError routine sends a dialog box to the user, warning about a device I/O error that indicates why a user I/O request failed.
old-location: kernel\ioraiseinformationalharderror.htm
old-project: kernel
ms.assetid: 14e9a28c-65cc-4e90-8220-85f1981c8cd7
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoRaiseInformationalHardError
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
req.alt-api: IoRaiseInformationalHardError
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoApcLte, HwStorPortProhibitedDDIs
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

# IoRaiseInformationalHardError function



## -description
<p>The <b>IoRaiseInformationalHardError</b> routine sends a dialog box to the user, warning about a device I/O error that indicates why a user I/O request failed.</p>


## -syntax

````
BOOLEAN IoRaiseInformationalHardError(
  _In_     NTSTATUS        ErrorStatus,
  _In_opt_ PUNICODE_STRING String,
  _In_opt_ PKTHREAD        Thread
);
````


## -parameters
<dl>

### -param <i>ErrorStatus</i> [in]

<dd>
<p>The error status code (IO_ERR_<i>XXX</i>). </p>
</dd>

### -param <i>String</i> [in, optional]

<dd>
<p>A pointer to a Unicode string, which provides additional information about the error. Some NT status codes require a string parameter, such as a file or directory name. If the specified <i>ErrorStatus</i> value does not require a string parameter, set <i>String</i> to <b>NULL</b>.</p>
</dd>

### -param <i>Thread</i> [in, optional]

<dd>
<p>A pointer to the thread whose IRP was failed due to the error specified by the <i>ErrorStatus</i> parameter.</p>
</dd>
</dl>

## -returns
<p><b>IoRaiseInformationalHardError</b> returns <b>TRUE</b> if the dialog box was successfully queued. This routine returns <b>FALSE</b> if dialog boxes are disabled for <i>Thread</i>, a pool allocation failed, too many dialog boxes are already queued, or an equivalent dialog box is already pending a user response (such as waiting for the user to press RETURN).</p>

## -remarks
<p><b>IoRaiseInformationalHardError</b> takes a system-defined NT error value as a parameter. Driver writers can use the event log APIs to communicate driver-defined event strings to the user.</p>

<p><b>IoRaiseInformationalHardError</b> behaves as follows:</p>

<p>If a previous call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550342">IoSetThreadHardErrorMode</a> routine disabled hard errors for the specified thread, <b>IoRaiseInformationalHardError</b> returns <b>FALSE</b>.</p>

<p>Starting with Windows Vista, if the routine is called from a thread in session 0 (that is, from any system thread), no dialog box appears when the routine succeeds and returns <b>TRUE</b>.</p>

<p><b>IoRaiseInformationalHardError</b> takes a system-defined NT error value as a parameter. Driver writers can use the event log APIs to communicate driver-defined event strings to the user.</p>

<p><b>IoRaiseInformationalHardError</b> behaves as follows:</p>

<p>If a previous call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550342">IoSetThreadHardErrorMode</a> routine disabled hard errors for the specified thread, <b>IoRaiseInformationalHardError</b> returns <b>FALSE</b>.</p>

<p>Starting with Windows Vista, if the routine is called from a thread in session 0 (that is, from any system thread), no dialog box appears when the routine succeeds and returns <b>TRUE</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547759">IrqlIoApcLte</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549707">IoSetHardErrorOrVerifyDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550342">IoSetThreadHardErrorMode</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559936">PsGetCurrentThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoRaiseInformationalHardError routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
