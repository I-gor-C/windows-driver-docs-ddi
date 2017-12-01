---
UID: NE.d3dkmdt._DXGKMDT_OPM_CGMSA
title: DXGKMDT_OPM_CGMSA
author: windows-driver-content
description: The DXGKMDT_OPM_CGMSA enumeration indicates the protection levels for a protected output that supports Content Generation Management System Analog (CGMS-A).
old-location: display\dxgkmdt_opm_cgmsa.htm
old-project: display
ms.assetid: 1318d00e-aac3-4ff2-89a2-bcabcdff6331
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
req.alt-api: DXGKMDT_OPM_CGMSA
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

# DXGKMDT_OPM_CGMSA enumeration



## -description
<p>The DXGKMDT_OPM_CGMSA enumeration indicates the protection levels for a protected output that supports Content Generation Management System Analog (CGMS-A). </p>


## -syntax

````
typedef enum _DXGKMDT_OPM_CGMSA { 
  DXGKMDT_OPM_CGMSA_OFF                        = 0,
  DXGKMDT_OPM_CGMSA_COPY_FREELY                = 1,
  DXGKMDT_OPM_CGMSA_COPY_NO_MORE               = 2,
  DXGKMDT_OPM_CGMSA_COPY_ONE_GENERATION        = 3,
  DXGKMDT_OPM_CGMSA_COPY_NEVER                 = 4,
  DXGKMDT_OPM_REDISTRIBUTION_CONTROL_REQUIRED  = 0x08
} DXGKMDT_OPM_CGMSA;
````


## -enum-fields
<dl>

### -field <a id="DXGKMDT_OPM_CGMSA_OFF"></a><a id="dxgkmdt_opm_cgmsa_off"></a><b>DXGKMDT_OPM_CGMSA_OFF</b>

<dd>
<p>Indicates that a video output's signal is not protected with the CGMS-A output protection scheme. </p>
</dd>

### -field <a id="DXGKMDT_OPM_CGMSA_COPY_FREELY"></a><a id="dxgkmdt_opm_cgmsa_copy_freely"></a><b>DXGKMDT_OPM_CGMSA_COPY_FREELY</b>

<dd>
<p>Indicates that the signal from a physical video output can be copied an infinite number of times. </p>
</dd>

### -field <a id="DXGKMDT_OPM_CGMSA_COPY_NO_MORE"></a><a id="dxgkmdt_opm_cgmsa_copy_no_more"></a><b>DXGKMDT_OPM_CGMSA_COPY_NO_MORE</b>

<dd>
<p>Indicates that the signal from a physical video output cannot be copied because the signal was already copied once. </p>
</dd>

### -field <a id="DXGKMDT_OPM_CGMSA_COPY_ONE_GENERATION"></a><a id="dxgkmdt_opm_cgmsa_copy_one_generation"></a><b>DXGKMDT_OPM_CGMSA_COPY_ONE_GENERATION</b>

<dd>
<p>Indicates that the signal from a physical video output can be copied once. However, the copy can never be copied. </p>
</dd>

### -field <a id="DXGKMDT_OPM_CGMSA_COPY_NEVER"></a><a id="dxgkmdt_opm_cgmsa_copy_never"></a><b>DXGKMDT_OPM_CGMSA_COPY_NEVER</b>

<dd>
<p>Indicates that the signal from a physical video output can never be copied. </p>
</dd>

### -field <a id="DXGKMDT_OPM_REDISTRIBUTION_CONTROL_REQUIRED"></a><a id="dxgkmdt_opm_redistribution_control_required"></a><b>DXGKMDT_OPM_REDISTRIBUTION_CONTROL_REQUIRED</b>

<dd>
<p>Indicates that the technological control of consumer redistribution is enabled. </p>
<p>The five preceding protection levels can be bitwise OR combined  with the DXGKMDT_OPM_REDISTRIBUTION_CONTROL_REQUIRED to turn on redistribution control. </p>
<p>DXGKMDT_OPM_REDISTRIBUTION_CONTROL_REQUIRED corresponds to the CEA-805-A standard's Redistribution Control Information (RCI) bit. For more information about the RCI bit, see the definition of the RCI bit in section 4.4.3.8 in the CEA-805-A standard. For more information about this standard, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=71276">Consumer Electronics Association</a> website. </p>
<p>DXGKMDT_OPM_REDISTRIBUTION_CONTROL_REQUIRED can be used only if a protected output has COPP semantics. A protected output must enable redistribution control if the DirectX graphics kernel subsystem passes DXGKMDT_OPM_REDISTRIBUTION_CONTROL_REQUIRED to the <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-configure-protected-output.md">DxgkDdiOPMConfigureProtectedOutput</a> function. <i>DxgkDdiOPMConfigureProtectedOutput</i> must fail if DXGKMDT_OPM_REDISTRIBUTION_CONTROL_REQUIRED is passed to it and the display miniport driver cannot enable redistribution control for any reason. </p>
</dd>
</dl>

## -remarks
<p>CGMS-A protects analog TV signals. Currently, OPM can use CGMS-A to protect signals from composite outputs, S-Video outputs, or component outputs. For more information about CGMS-A, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=70568">CGMS-A article</a>. </p>

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
<a href="..\d3dkmdt\ns-d3dkmdt--dxgkmdt-opm-set-protection-level-parameters.md">DXGKMDT_OPM_SET_PROTECTION_LEVEL_PARAMETERS</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--dxgkmdt-opm-standard-information.md">DXGKMDT_OPM_STANDARD_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKMDT_OPM_CGMSA enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
