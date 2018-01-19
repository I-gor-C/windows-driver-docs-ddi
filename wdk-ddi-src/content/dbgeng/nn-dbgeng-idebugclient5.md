---
UID : NN:dbgeng.IDebugClient5
title : IDebugClient5
author : windows-driver-content
description : IDebugClient5 interface
old-location : debugger\idebugclient5.htm
old-project : debugger
ms.assetid : 4230fbc2-524a-44b1-a090-011e334629a7
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugSystemObjects4, IDebugSystemObjects4::SetImplicitThreadDataOffset, SetImplicitThreadDataOffset
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : dbgeng.h
req.include-header : Dbgeng.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IDebugClient5,IDebugClient5.GetOutputLinePrefixWide,IDebugClient5.SetOutputLinePrefixWide,IDebugClient5.PushOutputLinePrefix,IDebugClient5.PushOutputLinePrefixWide,IDebugClient5.PopOutputLinePrefix,IDebugClient5.GetQuitLockString,IDebugClient5.SetQuitLockString,IDebugClient5.GetQuitLockStringWide,IDebugClient5.SetQuitLockStringWide
req.alt-loc : dbgeng.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---

# IDebugClient5 interface



## Methods

<p>The <b>IDebugClient5</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugClient5.AbandonCurrentProcess](nf-dbgeng-idebugclient5-abandoncurrentprocess.md) | The AbandonCurrentProcess method removes the current process from the debugger engine's process list without detaching or terminating the process. |
| [dbgeng.IDebugClient5.AddDumpInformationFile](nf-dbgeng-idebugclient5-adddumpinformationfile.md) | The AddDumpInformationFile method registers additional files containing supporting information that will be used when opening a dump file. The Unicode version of this method is AddDumpInformationFileWide. |
| [dbgeng.IDebugClient5.AddDumpInformationFileWide](nf-dbgeng-idebugclient5-adddumpinformationfilewide.md) | The AddDumpInformationFileWide method registers additional files containing supporting information that will be used when opening a dump file. The ASCII version of this method is AddDumpInformationFile. |
| [dbgeng.IDebugClient5.AddProcessOptions](nf-dbgeng-idebugclient5-addprocessoptions.md) | The AddProcessOptions method adds the process options to those options that affect the current process. |
| [dbgeng.IDebugClient5.AttachKernel](nf-dbgeng-idebugclient5-attachkernel.md) | The AttachKernel methods connect the debugger engine to a kernel target. |
| [dbgeng.IDebugClient5.AttachKernelWide](nf-dbgeng-idebugclient5-attachkernelwide.md) | The AttachKernelWide method connects the debugger engine to a kernel target. |
| [dbgeng.IDebugClient5.AttachProcess](nf-dbgeng-idebugclient5-attachprocess.md) | The AttachProcess method connects the debugger engine to a user-modeprocess. |
| [dbgeng.IDebugClient5.ConnectProcessServer](nf-dbgeng-idebugclient5-connectprocessserver.md) | The ConnectProcessServer methods connect to a process server. |
| [dbgeng.IDebugClient5.ConnectProcessServerWide](nf-dbgeng-idebugclient5-connectprocessserverwide.md) | The ConnectProcessServerWide method connects to a process server. |
| [dbgeng.IDebugClient5.ConnectSession](nf-dbgeng-idebugclient5-connectsession.md) | The ConnectSession method joins the client to an existing debugger session. |
| [dbgeng.IDebugClient5.CreateClient](nf-dbgeng-idebugclient5-createclient.md) | The CreateClient method creates a new client object for the current thread. |
| [dbgeng.IDebugClient5.CreateProcess](nf-dbgeng-idebugclient5-createprocess.md) | The CreateProcess method creates a process from the specified command line. |
| [dbgeng.IDebugClient5.CreateProcess2](nf-dbgeng-idebugclient5-createprocess2.md) | The CreateProcess2 method executes the given command to create a new process. |
| [dbgeng.IDebugClient5.CreateProcess2Wide](nf-dbgeng-idebugclient5-createprocess2wide.md) | The CreateProcess2Wide method executes the specified command to create a new process. |
| [dbgeng.IDebugClient5.CreateProcessAndAttach](nf-dbgeng-idebugclient5-createprocessandattach.md) | The CreateProcessAndAttach method creates a process from a specified command line, then attach to another user-mode process. |
| [dbgeng.IDebugClient5.CreateProcessAndAttach2](nf-dbgeng-idebugclient5-createprocessandattach2.md) | The CreateProcessAndAttach2 method creates a process from a specified command line, then attaches to that process or another user-mode process. |
| [dbgeng.IDebugClient5.CreateProcessAndAttach2Wide](nf-dbgeng-idebugclient5-createprocessandattach2wide.md) | The CreateProcessAndAttach2Wide method creates a process from a specified command line, then attach to that process or another user-mode process. |
| [dbgeng.IDebugClient5.CreateProcessAndAttachWide](nf-dbgeng-idebugclient5-createprocessandattachwide.md) | The CreateProcessAndAttachWide method creates a process from a specified command line, then attach to another user-mode process. |
| [dbgeng.IDebugClient5.CreateProcessWide](nf-dbgeng-idebugclient5-createprocesswide.md) | The CreateProcessWide method creates a process from the specified command line. |
| [dbgeng.IDebugClient5.DetachCurrentProcess](nf-dbgeng-idebugclient5-detachcurrentprocess.md) | The DetachCurrentProcess method detaches the debugger engine from the current process, resuming all its threads. |
| [dbgeng.IDebugClient5.DetachProcesses](nf-dbgeng-idebugclient5-detachprocesses.md) | The DetachProcesses method detaches the debugger engine from all processes in all targets, resuming all their threads. |
| [dbgeng.IDebugClient5.DisconnectProcessServer](nf-dbgeng-idebugclient5-disconnectprocessserver.md) | The DisconnectProcessServer method disconnects the debugger engine from a process server. |
| [dbgeng.IDebugClient5.DispatchCallbacks](nf-dbgeng-idebugclient5-dispatchcallbacks.md) | The DispatchCallbacks method lets the debugger engine use the current thread for callbacks. |
| [dbgeng.IDebugClient5.EndProcessServer](nf-dbgeng-idebugclient5-endprocessserver.md) | The EndProcessServer method requests that a process server be shut down. |
| [dbgeng.IDebugClient5.EndSession](nf-dbgeng-idebugclient5-endsession.md) | The EndSession method ends the current debugger session. |
| [dbgeng.IDebugClient5.ExitDispatch](nf-dbgeng-idebugclient5-exitdispatch.md) | The ExitDispatch method causes the DispatchCallbacks method to return. |
| [dbgeng.IDebugClient5.FlushCallbacks](nf-dbgeng-idebugclient5-flushcallbacks.md) | The FlushCallbacks method forces any remaining buffered output to be delivered to the IDebugOutputCallbacks object registered with this client. |
| [dbgeng.IDebugClient5.GetDumpFile](nf-dbgeng-idebugclient5-getdumpfile.md) | The GetDumpFile method describes the files containing supporting information that were used when opening the current dump target. |
| [dbgeng.IDebugClient5.GetDumpFileWide](nf-dbgeng-idebugclient5-getdumpfilewide.md) | The GetDumpFileWide method describes the files containing supporting information that were used when opening the current dump target. |
| [dbgeng.IDebugClient5.GetEventCallbacks](nf-dbgeng-idebugclient5-geteventcallbacks.md) | The GetEventCallbacks method returns the event callbacks object registered with this client. |
| [dbgeng.IDebugClient5.GetEventCallbacksWide](nf-dbgeng-idebugclient5-geteventcallbackswide.md) | The GetEventCallbacksWide method returns the event callbacks object registered with this client. |
| [dbgeng.IDebugClient5.GetExitCode](nf-dbgeng-idebugclient5-getexitcode.md) | The GetExitCode method returns the exit code of the current process if that process has already run through to completion. |
| [dbgeng.IDebugClient5.GetIdentity](nf-dbgeng-idebugclient5-getidentity.md) | The GetIdentity method returns a string describing the computer and user this client represents. |
| [dbgeng.IDebugClient5.GetIdentityWide](nf-dbgeng-idebugclient5-getidentitywide.md) | The GetIdentityWide method returns a string describing the computer and user this client represents. |
| [dbgeng.IDebugClient5.GetInputCallbacks](nf-dbgeng-idebugclient5-getinputcallbacks.md) | The GetInputCallbacks method returns the input callbacks object registered with this client. |
| [dbgeng.IDebugClient5.GetKernelConnectionOptions](nf-dbgeng-idebugclient5-getkernelconnectionoptions.md) | The GetKernelConnectionOptions method returns the connection options for the current kernel target. |
| [dbgeng.IDebugClient5.GetKernelConnectionOptionsWide](nf-dbgeng-idebugclient5-getkernelconnectionoptionswide.md) | The GetKernelConnectionOptionsWide method returns the connection options for the current kernel target. |
| [dbgeng.IDebugClient5.GetNumberDumpFiles](nf-dbgeng-idebugclient5-getnumberdumpfiles.md) | The GetNumberDumpFiles method returns the number of files containing supporting information that were used when opening the current dump target. |
| [dbgeng.IDebugClient5.GetNumberEventCallbacks](nf-dbgeng-idebugclient5-getnumbereventcallbacks.md) | The GetNumberEventCallbacks method returns the number of event callbacks that are interested in the given events. |
| [dbgeng.IDebugClient5.GetNumberInputCallbacks](nf-dbgeng-idebugclient5-getnumberinputcallbacks.md) | The GetNumberInputCallbacks method returns the number of input callbacks registered over all clients. |
| [dbgeng.IDebugClient5.GetNumberOutputCallbacks](nf-dbgeng-idebugclient5-getnumberoutputcallbacks.md) | The GetNumberOutputCallbacks method returns the number of output callbacks registered over all clients. |
| [dbgeng.IDebugClient5.GetOtherOutputMask](nf-dbgeng-idebugclient5-getotheroutputmask.md) | The GetOtherOutputMask method returns the output mask for another client. |
| [dbgeng.IDebugClient5.GetOutputCallbacks](nf-dbgeng-idebugclient5-getoutputcallbacks.md) | The GetOutputCallbacks method returns the output callbacks object registered with the client. |
| [dbgeng.IDebugClient5.GetOutputCallbacksWide](nf-dbgeng-idebugclient5-getoutputcallbackswide.md) | The GetOutputCallbacksWide method returns the output callbacks object registered with the client. |
| [dbgeng.IDebugClient5.GetOutputLinePrefixWide](nf-dbgeng-idebugclient5-getoutputlineprefixwide.md) | Gets a Unicode character string prefix for output lines. |
| [dbgeng.IDebugClient5.GetOutputMask](nf-dbgeng-idebugclient5-getoutputmask.md) | The GetOutputMask method returns the output mask currently set for the client. |
| [dbgeng.IDebugClient5.GetProcessOptions](nf-dbgeng-idebugclient5-getprocessoptions.md) | The GetProcessOptions method retrieves the process options affecting the current process. |
| [dbgeng.IDebugClient5.GetQuitLockString](nf-dbgeng-idebugclient5-getquitlockstring.md) | Gets a quit lock string. |
| [dbgeng.IDebugClient5.GetQuitLockStringWide](nf-dbgeng-idebugclient5-getquitlockstringwide.md) | Gets a Unicode character quit lock string. |
| [dbgeng.IDebugClient5.GetRunningProcessDescription](nf-dbgeng-idebugclient5-getrunningprocessdescription.md) | The GetRunningProcessDescription method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [dbgeng.IDebugClient5.GetRunningProcessDescriptionWide](nf-dbgeng-idebugclient5-getrunningprocessdescriptionwide.md) | The GetRunningProcessDescriptionWide method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [dbgeng.IDebugClient5.GetRunningProcessSystemIdByExecutableName](nf-dbgeng-idebugclient5-getrunningprocesssystemidbyexecutablename.md) | The GetRunningProcessSystemIdByExecutableName method searches for a process with a given executable file name and return its process ID. |
| [dbgeng.IDebugClient5.GetRunningProcessSystemIdByExecutableNameWide](nf-dbgeng-idebugclient5-getrunningprocesssystemidbyexecutablenamewide.md) | The GetRunningProcessSystemIdByExecutableNameWide method searches for a process with a given executable file name and return its process ID. |
| [dbgeng.IDebugClient5.GetRunningProcessSystemIds](nf-dbgeng-idebugclient5-getrunningprocesssystemids.md) | The GetRunningProcessSystemIds method returns the process IDs for each running process. |
| [dbgeng.IDebugClient5.IsKernelDebuggerEnabled](nf-dbgeng-idebugclient5-iskerneldebuggerenabled.md) | The IsKernelDebuggerEnabled method checks whether kernel debugging is enabled for the local kernel. |
| [dbgeng.IDebugClient5.OpenDumpFile](nf-dbgeng-idebugclient5-opendumpfile.md) | The OpenDumpFile method opens a dump file as a debugger target. |
| [dbgeng.IDebugClient5.OpenDumpFileWide](nf-dbgeng-idebugclient5-opendumpfilewide.md) | The OpenDumpFileWide method opens a dump file as a debugger target. |
| [dbgeng.IDebugClient5.OutputIdentity](nf-dbgeng-idebugclient5-outputidentity.md) | The OutputIdentity method formats and outputs a string describing the computer and user this client represents. |
| [dbgeng.IDebugClient5.OutputIdentityWide](nf-dbgeng-idebugclient5-outputidentitywide.md) | The OutputIdentityWide method formats and outputs a string describing the computer and user this client represents. |
| [dbgeng.IDebugClient5.OutputServers](nf-dbgeng-idebugclient5-outputservers.md) | The OutputServers method lists the servers running on a given computer. |
| [dbgeng.IDebugClient5.OutputServersWide](nf-dbgeng-idebugclient5-outputserverswide.md) | The OutputServersWide method lists the servers running on a given computer. |
| [dbgeng.IDebugClient5.PopOutputLinePrefix](nf-dbgeng-idebugclient5-popoutputlineprefix.md) | Restores a previously saved output line prefix. |
| [dbgeng.IDebugClient5.PushOutputLinePrefix](nf-dbgeng-idebugclient5-pushoutputlineprefix.md) | Saves an output line prefix. |
| [dbgeng.IDebugClient5.PushOutputLinePrefixWide](nf-dbgeng-idebugclient5-pushoutputlineprefixwide.md) | Saves a wide string output line prefix. |
| [dbgeng.IDebugClient5.RemoveProcessOptions](nf-dbgeng-idebugclient5-removeprocessoptions.md) | The RemoveProcessOptions method removes process options from those options that affect the current process. |
| [dbgeng.IDebugClient5.SetEventCallbacks](nf-dbgeng-idebugclient5-seteventcallbacks.md) | The SetEventCallbacks method registers an event callbacks object with this client. |
| [dbgeng.IDebugClient5.SetEventCallbacksWide](nf-dbgeng-idebugclient5-seteventcallbackswide.md) | The SetEventCallbacksWide method registers an event callbacks object with this client. |
| [dbgeng.IDebugClient5.SetInputCallbacks](nf-dbgeng-idebugclient5-setinputcallbacks.md) | The SetInputCallbacks method registers an input callbacks object with the client. |
| [dbgeng.IDebugClient5.SetKernelConnectionOptions](nf-dbgeng-idebugclient5-setkernelconnectionoptions.md) | The SetKernelConnectionOptions method updates some of the connection options for a live kernel target. |
| [dbgeng.IDebugClient5.SetKernelConnectionOptionsWide](nf-dbgeng-idebugclient5-setkernelconnectionoptionswide.md) | The SetKernelConnectionOptionsWide method updates some of the connection options for a live kernel target. |
| [dbgeng.IDebugClient5.SetOtherOutputMask](nf-dbgeng-idebugclient5-setotheroutputmask.md) | The SetOtherOutputMask method sets the output mask for another client. |
| [dbgeng.IDebugClient5.SetOutputCallbacks](nf-dbgeng-idebugclient5-setoutputcallbacks.md) | The SetOutputCallbacks method registers an output callbacks object with this client. |
| [dbgeng.IDebugClient5.SetOutputCallbacksWide](nf-dbgeng-idebugclient5-setoutputcallbackswide.md) | The SetOutputCallbacksWide method registers an output callbacks object with this client. |
| [dbgeng.IDebugClient5.SetOutputLinePrefixWide](nf-dbgeng-idebugclient5-setoutputlineprefixwide.md) | Sets a wide string prefix for output lines. |
| [dbgeng.IDebugClient5.SetOutputMask](nf-dbgeng-idebugclient5-setoutputmask.md) | The SetOutputMask method sets the output mask for the client. |
| [dbgeng.IDebugClient5.SetProcessOptions](nf-dbgeng-idebugclient5-setprocessoptions.md) | The SetProcessOptions method sets the process options affecting the current process. |
| [dbgeng.IDebugClient5.SetQuitLockString](nf-dbgeng-idebugclient5-setquitlockstring.md) | Sets a quit lock string. |
| [dbgeng.IDebugClient5.SetQuitLockStringWide](nf-dbgeng-idebugclient5-setquitlockstringwide.md) | Sets a quit lock Unicode character string. |
| [dbgeng.IDebugClient5.StartProcessServer](nf-dbgeng-idebugclient5-startprocessserver.md) | The StartProcessServer method starts a process server. |
| [dbgeng.IDebugClient5.StartProcessServerWide](nf-dbgeng-idebugclient5-startprocessserverwide.md) | The StartProcessServerWide method starts a process server. |
| [dbgeng.IDebugClient5.StartServer](nf-dbgeng-idebugclient5-startserver.md) | The StartServer method starts a debugging server. |
| [dbgeng.IDebugClient5.StartServerWide](nf-dbgeng-idebugclient5-startserverwide.md) | The StartServerWide method starts a debugging server. |
| [dbgeng.IDebugClient5.TerminateCurrentProcess](nf-dbgeng-idebugclient5-terminatecurrentprocess.md) | The TerminateCurrentProcess method attempts to terminate the current process. |
| [dbgeng.IDebugClient5.TerminateProcesses](nf-dbgeng-idebugclient5-terminateprocesses.md) | The TerminateProcesses method attempts to terminate all processes in all targets. |
| [dbgeng.IDebugClient5.WaitForProcessServerEnd](nf-dbgeng-idebugclient5-waitforprocessserverend.md) | The WaitForProcessServerEnd method waits for a local process server to exit. |
| [dbgeng.IDebugClient5.WriteDumpFile](nf-dbgeng-idebugclient5-writedumpfile.md) | The WriteDumpFile method creates a user-mode or kernel-modecrash dump file. |
| [dbgeng.IDebugClient5.WriteDumpFile2](nf-dbgeng-idebugclient5-writedumpfile2.md) | The WriteDumpFile2 method creates a user-mode or kernel-modecrash dump file. |
| [dbgeng.IDebugClient5.WriteDumpFileWide](nf-dbgeng-idebugclient5-writedumpfilewide.md) | The WriteDumpFileWide method creates a user-mode or kernel-modecrash dump file. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **DLL** |  |

    ## See Also

        <dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient5 interface%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>