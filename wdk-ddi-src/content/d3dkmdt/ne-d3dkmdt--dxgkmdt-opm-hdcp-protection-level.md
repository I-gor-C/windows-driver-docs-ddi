---
UID: NE.d3dkmdt._DXGKMDT_OPM_HDCP_PROTECTION_LEVEL
title: DXGKMDT_OPM_HDCP_PROTECTION_LEVEL
author: windows-driver-content
description: The DXGKMDT_OPM_HDCP_PROTECTION_LEVEL enumeration indicates the protection levels for a protected output that supports High-bandwidth Digital Content Protection (HDCP).
old-location: display\dxgkmdt_opm_hdcp_protection_level.htm
old-project: display
ms.assetid: e0d38f3b-19da-4118-a1d9-7d5a00bcad26
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKMDT_OPM_HDCP_PROTECTION_LEVEL
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
req.iface: 
---

# DXGKMDT_OPM_HDCP_PROTECTION_LEVEL enumeration



## -description
<p>The DXGKMDT_OPM_HDCP_PROTECTION_LEVEL enumeration indicates the protection levels for a protected output that supports High-bandwidth Digital Content Protection (HDCP). </p>


## -syntax

````
typedef enum _DXGKMDT_OPM_HDCP_PROTECTION_LEVEL { 
  DXGKMDT_OPM_HDCP_OFF          = 0,
  DXGKMDT_OPM_HDCP_ON           = 1,
  DXGKMDT_OPM_HDCP_FORCE_ULONG  = 0x7fffffff
} DXGKMDT_OPM_HDCP_PROTECTION_LEVEL;
````


## -enum-fields
<dl>

### -field <a id="DXGKMDT_OPM_HDCP_OFF"></a><a id="dxgkmdt_opm_hdcp_off"></a><b>DXGKMDT_OPM_HDCP_OFF</b>

<dd>
<p>Indicates that HDCP does not protect the output's signal. </p>
</dd>

### -field <a id="DXGKMDT_OPM_HDCP_ON"></a><a id="dxgkmdt_opm_hdcp_on"></a><b>DXGKMDT_OPM_HDCP_ON</b>

<dd>
<p>Indicates that HDCP protects the output's signal. </p>
</dd>

### -field <a id="DXGKMDT_OPM_HDCP_FORCE_ULONG"></a><a id="dxgkmdt_opm_hdcp_force_ulong"></a><b>DXGKMDT_OPM_HDCP_FORCE_ULONG</b>

<dd>
<p>Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. You should not use this value.</p>
</dd>
</dl>

## -remarks
<p>HDCP protects digital video signals from digital video output connectors. Currently, OPM can use HDCP to protect data from Digital Video Interface (DVI) and High-Definition Multimedia Interface (HDMI) connector outputs. For more information about the HDCP system, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=38728">HDCP Specification Revision 1.1</a>.</p>

<p>HDCP protects digital video signals from digital video output connectors. Currently, OPM can use HDCP to protect data from Digital Video Interface (DVI) and High-Definition Multimedia Interface (HDMI) connector outputs. For more information about the HDCP system, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=38728">HDCP Specification Revision 1.1</a>.</p>

<p>HDCP protects digital video signals from digital video output connectors. Currently, OPM can use HDCP to protect data from Digital Video Interface (DVI) and High-Definition Multimedia Interface (HDMI) connector outputs. For more information about the HDCP system, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=38728">HDCP Specification Revision 1.1</a>.</p>

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
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-configure-protected-output.md">DxgkDdiOPMConfigureProtectedOutput</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-copp-compatible-information.md">DxgkDdiOPMGetCOPPCompatibleInformation</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-information.md">DxgkDdiOPMGetInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560921">DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560925">DXGKMDT_OPM_STANDARD_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKMDT_OPM_HDCP_PROTECTION_LEVEL enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
