---
UID: NF.fwpsk.FwpsCopyStreamDataToBuffer0
title: FwpsCopyStreamDataToBuffer0
author: windows-driver-content
description: The FwpsCopyStreamDataToBuffer0 function copies stream data to a buffer.Note  FwpsCopyStreamDataToBuffer0 is a specific version of FwpsCopyStreamDataToBuffer.
old-location: netvista\fwpscopystreamdatatobuffer0.htm
ms.assetid: 758733a4-9657-48a4-bbcc-f266c72c1d6a
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsCopyStreamDataToBuffer0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FwpsCopyStreamDataToBuffer0
req.iface: 
---

# FwpsCopyStreamDataToBuffer0 function



## -description
<p>The 
  <b>FwpsCopyStreamDataToBuffer0</b> function copies stream data to a buffer.</p>


## -syntax

````
void NTAPI FwpsCopyStreamDataToBuffer0(
  _In_    const FWPS_STREAM_DATA0 *calloutStreamData,
  _Inout_       PVOID             buffer,
  _In_          SIZE_T            bytesToCopy,
  _Out_         SIZE_T            *bytesCopied
);
````


## -parameters
<dl>

### -param <i>calloutStreamData</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552419">FWPS_STREAM_DATA0</a> structure that contains
     the stream data to be copied.</p>
</dd>

### -param <i>buffer</i> [in, out]

<dd>
<p>A pointer to a location in memory that will store the copy of the stream data pointed to by the 
     <i>calloutStreamData</i> parameter. The size of the buffer must be greater than or equal to 
     <i>bytesToCopy</i>.</p>
</dd>

### -param <i>bytesToCopy</i> [in]

<dd>
<p>The amount of data, in bytes, to be copied into the receiving buffer.</p>
</dd>

### -param <i>bytesCopied</i> [out]

<dd>
<p>A pointer to a variable that receives the size, in bytes, of the stream data copied to the memory
     location pointed to by the 
     <i>buffer</i> parameter.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>To copy all indicated data to the receiving buffer, ensure that the buffer is at least 
    <i>calloutStreamData</i> -&gt;
    <b>DataLength</b> in size.</p>

<p>To copy all indicated data to the receiving buffer, ensure that the buffer is at least 
    <i>calloutStreamData</i> -&gt;
    <b>DataLength</b> in size.</p>

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
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552419">FWPS_STREAM_DATA0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsCopyStreamDataToBuffer0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
