---
UID: NN.dbgeng.IDebugClient2
title: IDebugClient2
author: windows-driver-content
description: IDebugClient2 interface
old-location: debugger\idebugclient2.htm
ms.assetid: 0ea32baa-b318-44ec-8696-a5b42fe73ed1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient2
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
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
req.iface: IDebugSystemObjects4
---

# IDebugClient2 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugClient2</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff549827">IDebugClient</a>. <b>IDebugClient2</b> also has these types of members:</p>

<p>The <b>IDebugClient2</b> interface has these methods.</p>

<p>Removes the current process from the debugger engine's process list without detaching or terminating the process.</p>

<p>Registers additional files containing supporting information that will be used when opening a dump file.</p>

<p>Detaches the debugger engine from the current process, resuming all its threads.
</p>

<p>Requests that a process server be shut down.</p>

<p>Checks whether kernel debugging is enabled for the local kernel.
</p>

<p> Attempts to terminate the current process.</p>

<p>Waits for a local process server to exit.
</p>

<p>Creates a user-mode or kernel-mode crash dump file.</p>

<p> </p>

## -members
<p>The <b>IDebugClient2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537786">AbandonCurrentProcess</a>
</td>
<td align="left" width="63%">
<p>Removes the current process from the debugger engine's process list without detaching or terminating the process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537865">AddDumpInformationFile</a>
</td>
<td align="left" width="63%">
<p>Registers additional files containing supporting information that will be used when opening a dump file.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541846">DetachCurrentProcess</a>
</td>
<td align="left" width="63%">
<p>Detaches the debugger engine from the current process, resuming all its threads.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542993">EndProcessServer</a>
</td>
<td align="left" width="63%">
<p>Requests that a process server be shut down.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551088">IsKernelDebuggerEnabled</a>
</td>
<td align="left" width="63%">
<p>Checks whether kernel debugging is enabled for the local kernel.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558866">TerminateCurrentProcess</a>
</td>
<td align="left" width="63%">
<p> Attempts to terminate the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561230">WaitForProcessServerEnd</a>
</td>
<td align="left" width="63%">
<p>Waits for a local process server to exit.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561382">WriteDumpFile2</a>
</td>
<td align="left" width="63%">
<p>Creates a user-mode or kernel-mode crash dump file.</p>
</td>
</tr>
</table><p>Removes the current process from the debugger engine's process list without detaching or terminating the process.</p>

<p>Registers additional files containing supporting information that will be used when opening a dump file.</p>

<p>Detaches the debugger engine from the current process, resuming all its threads.
</p>

<p>Requests that a process server be shut down.</p>

<p>Checks whether kernel debugging is enabled for the local kernel.
</p>

<p> Attempts to terminate the current process.</p>

<p>Waits for a local process server to exit.
</p>

<p>Creates a user-mode or kernel-mode crash dump file.</p>

<p> </p>

## -remarks


## -requirements
<table>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549827">IDebugClient</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550488">IDebugClient3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550494">IDebugClient4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient2 interface%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
