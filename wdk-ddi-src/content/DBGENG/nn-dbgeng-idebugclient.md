---
UID: NN.dbgeng.IDebugClient
title: IDebugClient
author: windows-driver-content
description: IDebugClient interface
old-location: debugger\idebugclient.htm
ms.assetid: 2e47f7ae-2017-4f05-9a06-6c09bb401e21
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
req.alt-api: IDebugClient,IDebugClient.GetOutputWidth,IDebugClient.SetOutputWidth,IDebugClient.GetOutputLinePrefix,IDebugClient.SetOutputLinePrefix
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

# IDebugClient interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugClient</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugClient</b> also has these types of members:</p>

<p>The <b>IDebugClient</b> interface has these methods.</p>

<p>Adds the process options to those options that affect the current process.
</p>

<p>Connects the debugger engine to a kernel target.
</p>

<p>Connects the debugger engine to a user-mode process.</p>

<p>Connects to a process server.</p>

<p>Joins the client to an existing debugger session.</p>

<p>Creates a new client object for the current thread.</p>

<p>Creates a process from the specified command line.
</p>

<p> Create a process from a specified command line, then attaches to another user-mode process.</p>

<p>Detaches the debugger engine from all processes in all targets, resuming all their threads.
</p>

<p>Disconnects the debugger engine from a process server.</p>

<p>Enables the debugger engine to use the current thread for callbacks.
</p>

<p>Ends the current debugger session.</p>

<p>Causes the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541970">DispatchCallbacks</a> method to return.</p>

<p> Forces any remaining buffered output to be delivered to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550801">IDebugOutputCallbacks</a> object registered with this client.</p>

<p>Returns the event callbacks object registered with this client.
</p>

<p>Returns the exit code of the current process if that process has already run through to completion.
</p>

<p>Returns a string describing the computer and user this client represents.
</p>

<p>Returns the input callbacks object registered with this client.</p>

<p>Returns the connection options for the current kernel target.
</p>

<p>Returns the output mask for another client.
</p>

<p>Returns the output callbacks object registered with the client.
</p>

<p></p>

<p>Returns the output mask currently set for the client.</p>

<p></p>

<p>Retrieves the process options affecting the current process.
</p>

<p>Returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line.</p>

<p> Searches for a process with a given executable file name and return its process ID.
</p>

<p> Returns the process IDs for each running process.</p>

<p>Opens a dump file as a debugger target.
</p>

<p> Formats and outputs a string describing the computer and user this client represents.
</p>

<p>Lists the servers running on a given computer.
</p>

<p>Removes process options from those options that affect the current process.
</p>

<p>Registers an event callbacks object with this client.
</p>

<p>Registers an input callbacks object with the client.</p>

<p>Updates some of the connection options for a live kernel target.
</p>

<p>Sets the output mask for another client.
</p>

<p>Registers an output callbacks object with this client.</p>

<p></p>

<p>Sets the output mask for the client.</p>

<p></p>

<p>Sets the process options affecting the current process.</p>

<p>Starts a process server.</p>

<p> Starts a debugging server.
</p>

<p>Attempts to terminate all processes in all targets.</p>

<p>Creates a user-mode or kernel-mode crash dump file.
</p>

<p> </p>

## -members
<p>The <b>IDebugClient</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537917">AddProcessOptions</a>
</td>
<td align="left" width="63%">
<p>Adds the process options to those options that affect the current process.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538145">AttachKernel</a>
</td>
<td align="left" width="63%">
<p>Connects the debugger engine to a kernel target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538150">AttachProcess</a>
</td>
<td align="left" width="63%">
<p>Connects the debugger engine to a user-mode process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539237">ConnectProcessServer</a>
</td>
<td align="left" width="63%">
<p>Connects to a process server.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539245">ConnectSession</a>
</td>
<td align="left" width="63%">
<p>Joins the client to an existing debugger session.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539320">CreateClient</a>
</td>
<td align="left" width="63%">
<p>Creates a new client object for the current thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539321">CreateProcess</a>
</td>
<td align="left" width="63%">
<p>Creates a process from the specified command line.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540048">CreateProcessAndAttach</a>
</td>
<td align="left" width="63%">
<p> Create a process from a specified command line, then attaches to another user-mode process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541851">DetachProcesses</a>
</td>
<td align="left" width="63%">
<p>Detaches the debugger engine from all processes in all targets, resuming all their threads.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541969">DisconnectProcessServer</a>
</td>
<td align="left" width="63%">
<p>Disconnects the debugger engine from a process server.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541970">DispatchCallbacks</a>
</td>
<td align="left" width="63%">
<p>Enables the debugger engine to use the current thread for callbacks.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543004">EndSession</a>
</td>
<td align="left" width="63%">
<p>Ends the current debugger session.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543265">ExitDispatch</a>
</td>
<td align="left" width="63%">
<p>Causes the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541970">DispatchCallbacks</a> method to return.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545475">FlushCallbacks</a>
</td>
<td align="left" width="63%">
<p> Forces any remaining buffered output to be delivered to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550801">IDebugOutputCallbacks</a> object registered with this client.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546601">GetEventCallbacks</a>
</td>
<td align="left" width="63%">
<p>Returns the event callbacks object registered with this client.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546679">GetExitCode</a>
</td>
<td align="left" width="63%">
<p>Returns the exit code of the current process if that process has already run through to completion.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546831">GetIdentity</a>
</td>
<td align="left" width="63%">
<p>Returns a string describing the computer and user this client represents.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546892">GetInputCallbacks</a>
</td>
<td align="left" width="63%">
<p>Returns the input callbacks object registered with this client.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546970">GetKernelConnectionOptions</a>
</td>
<td align="left" width="63%">
<p>Returns the connection options for the current kernel target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548066">GetOtherOutputMask</a>
</td>
<td align="left" width="63%">
<p>Returns the output mask for another client.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548071">GetOutputCallbacks</a>
</td>
<td align="left" width="63%">
<p>Returns the output callbacks object registered with the client.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetOutputLinePrefix</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548080">GetOutputMask</a>
</td>
<td align="left" width="63%">
<p>Returns the output mask currently set for the client.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetOutputWidth</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548163">GetProcessOptions</a>
</td>
<td align="left" width="63%">
<p>Retrieves the process options affecting the current process.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548243">GetRunningProcessDescription</a>
</td>
<td align="left" width="63%">
<p>Returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548254">GetRunningProcessSystemIdByExecutableName</a>
</td>
<td align="left" width="63%">
<p> Searches for a process with a given executable file name and return its process ID.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548265">GetRunningProcessSystemIds</a>
</td>
<td align="left" width="63%">
<p> Returns the process IDs for each running process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552322">OpenDumpFile</a>
</td>
<td align="left" width="63%">
<p>Opens a dump file as a debugger target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553219">OutputIdentity</a>
</td>
<td align="left" width="63%">
<p> Formats and outputs a string describing the computer and user this client represents.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553247">OutputServers</a>
</td>
<td align="left" width="63%">
<p>Lists the servers running on a given computer.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554505">RemoveProcessOptions</a>
</td>
<td align="left" width="63%">
<p>Removes process options from those options that affect the current process.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556671">SetEventCallbacks</a>
</td>
<td align="left" width="63%">
<p>Registers an event callbacks object with this client.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556721">SetInputCallbacks</a>
</td>
<td align="left" width="63%">
<p>Registers an input callbacks object with the client.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556729">SetKernelConnectionOptions</a>
</td>
<td align="left" width="63%">
<p>Updates some of the connection options for a live kernel target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556750">SetOtherOutputMask</a>
</td>
<td align="left" width="63%">
<p>Sets the output mask for another client.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556751">SetOutputCallbacks</a>
</td>
<td align="left" width="63%">
<p>Registers an output callbacks object with this client.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>SetOutputLinePrefix</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556756">SetOutputMask</a>
</td>
<td align="left" width="63%">
<p>Sets the output mask for the client.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>SetOutputWidth</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556765">SetProcessOptions</a>
</td>
<td align="left" width="63%">
<p>Sets the process options affecting the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558810">StartProcessServer</a>
</td>
<td align="left" width="63%">
<p>Starts a process server.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558813">StartServer</a>
</td>
<td align="left" width="63%">
<p> Starts a debugging server.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558867">TerminateProcesses</a>
</td>
<td align="left" width="63%">
<p>Attempts to terminate all processes in all targets.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561380">WriteDumpFile</a>
</td>
<td align="left" width="63%">
<p>Creates a user-mode or kernel-mode crash dump file.
</p>
</td>
</tr>
</table><p>Adds the process options to those options that affect the current process.
</p>

<p>Connects the debugger engine to a kernel target.
</p>

<p>Connects the debugger engine to a user-mode process.</p>

<p>Connects to a process server.</p>

<p>Joins the client to an existing debugger session.</p>

<p>Creates a new client object for the current thread.</p>

<p>Creates a process from the specified command line.
</p>

<p> Create a process from a specified command line, then attaches to another user-mode process.</p>

<p>Detaches the debugger engine from all processes in all targets, resuming all their threads.
</p>

<p>Disconnects the debugger engine from a process server.</p>

<p>Enables the debugger engine to use the current thread for callbacks.
</p>

<p>Ends the current debugger session.</p>

<p>Causes the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541970">DispatchCallbacks</a> method to return.</p>

<p> Forces any remaining buffered output to be delivered to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550801">IDebugOutputCallbacks</a> object registered with this client.</p>

<p>Returns the event callbacks object registered with this client.
</p>

<p>Returns the exit code of the current process if that process has already run through to completion.
</p>

<p>Returns a string describing the computer and user this client represents.
</p>

<p>Returns the input callbacks object registered with this client.</p>

<p>Returns the connection options for the current kernel target.
</p>

<p>Returns the output mask for another client.
</p>

<p>Returns the output callbacks object registered with the client.
</p>

<p></p>

<p>Returns the output mask currently set for the client.</p>

<p></p>

<p>Retrieves the process options affecting the current process.
</p>

<p>Returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line.</p>

<p> Searches for a process with a given executable file name and return its process ID.
</p>

<p> Returns the process IDs for each running process.</p>

<p>Opens a dump file as a debugger target.
</p>

<p> Formats and outputs a string describing the computer and user this client represents.
</p>

<p>Lists the servers running on a given computer.
</p>

<p>Removes process options from those options that affect the current process.
</p>

<p>Registers an event callbacks object with this client.
</p>

<p>Registers an input callbacks object with the client.</p>

<p>Updates some of the connection options for a live kernel target.
</p>

<p>Sets the output mask for another client.
</p>

<p>Registers an output callbacks object with this client.</p>

<p></p>

<p>Sets the output mask for the client.</p>

<p></p>

<p>Sets the process options affecting the current process.</p>

<p>Starts a process server.</p>

<p> Starts a debugging server.
</p>

<p>Attempts to terminate all processes in all targets.</p>

<p>Creates a user-mode or kernel-mode crash dump file.
</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550481">IDebugClient2</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient interface%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
