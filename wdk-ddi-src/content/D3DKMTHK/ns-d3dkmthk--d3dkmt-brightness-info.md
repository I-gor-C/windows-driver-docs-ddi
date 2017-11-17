---
UID: NS.d3dkmthk._D3DKMT_BRIGHTNESS_INFO
title: D3DKMT_BRIGHTNESS_INFO
author: windows-driver-content
description: Contains information about the brightness of an integrated display panel.
old-location: display\d3dkmt_brightness_info.htm
ms.assetid: a620b0b2-85ce-4373-a50c-299d8ce7a91c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
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
ms.keywords: D3DKMT_BRIGHTNESS_INFO, D3DKMT_BRIGHTNESS_INFO
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

### -field <b>Type</b>

<dd>
<p>A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/jj128342">D3DKMT_BRIGHTNESS_INFO_TYPE</a> that  indicates the type of brightness information to retrieve or set.</p>
</dd>

### -field <b>PossibleLevels</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/jj128343">D3DKMT_BRIGHTNESS_POSSIBLE_LEVELS</a> structure that contains information about all possible brightness levels that the integrated display panel supports.</p>
</dd>

### -field <b>Brightness</b>

<dd>
<p>The current brightness level.</p>
</dd>

### -field <b>BrightnessCaps</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/jj128359">DXGK_BRIGHTNESS_CAPS</a> structure that represents the brightness control capabilities of the integrated display panel.</p>
</dd>

### -field <b>BrightnessState</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/jj128361">DXGK_BRIGHTNESS_STATE</a> structure that represents the smooth brightness control capabilities of the integrated display panel.</p>
</dd>

### -field <b>OptimizationLevel</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/jj128358">DXGK_BACKLIGHT_OPTIMIZATION_LEVEL</a> structure that represents the optimization level of brightness control.</p>
</dd>

### -field <b>ReductionInfo</b>

<dd>
<p>A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/jj128357">DXGK_BACKLIGHT_INFO</a> that provides the current absolute level of backlight reduction.</p>
</dd>

### -field <b>VerboseLogging</b>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/jj128342">D3DKMT_BRIGHTNESS_INFO_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj128343">D3DKMT_BRIGHTNESS_POSSIBLE_LEVELS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj128357">DXGK_BACKLIGHT_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj128358">DXGK_BACKLIGHT_OPTIMIZATION_LEVEL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj128359">DXGK_BRIGHTNESS_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj128361">DXGK_BRIGHTNESS_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_BRIGHTNESS_INFO structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
