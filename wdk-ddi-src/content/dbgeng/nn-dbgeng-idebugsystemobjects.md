---
UID: NN.dbgeng.IDebugSystemObjects
title: IDebugSystemObjects
author: windows-driver-content
description: IDebugSystemObjects interface
old-location: debugger\idebugsystemobjects.htm
old-project: debugger
ms.assetid: ed830f09-10c0-4614-b002-8ede0e5e30bb
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: DebugCreateEx
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
req.alt-api: IDebugSystemObjects
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
---

# IDebugSystemObjects interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSystemObjects</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugSystemObjects</b> also has these types of members:

The <b>IDebugSystemObjects</b> interface has these methods.

Returns the location of the system data structure describing the current process.

Returns the name of executable file loaded in the current process.

Returns the system handle for the current process.

Returns the engine process ID for the current process.

Returns the process environment block (PEB) of the current process.

Returns the system process ID of the current process.

Returns the location of the system data structure for the current thread.

Returns the system handle for the current thread.

Returns the engine thread ID for the current thread.

Returns the system thread ID of the current thread.

Returns the location of the thread environment block (TEB) for the current thread.

Returns the engine process ID for the process on which the last event occurred.

Returns the engine thread ID for the thread on which the last event occurred.

Returns the number of processes for the current target.

Returns the number of threads in the current process.

Returns the engine process ID for the specified process.

Returns the engine process ID for the specified process.

Returns the engine process ID for the specified process.

Returns the engine process ID for a process specified by its system process ID.

Returns the engine process ID and system process ID for the specified processes in the current target.

Returns the engine thread ID for the specified thread.

Returns the engine thread ID for the specified thread.

Returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor.

Returns the engine thread ID for the specified thread.

Returns the engine thread ID of the specified thread.

Returns the engine and system thread IDs for the specified threads in the current process.

Returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target.

Makes the specified process the current process.

Makes the specified thread the current thread.

 


## -members
The <b>IDebugSystemObjects</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentprocessdataoffset">GetCurrentProcessDataOffset</a>
</td>
<td align="left" width="63%">
Returns the location of the system data structure describing the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentprocessexecutablename">GetCurrentProcessExecutableName</a>
</td>
<td align="left" width="63%">
Returns the name of executable file loaded in the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentprocesshandle">GetCurrentProcessHandle</a>
</td>
<td align="left" width="63%">
Returns the system handle for the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentprocessid">GetCurrentProcessId</a>
</td>
<td align="left" width="63%">
Returns the engine process ID for the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentprocesspeb">GetCurrentProcessPeb</a>
</td>
<td align="left" width="63%">
Returns the process environment block (PEB) of the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentprocesssystemid">GetCurrentProcessSystemId</a>
</td>
<td align="left" width="63%">
Returns the system process ID of the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentthreaddataoffset">GetCurrentThreadDataOffset</a>
</td>
<td align="left" width="63%">
Returns the location of the system data structure for the current thread.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentthreadhandle">GetCurrentThreadHandle</a>
</td>
<td align="left" width="63%">
Returns the system handle for the current thread.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentthreadid">GetCurrentThreadId</a>
</td>
<td align="left" width="63%">
Returns the engine thread ID for the current thread.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentthreadsystemid">GetCurrentThreadSystemId</a>
</td>
<td align="left" width="63%">
Returns the system thread ID of the current thread.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentthreadteb">GetCurrentThreadTeb</a>
</td>
<td align="left" width="63%">
Returns the location of the thread environment block (TEB) for the current thread.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.geteventprocess">GetEventProcess</a>
</td>
<td align="left" width="63%">
Returns the engine process ID for the process on which the last event occurred.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.geteventthread">GetEventThread</a>
</td>
<td align="left" width="63%">
Returns the engine thread ID for the thread on which the last event occurred.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnumberprocesses">GetNumberProcesses</a>
</td>
<td align="left" width="63%">
Returns the number of processes for the current target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnumberthreads">GetNumberThreads</a>
</td>
<td align="left" width="63%">
Returns the number of threads in the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getprocessidbydataoffset">GetProcessIdByDataOffset</a>
</td>
<td align="left" width="63%">
Returns the engine process ID for the specified process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getprocessidbyhandle">GetProcessIdByHandle</a>
</td>
<td align="left" width="63%">
Returns the engine process ID for the specified process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getprocessidbypeb">GetProcessIdByPeb</a>
</td>
<td align="left" width="63%">
Returns the engine process ID for the specified process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getprocessidbysystemid">GetProcessIdBySystemId</a>
</td>
<td align="left" width="63%">
Returns the engine process ID for a process specified by its system process ID.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getprocessidsbyindex">GetProcessIdsByIndex</a>
</td>
<td align="left" width="63%">
Returns the engine process ID and system process ID for the specified processes in the current target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getthreadidbydataoffset">GetThreadIdByDataOffset</a>
</td>
<td align="left" width="63%">
Returns the engine thread ID for the specified thread.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getthreadidbyhandle">GetThreadIdByHandle</a>
</td>
<td align="left" width="63%">
Returns the engine thread ID for the specified thread.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getthreadidbyprocessor">GetThreadIdByProcessor</a>
</td>
<td align="left" width="63%">
Returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getthreadidbysystemid">GetThreadIdBySystemId</a>
</td>
<td align="left" width="63%">
Returns the engine thread ID for the specified thread.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getthreadidbyteb">GetThreadIdByTeb</a>
</td>
<td align="left" width="63%">
Returns the engine thread ID of the specified thread.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getthreadidsbyindex">GetThreadIdsByIndex</a>
</td>
<td align="left" width="63%">
Returns the engine and system thread IDs for the specified threads in the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettotalnumberthreads">GetTotalNumberThreads</a>
</td>
<td align="left" width="63%">
Returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setcurrentprocessid">SetCurrentProcessId</a>
</td>
<td align="left" width="63%">
Makes the specified process the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setcurrentthreadid">SetCurrentThreadId</a>
</td>
<td align="left" width="63%">
Makes the specified thread the current thread.

</td>
</tr>
</table>Returns the location of the system data structure describing the current process.

Returns the name of executable file loaded in the current process.

Returns the system handle for the current process.

Returns the engine process ID for the current process.

Returns the process environment block (PEB) of the current process.

Returns the system process ID of the current process.

Returns the location of the system data structure for the current thread.

Returns the system handle for the current thread.

Returns the engine thread ID for the current thread.

Returns the system thread ID of the current thread.

Returns the location of the thread environment block (TEB) for the current thread.

Returns the engine process ID for the process on which the last event occurred.

Returns the engine thread ID for the thread on which the last event occurred.

Returns the number of processes for the current target.

Returns the number of threads in the current process.

Returns the engine process ID for the specified process.

Returns the engine process ID for the specified process.

Returns the engine process ID for the specified process.

Returns the engine process ID for a process specified by its system process ID.

Returns the engine process ID and system process ID for the specified processes in the current target.

Returns the engine thread ID for the specified thread.

Returns the engine thread ID for the specified thread.

Returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor.

Returns the engine thread ID for the specified thread.

Returns the engine thread ID of the specified thread.

Returns the engine and system thread IDs for the specified threads in the current process.

Returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target.

Makes the specified process the current process.

Makes the specified thread the current thread.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects2.md">IDebugSystemObjects2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects3.md">IDebugSystemObjects3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects4.md">IDebugSystemObjects4</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSystemObjects interface%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

