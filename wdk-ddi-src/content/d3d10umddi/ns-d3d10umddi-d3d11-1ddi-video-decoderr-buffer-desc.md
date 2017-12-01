---
UID: NS.d3d10umddi.D3D11_1DDI_VIDEO_DECODERR_BUFFER_DESC
title: D3D11_1DDI_VIDEO_DECODERR_BUFFER_DESC
author: windows-driver-content
description: Describes a compressed buffer for Microsoft DirectX Video Acceleration (DXVA) decoding.
old-location: display\d3d11_1ddi_video_decoderr_buffer_desc.htm
old-project: display
ms.assetid: aff44ad9-7ade-4b01-8e41-11d686728faa
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11_1DDI_VIDEO_DECODERR_BUFFER_DESC, D3D11_1DDI_VIDEO_DECODER_BUFFER_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEO_DECODER_BUFFER_DESC
req.alt-loc: D3d10umddi.h
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

# D3D11_1DDI_VIDEO_DECODERR_BUFFER_DESC structure



## -description
<p>Describes a compressed buffer for Microsoft DirectX Video Acceleration (DXVA) decoding.</p>


## -syntax

````
typedef struct D3D11_1DDI_VIDEO_DECODERR_BUFFER_DESC {
  D3D10DDI_HRESOURCE                   hResource;
  D3D11_1DDI_VIDEO_DECODER_BUFFER_TYPE BufferType;
  UINT                                 BufferIndex;
  UINT                                 DataOffset;
  UINT                                 DataSize;
  UINT                                 FirstMBaddress;
  UINT                                 NumMBsInBuffer;
  UINT                                 Width;
  UINT                                 Height;
  UINT                                 Stride;
  UINT                                 ReservedBits;
  void                                 *pIV;
  UINT                                 IVSize;
  BOOL                                 PartialEncryption;
  D3D11_1DDI_ENCRYPTED_BLOCK_INFO      EncryptedBlockInfo;
} D3D11_1DDI_VIDEO_DECODER_BUFFER_DESC;
````


## -struct-fields
<dl>

### -field <b>hResource</b>

<dd>
<p>A handle to the resource that will receive the decrypted and decode frame buffers.</p>
</dd>

### -field <b>BufferType</b>

<dd>
<p>The type of buffer, specified as a constant value of the <a href="..\d3d10umddi\ne-d3d10umddi-d3d11-ddi-video-decoder-buffer-type.md">D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE</a> enumeration.</p>
<p>In D3d10umddi.h, <a href="..\d3d10umddi\ne-d3d10umddi-d3d11-ddi-video-decoder-buffer-type.md">D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE</a> and <b>D3D11_1DDI_VIDEO_DECODER_BUFFER_TYPE</b> are defined as the same type.</p>
</dd>

### -field <b>BufferIndex</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>DataOffset</b>

<dd>
<p>The offset of the relevant data from the beginning of the buffer, in bytes. This value must be zero.</p>
</dd>

### -field <b>DataSize</b>

<dd>
<p>The offset of the relevant data from the beginning of the buffer, in bytes. This value must be zero.</p>
</dd>

### -field <b>FirstMBaddress</b>

<dd>
<p>The macroblock address of the first macroblock in the buffer. The macroblock address is given in raster scan order.</p>
</dd>

### -field <b>NumMBsInBuffer</b>

<dd>
<p>The number of macroblocks of data in the buffer. This count includes skipped macroblocks.</p>
</dd>

### -field <b>Width</b>

<dd>
<p>Reserved for system use. Set to zero.</p>
</dd>

### -field <b>Height</b>

<dd>
<p>Reserved for system use. Set to zero.</p>
</dd>

### -field <b>Stride</b>

<dd>
<p>Reserved for system use. Set to zero.</p>
</dd>

### -field <b>ReservedBits</b>

<dd>
<p>Reserved for system use. Set to zero.</p>
</dd>

### -field <b>pIV</b>

<dd>
<p>A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-aes-ctr-iv.md">D3D11_1DDI_AES_CTR_IV</a> structure that contains an initialization vector (IV) for the frame buffer data that was encrypted by using the 128-bit Advanced Encryption Standard CTR mode (AES-CTR) block cipher encryption algorithm.</p>
<p>If the decode buffer does not contain any encrypted data, set <b>pIV</b> to <b>NULL</b>.</p>
</dd>

### -field <b>IVSize</b>

<dd>
<p>The size of the buffer specified in the <b>pIV</b> member. If <b>pIV</b> is <b>NULL</b>, set this member to zero.</p>
</dd>

### -field <b>PartialEncryption</b>

<dd>
<p>If <b>TRUE</b>, the video surfaces are partially encrypted.</p>
</dd>

### -field <b>EncryptedBlockInfo</b>

<dd>
<p>A <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-encrypted-block-info.md">D3D11_1DDI_ENCRYPTED_BLOCK_INFO</a> structure that specifies which bytes of the surface are encrypted.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-aes-ctr-iv.md">D3D11_1DDI_AES_CTR_IV</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-encrypted-block-info.md">D3D11_1DDI_ENCRYPTED_BLOCK_INFO</a>
</dt>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3d11-ddi-video-decoder-buffer-type.md">D3D11_DDI_VIDEO_DECODER_BUFFER_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_VIDEO_DECODERR_BUFFER_DESC structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
