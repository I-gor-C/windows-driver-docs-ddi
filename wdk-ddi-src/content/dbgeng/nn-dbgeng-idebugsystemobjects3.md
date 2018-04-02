---
UID: NN:dbgeng.IDebugSystemObjects3
title: IDebugSystemObjects3
author: windows-driver-content
description: IDebugSystemObjects3 interface
old-location: debugger\idebugsystemobjects3.htm
old-project: debugger
ms.assetid: 8924c46b-e2b5-473f-aa0c-e755cd9cbbc6
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugSystemObjects3, IDebugSystemObjects3 interface [Windows Debugging], IDebugSystemObjects3 interface [Windows Debugging], described, dbgeng/IDebugSystemObjects3, debugger.idebugsystemobjects3
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
-	IDebugSystemObjects3
-	IDebugSystemObjects3.GetCurrentSystemServer
-	IDebugSystemObjects3.GetSystemByServer
-	IDebugSystemObjects3.GetCurrentSystemServerName
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugSystemObjects3 interface



## Methods

<p>The <b>IDebugSystemObjects3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugSystemObjects3::GetCurrentProcessDataOffset](nf-dbgeng-idebugsystemobjects3-getcurrentprocessdataoffset.md) | The GetCurrentProcessDataOffset method returns the location of the system data structure describing the current process. |
| [IDebugSystemObjects3::GetCurrentProcessExecutableName](nf-dbgeng-idebugsystemobjects3-getcurrentprocessexecutablename.md) | The GetCurrentProcessExecutableName method returns the name of executable file loaded in the current process. |
| [IDebugSystemObjects3::GetCurrentProcessHandle](nf-dbgeng-idebugsystemobjects3-getcurrentprocesshandle.md) | The GetCurrentProcessHandle method returns the system handle for the current process. |
| [IDebugSystemObjects3::GetCurrentProcessId](nf-dbgeng-idebugsystemobjects3-getcurrentprocessid.md) | The GetCurrentProcessId method returns the engine process ID for the current process. |
| [IDebugSystemObjects3::GetCurrentProcessPeb](nf-dbgeng-idebugsystemobjects3-getcurrentprocesspeb.md) | The GetCurrentProcessPeb method returns the process environment block (PEB) of the current process. |
| [IDebugSystemObjects3::GetCurrentProcessSystemId](nf-dbgeng-idebugsystemobjects3-getcurrentprocesssystemid.md) | The GetCurrentProcessSystemId method returns the system process ID of the current process. |
| [IDebugSystemObjects3::GetCurrentProcessUpTime](nf-dbgeng-idebugsystemobjects3-getcurrentprocessuptime.md) | The GetCurrentProcessUpTime method returns the length of time the current process has been running. |
| [IDebugSystemObjects3::GetCurrentSystemId](nf-dbgeng-idebugsystemobjects3-getcurrentsystemid.md) | The GetCurrentSystemId method returns the engine target ID for the current process. |
| [IDebugSystemObjects3::GetCurrentSystemServer](nf-dbgeng-idebugsystemobjects3-getcurrentsystemserver.md) | Gets the server for the current process. |
| [IDebugSystemObjects3::GetCurrentSystemServerName](nf-dbgeng-idebugsystemobjects3-getcurrentsystemservername.md) | Gets the server name for the current process. |
| [IDebugSystemObjects3::GetCurrentThreadDataOffset](nf-dbgeng-idebugsystemobjects3-getcurrentthreaddataoffset.md) | The GetCurrentThreadDataOffset method returns the location of the system data structure for the current thread. |
| [IDebugSystemObjects3::GetCurrentThreadHandle](nf-dbgeng-idebugsystemobjects3-getcurrentthreadhandle.md) | The GetCurrentThreadHandle method returns the system handle for the current thread. |
| [IDebugSystemObjects3::GetCurrentThreadId](nf-dbgeng-idebugsystemobjects3-getcurrentthreadid.md) | The GetCurrentThreadId method returns the engine thread ID for the current thread. |
| [IDebugSystemObjects3::GetCurrentThreadSystemId](nf-dbgeng-idebugsystemobjects3-getcurrentthreadsystemid.md) | The GetCurrentThreadSystemId method returns the system thread ID of the current thread. |
| [IDebugSystemObjects3::GetCurrentThreadTeb](nf-dbgeng-idebugsystemobjects3-getcurrentthreadteb.md) | The GetCurrentThreadTeb method returns the location of the thread environment block (TEB) for the current thread. |
| [IDebugSystemObjects3::GetEventProcess](nf-dbgeng-idebugsystemobjects3-geteventprocess.md) | The GetEventProcess method returns the engine process ID for the process on which the last event occurred. |
| [IDebugSystemObjects3::GetEventSystem](nf-dbgeng-idebugsystemobjects3-geteventsystem.md) | The GetEventSystem method returns the engine target ID for the target in which the last event occurred. |
| [IDebugSystemObjects3::GetEventThread](nf-dbgeng-idebugsystemobjects3-geteventthread.md) | The GetEventThread method returns the engine thread ID for the thread on which the last event occurred. |
| [IDebugSystemObjects3::GetImplicitProcessDataOffset](nf-dbgeng-idebugsystemobjects3-getimplicitprocessdataoffset.md) | The GetImplicitProcessDataOffset method returns the implicit process for the current target. |
| [IDebugSystemObjects3::GetImplicitThreadDataOffset](nf-dbgeng-idebugsystemobjects3-getimplicitthreaddataoffset.md) | The GetImplicitThreadDataOffset method returns the implicit thread for the current process. |
| [IDebugSystemObjects3::GetNumberProcesses](nf-dbgeng-idebugsystemobjects3-getnumberprocesses.md) | The GetNumberProcesses method returns the number of processes for the current target. |
| [IDebugSystemObjects3::GetNumberSystems](nf-dbgeng-idebugsystemobjects3-getnumbersystems.md) | The GetNumberSystems method returns the number of targets to which the engine is currently connected. |
| [IDebugSystemObjects3::GetNumberThreads](nf-dbgeng-idebugsystemobjects3-getnumberthreads.md) | The GetNumberThreads method returns the number of threads in the current process. |
| [IDebugSystemObjects3::GetProcessIdByDataOffset](nf-dbgeng-idebugsystemobjects3-getprocessidbydataoffset.md) | The GetProcessIdByDataOffset method returns the engine process ID for the specified process. The process is specified by its data offset. |
| [IDebugSystemObjects3::GetProcessIdByHandle](nf-dbgeng-idebugsystemobjects3-getprocessidbyhandle.md) | The GetProcessIdByHandle method returns the engine process ID for the specified process. The process is specified by its system handle. |
| [IDebugSystemObjects3::GetProcessIdByPeb](nf-dbgeng-idebugsystemobjects3-getprocessidbypeb.md) | The GetProcessIdByPeb method returns the engine process ID for the specified process. The process is specified by its process environment block (PEB). |
| [IDebugSystemObjects3::GetProcessIdBySystemId](nf-dbgeng-idebugsystemobjects3-getprocessidbysystemid.md) | The GetProcessIdBySystemId method returns the engine process ID for a process specified by its system process ID. |
| [IDebugSystemObjects3::GetProcessIdsByIndex](nf-dbgeng-idebugsystemobjects3-getprocessidsbyindex.md) | The GetProcessIdsByIndex method returns the engine process ID and system process ID for the specified processes in the current target. |
| [IDebugSystemObjects3::GetSystemByServer](nf-dbgeng-idebugsystemobjects3-getsystembyserver.md) | Gets the system for a server. |
| [IDebugSystemObjects3::GetSystemIdsByIndex](nf-dbgeng-idebugsystemobjects3-getsystemidsbyindex.md) | The GetSystemIdsByIndex method returns the engine target IDs for the specified targets. |
| [IDebugSystemObjects3::GetThreadIdByDataOffset](nf-dbgeng-idebugsystemobjects3-getthreadidbydataoffset.md) | The GetThreadIdByDataOffset method returns the engine thread ID for the specified thread. The thread is specified by its system data structure. |
| [IDebugSystemObjects3::GetThreadIdByHandle](nf-dbgeng-idebugsystemobjects3-getthreadidbyhandle.md) | The GetThreadIdByHandle method returns the engine thread ID for the specified thread. The thread is specified by its system handle. |
| [IDebugSystemObjects3::GetThreadIdByProcessor](nf-dbgeng-idebugsystemobjects3-getthreadidbyprocessor.md) | The GetThreadIdByProcessor method returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor. |
| [IDebugSystemObjects3::GetThreadIdBySystemId](nf-dbgeng-idebugsystemobjects3-getthreadidbysystemid.md) | The GetThreadIdBySystemId method returns the engine thread ID for the specified thread. The thread is specified by its system thread ID. |
| [IDebugSystemObjects3::GetThreadIdByTeb](nf-dbgeng-idebugsystemobjects3-getthreadidbyteb.md) | The GetThreadIdByTeb method returns the engine thread ID of the specified thread. The thread is specified by its thread environment block (TEB). |
| [IDebugSystemObjects3::GetThreadIdsByIndex](nf-dbgeng-idebugsystemobjects3-getthreadidsbyindex.md) | The GetThreadIdsByIndex method returns the engine and system thread IDs for the specified threads in the current process. |
| [IDebugSystemObjects3::GetTotalNumberThreads](nf-dbgeng-idebugsystemobjects3-gettotalnumberthreads.md) | The GetTotalNumberThreads method returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target. |
| [IDebugSystemObjects3::GetTotalNumberThreadsAndProcesses](nf-dbgeng-idebugsystemobjects3-gettotalnumberthreadsandprocesses.md) | The GetTotalNumberThreadsAndProcesses method returns the total number of threads and processes in all the targets the engine is attached to, in addition to the largest number of threads and processes in a target. |
| [IDebugSystemObjects3::SetCurrentProcessId](nf-dbgeng-idebugsystemobjects3-setcurrentprocessid.md) | The SetCurrentProcessId method makes the specified process the current process. |
| [IDebugSystemObjects3::SetCurrentSystemId](nf-dbgeng-idebugsystemobjects3-setcurrentsystemid.md) | The SetCurrentSystemId method makes the specified target the current target. |
| [IDebugSystemObjects3::SetCurrentThreadId](nf-dbgeng-idebugsystemobjects3-setcurrentthreadid.md) | The SetCurrentThreadId method makes the specified thread the current thread. |
| [IDebugSystemObjects3::SetImplicitProcessDataOffset](nf-dbgeng-idebugsystemobjects3-setimplicitprocessdataoffset.md) | The SetImplicitProcessDataOffset method sets the implicit process for the current target. |
| [IDebugSystemObjects3::SetImplicitThreadDataOffset](nf-dbgeng-idebugsystemobjects3-setimplicitthreaddataoffset.md) | The SetImplicitThreadDataOffset method sets the implicit thread for the current process. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550875">IDebugSystemObjects</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550885">IDebugSystemObjects2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550893">IDebugSystemObjects4</a>