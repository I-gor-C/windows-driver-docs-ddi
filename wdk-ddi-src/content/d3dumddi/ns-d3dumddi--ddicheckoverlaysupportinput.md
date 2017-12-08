---
UID: NS.d3dumddi._DDICHECKOVERLAYSUPPORTINPUT
title: DDICHECKOVERLAYSUPPORTINPUT
author: windows-driver-content
description: The DDICHECKOVERLAYSUPPORTINPUT structure describes an overlay display mode that the user-mode display driver uses to verify overlay support.
old-location: display\ddicheckoverlaysupportinput.htm
old-project: display
ms.assetid: 5f15743a-1ea7-4260-b2cb-f2871acb27f9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DDICHECKOVERLAYSUPPORTINPUT, DDICHECKOVERLAYSUPPORTINPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DDICHECKOVERLAYSUPPORTINPUT is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DDICHECKOVERLAYSUPPORTINPUT
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
req.iface: 
---

# DDICHECKOVERLAYSUPPORTINPUT structure



## -description
<p>The DDICHECKOVERLAYSUPPORTINPUT structure describes an overlay display mode that the user-mode display driver uses to verify overlay support. </p>


## -syntax

````
typedef struct _DDICHECKOVERLAYSUPPORTINPUT {
  UINT                    OverlayWidth;
  UINT                    OverlayHeight;
  D3DDDIFORMAT            OverlayFormat;
  UINT                    DisplayWidth;
  UINT                    DisplayHeight;
  UINT                    DisplayRefreshRate;
  D3DDDIFORMAT            DisplayFormat;
  D3DDDI_SCANLINEORDERING DisplayScanLineOrdering;
  D3DDDI_ROTATION         DisplayRotation;
} DDICHECKOVERLAYSUPPORTINPUT;
````


## -struct-fields
<dl>

### -field OverlayWidth

<dd>
<p>[in] The width of the overlay in pixels. </p>
</dd>

### -field OverlayHeight

<dd>
<p>[in] The height of the overlay in pixels. </p>
</dd>

### -field OverlayFormat

<dd>
<p>
      [in] A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the overlay. 
     </p>
</dd>

### -field DisplayWidth

<dd>
<p>[in] The screen width of the display in pixels. </p>
</dd>

### -field DisplayHeight

<dd>
<p>[in] The screen height of the display in pixels. </p>
</dd>

### -field DisplayRefreshRate

<dd>
<p>[in] The refresh rate of the display. </p>
</dd>

### -field DisplayFormat

<dd>
<p>[in] A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the display. </p>
</dd>

### -field DisplayScanLineOrdering

<dd>
<p>[in] A <a href="..\d3dukmdt\ne-d3dukmdt-d3dddi-scanlineordering.md">D3DDDI_SCANLINEORDERING</a>-typed value that indicates how the scan lines are drawn on the display. </p>
</dd>

### -field DisplayRotation

<dd>
<p>[in] A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-rotation.md">D3DDDI_ROTATION</a>-typed value that indicates how the display is oriented. </p>
</dd>
</dl>

## -remarks
<p>The runtime specifies a pointer to a DDICHECKOVERLAYSUPPORTINPUT structure in the <b>pInfo</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a> structure. The runtime also specifies the D3DDDICAPS_CHECKOVERLAYSUPPORT value in the <b>Type</b> member of D3DDDIARG_GETCAPS. The runtime specifies these values in a call to the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a> function to determine if the driver supports the overlay that DDICHECKOVERLAYSUPPORTINPUT describes. The driver's <i>GetCaps</i> returns a pointer to a D3DOVERLAYCAPS structure that contains information about the capabilities of the overlay through the <b>pData</b> member of D3DDDIARG_GETCAPS if the driver supports the overlay.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DDICHECKOVERLAYSUPPORTINPUT is supported beginning with the Windows 7 operating system.</p>
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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-rotation.md">D3DDDI_ROTATION</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt-d3dddi-scanlineordering.md">D3DDDI_SCANLINEORDERING</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DDICHECKOVERLAYSUPPORTINPUT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
