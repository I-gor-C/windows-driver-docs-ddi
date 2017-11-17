---
UID: NE.d3dkmdt._D3DKMDT_MONITOR_CAPABILITIES_ORIGIN
title: D3DKMDT_MONITOR_CAPABILITIES_ORIGIN
author: windows-driver-content
description: The D3DKMDT_MONITOR_CAPABILITIES_ORIGIN enumeration is used to indicate where a monitor's capability information was obtained.
old-location: display\d3dkmdt_monitor_capabilities_origin.htm
ms.assetid: fbbea7d7-2bd7-4dd0-bcb8-3fc93c7474a3
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
req.alt-api: D3DKMDT_MONITOR_CAPABILITIES_ORIGIN
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

# D3DKMDT_MONITOR_CAPABILITIES_ORIGIN enumeration



## -description
<p>The D3DKMDT_MONITOR_CAPABILITIES_ORIGIN enumeration is used to indicate where a monitor's capability information was obtained.</p>


## -syntax

````
typedef enum _D3DKMDT_MONITOR_CAPABILITIES_ORIGIN { 
  D3DKMDT_MCO_UNINITIALIZED                       = 0,
  D3DKMDT_MCO_DEFAULTMONITORPROFILE               = 1,
  D3DKMDT_MCO_MONITORDESCRIPTOR                   = 2,
  D3DKMDT_MCO_MONITORDESCRIPTOR_REGISTRYOVERRIDE  = 3,
  D3DKMDT_MCO_SPECIFICCAP_REGISTRYOVERRIDE        = 4,
  D3DKMDT_MCO_DRIVER                              = 5
} D3DKMDT_MONITOR_CAPABILITIES_ORIGIN;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_MCO_UNINITIALIZED"></a><a id="d3dkmdt_mco_uninitialized"></a><b>D3DKMDT_MCO_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_MONITOR_CAPABILITIES_ORIGIN has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_MCO_DEFAULTMONITORPROFILE"></a><a id="d3dkmdt_mco_defaultmonitorprofile"></a><b>D3DKMDT_MCO_DEFAULTMONITORPROFILE</b>

<dd>
<p>Indicates that the capability information was obtained from the default monitor profile.</p>
</dd>

### -field <a id="D3DKMDT_MCO_MONITORDESCRIPTOR"></a><a id="d3dkmdt_mco_monitordescriptor"></a><b>D3DKMDT_MCO_MONITORDESCRIPTOR</b>

<dd>
<p>Indicates that the capability information was obtained from an Extended Display Information Data (EDID) descriptor.</p>
</dd>

### -field <a id="D3DKMDT_MCO_MONITORDESCRIPTOR_REGISTRYOVERRIDE"></a><a id="d3dkmdt_mco_monitordescriptor_registryoverride"></a><b>D3DKMDT_MCO_MONITORDESCRIPTOR_REGISTRYOVERRIDE</b>

<dd>
<p>Indicates that the capability information was obtained from an INF file section that overrides the monitor's EDID descriptor.</p>
</dd>

### -field <a id="D3DKMDT_MCO_SPECIFICCAP_REGISTRYOVERRIDE"></a><a id="d3dkmdt_mco_specificcap_registryoverride"></a><b>D3DKMDT_MCO_SPECIFICCAP_REGISTRYOVERRIDE</b>

<dd>
<p>Indicates that the capability information was obtained from an INF file section that overrides a single capability.</p>
</dd>

### -field <a id="D3DKMDT_MCO_DRIVER"></a><a id="d3dkmdt_mco_driver"></a><b>D3DKMDT_MCO_DRIVER</b>

<dd>
<p>Indicates that the capability information was obtained by a call to the display miniport driver's <a href="https://msdn.microsoft.com/1fa29ab6-1faa-4be6-ae87-4cac9057471d">DxgkDdiRecommendMonitorModes</a> function.</p>
</dd>
</dl>

## -remarks
<p>The <b>Origin</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546133">D3DKMDT_MONITOR_SOURCE_MODE</a> structure is a constant from the D3DKMDT_MONITOR_CAPABILITIES_ORIGIN enumeration.</p>

<p>The <b>Origin</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546133">D3DKMDT_MONITOR_SOURCE_MODE</a> structure is a constant from the D3DKMDT_MONITOR_CAPABILITIES_ORIGIN enumeration.</p>

<p>The <b>Origin</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546133">D3DKMDT_MONITOR_SOURCE_MODE</a> structure is a constant from the D3DKMDT_MONITOR_CAPABILITIES_ORIGIN enumeration.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568435">Monitor Source Mode Set Interface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_MONITOR_CAPABILITIES_ORIGIN enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
