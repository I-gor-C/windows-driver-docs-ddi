---
UID: NS.d3dumddi._DXVADDI_DECODEBUFFERDESC
title: DXVADDI_DECODEBUFFERDESC
author: windows-driver-content
description: The DXVADDI_DECODEBUFFERDESC structure describes a buffer that is currently passed from the host decoder to the accelerator.
old-location: display\dxvaddi_decodebufferdesc.htm
ms.assetid: 809b4cf8-e4c5-4cb6-b58f-8b6b98111361
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_DECODEBUFFERDESC
req.alt-loc: d3dumddi.h
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
ms.keywords: DXVADDI_DECODEBUFFERDESC, DXVADDI_DECODEBUFFERDESC
req.iface: 
---

# DXVADDI_DECODEBUFFERDESC structure



## -description
<p>The DXVADDI_DECODEBUFFERDESC structure describes a buffer that is currently passed from the host decoder to the accelerator. </p>


## -syntax

````
typedef struct _DXVADDI_DECODEBUFFERDESC {
  HANDLE            hBuffer;
  D3DDDIFORMAT      CompressedBufferType;
  UINT              BufferIndex;
  UINT              DataOffset;
  UINT              DataSize;
  UINT              FirstMBaddress;
  UINT              NumMBsInBuffer;
  UINT              Width;
  UINT              Height;
  UINT              Stride;
  UINT              ReservedBits;
  DXVADDI_PVP_HW_IV *pCipherCounter;
} DXVADDI_DECODEBUFFERDESC;
````


## -struct-fields
<dl>

### -field <b>hBuffer</b>

<dd>
<p>[in] A handle to the buffer.</p>
</dd>

### -field <b>CompressedBufferType</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544312">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the buffer.</p>
</dd>

### -field <b>BufferIndex</b>

<dd>
<p>[in] Reserved. Do not use this member. For more information, see the Remarks section.</p>
</dd>

### -field <b>DataOffset</b>

<dd>
<p>[in] The offset of the relevant data from the beginning of the buffer, in bytes. The use of this member is currently restricted to the value zero. </p>
</dd>

### -field <b>DataSize</b>

<dd>
<p>[in] The amount of relevant data in the buffer, in bytes. The location of the last byte of content in the buffer is the value of <b>DataOffset</b> plus the value of <b>DataSize</b> minus 1.</p>
</dd>

### -field <b>FirstMBaddress</b>

<dd>
<p>[in] The macroblock address of the first macroblock in the buffer that is passed to the accelerator. The macroblock address is given in raster scan order. The address is determined by the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564012">DXVA_PictureParameters</a> structure. The following table shows examples of macroblock addresses.</p>
<table>
<tr>
<th>Macroblock</th>
<th>Address </th>
</tr>
<tr>
<td>
<p>Top-left </p>
</td>
<td>
<p>Zero</p>
</td>
</tr>
<tr>
<td>
<p>Top-right </p>
</td>
<td>
<p><b>wPicWidthInMBminus1</b> of DXVA_PictureParameters.</p>
</td>
</tr>
<tr>
<td>
<p>Bottom-left </p>
</td>
<td>
<p><b>wPicHeightInMBminus1</b> x (<b>wPicWidthInMBminus1</b>+1). Members of DXVA_PictureParameters.</p>
</td>
</tr>
<tr>
<td>
<p>Bottom-right</p>
</td>
<td>
<p>(<b>wPicHeightInMBminus1</b>+1) x (<b>wPicWidthInMBminus1</b>+1)-1. Members of DXVA_PictureParameters.</p>
</td>
</tr>
</table>
<p> </p>
<p>The <b>FirstMBaddress</b> member must be zero if the data buffer is one of the following types: picture decoding parameters, inverse-quantization matrix, slice control, bitstream data, AYUV, IA44/AI44, DPXD, Highlight, and DCCMD.</p>
<p>If the data buffer is a residual difference block data buffer, <b>FirstMBaddress</b> must have the same value as for the corresponding macroblock control command buffer. </p>
</dd>

### -field <b>NumMBsInBuffer</b>

<dd>
<p>[in] The number of macroblocks of data in the buffer, including skipped macroblocks. This member must be zero if the data buffer is one of the following types: picture decoding parameters, inverse-quantization matrix, AYUV, IA44/AI44, DPXD, Highlight, or DCCMD.</p>
<p>The value for <b>NumMBsInBuffer</b> depends on the type of data buffer that is being used, as shown in the following table.</p>
<table>
<tr>
<th>Buffer type</th>
<th>Value of NumMBsInBuffer</th>
</tr>
<tr>
<td>
<p>Macroblock control command</p>
</td>
<td>
<p>The sum of all of the values for <i>MBskipsFollowing,</i> added to the number of macroblock control commands in the macroblock control command buffer.</p>
</td>
</tr>
<tr>
<td>
<p>Residual difference block</p>
</td>
<td>
<p>The same value as for the corresponding macroblock control command buffer.</p>
</td>
</tr>
<tr>
<td>
<p>Slice-control command</p>
</td>
<td>
<p>The value of the <b>wNumberMBsInSlice</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564049">DXVA_SliceInfo</a> structure in the slice-control buffer.</p>
</td>
</tr>
<tr>
<td>
<p>Bitstream</p>
</td>
<td>
<p>The same value as for the corresponding slice-control command buffer.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Width</b>

<dd>
<p>[in] Reserved. Do not use this member. For more information, see the Remarks section.</p>
</dd>

### -field <b>Height</b>

<dd>
<p>[in] Reserved. Do not use this member. For more information, see the Remarks section.</p>
</dd>

### -field <b>Stride</b>

<dd>
<p>[in] Reserved. Do not use this member. For more information, see the Remarks section.</p>
</dd>

### -field <b>ReservedBits</b>

<dd>
<p>[in] Reserved bits that are used for packing and alignment. This member must be zero.</p>
</dd>

### -field <b>pCipherCounter</b>

<dd>
<p>[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562920">DXVADDI_PVP_HW_IV</a> structure that contains a 128-bit protected video path (PVP) value. </p>
</dd>
</dl>

## -remarks
<p>An array of DXVADDI_DECODEBUFFERDESC structures is referred to as a <i>buffer description list</i>. When a set of buffers is sent from the host decoder to the hardware accelerator, a buffer description list is sent to describe the buffers. The buffer description list contains one DXVADDI_DECODEBUFFERDESC structure for each buffer in this set. The buffer description list starts with a DXVADDI_DECODEBUFFERDESC structure for the first buffer of the first type, followed by a DXVADDI_DECODEBUFFERDESC structure for the next buffer of the same type, and so on. The buffer description list then continues with a DXVADDI_DECODEBUFFERDESC structure for the first buffer of the next type, and so on. This entire list is contained in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543001">D3DDDIARG_DECODEEXECUTE</a> structure.</p>

<p>Because Microsoft DirectX Video Acceleration (VA) version 2.0 uses Microsoft Direct3D surfaces rather than the private surfaces that DirectX VA 1.0 uses, the user-mode display driver obtains values for the index, width, height, and stride from the given compressed buffer type rather than from the values in the <b>BufferIndex</b>, <b>Width</b>, <b>Height</b>, and <b>Stride</b> members. In fact, the Microsoft Direct3D runtime sets these members to zero.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543001">D3DDDIARG_DECODEEXECUTE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564012">DXVA_PictureParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564049">DXVA_SliceInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562920">DXVADDI_PVP_HW_IV</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_DECODEBUFFERDESC structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
