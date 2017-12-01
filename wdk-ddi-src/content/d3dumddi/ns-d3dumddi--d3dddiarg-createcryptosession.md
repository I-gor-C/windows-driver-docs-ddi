---
UID: NS.d3dumddi._D3DDDIARG_CREATECRYPTOSESSION
title: D3DDDIARG_CREATECRYPTOSESSION
author: windows-driver-content
description: The D3DDDIARG_CREATECRYPTOSESSION structure describes an encryption session to create.
old-location: display\d3dddiarg_createcryptosession.htm
old-project: display
ms.assetid: 45bc4d3f-d573-4a11-8d25-160cb8f233f4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_CREATECRYPTOSESSION, D3DDDIARG_CREATECRYPTOSESSION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDIARG_CREATECRYPTOSESSION is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_CREATECRYPTOSESSION
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
req.iface: 
---

# D3DDDIARG_CREATECRYPTOSESSION structure



## -description
<p>The D3DDDIARG_CREATECRYPTOSESSION structure describes an encryption session to create. </p>


## -syntax

````
typedef struct _D3DDDIARG_CREATECRYPTOSESSION {
  GUID   CryptoType;
  GUID   DecodeProfile;
  HANDLE hCryptoSession;
} D3DDDIARG_CREATECRYPTOSESSION;
````


## -struct-fields
<dl>

### -field <b>CryptoType</b>

<dd>
<p>[in] A GUID that indicates the encryption type, which the driver uses for the encryption session that the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createcryptosession.md">CreateCryptoSession</a> function creates. The GUID can be one of the following:</p>
<p></p>
<dl>

### -field <a id="D3DCRYPTOTYPE_AES128_CTR"></a><a id="d3dcryptotype_aes128_ctr"></a>D3DCRYPTOTYPE_AES128_CTR

<dd>
<p>A GUID that indicates the 128 bit AES-CRT block cipher.</p>
</dd>

### -field <a id="D3DCRYPTOTYPE_PROPRIETARY"></a><a id="d3dcryptotype_proprietary"></a>D3DCRYPTOTYPE_PROPRIETARY

<dd>
<p>A GUID that indicates a proprietary encryption algorithm. </p>
</dd>
</dl>
</dd>

### -field <b>DecodeProfile</b>

<dd>
<p> [in] A GUID that indicates the DirectX Video Acceleration (DirectX VA) decode profile that the driver uses for the encryption session that the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createcryptosession.md">CreateCryptoSession</a> function creates. The driver uses this decode profile in conjunction with the encryption type that the <b>CryptoType</b> member specifies. </p>
</dd>

### -field <b>hCryptoSession</b>

<dd>
<p>[in/out] A handle to the encryption session. The user-mode display driver must set this handle to a value that the Microsoft Direct3D runtime can use to identify the encryption session in subsequent calls. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3DDDIARG_CREATECRYPTOSESSION is supported beginning with the Windows 7 operating system.</p>
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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createcryptosession.md">CreateCryptoSession</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_CREATECRYPTOSESSION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
