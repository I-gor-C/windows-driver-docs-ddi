---
UID: NS.d3dumddi._FORMATOP
title: FORMATOP
author: windows-driver-content
description: The FORMATOP structure describes a surface format and operations that can be performed with such a surface.
old-location: display\formatop.htm
old-project: display
ms.assetid: e846a41a-9d9c-4ccb-a478-260f333333f1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FORMATOP, FORMATOP
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FORMATOP
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

# FORMATOP structure



## -description
<p>The <b>FORMATOP</b> structure describes a surface format and operations that can be performed with such a surface.</p>


## -syntax

````
typedef struct _FORMATOP {
  D3DDDIFORMAT Format;
  UINT         Operations;
  UINT         FlipMsTypes;
  UINT         BltMsTypes;
  UINT         PrivateFormatBitCount;
} FORMATOP;
````


## -struct-fields
<dl>

### -field <b>Format</b>

<dd>
<p>[in] The <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the surface.</p>
</dd>

### -field <b>Operations</b>

<dd>
<p>[out] A valid bitwise <b>OR</b> of the following flags that indicate the operations that can be performed on surfaces with the pixel format that is specified in the <b>Format</b> member. Some of the following flags imply that other flags should be used. If a driver sets a flag that implies other flags, the driver is not required to set the implied flags, and the Direct3D runtime determines the use of the implied flags.</p>
<dl class="indent">

### -field <a id="FORMATOP_TEXTURE__0x00000001L_"></a><a id="formatop_texture__0x00000001l_"></a><a id="FORMATOP_TEXTURE__0X00000001L_"></a><p><a id="FORMATOP_TEXTURE__0x00000001L_"></a><a id="formatop_texture__0x00000001l_"></a><a id="FORMATOP_TEXTURE__0X00000001L_"></a><b>FORMATOP_TEXTURE (0x00000001L)</b></p>


<dd>
<p>Surfaces of the specified pixel format can be used as MIP-mapped textures.</p>
</dd>

### -field <a id="FORMATOP_VOLUMETEXTURE__0x00000002L_"></a><a id="formatop_volumetexture__0x00000002l_"></a><a id="FORMATOP_VOLUMETEXTURE__0X00000002L_"></a><p><a id="FORMATOP_VOLUMETEXTURE__0x00000002L_"></a><a id="formatop_volumetexture__0x00000002l_"></a><a id="FORMATOP_VOLUMETEXTURE__0X00000002L_"></a><b>FORMATOP_VOLUMETEXTURE (0x00000002L)</b></p>


<dd>
<p>Surfaces of this format can be used as volume textures. Note that this flag is independent of FORMATOP_TEXTURE. Therefore, a pixel format can be used for volume textures and not for conventional, MIP-mapped textures.</p>
</dd>

### -field <a id="FORMATOP_CUBETEXTURE__0x00000004L_"></a><a id="formatop_cubetexture__0x00000004l_"></a><a id="FORMATOP_CUBETEXTURE__0X00000004L_"></a><p><a id="FORMATOP_CUBETEXTURE__0x00000004L_"></a><a id="formatop_cubetexture__0x00000004l_"></a><a id="FORMATOP_CUBETEXTURE__0X00000004L_"></a><b>FORMATOP_CUBETEXTURE (0x00000004L)</b></p>


<dd>
<p>Surfaces of this format can be used as cubic environment map textures. Note that this flag is independent of FORMATOP_TEXTURE. Therefore, a pixel format can be used for cubic environment map textures and not for conventional, MIP-mapped textures.</p>
</dd>

### -field <a id="FORMATOP_OFFSCREEN_RENDERTARGET__0x00000008L_"></a><a id="formatop_offscreen_rendertarget__0x00000008l_"></a><a id="FORMATOP_OFFSCREEN_RENDERTARGET__0X00000008L_"></a><p><a id="FORMATOP_OFFSCREEN_RENDERTARGET__0x00000008L_"></a><a id="formatop_offscreen_rendertarget__0x00000008l_"></a><a id="FORMATOP_OFFSCREEN_RENDERTARGET__0X00000008L_"></a><b>FORMATOP_OFFSCREEN_RENDERTARGET (0x00000008L)</b></p>


<dd>
<p>Surfaces of this format can be used as offscreen render targets, regardless of the pixel format of the display mode, if the pixel format of the current display mode was reported with FORMATOP_DISPLAYMODE and FORMATOP_3DACCELERATION. If the pixel format of the current display mode did not have these flags set, no 3-D acceleration is available in this mode even if the render target is offscreen. The FORMATOP_OFFSCREEN_RENDERTARGET flag can be combined with FORMATOP_TEXTURE to indicate that the device can render to textures of the specified pixel format.</p>
<p>The FORMATOP_OFFSCREEN_RENDERTARGET flag also implies the FORMATOP_SAME_FORMAT_RENDERTARGET and FORMATOP_SAME_FORMAT_UP_TO_ALPHA_RENDERTARGET flags.</p>
</dd>

### -field <a id="FORMATOP_SAME_FORMAT_RENDERTARGET__0x00000010L_"></a><a id="formatop_same_format_rendertarget__0x00000010l_"></a><a id="FORMATOP_SAME_FORMAT_RENDERTARGET__0X00000010L_"></a><p><a id="FORMATOP_SAME_FORMAT_RENDERTARGET__0x00000010L_"></a><a id="formatop_same_format_rendertarget__0x00000010l_"></a><a id="FORMATOP_SAME_FORMAT_RENDERTARGET__0X00000010L_"></a><b>FORMATOP_SAME_FORMAT_RENDERTARGET (0x00000010L)</b></p>


<dd>
<p>Surfaces of this format can be used as render targets but only when the pixel format of the surface matches the pixel format of the current display mode. This flag does not apply only to offscreen render targets but can be specified on the pixel formats of display modes to indicate rendering target capability. This flag can be combined with FORMATOP_TEXTURE to indicate that the device can render to textures of the specified pixel format.</p>
<p>The FORMATOP_SAME_FORMAT_RENDERTARGET flag also implies the FORMATOP_SAME_FORMAT_UP_TO_ALPHA_RENDERTARGET flag.</p>
</dd>

### -field <a id="FORMATOP_ZSTENCIL__0x00000040L_"></a><a id="formatop_zstencil__0x00000040l_"></a><a id="FORMATOP_ZSTENCIL__0X00000040L_"></a><p><a id="FORMATOP_ZSTENCIL__0x00000040L_"></a><a id="formatop_zstencil__0x00000040l_"></a><a id="FORMATOP_ZSTENCIL__0X00000040L_"></a><b>FORMATOP_ZSTENCIL (0x00000040L)</b></p>


<dd>
<p>Surfaces of this format can be used as Z/stencil buffers but only if the depth of the Z/stencil surface matches the color depth of the rendering target to which the depth buffer is attached. Use the pixel stride when you are deciding on a match between Z/stencil and color buffer depth.</p>
</dd>

### -field <a id="FORMATOP_ZSTENCIL_WITH_ARBITRARY_COLOR_DEPTH__0x00000080L_"></a><a id="formatop_zstencil_with_arbitrary_color_depth__0x00000080l_"></a><a id="FORMATOP_ZSTENCIL_WITH_ARBITRARY_COLOR_DEPTH__0X00000080L_"></a><p><a id="FORMATOP_ZSTENCIL_WITH_ARBITRARY_COLOR_DEPTH__0x00000080L_"></a><a id="formatop_zstencil_with_arbitrary_color_depth__0x00000080l_"></a><a id="FORMATOP_ZSTENCIL_WITH_ARBITRARY_COLOR_DEPTH__0X00000080L_"></a><b>FORMATOP_ZSTENCIL_WITH_ARBITRARY_COLOR_DEPTH (0x00000080L)</b></p>


<dd>
<p>Surfaces of this format can be used as Z/stencil buffers, regardless of the color depth of the render target to which the surface is attached.</p>
<p>The FORMATOP_ZSTENCIL_WITH_ARBITRARY_COLOR_DEPTH flag also implies the FORMATOP_ZSTENCIL flag.</p>
</dd>

### -field <a id="FORMATOP_SAME_FORMAT_UP_TO_ALPHA_RENDERTARGET__0x00000100L_"></a><a id="formatop_same_format_up_to_alpha_rendertarget__0x00000100l_"></a><a id="FORMATOP_SAME_FORMAT_UP_TO_ALPHA_RENDERTARGET__0X00000100L_"></a><p><a id="FORMATOP_SAME_FORMAT_UP_TO_ALPHA_RENDERTARGET__0x00000100L_"></a><a id="formatop_same_format_up_to_alpha_rendertarget__0x00000100l_"></a><a id="FORMATOP_SAME_FORMAT_UP_TO_ALPHA_RENDERTARGET__0X00000100L_"></a><b>FORMATOP_SAME_FORMAT_UP_TO_ALPHA_RENDERTARGET (0x00000100L)</b></p>


<dd>
<p>Surfaces of this format can be used as render targets if the current display mode is the same depth and the alpha channel is ignored. For example, if the device can render to A8R8G8B8 when the display mode is X8R8G8B8, the format operation list entry for A8R8G8B8 should have this flag set.</p>
</dd>

### -field <a id="FORMATOP_DISPLAYMODE__0x00000400L_"></a><a id="formatop_displaymode__0x00000400l_"></a><a id="FORMATOP_DISPLAYMODE__0X00000400L_"></a><p><a id="FORMATOP_DISPLAYMODE__0x00000400L_"></a><a id="formatop_displaymode__0x00000400l_"></a><a id="FORMATOP_DISPLAYMODE__0X00000400L_"></a><b>FORMATOP_DISPLAYMODE (0x00000400L)</b></p>


<dd>
<p>A display mode with this pixel format that is supported by the driver model (including Flip). This flag should not be set on alpha formats.</p>
</dd>

### -field <a id="FORMATOP_3DACCELERATION__0x00000800L_"></a><a id="formatop_3dacceleration__0x00000800l_"></a><a id="FORMATOP_3DACCELERATION__0X00000800L_"></a><p><a id="FORMATOP_3DACCELERATION__0x00000800L_"></a><a id="formatop_3dacceleration__0x00000800l_"></a><a id="FORMATOP_3DACCELERATION__0X00000800L_"></a><b>FORMATOP_3DACCELERATION (0x00000800L)</b></p>


<dd>
<p>The graphics accelerator can support some level of Microsoft Direct3D acceleration when in a display mode with this pixel format, and the driver can create a context in this mode (for some render target format). This flag can be used only when reporting display mode formats (by specifying the FORMATOP_DISPLAYMODE). This flag should not be used to report offscreen render targets formats.</p>
</dd>

### -field <a id="FORMATOP_PIXELSIZE__0x00001000L_"></a><a id="formatop_pixelsize__0x00001000l_"></a><a id="FORMATOP_PIXELSIZE__0X00001000L_"></a><p><a id="FORMATOP_PIXELSIZE__0x00001000L_"></a><a id="formatop_pixelsize__0x00001000l_"></a><a id="FORMATOP_PIXELSIZE__0X00001000L_"></a><b>FORMATOP_PIXELSIZE (0x00001000L)</b></p>


<dd>
<p>The driver filled in the bits per pixel for the format in the <b>PrivateFormatBitCount</b> member.</p>
<p>If the driver requires that managed surfaces and textures use a private format (a format that can be processed by the driver but not natively by the Direct3D runtime), the driver must specify FORMATOP_PIXELSIZE and the pixel size in <b>PrivateFormatBitCount</b>.</p>
</dd>

### -field <a id="FORMATOP_CONVERT_TO_ARGB__0x00002000L_"></a><a id="formatop_convert_to_argb__0x00002000l_"></a><a id="FORMATOP_CONVERT_TO_ARGB__0X00002000L_"></a><p><a id="FORMATOP_CONVERT_TO_ARGB__0x00002000L_"></a><a id="formatop_convert_to_argb__0x00002000l_"></a><a id="FORMATOP_CONVERT_TO_ARGB__0X00002000L_"></a><b>FORMATOP_CONVERT_TO_ARGB (0x00002000L)</b></p>


<dd>
<p>Source surfaces of this format can be converted to any target surface with an RGB pixel format that has the FORMATOP_MEMBEROFGROUP_ARGB flag specified.</p>
</dd>

### -field <a id="FORMATOP_OFFSCREENPLAIN__0x00004000L_"></a><a id="formatop_offscreenplain__0x00004000l_"></a><a id="FORMATOP_OFFSCREENPLAIN__0X00004000L_"></a><p><a id="FORMATOP_OFFSCREENPLAIN__0x00004000L_"></a><a id="formatop_offscreenplain__0x00004000l_"></a><a id="FORMATOP_OFFSCREENPLAIN__0X00004000L_"></a><b>FORMATOP_OFFSCREENPLAIN (0x00004000L)</b></p>


<dd>
<p>The driver can stretch to and from and color fill surfaces of this format.</p>
</dd>

### -field <a id="FORMATOP_SRGBREAD__0x00008000L_"></a><a id="formatop_srgbread__0x00008000l_"></a><a id="FORMATOP_SRGBREAD__0X00008000L_"></a><p><a id="FORMATOP_SRGBREAD__0x00008000L_"></a><a id="formatop_srgbread__0x00008000l_"></a><a id="FORMATOP_SRGBREAD__0X00008000L_"></a><b>FORMATOP_SRGBREAD (0x00008000L)</b></p>


<dd>
<p>Surfaces of this format can be read from as <a href="http://go.microsoft.com/fwlink/p/?linkid=10112">sRGB</a>-formatted textures (that is, the sampler linearizes the looked-up data).</p>
</dd>

### -field <a id="FORMATOP_BUMPMAP__0x00010000L_"></a><a id="formatop_bumpmap__0x00010000l_"></a><a id="FORMATOP_BUMPMAP__0X00010000L_"></a><p><a id="FORMATOP_BUMPMAP__0x00010000L_"></a><a id="formatop_bumpmap__0x00010000l_"></a><a id="FORMATOP_BUMPMAP__0X00010000L_"></a><b>FORMATOP_BUMPMAP (0x00010000L)</b></p>


<dd>
<p>Surfaces of this format can be used as bump environment map textures. Note that this flag is independent of FORMATOP_TEXTURE. Therefore, a pixel format can be used for bump environment map textures and not for conventional, MIP-mapped textures.</p>
</dd>

### -field <a id="FORMATOP_DMAP__0x00020000L_"></a><a id="formatop_dmap__0x00020000l_"></a><a id="FORMATOP_DMAP__0X00020000L_"></a><p><a id="FORMATOP_DMAP__0x00020000L_"></a><a id="formatop_dmap__0x00020000l_"></a><a id="FORMATOP_DMAP__0X00020000L_"></a><b>FORMATOP_DMAP (0x00020000L)</b></p>


<dd>
<p>The displacement map sampler can sample surfaces of this format.</p>
</dd>

### -field <a id="FORMATOP_NOFILTER__0x00040000L_"></a><a id="formatop_nofilter__0x00040000l_"></a><a id="FORMATOP_NOFILTER__0X00040000L_"></a><p><a id="FORMATOP_NOFILTER__0x00040000L_"></a><a id="formatop_nofilter__0x00040000l_"></a><a id="FORMATOP_NOFILTER__0X00040000L_"></a><b>FORMATOP_NOFILTER (0x00040000L)</b></p>


<dd>
<p>Surfaces of this format cannot be used with texture filtering.</p>
</dd>

### -field <a id="FORMATOP_MEMBEROFGROUP_ARGB__0x00080000L_"></a><a id="formatop_memberofgroup_argb__0x00080000l_"></a><a id="FORMATOP_MEMBEROFGROUP_ARGB__0X00080000L_"></a><p><a id="FORMATOP_MEMBEROFGROUP_ARGB__0x00080000L_"></a><a id="formatop_memberofgroup_argb__0x00080000l_"></a><a id="FORMATOP_MEMBEROFGROUP_ARGB__0X00080000L_"></a><b>FORMATOP_MEMBEROFGROUP_ARGB (0x00080000L)</b></p>


<dd>
<p>Target surfaces of this format can be converted from any source surface with a pixel format that has the FORMATOP_CONVERT_TO_ARGB flag specified. The driver can specify FORMATOP_MEMBEROFGROUP_ARGB only for ARGB surfaces with at least 5 bits of color information for each channel. That is, the D3DDDIFMT_A1R5G5B5 format is valid, but the D3DDDIFMT_A4R4G4B4 format is invalid. If the driver specifies FORMATOP_MEMBEROFGROUP_ARGB with an invalid format, the Direct3D runtime prevents the Direct3D HAL from loading. Note that although this flag indicates ARGB formats, the runtime also allows the driver to specify surfaces with XRGB formats (for example, D3DDDIFMT_X1R5G5B5).</p>
</dd>

### -field <a id="FORMATOP_SRGBWRITE__0x00100000L_"></a><a id="formatop_srgbwrite__0x00100000l_"></a><a id="FORMATOP_SRGBWRITE__0X00100000L_"></a><p><a id="FORMATOP_SRGBWRITE__0x00100000L_"></a><a id="formatop_srgbwrite__0x00100000l_"></a><a id="FORMATOP_SRGBWRITE__0X00100000L_"></a><b>FORMATOP_SRGBWRITE (0x00100000L)</b></p>


<dd>
<p>Surfaces of this format can be written to as <a href="http://go.microsoft.com/fwlink/p/?linkid=10112">sRGB</a>-formatted targets (that is, the pixel pipe delinearizes data on output to this format).</p>
</dd>

### -field <a id="FORMATOP_NOALPHABLEND__0x00200000L_"></a><a id="formatop_noalphablend__0x00200000l_"></a><a id="FORMATOP_NOALPHABLEND__0X00200000L_"></a><p><a id="FORMATOP_NOALPHABLEND__0x00200000L_"></a><a id="formatop_noalphablend__0x00200000l_"></a><a id="FORMATOP_NOALPHABLEND__0X00200000L_"></a><b>FORMATOP_NOALPHABLEND (0x00200000L)</b></p>


<dd>
<p>Surfaces of this format cannot be used with alpha blending.</p>
</dd>

### -field <a id="FORMATOP_AUTOGENMIPMAP__0x00400000L_"></a><a id="formatop_autogenmipmap__0x00400000l_"></a><a id="FORMATOP_AUTOGENMIPMAP__0X00400000L_"></a><p><a id="FORMATOP_AUTOGENMIPMAP__0x00400000L_"></a><a id="formatop_autogenmipmap__0x00400000l_"></a><a id="FORMATOP_AUTOGENMIPMAP__0X00400000L_"></a><b>FORMATOP_AUTOGENMIPMAP (0x00400000L)</b></p>


<dd>
<p>The sublevels of MIP-mapped textures with this format can be automatically generated. For the driver to receive calls to its <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-generatemipsublevels.md">GenerateMipSubLevels</a> function, this flag must be exposed.</p>
</dd>

### -field <a id="FORMATOP_VERTEXTEXTURE__0x00800000L_"></a><a id="formatop_vertextexture__0x00800000l_"></a><a id="FORMATOP_VERTEXTEXTURE__0X00800000L_"></a><p><a id="FORMATOP_VERTEXTEXTURE__0x00800000L_"></a><a id="formatop_vertextexture__0x00800000l_"></a><a id="FORMATOP_VERTEXTEXTURE__0X00800000L_"></a><b>FORMATOP_VERTEXTEXTURE (0x00800000L)</b></p>


<dd>
<p>A vertex texture sampler can use surfaces of this format. That is, only surfaces of this format can be used as vertex textures. </p>
</dd>

### -field <a id="FORMATOP_NOTEXCOORDWRAPNORMIP__0x01000000L_"></a><a id="formatop_notexcoordwrapnormip__0x01000000l_"></a><a id="FORMATOP_NOTEXCOORDWRAPNORMIP__0X01000000L_"></a><p><a id="FORMATOP_NOTEXCOORDWRAPNORMIP__0x01000000L_"></a><a id="formatop_notexcoordwrapnormip__0x01000000l_"></a><a id="FORMATOP_NOTEXCOORDWRAPNORMIP__0X01000000L_"></a><b>FORMATOP_NOTEXCOORDWRAPNORMIP (0x01000000L)</b></p>


<dd>
<p>Surfaces of this format can only be conditionally used for texture mapping of 2-D textures with dimensions that are not powers of 2. For more information, see the definitions for D3DPTEXTURECAPS_POW2 and D3DPTEXTURECAPS_NONPOW2CONDITIONAL in the <a href="..\d3dcaps\ns-d3dcaps--d3dprimcaps.md">D3DPRIMCAPS</a> reference page.</p>
</dd>

### -field <a id="FORMATOP_PLANAR__0x02000000L_"></a><a id="formatop_planar__0x02000000l_"></a><a id="FORMATOP_PLANAR__0X02000000L_"></a><p><a id="FORMATOP_PLANAR__0x02000000L_"></a><a id="formatop_planar__0x02000000l_"></a><a id="FORMATOP_PLANAR__0X02000000L_"></a><b>FORMATOP_PLANAR (0x02000000L)</b></p>


<dd>
<p>Surfaces of this format are planar versus packed. The Direct3D runtime must allocate a buffer if it calls the user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-lock.md">Lock</a> function on a surface with a planar format while the surface is lost and the typical calculation of pitch multiplied times height is not possible. Most formats are packed except for those that the Microsoft DirectX Video Acceleration uses (for example, YUV formats).</p>
</dd>

### -field <a id="FORMATOP_OVERLAY__0x04000000L_"></a><a id="formatop_overlay__0x04000000l_"></a><a id="FORMATOP_OVERLAY__0X04000000L_"></a><p><a id="FORMATOP_OVERLAY__0x04000000L_"></a><a id="formatop_overlay__0x04000000l_"></a><a id="FORMATOP_OVERLAY__0X04000000L_"></a><b>FORMATOP_OVERLAY (0x04000000L)</b></p>


<dd>
<p>Surfaces of this format are used for overlay operations.</p>
</dd>

### -field <a id="FORMATOP_CAPTURE__0x08000000L_"></a><a id="formatop_capture__0x08000000l_"></a><a id="FORMATOP_CAPTURE__0X08000000L_"></a><p><a id="FORMATOP_CAPTURE__0x08000000L_"></a><a id="formatop_capture__0x08000000l_"></a><a id="FORMATOP_CAPTURE__0X08000000L_"></a><b>FORMATOP_CAPTURE (0x08000000L)</b></p>


<dd>
<p>If the <b>VideoEncoder</b> member of the <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-resourceflags2.md">D3DDDI_RESOURCEFLAGS2</a> structure is  set, surfaces of this format can be used as capture buffers.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="FORMATOP_VIDEO_ENCODER__0x10000000L_"></a><a id="formatop_video_encoder__0x10000000l_"></a><a id="FORMATOP_VIDEO_ENCODER__0X10000000L_"></a><p><a id="FORMATOP_VIDEO_ENCODER__0x10000000L_"></a><a id="formatop_video_encoder__0x10000000l_"></a><a id="FORMATOP_VIDEO_ENCODER__0X10000000L_"></a><b>FORMATOP_VIDEO_ENCODER (0x10000000L)</b></p>


<dd>
<p>If the <b>VideoEncoder</b> member of the <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-resourceflags2.md">D3DDDI_RESOURCEFLAGS2</a> structure is  set, surfaces of this format can be used as video encoder input resources.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="FORMATOP_MULTIPLANE_OVERLAY__0x20000000L_"></a><a id="formatop_multiplane_overlay__0x20000000l_"></a><a id="FORMATOP_MULTIPLANE_OVERLAY__0X20000000L_"></a><p><a id="FORMATOP_MULTIPLANE_OVERLAY__0x20000000L_"></a><a id="formatop_multiplane_overlay__0x20000000l_"></a><a id="FORMATOP_MULTIPLANE_OVERLAY__0X20000000L_"></a><b>FORMATOP_MULTIPLANE_OVERLAY (0x20000000L)</b></p>


<dd>
<p>Surfaces of this format support a multiplane overlay.</p>
<p>Supported starting with Windows 8.</p>
</dd>
</dl>
</dd>

### -field <b>FlipMsTypes</b>

<dd>
<p>[out] A 32-bitmask for full-screen multiple sampling.</p>
</dd>

### -field <b>BltMsTypes</b>

<dd>
<p>[out] A 32-bitmask for windowed multiple sampling.</p>
</dd>

### -field <b>PrivateFormatBitCount</b>

<dd>
<p>[out] The bits per pixel of a pixel format that is private to the driver (that is, not one of the standard pixel formats that are defined by the <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a> enumeration type). </p>
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
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-resourceflags2.md">D3DDDI_RESOURCEFLAGS2</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ne-d3dumddi--d3dddicaps-type.md">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20FORMATOP structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
