---
UID: NS.d3dkmthk._D3DKMT_BRIGHTNESS_INFO
title: D3DKMT_BRIGHTNESS_INFO
author: windows-driver-content
description: Contains information about the brightness of an integrated display panel.
old-location: display\d3dkmt_brightness_info.htm
old-project: display
ms.assetid: a620b0b2-85ce-4373-a50c-299d8ce7a91c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_BRIGHTNESS_INFO, D3DKMT_BRIGHTNESS_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_BRIGHTNESS_INFO
req.alt-loc: D3dkmthk.h
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

# D3DKMT_BRIGHTNESS_INFO structure



## -description
<p>Contains information about the brightness of an integrated display panel.</p>


## -syntax

````
typedef struct _D3DKMT_BRIGHTNESS_INFO {
  D3DKMT_BRIGHTNESS_INFO_TYPE Type;
  union {
    D3DKMT_BRIGHTNESS_POSSIBLE_LEVELS PossibleLevels;
    UCHAR                             Brightness;
    DXGK_BRIGHTNESS_CAPS              BrightnessCaps;
    DXGK_BRIGHTNESS_STATE             BrightnessState;
    DXGK_BACKLIGHT_OPTIMIZATION_LEVEL OptimizationLevel;
    DXGK_BACKLIGHT_INFO               ReductionInfo;
    BOOLEAN                           VerboseLogging;
  };
} D3DKMT_BRIGHTNESS_INFO;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>A value of type <a href="..\d3dkmthk\ne-d3dkmthk--d3dkmt-brightness-info-type.md">D3DKMT_BRIGHTNESS_INFO_TYPE</a> that  indicates the type of brightness information to retrieve or set.</p>
</dd>

### -field PossibleLevels

<dd>
<p>A <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-brightness-possible-levels.md">D3DKMT_BRIGHTNESS_POSSIBLE_LEVELS</a> structure that contains information about all possible brightness levels that the integrated display panel supports.</p>
</dd>

### -field Brightness

<dd>
<p>The current brightness level.</p>
</dd>

### -field BrightnessCaps

<dd>
<p>A <a href="..\d3dkmdt\ns-d3dkmdt--dxgk-brightness-caps.md">DXGK_BRIGHTNESS_CAPS</a> structure that represents the brightness control capabilities of the integrated display panel.</p>
</dd>

### -field BrightnessState

<dd>
<p>A <a href="..\d3dkmdt\ns-d3dkmdt--dxgk-brightness-state.md">DXGK_BRIGHTNESS_STATE</a> structure that represents the smooth brightness control capabilities of the integrated display panel.</p>
</dd>

### -field OptimizationLevel

<dd>
<p>A <a href="..\d3dkmdt\ne-d3dkmdt-dxgk-backlight-optimization-level.md">DXGK_BACKLIGHT_OPTIMIZATION_LEVEL</a> structure that represents the optimization level of brightness control.</p>
</dd>

### -field ReductionInfo

<dd>
<p>A value of type <a href="..\d3dkmdt\ns-d3dkmdt--dxgk-backlight-info.md">DXGK_BACKLIGHT_INFO</a> that provides the current absolute level of backlight reduction.</p>
</dd>

### -field VerboseLogging

<dd>
<p>A boolean value that indicates whether Event Tracing for Windows (ETW) logging of brightness information should be verbose.</p>
</dd>
</dl>

## -remarks


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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmthk\ne-d3dkmthk--d3dkmt-brightness-info-type.md">D3DKMT_BRIGHTNESS_INFO_TYPE</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-brightness-possible-levels.md">D3DKMT_BRIGHTNESS_POSSIBLE_LEVELS</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--dxgk-backlight-info.md">DXGK_BACKLIGHT_INFO</a>
</dt>
<dt>
<a href="..\d3dkmdt\ne-d3dkmdt-dxgk-backlight-optimization-level.md">DXGK_BACKLIGHT_OPTIMIZATION_LEVEL</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--dxgk-brightness-caps.md">DXGK_BRIGHTNESS_CAPS</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--dxgk-brightness-state.md">DXGK_BRIGHTNESS_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_BRIGHTNESS_INFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
