---
UID: NF.ntifs.CcSetFileSizes
title: CcSetFileSizes
author: windows-driver-content
description: The CcSetFileSizes routine updates the cache maps and section object for a cached file whose size has changed.
old-location: ifsk\ccsetfilesizes.htm
old-project: ifsk
ms.assetid: 1fc92167-ceab-4f8e-bd80-a8f1821846ed
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcSetFileSizes
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
req.alt-api: CcSetFileSizes
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

# CcSetFileSizes function



## -description
<p>The <b>CcSetFileSizes</b> routine updates the cache maps and section object for a cached file whose size has changed.</p>


## -syntax

````
VOID CcSetFileSizes(
  _In_ PFILE_OBJECT   FileObject,
  _In_ PCC_FILE_SIZES FileSizes
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to a file object for the cached file.</p>
</dd>

### -param <i>FileSizes</i> [in]

<dd>
<p>Pointer to a CC_FILE_SIZES structure containing <b>AllocationSize</b>, <b>FileSize</b> and <b>ValidDataLength</b> for the file. This structure is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _CC_FILE_SIZES {
    LARGE_INTEGER AllocationSize;
    LARGE_INTEGER FileSize;
    LARGE_INTEGER ValidDataLength;
} CC_FILE_SIZES, *PCC_FILE_SIZES;</pre>
</td>
</tr>
</table></span></div>
<table>
<tr>
<th>Member</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>AllocationSize</b></p>
</td>
<td>
<p>New section object size for the file. </p>
</td>
</tr>
<tr>
<td>
<p><b>FileSize</b></p>
</td>
<td>
<p>New file size for the file.</p>
</td>
</tr>
<tr>
<td>
<p><b>ValidDataLength</b></p>
</td>
<td>
<p>New valid data length for the file.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>File systems must call <b>CcSetFileSizes</b> to update the cache manager data structures whenever one of the following changes is made to a cached file:</p>

<p>Its allocation size is increased.</p>

<p>Its valid data length is decreased.</p>

<p>Its valid data length is increased by a non-cached I/O operation.</p>

<p>Its file size is increased or decreased.</p>

<p>If any failure occurs, <b>CcSetFileSizes</b> raises a status exception for that particular failure. For example, if a pool allocation failure occurs, <b>CcSetFileSizes</b> raises a STATUS_INSUFFICIENT_RESOURCES exception. Therefore, to gain control if a failure occurs, the driver should wrap the call to <b>CcSetFileSizes</b> in a <b>try-except</b> or <b>try-finally</b> statement.</p>

<p>To cache a file, use <a href="..\ntifs\nf-ntifs-ccinitializecachemap.md">CcInitializeCacheMap</a>.</p>

<p>The <b>CcGetFileSizePointer</b> macro returns the size of a file, given a pointer to a file object for the file.</p>

<p>Parameters</p>

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
<a href="..\ntifs\nf-ntifs-ccinitializecachemap.md">CcInitializeCacheMap</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcSetFileSizes routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
