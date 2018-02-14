---
UID: NN:dbgeng.IDebugSystemObjects4
title: IDebugSystemObjects4
author: windows-driver-content
description: IDebugSystemObjects4 interface
old-location: debugger\idebugsystemobjects4.htm
old-project: debugger
ms.assetid: 075143eb-03c4-41b2-b419-4618ed103843
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugsystemobjects4, IDebugSystemObjects4 interface [Windows Debugging], IDebugSystemObjects4 interface [Windows Debugging], described, IDebugSystemObjects4, dbgeng/IDebugSystemObjects4
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
-	IDebugSystemObjects4
-	IDebugSystemObjects4.GetCurrentSystemServerNameWide
product: Windows
targetos: Windows
req.typenames: "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---

# IDebugSystemObjects4 interface



## Methods

<p>The <b>IDebugSystemObjects4</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugSystemObjects4.GetCurrentProcessDataOffset](nf-dbgeng-idebugsystemobjects4-getcurrentprocessdataoffset.md) | The GetCurrentProcessDataOffset method returns the location of the system data structure describing the current process. |
| [dbgeng.IDebugSystemObjects4.GetCurrentProcessExecutableName](nf-dbgeng-idebugsystemobjects4-getcurrentprocessexecutablename.md) | The GetCurrentProcessExecutableName method returns the name of executable file loaded in the current process. |
| [dbgeng.IDebugSystemObjects4.GetCurrentProcessExecutableNameWide](nf-dbgeng-idebugsystemobjects4-getcurrentprocessexecutablenamewide.md) | The GetCurrentProcessExecutableNameWide method returns the name of executable file loaded in the current process. |
| [dbgeng.IDebugSystemObjects4.GetCurrentProcessHandle](nf-dbgeng-idebugsystemobjects4-getcurrentprocesshandle.md) | The GetCurrentProcessHandle method returns the system handle for the current process. |
| [dbgeng.IDebugSystemObjects4.GetCurrentProcessId](nf-dbgeng-idebugsystemobjects4-getcurrentprocessid.md) | The GetCurrentProcessId method returns the engine process ID for the current process. |
| [dbgeng.IDebugSystemObjects4.GetCurrentProcessPeb](nf-dbgeng-idebugsystemobjects4-getcurrentprocesspeb.md) | The GetCurrentProcessPeb method returns the process environment block (PEB) of the current process. |
| [dbgeng.IDebugSystemObjects4.GetCurrentProcessSystemId](nf-dbgeng-idebugsystemobjects4-getcurrentprocesssystemid.md) | The GetCurrentProcessSystemId method returns the system process ID of the current process. |
| [dbgeng.IDebugSystemObjects4.GetCurrentProcessUpTime](nf-dbgeng-idebugsystemobjects4-getcurrentprocessuptime.md) | The GetCurrentProcessUpTime method returns the length of time the current process has been running. |
| [dbgeng.IDebugSystemObjects4.GetCurrentSystemId](nf-dbgeng-idebugsystemobjects4-getcurrentsystemid.md) | The GetCurrentSystemId method returns the engine target ID for the current process. |
| [dbgeng.IDebugSystemObjects4.GetCurrentSystemServerNameWide](nf-dbgeng-idebugsystemobjects4-getcurrentsystemservernamewide.md) | Gets the server name for the current process. |
| [dbgeng.IDebugSystemObjects4.GetCurrentThreadDataOffset](nf-dbgeng-idebugsystemobjects4-getcurrentthreaddataoffset.md) | The GetCurrentThreadDataOffset method returns the location of the system data structure for the current thread. |
| [dbgeng.IDebugSystemObjects4.GetCurrentThreadHandle](nf-dbgeng-idebugsystemobjects4-getcurrentthreadhandle.md) | The GetCurrentThreadHandle method returns the system handle for the current thread. |
| [dbgeng.IDebugSystemObjects4.GetCurrentThreadId](nf-dbgeng-idebugsystemobjects4-getcurrentthreadid.md) | The GetCurrentThreadId method returns the engine thread ID for the current thread. |
| [dbgeng.IDebugSystemObjects4.GetCurrentThreadSystemId](nf-dbgeng-idebugsystemobjects4-getcurrentthreadsystemid.md) | The GetCurrentThreadSystemId method returns the system thread ID of the current thread. |
| [dbgeng.IDebugSystemObjects4.GetCurrentThreadTeb](nf-dbgeng-idebugsystemobjects4-getcurrentthreadteb.md) | The GetCurrentThreadTeb method returns the location of the thread environment block (TEB) for the current thread. |
| [dbgeng.IDebugSystemObjects4.GetEventProcess](nf-dbgeng-idebugsystemobjects4-geteventprocess.md) | The GetEventProcess method returns the engine process ID for the process on which the last event occurred. |
| [dbgeng.IDebugSystemObjects4.GetEventSystem](nf-dbgeng-idebugsystemobjects4-geteventsystem.md) | The GetEventSystem method returns the engine target ID for the target in which the last event occurred. |
| [dbgeng.IDebugSystemObjects4.GetEventThread](nf-dbgeng-idebugsystemobjects4-geteventthread.md) | The GetEventThread method returns the engine thread ID for the thread on which the last event occurred. |
| [dbgeng.IDebugSystemObjects4.GetImplicitProcessDataOffset](nf-dbgeng-idebugsystemobjects4-getimplicitprocessdataoffset.md) | The GetImplicitProcessDataOffset method returns the implicit process for the current target. |
| [dbgeng.IDebugSystemObjects4.GetImplicitThreadDataOffset](nf-dbgeng-idebugsystemobjects4-getimplicitthreaddataoffset.md) | The GetImplicitThreadDataOffset method returns the implicit thread for the current process. |
| [dbgeng.IDebugSystemObjects4.GetNumberProcesses](nf-dbgeng-idebugsystemobjects4-getnumberprocesses.md) | The GetNumberProcesses method returns the number of processes for the current target. |
| [dbgeng.IDebugSystemObjects4.GetNumberSystems](nf-dbgeng-idebugsystemobjects4-getnumbersystems.md) | The GetNumberSystems method returns the number of targets to which the engine is currently connected. |
| [dbgeng.IDebugSystemObjects4.GetNumberThreads](nf-dbgeng-idebugsystemobjects4-getnumberthreads.md) | The GetNumberThreads method returns the number of threads in the current process. |
| [dbgeng.IDebugSystemObjects4.GetProcessIdByDataOffset](nf-dbgeng-idebugsystemobjects4-getprocessidbydataoffset.md) | The GetProcessIdByDataOffset method returns the engine process ID for the specified process. The process is specified by its data offset. |
| [dbgeng.IDebugSystemObjects4.GetProcessIdByHandle](nf-dbgeng-idebugsystemobjects4-getprocessidbyhandle.md) | The GetProcessIdByHandle method returns the engine process ID for the specified process. The process is specified by its system handle. |
| [dbgeng.IDebugSystemObjects4.GetProcessIdByPeb](nf-dbgeng-idebugsystemobjects4-getprocessidbypeb.md) | The GetProcessIdByPeb method returns the engine process ID for the specified process. The process is specified by its process environment block (PEB). |
| [dbgeng.IDebugSystemObjects4.GetProcessIdBySystemId](nf-dbgeng-idebugsystemobjects4-getprocessidbysystemid.md) | The GetProcessIdBySystemId method returns the engine process ID for a process specified by its system process ID. |
| [dbgeng.IDebugSystemObjects4.GetProcessIdsByIndex](nf-dbgeng-idebugsystemobjects4-getprocessidsbyindex.md) | The GetProcessIdsByIndex method returns the engine process ID and system process ID for the specified processes in the current target. |
| [dbgeng.IDebugSystemObjects4.GetSystemIdsByIndex](nf-dbgeng-idebugsystemobjects4-getsystemidsbyindex.md) | The GetSystemIdsByIndex method returns the engine target IDs for the specified targets. |
| [dbgeng.IDebugSystemObjects4.GetThreadIdByDataOffset](nf-dbgeng-idebugsystemobjects4-getthreadidbydataoffset.md) | The GetThreadIdByDataOffset method returns the engine thread ID for the specified thread. The thread is specified by its system data structure. |
| [dbgeng.IDebugSystemObjects4.GetThreadIdByHandle](nf-dbgeng-idebugsystemobjects4-getthreadidbyhandle.md) | The GetThreadIdByHandle method returns the engine thread ID for the specified thread. The thread is specified by its system handle. |
| [dbgeng.IDebugSystemObjects4.GetThreadIdByProcessor](nf-dbgeng-idebugsystemobjects4-getthreadidbyprocessor.md) | The GetThreadIdByProcessor method returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor. |
| [dbgeng.IDebugSystemObjects4.GetThreadIdBySystemId](nf-dbgeng-idebugsystemobjects4-getthreadidbysystemid.md) | The GetThreadIdBySystemId method returns the engine thread ID for the specified thread. The thread is specified by its system thread ID. |
| [dbgeng.IDebugSystemObjects4.GetThreadIdByTeb](nf-dbgeng-idebugsystemobjects4-getthreadidbyteb.md) | The GetThreadIdByTeb method returns the engine thread ID of the specified thread. The thread is specified by its thread environment block (TEB). |
| [dbgeng.IDebugSystemObjects4.GetThreadIdsByIndex](nf-dbgeng-idebugsystemobjects4-getthreadidsbyindex.md) | The GetThreadIdsByIndex method returns the engine and system thread IDs for the specified threads in the current process. |
| [dbgeng.IDebugSystemObjects4.GetTotalNumberThreads](nf-dbgeng-idebugsystemobjects4-gettotalnumberthreads.md) | The GetTotalNumberThreads method returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target. |
| [dbgeng.IDebugSystemObjects4.GetTotalNumberThreadsAndProcesses](nf-dbgeng-idebugsystemobjects4-gettotalnumberthreadsandprocesses.md) | The GetTotalNumberThreadsAndProcesses method returns the total number of threads and processes in all the targets the engine is attached to, in addition to the largest number of threads and processes in a target. |
| [dbgeng.IDebugSystemObjects4.SetCurrentProcessId](nf-dbgeng-idebugsystemobjects4-setcurrentprocessid.md) | The SetCurrentProcessId method makes the specified process the current process. |
| [dbgeng.IDebugSystemObjects4.SetCurrentSystemId](nf-dbgeng-idebugsystemobjects4-setcurrentsystemid.md) | The SetCurrentSystemId method makes the specified target the current target. |
| [dbgeng.IDebugSystemObjects4.SetCurrentThreadId](nf-dbgeng-idebugsystemobjects4-setcurrentthreadid.md) | The SetCurrentThreadId method makes the specified thread the current thread. |
| [dbgeng.IDebugSystemObjects4.SetImplicitProcessDataOffset](nf-dbgeng-idebugsystemobjects4-setimplicitprocessdataoffset.md) | The SetImplicitProcessDataOffset method sets the implicit process for the current target. |
| [dbgeng.IDebugSystemObjects4.SetImplicitThreadDataOffset](nf-dbgeng-idebugsystemobjects4-setimplicitthreaddataoffset.md) | The SetImplicitThreadDataOffset method sets the implicit thread for the current process. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects.md">IDebugSystemObjects</a>



<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects3.md">IDebugSystemObjects3</a>



<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects2.md">IDebugSystemObjects2</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSystemObjects4 interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>