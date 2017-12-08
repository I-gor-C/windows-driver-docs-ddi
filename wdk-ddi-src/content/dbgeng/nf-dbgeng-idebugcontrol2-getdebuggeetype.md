---
UID: NF.dbgeng.IDebugControl2.GetDebuggeeType
title: IDebugControl2::GetDebuggeeType
author: windows-driver-content
description: The GetDebuggeeType method describes the nature of the current target.
old-location: debugger\getdebuggeetype.htm
old-project: debugger
ms.assetid: 86f236fa-73f8-4071-b6da-6de2d276cbff
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl2, GetDebuggeeType, IDebugControl2::GetDebuggeeType
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.GetDebuggeeType,IDebugControl2.GetDebuggeeType,IDebugControl3.GetDebuggeeType
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
req.iface: IDebugControl2
---

# IDebugControl2::GetDebuggeeType method



## -description
<p>The <b>GetDebuggeeType</b> method describes the nature of the current target.</p>


## -syntax

````
HRESULT GetDebuggeeType(
  [out] PULONG Class,
  [out] PULONG Qualifier
);
````


## -parameters
<dl>

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
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>