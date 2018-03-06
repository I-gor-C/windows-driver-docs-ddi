---
UID: NN:dbgeng.IDebugSystemObjects2
title: IDebugSystemObjects2
author: windows-driver-content
description: IDebugSystemObjects2 interface
old-location: debugger\idebugsystemobjects2.htm
old-project: debugger
ms.assetid: 9e354357-590b-45cf-bace-5b431f408422
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IDebugSystemObjects2, IDebugSystemObjects2 interface [Windows Debugging], IDebugSystemObjects2 interface [Windows Debugging], described, dbgeng/IDebugSystemObjects2, debugger.idebugsystemobjects2
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	dbgeng.h
api_name:
-	IDebugSystemObjects2
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugSystemObjects2 interface



## Methods

<p>The <b>IDebugSystemObjects2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugSystemObjects2::GetCurrentProcessDataOffset](nf-dbgeng-idebugsystemobjects2-getcurrentprocessdataoffset.md) | The GetCurrentProcessDataOffset method returns the location of the system data structure describing the current process. |
| [IDebugSystemObjects2::GetCurrentProcessExecutableName](nf-dbgeng-idebugsystemobjects2-getcurrentprocessexecutablename.md) | The GetCurrentProcessExecutableName method returns the name of executable file loaded in the current process. |
| [IDebugSystemObjects2::GetCurrentProcessHandle](nf-dbgeng-idebugsystemobjects2-getcurrentprocesshandle.md) | The GetCurrentProcessHandle method returns the system handle for the current process. |
| [IDebugSystemObjects2::GetCurrentProcessId](nf-dbgeng-idebugsystemobjects2-getcurrentprocessid.md) | The GetCurrentProcessId method returns the engine process ID for the current process. |
| [IDebugSystemObjects2::GetCurrentProcessPeb](nf-dbgeng-idebugsystemobjects2-getcurrentprocesspeb.md) | The GetCurrentProcessPeb method returns the process environment block (PEB) of the current process. |
| [IDebugSystemObjects2::GetCurrentProcessSystemId](nf-dbgeng-idebugsystemobjects2-getcurrentprocesssystemid.md) | The GetCurrentProcessSystemId method returns the system process ID of the current process. |
| [IDebugSystemObjects2::GetCurrentProcessUpTime](nf-dbgeng-idebugsystemobjects2-getcurrentprocessuptime.md) | The GetCurrentProcessUpTime method returns the length of time the current process has been running. |
| [IDebugSystemObjects2::GetCurrentThreadDataOffset](nf-dbgeng-idebugsystemobjects2-getcurrentthreaddataoffset.md) | The GetCurrentThreadDataOffset method returns the location of the system data structure for the current thread. |
| [IDebugSystemObjects2::GetCurrentThreadHandle](nf-dbgeng-idebugsystemobjects2-getcurrentthreadhandle.md) | The GetCurrentThreadHandle method returns the system handle for the current thread. |
| [IDebugSystemObjects2::GetCurrentThreadId](nf-dbgeng-idebugsystemobjects2-getcurrentthreadid.md) | The GetCurrentThreadId method returns the engine thread ID for the current thread. |
| [IDebugSystemObjects2::GetCurrentThreadSystemId](nf-dbgeng-idebugsystemobjects2-getcurrentthreadsystemid.md) | The GetCurrentThreadSystemId method returns the system thread ID of the current thread. |
| [IDebugSystemObjects2::GetCurrentThreadTeb](nf-dbgeng-idebugsystemobjects2-getcurrentthreadteb.md) | The GetCurrentThreadTeb method returns the location of the thread environment block (TEB) for the current thread. |
| [IDebugSystemObjects2::GetEventProcess](nf-dbgeng-idebugsystemobjects2-geteventprocess.md) | The GetEventProcess method returns the engine process ID for the process on which the last event occurred. |
| [IDebugSystemObjects2::GetEventThread](nf-dbgeng-idebugsystemobjects2-geteventthread.md) | The GetEventThread method returns the engine thread ID for the thread on which the last event occurred. |
| [IDebugSystemObjects2::GetImplicitProcessDataOffset](nf-dbgeng-idebugsystemobjects2-getimplicitprocessdataoffset.md) | The GetImplicitProcessDataOffset method returns the implicit process for the current target. |
| [IDebugSystemObjects2::GetImplicitThreadDataOffset](nf-dbgeng-idebugsystemobjects2-getimplicitthreaddataoffset.md) | The GetImplicitThreadDataOffset method returns the implicit thread for the current process. |
| [IDebugSystemObjects2::GetNumberProcesses](nf-dbgeng-idebugsystemobjects2-getnumberprocesses.md) | The GetNumberProcesses method returns the number of processes for the current target. |
| [IDebugSystemObjects2::GetNumberThreads](nf-dbgeng-idebugsystemobjects2-getnumberthreads.md) | The GetNumberThreads method returns the number of threads in the current process. |
| [IDebugSystemObjects2::GetProcessIdByDataOffset](nf-dbgeng-idebugsystemobjects2-getprocessidbydataoffset.md) | The GetProcessIdByDataOffset method returns the engine process ID for the specified process. The process is specified by its data offset. |
| [IDebugSystemObjects2::GetProcessIdByHandle](nf-dbgeng-idebugsystemobjects2-getprocessidbyhandle.md) | The GetProcessIdByHandle method returns the engine process ID for the specified process. The process is specified by its system handle. |
| [IDebugSystemObjects2::GetProcessIdByPeb](nf-dbgeng-idebugsystemobjects2-getprocessidbypeb.md) | The GetProcessIdByPeb method returns the engine process ID for the specified process. The process is specified by its process environment block (PEB). |
| [IDebugSystemObjects2::GetProcessIdBySystemId](nf-dbgeng-idebugsystemobjects2-getprocessidbysystemid.md) | The GetProcessIdBySystemId method returns the engine process ID for a process specified by its system process ID. |
| [IDebugSystemObjects2::GetProcessIdsByIndex](nf-dbgeng-idebugsystemobjects2-getprocessidsbyindex.md) | The GetProcessIdsByIndex method returns the engine process ID and system process ID for the specified processes in the current target. |
| [IDebugSystemObjects2::GetThreadIdByDataOffset](nf-dbgeng-idebugsystemobjects2-getthreadidbydataoffset.md) | The GetThreadIdByDataOffset method returns the engine thread ID for the specified thread. The thread is specified by its system data structure. |
| [IDebugSystemObjects2::GetThreadIdByHandle](nf-dbgeng-idebugsystemobjects2-getthreadidbyhandle.md) | The GetThreadIdByHandle method returns the engine thread ID for the specified thread. The thread is specified by its system handle. |
| [IDebugSystemObjects2::GetThreadIdByProcessor](nf-dbgeng-idebugsystemobjects2-getthreadidbyprocessor.md) | The GetThreadIdByProcessor method returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor. |
| [IDebugSystemObjects2::GetThreadIdBySystemId](nf-dbgeng-idebugsystemobjects2-getthreadidbysystemid.md) | The GetThreadIdBySystemId method returns the engine thread ID for the specified thread. The thread is specified by its system thread ID. |
| [IDebugSystemObjects2::GetThreadIdByTeb](nf-dbgeng-idebugsystemobjects2-getthreadidbyteb.md) | The GetThreadIdByTeb method returns the engine thread ID of the specified thread. The thread is specified by its thread environment block (TEB). |
| [IDebugSystemObjects2::GetThreadIdsByIndex](nf-dbgeng-idebugsystemobjects2-getthreadidsbyindex.md) | The GetThreadIdsByIndex method returns the engine and system thread IDs for the specified threads in the current process. |
| [IDebugSystemObjects2::GetTotalNumberThreads](nf-dbgeng-idebugsystemobjects2-gettotalnumberthreads.md) | The GetTotalNumberThreads method returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target. |
| [IDebugSystemObjects2::SetCurrentProcessId](nf-dbgeng-idebugsystemobjects2-setcurrentprocessid.md) | The SetCurrentProcessId method makes the specified process the current process. |
| [IDebugSystemObjects2::SetCurrentThreadId](nf-dbgeng-idebugsystemobjects2-setcurrentthreadid.md) | The SetCurrentThreadId method makes the specified thread the current thread. |
| [IDebugSystemObjects2::SetImplicitProcessDataOffset](nf-dbgeng-idebugsystemobjects2-setimplicitprocessdataoffset.md) | The SetImplicitProcessDataOffset method sets the implicit process for the current target. |
| [IDebugSystemObjects2::SetImplicitThreadDataOffset](nf-dbgeng-idebugsystemobjects2-setimplicitthreaddataoffset.md) | The SetImplicitThreadDataOffset method sets the implicit thread for the current process. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects4.md">IDebugSystemObjects4</a>



<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects.md">IDebugSystemObjects</a>



<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects3.md">IDebugSystemObjects3</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSystemObjects2 interface%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>