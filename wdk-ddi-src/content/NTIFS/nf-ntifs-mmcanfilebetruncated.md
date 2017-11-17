---
UID: NF.ntifs.MmCanFileBeTruncated
title: MmCanFileBeTruncated
author: windows-driver-content
description: The MmCanFileBeTruncated routine checks whether a file can be truncated.
old-location: ifsk\mmcanfilebetruncated.htm
ms.assetid: 219ecf09-54eb-4972-ae71-0eb3e7ea8ea9
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmCanFileBeTruncated
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
req.irql: < DISPATCH_LEVEL
ms.keywords: MmCanFileBeTruncated
req.iface: 
---

# MmCanFileBeTruncated function



## -description
<p>The <b>MmCanFileBeTruncated</b> routine checks whether a file can be truncated.</p>


## -syntax

````
BOOLEAN MmCanFileBeTruncated(
  _In_     PSECTION_OBJECT_POINTERS SectionPointer,
  _In_opt_ PLARGE_INTEGER           NewFileSize
);
````


## -parameters
<dl>

### -param <i>SectionPointer</i> [in]

<dd>
<p>Pointer to a structure that contains the file object's section object pointers.</p>
</dd>

### -param <i>NewFileSize</i> [in, optional]

<dd>
<p>Pointer to a variable that specifies the size to which the file is to be truncated.</p>
</dd>
</dl>

## -returns
<p><b>MmCanFileBeTruncated</b> returns <b>TRUE</b> if the file can be truncated, <b>FALSE</b> otherwise.</p>

## -remarks
<p><b>MmCanFileBeTruncated</b> must always be called before a file is truncated.</p>

<p>A file cannot be truncated (and <b>MmCanFileBeTruncated</b> will return <b>FALSE</b>) if any of the following are true:</p>

<p>An image section exists for the file.</p>

<p>There are one or more outstanding write probes on the file's data section.</p>

<p>There is a mapped view of file's data section within the truncation range determined by <i>NewFileSize</i>.</p>

<p>One or more users hold references to the data section for the file, and <i>NewFileSize</i> &lt;= the current file size.</p>

<p><b>MmCanFileBeTruncated</b> must always be called before a file is truncated.</p>

<p>A file cannot be truncated (and <b>MmCanFileBeTruncated</b> will return <b>FALSE</b>) if any of the following are true:</p>

<p>An image section exists for the file.</p>

<p>There are one or more outstanding write probes on the file's data section.</p>

<p>There is a mapped view of file's data section within the truncation range determined by <i>NewFileSize</i>.</p>

<p>One or more users hold references to the data section for the file, and <i>NewFileSize</i> &lt;= the current file size.</p>

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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539188">CcPurgeCacheSection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549808">MmFlushImageSection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MmCanFileBeTruncated routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
