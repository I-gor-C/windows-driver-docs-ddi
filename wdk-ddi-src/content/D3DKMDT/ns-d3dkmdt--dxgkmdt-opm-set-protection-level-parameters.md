---
UID: NS.d3dkmdt._DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS
title: DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS
author: windows-driver-content
description: The DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS structure contains parameters to set the protection level of a protected output in a call to the DxgkDdiOPMConfigureProtectedOutput function.
old-location: display\dxgkmdt_opm_set_protection_level_parameters.htm
ms.assetid: e5b35b0d-c7ad-4a67-8552-13df4c9c2b84
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS
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
req.irql: 
ms.keywords: DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS, DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS
req.iface: 
---

# DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS structure



## -description
<p>The DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS structure contains parameters to set the protection level of a protected output in a call to the <a href="https://msdn.microsoft.com/a7829587-c1e7-43ec-a0bb-92bca94b7c3d">DxgkDdiOPMConfigureProtectedOutput</a> function.</p>


## -syntax

````
typedef struct _DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS {
  ULONG ulProtectionType;
  ULONG ulProtectionLevel;
  ULONG Reserved;
  ULONG Reserved2;
} DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>ulProtectionType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560898">DXGKMDT_OPM_PROTECTION_TYPE</a>-typed value that indicates the protection type to set a protection level for. </p>
</dd>

### -field <b>ulProtectionLevel</b>

<dd>
<p>A value that specifies the protection level to set for one of the following protection types that is specified in the <b>ulProtectionType</b> member:  </p>
<p></p>
<dl>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_ACP"></a><a id="dxgkmdt_opm_protection_type_acp"></a>DXGKMDT_OPM_PROTECTION_TYPE_ACP

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560834">DXGKMDT_OPM_ACP_PROTECTION_LEVEL</a>-typed value that identifies the Analog Copy Protection (ACP) level that the protected output uses.</p>
</dd>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_CGMSA"></a><a id="dxgkmdt_opm_protection_type_cgmsa"></a>DXGKMDT_OPM_PROTECTION_TYPE_CGMSA

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560846">DXGKMDT_OPM_CGMSA</a>-typed value that identifies the Content Generation Management System Analog (CGMS-A) protection level that the protected output uses.</p>
</dd>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_HDCP_or_DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP"></a><a id="dxgkmdt_opm_protection_type_hdcp_or_dxgkmdt_opm_protection_type_copp_compatible_hdcp"></a><a id="DXGKMDT_OPM_PROTECTION_TYPE_HDCP_OR_DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP"></a>DXGKMDT_OPM_PROTECTION_TYPE_HDCP or DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560878">DXGKMDT_OPM_HDCP_PROTECTION_LEVEL</a>-typed value that identifies the High-bandwidth Digital Content Protection (HDCP) level that the protected output uses. Protected outputs with COPP semantics can use only DXGKMDT_OPM_PROTECTION_TYPE_COPP_COMPATIBLE_HDCP; protected outputs with OPM semantics can use only DXGKMDT_OPM_PROTECTION_TYPE_HDCP. </p>
</dd>

### -field <a id="DXGKMDT_OPM_PROTECTION_TYPE_DPCP"></a><a id="dxgkmdt_opm_protection_type_dpcp"></a>DXGKMDT_OPM_PROTECTION_TYPE_DPCP

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560861">DXGKMDT_OPM_DPCP_PROTECTION_LEVEL</a>-typed value that identifies the DisplayPort Copy Protection (DPCP) protection level that the protected output uses.</p>
</dd>
</dl>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Must be set to zero. </p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. Must be set to zero. </p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/a7829587-c1e7-43ec-a0bb-92bca94b7c3d">DxgkDdiOPMConfigureProtectedOutput</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560834">DXGKMDT_OPM_ACP_PROTECTION_LEVEL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560846">DXGKMDT_OPM_CGMSA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560861">DXGKMDT_OPM_DPCP_PROTECTION_LEVEL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560878">DXGKMDT_OPM_HDCP_PROTECTION_LEVEL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560898">DXGKMDT_OPM_PROTECTION_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
