---
UID: NF.wdm.KeSetPriorityThread
title: KeSetPriorityThread function
author: windows-driver-content
description: The KeSetPriorityThread routine sets the run-time priority of a driver-created thread.
old-location: kernel\kesetprioritythread.htm
old-project: kernel
ms.assetid: 400176a1-9192-424b-be37-9386cc3ffbb2
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KeSetPriorityThread
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeSetPriorityThread
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# KeSetPriorityThread function



## -description
The <b>KeSetPriorityThread</b> routine sets the run-time priority of a driver-created thread.


## -syntax

````
KPRIORITY KeSetPriorityThread(
  _Inout_ PKTHREAD  Thread,
  _In_    KPRIORITY Priority
);
````


## -parameters

### -param Thread [in, out]

Pointer to the driver-created thread.

### -param Priority [in]

Specifies the priority of the driver-created thread, usually to the real-time priority value, LOW_REALTIME_PRIORITY. The value LOW_PRIORITY is reserved for system use. 

## -returns
<b>KeSetPriorityThread</b> returns the old priority of the thread.

## -remarks
If a call to <b>KeSetPriorityThread</b> resets the thread's priority to a lower value, execution of the thread can be rescheduled even if it is currently running or is about to be dispatched for execution. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available starting with Windows 2000.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.kegetcurrentthread">KeGetCurrentThread</a>
</dt>
<dt>
<a href="kernel.kequeryprioritythread">KeQueryPriorityThread</a>
</dt>
<dt>
<a href="kernel.kesetbaseprioritythread">KeSetBasePriorityThread</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeSetPriorityThread routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
