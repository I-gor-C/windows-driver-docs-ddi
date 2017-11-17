---
UID: NF.wdm.IoWithinStackLimits
title: IoWithinStackLimits
author: windows-driver-content
description: The IoWithinStackLimits routine determines whether a region of memory is within the stack limit of the current thread.
old-location: kernel\iowithinstacklimits.htm
ms.assetid: af182cd5-23b5-4d5b-b3d4-ec65ec087d0b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available on Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoWithinStackLimits
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
req.irql: <= APC_LEVEL
ms.keywords: IoWithinStackLimits
req.iface: 
req.product: Windows 10 or later.
---

# IoWithinStackLimits function



## -description
<p>The <b>IoWithinStackLimits</b> routine determines whether a region of memory is within the stack limit of the current thread.</p>


## -syntax

````
LOGICAL IoWithinStackLimits(
  _In_ ULONG_PTR RegionStart,
  _In_ SIZE_T    RegionSize
);
````


## -parameters
<dl>

### -param <i>RegionStart</i> [in]

<dd>
<p>A pointer to the start of the region.</p>
</dd>

### -param <i>RegionSize</i> [in]

<dd>
<p>The size of the region.</p>
</dd>
</dl>

## -returns
<p><b>IoWithinStackLimits</b> returns <b>TRUE</b> is the current thread's stack contains the region completely and <b>FALSE</b> otherwise.</p>

## -remarks
<p>The <b>IoWithinStackLimits</b> routine considers all possible stack segments and the DPC stack, if necessary.</p>

<p>The <b>IoWithinStackLimits</b> routine considers all possible stack segments and the DPC stack, if necessary.</p>

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
<p>Available on Windows Vista and later versions of the Windows operating system.</p>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549247">IoGetInitialStack</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549286">IoGetRemainingStackSize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549299">IoGetStackLimits</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWithinStackLimits routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
