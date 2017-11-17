---
UID: NC.d3dumddi.PFND3DDDI_GETENCRYPTIONBLTKEY
title: PFND3DDDI_GETENCRYPTIONBLTKEY
author: windows-driver-content
description: The GetEncryptionBltKey function returns the key that is used to decrypt the data that the driver's EncryptionBlt function returns.
old-location: display\getencryptionbltkey.htm
ms.assetid: b3c3e792-bc8a-485e-a208-66b7d921cc15
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: GetEncryptionBltKey is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetEncryptionBltKey
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# PFND3DDDI_GETENCRYPTIONBLTKEY callback



## -description
<p>The <i>GetEncryptionBltKey</i> function returns the key that is used to decrypt the data that the driver's <a href="https://msdn.microsoft.com/a92bfff7-8af6-48c3-9e7f-95b9426aaaf2">EncryptionBlt</a> function returns. </p>


## -prototype

````
PFND3DDDI_GETENCRYPTIONBLTKEY GetEncryptionBltKey;

__checkReturn HRESULT APIENTRY GetEncryptionBltKey(
  _In_          HANDLE                        hDevice,
  _Inout_ const D3DDDIARG_GETENCRYPTIONBLTKEY *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in, out]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543164">D3DDDIARG_GETENCRYPTIONBLTKEY</a> structure that describes the key for an encrypted session. </p>
</dd>
</dl>

## -returns
<p><i>GetEncryptionBltKey</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The key for an encrypted session is successfully retrieved. </p><dl>
<dt><b>D3DDDIERR_NOTAVAILABLE</b></dt>
</dl><p>The driver does not support the <i>GetEncryptionBltKey</i> function. </p>

<p> </p>

## -remarks
<p>The hardware and driver can optionally support the <i>GetEncryptionBltKey</i> function for all crypto types.  </p>

<p>Each time the Direct3D runtime calls the driver's <i>GetEncryptionBltKey</i> function, the driver should generate a new read-back key. If the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function previously created the encryption session with the <b>CryptoType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542923">D3DDDIARG_CREATECRYPTOSESSION</a> structure set to D3DCRYPTOTYPE_AES128_CTR, the driver and hardware should encrypt the read-back key with the session key.</p>

<p>The hardware and driver can optionally support the <i>GetEncryptionBltKey</i> function for all crypto types.  </p>

<p>Each time the Direct3D runtime calls the driver's <i>GetEncryptionBltKey</i> function, the driver should generate a new read-back key. If the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function previously created the encryption session with the <b>CryptoType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542923">D3DDDIARG_CREATECRYPTOSESSION</a> structure set to D3DCRYPTOTYPE_AES128_CTR, the driver and hardware should encrypt the read-back key with the session key.</p>

## -requirements
<table>
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
<p>Version</p>
</th>
<td width="70%">
<p><i>GetEncryptionBltKey</i> is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542923">D3DDDIARG_CREATECRYPTOSESSION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543164">D3DDDIARG_GETENCRYPTIONBLTKEY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a92bfff7-8af6-48c3-9e7f-95b9426aaaf2">EncryptionBlt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_GETENCRYPTIONBLTKEY callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
