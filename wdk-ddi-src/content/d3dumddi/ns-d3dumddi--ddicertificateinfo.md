---
UID: NS.d3dumddi._DDICERTIFICATEINFO
title: DDICERTIFICATEINFO
author: windows-driver-content
description: The DDICERTIFICATEINFO structure describes information about the certificate that the driver uses.
old-location: display\ddicertificateinfo.htm
old-project: display
ms.assetid: 205936c3-fb5a-48e7-8f13-328563c2f0d2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DDICERTIFICATEINFO, DDICERTIFICATEINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DDICERTIFICATEINFO is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DDICERTIFICATEINFO
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

# DDICERTIFICATEINFO structure



## -description
<p>The DDICERTIFICATEINFO structure describes information about the certificate that the driver uses. </p>


## -syntax

````
typedef struct _DDICERTIFICATEINFO {
  D3DDDI_CERTIFICATETYPE      CertificateType;
  DDIAUTHENTICATEDCHANNELTYPE ChannelType;
  GUID                        CryptoSessionType;
} DDICERTIFICATEINFO;
````


## -struct-fields
<dl>

### -field <b>CertificateType</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544387">D3DDDI_CERTIFICATETYPE</a>-typed value that indicates the certificate type.</p>
</dd>

### -field <b>ChannelType</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff549536">DDIAUTHENTICATEDCHANNELTYPE</a>-typed value that indicates the authenticated-channel type. </p>
</dd>

### -field <b>CryptoSessionType</b>

<dd>
<p>[in] A GUID that indicates the encryption session. </p>
</dd>
</dl>

## -remarks
<p>The runtime specifies a pointer to a DDICERTIFICATEINFO structure in the <b>pInfo</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a> structure--along with the D3DDDICAPS_GETCERTIFICATE value in the <b>Type</b> member of D3DDDIARG_GETCAPS--in a call to the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a> function to retrieve the certificate. The runtime also supplies a buffer in the <b>pData</b> member of D3DDDIARG_GETCAPS to hold the certificate. The runtime receives information about the size of the buffer when the runtime calls the driver's <b>GetCaps</b> with the D3DDDICAPS_GETCERTIFICATESIZE value set in the <b>Type</b> member of D3DDDIARG_GETCAPS. The driver returns a pointer to the certificate in the supplied buffer. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DDICERTIFICATEINFO is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544387">D3DDDI_CERTIFICATETYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549536">DDIAUTHENTICATEDCHANNELTYPE</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DDICERTIFICATEINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
