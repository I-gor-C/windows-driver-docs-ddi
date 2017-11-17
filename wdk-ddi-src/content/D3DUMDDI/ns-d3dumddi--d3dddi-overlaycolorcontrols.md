---
UID: NS.d3dumddi._D3DDDI_OVERLAYCOLORCONTROLS
title: D3DDDI_OVERLAYCOLORCONTROLS
author: windows-driver-content
description: The D3DDDI_OVERLAYCOLORCONTROLS structure describes color-control settings for an overlay.
old-location: display\d3dddi_overlaycolorcontrols.htm
ms.assetid: 201fd9e8-74c3-4da0-b01d-f43f9aec4894
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_OVERLAYCOLORCONTROLS
req.alt-loc: d3dumddi.h
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
ms.keywords: D3DDDI_OVERLAYCOLORCONTROLS, D3DDDI_OVERLAYCOLORCONTROLS
req.iface: 
---

# D3DDDI_OVERLAYCOLORCONTROLS structure



## -description
<p>The D3DDDI_OVERLAYCOLORCONTROLS structure describes color-control settings for an overlay. </p>


## -syntax

````
typedef struct _D3DDDI_OVERLAYCOLORCONTROLS {
  INT                              BrightnessSetting;
  INT                              ContrastSetting;
  INT                              HueSetting;
  INT                              SaturationSetting;
  INT                              SharpnessSetting;
  INT                              GammaSetting;
  INT                              ColorEnableSetting;
  D3DDDI_OVERLAYCOLORCONTROLSFLAGS Flags;
} D3DDDI_OVERLAYCOLORCONTROLS;
````


## -struct-fields
<dl>

### -field <b>BrightnessSetting</b>

<dd>
<p>[in] An INT value that specifies the brightness of the output image as it is written to the overlay. This member is set if the <b>Brightness</b> bit-field flag is set in the <b>Flags</b> member.</p>
</dd>

### -field <b>ContrastSetting</b>

<dd>
<p>[in] An INT value that specifies the contrast of the output image as it is written to the overlay. This member is set if the <b>Contrast</b> bit-field flag is set in the <b>Flags</b> member.</p>
</dd>

### -field <b>HueSetting</b>

<dd>
<p>[in] An INT value that specifies the hue of the output image as it is written to the overlay. This member is set if the <b>Hue</b> bit-field flag is set in the <b>Flags</b> member.</p>
</dd>

### -field <b>SaturationSetting</b>

<dd>
<p>[in] An INT value that specifies the saturation of the output image as it is written to the overlay. This member is set if the <b>Saturation</b> bit-field flag is set in the <b>Flags</b> member.</p>
</dd>

### -field <b>SharpnessSetting</b>

<dd>
<p>[in] An INT value that specifies the sharpness of the output image as it is written to the overlay. This member is set if the <b>Sharpness</b> bit-field flag is set in the <b>Flags</b> member.</p>
</dd>

### -field <b>GammaSetting</b>

<dd>
<p>[in] An INT value that specifies the gamma setting of the output image as it is written to the overlay. This member is set if the <b>Gamma</b> bit-field flag is set in the <b>Flags</b> member.</p>
</dd>

### -field <b>ColorEnableSetting</b>

<dd>
<p>[in] An INT value that specifies the color-enable setting of the output image as it is written to the overlay. This member is set if the <b>ColorEnable</b> bit-field flag is set in the <b>Flags</b> member.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544615">D3DDDI_OVERLAYCOLORCONTROLSFLAGS</a> structure that identifies color-control settings that the overlay hardware supports.</p>
</dd>
</dl>

## -remarks


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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543169">D3DDDIARG_GETOVERLAYCOLORCONTROLS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543323">D3DDDIARG_SETOVERLAYCOLORCONTROLS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544615">D3DDDI_OVERLAYCOLORCONTROLSFLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_OVERLAYCOLORCONTROLS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
