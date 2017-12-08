---
UID: NF.dbgeng.IDebugControl7.GetDebuggeeType2
title: IDebugControl7::GetDebuggeeType2
author: windows-driver-content
description: The GetDebuggeeType2 method describes the nature of the current target.
old-location: debugger\idebugcontrol7_getdebuggeetype2.htm
old-project: debugger
ms.assetid: DA1F45F5-5B15-4DAD-A746-E467FE1BAE42
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl7, GetDebuggeeType2, IDebugControl7::GetDebuggeeType2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl7.GetDebuggeeType2
req.alt-loc: dbgeng.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IDebugControl7
---

# IDebugControl7::GetDebuggeeType2 method



## -description
<p>The GetDebuggeeType2 method describes the nature of the current target. </p>


## -syntax

````
void GetDebuggeeType2(
  [in]  ULONG  Flags,
  [out] PULONG Class,
  [out] PULONG Qualifier
);
````


## -parameters
<dl>

### -param Flags [in]

<dd>
<p>Takes a single flag, DEBUG_EXEC_FLAGS_NONBLOCK, that indicates whether the function GetDebuggeeType2 should own the engine critical section object (g_EngineLock) before finding the debuggee type.

</p>
<p>If the Flag is present, then the function  will try to own the critical section. If that fails, it  will continue without blocking the caller thread.
</p>
<p>If the flag is not passed in, then the function will wait for the engine critical section to become available before continuing.</p>
</dd>

### -param Class [out]

<dd>
<p>Receives the class of the current target.  It will be set to one of the values in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_CLASS_UNINITIALIZED</p>
</td>
<td>
<p>There is no current target.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CLASS_KERNEL</p>
</td>
<td>
<p>The current target is a kernel-mode target.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_CLASS_USER_WINDOWS</p>
</td>
<td>
<p>The current target is a user-mode target.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param Qualifier [out]

<dd>
<p>Provides more details about the type of the target.  Its interpretation depends on the value of <i>Class</i>.  When class is DEBUG_CLASS_UNINITIALIZED, <i>Qualifier</i> returns zero.  The following values are applicable for kernel-mode targets.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_KERNEL_CONNECTION</p>
</td>
<td>
<p>The current target is a live kernel being debugged in the standard way (using a COM port, 1394 bus, or named pipe).</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_KERNEL_LOCAL</p>
</td>
<td>
<p>The current target is the local kernel.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_KERNEL_EXDI_DRIVER</p>
</td>
<td>
<p>The current target is a live kernel connected using eXDI drivers.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_KERNEL_SMALL_DUMP</p>
</td>
<td>
<p>The current target is a kernel-mode Small Memory Dump file.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_KERNEL_DUMP</p>
</td>
<td>
<p>The current target is a kernel-mode Kernel Memory Dump file.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_KERNEL_FULL_DUMP</p>
</td>
<td>
<p>The current target is a kernel-mode Complete Memory Dump file.</p>
</td>
</tr>
</table>
<p> </p>
<p>The following values are applicable for user-mode targets.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_USER_WINDOWS_PROCESS</p>
</td>
<td>
<p>The current target is a user-mode process on the same computer as the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_USER_WINDOWS_PROCESS_SERVER</p>
</td>
<td>
<p>The current target is a user-mode process connected using a process server.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_USER_WINDOWS_SMALL_DUMP</p>
</td>
<td>
<p>The current target is a user-mode Minidump file.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_USER_WINDOWS_DUMP</p>
</td>
<td>
<p>The current target is a Full User-Mode Dump file.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol7.md">IDebugControl7</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl7::GetDebuggeeType2 method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
