---
UID: NS.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES
title: DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES
author: windows-driver-content
description: Used by the display miniport driver to specify overlay plane attributes.
old-location: display\dxgk_multiplane_overlay_attributes.htm
old-project: display
ms.assetid: 1f48a08f-138c-44b4-b13f-efa9b448ce4f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES, DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES
req.alt-loc: D3dkmddi.h
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

# DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES structure



## -description
<p>Used by the display miniport driver to specify overlay plane attributes.</p>


## -syntax

````
typedef struct _DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES {
  DXGK_MULTIPLANE_OVERLAY_FLAGS              Flags;
  RECT                                       SrcRect;
  RECT                                       DstRect;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  RECT                                       ClipRect;
#endif 
  D3DDDI_ROTATION                            Rotation;
  DXGK_MULTIPLANE_OVERLAY_BLEND              Blend;
#if (DXGKDDI_INTERFACE_VERSION < DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  UINT                                       NumFilters;
  void                                       *pFilters;
#endif 
  DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT VideoFrameFormat;
  DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS        YCbCrFlags;
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT      StereoFormat;
  BOOL                                       StereoLeftViewFrame0;
  BOOL                                       StereoBaseViewFrame0;
  DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE   StereoFlipMode;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY    StretchQuality;
#endif 
} DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field Flags

<dd>
<p>Specifies a flip operation as one of the applicable constant values in the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-flags.md">DXGK_MULTIPLANE_OVERLAY_FLAGS</a> enumeration.</p>
</dd>

### -field SrcRect

<dd>
<p>Specifies the source rectangle, of type <a href="display.rect">RECT</a>, relative to the source resource.</p>
</dd>

### -field DstRect

<dd>
<p>Specifies the destination rectangle, of type <a href="display.rect">RECT</a>, relative to the monitor resolution.</p>
</dd>

### -field ClipRect

<dd>
<p>Specifies any additional clipping, of type <a href="display.rect">RECT</a>, relative to the <b>DstRect</b> rectangle, after the data has been stretched according to the values of <b>SrcRect</b> and <b>DstRect</b>.</p>
<p>The driver and hardware can use the <b>ClipRect</b> member to apply a common stretch factor as the clipping changes when an app occludes part of the <b>DstRect</b> destination rectangle.</p>
</dd>

### -field Rotation

<dd>
<p>Specifies the clockwise rotation of the overlay plane, given as a value from the <a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-rotation.md">D3DDDI_ROTATION</a> enumeration.</p>
</dd>

### -field Blend

<dd>
<p>Specifies the blend mode that applies to this overlay plane and the plane beneath it, given as a value from the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-blend.md">DXGK_MULTIPLANE_OVERLAY_BLEND</a> enumeration.</p>
</dd>

### -field NumFilters

<dd>
<p>Optionally specifies the number of filters that the driver and hardware implement on the overlay plane. Note that the operating system ignores this member.</p>
</dd>

### -field pFilters

<dd>
<p>An optional pointer to a buffer that specifies the filters that the driver and hardware implement on the overlay plane. Note that the operating system ignores this member.</p>
</dd>

### -field VideoFrameFormat

<dd>
<p>Specifies the overlay plane's video frame format, given as a value from the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-video-frame-format.md">DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT</a> enumeration.</p>
<div class="alert"><b>Note</b>  This value must always be <b>DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT_PROGRESSIVE</b>. The operating system does not support the other enumeration values.</div>
<div> </div>
</dd>

### -field YCbCrFlags

<dd>
<p>Specifies YUV range and conversion info given as a value from the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-ycbcr-flags.md">DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS</a> enumeration.</p>
</dd>

### -field StereoFormat

<dd>
<p>Specifies the overlay plane's video frame format, given as a value from the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stereo-format.md">DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT</a> enumeration.</p>
<div class="alert"><b>Note</b>  This value must always be <b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO</b>. The operating system does not support the other enumeration values.</div>
<div> </div>
</dd>

### -field StereoLeftViewFrame0

<dd>
<p>Reserved for system use. Must always be <b>FALSE</b>.</p>
</dd>

### -field StereoBaseViewFrame0

<dd>
<p>Reserved for system use. Must always be <b>FALSE</b>.</p>
</dd>

### -field StereoFlipMode

<dd>
<p>Specifies the overlay plane's stereo flip mode, given as a value from the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stereo-flip-mode.md">DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE</a> enumeration.</p>
<div class="alert"><b>Note</b>  This value must always be <b>DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE</b>. The operating system does not support the other enumeration values.</div>
<div> </div>
</dd>

### -field StretchQuality

<dd>
<p>Specifies the overlay plane's stretch quality, given as a value from the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stretch-quality.md">DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY</a> enumeration.</p>
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
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
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-blend.md">DXGK_MULTIPLANE_OVERLAY_BLEND</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-flags.md">DXGK_MULTIPLANE_OVERLAY_FLAGS</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stereo-flip-mode.md">DXGK_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stereo-format.md">DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-stretch-quality.md">DXGK_MULTIPLANE_OVERLAY_STRETCH_QUALITY</a>
</dt>
<dt>
<a href="..\d3dkmddi\ne-d3dkmddi--dxgk-multiplane-overlay-video-frame-format.md">DXGK_MULTIPLANE_OVERLAY_VIDEO_FRAME_FORMAT</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-ycbcr-flags.md">DXGK_MULTIPLANE_OVERLAY_YCbCr_FLAGS</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-rotation.md">D3DDDI_ROTATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
