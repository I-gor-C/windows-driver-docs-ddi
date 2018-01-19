---
UID : NC:d3d10umddi.PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS
title : PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS
author : windows-driver-content
description : Submits one or more video frame buffers for DirectX Video Acceleration (DXVA) decoding.
old-location : display\videodecodersubmitbuffers.htm
old-project : display
ms.assetid : fc1644d8-9058-4100-8e3e-f4727af89773
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SETRESULT_INFO, *PSETRESULT_INFO, SETRESULT_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnVideoDecoderSubmitBuffers
req.alt-loc : D3d10umddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS callback function
Submits one or more video frame buffers for DirectX Video Acceleration (DXVA) decoding.

## Syntax

```
PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS Pfnd3d111DdiVideodecodersubmitbuffers;

HRESULT Pfnd3d111DdiVideodecodersubmitbuffers(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HDECODE,
   UINT,
  CONST D3D11_1DDI_VIDEO_DECODER_BUFFER_DESC *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HDECODE`



`UINT`



`*`




## Return Value

<b>VideoDecoderSubmitBuffers</b> returns one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The video buffers were submitted successfully.
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
        Memory was not available to complete the operation.

## Remarks

The <i>pBufferDesc</i> parameter points to an array of one or more  <a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_decoderr_buffer_desc.md">D3D11_1DDI_VIDEO_DECODER_BUFFER_DESC</a> structures. Each element in the array describes a compressed video frame buffer that is submitted for decoding.


Each <a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_decoderr_buffer_desc.md">D3D11_1DDI_VIDEO_DECODER_BUFFER_DESC</a> structure includes the following data:

The resource that will receive the decrypted and decode frame buffers.

A <a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_encrypted_block_info.md">D3D11_1DDI_ENCRYPTED_BLOCK_INFO</a> structure that specifies which bytes of the frame buffer are encrypted.



A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_aes_ctr_iv.md">D3D11_1DDI_AES_CTR_IV</a> structure that contains an initialization vector (IV) for the frame buffer data that was encrypted by using the 128-bit Advanced Encryption Standard CTR mode (AES-CTR) block cipher encryption algorithm.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideodecoder.md">CreateVideoDecoder</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_aes_ctr_iv.md">D3D11_1DDI_AES_CTR_IV</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_encrypted_block_info.md">D3D11_1DDI_ENCRYPTED_BLOCK_INFO</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_decoderr_buffer_desc.md">D3D11_1DDI_VIDEO_DECODER_BUFFER_DESC</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEODECODERSUBMITBUFFERS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>