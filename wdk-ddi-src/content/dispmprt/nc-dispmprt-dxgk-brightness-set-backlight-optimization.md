---
UID: NC.dispmprt.DXGK_BRIGHTNESS_SET_BACKLIGHT_OPTIMIZATION
title: DXGK_BRIGHTNESS_SET_BACKLIGHT_OPTIMIZATION
author: windows-driver-content
description: Called by the Microsoft DirectX graphics kernel subsystem to set the level of optimization that the display miniport driver uses to control the brightness of an integrated display panel.
old-location: display\dxgkddisetbacklightoptimization.htm
old-project: display
ms.assetid: b8c37df8-ba86-4cfd-add0-49ba9c90f04a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiSetBacklightOptimization
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
req.iface: IDebugSystemObjects4
---

# DXGK_BRIGHTNESS_SET_BACKLIGHT_OPTIMIZATION callback



## -description
<p>Called by the Microsoft DirectX graphics kernel subsystem to set the level of optimization that the display miniport driver uses to control the brightness of an integrated display panel.</p>


## -prototype

````
DXGK_BRIGHTNESS_SET_BACKLIGHT_OPTIMIZATION DxgkDdiSetBacklightOptimization;

NTSTATUS* DxgkDdiSetBacklightOptimization(
  _In_ PVOID                             Context,
  _In_ DXGK_BACKLIGHT_OPTIMIZATION_LEVEL OptimizationLevel
)
{ ... }
````


## -parameters
<dl>

### -param Context [in]

<dd>
<p>A handle to a context block that is associated with a display adapter. The display miniport driver's <a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a> function previously provided this handle to the DirectX graphics kernel subsystem.</p>
</dd>

### -param OptimizationLevel [in]

<dd>
<p>A value of type <a href="..\d3dkmdt\ne-d3dkmdt-dxgk-backlight-optimization-level.md">DXGK_BACKLIGHT_OPTIMIZATION_LEVEL</a> that indicates the optimization level of brightness control.</p>
</dd>
</dl>

## -returns
<p>Returns <b>STATUS_SUCCESS</b> if it succeeds. Otherwise, it returns one of the error codes that are defined in Ntstatus.h.</p>

## -remarks
<p>The display miniport driver can dynamically change the backlight optimization level of the integrated display panel based upon the current content on the screen.</p>

<p>The driver must respond to requests from the operating system to change the backlight optimization level in the <i>OptimizationLevel</i> parameter. Such requests are based upon system state changes.</p>

<p>After the driver has enabled adaptive brightness on the display panel in response to a call to the <a href="..\dispmprt\nc-dispmprt-dxgk-brightness-set-state.md">DxgkDdiSetBrightnessState</a> function, it must not disable adaptive brightness.</p>

<p>When the driver transitions from one backlight optimization level to another, it should make a gradual transition in brightness settings of the integrated display panel. An important  example of this type of transition is when a user adjusts video playback controls and the operating system responds by resetting the value of <i>OptimizationLevel</i> from <b>DxgkBacklightOptimizationDynamic</b> to <b>DxgkBacklightOptimizationDesktop</b>.</p>

<p>Connecting additional display devices to the system must not compromise the ability of the driver to perform adaptive brightness control on the integrated display panel.</p>

<p>This function should be made pageable.</p>

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmdt\ne-d3dkmdt-dxgk-backlight-optimization-level.md">DXGK_BACKLIGHT_OPTIMIZATION_LEVEL</a>
</dt>
<dt>
<a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgk-brightness-set-state.md">DxgkDdiSetBrightnessState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BRIGHTNESS_SET_BACKLIGHT_OPTIMIZATION callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
