---
UID: NF.ntifs.RtlGetCompressionWorkSpaceSize
title: RtlGetCompressionWorkSpaceSize
author: windows-driver-content
description: The RtlGetCompressionWorkSpaceSize function is used to determine the correct size of the WorkSpace buffer for the RtlCompressBuffer and RtlDecompressFragment functions.
old-location: ifsk\rtlgetcompressionworkspacesize.htm
old-project: ifsk
ms.assetid: f0e856f8-9c01-4219-b521-ab4a5c9bc35c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlGetCompressionWorkSpaceSize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and all later versions of Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlGetCompressionWorkSpaceSize
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

# RtlGetCompressionWorkSpaceSize function



## -description
<p>The <b>RtlGetCompressionWorkSpaceSize</b> function is used to determine the correct size of the <i>WorkSpace</i> buffer for the <a href="..\ntifs\nf-ntifs-rtlcompressbuffer.md">RtlCompressBuffer</a> and <a href="..\ntifs\nf-ntifs-rtldecompressfragment.md">RtlDecompressFragment</a> functions.</p>


## -syntax

````
NTSTATUS RtlGetCompressionWorkSpaceSize(
  _In_  USHORT CompressionFormatAndEngine,
  _Out_ PULONG CompressBufferWorkSpaceSize,
  _Out_ PULONG CompressFragmentWorkSpaceSize
);
````


## -parameters
<dl>

### -param <i>CompressionFormatAndEngine</i> [in]

<dd>
<p>Bitmask specifying the compression format and engine type. This parameter must be set to one of the following bitwise OR combinations:</p>
<ul>
<li>
<p>COMPRESSION_FORMAT_LZNT1 | COMPRESSION_ENGINE_STANDARD</p>
</li>
<li>
<p>COMPRESSION_FORMAT_LZNT1 | COMPRESSION_ENGINE_MAXIMUM</p>
</li>
</ul>
<p>The meanings of these, and other related values, are as follows:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>COMPRESSION_FORMAT_NONE</p>
</td>
<td>
<p>Not supported by this function.</p>
</td>
</tr>
<tr>
<td>
<p>COMPRESSION_FORMAT_DEFAULT</p>
</td>
<td>
<p>Not supported by this function.</p>
</td>
</tr>
<tr>
<td>
<p>COMPRESSION_FORMAT_LZNT1</p>
</td>
<td>
<p>Specifies that compression should be performed. This value is required.</p>
</td>
</tr>
<tr>
<td>
<p>COMPRESSION_ENGINE_STANDARD</p>
</td>
<td>
<p>Data is compressed using an algorithm which provides a balance between data compression and performance. This value cannot be used with COMPRESSION_ENGINE_MAXIMUM.</p>
</td>
</tr>
<tr>
<td>
<p>COMPRESSION_ENGINE_MAXIMUM</p>
</td>
<td>
<p>Data is compressed using an algorithm which provides maximum data compression but with relatively slower performance. This value cannot be used with COMPRESSION_ENGINE_STANDARD.</p>
</td>
</tr>
<tr>
<td>
<p>COMPRESSION_ENGINE_HIBER</p>
</td>
<td>
<p>Not supported by this function.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>CompressBufferWorkSpaceSize</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer receiving the size, in bytes, required to compress a buffer. This value is used to determine the correct size of <a href="..\ntifs\nf-ntifs-rtlcompressbuffer.md">RtlCompressBuffer</a>'s <i>WorkSpace</i> buffer.</p>
</dd>

### -param <i>CompressFragmentWorkSpaceSize</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer receiving the size, in bytes, required to decompress a compressed buffer to a fragment. This value is used to determine the correct size of <a href="..\ntifs\nf-ntifs-rtldecompressfragment.md">RtlDecompressFragment</a>'s <i>WorkSpace</i> buffer. Note that the <b>RtlCompressFragment</b> function does not currently exist.</p>
</dd>
</dl>

## -returns
<p><b>RtlGetCompressionWorkSpaceSize</b>returns an appropriate error status, such as one of the following:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The required buffer sizes, in bytes, were successfully returned.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid compression format was specified via the <i>CompressionFormatAndEngine</i> parameter. If <i>CompressionFormatAndEngine</i> is either COMPRESSION_FORMAT_NONE or COMPRESSION_FORMAT_DEFAULT (but not both), this value is returned.</p><dl>
<dt><b>STATUS_UNSUPPORTED_COMPRESSION</b></dt>
</dl><p>An invalid compression format was specified via the <i>CompressionFormatAndEngine</i> parameter. If <i>CompressionFormatAndEngine</i> is not one of the following, STATUS_UNSUPPORTED_COMPRESSION is returned:

</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>An invalid compression engine was specified via the <i>CompressionFormatAndEngine</i> parameter. If <i>CompressionFormatAndEngine</i> is not COMPRESSION_ENGINE_STANDARD or COMPRESSION_ENGINE_MAXIMUM (but not both), this value is returned.</p>

<p> </p>

## -remarks
<p>The <a href="..\ntifs\nf-ntifs-rtlcompressbuffer.md">RtlCompressBuffer</a> and <a href="..\ntifs\nf-ntifs-rtldecompressfragment.md">RtlDecompressFragment</a>functions require an appropriately sized work space buffer to compress and decompress successfully. To determine the correct work space buffer size, in bytes, call the <b>RtlGetCompressionWorkSpaceSize</b> function. </p>

<p>As an example, the <i>WorkSpace</i> parameter of the <a href="..\ntifs\nf-ntifs-rtlcompressbuffer.md">RtlCompressBuffer</a> function must point to an adequately sized work space buffer. The <i>CompressBufferWorkSpaceSize</i> parameter of the <b>RtlGetCompressionWorkSpaceSize</b> provides this size.</p>

<p>To compress an uncompressed buffer, use the <a href="..\ntifs\nf-ntifs-rtlcompressbuffer.md">RtlCompressBuffer</a> function.</p>

<p>To decompress a compressed buffer, use the <a href="..\ntifs\nf-ntifs-rtldecompressbuffer.md">RtlDecompressBuffer</a> function.</p>

<p>To decompress only a portion of a compressed buffer (that is, a "fragment" of the buffer), use the <a href="..\ntifs\nf-ntifs-rtldecompressfragment.md">RtlDecompressFragment</a> function.</p>

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
<p>Available in Windows XP and all later versions of Windows operating systems.</p>
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
<a href="..\ntifs\ns-ntifs--file-compression-information.md">FILE_COMPRESSION_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtlcompressbuffer.md">RtlCompressBuffer</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtldecompressbuffer.md">RtlDecompressBuffer</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtldecompressfragment.md">RtlDecompressFragment</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlGetCompressionWorkSpaceSize function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
