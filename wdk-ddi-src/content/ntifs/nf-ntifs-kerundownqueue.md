---
UID: NF.ntifs.KeRundownQueue
title: KeRundownQueue
author: windows-driver-content
description: The KeRundownQueue routine cleans up a queue object, flushing any queued entries.
old-location: ifsk\kerundownqueue.htm
old-project: ifsk
ms.assetid: fc496af8-0b4b-4de4-8890-f2290970ced5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: KeRundownQueue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeRundownQueue
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# KeRundownQueue function



## -description
<p>The <b>KeRundownQueue</b> routine cleans up a queue object, flushing any queued entries. </p>


## -syntax

````
PLIST_ENTRY KeRundownQueue(
  _Inout_ PRKQUEUE Queue
);
````


## -parameters
<dl>

### -param Queue [in, out]

<dd>
<p>Pointer to an initialized queue object for which the caller provides resident storage in nonpaged pool.</p>
</dd>
</dl>

## -returns
<p>If the queue is empty, <b>KeRundownQueue</b> returns <b>NULL</b>; otherwise, it returns the address of the first entry in the queue. </p>

## -remarks
<p>File systems call <b>KeRundownQueue</b> to discard all entries from a queue before freeing or reusing the queue object.</p>

<p>If the queue object is to be reused, the caller must call <a href="..\ntifs\nf-ntifs-keinitializequeue.md">KeInitializeQueue</a> after calling <b>KeRundownQueue</b>, in order to reinitialize the queue object before reusing it. </p>

<p><b>KeRundownQueue</b> returns no information about how many queued entries are discarded. </p>

<p><b>KeRundownQueue</b> should never be called for a queue if any threads are waiting on the queue object.</p>

<p>For more information about using driver-managed internal queues, see <a href="kernel.driver_managed_queues">Driver-Managed Queues</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-keinitializequeue.md">KeInitializeQueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20KeRundownQueue routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
