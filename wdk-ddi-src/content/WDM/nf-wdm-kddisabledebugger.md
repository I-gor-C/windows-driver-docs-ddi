---
UID: NF.wdm.KdDisableDebugger
title: KdDisableDebugger
author: windows-driver-content
description: The KdDisableDebugger routine disables the kernel debugger.
old-location: devtest\kddisabledebugger.htm
ms.assetid: 491f1b10-342d-4edf-9b70-732f9d4755f2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: devtest
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KdDisableDebugger
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
ms.keywords: KdDisableDebugger
req.iface: 
req.product: Windows 10 or later.
---

# KdDisableDebugger function



## -description
<p>The <b>KdDisableDebugger</b> routine disables the kernel debugger. </p>


## -syntax

````
NTSTATUS KdDisableDebugger(void);
````


## -parameters


## -returns
<p><b>KdDisableDebugger</b> returns STATUS_SUCCESS if the kernel debugger was successfully disabled. Otherwise, the return value can be one of the following error status codes:</p>

<p>STATUS_ACCESS_DENIED</p>

<p>STATUS_DEBUGGER_INACTIVE</p>

<p><b>KdDisableDebugger</b> returns STATUS_SUCCESS if the kernel debugger was successfully disabled. Otherwise, the return value can be one of the following error status codes:</p>

<p>STATUS_ACCESS_DENIED</p>

<p>STATUS_DEBUGGER_INACTIVE</p>

<p><b>KdDisableDebugger</b> returns STATUS_SUCCESS if the kernel debugger was successfully disabled. Otherwise, the return value can be one of the following error status codes:</p>

<p>STATUS_ACCESS_DENIED</p>

<p>STATUS_DEBUGGER_INACTIVE</p>

## -remarks
<p>If the operating system was booted with no debug controls, <b>KdDisableDebugger</b> returns STATUS_DEBUGGER_INACTIVE.</p>

<p>If the kernel debugger is blocked (that is, the <b>KdBlockEnable</b> system variable is set to a value other than <b>FALSE</b>), <b>KdDisableDebugger</b> returns STATUS_ACCESS_DENIED. </p>

<p>After a caller calls <b>KdDisableDebugger</b> to disable the kernel debugger, the caller can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548085">KdEnableDebugger</a> routine to re-enable the kernel debugger.</p>

<p>If the operating system was booted with no debug controls, <b>KdDisableDebugger</b> returns STATUS_DEBUGGER_INACTIVE.</p>

<p>If the kernel debugger is blocked (that is, the <b>KdBlockEnable</b> system variable is set to a value other than <b>FALSE</b>), <b>KdDisableDebugger</b> returns STATUS_ACCESS_DENIED. </p>

<p>After a caller calls <b>KdDisableDebugger</b> to disable the kernel debugger, the caller can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548085">KdEnableDebugger</a> routine to re-enable the kernel debugger.</p>

<p>If the operating system was booted with no debug controls, <b>KdDisableDebugger</b> returns STATUS_DEBUGGER_INACTIVE.</p>

<p>If the kernel debugger is blocked (that is, the <b>KdBlockEnable</b> system variable is set to a value other than <b>FALSE</b>), <b>KdDisableDebugger</b> returns STATUS_ACCESS_DENIED. </p>

<p>After a caller calls <b>KdDisableDebugger</b> to disable the kernel debugger, the caller can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548085">KdEnableDebugger</a> routine to re-enable the kernel debugger.</p>

<p>If the operating system was booted with no debug controls, <b>KdDisableDebugger</b> returns STATUS_DEBUGGER_INACTIVE.</p>

<p>If the kernel debugger is blocked (that is, the <b>KdBlockEnable</b> system variable is set to a value other than <b>FALSE</b>), <b>KdDisableDebugger</b> returns STATUS_ACCESS_DENIED. </p>

<p>After a caller calls <b>KdDisableDebugger</b> to disable the kernel debugger, the caller can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548085">KdEnableDebugger</a> routine to re-enable the kernel debugger.</p>

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
<p>Available in Microsoft Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548085">KdEnableDebugger</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [devtest\devtest]:%20KdDisableDebugger routine%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
