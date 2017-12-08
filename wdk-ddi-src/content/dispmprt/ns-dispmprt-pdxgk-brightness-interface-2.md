---
UID: NS.dispmprt.PDXGK_BRIGHTNESS_INTERFACE_2
title: PDXGK_BRIGHTNESS_INTERFACE_2
author: windows-driver-content
description: Contains pointers to functions in the Panel Brightness Control Interface Version 2. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive and smooth brightness control.
old-location: display\dxgk_brightness_interface_2.htm
old-project: display
ms.assetid: 0c0b877f-cef0-4e98-9f37-60f2d96b81bd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: PDXGK_BRIGHTNESS_INTERFACE_2, DXGK_BRIGHTNESS_INTERFACE_2, *PDXGK_BRIGHTNESS_INTERFACE_2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_BRIGHTNESS_INTERFACE_2
req.alt-loc: Dispmprt.h
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

# PDXGK_BRIGHTNESS_INTERFACE_2 structure



## -description
<p>Contains pointers to functions in the Panel Brightness Control Interface Version 2. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive and smooth brightness control.</p>


## -syntax

````
typedef struct {
  USHORT                                     Size;
  USHORT                                     Version;
  PVOID                                      Context;
  PINTERFACE_REFERENCE                       InterfaceReference;
  PINTERFACE_DEREFERENCE                     InterfaceDereference;
  DXGK_BRIGHTNESS_GET_POSSIBLE               GetPossibleBrightness;
  DXGK_BRIGHTNESS_SET                        SetBrightness;
  DXGK_BRIGHTNESS_GET                        GetBrightness;
  DXGK_BRIGHTNESS_GET_CAPS                   GetBrightnessCaps;
  DXGK_BRIGHTNESS_SET_STATE                  SetBrightnessState;
  DXGK_BRIGHTNESS_SET_BACKLIGHT_OPTIMIZATION SetBacklightOptimization;
  DXGK_BRIGHTNESS_GET_BACKLIGHT_REDUCTION    GetBacklightReduction;
} DXGK_BRIGHTNESS_INTERFACE_2, *PDXGK_BRIGHTNESS_INTERFACE_2;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>[in] The size, in bytes, of this structure.</p>
</dd>

### -field Version

<dd>
<p>[in] The version number of the brightness interface. Version number constants are defined in Dispmprt.h (for example, <b>DXGK_BRIGHTNESS_INTERFACE_VERSION_2</b>).</p>
</dd>

### -field Context

<dd>
<p>[in] A pointer to a private context block.</p>
</dd>

### -field InterfaceReference

<dd>
<p>[out] A pointer to an interface reference function that is implemented by the display miniport driver.</p>
</dd>

### -field InterfaceDereference

<dd>
<p>[out] A pointer to an interface dereference function that is implemented by the display miniport driver.</p>
</dd>

### -field GetPossibleBrightness

<dd>
<p>[out] A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgk-brightness-get-possible.md">DxgkDdiGetPossibleBrightness</a> function.</p>
</dd>

### -field SetBrightness

<dd>
<p>[out] A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgk-brightness-set.md">DxgkDdiSetBrightness</a> function.</p>
</dd>

### -field GetBrightness

<dd>
<p>[out] A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgk-brightness-get.md">DxgkDdiGetBrightness</a> function.</p>
</dd>

### -field GetBrightnessCaps

<dd>
<p>[out] A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgk-brightness-get-caps.md">DxgkDdiGetBrightnessCaps</a> function. This function is available starting with Windows 8.</p>
</dd>

### -field SetBrightnessState

<dd>
<p>[out] A pointer to the display miniport driver's  <a href="..\dispmprt\nc-dispmprt-dxgk-brightness-set-state.md">DxgkDdiSetBrightnessState</a> function. This function is available starting with Windows 8.</p>
</dd>

### -field SetBacklightOptimization

<dd>
<p>[out] A pointer to the display miniport driver's  <a href="..\dispmprt\nc-dispmprt-dxgk-brightness-set-backlight-optimization.md">DxgkDdiSetBacklightOptimization</a> function. This function is available starting with Windows 8.</p>
</dd>

### -field GetBacklightReduction

<dd>
<p>[out] A pointer to the display miniport driver's  <a href="..\dispmprt\nc-dispmprt-dxgk-brightness-get-backlight-reduction.md">DxgkDdiGetBacklightReduction</a> function. This function is available starting with Windows 8.</p>
</dd>
</dl>

## -remarks
<p>This structure provides additional members, beyond those in the <a href="display.dxgk_brightness_interface">DXGK_BRIGHTNESS_INTERFACE</a> interface, that point to driver-implemented functions that control, measure, and optimize display panel brightness and allow smooth brightness control.</p>

<p>For more information on this interface, see <a href="display.brightness_control_interface_v__2__adaptive_and_smooth_brightness_control_">Brightness Control Interface V. 2 (Adaptive and Smooth Brightness Control)</a>.</p>

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
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgk_brightness_interface">DXGK_BRIGHTNESS_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BRIGHTNESS_INTERFACE_2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
