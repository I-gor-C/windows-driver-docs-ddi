---
UID: NE.d3dkmthk._D3DKMDT_MODE_PRUNING_REASON
title: D3DKMDT_MODE_PRUNING_REASON
author: windows-driver-content
description: The D3DKMDT_MODE_PRUNING_REASON enumeration type contains values that identify the reason why the monitor either supports a display mode or does not support a display mode.
old-location: display\d3dkmdt_mode_pruning_reason.htm
ms.assetid: 41b80b84-3ed6-4ca3-a2ca-63982585d6dc
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_MODE_PRUNING_REASON
req.alt-loc: d3dkmthk.h
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
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
req.iface: 
---

# D3DKMDT_MODE_PRUNING_REASON enumeration



## -description
<p>The D3DKMDT_MODE_PRUNING_REASON enumeration type contains values that identify the reason why the monitor either supports a display mode or does not support a display mode. </p>


## -syntax

````
typedef enum _D3DKMDT_MODE_PRUNING_REASON { 
  D3DKMDT_MPR_UNINITIALIZED                                = 0,
  D3DKMDT_MPR_ALLCAPS                                      = 1,
  D3DKMDT_MPR_DESCRIPTOR_MONITOR_SOURCE_MODE               = 2,
  D3DKMDT_MPR_DESCRIPTOR_MONITOR_FREQUENCY_RANGE           = 3,
  D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_SOURCE_MODE      = 4,
  D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_FREQUENCY_RANGE  = 5,
  D3DKMDT_MPR_DEFAULT_PROFILE_MONITOR_SOURCE_MODE          = 6,
  D3DKMDT_MPR_DRIVER_RECOMMENDED_MONITOR_SOURCE_MODE       = 7,
  D3DKMDT_MPR_MONITOR_FREQUENCY_RANGE_OVERRIDE             = 8,
  D3DKMDT_MPR_CLONE_PATH_PRUNED                            = 9,
  D3DKMDT_MPR_MAXVALID                                     = 10
} D3DKMDT_MODE_PRUNING_REASON;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_MPR_UNINITIALIZED"></a><a id="d3dkmdt_mpr_uninitialized"></a><b>D3DKMDT_MPR_UNINITIALIZED</b>

<dd>
<p>A variable of type D3DKMDT_MODE_PRUNING_REASON has not yet been assigned a meaningful value. </p>
</dd>

### -field <a id="D3DKMDT_MPR_ALLCAPS"></a><a id="d3dkmdt_mpr_allcaps"></a><b>D3DKMDT_MPR_ALLCAPS</b>

<dd>
<p>The monitor does not support the display mode because none of the available monitor capabilites imply support of the display mode. </p>
</dd>

### -field <a id="D3DKMDT_MPR_DESCRIPTOR_MONITOR_SOURCE_MODE"></a><a id="d3dkmdt_mpr_descriptor_monitor_source_mode"></a><b>D3DKMDT_MPR_DESCRIPTOR_MONITOR_SOURCE_MODE</b>

<dd>
<p>The monitor supports the display mode because of the monitor source mode in the monitor descriptor.</p>
</dd>

### -field <a id="D3DKMDT_MPR_DESCRIPTOR_MONITOR_FREQUENCY_RANGE"></a><a id="d3dkmdt_mpr_descriptor_monitor_frequency_range"></a><b>D3DKMDT_MPR_DESCRIPTOR_MONITOR_FREQUENCY_RANGE</b>

<dd>
<p>The monitor does not support the display mode because of the monitor frequency range in the monitor descriptor. </p>
</dd>

### -field <a id="D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_SOURCE_MODE"></a><a id="d3dkmdt_mpr_descriptor_override_monitor_source_mode"></a><b>D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_SOURCE_MODE</b>

<dd>
<p>The monitor supports the display mode because of the monitor source mode in the monitor descriptor override. </p>
</dd>

### -field <a id="D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_FREQUENCY_RANGE"></a><a id="d3dkmdt_mpr_descriptor_override_monitor_frequency_range"></a><b>D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_FREQUENCY_RANGE</b>

<dd>
<p>The monitor does not support the display mode because of the monitor frequency range in the monitor descriptor override. </p>
</dd>

### -field <a id="D3DKMDT_MPR_DEFAULT_PROFILE_MONITOR_SOURCE_MODE"></a><a id="d3dkmdt_mpr_default_profile_monitor_source_mode"></a><b>D3DKMDT_MPR_DEFAULT_PROFILE_MONITOR_SOURCE_MODE</b>

<dd>
<p>The monitor supports the display mode because of the monitor source mode in the default monitor profile. </p>
</dd>

### -field <a id="D3DKMDT_MPR_DRIVER_RECOMMENDED_MONITOR_SOURCE_MODE"></a><a id="d3dkmdt_mpr_driver_recommended_monitor_source_mode"></a><b>D3DKMDT_MPR_DRIVER_RECOMMENDED_MONITOR_SOURCE_MODE</b>

<dd>
<p>The monitor supports the display mode because of the monitor source mode that the display miniport driver recommends. </p>
</dd>

### -field <a id="D3DKMDT_MPR_MONITOR_FREQUENCY_RANGE_OVERRIDE"></a><a id="d3dkmdt_mpr_monitor_frequency_range_override"></a><b>D3DKMDT_MPR_MONITOR_FREQUENCY_RANGE_OVERRIDE</b>

<dd>
<p>The monitor supports the display mode because of the monitor frequency range override. </p>
</dd>

### -field <a id="D3DKMDT_MPR_CLONE_PATH_PRUNED"></a><a id="d3dkmdt_mpr_clone_path_pruned"></a><b>D3DKMDT_MPR_CLONE_PATH_PRUNED</b>

<dd>
<p>Supported in Windows 7 and later versions.</p>
<p>The display mode is pruned (that is, the monitor does not support the display mode) because other paths in the clone cluster have no mode supported by the monitor. </p>
</dd>

### -field <a id="D3DKMDT_MPR_MAXVALID"></a><a id="d3dkmdt_mpr_maxvalid"></a><b>D3DKMDT_MPR_MAXVALID</b>

<dd>
<p>Valid enumeration values were exceeded. </p>
</dd>
</dl>

## -remarks
<p>The setting of the <b>ValidatedAgainstMonitorCaps</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545991">D3DKMDT_DISPLAYMODE_FLAGS</a> structure indicates whether the monitor supports a display mode or not. If the monitor does not support a display mode, the operating system removes the display mode from the list of display modes that are available to the monitor.</p>

<p>When a display mode is supported, the reason type can be one of the following:</p>

<p>D3DKMDT_MPR_DRIVER_RECOMMENDED_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_DESCRIPTOR_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_DEFAULT_PROFILE_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_MONITOR_FREQUENCY_RANGE_OVERRIDE</p>

<p>When a display mode is not supported, the reason type can be one of the following:</p>

<p>D3DKMDT_MPR_DESCRIPTOR_MONITOR_FREQUENCY_RANGE</p>

<p>D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_FREQUENCY_RANGE</p>

<p>D3DKMDT_MPR_ALLCAPS</p>

<p>The setting of the <b>ValidatedAgainstMonitorCaps</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545991">D3DKMDT_DISPLAYMODE_FLAGS</a> structure indicates whether the monitor supports a display mode or not. If the monitor does not support a display mode, the operating system removes the display mode from the list of display modes that are available to the monitor.</p>

<p>When a display mode is supported, the reason type can be one of the following:</p>

<p>D3DKMDT_MPR_DRIVER_RECOMMENDED_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_DESCRIPTOR_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_DEFAULT_PROFILE_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_MONITOR_FREQUENCY_RANGE_OVERRIDE</p>

<p>When a display mode is not supported, the reason type can be one of the following:</p>

<p>D3DKMDT_MPR_DESCRIPTOR_MONITOR_FREQUENCY_RANGE</p>

<p>D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_FREQUENCY_RANGE</p>

<p>D3DKMDT_MPR_ALLCAPS</p>

<p>The setting of the <b>ValidatedAgainstMonitorCaps</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545991">D3DKMDT_DISPLAYMODE_FLAGS</a> structure indicates whether the monitor supports a display mode or not. If the monitor does not support a display mode, the operating system removes the display mode from the list of display modes that are available to the monitor.</p>

<p>When a display mode is supported, the reason type can be one of the following:</p>

<p>D3DKMDT_MPR_DRIVER_RECOMMENDED_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_DESCRIPTOR_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_DEFAULT_PROFILE_MONITOR_SOURCE_MODE</p>

<p>D3DKMDT_MPR_MONITOR_FREQUENCY_RANGE_OVERRIDE</p>

<p>When a display mode is not supported, the reason type can be one of the following:</p>

<p>D3DKMDT_MPR_DESCRIPTOR_MONITOR_FREQUENCY_RANGE</p>

<p>D3DKMDT_MPR_DESCRIPTOR_OVERRIDE_MONITOR_FREQUENCY_RANGE</p>

<p>D3DKMDT_MPR_ALLCAPS</p>

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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545991">D3DKMDT_DISPLAYMODE_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_MODE_PRUNING_REASON enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
