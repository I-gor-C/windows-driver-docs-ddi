---
UID: NF.ntifs.MmFlushImageSection
title: MmFlushImageSection
author: windows-driver-content
description: The MmFlushImageSection routine flushes the image section for a file.
old-location: ifsk\mmflushimagesection.htm
old-project: ifsk
ms.assetid: e5c94f80-8ff8-4945-b1b8-a12190c3dec7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: MmFlushImageSection
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
req.alt-api: MmFlushImageSection
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
req.iface: 
---

# MmFlushImageSection function



## -description
<p>The <b>MmFlushImageSection</b> routine flushes the image section for a file.</p>


## -syntax

````
BOOLEAN MmFlushImageSection(
  _In_ PSECTION_OBJECT_POINTERS SectionPointer,
  _In_ MMFLUSH_TYPE             FlushType
);
````


## -parameters
<dl>

### -param <i>SectionPointer</i> [in]

<dd>
<p>Pointer to a structure that contains the file object's section object pointers.</p>
</dd>

### -param <i>FlushType</i> [in]

<dd>
<p>Specifies the reason for the flush operation. It can be one of the values listed in the following table. </p>
<table>
<tr>
<th>FlushType Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>MmFlushForDelete</b></p>
</td>
<td>
<p>The file is being deleted. </p>
</td>
</tr>
<tr>
<td>
<p><b>MmFlushForWrite</b></p>
</td>
<td>
<p>The file is being opened for write access. </p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>MmFlushImageSection</b> returns <b>TRUE</b> if the flush operation is successful, or if no image section exists for the file; otherwise <b>MmFlushImageSection</b> returns <b>FALSE</b>.</p>

## -remarks
<p>A file system must call the <b>MmFlushImageSection</b> routine before deleting a file or opening a file for write access. </p>

<p>Before deleting a file, the file system should call <b>MmFlushImageSection</b> from its IRP_MJ_SET_INFORMATION or IRP_MJ_CLEANUP dispatch routine, passing <b>MmFlushForDelete</b> for the <i>FlushType</i> parameter. </p>

<p>When opening a file for write access, the file system should call <b>MmFlushImageSection</b> from its IRP_MJ_CREATE dispatch routine, passing <b>MmFlushForWrite</b> for the <i>FlushType</i> parameter. </p>

<p>If there are no mapped views of the image section, <b>MmFlushImageSection</b> destroys the image section and returns any used pages to the free list. </p>

<p>Before using <b>MmFlushImageSection</b>, file system writers are strongly encouraged to study the way this routine is used in the FASTFAT sample. </p>

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
<a href="..\ntifs\nf-ntifs-ccpurgecachesection.md">CcPurgeCacheSection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MmFlushImageSection routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
