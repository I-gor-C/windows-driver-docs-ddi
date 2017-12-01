---
UID: NC.dispmprt.DXGK_BRIGHTNESS_GET_CAPS
title: DXGK_BRIGHTNESS_GET_CAPS
author: windows-driver-content
description: Retrieves brightness control capabilities of an integrated display panel.
old-location: display\dxgkddigetbrightnesscaps.htm
old-project: display
ms.assetid: 3418dd2b-63cb-411f-9bae-390148885907
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
req.alt-api: DxgkDdiGetBrightnessCaps
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

# DXGK_BRIGHTNESS_GET_CAPS callback



## -description
<p>Retrieves brightness control capabilities of an integrated display panel.</p>


## -prototype

````
DXGK_BRIGHTNESS_GET_CAPS DxgkDdiGetBrightnessCaps;

NTSTATUS* DxgkDdiGetBrightnessCaps(
  _In_ PVOID                Context,
  _In_ DXGK_BRIGHTNESS_CAPS *BrightnessCaps
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A handle to a context block that is associated with a display adapter. The display miniport driver's <a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a> function previously provided this handle to the DirectX graphics kernel subsystem.</p>
</dd>

### -param <i>BrightnessCaps</i> [in]

<dd>
<p>A pointer to a <a href="..\d3dkmdt\ns-d3dkmdt--dxgk-brightness-caps.md">DXGK_BRIGHTNESS_CAPS</a> structure that represents the brightness control capabilities of the display panel.</p>
</dd>
</dl>

## -returns
<p>Returns <b>STATUS_SUCCESS</b> if it succeeds. Otherwise, it returns one of the error codes that are defined in Ntstatus.h.</p>

## -remarks
<p>This function lets the display miniport driver independently indicate its support for adaptive brightness control and/or smooth brightness control.</p>

<p>If the hardware includes an ambient light sensor, it must support smooth brightness control. The display miniport driver, not an embedded controller, must control the smooth brightness functioning of the integrated display panel.</p>

<p>If the driver is started by a Plug and Play (PnP) event, it must  transition smoothly from the initial brightness level set by firmware to the level set by the operating system. If additional devices are connected to the system, they must not affect the driver's ability to perform smooth brightness  control on the integrated display panel.</p>

<p>The driver must continue to support smooth brightness control even if adaptive brightness control is initiated.</p>

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
<a href="..\d3dkmdt\ns-d3dkmdt--dxgk-brightness-caps.md">DXGK_BRIGHTNESS_CAPS</a>
</dt>
<dt>
<a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BRIGHTNESS_GET_CAPS callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
