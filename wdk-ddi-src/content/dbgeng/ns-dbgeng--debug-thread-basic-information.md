---
UID: NS.dbgeng._DEBUG_THREAD_BASIC_INFORMATION
title: DEBUG_THREAD_BASIC_INFORMATION
author: windows-driver-content
description: The DEBUG_THREAD_BASIC_INFORMATION structure describes an operating system thread.
old-location: debugger\debug_thread_basic_information.htm
old-project: debugger
ms.assetid: e964ed63-6c00-4308-955c-f8a99490a248
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DEBUG_THREAD_BASIC_INFORMATION, DEBUG_THREAD_BASIC_INFORMATION, *PDEBUG_THREAD_BASIC_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_THREAD_BASIC_INFORMATION
req.alt-loc: DbgEng.h
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
req.iface: IDebugSystemObjects4
---

# DEBUG_THREAD_BASIC_INFORMATION structure



## -description
<p>The DEBUG_THREAD_BASIC_INFORMATION structure describes an operating system thread.</p>


## -syntax

````
typedef struct _DEBUG_THREAD_BASIC_INFORMATION {
  ULONG   Valid;
  ULONG   ExitStatus;
  ULONG   PriorityClass;
  ULONG   Priority;
  ULONG64 CreateTime;
  ULONG64 ExitTime;
  ULONG64 KernelTime;
  ULONG64 UserTime;
  ULONG64 StartOffset;
  ULONG64 Affinity;
}  DEBUG_THREAD_BASIC_INFORMATION, *PDEBUG_THREAD_BASIC_INFORMATION;
````


## -struct-fields
<dl>

### -field Valid

<dd>
<p>A bitset that specifies which other members of the structure contain valid information. A member of the structure is valid if the corresponding bit flag is set in <b>Valid</b>.</p>
<table>
<tr>
<th>Flag</th>
<th>Members</th>
</tr>
<tr>
<td>
<p>DEBUG_TBINFO_EXIT_STATUS</p>
</td>
<td>
<p><b>ExitStatus</b></p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_TBINFO_PRIORITY_CLASS</p>
</td>
<td>
<p><b>PriorityClass</b></p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_TBINFO_PRIORITY</p>
</td>
<td>
<p><b>Priority</b></p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_TBINFO_TIMES</p>
</td>
<td>
<p><b>CreateTime</b>, <b>ExitTime</b>, <b>KernelTime</b>, <b> UserTime</b></p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_TBINFO_START_OFFSET</p>
</td>
<td>
<p><b>StartOffset</b></p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_TBINFO_AFFINITY</p>
</td>
<td>
<p><b>Affinity</b></p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field ExitStatus

<dd>
<p>The exit code of the thread. If the thread is still running, <b>ExitStatus</b> is set to STILL_ACTIVE.</p>
<p><b>ExitStatus</b> is only valid if the  DEBUG_TBINFO_EXIT_STATUS bit flag is set in <b>Valid</b>.</p>
</dd>

### -field PriorityClass

<dd>
<p>The priority class of the thread. The priority classes are defined by the <i>XXX</i>_PRIORITY_CLASS constants in WinBase.h. For more information about thread priority classes, see the Platform SDK.</p>
<p><b>PriorityClass</b> is only valid if the DEBUG_TBINFO_PRIORITY_CLASS bit flag is set in <b>Valid</b>.</p>
</dd>

### -field Priority

<dd>
<p>The priority of the thread relative to the priority class. Some thread priorities are defined by the THREAD_PRIORITY_<i>XXX</i> constants in WinBase.h.  For more information about thread priorities,  see the Platform SDK.</p>
<p><b>Priority</b> is only valid if the DEBUG_TBINFO_PRIORITY bit flag is set in <b>Valid</b>.</p>
</dd>

### -field CreateTime

<dd>
<p>The creation time of the thread.</p>
<p><b>CreateTime</b> is only valid if the DEBUG_TBINFO_TIMES bit flag is set in <b>Valid</b>.</p>
</dd>

### -field ExitTime

<dd>
<p>The exit time of the thread.</p>
<p><b>ExitTime</b> is only valid if the DEBUG_TBINFO_TIMES bit flag is set in <b>Valid</b>.</p>
</dd>

### -field KernelTime

<dd>
<p>The amount of time the thread has executed in kernel mode.</p>
<p><b>KernelTime</b> is only valid if the DEBUG_TBINFO_TIMES bit flag is set in <b>Valid</b>.</p>
</dd>

### -field UserTime

<dd>
<p>The amount of time the thread has executed in user-mode.</p>
<p><b>UserTime</b> is only valid if the DEBUG_TBINFO_TIMES bit flag is set in <b>Valid</b>.</p>
</dd>

### -field StartOffset

<dd>
<p>The starting address of the thread.</p>
<p><b>StartOffset</b> is only valid if the DEBUG_TBINFO_START_OFFSET bit flag is set in <b>Valid</b>.</p>
</dd>

### -field Affinity

<dd>
<p>The thread affinity mask for the thread in a Symmetric Multiple Processor (SMP) computer. For more information about the thread affinity mask, see the Platform SDK.</p>
<p><b>Affinity</b> is only valid if the DEBUG_TBINFO_AFFINITY bit flag is set in <b>Valid</b>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>DbgEng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>