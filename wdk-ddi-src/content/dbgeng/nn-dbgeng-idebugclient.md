---
UID: NN.dbgeng.IDebugClient
title: IDebugClient
author: windows-driver-content
description: IDebugClient interface
old-location: debugger\idebugclient.htm
old-project: debugger
ms.assetid: 2e47f7ae-2017-4f05-9a06-6c09bb401e21
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
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

<p>Causes the <a href="debugger.dispatchcallbacks">DispatchCallbacks</a> method to return.</p>

<p> Forces any remaining buffered output to be delivered to the <a href="..\dbgeng\nn-dbgeng-idebugoutputcallbacks.md">IDebugOutputCallbacks</a> object registered with this client.</p>

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
<a href="debugger.addprocessoptions">AddProcessOptions</a>
</td>
<td align="left" width="63%">
<p>Adds the process options to those options that affect the current process.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.attachkernel">AttachKernel</a>
</td>
<td align="left" width="63%">
<p>Connects the debugger engine to a kernel target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.attachprocess">AttachProcess</a>
</td>
<td align="left" width="63%">
<p>Connects the debugger engine to a user-mode process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.connectprocessserver">ConnectProcessServer</a>
</td>
<td align="left" width="63%">
<p>Connects to a process server.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.connectsession">ConnectSession</a>
</td>
<td align="left" width="63%">
<p>Joins the client to an existing debugger session.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.createclient">CreateClient</a>
</td>
<td align="left" width="63%">
<p>Creates a new client object for the current thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.createprocess">CreateProcess</a>
</td>
<td align="left" width="63%">
<p>Creates a process from the specified command line.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.createprocessandattach">CreateProcessAndAttach</a>
</td>
<td align="left" width="63%">
<p> Create a process from a specified command line, then attaches to another user-mode process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.detachprocesses">DetachProcesses</a>
</td>
<td align="left" width="63%">
<p>Detaches the debugger engine from all processes in all targets, resuming all their threads.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.disconnectprocessserver">DisconnectProcessServer</a>
</td>
<td align="left" width="63%">
<p>Disconnects the debugger engine from a process server.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.dispatchcallbacks">DispatchCallbacks</a>
</td>
<td align="left" width="63%">
<p>Enables the debugger engine to use the current thread for callbacks.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.endsession">EndSession</a>
</td>
<td align="left" width="63%">
<p>Ends the current debugger session.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.exitdispatch">ExitDispatch</a>
</td>
<td align="left" width="63%">
<p>Causes the <a href="debugger.dispatchcallbacks">DispatchCallbacks</a> method to return.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.flushcallbacks">FlushCallbacks</a>
</td>
<td align="left" width="63%">
<p> Forces any remaining buffered output to be delivered to the <a href="..\dbgeng\nn-dbgeng-idebugoutputcallbacks.md">IDebugOutputCallbacks</a> object registered with this client.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.geteventcallbacks">GetEventCallbacks</a>
</td>
<td align="left" width="63%">
<p>Returns the event callbacks object registered with this client.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getexitcode">GetExitCode</a>
</td>
<td align="left" width="63%">
<p>Returns the exit code of the current process if that process has already run through to completion.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getidentity">GetIdentity</a>
</td>
<td align="left" width="63%">
<p>Returns a string describing the computer and user this client represents.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getinputcallbacks">GetInputCallbacks</a>
</td>
<td align="left" width="63%">
<p>Returns the input callbacks object registered with this client.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getkernelconnectionoptions">GetKernelConnectionOptions</a>
</td>
<td align="left" width="63%">
<p>Returns the connection options for the current kernel target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getotheroutputmask">GetOtherOutputMask</a>
</td>
<td align="left" width="63%">
<p>Returns the output mask for another client.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoutputcallbacks">GetOutputCallbacks</a>
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
<a href="debugger.getoutputmask">GetOutputMask</a>
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
<a href="debugger.getprocessoptions">GetProcessOptions</a>
</td>
<td align="left" width="63%">
<p>Retrieves the process options affecting the current process.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getrunningprocessdescription">GetRunningProcessDescription</a>
</td>
<td align="left" width="63%">
<p>Returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getrunningprocesssystemidbyexecutablename">GetRunningProcessSystemIdByExecutableName</a>
</td>
<td align="left" width="63%">
<p> Searches for a process with a given executable file name and return its process ID.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getrunningprocesssystemids">GetRunningProcessSystemIds</a>
</td>
<td align="left" width="63%">
<p> Returns the process IDs for each running process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.opendumpfile">OpenDumpFile</a>
</td>
<td align="left" width="63%">
<p>Opens a dump file as a debugger target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputidentity">OutputIdentity</a>
</td>
<td align="left" width="63%">
<p> Formats and outputs a string describing the computer and user this client represents.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputservers">OutputServers</a>
</td>
<td align="left" width="63%">
<p>Lists the servers running on a given computer.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.removeprocessoptions">RemoveProcessOptions</a>
</td>
<td align="left" width="63%">
<p>Removes process options from those options that affect the current process.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.seteventcallbacks">SetEventCallbacks</a>
</td>
<td align="left" width="63%">
<p>Registers an event callbacks object with this client.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setinputcallbacks">SetInputCallbacks</a>
</td>
<td align="left" width="63%">
<p>Registers an input callbacks object with the client.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setkernelconnectionoptions">SetKernelConnectionOptions</a>
</td>
<td align="left" width="63%">
<p>Updates some of the connection options for a live kernel target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setotheroutputmask">SetOtherOutputMask</a>
</td>
<td align="left" width="63%">
<p>Sets the output mask for another client.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setoutputcallbacks">SetOutputCallbacks</a>
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
<a href="debugger.setoutputmask">SetOutputMask</a>
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
<a href="debugger.setprocessoptions">SetProcessOptions</a>
</td>
<td align="left" width="63%">
<p>Sets the process options affecting the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.startprocessserver">StartProcessServer</a>
</td>
<td align="left" width="63%">
<p>Starts a process server.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.startserver">StartServer</a>
</td>
<td align="left" width="63%">
<p> Starts a debugging server.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.terminateprocesses">TerminateProcesses</a>
</td>
<td align="left" width="63%">
<p>Attempts to terminate all processes in all targets.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writedumpfile">WriteDumpFile</a>
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

<p>Causes the <a href="debugger.dispatchcallbacks">DispatchCallbacks</a> method to return.</p>

<p> Forces any remaining buffered output to be delivered to the <a href="..\dbgeng\nn-dbgeng-idebugoutputcallbacks.md">IDebugOutputCallbacks</a> object registered with this client.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugclient2.md">IDebugClient2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient interface%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
