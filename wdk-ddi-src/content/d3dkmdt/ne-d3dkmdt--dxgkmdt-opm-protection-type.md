---
UID: NE.d3dkmdt._DXGKMDT_OPM_PROTECTION_TYPE
title: DXGKMDT_OPM_PROTECTION_TYPE
author: windows-driver-content
description: The DXGKMDT_OPM_PROTECTION_TYPE enumeration indicates the type of protections that a video output supports.
old-location: display\dxgkmdt_opm_protection_type.htm
old-project: display
ms.assetid: 2e82c863-16d8-4b79-b662-fc1c766a2f05
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
req.alt-api: DXGKMDT_OPM_PROTECTION_TYPE
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

# DXGKMDT_OPM_PROTECTION_TYPE enumeration



## -description
<p>The DXGKMDT_OPM_PROTECTION_TYPE enumeration indicates the type of protections that a video output supports.</p>


## -syntax

````
typedef enum _DXGKMDT_OPM_PROTECTION_TYPE { 
  DXGKMDT_OPM_PROTECTION_TYPE_OTHER                 = 0x80000000,
  DXGKMDT_OPM_PROTECTION_TYPE_NONE                  = 0x00000000,
  DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP  = 0x00000001,
  DXGKMDT_OPM_PROTECTION_TYPE_ACP                   = 0x00000002,
  DXGKMDT_OPM_PROTECTION_TYPE_CGMSA                 = 0x00000004,
  DXGKMDT_OPM_PROTECTION_TYPE_HDCP                  = 0x00000008,
  DXGKMDT_OPM_PROTECTION_TYPE_DPCP                  = 0x00000010,
  DXGKMDT_OPM_PROTECTION_TYPE_MASK                  = 0x8000001F
} DXGKMDT_OPM_PROTECTION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_OTHER"></a><a id="dxgkmdt_opm_protection_type_other"></a><b>DXGKMDT_OPM_PROTECTION_TYPE_OTHER</b>

<dd>
<p>Indicates a protection type other than those given in the following constants of this enumeration. </p>
</dd>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_NONE"></a><a id="dxgkmdt_opm_protection_type_none"></a><b>DXGKMDT_OPM_PROTECTION_TYPE_NONE</b>

<dd>
<p>Indicates that the video output does not support any protection type. </p>
</dd>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP"></a><a id="dxgkmdt_opm_protection_type_copp_compatible_hdcp"></a><b>DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP</b>

<dd>
<p>Indicates that the protected output supports High-bandwidth Digital Content Protection (HDCP) that is compatible with Certified Output Protection Protocol (COPP). For more information about HDCP, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=38728">HDCP Specification Revision 1.1</a>. This protection type can be used only with protected output objects that have COPP semantics. OPM can use this value in a call to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-copp-compatible-information.md">DxgkDdiOPMGetCOPPCompatibleInformation</a> function to determine whether a protected output supports COPP-compatible HDCP. OPM can also use this value in a call to the driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-configure-protected-output.md">DxgkDdiOPMConfigureProtectedOutput</a> function to change the COPP-compatible HDCP protection level. </p>
</dd>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_ACP"></a><a id="dxgkmdt_opm_protection_type_acp"></a><b>DXGKMDT_OPM_PROTECTION_TYPE_ACP</b>

<dd>
<p>Indicates that the protected output supports Analog Copy Protection (ACP). ACP protects analog TV signals. Currently, OPM can use ACP to protect signals from composite outputs, S-Video outputs, or component outputs. For more information about ACP, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=71273">Rovi (formerly Macrovision)</a> website. OPM can use this value in a call to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-copp-compatible-information.md">DxgkDdiOPMGetCOPPCompatibleInformation</a> function to determine whether a protected output supports ACP. OPM can also use this value in a call to the driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-configure-protected-output.md">DxgkDdiOPMConfigureProtectedOutput</a> function to change the ACP protection level. </p>
</dd>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_CGMSA"></a><a id="dxgkmdt_opm_protection_type_cgmsa"></a><b>DXGKMDT_OPM_PROTECTION_TYPE_CGMSA</b>

<dd>
<p>Indicates that the protected output supports Content Generation Management System Analog (CGMS-A). CGMS-A protects analog TV signals. Currently, OPM can use CGMS-A to protect signals from composite outputs, S-Video outputs, or component outputs. For more information about CGMS-A, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=70568">CGMS-A article</a>. OPM can use this value in a call to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-copp-compatible-information.md">DxgkDdiOPMGetCOPPCompatibleInformation</a> function to determine whether a protected output supports CGMS-A. OPM can also use this value in a call to the driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-configure-protected-output.md">DxgkDdiOPMConfigureProtectedOutput</a> function to change the CGMS-A protection level. </p>
</dd>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_HDCP"></a><a id="dxgkmdt_opm_protection_type_hdcp"></a><b>DXGKMDT_OPM_PROTECTION_TYPE_HDCP</b>

<dd>
<p>Indicates that the protected output supports HDCP. This protection type can be used only with protected output objects that have OPM semantics. OPM can use this value in a call to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-information.md">DxgkDdiOPMGetInformation</a> function to determine whether a protected output supports HDCP. OPM can also use this value in a call to the driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-configure-protected-output.md">DxgkDdiOPMConfigureProtectedOutput</a> function to change the HDCP protection level. </p>
</dd>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_DPCP"></a><a id="dxgkmdt_opm_protection_type_dpcp"></a><b>DXGKMDT_OPM_PROTECTION_TYPE_DPCP</b>

<dd>
<p>Indicates that the protected output supports DisplayPort Copy Protection (DPCP). For more information about DisplayPort, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=71382">DisplayPort article</a>. This protection type can be used only with protected output objects that have OPM semantics. OPM can use this value in a call to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-get-information.md">DxgkDdiOPMGetInformation</a> function to determine whether a protected output supports DPCP. OPM can also use this value in a call to the driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-configure-protected-output.md">DxgkDdiOPMConfigureProtectedOutput</a> function to change the DPCP protection level. </p>
</dd>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_MASK"></a><a id="dxgkmdt_opm_protection_type_mask"></a><b>DXGKMDT_OPM_PROTECTION_TYPE_MASK</b>

<dd>
<p>A mask value that indicates the valid bitfields in a bitwise OR combination of the values from this enumeration. </p>
</dd>
</dl>

## -remarks
<p>DXGKMDT_OPM_PROTECTION_TYPE_HDCP and DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP are used to turn HDCP on or off and to determine if HDCP is on or off. </p>

<p>If a protected output supports DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP, it supports HDCP repeaters, and an application handles HDCP revocation. If a protected output supports DXGKMDT_OPM_PROTECTION_TYPE_HDCP, it supports HDCP repeaters and handles HDCP revocation.</p>

<p>DXGKMDT_OPM_PROTECTION_TYPE_HDCP and DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP are used to turn HDCP on or off and to determine if HDCP is on or off. </p>

<p>If a protected output supports DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP, it supports HDCP repeaters, and an application handles HDCP revocation. If a protected output supports DXGKMDT_OPM_PROTECTION_TYPE_HDCP, it supports HDCP repeaters and handles HDCP revocation.</p>

<p>DXGKMDT_OPM_PROTECTION_TYPE_HDCP and DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP are used to turn HDCP on or off and to determine if HDCP is on or off. </p>

<p>If a protected output supports DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP, it supports HDCP repeaters, and an application handles HDCP revocation. If a protected output supports DXGKMDT_OPM_PROTECTION_TYPE_HDCP, it supports HDCP repeaters and handles HDCP revocation.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKMDT_OPM_PROTECTION_TYPE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
