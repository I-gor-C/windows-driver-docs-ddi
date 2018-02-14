---
UID: NN:dbgeng.IDebugClient4
title: IDebugClient4
author: windows-driver-content
description: IDebugClient4 interface
old-location: debugger\idebugclient4.htm
old-project: debugger
ms.assetid: fcfa64f3-6cdf-4e5a-bb02-13a748fd6dda
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugclient4, IDebugClient4 interface [Windows Debugging], IDebugClient4 interface [Windows Debugging], described, IDebugClient4, dbgeng/IDebugClient4
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
-	IDebugClient4
product: Windows
targetos: Windows
req.typenames: "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---

# IDebugClient4 interface



## Methods

<p>The <b>IDebugClient4</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugClient4.AbandonCurrentProcess](nf-dbgeng-idebugclient4-abandoncurrentprocess.md) | The AbandonCurrentProcess method removes the current process from the debugger engine's process list without detaching or terminating the process. |
| [dbgeng.IDebugClient4.AddDumpInformationFile](nf-dbgeng-idebugclient4-adddumpinformationfile.md) | The AddDumpInformationFile method registers additional files containing supporting information that will be used when opening a dump file. The Unicode version of this method is AddDumpInformationFileWide. |
| [dbgeng.IDebugClient4.AddDumpInformationFileWide](nf-dbgeng-idebugclient4-adddumpinformationfilewide.md) | The AddDumpInformationFileWide method registers additional files containing supporting information that will be used when opening a dump file. The ASCII version of this method is AddDumpInformationFile. |
| [dbgeng.IDebugClient4.AddProcessOptions](nf-dbgeng-idebugclient4-addprocessoptions.md) | The AddProcessOptions method adds the process options to those options that affect the current process. |
| [dbgeng.IDebugClient4.AttachKernel](nf-dbgeng-idebugclient4-attachkernel.md) | The AttachKernel methods connect the debugger engine to a kernel target. |
| [dbgeng.IDebugClient4.AttachProcess](nf-dbgeng-idebugclient4-attachprocess.md) | The AttachProcess method connects the debugger engine to a user-modeprocess. |
| [dbgeng.IDebugClient4.ConnectProcessServer](nf-dbgeng-idebugclient4-connectprocessserver.md) | The ConnectProcessServer methods connect to a process server. |
| [dbgeng.IDebugClient4.ConnectSession](nf-dbgeng-idebugclient4-connectsession.md) | The ConnectSession method joins the client to an existing debugger session. |
| [dbgeng.IDebugClient4.CreateClient](nf-dbgeng-idebugclient4-createclient.md) | The CreateClient method creates a new client object for the current thread. |
| [dbgeng.IDebugClient4.CreateProcess](nf-dbgeng-idebugclient4-createprocess.md) | The CreateProcess method creates a process from the specified command line. |
| [dbgeng.IDebugClient4.CreateProcessAndAttach](nf-dbgeng-idebugclient4-createprocessandattach.md) | The CreateProcessAndAttach method creates a process from a specified command line, then attach to another user-mode process. |
| [dbgeng.IDebugClient4.CreateProcessAndAttachWide](nf-dbgeng-idebugclient4-createprocessandattachwide.md) | The CreateProcessAndAttachWide method creates a process from a specified command line, then attach to another user-mode process. |
| [dbgeng.IDebugClient4.CreateProcessWide](nf-dbgeng-idebugclient4-createprocesswide.md) | The CreateProcessWide method creates a process from the specified command line. |
| [dbgeng.IDebugClient4.DetachCurrentProcess](nf-dbgeng-idebugclient4-detachcurrentprocess.md) | The DetachCurrentProcess method detaches the debugger engine from the current process, resuming all its threads. |
| [dbgeng.IDebugClient4.DetachProcesses](nf-dbgeng-idebugclient4-detachprocesses.md) | The DetachProcesses method detaches the debugger engine from all processes in all targets, resuming all their threads. |
| [dbgeng.IDebugClient4.DisconnectProcessServer](nf-dbgeng-idebugclient4-disconnectprocessserver.md) | The DisconnectProcessServer method disconnects the debugger engine from a process server. |
| [dbgeng.IDebugClient4.DispatchCallbacks](nf-dbgeng-idebugclient4-dispatchcallbacks.md) | The DispatchCallbacks method lets the debugger engine use the current thread for callbacks. |
| [dbgeng.IDebugClient4.EndProcessServer](nf-dbgeng-idebugclient4-endprocessserver.md) | The EndProcessServer method requests that a process server be shut down. |
| [dbgeng.IDebugClient4.EndSession](nf-dbgeng-idebugclient4-endsession.md) | The EndSession method ends the current debugger session. |
| [dbgeng.IDebugClient4.ExitDispatch](nf-dbgeng-idebugclient4-exitdispatch.md) | The ExitDispatch method causes the DispatchCallbacks method to return. |
| [dbgeng.IDebugClient4.FlushCallbacks](nf-dbgeng-idebugclient4-flushcallbacks.md) | The FlushCallbacks method forces any remaining buffered output to be delivered to the IDebugOutputCallbacks object registered with this client. |
| [dbgeng.IDebugClient4.GetDumpFile](nf-dbgeng-idebugclient4-getdumpfile.md) | The GetDumpFile method describes the files containing supporting information that were used when opening the current dump target. |
| [dbgeng.IDebugClient4.GetDumpFileWide](nf-dbgeng-idebugclient4-getdumpfilewide.md) | The GetDumpFileWide method describes the files containing supporting information that were used when opening the current dump target. |
| [dbgeng.IDebugClient4.GetEventCallbacks](nf-dbgeng-idebugclient4-geteventcallbacks.md) | The GetEventCallbacks method returns the event callbacks object registered with this client. |
| [dbgeng.IDebugClient4.GetExitCode](nf-dbgeng-idebugclient4-getexitcode.md) | The GetExitCode method returns the exit code of the current process if that process has already run through to completion. |
| [dbgeng.IDebugClient4.GetIdentity](nf-dbgeng-idebugclient4-getidentity.md) | The GetIdentity method returns a string describing the computer and user this client represents. |
| [dbgeng.IDebugClient4.GetInputCallbacks](nf-dbgeng-idebugclient4-getinputcallbacks.md) | The GetInputCallbacks method returns the input callbacks object registered with this client. |
| [dbgeng.IDebugClient4.GetKernelConnectionOptions](nf-dbgeng-idebugclient4-getkernelconnectionoptions.md) | The GetKernelConnectionOptions method returns the connection options for the current kernel target. |
| [dbgeng.IDebugClient4.GetNumberDumpFiles](nf-dbgeng-idebugclient4-getnumberdumpfiles.md) | The GetNumberDumpFiles method returns the number of files containing supporting information that were used when opening the current dump target. |
| [dbgeng.IDebugClient4.GetOtherOutputMask](nf-dbgeng-idebugclient4-getotheroutputmask.md) | The GetOtherOutputMask method returns the output mask for another client. |
| [dbgeng.IDebugClient4.GetOutputCallbacks](nf-dbgeng-idebugclient4-getoutputcallbacks.md) | The GetOutputCallbacks method returns the output callbacks object registered with the client. |
| [dbgeng.IDebugClient4.GetOutputMask](nf-dbgeng-idebugclient4-getoutputmask.md) | The GetOutputMask method returns the output mask currently set for the client. |
| [dbgeng.IDebugClient4.GetProcessOptions](nf-dbgeng-idebugclient4-getprocessoptions.md) | The GetProcessOptions method retrieves the process options affecting the current process. |
| [dbgeng.IDebugClient4.GetRunningProcessDescription](nf-dbgeng-idebugclient4-getrunningprocessdescription.md) | The GetRunningProcessDescription method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [dbgeng.IDebugClient4.GetRunningProcessDescriptionWide](nf-dbgeng-idebugclient4-getrunningprocessdescriptionwide.md) | The GetRunningProcessDescriptionWide method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [dbgeng.IDebugClient4.GetRunningProcessSystemIdByExecutableName](nf-dbgeng-idebugclient4-getrunningprocesssystemidbyexecutablename.md) | The GetRunningProcessSystemIdByExecutableName method searches for a process with a given executable file name and return its process ID. |
| [dbgeng.IDebugClient4.GetRunningProcessSystemIdByExecutableNameWide](nf-dbgeng-idebugclient4-getrunningprocesssystemidbyexecutablenamewide.md) | The GetRunningProcessSystemIdByExecutableNameWide method searches for a process with a given executable file name and return its process ID. |
| [dbgeng.IDebugClient4.GetRunningProcessSystemIds](nf-dbgeng-idebugclient4-getrunningprocesssystemids.md) | The GetRunningProcessSystemIds method returns the process IDs for each running process. |
| [dbgeng.IDebugClient4.IsKernelDebuggerEnabled](nf-dbgeng-idebugclient4-iskerneldebuggerenabled.md) | The IsKernelDebuggerEnabled method checks whether kernel debugging is enabled for the local kernel. |
| [dbgeng.IDebugClient4.OpenDumpFile](nf-dbgeng-idebugclient4-opendumpfile.md) | The OpenDumpFile method opens a dump file as a debugger target. |
| [dbgeng.IDebugClient4.OpenDumpFileWide](nf-dbgeng-idebugclient4-opendumpfilewide.md) | The OpenDumpFileWide method opens a dump file as a debugger target. |
| [dbgeng.IDebugClient4.OutputIdentity](nf-dbgeng-idebugclient4-outputidentity.md) | The OutputIdentity method formats and outputs a string describing the computer and user this client represents. |
| [dbgeng.IDebugClient4.OutputServers](nf-dbgeng-idebugclient4-outputservers.md) | The OutputServers method lists the servers running on a given computer. |
| [dbgeng.IDebugClient4.RemoveProcessOptions](nf-dbgeng-idebugclient4-removeprocessoptions.md) | The RemoveProcessOptions method removes process options from those options that affect the current process. |
| [dbgeng.IDebugClient4.SetEventCallbacks](nf-dbgeng-idebugclient4-seteventcallbacks.md) | The SetEventCallbacks method registers an event callbacks object with this client. |
| [dbgeng.IDebugClient4.SetInputCallbacks](nf-dbgeng-idebugclient4-setinputcallbacks.md) | The SetInputCallbacks method registers an input callbacks object with the client. |
| [dbgeng.IDebugClient4.SetKernelConnectionOptions](nf-dbgeng-idebugclient4-setkernelconnectionoptions.md) | The SetKernelConnectionOptions method updates some of the connection options for a live kernel target. |
| [dbgeng.IDebugClient4.SetOtherOutputMask](nf-dbgeng-idebugclient4-setotheroutputmask.md) | The SetOtherOutputMask method sets the output mask for another client. |
| [dbgeng.IDebugClient4.SetOutputCallbacks](nf-dbgeng-idebugclient4-setoutputcallbacks.md) | The SetOutputCallbacks method registers an output callbacks object with this client. |
| [dbgeng.IDebugClient4.SetOutputMask](nf-dbgeng-idebugclient4-setoutputmask.md) | The SetOutputMask method sets the output mask for the client. |
| [dbgeng.IDebugClient4.SetProcessOptions](nf-dbgeng-idebugclient4-setprocessoptions.md) | The SetProcessOptions method sets the process options affecting the current process. |
| [dbgeng.IDebugClient4.StartProcessServer](nf-dbgeng-idebugclient4-startprocessserver.md) | The StartProcessServer method starts a process server. |
| [dbgeng.IDebugClient4.StartServer](nf-dbgeng-idebugclient4-startserver.md) | The StartServer method starts a debugging server. |
| [dbgeng.IDebugClient4.TerminateCurrentProcess](nf-dbgeng-idebugclient4-terminatecurrentprocess.md) | The TerminateCurrentProcess method attempts to terminate the current process. |
| [dbgeng.IDebugClient4.TerminateProcesses](nf-dbgeng-idebugclient4-terminateprocesses.md) | The TerminateProcesses method attempts to terminate all processes in all targets. |
| [dbgeng.IDebugClient4.WaitForProcessServerEnd](nf-dbgeng-idebugclient4-waitforprocessserverend.md) | The WaitForProcessServerEnd method waits for a local process server to exit. |
| [dbgeng.IDebugClient4.WriteDumpFile](nf-dbgeng-idebugclient4-writedumpfile.md) | The WriteDumpFile method creates a user-mode or kernel-modecrash dump file. |
| [dbgeng.IDebugClient4.WriteDumpFile2](nf-dbgeng-idebugclient4-writedumpfile2.md) | The WriteDumpFile2 method creates a user-mode or kernel-modecrash dump file. |
| [dbgeng.IDebugClient4.WriteDumpFileWide](nf-dbgeng-idebugclient4-writedumpfilewide.md) | The WriteDumpFileWide method creates a user-mode or kernel-modecrash dump file. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>



<a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient4 interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>