---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETCRYPTOKEYEXCHANGETYPE
title: PFND3D11_1DDI_GETCRYPTOKEYEXCHANGETYPE
author: windows-driver-content
description: Queries the type of key exchange that is supported by the cryptographic engine of the display adapter for a specified encryption algorithm and video decoder profile.
old-location: display\getcryptokeyexchangetype.htm
old-project: display
ms.assetid: 64870c9f-facf-4344-93d0-12cbcec86e11
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetCryptoKeyExchangeType
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

# PFND3D11_1DDI_GETCRYPTOKEYEXCHANGETYPE callback



## -description
<p>Queries the type of key exchange that is supported by the cryptographic engine of the display adapter for a specified encryption algorithm and video decoder profile.  </p>


## -prototype

````
PFND3D11_1DDI_GETCRYPTOKEYEXCHANGETYPE GetCryptoKeyExchangeType;

HRESULT APIENTRY* GetCryptoKeyExchangeType(
  _In_        D3D10DDI_HDEVICE hDevice,
  _In_  const GUID             *pCryptoType,
  _In_  const GUID             *pDecodeProfile,
  _In_        UINT             Index,
  _Out_       GUID             *pKeyExchangeType
)
{ ... }
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p>A handle to the display device (graphics context).

</p>
</dd>

### -param pCryptoType [in]

<dd>
<p>A pointer to a GUID that specifies the type of encryption algorithm to query.</p>
</dd>

### -param pDecodeProfile [in]

<dd>
<p>A pointer to a GUID that specifies the decoder profile to query.</p>
</dd>

### -param Index [in]

<dd>
<p>The zero-based index of the key exchange type.</p>
</dd>

### -param pKeyExchangeType [out]

<dd>
<p>A pointer to a GUID that specifies the supported key exchange type for the specified index.</p>
</dd>
</dl>

## -returns
<p><b>GetCryptoKeyExchangeType</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The content protection capabilities were queried successfully.</p><dl>
<dt><b>D3DERR_INVALID_CRYPTO</b></dt>
</dl><p>The encryption algorithm specified by the <i>pCryptoType</i> parameter is not supported.</p>

<p> </p>

## -remarks
<p>The <b>GetCryptoKeyExchangeType</b> function can be called to query the key exchange types for any index from 0 to (<b>D3D11_1DDI_VIDEO_CONTENT_PROTECTION_CAPS.KeyExchangeTypeCount</b>– 1). </p>

<p>The <i>pCryptoType</i> parameter can contain one of the following values:</p>

<p><b>D3DCRYPTOTYPE_AES128_CTR</b> if the driver is configured to use the 128-bit Advanced Encryption Standard CTR mode (AES-CTR) block cipher. 
</p>

<p><b>D3DCRYPTOTYPE_PROPRIETARY</b> if the driver is configured to use a proprietary encryption algorithm. 
</p>

<p><b>NULL_GUID</b> if the driver is not configured to use any encryption algorithm.</p>

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
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
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-video-content-protection-caps.md">D3D11_1DDI_VIDEO_CONTENT_PROTECTION_CAPS</a>
</dt>
<dt>
<a href="display.getcontentprotectioncaps">GetContentProtectionCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_GETCRYPTOKEYEXCHANGETYPE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
