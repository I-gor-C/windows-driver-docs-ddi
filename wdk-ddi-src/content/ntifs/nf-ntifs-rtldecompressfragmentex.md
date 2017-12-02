---
UID: NF.ntifs.RtlDecompressFragmentEx
title: RtlDecompressFragmentEx
author: windows-driver-content
description: The RtlDecompressFragmentEx function is used to decompress part of a compressed buffer (that is, a buffer &#0034;fragment&#0034;), using multiple processors where possible.
old-location: ifsk\rtldecompressfragmentex.htm
old-project: ifsk
ms.assetid: A4FE108D-85CE-4F6A-A17A-E81684764FD3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlDecompressFragmentEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting in Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlDecompressFragmentEx
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

# RtlDecompressFragmentEx function



## -description
<p>The <b>RtlDecompressFragmentEx</b> function is used to decompress part of a compressed buffer (that is, a buffer "fragment"), using multiple processors where possible.</p>


## -syntax

````
NTSTATUS RtlDecompressFragmentEx(
  _In_  ULONG  CompressionFormat,
  _Out_ PUCHAR UncompressedFragment,
  _In_  ULONG  UncompressedFragmentSize,
  _In_  PUCHAR CompressedBuffer,
  _In_  ULONG  CompressedBufferSize,
  _In_  ULONG  FragmentOffset,
  _In_  ULONG  UncompressedChunkSize,
  _Out_ PULONG FinalUncompressedSize,
  _In_  PVOID  WorkSpace
);
````


## -parameters
<dl>

### -param CompressionFormat [in]

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

### -param UncompressedFragment [out]

<dd>
<p>Pointer to a caller-allocated buffer (allocated from paged or non-paged pool) receiving the decompressed data from <i>CompressedBuffer</i>. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param UncompressedFragmentSize [in]

<dd>
<p>The size, in bytes, of the <i>UncompressedFragment</i> buffer.</p>
</dd>

### -param CompressedBuffer [in]

<dd>
<p>A pointer to the buffer containing the data to decompress. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param CompressedBufferSize [in]

<dd>
<p>The size, in bytes, of the <i>CompressedBuffer</i> buffer.</p>
</dd>

### -param FragmentOffset [in]

<dd>
<p>The zero-based offset, in bytes, where the uncompressed fragment is being extract from. This offset value is the position within the original uncompressed buffer.</p>
</dd>

### -param UncompressedChunkSize [in]

<dd>
<p>The size, in bytes, of each chunk within the compression buffer.  Valid values are 512, 1024, 2048 and 4096.</p>
</dd>

### -param FinalUncompressedSize [out]

<dd>
<p>A pointer to a caller-allocated variable which receives the size, in bytes, of the decompressed data stored in <i>UncompressedFragment</i>. This parameter is required and cannot be <b>NULL</b>.</p>
</dd>

### -param WorkSpace [in]

<dd>
<p>A pointer to a caller-allocated work space buffer used by the <b>RtlDecompressFragmentEx</b> function during decompression. Use the <a href="..\ntifs\nf-ntifs-rtlgetcompressionworkspacesize.md">RtlGetCompressionWorkSpaceSize</a> function to determine the correct work space buffer size.</p>
</dd>
</dl>

## -returns
<p>
<a href="..\ntifs\nf-ntifs-rtldecompressfragment.md">RtlDecompressFragment</a>returns an appropriate error status, such as one of the following:</p><dl>
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
<p>Available in starting in Windows 10.</p>
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
<a href="..\ntifs\nf-ntifs-rtldecompressbufferex.md">RtlDecompressBufferEx</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtldecompressbufferex2.md">RtlDecompressBufferEx2</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-rtldecompressfragment.md">RtlDecompressFragment</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlDecompressFragmentEx routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
