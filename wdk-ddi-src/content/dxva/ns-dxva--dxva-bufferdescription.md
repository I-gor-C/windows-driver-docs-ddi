---
UID: NS.dxva._DXVA_BufferDescription
title: DXVA_BufferDescription
author: windows-driver-content
description: The DXVA_BufferDescription structure is sent by the host decoder to the accelerator to provide information to the accelerator about the buffer that is currently being passed from the host to the accelerator.
old-location: display\dxva_bufferdescription.htm
old-project: display
ms.assetid: 34b1585d-ceba-4e13-b5c1-70ce29a940c5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVA_BufferDescription, DXVA_BufferDescription, *LPDXVA_BufferDescription
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_BufferDescription
req.alt-loc: dxva.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# DXVA_BufferDescription structure



## -description
<p>The DXVA_BufferDescription structure is sent by the host decoder to the accelerator to provide information to the accelerator about the buffer that is currently being passed from the host to the accelerator. </p>


## -syntax

````
typedef struct _DXVA_BufferDescription {
  DWORD dwTypeIndex;
  DWORD dwBufferIndex;
  DWORD dwDataOffset;
  DWORD dwDataSize;
  DWORD dwFirstMBaddress;
  DWORD dwNumMBsInBuffer;
  DWORD dwWidth;
  DWORD dwHeight;
  DWORD dwStride;
  DWORD dwReservedBits;
} DXVA_BufferDescription, *LPDXVA_BufferDescription;
````


## -struct-fields
<dl>

### -field dwTypeIndex

<dd>
<p>Identifies the type of buffer passed to the accelerator. The following table lists the numeric identifiers and the associated buffer type.</p>
<table>
<tr>
<th>Value </th>
<th>Buffer Type</th>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>Picture decoding parameter buffers.</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/7a416992-04d3-4307-83b3-9fb94c17d60e">Macroblock control command buffers</a> (closely associated with and having a 1:1 correspondence with residual difference block data buffers).</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>Residual difference block data buffers. See <a href="https://msdn.microsoft.com/7a416992-04d3-4307-83b3-9fb94c17d60e">Macroblock-Oriented Picture Decoding</a> for more information.</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>Deblocking filter control command buffers (with or without a restriction on the effect of the filter).</p>
</td>
</tr>
<tr>
<td>
<p>5</p>
</td>
<td>
<p>Inverse-quantization matrix buffers (only used with off-host VLD processing).</p>
</td>
</tr>
<tr>
<td>
<p>6</p>
</td>
<td>
<p>Slice-control buffers (closely associated with and having a 1:1 correspondence with bitstream data buffers).</p>
</td>
</tr>
<tr>
<td>
<p>7</p>
</td>
<td>
<p>Bitstream data buffers.</p>
</td>
</tr>
<tr>
<td>
<p>8</p>
</td>
<td>
<p>AYUV alpha-blending sample buffers.</p>
</td>
</tr>
<tr>
<td>
<p>9</p>
</td>
<td>
<p>IA44/AI44 alpha-blending surface buffers.</p>
</td>
</tr>
<tr>
<td>
<p>10</p>
</td>
<td>
<p>DPXD alpha-blending surface buffers.</p>
</td>
</tr>
<tr>
<td>
<p>11</p>
</td>
<td>
<p>Highlight data buffers.</p>
</td>
</tr>
<tr>
<td>
<p>12</p>
</td>
<td>
<p>DCCMD data buffers.</p>
</td>
</tr>
<tr>
<td>
<p>13</p>
</td>
<td>
<p>Alpha-blend combination buffers.</p>
</td>
</tr>
<tr>
<td>
<p>14</p>
</td>
<td>
<p>Picture resampling control buffers.</p>
</td>
</tr>
<tr>
<td>
<p>15</p>
</td>
<td>
<p>Read-back command buffers containing commands to read macroblocks of the resulting picture back to the host.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field dwBufferIndex

<dd>
<p>Specifies the sequence number of the buffer within the buffers of the same type that were passed in the same <a href="https://msdn.microsoft.com/7d820491-2df2-4036-8f3d-e6bcff4cd1f6">buffer description list</a>.</p>
</dd>

### -field dwDataOffset

<dd>
<p>Specifies the offset of the relevant data from the beginning of the buffer in bytes. The use of this member is currently restricted to the value zero. </p>
</dd>

### -field dwDataSize

<dd>
<p>Specifies the amount of relevant data in the buffer in bytes. The location of the last byte of content in the buffer is <b>dwDataOffset</b>, plus <b>dwDataSize</b> minus 1.</p>
</dd>

### -field dwFirstMBaddress

<dd>
<p>Specifies the macroblock address of the first macroblock in the buffer passed to the accelerator. The macroblock address is given in raster scan order. The address is determined by the members of <a href="..\dxva\ns-dxva--dxva-pictureparameters.md">DXVA_PictureParameters</a>. Examples of macroblock addresses are as follows.</p>
<table>
<tr>
<th>Macroblock</th>
<th>Address </th>
</tr>
<tr>
<td>
<p>top-left </p>
</td>
<td>
<p>zero</p>
</td>
</tr>
<tr>
<td>
<p>top-right </p>
</td>
<td>
<p><b>wPicWidthInMBminus1</b></p>
</td>
</tr>
<tr>
<td>
<p>lower-left </p>
</td>
<td>
<p><b>wPicHeightInMBminus1</b> x (<b>wPicWidthInMBminus1</b>+1)</p>
</td>
</tr>
<tr>
<td>
<p>lower-right</p>
</td>
<td>
<p>(<b>wPicHeightInMBminus1</b>+1) x (<b>wPicWidthInMBminus1</b>+1)-1</p>
</td>
</tr>
</table>
<p> </p>
<p>This member must be zero if the data buffer is among the following types: picture decoding parameters, inverse-quantization matrix, slice control, bitstream data, AYUV, IA44/AI44, DPXD, Highlight, and DCCMD.</p>
<p>If the data buffer is a residual difference block data buffer, <b>dwFirstMBaddress</b> must have the same value as for the corresponding macroblock control command buffer. See <a href="https://msdn.microsoft.com/7a416992-04d3-4307-83b3-9fb94c17d60e">Macroblock-Oriented Picture Decoding</a> for more information.</p>
</dd>

### -field dwNumMBsInBuffer

<dd>
<p>Specifies the number of macroblocks of data in the buffer. This count includes skipped macroblocks. Must be zero if the data buffer is among the following types: picture decoding parameters, inverse-quantization matrix, AYUV, IA44/AI44, DPXD, Highlight, or DCCMD.</p>
<p>The value for <b>dwNumMBsInBuffer</b> depends on the type of data buffer being used as shown in the following table.</p>
<table>
<tr>
<th>Buffer Type</th>
<th>Value of dwNumMBsInBuffer</th>
</tr>
<tr>
<td>
<p>Macroblock control command</p>
</td>
<td>
<p>Must be equal to the sum of all values for <i>MBskipsFollowing,</i> added to the number of macroblock control commands in the macroblock control command buffer.</p>
</td>
</tr>
<tr>
<td>
<p>Residual difference block</p>
</td>
<td>
<p>Must have the same value as for the corresponding macroblock control command buffer.</p>
</td>
</tr>
<tr>
<td>
<p>Slice-control command</p>
</td>
<td>
<p>Must be equal to the value of the <b>wNumberMBsInSlice</b> member of the <a href="..\dxva\ns-dxva--dxva-sliceinfo.md">DXVA_SliceInfo</a> structure in the slice-control buffer.</p>
</td>
</tr>
<tr>
<td>
<p>Bitstream</p>
</td>
<td>
<p>Must have the same value as for the corresponding slice-control command buffer.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field dwWidth

<dd>
<p>Specifies the width of the data in the buffer as the number of units of bits for the following types of data: AYUV (data is specified in 32-bit units), IA44/AI44 (data is specified in 8-bit units), or DPXD (data is specified in 2-bit units). This member must be zero if the data buffer is not among the preceding types.</p>
</dd>

### -field dwHeight

<dd>
<p>Specifies the height of the data in the buffer as the number of units of bits for the following types of data: AYUV (data is specified in 32-bit units), IA44/AI44 (data is specified in 8-bit units), or DPXD (data is specified in 2-bit units).This member must be zero if the data buffer is not among the preceding types.</p>
</dd>

### -field dwStride

<dd>
<p>Specifies the stride of the data in the buffer as the number of units of bits for the following types of data: AYUV (data is specified in 32-bit units), IA44/AI44 (data is specified in 8-bit units), or DPXD (data is specified in 2-bit units). The stride for the applicable buffer types is determined from the buffer allocation setup performed by the accelerator. This member must be zero if the data buffer is not among the preceding types.</p>
</dd>

### -field dwReservedBits

<dd>
<p>Reserved bits used for packing and alignment. Must be zero.</p>
</dd>
</dl>

## -remarks
<p>An array of DXVA_BufferDescription structures is referred to as a buffer description list. When a set of buffers is sent from the host decoder to the hardware accelerator, a buffer description list is sent to describe the buffers. The buffer description list contains one DXVA_BufferDescription structure for each buffer in this set. The buffer description list starts with a DXVA_BufferDescription structure for the first buffer of the first type, followed by a DXVA_BufferDescription structure for the next buffer of the same type, and so on. The buffer description list then continues with a DXVA_BufferDescription structure for the first buffer of the next type, and so on.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dxva\ns-dxva--dxva-sliceinfo.md">DXVA_SliceInfo</a>
</dt>
<dt>
<a href="..\dxva\ns-dxva--dxva-pictureparameters.md">DXVA_PictureParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_BufferDescription structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
