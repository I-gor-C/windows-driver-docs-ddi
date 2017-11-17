---
UID: NE.d3dkmdt._DXGKMDT_CERTIFICATE_TYPE
title: DXGKMDT_CERTIFICATE_TYPE
author: windows-driver-content
description: The DXGKMDT_CERTIFICATE_TYPE enumeration identifies the type of certificate that callers of the DxgkDdiOPMGetCertificateSize and DxgkDdiOPMGetCertificate functions require.
old-location: display\dxgkmdt_certificate_type.htm
ms.assetid: aad96bf7-46d3-4859-b324-f48cdb99a594
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKMDT_CERTIFICATE_TYPE
req.alt-loc: d3dkmdt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# DXGKMDT_CERTIFICATE_TYPE enumeration



## -description
<p>The DXGKMDT_CERTIFICATE_TYPE enumeration identifies the type of certificate that callers of the <a href="https://msdn.microsoft.com/fe4197ad-52a2-47b3-ad96-57ea73cd931f">DxgkDdiOPMGetCertificateSize</a> and <a href="https://msdn.microsoft.com/3c055598-5f07-46e1-830d-1df9a459f742">DxgkDdiOPMGetCertificate</a> functions require. </p>


## -syntax

````
typedef enum _DXGKMDT_CERTIFICATE_TYPE { 
  DXGKMDT_OPM_CERTIFICATE   = 0,
  DXGKMDT_COPP_CERTIFICATE  = 1,
  DXGKMDT_UAB_CERTIFICATE   = 2,
  DXGKMDT_FORCE_ULONG       = 0xFFFFFFFF
} DXGKMDT_CERTIFICATE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DXGKMDT_OPM_CERTIFICATE"></a><a id="dxgkmdt_opm_certificate"></a><b>DXGKMDT_OPM_CERTIFICATE</b>

<dd>
<p>Indicates an Output Protection Management (OPM) certificate. </p>
</dd>

### -field <a id="DXGKMDT_COPP_CERTIFICATE"></a><a id="dxgkmdt_copp_certificate"></a><b>DXGKMDT_COPP_CERTIFICATE</b>

<dd>
<p>Indicates a Certified Output Protection Protocol (COPP) certificate. </p>
</dd>

### -field <a id="DXGKMDT_UAB_CERTIFICATE"></a><a id="dxgkmdt_uab_certificate"></a><b>DXGKMDT_UAB_CERTIFICATE</b>

<dd>
<p>Indicates a User Accessible Bus (UAB) certificate. </p>
</dd>

### -field <a id="DXGKMDT_FORCE_ULONG"></a><a id="dxgkmdt_force_ulong"></a><b>DXGKMDT_FORCE_ULONG</b>

<dd>
<p>Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. You should not use this value. </p>
</dd>
</dl>

## -remarks
<p>For more information about certificates that are used with OPM, download the Output Content Protection document at the <a href="http://go.microsoft.com/fwlink/p/?linkid=204788">Output Content Protection and Windows Vista</a> website.</p>

<p>For more information about certificates that are used with OPM, download the Output Content Protection document at the <a href="http://go.microsoft.com/fwlink/p/?linkid=204788">Output Content Protection and Windows Vista</a> website.</p>

<p>For more information about certificates that are used with OPM, download the Output Content Protection document at the <a href="http://go.microsoft.com/fwlink/p/?linkid=204788">Output Content Protection and Windows Vista</a> website.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/3c055598-5f07-46e1-830d-1df9a459f742">DxgkDdiOPMGetCertificate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fe4197ad-52a2-47b3-ad96-57ea73cd931f">DxgkDdiOPMGetCertificateSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKMDT_CERTIFICATE_TYPE enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
