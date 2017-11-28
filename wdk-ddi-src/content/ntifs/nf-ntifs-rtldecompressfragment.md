---
UID: NF.ntifs.RtlDecompressFragment
title: RtlDecompressFragment
author: windows-driver-content
description: The RtlDecompressFragment function is used to decompress part of a compressed buffer (that is, a buffer &#0034;fragment&#0034;).
old-location: ifsk\rtldecompressfragment.htm
old-project: ifsk
ms.assetid: 80450bfb-ae3a-46cd-8cf2-905df5adf70d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlDecompressFragment
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of all Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlDecompressFragment
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

# RtlDecompressFragment function



## -description
<p>The <b>RtlDecompressFragment</b> function is used to decompress part of a compressed buffer (that is, a buffer "fragment").</p>


## -syntax

````
NTSTATUS RtlDecompressFragment(
  _In_  USHORT CompressionFormat,
  _Out_ PUCHAR UncompressedFragment,
  _In_  ULONG  UncompressedFragmentSize,
  _In_  PUCHAR CompressedBuffer,
  _In_  ULONG  CompressedBufferSize,
  _In_  ULONG  FragmentOffset,
  _Out_ PULONG FinalUncompressedSize,
  _In_  PVOID  WorkSpace
);
````


## -parameters
<dl>

### -param <i>CompressionFormat</i> [in]

<dd>
<p>Bitmask specifying the compression format of the compressed buffer. This parameter must be set to COMPRESSION_FORMAT_LZNT1. The meaning of this and other related compression format values are as follows:</p>
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
</table>
<p> </p>
</dd>

### -param <i>UncompressedFragment</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer (allocated from paged or non-paged pool) receiving the decompressed data from <i>CompressedBuffer</i>. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>UncompressedFragmentSize</i> [in]

<dd>
<p>The size, in bytes, of the <i>UncompressedFragment</i> buffer.</p>
</dd>

### -param <i>CompressedBuffer</i> [in]

<dd>
<p>A pointer to the buffer containing the data to decompress. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>CompressedBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the <i>CompressedBuffer</i> buffer.</p>
</dd>

### -param <i>FragmentOffset</i> [in]

<dd>
<p>The zero-based offset, in bytes, where the uncompressed fragment is being extract from. This offset value is the position within the original uncompressed buffer.</p>
</dd>

### -param <i>FinalUncompressedSize</i> [out]

<dd>
<p>A pointer to a caller-allocated variable which receives the size, in bytes, of the decompressed data stored in <i>UncompressedFragment</i>. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param <i>WorkSpace</i> [in]

<dd>
<p>A pointer to a caller-allocated work space buffer used by the <b>RtlDecompressFragment</b> function during decompression. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552291">RtlGetCompressionWorkSpaceSize</a> function to determine the correct work space buffer size.</p>
</dd>
</dl>

## -returns
<p><b>RtlDecompressFragment</b>returns an appropriate error status, such as one of the following:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The <i>CompressedBuffer</i> buffer was successfully decompressed into <i>UncompressedFragment</i>.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid compression format was specified via the <i>CompressionFormat</i> parameter. If <i>CompressionFormat</i> is either COMPRESSION_FORMAT_NONE or COMPRESSION_FORMAT_DEFAULT (but not both), this value is returned.</p><dl>
<dt><b>STATUS_UNSUPPORTED_COMPRESSION</b></dt>
</dl><p>An invalid compression format was specified via the <i>CompressionFormat</i> parameter. If <i>CompressionFormat</i> is not one of the following, STATUS_UNSUPPORTED_COMPRESSION is returned:</p><dl>
<dt><b>STATUS_BAD_COMPRESSION_BUFFER</b></dt>
</dl><p><i>UncompressedFragment</i> is not large enough to contain the uncompressed data.</p>

<p> </p>

## -remarks
<p>Relative to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552191">RtlDecompressBuffer</a> function, <b>RtlDecompressFragment</b> is used for decompressing a portion of the data from a compressed buffer (as opposed to the entire buffer). </p>

<p>To determine the correct buffer size for the <i>WorkSpace</i> parameter, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552291">RtlGetCompressionWorkSpaceSize</a> function (that is, the value returned by the <b>RtlGetCompressionWorkSpaceSize</b> parameter).</p>

<p>To compress an uncompressed buffer, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552127">RtlCompressBuffer</a> function.</p>

<p>To decompress an entire compressed buffer, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552191">RtlDecompressBuffer</a> function.</p>

<p>Relative to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552191">RtlDecompressBuffer</a> function, <b>RtlDecompressFragment</b> is used for decompressing a portion of the data from a compressed buffer (as opposed to the entire buffer). </p>

<p>To determine the correct buffer size for the <i>WorkSpace</i> parameter, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552291">RtlGetCompressionWorkSpaceSize</a> function (that is, the value returned by the <b>RtlGetCompressionWorkSpaceSize</b> parameter).</p>

<p>To compress an uncompressed buffer, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552127">RtlCompressBuffer</a> function.</p>

<p>To decompress an entire compressed buffer, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552191">RtlDecompressBuffer</a> function.</p>

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
<p>Available in Windows XP and later versions of all Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439511">RtlDecompressBufferEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt426737">RtlDecompressBufferEx2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt426738">RtlDecompressFragmentEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlDecompressFragment function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
