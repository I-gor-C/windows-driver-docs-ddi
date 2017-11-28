---
UID: NF.ntifs.RtlDecompressBufferEx
title: RtlDecompressBufferEx
author: windows-driver-content
description: The RtlDecompressBufferEx function decompresses an entire compressed buffer.
old-location: ifsk\rtldecompressbufferex.htm
old-project: ifsk
ms.assetid: 5AB55689-66F4-41BD-97B6-1E01899AFE23
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlDecompressBufferEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting in Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlDecompressBufferEx
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
req.iface: 
---

# RtlDecompressBufferEx function



## -description
<p>The <b>RtlDecompressBufferEx</b> function decompresses an entire compressed buffer.</p>


## -syntax

````
NTSTATUS RtlDecompressBufferEx(
  _In_  USHORT CompressionFormat,
  _Out_ PUCHAR UncompressedBuffer,
  _In_  ULONG  UncompressedBufferSize,
  _In_  PUCHAR CompressedBuffer,
  _In_  ULONG  CompressedBufferSize,
  _Out_ PULONG FinalUncompressedSize,
  _In_  PVOID  WorkSpace
);
````


## -parameters
<dl>

### -param <i>CompressionFormat</i> [in]

<dd>
<p>A bitmask that specifies the compression format of the compressed buffer. This parameter must be set to COMPRESSION_FORMAT_LZNT1. The meaning of this and other related compression format values are as follows.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="COMPRESSION_FORMAT_NONE"></a><a id="compression_format_none"></a><dl>

### -param <b>COMPRESSION_FORMAT_NONE</b>

</dl>
</td>
<td width="60%">
<p>Not supported by this function.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="COMPRESSION_FORMAT_DEFAULT"></a><a id="compression_format_default"></a><dl>

### -param <b>COMPRESSION_FORMAT_DEFAULT</b>

</dl>
</td>
<td width="60%">
<p>Not supported by this function.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="COMPRESSION_FORMAT_LZNT1"></a><a id="compression_format_lznt1"></a><dl>

### -param <b>COMPRESSION_FORMAT_LZNT1</b>

</dl>
</td>
<td width="60%">
<p>The function will perform LZ decompression.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="COMPRESSION_FORMAT_XPRESS"></a><a id="compression_format_xpress"></a><dl>

### -param <b>COMPRESSION_FORMAT_XPRESS</b>

</dl>
</td>
<td width="60%">
<p>The function will perform Xpress decompression.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="COMPRESSION_FORMAT_XPRESS_HUFF"></a><a id="compression_format_xpress_huff"></a><dl>

### -param <b>COMPRESSION_FORMAT_XPRESS_HUFF</b>

</dl>
</td>
<td width="60%">
<p>The function will perform Xpress Huffman decompression.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>UncompressedBuffer</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer (allocated from paged or non-paged pool) that receives the decompressed data from <i>CompressedBuffer</i>. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>UncompressedBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the <i>UncompressedBuffer</i>buffer.</p>
</dd>

### -param <i>CompressedBuffer</i> [in]

<dd>
<p>A pointer to the buffer that contains the data to decompress. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>CompressedBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the <i>CompressedBuffer</i> buffer.</p>
</dd>

### -param <i>FinalUncompressedSize</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives the size, in bytes, of the decompressed data stored in <i>UncompressedBuffer</i>. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>WorkSpace</i> [in]

<dd>
<p>A pointer to a caller-allocated work space buffer used by the <b>RtlDecompressBufferEx</b> function during decompression. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552291">RtlGetCompressionWorkSpaceSize</a> function to determine the correct work space buffer size.</p>
</dd>
</dl>

## -returns
<p><b>RtlDecompressBufferEx</b> returns an appropriate error status value, such as one of the following.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The <i>CompressedBuffer</i> buffer was successfully decompressed.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid compression format was specified through the <i>CompressionFormat</i> parameter. If <i>CompressionFormat</i> is either COMPRESSION_FORMAT_NONE or COMPRESSION_FORMAT_DEFAULT (but not both), this value is returned.</p><dl>
<dt><b>STATUS_UNSUPPORTED_COMPRESSION</b></dt>
</dl><p>An invalid compression format was specified through the <i>CompressionFormat</i> parameter. If <i>CompressionFormat</i> is not one of the following, STATUS_UNSUPPORTED_COMPRESSION is returned:</p>

<p> COMPRESSION_FORMAT_LZNT1</p>

<p> COMPRESSION_FORMAT_XPRESS</p>

<p> COMPRESSION_FORMAT_XPRESS_HUFF</p>

<p> COMPRESSION_FORMAT_NONE (in this case, STATUS_INVALID_PARAMETER is returned).</p>

<p> COMPRESSION_FORMAT_DEFAULT (in this case, STATUS_INVALID_PARAMETER is returned).</p><dl>
<dt><b>STATUS_BAD_COMPRESSION_BUFFER</b></dt>
</dl><p><i>UncompressedBuffer</i> is not large enough to contain the uncompressed data.</p>

<p> </p>

## -remarks
<p>The <b>RtlDecompressBufferEx</b> function takes as input an entire compressed buffer and produces its decompressed equivalent provided that the uncompressed data fits within the specified destination buffer.</p>

<p>To decompress only a portion of a compressed buffer (that is, a "fragment" of the buffer), use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552197">RtlDecompressFragment</a> function.</p>

<p>To compress an uncompressed buffer, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552127">RtlCompressBuffer</a> function.</p>

<p>The <b>RtlDecompressBufferEx</b> function takes as input an entire compressed buffer and produces its decompressed equivalent provided that the uncompressed data fits within the specified destination buffer.</p>

<p>To decompress only a portion of a compressed buffer (that is, a "fragment" of the buffer), use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552197">RtlDecompressFragment</a> function.</p>

<p>To compress an uncompressed buffer, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552127">RtlCompressBuffer</a> function.</p>

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
<p>Available in starting in Windows 8.</p>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540239">FILE_COMPRESSION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552127">RtlCompressBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552191">RtlDecompressBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt426737">RtlDecompressBufferEx2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552197">RtlDecompressFragment</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt426738">RtlDecompressFragmentEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlDecompressBufferEx function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
