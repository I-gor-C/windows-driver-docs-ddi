---
UID : NC:d3d10umddi.PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS
title : PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS
author : windows-driver-content
description : Queries the available content protection for a specified encryption algorithm and video decoder profile.
old-location : display\getcontentprotectioncaps.htm
old-project : display
ms.assetid : 51024d63-f58c-45a7-bd6f-9f24a6805878
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
req.alt-api : pfnGetContentProtectionCaps
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


# PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS callback function
Queries the available content protection for a specified encryption algorithm and video decoder profile.

## Syntax

```
PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS Pfnd3d111DdiGetcontentprotectioncaps;

HRESULT Pfnd3d111DdiGetcontentprotectioncaps(
  D3D10DDI_HDEVICE hDevice,
  CONST GUID *pCryptoType,
  CONST GUID *pDecodeProfile,
  D3D11_1DDI_VIDEO_CONTENT_PROTECTION_CAPS *pCaps
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*pCryptoType`



`*pDecodeProfile`



`*pCaps`




## Return Value

<b>GetContentProtectionCaps</b> returns one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The content protection capabilities were queried successfully.
<dl>
<dt><b>D3DERR_INVALID_CRYPTO</b></dt>
</dl>The encryption algorithm specified by the <i>pCryptoType</i> parameter is not supported.

## Remarks

The <i>pCryptoType</i> parameter can contain one of the following values:

<b>D3DCRYPTOTYPE_AES128_CTR</b> if the driver is configured to use the 128-bit Advanced Encryption Standard CTR mode (AES-CTR) block cipher.


<b>D3DCRYPTOTYPE_PROPRIETARY</b> if the driver is configured to use a proprietary encryption algorithm.


<b>NULL_GUID</b> if the driver is not configured to use any encryption algorithm.

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
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_video_content_protection_caps.md">D3D11_1DDI_VIDEO_CONTENT_PROTECTION_CAPS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>