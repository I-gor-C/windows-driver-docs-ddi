---
UID: NF.wdm.DbgBreakPointWithStatus
title: DbgBreakPointWithStatus
author: windows-driver-content
description: The DbgBreakPointWithStatus routine breaks into the kernel debugger and sends the value of Status to the debugger.
old-location: devtest\dbgbreakpointwithstatus.htm
ms.assetid: d508c9de-5fae-47c1-88fa-df9048662419
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: devtest
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DbgBreakPointWithStatus
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: DebugBreakUsage
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntdll.lib (user mode); 
NtosKrnl.lib (kernel mode)
req.dll: NtosKrnl.exe
req.irql: 
ms.keywords: DbgBreakPointWithStatus
req.iface: 
req.product: Windows 10 or later.
---

# DbgBreakPointWithStatus function



## -description
<p>The <b>DbgBreakPointWithStatus</b> routine breaks into the kernel debugger and sends the value of <i>Status</i> to the debugger.</p>


## -syntax

````
NTSYSAPI VOID DbgBreakPointWithStatus(
  _In_ ULONG Status
);
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies a ULONG value that is sent to the debugger (for example, a status code or an address).</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>DbgBreakPointWithStatus</b> is identical to <b>DbgBreakPoint</b>, except for the <i>Status</i> message.</p>

<p>On x86 computers, the <i>Status</i> parameter is stored in the <b>eax</b> register. On machines that have register calling conventions, <i>Status</i> is stored in the first argument register.</p>

<p>This routine raises an exception that is handled by the kernel debugger if one is installed; otherwise it is handled by the debug system. If a debugger is not connected to the system, the exception can be handled in the standard way.</p>

<p>In kernel mode, a break exception that is not handled will cause a bug check. You can, however, connect a kernel-mode debugger to a target computer that has stopped responding and has kernel debugging enabled. For more information, see <a href="https://msdn.microsoft.com/938ef180-84de-442f-9b6c-1138c2fc8d5a">Windows Debugging</a>.</p>

<p><b>DbgBreakPointWithStatus</b> is identical to <b>DbgBreakPoint</b>, except for the <i>Status</i> message.</p>

<p>On x86 computers, the <i>Status</i> parameter is stored in the <b>eax</b> register. On machines that have register calling conventions, <i>Status</i> is stored in the first argument register.</p>

<p>This routine raises an exception that is handled by the kernel debugger if one is installed; otherwise it is handled by the debug system. If a debugger is not connected to the system, the exception can be handled in the standard way.</p>

<p>In kernel mode, a break exception that is not handled will cause a bug check. You can, however, connect a kernel-mode debugger to a target computer that has stopped responding and has kernel debugging enabled. For more information, see <a href="https://msdn.microsoft.com/938ef180-84de-442f-9b6c-1138c2fc8d5a">Windows Debugging</a>.</p>

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
<p>Available in Microsoft Windows 2000 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Wdm.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntdll.lib (user mode); </dt>
<dt>NtosKrnl.lib (kernel mode)</dt>
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
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543670">DebugBreakUsage</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543626">DbgBreakPoint</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548063">KdBreakPoint</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548065">KdBreakPointWithStatus</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [devtest\devtest]:%20DbgBreakPointWithStatus routine%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
