---
UID: NN:dbgeng.IDebugSystemObjects
title: IDebugSystemObjects
author: windows-driver-content
description: IDebugSystemObjects interface
old-location: debugger\idebugsystemobjects.htm
old-project: Debugger
ms.assetid: ed830f09-10c0-4614-b002-8ede0e5e30bb
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: debugger.idebugsystemobjects, IDebugSystemObjects interface [Windows Debugging], IDebugSystemObjects interface [Windows Debugging], described, IDebugSystemObjects, dbgeng/IDebugSystemObjects, IDebugSystemObjects_82c2f1f3-4eb4-4071-ba0b-d2e4d2929ce2.xml
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
-	IDebugSystemObjects
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugSystemObjects interface



## Methods

<p>The <b>IDebugSystemObjects</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugSystemObjects.GetCurrentProcessDataOffset](nf-dbgeng-idebugsystemobjects-getcurrentprocessdataoffset.md) | The GetCurrentProcessDataOffset method returns the location of the system data structure describing the current process. |
| [dbgeng.IDebugSystemObjects.GetCurrentProcessExecutableName](nf-dbgeng-idebugsystemobjects-getcurrentprocessexecutablename.md) | The GetCurrentProcessExecutableName method returns the name of executable file loaded in the current process. |
| [dbgeng.IDebugSystemObjects.GetCurrentProcessHandle](nf-dbgeng-idebugsystemobjects-getcurrentprocesshandle.md) | The GetCurrentProcessHandle method returns the system handle for the current process. |
| [dbgeng.IDebugSystemObjects.GetCurrentProcessId](nf-dbgeng-idebugsystemobjects-getcurrentprocessid.md) | The GetCurrentProcessId method returns the engine process ID for the current process. |
| [dbgeng.IDebugSystemObjects.GetCurrentProcessPeb](nf-dbgeng-idebugsystemobjects-getcurrentprocesspeb.md) | The GetCurrentProcessPeb method returns the process environment block (PEB) of the current process. |
| [dbgeng.IDebugSystemObjects.GetCurrentProcessSystemId](nf-dbgeng-idebugsystemobjects-getcurrentprocesssystemid.md) | The GetCurrentProcessSystemId method returns the system process ID of the current process. |
| [dbgeng.IDebugSystemObjects.GetCurrentThreadDataOffset](nf-dbgeng-idebugsystemobjects-getcurrentthreaddataoffset.md) | The GetCurrentThreadDataOffset method returns the location of the system data structure for the current thread. |
| [dbgeng.IDebugSystemObjects.GetCurrentThreadHandle](nf-dbgeng-idebugsystemobjects-getcurrentthreadhandle.md) | The GetCurrentThreadHandle method returns the system handle for the current thread. |
| [dbgeng.IDebugSystemObjects.GetCurrentThreadId](nf-dbgeng-idebugsystemobjects-getcurrentthreadid.md) | The GetCurrentThreadId method returns the engine thread ID for the current thread. |
| [dbgeng.IDebugSystemObjects.GetCurrentThreadSystemId](nf-dbgeng-idebugsystemobjects-getcurrentthreadsystemid.md) | The GetCurrentThreadSystemId method returns the system thread ID of the current thread. |
| [dbgeng.IDebugSystemObjects.GetCurrentThreadTeb](nf-dbgeng-idebugsystemobjects-getcurrentthreadteb.md) | The GetCurrentThreadTeb method returns the location of the thread environment block (TEB) for the current thread. |
| [dbgeng.IDebugSystemObjects.GetEventProcess](nf-dbgeng-idebugsystemobjects-geteventprocess.md) | The GetEventProcess method returns the engine process ID for the process on which the last event occurred. |
| [dbgeng.IDebugSystemObjects.GetEventThread](nf-dbgeng-idebugsystemobjects-geteventthread.md) | The GetEventThread method returns the engine thread ID for the thread on which the last event occurred. |
| [dbgeng.IDebugSystemObjects.GetNumberProcesses](nf-dbgeng-idebugsystemobjects-getnumberprocesses.md) | The GetNumberProcesses method returns the number of processes for the current target. |
| [dbgeng.IDebugSystemObjects.GetNumberThreads](nf-dbgeng-idebugsystemobjects-getnumberthreads.md) | The GetNumberThreads method returns the number of threads in the current process. |
| [dbgeng.IDebugSystemObjects.GetProcessIdByDataOffset](nf-dbgeng-idebugsystemobjects-getprocessidbydataoffset.md) | The GetProcessIdByDataOffset method returns the engine process ID for the specified process. The process is specified by its data offset. |
| [dbgeng.IDebugSystemObjects.GetProcessIdByHandle](nf-dbgeng-idebugsystemobjects-getprocessidbyhandle.md) | The GetProcessIdByHandle method returns the engine process ID for the specified process. The process is specified by its system handle. |
| [dbgeng.IDebugSystemObjects.GetProcessIdByPeb](nf-dbgeng-idebugsystemobjects-getprocessidbypeb.md) | The GetProcessIdByPeb method returns the engine process ID for the specified process. The process is specified by its process environment block (PEB). |
| [dbgeng.IDebugSystemObjects.GetProcessIdBySystemId](nf-dbgeng-idebugsystemobjects-getprocessidbysystemid.md) | The GetProcessIdBySystemId method returns the engine process ID for a process specified by its system process ID. |
| [dbgeng.IDebugSystemObjects.GetProcessIdsByIndex](nf-dbgeng-idebugsystemobjects-getprocessidsbyindex.md) | The GetProcessIdsByIndex method returns the engine process ID and system process ID for the specified processes in the current target. |
| [dbgeng.IDebugSystemObjects.GetThreadIdByDataOffset](nf-dbgeng-idebugsystemobjects-getthreadidbydataoffset.md) | The GetThreadIdByDataOffset method returns the engine thread ID for the specified thread. The thread is specified by its system data structure. |
| [dbgeng.IDebugSystemObjects.GetThreadIdByHandle](nf-dbgeng-idebugsystemobjects-getthreadidbyhandle.md) | The GetThreadIdByHandle method returns the engine thread ID for the specified thread. The thread is specified by its system handle. |
| [dbgeng.IDebugSystemObjects.GetThreadIdByProcessor](nf-dbgeng-idebugsystemobjects-getthreadidbyprocessor.md) | The GetThreadIdByProcessor method returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor. |
| [dbgeng.IDebugSystemObjects.GetThreadIdBySystemId](nf-dbgeng-idebugsystemobjects-getthreadidbysystemid.md) | The GetThreadIdBySystemId method returns the engine thread ID for the specified thread. The thread is specified by its system thread ID. |
| [dbgeng.IDebugSystemObjects.GetThreadIdByTeb](nf-dbgeng-idebugsystemobjects-getthreadidbyteb.md) | The GetThreadIdByTeb method returns the engine thread ID of the specified thread. The thread is specified by its thread environment block (TEB). |
| [dbgeng.IDebugSystemObjects.GetThreadIdsByIndex](nf-dbgeng-idebugsystemobjects-getthreadidsbyindex.md) | The GetThreadIdsByIndex method returns the engine and system thread IDs for the specified threads in the current process. |
| [dbgeng.IDebugSystemObjects.GetTotalNumberThreads](nf-dbgeng-idebugsystemobjects-gettotalnumberthreads.md) | The GetTotalNumberThreads method returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target. |
| [dbgeng.IDebugSystemObjects.SetCurrentProcessId](nf-dbgeng-idebugsystemobjects-setcurrentprocessid.md) | The SetCurrentProcessId method makes the specified process the current process. |
| [dbgeng.IDebugSystemObjects.SetCurrentThreadId](nf-dbgeng-idebugsystemobjects-setcurrentthreadid.md) | The SetCurrentThreadId method makes the specified thread the current thread. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects4.md">IDebugSystemObjects4</a>



<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects3.md">IDebugSystemObjects3</a>



<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects3.md">IDebugSystemObjects3</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugSystemObjects interface%20 RELEASE:%20(2/15/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>