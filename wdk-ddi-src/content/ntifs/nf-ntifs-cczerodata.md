---
UID: NF.ntifs.CcZeroData
title: CcZeroData
author: windows-driver-content
description: The CcZeroData routine zeros the specified range of bytes in a cached or noncached file.
old-location: ifsk\cczerodata.htm
old-project: ifsk
ms.assetid: 97a0f314-5813-4ff8-8a94-c675874cdc3b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcZeroData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 and later Windows operating systems.  See Remarks for changes for Vista and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcZeroData
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
req.irql: <=APC_LEVEL
req.iface: 
---

# CcZeroData function



## -description
<p>The <b>CcZeroData</b> routine zeros the specified range of bytes in a cached or noncached file.</p>


## -syntax

````
BOOLEAN CcZeroData(
  _In_ PFILE_OBJECT   FileObject,
  _In_ PLARGE_INTEGER StartOffset,
  _In_ PLARGE_INTEGER EndOffset,
  _In_ BOOLEAN        Wait
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>A pointer to a file object (<a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a>) for the file in which a range of bytes is to be zeroed.</p>
</dd>

### -param <i>StartOffset</i> [in]

<dd>
<p>A pointer to a variable that specifies the byte offset within the file to the first byte that is to be zeroed.</p>
</dd>

### -param <i>EndOffset</i> [in]

<dd>
<p>A pointer to a variable that specifies the byte offset within the file to the last byte that is to be zeroed.</p>
</dd>

### -param <i>Wait</i> [in]

<dd>
<p>Set to <b>TRUE</b> if the caller should be put into a wait state until the entire byte range has been zeroed. Otherwise, this parameter is set to <b>FALSE</b>.</p>
</dd>
</dl>

## -returns
<p><b>CcZeroData</b> returns <b>TRUE</b> if the data is zeroed successfully; otherwise, returns <b>FALSE</b>.</p>

## -remarks
<p>The file to be zeroed can be cached or noncached. However, if the file is noncached, the values of <i>StartOffset</i> and <i>EndOffset</i> must both be multiples of the volume's sector size. (For information about how to determine sector size, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553208">Kernel-Mode Driver Architecture Design Guide</a> and <a href="kernel.kernel_mode_driver_reference">Kernel-Mode Driver Architecture Reference</a>.)</p>

<p>If a pool allocation failure occurs and <i>Wait</i> was specified as <b>TRUE</b>, <b>CcZeroData</b> raises a STATUS_INSUFFICIENT_RESOURCES exception. If a pool allocation failure occurs and <i>Wait</i> was specified as <b>FALSE</b>, <b>CcZeroData</b> returns <b>FALSE</b>, but does not raise an exception.</p>

<p>If the <i>FileObject</i> supplied does not have caching enabled, but caching exists on the stream (that is, another file object for the same file has caching enabled), then zeroing will be treated as though write-through caching is enabled.</p>

<p>If <i>Wait</i> is set to <b>TRUE</b>, <b>CcZeroData</b> is guaranteed to complete the zero data request and return <b>TRUE</b>. If the required pages of the cached file are already resident in memory, the data will be zeroed immediately and no blocking will occur. If any needed pages are not resident, the caller will be put in a wait state until all required pages have been made resident and the data can be zeroed.</p>

<p>If <i>Wait</i> is <b>FALSE</b> and if the required pages of the cached file are not already resident in memory, <b>CcZeroData</b> will refuse to block and will return <b>FALSE</b>.</p>

<p>If a pool allocation failure occurs, <b>CcZeroData</b> raises a STATUS_INSUFFICIENT_RESOURCES exception.  If <b>CcZeroData</b> encounters any other errors, including IO errors, the errors will be raised to the caller.</p>

<p>For Windows Vista and later Windows operating systems, the behavior of <b>CcZeroData</b> is as follows:</p>

<p>If the stream is cached and write_through, <i>StartOffset</i> does not have to be sector aligned.  </p>

<p>If <i>EndOffset</i> is not aligned, it will be rounded up to the next sector size.  </p>

<p>The file to be zeroed can be cached or noncached. However, if the file is noncached, the values of <i>StartOffset</i> and <i>EndOffset</i> must both be multiples of the volume's sector size. (For information about how to determine sector size, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553208">Kernel-Mode Driver Architecture Design Guide</a> and <a href="kernel.kernel_mode_driver_reference">Kernel-Mode Driver Architecture Reference</a>.)</p>

<p>If a pool allocation failure occurs and <i>Wait</i> was specified as <b>TRUE</b>, <b>CcZeroData</b> raises a STATUS_INSUFFICIENT_RESOURCES exception. If a pool allocation failure occurs and <i>Wait</i> was specified as <b>FALSE</b>, <b>CcZeroData</b> returns <b>FALSE</b>, but does not raise an exception.</p>

<p>If the <i>FileObject</i> supplied does not have caching enabled, but caching exists on the stream (that is, another file object for the same file has caching enabled), then zeroing will be treated as though write-through caching is enabled.</p>

<p>If <i>Wait</i> is set to <b>TRUE</b>, <b>CcZeroData</b> is guaranteed to complete the zero data request and return <b>TRUE</b>. If the required pages of the cached file are already resident in memory, the data will be zeroed immediately and no blocking will occur. If any needed pages are not resident, the caller will be put in a wait state until all required pages have been made resident and the data can be zeroed.</p>

<p>If <i>Wait</i> is <b>FALSE</b> and if the required pages of the cached file are not already resident in memory, <b>CcZeroData</b> will refuse to block and will return <b>FALSE</b>.</p>

<p>If a pool allocation failure occurs, <b>CcZeroData</b> raises a STATUS_INSUFFICIENT_RESOURCES exception.  If <b>CcZeroData</b> encounters any other errors, including IO errors, the errors will be raised to the caller.</p>

<p>For Windows Vista and later Windows operating systems, the behavior of <b>CcZeroData</b> is as follows:</p>

<p>If the stream is cached and write_through, <i>StartOffset</i> does not have to be sector aligned.  </p>

<p>If <i>EndOffset</i> is not aligned, it will be rounded up to the next sector size.  </p>

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
<p>Available in Microsoft Windows 2000 and later Windows operating systems.  See Remarks for changes for Vista and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Fltkernel.h or Ntifs.h)</dt>
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
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539143">CcIsFileCached</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcZeroData routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
