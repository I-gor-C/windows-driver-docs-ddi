---
UID: NF.wdm.IoWriteErrorLogEntry
title: IoWriteErrorLogEntry
author: windows-driver-content
description: The IoWriteErrorLogEntry routine queues a given error log packet to the system error logging thread.
old-location: kernel\iowriteerrorlogentry.htm
old-project: kernel
ms.assetid: 1259c344-584c-410a-a152-5de1f433082c
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoWriteErrorLogEntry
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
req.alt-api: IoWriteErrorLogEntry
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlDispatch
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
req.product: Windows 10 or later.
---

# IoWriteErrorLogEntry function



## -description
<p>The <b>IoWriteErrorLogEntry</b> routine queues a given error log packet to the system error logging thread.</p>


## -syntax

````
VOID IoWriteErrorLogEntry(
  _In_ PVOID ElEntry
);
````


## -parameters
<dl>

### -param <i>ElEntry</i> [in]

<dd>
<p>Pointer to the error log packet the driver has allocated with <a href="https://msdn.microsoft.com/library/windows/hardware/ff548245">IoAllocateErrorLogEntry</a> and filled in by the caller. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>IoWriteErrorLogEntry</b> frees the error log entry. Drivers must not call <b>IoFreeErrorLogEntry</b> on a log entry that they have already passed to <b>IoWriteErrorLogEntry</b>.</p>

<p><b>IoWriteErrorLogEntry</b> frees the error log entry. Drivers must not call <b>IoFreeErrorLogEntry</b> on a log entry that they have already passed to <b>IoWriteErrorLogEntry</b>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547743">IrqlDispatch</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550571">IO_ERROR_LOG_PACKET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548245">IoAllocateErrorLogEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549107">IoFreeErrorLogEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWriteErrorLogEntry routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
