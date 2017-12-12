---
UID: NF.wdm.RtlPrefetchMemoryNonTemporal
title: RtlPrefetchMemoryNonTemporal function
author: windows-driver-content
description: The RtlPrefetchMemoryNonTemporal routine provides a hint to the processor that a buffer should be temporarily moved into the processor cache.
old-location: kernel\rtlprefetchmemorynontemporal.htm
old-project: kernel
ms.assetid: d11c3414-86c8-4b68-829e-4523519c5299
ms.author: windowsdriverdev
ms.date: 12/7/2017
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
req.product: Windows 10 or later.
---

# RtlPrefetchMemoryNonTemporal function



## -description
The <b>RtlPrefetchMemoryNonTemporal</b> routine provides a hint to the processor that a buffer should be temporarily moved into the processor cache.



## -syntax

````
VOID RtlPrefetchMemoryNonTemporal(
  _In_ PVOID  Source,
  _In_ SIZE_T Length
);
````


## -parameters

### -param Source [in]

A pointer to the buffer to be moved into the processor cache. 


### -param Length [in]

The length of the buffer to be moved. 


## -returns
None.


## -remarks
You should use this routine only for a buffer that will be written to or read from exactly once. Note that <b>RtlPrefetchMemoryNonTemporal</b> is only a hint to the processor: the buffer is not guaranteed to be moved into the cache. On x86-based and x64-based systems, this routine uses the <b>prefetchnta</b> instruction.


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
Available in Windows Server 2003 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Ntddk.h or Wdm.h)</dt>
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
Any level

</td>
</tr>
</table>