---
UID: NS.ksmedia._DDPIXELFORMAT
title: DDPIXELFORMAT
author: windows-driver-content
description: The DDPIXELFORMAT structure describes the pixel format of a DirectDrawSurface object.
old-location: display\ddpixelformat.htm
old-project: display
ms.assetid: bbc26c03-c154-4b1e-883e-2942b59ded02
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DDPIXELFORMAT, DDPIXELFORMAT, *LPDDPIXELFORMAT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ddraw.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DDPIXELFORMAT
req.alt-loc: ksmedia.h
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

# DDPIXELFORMAT structure



## -description
<p>The DDPIXELFORMAT structure describes the pixel format of a DirectDrawSurface object. </p>


## -syntax

````
typedef struct _DDPIXELFORMAT {
  DWORD dwSize;
  DWORD dwFlags;
  DWORD dwFourCC;
  union {
    DWORD dwRGBBitCount;
    DWORD dwYUVBitCount;
    DWORD dwZBufferBitDepth;
    DWORD dwAlphaBitDepth;
    DWORD dwLuminanceBitCount;
    DWORD dwBumpBitCount;
    DWORD dwPrivateFormatBitCount;
  };
  union {
    DWORD dwRBitMask;
    DWORD dwYBitMask;
    DWORD dwStencilBitDepth;
    DWORD dwLuminanceBitMask;
    DWORD dwBumpDuBitMask;
    DWORD dwOperations;
  };
  union {
    DWORD  dwGBitMask;
    DWORD  dwUBitMask;
    DWORD  dwZBitMask;
    DWORD  dwBumpDvBitMask;
    struct {
      WORD wFlipMSTypes;
      WORD wBltMSTypes;
    } MultiSampleCaps;
  };
  union {
    DWORD dwBBitMask;
    DWORD dwVBitMask;
    DWORD dwStencilBitMask;
    DWORD dwBumpLuminanceBitMask;
  };
  union {
    DWORD dwRGBAlphaBitMask, dwYUVAlphaBitMask;
    DWORD dwLuminanceAlphaBitMask;
    DWORD dwRGBZBitMask, dwYUVZBitMask;
  };
} DDPIXELFORMAT, *LPDDPIXELFORMAT;
````


## -struct-fields
<dl>

### -field dwSize

<dd>
<p>Specifies the size in bytes of the DDPIXELFORMAT structure. The driver must initialize this member before the structure is used.</p>
<p><b>DirectX 9.0 and later versions only.</b> Specifies, on input, the version of the Microsoft DirectX runtime being used by the application. This member is set to DD_RUNTIME_VERSION, which is 0x00000900 for DirectX 9.0, in the <b>format</b> member of the <a href="..\d3dhal\ns-d3dhal--dd-getformatdata.md">DD_GETFORMATDATA</a> structure for a D3DGDI2_TYPE_GETFORMAT query.</p>
</dd>

### -field dwFlags

<dd>
<p>Indicates a set of flags that specify optional control flags. This member is a bitwise OR of any of the following values:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DDPF_ALPHA</p>
</td>
<td>
<p>The pixel format describes an alpha-only surface.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_ALPHAPIXELS</p>
</td>
<td>
<p>The surface has alpha channel information in the pixel format.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_ALPHAPREMULT</p>
</td>
<td>
<p>The color components in the pixel are premultiplied by the alpha value in the pixel. If this flag is set, the DDPF_ALPHAPIXELS flag must also be set. If this flag is not set but the DDPF_ALPHAPIXELS flag is set, the color components in the pixel format are not premultiplied by alpha. In this case, the color components must be multiplied by the alpha value at the time that an alpha-blending operation is performed.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_BUMPDUDV</p>
</td>
<td>
<p>Bump map dUdV data in the pixel format is valid.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_BUMPHEIGHT</p>
</td>
<td>
<p>Bump map height data in the pixel format is valid.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_COMPRESSED</p>
</td>
<td>
<p>The surface accepts pixel data in the specified format and compresses it during the write operation.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_D3DFORMAT</p>
</td>
<td>
<p>Indicates a DirectX 8.0 and later format capability entry in the texture format list. This flag is not exposed to applications.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_FOURCC</p>
</td>
<td>
<p>The <a href="wdkgloss.f#wdkgloss.fourcc#wdkgloss.fourcc"><i>FOURCC</i></a> code is valid.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_LUMINANCE</p>
</td>
<td>
<p>Luminance data in the pixel format is valid. Use this flag for luminance-only or luminance-plus-alpha surfaces; the bit depth is then specified in the <b>dwLuminanceBitCount</b> member.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_LUMINANCEPIXELS</p>
</td>
<td>
<p>Luminance data in the pixel format is valid. Use this flag when hanging luminance off, for example, bumpmap surfaces. The bitmask for the luminance portion of the pixel is then specified in the <b>dwBumpLuminanceBitMask</b> member.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_NOVEL_TEXTURE_FORMAT</p>
</td>
<td>
<p>Indicates a new surface format that the runtime might not expose to all applications.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_PALETTEINDEXED1</p>
</td>
<td>
<p>The surface is 1-bit color indexed.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_PALETTEINDEXED2</p>
</td>
<td>
<p>The surface is 2-bit color indexed.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_PALETTEINDEXED4</p>
</td>
<td>
<p>The surface is 4-bit color indexed.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_PALETTEINDEXED8</p>
</td>
<td>
<p>The surface is 8-bit color indexed.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_PALETTEINDEXEDTO8</p>
</td>
<td>
<p>The surface is 1-, 2-, or 4-bit color indexed to an 8-bit palette.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_RGB</p>
</td>
<td>
<p>The RGB data in the pixel format structure is valid.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_RGBTOYUV</p>
</td>
<td>
<p>The surface accepts RGB data and translates it during the write operation to YUV data. The format of the data to be written is contained in the pixel format structure. The DDPF_RGB flag is set.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_STENCILBUFFER</p>
</td>
<td>
<p>The surface encodes stencil and depth information in each pixel of the z-buffer.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_YUV</p>
</td>
<td>
<p>The YUV data in the pixel format structure is valid.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_ZBUFFER</p>
</td>
<td>
<p>The pixel format describes a z-buffer-only surface.</p>
</td>
</tr>
<tr>
<td>
<p>DDPF_ZPIXELS</p>
</td>
<td>
<p>The surface is in RGBZ format.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field dwFourCC

<dd>
<p>Specifies a surface format code including any of the codes in the D3DFORMAT enumerated type. Some <a href="wdkgloss.f#wdkgloss.fourcc#wdkgloss.fourcc"><i>FOURCC</i></a> codes are part of D3DFORMAT. For more information about D3DFORMAT, see the SDK documentation. Hardware vendors can also define and supply format codes that are specific to their hardware. </p>
</dd>

### -field dwRGBBitCount

<dd>
<p>Specifies the number of RGB bits per pixel (4, 8, 16, 24, or 32). </p>
</dd>

### -field dwYUVBitCount

<dd>
<p>Specifies the number of YUV bits per pixel. </p>
</dd>

### -field dwZBufferBitDepth

<dd>
<p>Specifies the Z-buffer bit depth (8, 16, 24, or 32 bits). </p>
</dd>

### -field dwAlphaBitDepth

<dd>
<p>Specifies the Alpha channel bit depth. </p>
</dd>

### -field dwLuminanceBitCount

<dd>
<p>Specifies the number of bits per pixel.</p>
</dd>

### -field dwBumpBitCount

<dd>
<p>Specifies the total number of bits per "bumpel" (bump-map texel).</p>
</dd>

### -field dwPrivateFormatBitCount

<dd>
<p>Specifies the bits per pixel of a pixel format private to the driver (that is, not one of the standard ones defined by Microsoft Direct3D).</p>
</dd>

### -field dwRBitMask

<dd>
<p>Specifies the mask for red bits. </p>
</dd>

### -field dwYBitMask

<dd>
<p>Specifies the mask for Y bits. </p>
</dd>

### -field dwStencilBitDepth

<dd>
<p>Specifies the bit depth of the stencil buffer. This member specifies how many bits are reserved within each pixel of the z-buffer for stencil information.</p>
</dd>

### -field dwLuminanceBitMask

<dd>
<p>Specifies the mask for luminance bits.</p>
</dd>

### -field dwBumpDuBitMask

<dd>
<p>Specifies the mask for bump map U delta bits.</p>
</dd>

### -field dwOperations

<dd>
<p><b>DirectX 8.0 and later versions only.</b> Specifies the intended operations that can be performed on surfaces with this pixel format, for example, whether such surfaces can be used as textures, bump environment maps, cube maps, volume textures, or render targets. The operations that can be reported are as follows:</p>
<table>
<tr>
<th>Operation</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_TEXTURE</p>
</td>
<td>
<p>When this flag is specified in a pixel format, it indicates that surfaces of this format can be used as MIP mapped textures.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_VOLUMETEXTURE</p>
</td>
<td>
<p>When this flag is specified in a pixel format, it indicates that surfaces of this format can be used as volume textures. Please note, that this flag is independent of D3DFORMAT_OP_TEXTURE. Thus, it is possible to specify a pixel format that can only be used for volume textures and not for conventional, MIP mapped textures.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_CUBETEXTURE</p>
</td>
<td>
<p>When this flag is specified in a pixel format, it indicates that surfaces of this format can be used as cubic environment map textures. Please note, that this flag is independent of D3DFORMAT_OP_TEXTURE. Thus, it is possible to specify a pixel format that can only be used for cubic environment map textures and not for conventional, MIP mapped textures.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_OFFSCREEN_RENDERTARGET</p>
</td>
<td>
<p>When this flag is specified in a pixel format, it indicates that surfaces of this format can be used as an offscreen render target regardless of the pixel format of the display mode (providing the pixel format of the current display mode was reported with the D3DFORMAT_OP_DISPLAYMODE and D3DFORMAT_OP_3DACCELERATION). If the pixel format of the current display mode did not have these flags set it indicates no 3D acceleration is available in this mode even if the render target is offscreen. This flag can be combined with D3DFORMAT_OP_TEXTURE to indicate that the device can render to textures of the specified pixel format.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_SAME_FORMAT_RENDERTARGET</p>
</td>
<td>
<p>When this flag is specified in a pixel format, it indicates that surfaces of this format can be used as render targets but only when the pixel format of the surface matches the pixel format of the current display mode. This flag does not only apply to offscreen render target but can be specified on the pixel formats of display modes to indicate rendering target capability. This flag can be combined with D3DFORMAT_OP_TEXTURE to indicate that the device can render to textures of the specified pixel format.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_ZSTENCIL</p>
</td>
<td>
<p>When this flag is specified in a pixel format, it indicates that surfaces of this format can be used as Z/Stencil buffers but only if the depth of the Z/Stencil surface matches the color depth of the rendering target to which the depth buffer is attached. When deciding on a match between Z/Stencil and color buffer depth, the pixel stride is used.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_ZSTENCIL_WITH_ARBITRARY_COLOR_DEPTH</p>
</td>
<td>
<p>When this flag is specified in a pixel format, it indicates that surfaces of this format can be used as Z/Stencil buffers regardless of the color depth of the render target to which the surface is attached. When specifying this flag you also should specify D3DFORMAT_OP_ZSTENCIL.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_SAME_FORMAT_UP_TO_ALPHA_RENDERTARGET</p>
</td>
<td>
<p>When this flag is specified in a pixel format, it indicates that surfaces of this format can be used as a render target if the current display mode is the same depth, if the alpha channel is ignored. For example, if the device can render to A8R8G8B8 when the display mode is X8R8G8B8, then the format operation list entry for A8R8G8B8 should have this flag set.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_DISPLAYMODE</p>
</td>
<td>
<p>When this flag is specified, it indicates that there is a display mode with this pixel format that has DirectDraw support (including Flip). This flag should not be set on alpha formats.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_3DACCELERATION</p>
</td>
<td>
<p>When this flag is specified, the graphics accelerator can support some level of Direct3D acceleration when in a display mode with this pixel format and also implies that the driver can create a context in this mode (for some render target format). This flag can only be used when reporting display mode formats (by specifying the D3DFORMAT_OP_DISPLAYMODE). It is not required and indeed should not be set when reporting offscreen render targets formats.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_PIXELSIZE</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that the driver filled in the bits per pixel for the format in the dwPrivateFormatBitCount member. 


### -field If the driver requires that managed surfaces and textures use a private format (a format that is understood by the driver but not natively by the Direct3D runtime), then the driver must specify this flag, along with the pixel size in dwPrivateFormatBitCount.

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_CONVERT_TO_ARGB</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that source surfaces of this format can be converted to any target surface with an RGB pixel format that has the D3DFORMAT_MEMBEROFGROUP_ARGB flag specified in dwOperations.

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_OFFSCREENPLAIN</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that the driver can stretch to and from and color fill surfaces of this format.

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_SRGBREAD</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that surfaces of this format can be read from as SRGB textures (that is, the sampler linearizes the looked up data).

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_BUMPMAP</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that surfaces of this format can be used as bump environment map textures.


### -field Note that this flag is independent of D3DFORMAT_OP_TEXTURE. Therefore, you can specify a pixel format that can only be used for bump environment map textures and not for conventional MIP mapped textures.

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_DMAP</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that surfaces of this format can be sampled by the displacement map sampler.

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_NOFILTER</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that surfaces of this format cannot be used with texture filtering.

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_MEMBEROFGROUP_ARGB</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that target surfaces of this format can be converted from any source surface with a pixel format that has the D3DFORMAT_OP_CONVERT_TO_ARGB flag specified in DirectX 9.0 and later versions only..


### -field The driver can only specify this flag for ARGB surfaces with at least 5 bits color information per channel. That is, the D3DFMT_A1R5G5B5 format is valid. However, the D3DFMT_A4R4G4B4 format is invalid. If the driver specifies this flag with an invalid format, the runtime prevents the Direct3D HAL from loading. Note that although this flag indicates ARGB formats, the runtime also allows the driver to specify surfaces with XRGB formats (for example, D3DFMT_X1R5G5B5).

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_SRGBWRITE</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that surfaces of this format can be written to as SRGB targets (that is, the pixel pipe delinearizes data on output to this format).

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_NOALPHABLEND</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that surfaces of this format cannot be used with alpha blending.

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_AUTOGENMIPMAP</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that the sublevels of MIP-map textures with this format can be automatically generated. To receive D3DDP2OP_GENERATEMIPSUBLEVELS operation requests, this flag must be exposed. 

</dl>
</p>
</td>
</tr>
<tr>
<td>
<p>D3DFORMAT_OP_VERTEXTEXTURE</p>
</td>
<td>
<p>
<dl>

### -field DirectX 9.0 and later versions only.


### -field When this flag is specified in a pixel format, it indicates that surfaces of this format can be used by a vertex texture sampler. That is, only surfaces of this format can be used as vertex textures. 

</dl>
</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field dwGBitMask

<dd>
<p>Specifies the mask for green bits. </p>
</dd>

### -field dwUBitMask

<dd>
<p>Specifies the mask for U bits. </p>
</dd>

### -field dwZBitMask

<dd>
<p>Specifies the mask for Z bits.</p>
</dd>

### -field dwBumpDvBitMask

<dd>
<p>Specifies the mask for bump map V delta bits.</p>
</dd>

### -field MultiSampleCaps

<dd>
<p><b>DirectX 8.0 and later versions only.</b> Structure that contains the following two members. It specifies 16-bitmasks for the number of samples per pixel for both flip (fullscreen) and blt (windowed) multisampling. It is used when specifying surfaces that can be used when performing multisample rendering (see the Remarks section). Each bit in these 16-bitmasks indicates support of multisampling with a specific number of samples. For example, bit 0 indicates the support of multisampling with only a single sample, bit 1 indicates the support of multisampling with two samples, bit 2 indicates the support of multisampling with three samples, and so on. The driver can indicate more than one supported level by combining the bits using a bitwise OR (see Remarks).</p>
<dl>

### -field wFlipMSTypes

<dd>
<p><b>DirectX 8.0 and later versions only.</b> Specifies a 16-bitmask for fullscreen multisampling.</p>
</dd>

### -field wBltMSTypes

<dd>
<p><b>DirectX 8.0 and later versions only.</b> Specifies a 16-bitmask for windowed multisampling.</p>
</dd>
</dl>
</dd>

### -field dwBBitMask

<dd>
<p>Specifies the mask for blue bits. </p>
</dd>

### -field dwVBitMask

<dd>
<p>Specifies the mask for V bits. </p>
</dd>

### -field dwStencilBitMask

<dd>
<p>Specifies the mask for stencil bits within each z-buffer pixel.</p>
</dd>

### -field dwBumpLuminanceBitMask

<dd>
<p>Specifies the mask for luminance in a bump map.</p>
</dd>

### -field dwRGBAlphaBitMask, dwYUVAlphaBitMask

<dd>
<p>Specify the masks for alpha channel. </p>
</dd>

### -field dwLuminanceAlphaBitMask

<dd>
<p>Specifies the mask for luminance in the alpha channel.</p>
</dd>

### -field dwRGBZBitMask, dwYUVZBitMask

<dd>
<p>Specifies the masks for the z channel. </p>
</dd>
</dl>

## -remarks
<p>The DirectX 8.0 and later runtime imposes the following rules on the operation (op) list:</p>

<p>Only one Endian-ness (big or little) for any DS format is allowed, for example D15S1 or S1D15, not both independent of other bits.</p>

<p>A list should only include D3DFORMAT_OP_DISPLAYMODE for exactly one 16bpp format (for example it should not enumerate 5:5:5 and 5:6:5).</p>

<p>A list should not contain any alpha formats with D3DFORMAT_OP_DISPLAYMODE or D3DFORMAT_OP_3DACCELLERATION set.</p>

<p>The D3DFORMAT_OP_3DACCELLERATION flag can only be set when the D3DFORMAT_OP_DISPLAYMODE flag is also set.</p>

<p>If the driver supports a lockable D16, it should report D3DFMT_D16_LOCKABLE in the op list; otherwise, it should report D3DFMT_D16.</p>

<p>Drivers supporting multisampling must fill in the <b>MultiSampleCaps</b> in the Depth/Stencil formats for which multisampling can be supported. This allows the runtime to detect if a driver supports multisampling for combinations of render target and Z buffer formats. For additional information about the restrictions related to stretch blt multisampling, see the description of D3DPRASTERCAPS_STRETCHBLTMULTISAMPLE cap in the rastercaps contained in the D3DCAPS8 structure in the SDK documentation.</p>

<p>The enumerated type D3DMULTISAMPLE_TYPE defined in <i>d3d8types.h</i> is used when setting the bits in <b>wFlipMSTypes</b> and <b>wBltMSTypes</b>. To specify support for a specific number of samples per pixel, simply logically shift 1 by the appropriate value from the D3DMULTISAMPLE_TYPE enumerated type less 1 and OR this into the appropriate field (<b>wFlipMSTypes</b> and <b>wBltMSTypes</b>).</p>

<p>For example, if the driver supports both two and four samples per pixel when flipping (fullscreen mode) and four samples per pixel when blitting (windowed mode) on X8R8G8B8 surface the following entry would be reported in the surface format list.</p>

<p>It is not necessary to specify 1 &lt;&lt; (D3DMULTISAMPLE_NONE - 1) when reporting formats. It is assumed that any format reported can also be used without multisampling. If the hardware supports multisample rendering with a z-buffer the z-buffer formats reported should also include the supported samples-per-pixels.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ddraw.h)</dt>
</dl>
</td>
</tr>
</table>