---
UID: NS.d3d10umddi.D3D11_1DDIARG_CREATECRYPTOSESSION
title: D3D11_1DDIARG_CREATECRYPTOSESSION
author: windows-driver-content
description: Specifies the attributes of the cryptographic session to be created by the user-mode driver's CreateCryptoSession function.
old-location: display\d3d11_1ddiarg_createcryptosession.htm
ms.assetid: 9e63a4eb-050b-4f12-ad43-00e62021abd3
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDIARG_CREATECRYPTOSESSION
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
ms.keywords: D3D11_1DDIARG_CREATECRYPTOSESSION, D3D11_1DDIARG_CREATECRYPTOSESSION
req.iface: 
---

# D3D11_1DDIARG_CREATECRYPTOSESSION structure



## -description
<p>Specifies the attributes of the cryptographic session to be created by the user-mode driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function.</p>


## -syntax

````
typedef struct D3D11_1DDIARG_CREATECRYPTOSESSION {
  GUID CryptoType;
  GUID DecodeProfile;
  GUID KeyExchangeType;
} D3D11_1DDIARG_CREATECRYPTOSESSION;
````


## -struct-fields
<dl>

### -field <b>CryptoType</b>

<dd>
<p>a GUID that indicates the encryption type, which the driver uses for the encryption session that the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function creates. The GUID can be one of the following:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="D3D11_1DDI_CRYPTO_TYPE_AES128_CTR"></a><a id="d3d11_1ddi_crypto_type_aes128_ctr"></a><dl>

### -field <b>D3D11_1DDI_CRYPTO_TYPE_AES128_CTR</b>

</dl>
</td>
<td width="60%">
<p>A 128-bit Advanced Encryption Standard CTR mode (AES-CTR) block cipher.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="D3D11_1DDI_CRYPTO_TYPE_PROPRIETARY"></a><a id="d3d11_1ddi_crypto_type_proprietary"></a><dl>

### -field <b>D3D11_1DDI_CRYPTO_TYPE_PROPRIETARY</b>

</dl>
</td>
<td width="60%">
<p>A proprietary encryption algorithm.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DecodeProfile</b>

<dd>
<p>A GUID that specifies the DirectX Video Acceleration (DXVA) decode profile that the driver uses for the encryption session that the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function creates. For a list of possible values, see <b>CreateCryptoSession</b>. If DXVA decoding will not be used, set this parameter to <b>NULL_GUID</b>.</p>
</dd>

### -field <b>KeyExchangeType</b>

<dd>
<p>A GUID that specifies the type of key exchange.
The following GUID is defined.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="D3D11_1DDI_KEY_EXCHANGE_RSAES_OAEP"></a><a id="d3d11_1ddi_key_exchange_rsaes_oaep"></a><dl>

### -field <b>D3D11_1DDI_KEY_EXCHANGE_RSAES_OAEP</b>

</dl>
</td>
<td width="60%">
<p>The caller will create the session key, encrypt it with RSA Encryption Scheme - Optimal Asymmetric Encryption Padding (RSAES-OAEP) by using the driver's public key, and pass the session key to the driver.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION"></a><a id="d3dwddm2_0ddi_key_exchange_hw_protection"></a><dl>

### -field <b>D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION</b>

</dl>
</td>
<td width="60%">
<p>The crypto session will be used purely for communication between user mode DRM component and the secure execution environment.

</p>
<p>When this GUID is specified, the following DDIs should not be called for the crypto session:</p>
<ul>
<li>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451654">GetCertificateSize</a>
</li>
<li>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451652">GetCertificate</a>
</li>
<li>
<a href="https://msdn.microsoft.com/a92bfff7-8af6-48c3-9e7f-95b9426aaaf2">EncryptionBlt</a>
</li>
<li>
<a href="https://msdn.microsoft.com/1bfe2b9c-90f6-48bf-b0b3-30788ef94110">DecryptionBlt</a>
</li>
<li>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451696">StartSessionKeyRefresh</a>
</li>
<li>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451648">FinishSessionKeyRefresh</a>
</li>
<li>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451660">GetEncryptionBltKey</a>
</li>
</ul>
<p>
The DRM commands are sent to the user mode driver by calling the <a href="https://msdn.microsoft.com/a48dcbae-3236-4523-bc14-4be694da9a7b">NegotiateCryptoSessionKeyExchange</a> function where the data passed is a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn894610">D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_DATA</a> structure.
</p>
</td>
</tr>
</table>
<p> </p>
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