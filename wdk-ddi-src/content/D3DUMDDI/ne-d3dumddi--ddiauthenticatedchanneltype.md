---
UID: NE.d3dumddi._DDIAUTHENTICATEDCHANNELTYPE
title: DDIAUTHENTICATEDCHANNELTYPE
author: windows-driver-content
description: The DDIAUTHENTICATEDCHANNELTYPE enumeration contains values that identify authenticated-channel types.
old-location: display\ddiauthenticatedchanneltype.htm
ms.assetid: 431575b7-1173-448c-98a9-790bc2721da0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DDIAUTHENTICATEDCHANNELTYPE is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DDIAUTHENTICATEDCHANNELTYPE
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

# DDIAUTHENTICATEDCHANNELTYPE enumeration



## -description
<p>The DDIAUTHENTICATEDCHANNELTYPE enumeration contains values that identify authenticated-channel types. </p>


## -syntax

````
typedef enum _DDIAUTHENTICATEDCHANNELTYPE { 
  DDIAUTHENTICATEDCHANNEL_DRIVER_SOFTWARE  = 2,
  DDIAUTHENTICATEDCHANNEL_DRIVER_HARDWARE  = 3
} DDIAUTHENTICATEDCHANNELTYPE;
````


## -enum-fields
<dl>

### -field <a id="DDIAUTHENTICATEDCHANNEL_DRIVER_SOFTWARE"></a><a id="ddiauthenticatedchannel_driver_software"></a><b>DDIAUTHENTICATEDCHANNEL_DRIVER_SOFTWARE</b>

<dd>
<p>The value specifies that the authenticated-channel type is software. </p>
</dd>

### -field <a id="DDIAUTHENTICATEDCHANNEL_DRIVER_HARDWARE"></a><a id="ddiauthenticatedchannel_driver_hardware"></a><b>DDIAUTHENTICATEDCHANNEL_DRIVER_HARDWARE</b>

<dd>
<p>The value specifies that the authenticated-channel type is hardware.</p>
</dd>
</dl>

## -remarks
<p>The user-mode display driver receives a DDIAUTHENTICATEDCHANNELTYPE-typed value in the <b>ChannelType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549552">DDICERTIFICATEINFO</a> structure. The <b>pInfo</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a> structure points to this DDICERTIFICATEINFO structure when the driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function is called with the D3DDDICAPS_GETCERTIFICATE value set in the <b>Type</b> member of D3DDDIARG_GETCAPS. </p>

<p>The Microsoft Direct3D runtime specifies a DDIAUTHENTICATEDCHANNELTYPE-typed value in the <b>ChannelType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542918">D3DDDIARG_CREATEAUTHENTICATEDCHANNEL</a> structure that the <i>pData</i> parameter points to in a call to the driver's <a href="https://msdn.microsoft.com/0a565bff-fc6f-41c1-a6fd-3a82dd0d7889">CreateAuthenticatedChannel</a> function.</p>

<p>The user-mode display driver receives a DDIAUTHENTICATEDCHANNELTYPE-typed value in the <b>ChannelType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549552">DDICERTIFICATEINFO</a> structure. The <b>pInfo</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a> structure points to this DDICERTIFICATEINFO structure when the driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function is called with the D3DDDICAPS_GETCERTIFICATE value set in the <b>Type</b> member of D3DDDIARG_GETCAPS. </p>

<p>The Microsoft Direct3D runtime specifies a DDIAUTHENTICATEDCHANNELTYPE-typed value in the <b>ChannelType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542918">D3DDDIARG_CREATEAUTHENTICATEDCHANNEL</a> structure that the <i>pData</i> parameter points to in a call to the driver's <a href="https://msdn.microsoft.com/0a565bff-fc6f-41c1-a6fd-3a82dd0d7889">CreateAuthenticatedChannel</a> function.</p>

<p>The user-mode display driver receives a DDIAUTHENTICATEDCHANNELTYPE-typed value in the <b>ChannelType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549552">DDICERTIFICATEINFO</a> structure. The <b>pInfo</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a> structure points to this DDICERTIFICATEINFO structure when the driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function is called with the D3DDDICAPS_GETCERTIFICATE value set in the <b>Type</b> member of D3DDDIARG_GETCAPS. </p>

<p>The Microsoft Direct3D runtime specifies a DDIAUTHENTICATEDCHANNELTYPE-typed value in the <b>ChannelType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542918">D3DDDIARG_CREATEAUTHENTICATEDCHANNEL</a> structure that the <i>pData</i> parameter points to in a call to the driver's <a href="https://msdn.microsoft.com/0a565bff-fc6f-41c1-a6fd-3a82dd0d7889">CreateAuthenticatedChannel</a> function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DDIAUTHENTICATEDCHANNELTYPE is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/0a565bff-fc6f-41c1-a6fd-3a82dd0d7889">CreateAuthenticatedChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542918">D3DDDIARG_CREATEAUTHENTICATEDCHANNEL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549552">DDICERTIFICATEINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DDIAUTHENTICATEDCHANNELTYPE enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
