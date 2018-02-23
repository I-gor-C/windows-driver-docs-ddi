---
UID: NN:dbgeng.IDebugClient2
title: IDebugClient2
author: windows-driver-content
description: IDebugClient2 interface
old-location: debugger\idebugclient2.htm
old-project: Debugger
ms.assetid: 0ea32baa-b318-44ec-8696-a5b42fe73ed1
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: debugger.idebugclient2, IDebugClient2 interface [Windows Debugging], IDebugClient2 interface [Windows Debugging], described, IDebugClient2, dbgeng/IDebugClient2
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
req.lib: dbgeng.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	dbgeng.h
apiname:
-	IDebugClient2
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugClient2 interface



## Methods

<p>The <b>IDebugClient2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugClient2.AbandonCurrentProcess](nf-dbgeng-idebugclient2-abandoncurrentprocess.md) | The AbandonCurrentProcess method removes the current process from the debugger engine's process list without detaching or terminating the process. |
| [dbgeng.IDebugClient2.AddDumpInformationFile](nf-dbgeng-idebugclient2-adddumpinformationfile.md) | The AddDumpInformationFile method registers additional files containing supporting information that will be used when opening a dump file. The Unicode version of this method is AddDumpInformationFileWide. |
| [dbgeng.IDebugClient2.AddProcessOptions](nf-dbgeng-idebugclient2-addprocessoptions.md) | The AddProcessOptions method adds the process options to those options that affect the current process. |
| [dbgeng.IDebugClient2.AttachKernel](nf-dbgeng-idebugclient2-attachkernel.md) | The AttachKernel methods connect the debugger engine to a kernel target. |
| [dbgeng.IDebugClient2.AttachProcess](nf-dbgeng-idebugclient2-attachprocess.md) | The AttachProcess method connects the debugger engine to a user-modeprocess. |
| [dbgeng.IDebugClient2.ConnectProcessServer](nf-dbgeng-idebugclient2-connectprocessserver.md) | The ConnectProcessServer methods connect to a process server. |
| [dbgeng.IDebugClient2.ConnectSession](nf-dbgeng-idebugclient2-connectsession.md) | The ConnectSession method joins the client to an existing debugger session. |
| [dbgeng.IDebugClient2.CreateClient](nf-dbgeng-idebugclient2-createclient.md) | The CreateClient method creates a new client object for the current thread. |
| [dbgeng.IDebugClient2.CreateProcess](nf-dbgeng-idebugclient2-createprocess.md) | The CreateProcess method creates a process from the specified command line. |
| [dbgeng.IDebugClient2.CreateProcessAndAttach](nf-dbgeng-idebugclient2-createprocessandattach.md) | The CreateProcessAndAttach method creates a process from a specified command line, then attach to another user-mode process. |
| [dbgeng.IDebugClient2.DetachCurrentProcess](nf-dbgeng-idebugclient2-detachcurrentprocess.md) | The DetachCurrentProcess method detaches the debugger engine from the current process, resuming all its threads. |
| [dbgeng.IDebugClient2.DetachProcesses](nf-dbgeng-idebugclient2-detachprocesses.md) | The DetachProcesses method detaches the debugger engine from all processes in all targets, resuming all their threads. |
| [dbgeng.IDebugClient2.DisconnectProcessServer](nf-dbgeng-idebugclient2-disconnectprocessserver.md) | The DisconnectProcessServer method disconnects the debugger engine from a process server. |
| [dbgeng.IDebugClient2.DispatchCallbacks](nf-dbgeng-idebugclient2-dispatchcallbacks.md) | The DispatchCallbacks method lets the debugger engine use the current thread for callbacks. |
| [dbgeng.IDebugClient2.EndProcessServer](nf-dbgeng-idebugclient2-endprocessserver.md) | The EndProcessServer method requests that a process server be shut down. |
| [dbgeng.IDebugClient2.EndSession](nf-dbgeng-idebugclient2-endsession.md) | The EndSession method ends the current debugger session. |
| [dbgeng.IDebugClient2.ExitDispatch](nf-dbgeng-idebugclient2-exitdispatch.md) | The ExitDispatch method causes the DispatchCallbacks method to return. |
| [dbgeng.IDebugClient2.FlushCallbacks](nf-dbgeng-idebugclient2-flushcallbacks.md) | The FlushCallbacks method forces any remaining buffered output to be delivered to the IDebugOutputCallbacks object registered with this client. |
| [dbgeng.IDebugClient2.GetEventCallbacks](nf-dbgeng-idebugclient2-geteventcallbacks.md) | The GetEventCallbacks method returns the event callbacks object registered with this client. |
| [dbgeng.IDebugClient2.GetExitCode](nf-dbgeng-idebugclient2-getexitcode.md) | The GetExitCode method returns the exit code of the current process if that process has already run through to completion. |
| [dbgeng.IDebugClient2.GetIdentity](nf-dbgeng-idebugclient2-getidentity.md) | The GetIdentity method returns a string describing the computer and user this client represents. |
| [dbgeng.IDebugClient2.GetInputCallbacks](nf-dbgeng-idebugclient2-getinputcallbacks.md) | The GetInputCallbacks method returns the input callbacks object registered with this client. |
| [dbgeng.IDebugClient2.GetKernelConnectionOptions](nf-dbgeng-idebugclient2-getkernelconnectionoptions.md) | The GetKernelConnectionOptions method returns the connection options for the current kernel target. |
| [dbgeng.IDebugClient2.GetOtherOutputMask](nf-dbgeng-idebugclient2-getotheroutputmask.md) | The GetOtherOutputMask method returns the output mask for another client. |
| [dbgeng.IDebugClient2.GetOutputCallbacks](nf-dbgeng-idebugclient2-getoutputcallbacks.md) | The GetOutputCallbacks method returns the output callbacks object registered with the client. |
| [dbgeng.IDebugClient2.GetOutputMask](nf-dbgeng-idebugclient2-getoutputmask.md) | The GetOutputMask method returns the output mask currently set for the client. |
| [dbgeng.IDebugClient2.GetProcessOptions](nf-dbgeng-idebugclient2-getprocessoptions.md) | The GetProcessOptions method retrieves the process options affecting the current process. |
| [dbgeng.IDebugClient2.GetRunningProcessDescription](nf-dbgeng-idebugclient2-getrunningprocessdescription.md) | The GetRunningProcessDescription method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [dbgeng.IDebugClient2.GetRunningProcessSystemIdByExecutableName](nf-dbgeng-idebugclient2-getrunningprocesssystemidbyexecutablename.md) | The GetRunningProcessSystemIdByExecutableName method searches for a process with a given executable file name and return its process ID. |
| [dbgeng.IDebugClient2.GetRunningProcessSystemIds](nf-dbgeng-idebugclient2-getrunningprocesssystemids.md) | The GetRunningProcessSystemIds method returns the process IDs for each running process. |
| [dbgeng.IDebugClient2.IsKernelDebuggerEnabled](nf-dbgeng-idebugclient2-iskerneldebuggerenabled.md) | The IsKernelDebuggerEnabled method checks whether kernel debugging is enabled for the local kernel. |
| [dbgeng.IDebugClient2.OpenDumpFile](nf-dbgeng-idebugclient2-opendumpfile.md) | The OpenDumpFile method opens a dump file as a debugger target. |
| [dbgeng.IDebugClient2.OutputIdentity](nf-dbgeng-idebugclient2-outputidentity.md) | The OutputIdentity method formats and outputs a string describing the computer and user this client represents. |
| [dbgeng.IDebugClient2.OutputServers](nf-dbgeng-idebugclient2-outputservers.md) | The OutputServers method lists the servers running on a given computer. |
| [dbgeng.IDebugClient2.RemoveProcessOptions](nf-dbgeng-idebugclient2-removeprocessoptions.md) | The RemoveProcessOptions method removes process options from those options that affect the current process. |
| [dbgeng.IDebugClient2.SetEventCallbacks](nf-dbgeng-idebugclient2-seteventcallbacks.md) | The SetEventCallbacks method registers an event callbacks object with this client. |
| [dbgeng.IDebugClient2.SetInputCallbacks](nf-dbgeng-idebugclient2-setinputcallbacks.md) | The SetInputCallbacks method registers an input callbacks object with the client. |
| [dbgeng.IDebugClient2.SetKernelConnectionOptions](nf-dbgeng-idebugclient2-setkernelconnectionoptions.md) | The SetKernelConnectionOptions method updates some of the connection options for a live kernel target. |
| [dbgeng.IDebugClient2.SetOtherOutputMask](nf-dbgeng-idebugclient2-setotheroutputmask.md) | The SetOtherOutputMask method sets the output mask for another client. |
| [dbgeng.IDebugClient2.SetOutputCallbacks](nf-dbgeng-idebugclient2-setoutputcallbacks.md) | The SetOutputCallbacks method registers an output callbacks object with this client. |
| [dbgeng.IDebugClient2.SetOutputMask](nf-dbgeng-idebugclient2-setoutputmask.md) | The SetOutputMask method sets the output mask for the client. |
| [dbgeng.IDebugClient2.SetProcessOptions](nf-dbgeng-idebugclient2-setprocessoptions.md) | The SetProcessOptions method sets the process options affecting the current process. |
| [dbgeng.IDebugClient2.StartProcessServer](nf-dbgeng-idebugclient2-startprocessserver.md) | The StartProcessServer method starts a process server. |
| [dbgeng.IDebugClient2.StartServer](nf-dbgeng-idebugclient2-startserver.md) | The StartServer method starts a debugging server. |
| [dbgeng.IDebugClient2.TerminateCurrentProcess](nf-dbgeng-idebugclient2-terminatecurrentprocess.md) | The TerminateCurrentProcess method attempts to terminate the current process. |
| [dbgeng.IDebugClient2.TerminateProcesses](nf-dbgeng-idebugclient2-terminateprocesses.md) | The TerminateProcesses method attempts to terminate all processes in all targets. |
| [dbgeng.IDebugClient2.WaitForProcessServerEnd](nf-dbgeng-idebugclient2-waitforprocessserverend.md) | The WaitForProcessServerEnd method waits for a local process server to exit. |
| [dbgeng.IDebugClient2.WriteDumpFile](nf-dbgeng-idebugclient2-writedumpfile.md) | The WriteDumpFile method creates a user-mode or kernel-modecrash dump file. |
| [dbgeng.IDebugClient2.WriteDumpFile2](nf-dbgeng-idebugclient2-writedumpfile2.md) | The WriteDumpFile2 method creates a user-mode or kernel-modecrash dump file. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>



<a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>



<a href="..\dbgeng\nn-dbgeng-idebugclient.md">IDebugClient</a>



<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugClient2 interface%20 RELEASE:%20(2/15/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>