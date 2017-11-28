---
UID: NF.ntifs.RtlCompressBuffer
title: RtlCompressBuffer
author: windows-driver-content
description: The RtlCompressBuffer function compresses a buffer and can be used by a file system driver to facilitate the implementation of file compression.
old-location: ifsk\rtlcompressbuffer.htm
old-project: ifsk
ms.assetid: 49fb1062-9709-4691-9655-8cbf3c5055fb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlCompressBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlCompressBuffer
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

# RtlCompressBuffer function



## -description
<p>The <b>RtlCompressBuffer</b> function compresses a buffer and can be used by a file system driver to facilitate the implementation of file compression.</p>


## -syntax

````
NTSTATUS RtlCompressBuffer(
  _In_  USHORT CompressionFormatAndEngine,
  _In_  PUCHAR UncompressedBuffer,
  _In_  ULONG  UncompressedBufferSize,
  _Out_ PUCHAR CompressedBuffer,
  _In_  ULONG  CompressedBufferSize,
  _In_  ULONG  UncompressedChunkSize,
  _Out_ PULONG FinalCompressedSize,
  _In_  PVOID  WorkSpace
);
````


## -parameters
<dl>

### -param <i>CompressionFormatAndEngine</i> [in]

<dd>
<p>A bitmask that specifies the compression format and engine type. This parameter must be set to  a  valid bitwise OR combination of one format type and one engine type. For example, COMPRESSION_FORMAT_LZNT1 | COMPRESSION_ENGINE_STANDARD.</p>
<p>The meanings of these, and other related values, are as follows.</p>
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
<p>The function will perform LZ compression.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="COMPRESSION_FORMAT_XPRESS"></a><a id="compression_format_xpress"></a><dl>

### -param <b>COMPRESSION_FORMAT_XPRESS</b>

</dl>
</td>
<td width="60%">
<p>The function will perform Xpress compression.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="COMPRESSION_FORMAT_XPRESS_HUFF"></a><a id="compression_format_xpress_huff"></a><dl>

### -param <b>COMPRESSION_FORMAT_XPRESS_HUFF</b>

</dl>
</td>
<td width="60%">
<p>The function will perform Xpress Huffman compression.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="COMPRESSION_ENGINE_STANDARD"></a><a id="compression_engine_standard"></a><dl>

### -param <b>COMPRESSION_ENGINE_STANDARD</b>

</dl>
</td>
<td width="60%">
<p>The <i>UncompressedBuffer</i> buffer is compressed using an algorithm that provides a balance between data compression and performance. This value cannot be used with COMPRESSION_ENGINE_MAXIMUM.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="COMPRESSION_ENGINE_MAXIMUM"></a><a id="compression_engine_maximum"></a><dl>

### -param <b>COMPRESSION_ENGINE_MAXIMUM</b>

</dl>
</td>
<td width="60%">
<p>The <i>UncompressedBuffer</i> buffer is compressed using an algorithm that provides maximum data compression but with relatively slower performance. This value cannot be used with COMPRESSION_ENGINE_STANDARD.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="COMPRESSION_ENGINE_HIBER"></a><a id="compression_engine_hiber"></a><dl>

### -param <b>COMPRESSION_ENGINE_HIBER</b>

</dl>
</td>
<td width="60%">
<p>Not supported by this function.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>UncompressedBuffer</i> [in]

<dd>
<p>A pointer to a caller-allocated buffer (allocated from paged or non-paged pool) that contains the data to be compressed. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>UncompressedBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the <i>UncompressedBuffer</i> buffer.</p>
</dd>

### -param <i>CompressedBuffer</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer (allocated from paged or non-paged pool) that receives the compressed data. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>CompressedBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the <i>CompressedBuffer</i> buffer.</p>
</dd>

### -param <i>UncompressedChunkSize</i> [in]

<dd>
<p>The chunk size to use when compressing the <i>UncompressedBuffer</i> buffer. This parameter must be one of the following values:  512, 1024, 2048, or 4096. The operating system uses 4096, and the recommended value for this parameter is also 4096.</p>
</dd>

### -param <i>FinalCompressedSize</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives the size, in bytes, of the compressed data stored in <i>CompressedBuffer</i>. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>WorkSpace</i> [in]

<dd>
<p>A pointer to a caller-allocated work space buffer used by the <b>RtlCompressBuffer</b> function during compression. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552291">RtlGetCompressionWorkSpaceSize</a> function to determine the correct work space buffer size.</p>
</dd>
</dl>

## -returns
<p><b>RtlCompressBuffer</b> returns an appropriate error status value, such as one of the following.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The <i>UncompressedBuffer</i> buffer was successfully compressed.</p><dl>
<dt><b>STATUS_BUFFER_ALL_ZEROS</b></dt>
</dl><p>The <i>UncompressedBuffer</i> buffer was successfully compressed, but this buffer contains only zeros.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><dl>
<dt><b>STATUS_UNSUPPORTED_COMPRESSION</b></dt>
</dl><p>COMPRESSION_FORMAT_LZNT1</p>

<p> COMPRESSION_FORMAT_XPRESS</p>

<p> COMPRESSION_FORMAT_XPRESS_HUFF</p>

<p>COMPRESSION_FORMAT_NONE (in this case, STATUS_INVALID_PARAMETER is returned)</p>

<p>COMPRESSION_FORMAT_DEFAULT (in this case, STATUS_INVALID_PARAMETER is returned)</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>An invalid compression engine was specified through the <i>CompressionFormatAndEngine</i> parameter. If <i>CompressionFormatAndEngine</i> is not COMPRESSION_ENGINE_STANDARD or COMPRESSION_ENGINE_MAXIMUM (but not both), this value is returned.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The compressed buffer is too small to hold the compressed data. That is, <i>FinalCompressedSize</i> is greater than <i>CompressedBufferSize</i>.</p>

<p> </p>

## -remarks
<p>The <b>RtlCompressBuffer</b> function takes as input an uncompressed buffer and produces its compressed equivalent provided that the compressed data fits within the specified destination buffer.</p>

<p>To determine the correct buffer size for the <i>WorkSpace</i> parameter, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552291">RtlGetCompressionWorkSpaceSize</a> function.</p>

<p>To decompress a compressed buffer, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552191">RtlDecompressBuffer</a> function.</p>

<p>To extract an uncompressed fragment from a compressed buffer, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552197">RtlDecompressFragment</a> function.</p>

<p>The <b>RtlCompressBuffer</b> function takes as input an uncompressed buffer and produces its compressed equivalent provided that the compressed data fits within the specified destination buffer.</p>

<p>To determine the correct buffer size for the <i>WorkSpace</i> parameter, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552291">RtlGetCompressionWorkSpaceSize</a> function.</p>

<p>To decompress a compressed buffer, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552191">RtlDecompressBuffer</a> function.</p>

<p>To extract an uncompressed fragment from a compressed buffer, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552197">RtlDecompressFragment</a> function.</p>

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
<p>Available starting in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552191">RtlDecompressBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552197">RtlDecompressFragment</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552291">RtlGetCompressionWorkSpaceSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlCompressBuffer function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
