---
UID: NF.dbgeng.IDebugSystemObjects4.GetTotalNumberThreadsAndProcesses
title: IDebugSystemObjects4::GetTotalNumberThreadsAndProcesses method
author: windows-driver-content
description: The GetTotalNumberThreadsAndProcesses method returns the total number of threads and processes in all the targets the engine is attached to, in addition to the largest number of threads and processes in a target.
old-location: debugger\gettotalnumberthreadsandprocesses.htm
old-project: Debugger
ms.assetid: 452dc67b-1938-4757-99bd-507a32d9a71a
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugSystemObjects4, IDebugSystemObjects4::GetTotalNumberThreadsAndProcesses, GetTotalNumberThreadsAndProcesses
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSystemObjects3.GetTotalNumberThreadsAndProcesses,IDebugSystemObjects4.GetTotalNumberThreadsAndProcesses
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

# IDebugSystemObjects4::GetTotalNumberThreadsAndProcesses method



## -description
The <b>GetTotalNumberThreadsAndProcesses</b> method returns the total number of <a href="debugger.controlling_threads_and_processes#threads#threads">threads</a> and <a href="debugger.controlling_threads_and_processes#processes#processes">processes</a> in all the targets the engine is attached to, in addition to the largest number of threads and processes in a target.



## -syntax

````
HRESULT GetTotalNumberThreadsAndProcesses(
  [out] PULONG TotalThreads,
  [out] PULONG TotalProcesses,
  [out] PULONG LargestProcessThreads,
  [out] PULONG LargestSystemThreads,
  [out] PULONG LargestSystemProcesses
);
````


## -parameters

### -param TotalThreads [out]

Receives the total number of threads in all processes in all targets.


### -param TotalProcesses [out]

Receives the total number of processes in all targets.


### -param LargestProcessThreads [out]

Receives the largest number of threads in any process on any target.


### -param LargestSystemThreads [out]

Receives the largest number of threads in any target.


### -param LargestSystemProcesses [out]

Receives the largest number of processes in any target.


## -returns
This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

 


## -remarks
If no target is found, all the values are set to zero.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects3.md">IDebugSystemObjects3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsystemobjects4.md">IDebugSystemObjects4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558896">Threads and Processes</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugSystemObjects3::GetTotalNumberThreadsAndProcesses method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
