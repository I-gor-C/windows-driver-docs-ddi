---
UID: NF.fltkernel.FltAllocatePoolAlignedWithTag
title: FltAllocatePoolAlignedWithTag
author: windows-driver-content
description: FltAllocatePoolAlignedWithTag allocates a device-aligned buffer for use in a noncached I/O operation.
old-location: ifsk\fltallocatepoolalignedwithtag.htm
ms.assetid: ffb1493f-6076-4b93-8431-b3ffd4679f96
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltAllocatePoolAlignedWithTag
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL (see Remarks section)
ms.keywords: FltAllocatePoolAlignedWithTag
req.iface: 
---

# FltAllocatePoolAlignedWithTag function



## -description
<p><b>FltAllocatePoolAlignedWithTag</b> allocates a device-aligned buffer for use in a noncached I/O operation. </p>


## -syntax

````
PVOID FltAllocatePoolAlignedWithTag(
  _In_ PFLT_INSTANCE Instance,
  _In_ POOL_TYPE     PoolType,
  _In_ SIZE_T        NumberOfBytes,
  _In_ ULONG         Tag
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for a caller-owned minifilter driver instance that is attached to the volume. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>Type of pool to allocate. One of the following: </p>
<p><b>NonPagedPool</b></p>
<p><b>PagedPool</b></p>
<p><b>NonPagedPoolCacheAligned</b></p>
<p><b>PagedPoolCacheAligned</b></p>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a> for a description of the available pool memory types. </p>
</dd>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>Number of bytes to allocate. This parameter is required and can be zero. </p>
</dd>

### -param <i>Tag</i> [in]

<dd>
<p>Specifies the pool tag for the allocated memory. Drivers normally specify the pool tag as a string of one to four 7-bit ASCII characters, delimited by single quotation marks (for example, 'abcd'). This parameter is required and cannot be zero. </p>
</dd>
</dl>

## -returns
<p>If not enough free pool is available to satisfy the request, <b>FltAllocatePoolAlignedWithTag</b> returns a <b>NULL</b> pointer. Otherwise, <b>FltAllocatePoolAlignedWithTag</b> returns a pointer to the newly allocated buffer. </p>

## -remarks
<p><b>FltAllocatePoolAlignedWithTag</b> allocates a buffer that is aligned in accordance with the underlying device for the given volume. Such device-aligned buffers are required for noncached I/O. (They can also be used for cached I/O.) Thus when calling routines that perform noncached I/O, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a>, minifilter drivers should call <b>FltAllocatePoolAlignedWithTag</b> instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a>. </p>

<p>If the caller specifies a value of zero for the <i>NumberOfBytes</i> parameter, <b>FltAllocatePoolAlignedWithTag</b> allocates the smallest amount of memory that meets the alignment requirement. </p>

<p>The system associates the pool tag specified by the <i>Tag</i> parameter with the allocated buffer. Programming tools, such as the Windows Debugger (WinDbg), can display the pool tag associated with each allocated buffer. The value of the pool tag is normally displayed in reversed order. For example, if a caller passes 'Fred' as the value of the <i>Tag</i> parameter, this value would appear as 'derF' if pool is dumped or when tracking pool usage in the debugger. </p>

<p>For more information about memory management, see <a href="https://msdn.microsoft.com/e030a37c-26ab-4177-9980-4336928975e1">Memory Management</a>. </p>

<p>When the buffer that <b>FltAllocatePoolAlignedWithTag</b> allocates is no longer needed, the caller is responsible for freeing it by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff542979">FltFreePoolAlignedWithTag</a>. </p>

<p>Callers of <b>FltAllocatePoolAlignedWithTag</b> can be running at IRQL DISPATCH_LEVEL only if a NonPaged<i>XxxPoolType</i> is specified. Otherwise, callers must be running at IRQL &lt;= APC_LEVEL. </p>

<p><b>FltAllocatePoolAlignedWithTag</b> allocates a buffer that is aligned in accordance with the underlying device for the given volume. Such device-aligned buffers are required for noncached I/O. (They can also be used for cached I/O.) Thus when calling routines that perform noncached I/O, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a>, minifilter drivers should call <b>FltAllocatePoolAlignedWithTag</b> instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a>. </p>

<p>If the caller specifies a value of zero for the <i>NumberOfBytes</i> parameter, <b>FltAllocatePoolAlignedWithTag</b> allocates the smallest amount of memory that meets the alignment requirement. </p>

<p>The system associates the pool tag specified by the <i>Tag</i> parameter with the allocated buffer. Programming tools, such as the Windows Debugger (WinDbg), can display the pool tag associated with each allocated buffer. The value of the pool tag is normally displayed in reversed order. For example, if a caller passes 'Fred' as the value of the <i>Tag</i> parameter, this value would appear as 'derF' if pool is dumped or when tracking pool usage in the debugger. </p>

<p>For more information about memory management, see <a href="https://msdn.microsoft.com/e030a37c-26ab-4177-9980-4336928975e1">Memory Management</a>. </p>

<p>When the buffer that <b>FltAllocatePoolAlignedWithTag</b> allocates is no longer needed, the caller is responsible for freeing it by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff542979">FltFreePoolAlignedWithTag</a>. </p>

<p>Callers of <b>FltAllocatePoolAlignedWithTag</b> can be running at IRQL DISPATCH_LEVEL only if a NonPaged<i>XxxPoolType</i> is specified. Otherwise, callers must be running at IRQL &lt;= APC_LEVEL. </p>

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
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542979">FltFreePoolAlignedWithTag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544610">FltWriteFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltAllocatePoolAlignedWithTag function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
