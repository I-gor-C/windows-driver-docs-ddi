---
UID: NS.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2
title: DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2
author: windows-driver-content
description: DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2 is used by the display miniport driver to specify overlay plane attributes.
old-location: display\dxgk_multiplane_overlay_attributes2.htm
old-project: display
ms.assetid: 48C481EF-F3A1-48BF-B251-86D06AC125CC
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2, DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2
req.alt-loc: d3dkmddi.h
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

# DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2 structure



## -description
<p><b>DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2</b> is used by the display miniport driver to specify overlay plane attributes.
</p>


## -syntax

````
typedef struct _DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2 {
  DXGK_MULTIPLANE_OVERLAY_FLAGS              Flags;
  RECT                                       SrcRect;
  RECT                                       DstRect;
  RECT                                       ClipRect;
  D3DDDI_ROTATION                            Rotation;
  DXGK_MULTIPLANE_OVERLAY_BLEND              Blend;
  DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT VideoFrameFormat;
  D3DDDI_COLOR_SPACE_TYPE                    ColorSpaceType;
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT      StereoFormat;
  BOOL                                       StereoLeftViewFrame0;
  BOOL                                       StereoBaseViewFrame0;
  DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE   StereoFlipMode;
  DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY    StretchQuality;
  UINT                                       ColorKey;
} DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>Specifies a combination of flip operations by performing a bitwise OR operation on the values in the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-flags.md">DXGK_MULTIPLANE_OVERLAY_FLAGS</a> enumeration.</p>
</dd>

### -field <b>SrcRect</b>

<dd>
<p>Specifies the source rectangle relative to the source resource.</p>
</dd>

### -field <b>DstRect</b>

<dd>
<p>Specifies the destination rectangle relative to the monitor resolution.</p>
</dd>

### -field <b>ClipRect</b>

<dd>
<p>Specifies any additional clipping region relative to <b>DstRect</b> 
                                                            after the data has been stretched according to the values of <b>SrcRect</b> and <b>DstRect</b>.</p>
<p>The driver and hardware can use the <b>ClipRect</b> member to apply a common stretch factor 
                                                            as the clipping changes when an application occludes part of the <b>DstRect</b> destination rectangle.</p>
</dd>

### -field <b>Rotation</b>

<dd>
<p>Specifies the clockwise rotation of the overlay plane, given as a value from the <a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-rotation.md">D3DDDI_ROTATION</a> enumeration.</p>
</dd>

### -field <b>Blend</b>

<dd>
<p>Specifies the blend mode that applies to this overlay plane and the plane beneath it, given as a value from the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-blend.md">DXGK_MULTIPLANE_OVERLAY_BLEND</a> enumeration.</p>
</dd>

### -field <b>VideoFrameFormat</b>

<dd>
<p>Specifies the overlay plane's video frame format, given as a value from the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-video-frame-format.md">DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT</a> enumeration.</p>
</dd>

### -field <b>ColorSpaceType</b>

<dd>
<p>Specifies the colorspace configuration, given as a value from the <a href="..\d3dukmdt\ne-d3dukmdt-d3dddi-color-space-type.md">D3DDDI_COLOR_SPACE_TYPE</a> enumeration.</p>
</dd>

### -field <b>StereoFormat</b>

<dd>
<p>Specifies the overlay plane's video frame format, given as a value from the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stereo-format.md">DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT</a> enumeration.</p>
</dd>

### -field <b>StereoLeftViewFrame0</b>

<dd>
<p>Reserved for system use. Must always be <b>FALSE</b>.</p>
</dd>

### -field <b>StereoBaseViewFrame0</b>

<dd>
<p>Reserved for system use. Must always be <b>FALSE</b>.</p>
</dd>

### -field <b>StereoFlipMode</b>

<dd>
<p>Specifies the overlay plane's stereo flip mode, given as a value from the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stereo-flip-mode.md">DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE</a> enumeration.</p>
</dd>

### -field <b>StretchQuality</b>

<dd>
<p>Specifies the overlay plane's stretch quality, given as a value from the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stretch-quality.md">DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY</a> enumeration.</p>
</dd>

### -field <b>ColorKey</b>

<dd>
<p>Specifies the color key value used when color key blending is enabled for legacy overlays.</p>
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
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-flags.md">DXGK_MULTIPLANE_OVERLAY_FLAGS</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-rotation.md">D3DDDI_ROTATION</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-blend.md">DXGK_MULTIPLANE_OVERLAY_BLEND</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-video-frame-format.md">DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt-d3dddi-color-space-type.md">D3DDDI_COLOR_SPACE_TYPE</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stereo-format.md">DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stereo-flip-mode.md">DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stretch-quality.md">DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
