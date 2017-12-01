---
UID: NC.d3d10umddi.PFND3D11_1DDI_NEGOTIATECRYPTOSESSIONKEYESCHANGE
title: PFND3D11_1DDI_NEGOTIATECRYPTOSESSIONKEYESCHANGE
author: windows-driver-content
description: Establishes a session key for a cryptographic session object.
old-location: display\negotiatecryptosessionkeyexchange.htm
old-project: display
ms.assetid: a48dcbae-3236-4523-bc14-4be694da9a7b
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
req.alt-api: NegotiateCryptoSessionKeyExchange
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

# PFND3D11_1DDI_NEGOTIATECRYPTOSESSIONKEYESCHANGE callback



## -description
<p>Establishes a session key for a cryptographic session object.</p>


## -prototype

````
PFND3D11_1DDI_NEGOTIATECRYPTOSESSIONKEYESCHANGE NegotiateCryptoSessionKeyExchange;

HRESULT APIENTRY* NegotiateCryptoSessionKeyExchange(
  _In_ D3D10DDI_HDEVICE          hDevice,
  _In_ D3D11_1DDI_HCRYPTOSESSION hCryptoSession,
  _In_ UINT                      DataSize,
  _In_ VOID                      *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device (graphics context).

</p>
</dd>

### -param <i>hCryptoSession</i> [in]

<dd>
<p>A handle to the cryptographic session object that was created through a call to the <a href="display.createcryptosession1">CreateCryptoSession</a> function. 

</p>
</dd>

### -param <i>DataSize</i> [in]

<dd>
<p>The size, in bytes, of the data in the <i>pData</i> array.

</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a byte array that contains the encrypted session key.</p>
</dd>
</dl>

## -returns
<p><i>NegotiateCryptoSessionKeyExchange</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The session key for the cryptographic session was negotiated successfully.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
        Memory was not available to complete the operation.</p>

<p> </p>

## -remarks
<p>The <i>pData</i> parameter references a buffer that contains a session key for the cryptographic session. The key exchange mechanism depends on the type of the encryption algorithm that is used by the cryptographic session.</p>

<p>For sessions that use the RSA Encryption Scheme - Optimal Asymmetric Encryption Padding (RSAES-OAEP) algorithm, the key buffer must contain 256 bytes of data and must be encrypted by using the RSA Encryption Scheme - Optimal Asymmetric Encryption Padding (RSAES-OAEP) algorithm with the public key from the cryptographic session certificate.</p>

<p>The key exchange for a cryptographic session is identical to the key exchange for the Output Protection Manager (OPM) interface. However,  the OPM key buffer contains additional data besides the session key.  </p>

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
<a href="display.createcryptosession1">CreateCryptoSession</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_NEGOTIATECRYPTOSESSIONKEYESCHANGE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
