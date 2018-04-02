---
UID: NN:dbgeng.IDebugClient3
title: IDebugClient3
author: windows-driver-content
description: IDebugClient3 interface
old-location: debugger\idebugclient3.htm
old-project: debugger
ms.assetid: 316a4d8b-4cf6-4270-8d9b-e1ede53d567d
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugClient3, IDebugClient3 interface [Windows Debugging], IDebugClient3 interface [Windows Debugging], described, dbgeng/IDebugClient3, debugger.idebugclient3
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
-	IDebugClient3
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugClient3 interface



## Methods

<p>The <b>IDebugClient3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugClient3::AbandonCurrentProcess](nf-dbgeng-idebugclient3-abandoncurrentprocess.md) | The AbandonCurrentProcess method removes the current process from the debugger engine's process list without detaching or terminating the process. |
| [IDebugClient3::AddDumpInformationFile](nf-dbgeng-idebugclient3-adddumpinformationfile.md) | The AddDumpInformationFile method registers additional files containing supporting information that will be used when opening a dump file. The Unicode version of this method is AddDumpInformationFileWide. |
| [IDebugClient3::AddProcessOptions](nf-dbgeng-idebugclient3-addprocessoptions.md) | The AddProcessOptions method adds the process options to those options that affect the current process. |
| [IDebugClient3::AttachKernel](nf-dbgeng-idebugclient3-attachkernel.md) | The AttachKernel methods connect the debugger engine to a kernel target. |
| [IDebugClient3::AttachProcess](nf-dbgeng-idebugclient3-attachprocess.md) | The AttachProcess method connects the debugger engine to a user-modeprocess. |
| [IDebugClient3::ConnectProcessServer](nf-dbgeng-idebugclient3-connectprocessserver.md) | The ConnectProcessServer methods connect to a process server. |
| [IDebugClient3::ConnectSession](nf-dbgeng-idebugclient3-connectsession.md) | The ConnectSession method joins the client to an existing debugger session. |
| [IDebugClient3::CreateClient](nf-dbgeng-idebugclient3-createclient.md) | The CreateClient method creates a new client object for the current thread. |
| [IDebugClient3::CreateProcess](nf-dbgeng-idebugclient3-createprocess.md) | The CreateProcess method creates a process from the specified command line. |
| [IDebugClient3::CreateProcessAndAttach](nf-dbgeng-idebugclient3-createprocessandattach.md) | The CreateProcessAndAttach method creates a process from a specified command line, then attach to another user-mode process. |
| [IDebugClient3::CreateProcessAndAttachWide](nf-dbgeng-idebugclient3-createprocessandattachwide.md) | The CreateProcessAndAttachWide method creates a process from a specified command line, then attach to another user-mode process. |
| [IDebugClient3::CreateProcessWide](nf-dbgeng-idebugclient3-createprocesswide.md) | The CreateProcessWide method creates a process from the specified command line. |
| [IDebugClient3::DetachCurrentProcess](nf-dbgeng-idebugclient3-detachcurrentprocess.md) | The DetachCurrentProcess method detaches the debugger engine from the current process, resuming all its threads. |
| [IDebugClient3::DetachProcesses](nf-dbgeng-idebugclient3-detachprocesses.md) | The DetachProcesses method detaches the debugger engine from all processes in all targets, resuming all their threads. |
| [IDebugClient3::DisconnectProcessServer](nf-dbgeng-idebugclient3-disconnectprocessserver.md) | The DisconnectProcessServer method disconnects the debugger engine from a process server. |
| [IDebugClient3::DispatchCallbacks](nf-dbgeng-idebugclient3-dispatchcallbacks.md) | The DispatchCallbacks method lets the debugger engine use the current thread for callbacks. |
| [IDebugClient3::EndProcessServer](nf-dbgeng-idebugclient3-endprocessserver.md) | The EndProcessServer method requests that a process server be shut down. |
| [IDebugClient3::EndSession](nf-dbgeng-idebugclient3-endsession.md) | The EndSession method ends the current debugger session. |
| [IDebugClient3::ExitDispatch](nf-dbgeng-idebugclient3-exitdispatch.md) | The ExitDispatch method causes the DispatchCallbacks method to return. |
| [IDebugClient3::FlushCallbacks](nf-dbgeng-idebugclient3-flushcallbacks.md) | The FlushCallbacks method forces any remaining buffered output to be delivered to the IDebugOutputCallbacks object registered with this client. |
| [IDebugClient3::GetEventCallbacks](nf-dbgeng-idebugclient3-geteventcallbacks.md) | The GetEventCallbacks method returns the event callbacks object registered with this client. |
| [IDebugClient3::GetExitCode](nf-dbgeng-idebugclient3-getexitcode.md) | The GetExitCode method returns the exit code of the current process if that process has already run through to completion. |
| [IDebugClient3::GetIdentity](nf-dbgeng-idebugclient3-getidentity.md) | The GetIdentity method returns a string describing the computer and user this client represents. |
| [IDebugClient3::GetInputCallbacks](nf-dbgeng-idebugclient3-getinputcallbacks.md) | The GetInputCallbacks method returns the input callbacks object registered with this client. |
| [IDebugClient3::GetKernelConnectionOptions](nf-dbgeng-idebugclient3-getkernelconnectionoptions.md) | The GetKernelConnectionOptions method returns the connection options for the current kernel target. |
| [IDebugClient3::GetOtherOutputMask](nf-dbgeng-idebugclient3-getotheroutputmask.md) | The GetOtherOutputMask method returns the output mask for another client. |
| [IDebugClient3::GetOutputCallbacks](nf-dbgeng-idebugclient3-getoutputcallbacks.md) | The GetOutputCallbacks method returns the output callbacks object registered with the client. |
| [IDebugClient3::GetOutputMask](nf-dbgeng-idebugclient3-getoutputmask.md) | The GetOutputMask method returns the output mask currently set for the client. |
| [IDebugClient3::GetProcessOptions](nf-dbgeng-idebugclient3-getprocessoptions.md) | The GetProcessOptions method retrieves the process options affecting the current process. |
| [IDebugClient3::GetRunningProcessDescription](nf-dbgeng-idebugclient3-getrunningprocessdescription.md) | The GetRunningProcessDescription method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [IDebugClient3::GetRunningProcessDescriptionWide](nf-dbgeng-idebugclient3-getrunningprocessdescriptionwide.md) | The GetRunningProcessDescriptionWide method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [IDebugClient3::GetRunningProcessSystemIdByExecutableName](nf-dbgeng-idebugclient3-getrunningprocesssystemidbyexecutablename.md) | The GetRunningProcessSystemIdByExecutableName method searches for a process with a given executable file name and return its process ID. |
| [IDebugClient3::GetRunningProcessSystemIdByExecutableNameWide](nf-dbgeng-idebugclient3-getrunningprocesssystemidbyexecutablenamewide.md) | The GetRunningProcessSystemIdByExecutableNameWide method searches for a process with a given executable file name and return its process ID. |
| [IDebugClient3::GetRunningProcessSystemIds](nf-dbgeng-idebugclient3-getrunningprocesssystemids.md) | The GetRunningProcessSystemIds method returns the process IDs for each running process. |
| [IDebugClient3::IsKernelDebuggerEnabled](nf-dbgeng-idebugclient3-iskerneldebuggerenabled.md) | The IsKernelDebuggerEnabled method checks whether kernel debugging is enabled for the local kernel. |
| [IDebugClient3::OpenDumpFile](nf-dbgeng-idebugclient3-opendumpfile.md) | The OpenDumpFile method opens a dump file as a debugger target. |
| [IDebugClient3::OutputIdentity](nf-dbgeng-idebugclient3-outputidentity.md) | The OutputIdentity method formats and outputs a string describing the computer and user this client represents. |
| [IDebugClient3::OutputServers](nf-dbgeng-idebugclient3-outputservers.md) | The OutputServers method lists the servers running on a given computer. |
| [IDebugClient3::RemoveProcessOptions](nf-dbgeng-idebugclient3-removeprocessoptions.md) | The RemoveProcessOptions method removes process options from those options that affect the current process. |
| [IDebugClient3::SetEventCallbacks](nf-dbgeng-idebugclient3-seteventcallbacks.md) | The SetEventCallbacks method registers an event callbacks object with this client. |
| [IDebugClient3::SetInputCallbacks](nf-dbgeng-idebugclient3-setinputcallbacks.md) | The SetInputCallbacks method registers an input callbacks object with the client. |
| [IDebugClient3::SetKernelConnectionOptions](nf-dbgeng-idebugclient3-setkernelconnectionoptions.md) | The SetKernelConnectionOptions method updates some of the connection options for a live kernel target. |
| [IDebugClient3::SetOtherOutputMask](nf-dbgeng-idebugclient3-setotheroutputmask.md) | The SetOtherOutputMask method sets the output mask for another client. |
| [IDebugClient3::SetOutputCallbacks](nf-dbgeng-idebugclient3-setoutputcallbacks.md) | The SetOutputCallbacks method registers an output callbacks object with this client. |
| [IDebugClient3::SetOutputMask](nf-dbgeng-idebugclient3-setoutputmask.md) | The SetOutputMask method sets the output mask for the client. |
| [IDebugClient3::SetProcessOptions](nf-dbgeng-idebugclient3-setprocessoptions.md) | The SetProcessOptions method sets the process options affecting the current process. |
| [IDebugClient3::StartProcessServer](nf-dbgeng-idebugclient3-startprocessserver.md) | The StartProcessServer method starts a process server. |
| [IDebugClient3::StartServer](nf-dbgeng-idebugclient3-startserver.md) | The StartServer method starts a debugging server. |
| [IDebugClient3::TerminateCurrentProcess](nf-dbgeng-idebugclient3-terminatecurrentprocess.md) | The TerminateCurrentProcess method attempts to terminate the current process. |
| [IDebugClient3::TerminateProcesses](nf-dbgeng-idebugclient3-terminateprocesses.md) | The TerminateProcesses method attempts to terminate all processes in all targets. |
| [IDebugClient3::WaitForProcessServerEnd](nf-dbgeng-idebugclient3-waitforprocessserverend.md) | The WaitForProcessServerEnd method waits for a local process server to exit. |
| [IDebugClient3::WriteDumpFile](nf-dbgeng-idebugclient3-writedumpfile.md) | The WriteDumpFile method creates a user-mode or kernel-modecrash dump file. |
| [IDebugClient3::WriteDumpFile2](nf-dbgeng-idebugclient3-writedumpfile2.md) | The WriteDumpFile2 method creates a user-mode or kernel-modecrash dump file. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550481">IDebugClient2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550494">IDebugClient4</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>