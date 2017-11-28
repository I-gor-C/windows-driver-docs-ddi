---
UID: NF.ntifs.CcUninitializeCacheMap
title: CcUninitializeCacheMap
author: windows-driver-content
description: The CcUninitializeCacheMap routine stops the caching of a cached file.
old-location: ifsk\ccuninitializecachemap.htm
old-project: ifsk
ms.assetid: 00e5abd6-c2d7-4408-aaf4-27a67dd3ee51
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcUninitializeCacheMap
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
req.alt-api: CcUninitializeCacheMap
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
---

# CcUninitializeCacheMap function



## -description
<p>The <b>CcUninitializeCacheMap</b> routine stops the caching of a cached file.</p>


## -syntax

````
BOOLEAN CcUninitializeCacheMap(
  _In_     PFILE_OBJECT              FileObject,
  _In_opt_ PLARGE_INTEGER            TruncateSize,
  _In_opt_ PCACHE_UNINITIALIZE_EVENT UninitializeCompleteEvent
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to a file object for the cached file.</p>
</dd>

### -param <i>TruncateSize</i> [in, optional]

<dd>
<p>If specified, the file was truncated to the specified size, and the cache should be purged accordingly.</p>
</dd>

### -param <i>UninitializeCompleteEvent</i> [in, optional]

<dd>
<p>If specified, the provided event is set to the signaled state when the cached file data has been flushed to disk.</p>
</dd>
</dl>

## -returns
<p><b>CcUninitializeCacheMap</b> returns <b>TRUE</b> if caching was stopped successfully, <b>FALSE</b> otherwise.</p>

## -remarks
<p>All file systems that support file caching must call <b>CcUninitializeCacheMap</b> when closing a file, whether the file is cached or not. Even if the file was created with caching disabled, the file system still must call <b>CcUninitializeCacheMap</b>.</p>

<p>To cache a file, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>.</p>

<p>All file systems that support file caching must call <b>CcUninitializeCacheMap</b> when closing a file, whether the file is cached or not. Even if the file was created with caching disabled, the file system still must call <b>CcUninitializeCacheMap</b>.</p>

<p>To cache a file, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539188">CcPurgeCacheSection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcUninitializeCacheMap routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
