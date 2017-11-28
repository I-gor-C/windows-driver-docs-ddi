---
UID: NF.ntifs.CcGetFlushedValidData
title: CcGetFlushedValidData
author: windows-driver-content
description: The CcGetFlushedValidData routine determines how much of a cached file has been flushed to disk.
old-location: ifsk\ccgetflushedvaliddata.htm
old-project: ifsk
ms.assetid: a0e3700a-768f-4025-b5f2-715e25e1d10d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcGetFlushedValidData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available on Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcGetFlushedValidData
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

# CcGetFlushedValidData function



## -description
<p>The <b>CcGetFlushedValidData</b> routine determines how much of a cached file has been flushed to disk.</p>


## -syntax

````
LARGE_INTEGER CcGetFlushedValidData(
  _In_ PSECTION_OBJECT_POINTERS SectionObjectPointer,
  _In_ BOOLEAN                  BcbListHeld
);
````


## -parameters
<dl>

### -param <i>SectionObjectPointer</i> [in]

<dd>
<p>Pointer to a structure containing the file object's section object pointers.</p>
</dd>

### -param <i>BcbListHeld</i> [in]

<dd>
<p>Reserved for system use. Must be <b>FALSE</b>.</p>
</dd>
</dl>

## -returns
<p>If the entire file has been flushed, <b>CcGetFlushedValidData</b> returns the valid data length for the file. If there are dirty pages that have not been flushed to disk, <b>CcGetFlushedValidData</b> returns the starting byte offset of the lowest dirty page currently in the file. If the file is not cached or is no longer cached, MAXLONGLONG is returned in the quad part.</p>

## -remarks
<p>The file system is responsible for ensuring that the value of <i>SectionObjectPointer</i> remains valid while in use. It is impossible for the cache manager to guarantee this.</p>

<p>The file system is responsible for ensuring that the value of <i>SectionObjectPointer</i> remains valid while in use. It is impossible for the cache manager to guarantee this.</p>

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
<p>Available on Microsoft Windows 2000 and later.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539082">CcFlushCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539188">CcPurgeCacheSection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcGetFlushedValidData routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
