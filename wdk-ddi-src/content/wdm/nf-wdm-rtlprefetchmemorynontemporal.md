---
UID: NF.wdm.RtlPrefetchMemoryNonTemporal
title: RtlPrefetchMemoryNonTemporal
author: windows-driver-content
description: The RtlPrefetchMemoryNonTemporal routine provides a hint to the processor that a buffer should be temporarily moved into the processor cache.
old-location: kernel\rtlprefetchmemorynontemporal.htm
old-project: kernel
ms.assetid: d11c3414-86c8-4b68-829e-4523519c5299
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlPrefetchMemoryNonTemporal
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Ntddk.h, Wdm.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Server 2003 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlPrefetchMemoryNonTemporal
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
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# RtlPrefetchMemoryNonTemporal function



## -description
<p>The <b>RtlPrefetchMemoryNonTemporal</b> routine provides a hint to the processor that a buffer should be temporarily moved into the processor cache.</p>


## -syntax

````
VOID RtlPrefetchMemoryNonTemporal(
  _In_ PVOID  Source,
  _In_ SIZE_T Length
);
````


## -parameters
<dl>

### -param <i>Source</i> [in]

<dd>
<p>A pointer to the buffer to be moved into the processor cache. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length of the buffer to be moved. </p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>You should use this routine only for a buffer that will be written to or read from exactly once. Note that <b>RtlPrefetchMemoryNonTemporal</b> is only a hint to the processor: the buffer is not guaranteed to be moved into the cache. On x86-based and x64-based systems, this routine uses the <b>prefetchnta</b> instruction.</p>

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
<p>Available in Windows Server 2003 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Ntddk.h or Wdm.h)</dt>
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
<p>Any level</p>
</td>
</tr>
</table>