---
UID: NE.d3dkmdt.DXGK_BACKLIGHT_OPTIMIZATION_LEVEL
title: DXGK_BACKLIGHT_OPTIMIZATION_LEVEL
author: windows-driver-content
description: Indicates the optimization level of brightness control. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive brightness control.
old-location: display\dxgk_backlight_optimization_level.htm
ms.assetid: 8ad096bb-0012-40fc-a038-2f25d6a59b43
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_BACKLIGHT_OPTIMIZATION_LEVEL
req.alt-loc: D3dkmdt.h
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

# DXGK_BACKLIGHT_OPTIMIZATION_LEVEL enumeration



## -description
<p>Indicates the optimization level of brightness control. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive brightness control.</p>


## -syntax

````
typedef enum  { 
  DxgkBacklightOptimizationDisable  = 0,
  DxgkBacklightOptimizationDesktop  = 1,
  DxgkBacklightOptimizationDynamic  = 2,
  DxgkBacklightOptimizationDimmed   = 3,
  DxgkBacklightOptimizationEDR      = 4
} DXGK_BACKLIGHT_OPTIMIZATION_LEVEL;
````


## -enum-fields
<dl>

### -field <a id="DxgkBacklightOptimizationDisable"></a><a id="dxgkbacklightoptimizationdisable"></a><a id="DXGKBACKLIGHTOPTIMIZATIONDISABLE"></a><b>DxgkBacklightOptimizationDisable</b>

<dd>
<p>The display miniport driver must completely disable adaptive brightness control.</p>
<p>The operating system always sets this value if the system is on AC power.</p>
</dd>

### -field <a id="DxgkBacklightOptimizationDesktop"></a><a id="dxgkbacklightoptimizationdesktop"></a><a id="DXGKBACKLIGHTOPTIMIZATIONDESKTOP"></a><b>DxgkBacklightOptimizationDesktop</b>

<dd>
<p>The display miniport driver should optimize backlight settings for desktop presentation when the system is on DC power and the other possible scenarios (disabled, dynamic, and dimmed) are not active. This type of optimization is appropriate for displaying photos, internet browsers, common document types, and video playback controls.</p>
<p>This is the default adaptive brightness setting when the system is on DC power.</p>
</dd>

### -field <a id="DxgkBacklightOptimizationDynamic"></a><a id="dxgkbacklightoptimizationdynamic"></a><a id="DXGKBACKLIGHTOPTIMIZATIONDYNAMIC"></a><b>DxgkBacklightOptimizationDynamic</b>

<dd>
<p>The display miniport driver should optimize backlight settings for presentation of full-screen video. Typical playback scenarios include playing movies and full-screen video. </p>
<p>The operating system sets this value if a full-screen Windows App is using the HTML5 video tag with JavaScript or the <a href="w_ui_xaml_ctrl.mediaelement">MediaElement</a> control with XAML.</p>
<p>The operating system sets this value only when only full-screen video content is displayed on the screen. This value is not set if playback controls or charms are displayed during video playback; in this case, adaptive brightness will not be enabled.</p>
</dd>

### -field <a id="DxgkBacklightOptimizationDimmed"></a><a id="dxgkbacklightoptimizationdimmed"></a><a id="DXGKBACKLIGHTOPTIMIZATIONDIMMED"></a><b>DxgkBacklightOptimizationDimmed</b>

<dd>
<p>The display miniport driver should optimize backlight settings to display at a low light level that is still visible even if it is not easily readable. In this scenario the display is typically set to a 30 percent brightness level.</p>
<p>After a defined period of no user input, the operating system sets this value to dim the display.</p>
</dd>

### -field <a id="DxgkBacklightOptimizationEDR"></a><a id="dxgkbacklightoptimizationedr"></a><a id="DXGKBACKLIGHTOPTIMIZATIONEDR"></a><b>DxgkBacklightOptimizationEDR</b>

<dd>
<p>Optimization level which informs the driver that the display is being driven with either High Dynamic Range or Enhanced Dynamic Range content so any backlight optimizations can be tailored to the scenario.                                                                                                                                                                                                                                                                                                         </p>
</dd>
</dl>

## -remarks
<p>For more information on usage scenarios involving <b>DXGK_BACKLIGHT_OPTIMIZATION_LEVEL</b> enumeration values, see Remarks in the <a href="https://msdn.microsoft.com/b8c37df8-ba86-4cfd-add0-49ba9c90f04a">DxgkDdiSetBacklightOptimization</a> function.</p>

<p>For more information on usage scenarios involving <b>DXGK_BACKLIGHT_OPTIMIZATION_LEVEL</b> enumeration values, see Remarks in the <a href="https://msdn.microsoft.com/b8c37df8-ba86-4cfd-add0-49ba9c90f04a">DxgkDdiSetBacklightOptimization</a> function.</p>

<p>For more information on usage scenarios involving <b>DXGK_BACKLIGHT_OPTIMIZATION_LEVEL</b> enumeration values, see Remarks in the <a href="https://msdn.microsoft.com/b8c37df8-ba86-4cfd-add0-49ba9c90f04a">DxgkDdiSetBacklightOptimization</a> function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<a href="https://msdn.microsoft.com/b8c37df8-ba86-4cfd-add0-49ba9c90f04a">DxgkDdiSetBacklightOptimization</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BACKLIGHT_OPTIMIZATION_LEVEL enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
