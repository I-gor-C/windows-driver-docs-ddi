---
UID: NC.d3dumddi.PFND3DDDI_CREATECRYPTOSESSION
title: PFND3DDDI_CREATECRYPTOSESSION
author: windows-driver-content
description: The CreateCryptoSession function creates a crypto session that the Direct3D runtime uses to manage a session key and to perform crypto operations into and out of protected memory.
old-location: display\createcryptosession.htm
ms.assetid: 85d4ae6c-059d-4256-bdda-18de3d20537a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Supported starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CreateCryptoSession
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

# PFND3DDDI_CREATECRYPTOSESSION callback



## -description
<p>The <b>CreateCryptoSession</b> function creates a crypto session that the Direct3D runtime uses to manage a session key and to perform crypto operations into and out of protected memory. </p>


## -prototype

````
PFND3DDDI_CREATECRYPTOSESSION CreateCryptoSession;

__checkReturn HRESULT APIENTRY CreateCryptoSession(
  _In_    HANDLE                        hDevice,
  _Inout_ D3DDDIARG_CREATECRYPTOSESSION *pData
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
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff542923">D3DDDIARG_CREATECRYPTOSESSION</a> structure. On input, this structure contains information that the driver can use. On output, the driver specifies information in the structure that the Microsoft Direct3D runtime can use. </p>
</dd>
</dl>

## -returns
<p><b>CreateCryptoSession</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The crypto session is successfully created. </p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> could not allocate the required memory for it to complete.</p><dl>
<dt><b>D3DDDIERR_NOTAVAILABLE</b></dt>
</dl><p>The driver does not support the GUID that is specified in the <b>CryptoType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542923">D3DDDIARG_CREATECRYPTOSESSION</a> structure or the NULL_GUID (all zeros) is specified in the <b>CryptoType</b> member. </p><dl>
<dt><b>D3DDDIERR_UNSUPPORTEDCRYPTO</b></dt>
</dl><p>The driver does not support the crypto type for the specified decode type. </p>

<p> </p>

## -remarks
<p>If the <b>DecodeProfile</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542923">D3DDDIARG_CREATECRYPTOSESSION</a> structure is NULL_GUID, the crypto session will not be used for DirectX Video Acceleration (DirectX VA) decoding. If <b>DecodeProfile</b> is not <b>NULL</b> GUID, the driver should fail with D3DDDIERR_UNSUPPORTEDCRYPTO if the crypto type in the <b>CryptoType</b> member is not supported by the decode profile. </p>

<p>The driver returns a handle for the crypto session in the <b>hCryptoSession</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff542923">D3DDDIARG_CREATECRYPTOSESSION</a> that the runtime passes in all subsequent crypto session calls (for example, <a href="https://msdn.microsoft.com/f8055bb3-b8f1-47f5-9ae0-8e7a26989871">CryptoSessionKeyExchange</a>). </p>

<p>The driver must keep track of the display device (<b>hDevice</b>) that was used to create the crypto session. The driver should fail all subsequent calls that use this created crypto session if the display device that is specified in those calls is different from the display device that was used to create the crypto session.</p>

<p>If the <b>DecodeProfile</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542923">D3DDDIARG_CREATECRYPTOSESSION</a> structure is NULL_GUID, the crypto session will not be used for DirectX Video Acceleration (DirectX VA) decoding. If <b>DecodeProfile</b> is not <b>NULL</b> GUID, the driver should fail with D3DDDIERR_UNSUPPORTEDCRYPTO if the crypto type in the <b>CryptoType</b> member is not supported by the decode profile. </p>

<p>The driver returns a handle for the crypto session in the <b>hCryptoSession</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff542923">D3DDDIARG_CREATECRYPTOSESSION</a> that the runtime passes in all subsequent crypto session calls (for example, <a href="https://msdn.microsoft.com/f8055bb3-b8f1-47f5-9ae0-8e7a26989871">CryptoSessionKeyExchange</a>). </p>

<p>The driver must keep track of the display device (<b>hDevice</b>) that was used to create the crypto session. The driver should fail all subsequent calls that use this created crypto session if the display device that is specified in those calls is different from the display device that was used to create the crypto session.</p>

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
<p>Supported starting with Windows 7.</p>
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
<a href="https://msdn.microsoft.com/f8055bb3-b8f1-47f5-9ae0-8e7a26989871">CryptoSessionKeyExchange</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542923">D3DDDIARG_CREATECRYPTOSESSION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_CREATECRYPTOSESSION callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
