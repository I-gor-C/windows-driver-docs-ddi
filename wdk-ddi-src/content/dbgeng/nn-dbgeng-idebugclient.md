---
UID: NN:dbgeng.IDebugClient
title: IDebugClient
author: windows-driver-content
description: IDebugClient interface
old-location: debugger\idebugclient.htm
old-project: debugger
ms.assetid: 2e47f7ae-2017-4f05-9a06-6c09bb401e21
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IDebugClient, IDebugClient interface [Windows Debugging], IDebugClient interface [Windows Debugging], described, IDebugClient_3f5f6372-0e7d-4050-b09a-b7776ff8bf7c.xml, dbgeng/IDebugClient, debugger.idebugclient
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	dbgeng.h
api_name:
-	IDebugClient
-	IDebugClient.GetOutputWidth
-	IDebugClient.SetOutputWidth
-	IDebugClient.GetOutputLinePrefix
-	IDebugClient.SetOutputLinePrefix
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugClient interface



## Methods

<p>The <b>IDebugClient</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugClient::AddProcessOptions](nf-dbgeng-idebugclient-addprocessoptions.md) | The AddProcessOptions method adds the process options to those options that affect the current process. |
| [IDebugClient::AttachKernel](nf-dbgeng-idebugclient-attachkernel.md) | The AttachKernel methods connect the debugger engine to a kernel target. |
| [IDebugClient::AttachProcess](nf-dbgeng-idebugclient-attachprocess.md) | The AttachProcess method connects the debugger engine to a user-modeprocess. |
| [IDebugClient::ConnectProcessServer](nf-dbgeng-idebugclient-connectprocessserver.md) | The ConnectProcessServer methods connect to a process server. |
| [IDebugClient::ConnectSession](nf-dbgeng-idebugclient-connectsession.md) | The ConnectSession method joins the client to an existing debugger session. |
| [IDebugClient::CreateClient](nf-dbgeng-idebugclient-createclient.md) | The CreateClient method creates a new client object for the current thread. |
| [IDebugClient::CreateProcess](nf-dbgeng-idebugclient-createprocess.md) | The CreateProcess method creates a process from the specified command line. |
| [IDebugClient::CreateProcessAndAttach](nf-dbgeng-idebugclient-createprocessandattach.md) | The CreateProcessAndAttach method creates a process from a specified command line, then attach to another user-mode process. |
| [IDebugClient::DetachProcesses](nf-dbgeng-idebugclient-detachprocesses.md) | The DetachProcesses method detaches the debugger engine from all processes in all targets, resuming all their threads. |
| [IDebugClient::DisconnectProcessServer](nf-dbgeng-idebugclient-disconnectprocessserver.md) | The DisconnectProcessServer method disconnects the debugger engine from a process server. |
| [IDebugClient::DispatchCallbacks](nf-dbgeng-idebugclient-dispatchcallbacks.md) | The DispatchCallbacks method lets the debugger engine use the current thread for callbacks. |
| [IDebugClient::EndSession](nf-dbgeng-idebugclient-endsession.md) | The EndSession method ends the current debugger session. |
| [IDebugClient::ExitDispatch](nf-dbgeng-idebugclient-exitdispatch.md) | The ExitDispatch method causes the DispatchCallbacks method to return. |
| [IDebugClient::FlushCallbacks](nf-dbgeng-idebugclient-flushcallbacks.md) | The FlushCallbacks method forces any remaining buffered output to be delivered to the IDebugOutputCallbacks object registered with this client. |
| [IDebugClient::GetEventCallbacks](nf-dbgeng-idebugclient-geteventcallbacks.md) | The GetEventCallbacks method returns the event callbacks object registered with this client. |
| [IDebugClient::GetExitCode](nf-dbgeng-idebugclient-getexitcode.md) | The GetExitCode method returns the exit code of the current process if that process has already run through to completion. |
| [IDebugClient::GetIdentity](nf-dbgeng-idebugclient-getidentity.md) | The GetIdentity method returns a string describing the computer and user this client represents. |
| [IDebugClient::GetInputCallbacks](nf-dbgeng-idebugclient-getinputcallbacks.md) | The GetInputCallbacks method returns the input callbacks object registered with this client. |
| [IDebugClient::GetKernelConnectionOptions](nf-dbgeng-idebugclient-getkernelconnectionoptions.md) | The GetKernelConnectionOptions method returns the connection options for the current kernel target. |
| [IDebugClient::GetOtherOutputMask](nf-dbgeng-idebugclient-getotheroutputmask.md) | The GetOtherOutputMask method returns the output mask for another client. |
| [IDebugClient::GetOutputCallbacks](nf-dbgeng-idebugclient-getoutputcallbacks.md) | The GetOutputCallbacks method returns the output callbacks object registered with the client. |
| [IDebugClient::GetOutputLinePrefix](nf-dbgeng-idebugclient-getoutputlineprefix.md) | Gets the prefix used for multiple lines of output. |
| [IDebugClient::GetOutputMask](nf-dbgeng-idebugclient-getoutputmask.md) | The GetOutputMask method returns the output mask currently set for the client. |
| [IDebugClient::GetOutputWidth](nf-dbgeng-idebugclient-getoutputwidth.md) | Gets the width of an output line for commands that produce formatted output. |
| [IDebugClient::GetProcessOptions](nf-dbgeng-idebugclient-getprocessoptions.md) | The GetProcessOptions method retrieves the process options affecting the current process. |
| [IDebugClient::GetRunningProcessDescription](nf-dbgeng-idebugclient-getrunningprocessdescription.md) | The GetRunningProcessDescription method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [IDebugClient::GetRunningProcessSystemIdByExecutableName](nf-dbgeng-idebugclient-getrunningprocesssystemidbyexecutablename.md) | The GetRunningProcessSystemIdByExecutableName method searches for a process with a given executable file name and return its process ID. |
| [IDebugClient::GetRunningProcessSystemIds](nf-dbgeng-idebugclient-getrunningprocesssystemids.md) | The GetRunningProcessSystemIds method returns the process IDs for each running process. |
| [IDebugClient::OpenDumpFile](nf-dbgeng-idebugclient-opendumpfile.md) | The OpenDumpFile method opens a dump file as a debugger target. |
| [IDebugClient::OutputIdentity](nf-dbgeng-idebugclient-outputidentity.md) | The OutputIdentity method formats and outputs a string describing the computer and user this client represents. |
| [IDebugClient::OutputServers](nf-dbgeng-idebugclient-outputservers.md) | The OutputServers method lists the servers running on a given computer. |
| [IDebugClient::RemoveProcessOptions](nf-dbgeng-idebugclient-removeprocessoptions.md) | The RemoveProcessOptions method removes process options from those options that affect the current process. |
| [IDebugClient::SetEventCallbacks](nf-dbgeng-idebugclient-seteventcallbacks.md) | The SetEventCallbacks method registers an event callbacks object with this client. |
| [IDebugClient::SetInputCallbacks](nf-dbgeng-idebugclient-setinputcallbacks.md) | The SetInputCallbacks method registers an input callbacks object with the client. |
| [IDebugClient::SetKernelConnectionOptions](nf-dbgeng-idebugclient-setkernelconnectionoptions.md) | The SetKernelConnectionOptions method updates some of the connection options for a live kernel target. |
| [IDebugClient::SetOtherOutputMask](nf-dbgeng-idebugclient-setotheroutputmask.md) | The SetOtherOutputMask method sets the output mask for another client. |
| [IDebugClient::SetOutputCallbacks](nf-dbgeng-idebugclient-setoutputcallbacks.md) | The SetOutputCallbacks method registers an output callbacks object with this client. |
| [IDebugClient::SetOutputLinePrefix](nf-dbgeng-idebugclient-setoutputlineprefix.md) | Sets a prefix for multiple lines of output. |
| [IDebugClient::SetOutputMask](nf-dbgeng-idebugclient-setoutputmask.md) | The SetOutputMask method sets the output mask for the client. |
| [IDebugClient::SetOutputWidth](nf-dbgeng-idebugclient-setoutputwidth.md) | Controls the width of an output line for commands that produce formatted output. |
| [IDebugClient::SetProcessOptions](nf-dbgeng-idebugclient-setprocessoptions.md) | The SetProcessOptions method sets the process options affecting the current process. |
| [IDebugClient::StartProcessServer](nf-dbgeng-idebugclient-startprocessserver.md) | The StartProcessServer method starts a process server. |
| [IDebugClient::StartServer](nf-dbgeng-idebugclient-startserver.md) | The StartServer method starts a debugging server. |
| [IDebugClient::TerminateProcesses](nf-dbgeng-idebugclient-terminateprocesses.md) | The TerminateProcesses method attempts to terminate all processes in all targets. |
| [IDebugClient::WriteDumpFile](nf-dbgeng-idebugclient-writedumpfile.md) | The WriteDumpFile method creates a user-mode or kernel-modecrash dump file. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>



<a href="..\dbgeng\nn-dbgeng-idebugclient2.md">IDebugClient2</a>



<a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>



<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>