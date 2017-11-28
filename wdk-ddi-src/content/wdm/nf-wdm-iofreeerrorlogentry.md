---
UID: NF.wdm.IoFreeErrorLogEntry
title: IoFreeErrorLogEntry
author: windows-driver-content
description: The IoFreeErrorLogEntry routine frees an unused error log entry.
old-location: kernel\iofreeerrorlogentry.htm
old-project: kernel
ms.assetid: 7244a63b-404f-45e0-b2f7-6c4ea70e4a21
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoFreeErrorLogEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoFreeErrorLogEntry
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
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# IoFreeErrorLogEntry function



## -description
<p>The <b>IoFreeErrorLogEntry</b> routine frees an unused error log entry. </p>


## -syntax

````
VOID IoFreeErrorLogEntry(
  _In_ PVOID ElEntry
);
````


## -parameters
<dl>

### -param <i>ElEntry</i> [in]

<dd>
<p>Pointer to an error log packet allocated by <a href="https://msdn.microsoft.com/library/windows/hardware/ff548245">IoAllocateErrorLogEntry</a>. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Drivers use <b>IoFreeErrorLogEntry</b> to free an error log entry allocated by <a href="https://msdn.microsoft.com/library/windows/hardware/ff548245">IoAllocateErrorLogEntry</a>. <a href="https://msdn.microsoft.com/library/windows/hardware/ff550527">IoWriteErrorLogEntry</a> also frees any error log entries passed to it, so drivers must not call both on the same log entry.</p>

<p>Drivers use <b>IoFreeErrorLogEntry</b> to free an error log entry allocated by <a href="https://msdn.microsoft.com/library/windows/hardware/ff548245">IoAllocateErrorLogEntry</a>. <a href="https://msdn.microsoft.com/library/windows/hardware/ff550527">IoWriteErrorLogEntry</a> also frees any error log entries passed to it, so drivers must not call both on the same log entry.</p>

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
<p>Available in Windows XP and later versions of the Windows operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550527">IoWriteErrorLogEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoFreeErrorLogEntry routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
