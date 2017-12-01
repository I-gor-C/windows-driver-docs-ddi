---
UID: NS.d3dkmdt._DXGK_BRIGHTNESS_STATE
title: DXGK_BRIGHTNESS_STATE
author: windows-driver-content
description: Used to enable smooth brightness control for an integrated display panel.
old-location: display\dxgk_brightness_state.htm
old-project: display
ms.assetid: 60896a51-63c9-46fd-96ee-9cdbb72ac30c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_BRIGHTNESS_STATE, DXGK_BRIGHTNESS_STATE
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
req.alt-api: DXGK_BRIGHTNESS_STATE
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

# DXGK_BRIGHTNESS_STATE structure



## -description
<p>Used to enable smooth brightness control for an integrated display panel. The display miniport driver must enable smooth brightness control when its <a href="..\dispmprt\nc-dispmprt-dxgk-brightness-set-state.md">DxgkDdiSetBrightnessState</a> function is called and <i>BrightnessState</i>-&gt;<b>SmoothBrightness</b> is set to 1.<p>Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers.</p>
</p>
<p>Used by Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers.</p>


## -syntax

````
typedef struct _DXGK_BRIGHTNESS_STATE {
  union {
    struct {
      UINT SmoothBrightness  :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  };
} DXGK_BRIGHTNESS_STATE;
````


## -struct-fields
<dl>

### -field <b>SmoothBrightness</b>

<dd>
<p>[in] If set, the display miniport driver must enable smooth brightness control on the display panel.</p>
<p>Setting this member is equivalent to setting the first bit of a 32-bit value (0x00000001).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>[in] This member is reserved and should be set to zero.
Setting this member is equivalent to setting the remaining 31 bits (0xFFFFFFFE) of a 32-bit value to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>[in] A member in the union that <b>DXGK_BRIGHTNESS_STATE</b> contains that can hold one 32-bit value that identifies information about whether the display miniport driver must support smooth brightness control.</p>
</dd>
</dl>

## -remarks
<p>Do not assume that the <b>SmoothBrightness</b> members of <b>DXGK_BRIGHTNESS_STATE</b> and <a href="..\d3dkmdt\ns-d3dkmdt--dxgk-brightness-caps.md">DXGK_BRIGHTNESS_CAPS</a> are the same. <b>DXGK_BRIGHTNESS_STATE</b>.<b>SmoothBrightness</b> is used to enable  smooth brightness control on an integrated display panel. <b>DXGK_BRIGHTNESS_CAPS</b>.<b>SmoothBrightness</b> is used to query smooth brightness control capabilities of the display panel.</p>

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
<a href="..\dispmprt\nc-dispmprt-dxgk-brightness-set-state.md">DxgkDdiSetBrightnessState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BRIGHTNESS_STATE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
