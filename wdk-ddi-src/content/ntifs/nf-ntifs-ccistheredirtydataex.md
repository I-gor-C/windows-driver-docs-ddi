---
UID: NF.ntifs.CcIsThereDirtyDataEx
title: CcIsThereDirtyDataEx
author: windows-driver-content
description: The CcIsThereDirtyDataEx routine determines whether a volume contains any files that have dirty data in the system cache.
old-location: ifsk\ccistheredirtydataex.htm
old-project: ifsk
ms.assetid: 88378f82-2975-4b53-9dde-53ab81df3c53
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcIsThereDirtyDataEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcIsThereDirtyDataEx
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
req.iface: 
---

# CcIsThereDirtyDataEx function



## -description
<p>The <b>CcIsThereDirtyDataEx</b> routine determines whether a volume contains any files that have dirty data in the system cache.</p>


## -syntax

````
BOOLEAN CcIsThereDirtyDataEx(
  _In_     PVPB   Vpb,
  _In_opt_ PULONG NumberOfDirtyPages
);
````


## -parameters
<dl>

### -param <i>Vpb</i> [in]

<dd>
<p>A pointer to a volume parameter block (VPB) for the volume. </p>
</dd>

### -param <i>NumberOfDirtyPages</i> [in, optional]

<dd>
<p>An optional pointer to an unsigned long buffer that receives the number of dirty pages on the volume (associated with the Vpb parameter). </p>
</dd>
</dl>

## -returns
<p>The <b>CcIsThereDirtyDataEx</b> routine returns <b>TRUE</b> if the volume contains one or more cached files whose data has been modified in the cache, but not yet flushed to disk. Otherwise, this routine returns <b>FALSE</b>.</p>

## -remarks
<p>This routine will return <b>TRUE</b> if any dirty pages exist including temporary files (<a href="https://msdn.microsoft.com/library/windows/hardware/ff539145">CcIsThereDirtyData</a> ignores temporary files).  It will also return <b>TRUE</b> if there is any data currently queued to the volume.</p>

<p>This routine will return <b>TRUE</b> if any dirty pages exist including temporary files (<a href="https://msdn.microsoft.com/library/windows/hardware/ff539145">CcIsThereDirtyData</a> ignores temporary files).  It will also return <b>TRUE</b> if there is any data currently queued to the volume.</p>

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
<p>Available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or FltKernel.h)</dt>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539082">CcFlushCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539188">CcPurgeCacheSection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539145">CcIsThereDirtyData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcIsThereDirtyDataEx routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
