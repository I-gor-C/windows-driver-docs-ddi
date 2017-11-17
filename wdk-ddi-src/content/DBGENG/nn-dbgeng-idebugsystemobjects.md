---
UID: NN.dbgeng.IDebugSystemObjects
title: IDebugSystemObjects
author: windows-driver-content
description: IDebugSystemObjects interface
old-location: debugger\idebugsystemobjects.htm
ms.assetid: ed830f09-10c0-4614-b002-8ede0e5e30bb
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: debugger
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
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
req.iface: IDebugSystemObjects4
---

# IDebugSystemObjects interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSystemObjects</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugSystemObjects</b> also has these types of members:</p>

<p>The <b>IDebugSystemObjects</b> interface has these methods.</p>

<p>Returns the location of the system data structure describing the current process.</p>

<p>Returns the name of executable file loaded in the current process.</p>

<p>Returns the system handle for the current process.</p>

<p>Returns the engine process ID for the current process.</p>

<p>Returns the process environment block (PEB) of the current process.</p>

<p>Returns the system process ID of the current process.</p>

<p>Returns the location of the system data structure for the current thread.</p>

<p>Returns the system handle for the current thread.</p>

<p>Returns the engine thread ID for the current thread.</p>

<p>Returns the system thread ID of the current thread.</p>

<p>Returns the location of the thread environment block (TEB) for the current thread.</p>

<p>Returns the engine process ID for the process on which the last event occurred.</p>

<p>Returns the engine thread ID for the thread on which the last event occurred.</p>

<p>Returns the number of processes for the current target.</p>

<p>Returns the number of threads in the current process.</p>

<p>Returns the engine process ID for the specified process.</p>

<p>Returns the engine process ID for the specified process.</p>

<p>Returns the engine process ID for the specified process.</p>

<p>Returns the engine process ID for a process specified by its system process ID.</p>

<p>Returns the engine process ID and system process ID for the specified processes in the current target.</p>

<p>Returns the engine thread ID for the specified thread.</p>

<p>Returns the engine thread ID for the specified thread.</p>

<p>Returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor.</p>

<p>Returns the engine thread ID for the specified thread.</p>

<p>Returns the engine thread ID of the specified thread.</p>

<p>Returns the engine and system thread IDs for the specified threads in the current process.</p>

<p>Returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target.</p>

<p>Makes the specified process the current process.</p>

<p>Makes the specified thread the current thread.</p>

<p> </p>

## -members
<p>The <b>IDebugSystemObjects</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545787">GetCurrentProcessDataOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the system data structure describing the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545794">GetCurrentProcessExecutableName</a>
</td>
<td align="left" width="63%">
<p>Returns the name of executable file loaded in the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545816">GetCurrentProcessHandle</a>
</td>
<td align="left" width="63%">
<p>Returns the system handle for the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545836">GetCurrentProcessId</a>
</td>
<td align="left" width="63%">
<p>Returns the engine process ID for the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545839">GetCurrentProcessPeb</a>
</td>
<td align="left" width="63%">
<p>Returns the process environment block (PEB) of the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545850">GetCurrentProcessSystemId</a>
</td>
<td align="left" width="63%">
<p>Returns the system process ID of the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545894">GetCurrentThreadDataOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the system data structure for the current thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545904">GetCurrentThreadHandle</a>
</td>
<td align="left" width="63%">
<p>Returns the system handle for the current thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546542">GetCurrentThreadId</a>
</td>
<td align="left" width="63%">
<p>Returns the engine thread ID for the current thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546544">GetCurrentThreadSystemId</a>
</td>
<td align="left" width="63%">
<p>Returns the system thread ID of the current thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546549">GetCurrentThreadTeb</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the thread environment block (TEB) for the current thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546640">GetEventProcess</a>
</td>
<td align="left" width="63%">
<p>Returns the engine process ID for the process on which the last event occurred.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546646">GetEventThread</a>
</td>
<td align="left" width="63%">
<p>Returns the engine thread ID for the thread on which the last event occurred.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547946">GetNumberProcesses</a>
</td>
<td align="left" width="63%">
<p>Returns the number of processes for the current target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547992">GetNumberThreads</a>
</td>
<td align="left" width="63%">
<p>Returns the number of threads in the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548140">GetProcessIdByDataOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the engine process ID for the specified process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548147">GetProcessIdByHandle</a>
</td>
<td align="left" width="63%">
<p>Returns the engine process ID for the specified process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548150">GetProcessIdByPeb</a>
</td>
<td align="left" width="63%">
<p>Returns the engine process ID for the specified process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548155">GetProcessIdBySystemId</a>
</td>
<td align="left" width="63%">
<p>Returns the engine process ID for a process specified by its system process ID.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548160">GetProcessIdsByIndex</a>
</td>
<td align="left" width="63%">
<p>Returns the engine process ID and system process ID for the specified processes in the current target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549302">GetThreadIdByDataOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the engine thread ID for the specified thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549312">GetThreadIdByHandle</a>
</td>
<td align="left" width="63%">
<p>Returns the engine thread ID for the specified thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549319">GetThreadIdByProcessor</a>
</td>
<td align="left" width="63%">
<p>Returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549329">GetThreadIdBySystemId</a>
</td>
<td align="left" width="63%">
<p>Returns the engine thread ID for the specified thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549336">GetThreadIdByTeb</a>
</td>
<td align="left" width="63%">
<p>Returns the engine thread ID of the specified thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549339">GetThreadIdsByIndex</a>
</td>
<td align="left" width="63%">
<p>Returns the engine and system thread IDs for the specified threads in the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549356">GetTotalNumberThreads</a>
</td>
<td align="left" width="63%">
<p>Returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556645">SetCurrentProcessId</a>
</td>
<td align="left" width="63%">
<p>Makes the specified process the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556650">SetCurrentThreadId</a>
</td>
<td align="left" width="63%">
<p>Makes the specified thread the current thread.</p>
</td>
</tr>
</table><p>Returns the location of the system data structure describing the current process.</p>

<p>Returns the name of executable file loaded in the current process.</p>

<p>Returns the system handle for the current process.</p>

<p>Returns the engine process ID for the current process.</p>

<p>Returns the process environment block (PEB) of the current process.</p>

<p>Returns the system process ID of the current process.</p>

<p>Returns the location of the system data structure for the current thread.</p>

<p>Returns the system handle for the current thread.</p>

<p>Returns the engine thread ID for the current thread.</p>

<p>Returns the system thread ID of the current thread.</p>

<p>Returns the location of the thread environment block (TEB) for the current thread.</p>

<p>Returns the engine process ID for the process on which the last event occurred.</p>

<p>Returns the engine thread ID for the thread on which the last event occurred.</p>

<p>Returns the number of processes for the current target.</p>

<p>Returns the number of threads in the current process.</p>

<p>Returns the engine process ID for the specified process.</p>

<p>Returns the engine process ID for the specified process.</p>

<p>Returns the engine process ID for the specified process.</p>

<p>Returns the engine process ID for a process specified by its system process ID.</p>

<p>Returns the engine process ID and system process ID for the specified processes in the current target.</p>

<p>Returns the engine thread ID for the specified thread.</p>

<p>Returns the engine thread ID for the specified thread.</p>

<p>Returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor.</p>

<p>Returns the engine thread ID for the specified thread.</p>

<p>Returns the engine thread ID of the specified thread.</p>

<p>Returns the engine and system thread IDs for the specified threads in the current process.</p>

<p>Returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target.</p>

<p>Makes the specified process the current process.</p>

<p>Makes the specified thread the current thread.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550885">IDebugSystemObjects2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550892">IDebugSystemObjects3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550893">IDebugSystemObjects4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSystemObjects interface%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
