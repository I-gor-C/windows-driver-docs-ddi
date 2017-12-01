---
UID: NS.d3dkmdt._DXGK_BACKLIGHT_INFO
title: DXGK_BACKLIGHT_INFO
author: windows-driver-content
description: Contains the current level of backlight reduction that is applied to the integrated display panel. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive brightness control.
old-location: display\dxgk_backlight_info.htm
old-project: display
ms.assetid: 9008e5e6-e03c-4d34-99bd-3e6624327fcc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_BACKLIGHT_INFO, DXGK_BACKLIGHT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_BACKLIGHT_INFO
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
req.irql: 
req.iface: 
---

# DXGK_BACKLIGHT_INFO structure



## -description
<p>Contains the current level of backlight reduction that is applied to the integrated display panel. Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers that support adaptive brightness control.</p>


## -syntax

````
typedef struct _DXGK_BACKLIGHT_INFO {
  USHORT                        BacklightUsersetting;
  USHORT                        BacklightEffective;
  D3DDDI_GAMMA_RAMP_RGB256x3x16 GammaRamp;
} DXGK_BACKLIGHT_INFO;
````


## -struct-fields
<dl>

### -field <b>BacklightUsersetting</b>

<dd>
<p>[out] The absolute brightness level in hardware that corresponds to the current percent brightness level requested by the operating system.</p>
<p>This member can range in value from 0 to 65535.</p>
</dd>

### -field <b>BacklightEffective</b>

<dd>
<p>[out] The absolute brightness level in hardware that is currently set by the display miniport drive for adaptive brightness control.</p>
<p>This member can range in value from 0 to 65535.</p>
</dd>

### -field <b>GammaRamp</b>

<dd>
<p>[out] A <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-gamma-ramp-rgb256x3x16.md">D3DDDI_GAMMA_RAMP_RGB256x3x16</a> structure that contains a description of a gamma lookup table.
This lookup table represents the gamma ramp that has been optimized for backlight display by the display miniport driver from a gamma ramp set by an application.</p>
</dd>
</dl>

## -remarks
<p>For more information about the use of this structure, see Remarks of the <a href="..\dispmprt\nc-dispmprt-dxgk-brightness-get-backlight-reduction.md">DxgkDdiGetBacklightReduction</a> function.</p>

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
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-gamma-ramp-rgb256x3x16.md">D3DDDI_GAMMA_RAMP_RGB256x3x16</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgk-brightness-get-backlight-reduction.md">DxgkDdiGetBacklightReduction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BACKLIGHT_INFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
