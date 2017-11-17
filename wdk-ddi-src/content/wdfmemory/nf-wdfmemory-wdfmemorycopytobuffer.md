---
UID: NF.wdfmemory.WdfMemoryCopyToBuffer
title: WdfMemoryCopyToBuffer
author: windows-driver-content
description: The WdfMemoryCopyToBuffer method copies the contents of a specified memory object's buffer into a specified destination buffer.
old-location: wdf\wdfmemorycopytobuffer.htm
ms.assetid: cb1fc590-3d3a-4b06-b467-28c3adb43706
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfmemory.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfMemoryCopyToBuffer
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctlA, BufAfterReqCompletedReadA, BufAfterReqCompletedWriteA, DriverCreate, MemAfterReqCompletedIntIoctlA, MemAfterReqCompletedIoctlA, MemAfterReqCompletedReadA, MemAfterReqCompletedWriteA
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: Any level (see Remarks section)
ms.keywords: WdfMemoryCopyToBuffer
req.iface: 
req.product: Windows 10 or later.
---

# WdfMemoryCopyToBuffer function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfMemoryCopyToBuffer</b> method copies the contents of a specified memory object's buffer into a specified destination buffer.</p>


## -syntax

````
NTSTATUS WdfMemoryCopyToBuffer(
  _In_  WDFMEMORY SourceMemory,
  _In_  size_t    SourceOffset,
  _Out_ PVOID     Buffer,
  _In_  size_t    NumBytesToCopyTo
);
````


## -parameters
<dl>

### -param <i>SourceMemory</i> [in]

<dd>
<p>A handle to a framework memory object that represents the source buffer.</p>
</dd>

### -param <i>SourceOffset</i> [in]

<dd>
<p>An offset, in bytes, from the beginning of the source buffer. The copy operation begins at the specified offset in the source buffer.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to a destination buffer.</p>
</dd>

### -param <i>NumBytesToCopyTo</i> [in]

<dd>
<p>The number of bytes to copy from the source buffer to the destination buffer. This value must not be greater than the size of the source buffer.</p>
</dd>
</dl>

## -returns
<p><b>WdfMemoryCopyToBuffer</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The byte offset that the <i>SourceOffset</i> parameter specified was too large, or the <i>NumBytesToCopyTo</i> parameter was greater than the size of the source buffer.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>The framework does not allow the driver to copy more bytes than the source buffer that the <i>SourceMemory</i> parameter specifies can contain. </p>

<p>For more information about framework memory objects, see <a href="wdf.using_memory_buffers">Using Memory Buffers</a>.</p>

<p>If the source or destination buffer was allocated from the pageable memory pool, the <b>WdfMemoryCopyToBuffer</b> method must be called at IRQL &lt;= APC_LEVEL. Otherwise, the method can be called at any IRQL.</p>

<p>The following code example allocates a new buffer and copies the contents of a memory object's buffer into the new buffer.</p>

<p>The framework does not allow the driver to copy more bytes than the source buffer that the <i>SourceMemory</i> parameter specifies can contain. </p>

<p>For more information about framework memory objects, see <a href="wdf.using_memory_buffers">Using Memory Buffers</a>.</p>

<p>If the source or destination buffer was allocated from the pageable memory pool, the <b>WdfMemoryCopyToBuffer</b> method must be called at IRQL &lt;= APC_LEVEL. Otherwise, the method can be called at any IRQL.</p>

<p>The following code example allocates a new buffer and copies the contents of a memory object's buffer into the new buffer.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfmemory.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level (see Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975066">BufAfterReqCompletedIntIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542318">BufAfterReqCompletedIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542328">BufAfterReqCompletedReadA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542340">BufAfterReqCompletedWriteA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549090">MemAfterReqCompletedIntIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549106">MemAfterReqCompletedIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549116">MemAfterReqCompletedReadA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549125">MemAfterReqCompletedWriteA</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548701">WdfMemoryCopyFromBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfMemoryCopyToBuffer method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
