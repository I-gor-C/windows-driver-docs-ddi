---
UID: NS.d3dumddi._DDICONTENTPROTECTIONCAPS
title: DDICONTENTPROTECTIONCAPS
author: windows-driver-content
description: The DDICONTENTPROTECTIONCAPS structure describes a specific encryption and decode combination that the driver uses.
old-location: display\ddicontentprotectioncaps.htm
ms.assetid: d223712d-2c77-4bec-b8c0-d677d4caeac2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DDICONTENTPROTECTIONCAPS is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DDICONTENTPROTECTIONCAPS
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
ms.keywords: DDICONTENTPROTECTIONCAPS, DDICONTENTPROTECTIONCAPS
req.iface: 
---

# DDICONTENTPROTECTIONCAPS structure



## -description
<p>The DDICONTENTPROTECTIONCAPS structure describes a specific encryption and decode combination that the driver uses. </p>


## -syntax

````
typedef struct _DDICONTENTPROTECTIONCAPS {
  GUID CryptoType;
  GUID DecodeProfile;
} DDICONTENTPROTECTIONCAPS;
````


## -struct-fields
<dl>

### -field <b>CryptoType</b>

<dd>
<p>[in] A GUID that indicates the encryption type that the driver uses. The currently defined GUIDs are:</p>
<p></p>
<dl>

### -field <a id="D3DCRYPTOTYPE_AES128_CTR"></a><a id="d3dcryptotype_aes128_ctr"></a>D3DCRYPTOTYPE_AES128_CTR

<dd>
<p>A GUID that indicates the 128-bit AES-CRT block cipher.</p>
</dd>

### -field <a id="D3DCRYPTOTYPE_PROPRIETARY"></a><a id="d3dcryptotype_proprietary"></a>D3DCRYPTOTYPE_PROPRIETARY

<dd>
<p>A GUID that indicates a proprietary encryption algorithm. </p>
</dd>
</dl>
<p>A <b>NULL</b> value indicates that no encryption is used. </p>
</dd>

### -field <b>DecodeProfile</b>

<dd>
<p>[in] A GUID that indicates the DirectX Video Acceleration (DirectX VA) decode profile that the driver uses along with the encryption type, which the <b>CryptoType</b> member specifies. Not all drivers allow all types of encryption. For example, MPEG2 IDCT frequently requires that the private libraries, which the hardware vendor supplies, perform the proprietary encryption. A <b>NULL</b> value indicates that DirectX VA decode profile is not used. </p>
</dd>
</dl>

## -remarks
<p>The runtime specifies a pointer to a DDICONTENTPROTECTIONCAPS structure in the <b>pInfo</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a> structure--along with the D3DDDICAPS_GETCONTENTPROTECTIONCAPS value in the <b>Type</b> member of D3DDDIARG_GETCAPS--in a call to the user-mode display driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function to determine the content-protection capabilities that the driver supports. The driver's <b>GetCaps</b> returns a pointer to a populated D3DCONTENTPROTECTIONCAPS structure in the <b>pData</b> member of D3DDDIARG_GETCAPS that describes the content-protection capabilities that the driver supports. An application calls the <b>IDirect3DDevice9Video::GetContentProtectionCaps</b> method to retrieve these content-protection capabilities. For more information about <b>IDirect3DDevice9Video::GetContentProtectionCaps</b> and D3DCONTENTPROTECTIONCAPS, see the DirectX SDK documentation.</p>

<p>If the runtime specifies NULL_GUID (all zeros) in <b>DecodeProfile</b>, the driver should return the content-protection capabilities that are relevant for when a DirectX VA decode profile is not used. These content-protection capabilities correspond to the content-protection DDI functions that the driver optionally implements. For more information about these optional functions, see <a href="https://msdn.microsoft.com/770e0fce-d3b5-4599-8165-eadf3f23f9dc">Content Protection DDI</a>.</p>

<p>If the encryption type that is specified in the <b>CryptoType</b> member is supported by the graphics hardware and the driver, but is not supported by the DirectX VA decode profile that is specified in the <b>DecodeProfile</b> member, the driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function should return D3DDDIERR_UNSUPPORTEDCRYPTO. If the encryption type that is specified in the <b>CryptoType</b> member is not supported at all, the driver's <b>GetCaps</b> function should return D3DDDIERR_NOTAVAILABLE.</p>

<p>If the runtime specifies NULL_GUID in the <b>CryptoType</b> member, the driver should report a superset of its content-protection capabilities. For example, if encryption type A supports some capabilities and encryption type B supports some other capabilities, the driver should return the cumulative capabilities. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DDICONTENTPROTECTIONCAPS is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DDICONTENTPROTECTIONCAPS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
