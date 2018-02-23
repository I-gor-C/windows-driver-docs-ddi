---
UID: NS:ksmedia._DDPIXELFORMAT
title: "_DDPIXELFORMAT"
author: windows-driver-content
description: The DDPIXELFORMAT structure describes the pixel format of a DirectDrawSurface object.
old-location: display\ddpixelformat.htm
old-project: display
ms.assetid: bbc26c03-c154-4b1e-883e-2942b59ded02
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: display.ddpixelformat, ddstrcts_861a4798-418e-492a-b4cb-c4f1ce794a71.xml, _DDPIXELFORMAT, ksmedia/LPDDPIXELFORMAT, ksmedia/DDPIXELFORMAT, DDPIXELFORMAT, LPDDPIXELFORMAT, *LPDDPIXELFORMAT, DDPIXELFORMAT structure [Display Devices], LPDDPIXELFORMAT structure pointer [Display Devices]
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ksmedia.h
apiname:
-	DDPIXELFORMAT
product: Windows
targetos: Windows
req.typenames: "*LPDDPIXELFORMAT, DDPIXELFORMAT"
---

# _DDPIXELFORMAT structure
The DDPIXELFORMAT structure describes the pixel format of a DirectDrawSurface object.

## Syntax
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

## Members


`dwFlags`

Indicates a set of flags that specify optional control flags. This member is a bitwise OR of any of the following values:

<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
DDPF_ALPHA

</td>
<td>
The pixel format describes an alpha-only surface.

</td>
</tr>
<tr>
<td>
DDPF_ALPHAPIXELS

</td>
<td>
The surface has alpha channel information in the pixel format.

</td>
</tr>
<tr>
<td>
DDPF_ALPHAPREMULT

</td>
<td>
The color components in the pixel are premultiplied by the alpha value in the pixel. If this flag is set, the DDPF_ALPHAPIXELS flag must also be set. If this flag is not set but the DDPF_ALPHAPIXELS flag is set, the color components in the pixel format are not premultiplied by alpha. In this case, the color components must be multiplied by the alpha value at the time that an alpha-blending operation is performed.

</td>
</tr>
<tr>
<td>
DDPF_BUMPDUDV

</td>
<td>
Bump map dUdV data in the pixel format is valid.

</td>
</tr>
<tr>
<td>
DDPF_BUMPHEIGHT

</td>
<td>
Bump map height data in the pixel format is valid.

</td>
</tr>
<tr>
<td>
DDPF_COMPRESSED

</td>
<td>
The surface accepts pixel data in the specified format and compresses it during the write operation.

</td>
</tr>
<tr>
<td>
DDPF_D3DFORMAT

</td>
<td>
Indicates a DirectX 8.0 and later format capability entry in the texture format list. This flag is not exposed to applications.

</td>
</tr>
<tr>
<td>
DDPF_FOURCC

</td>
<td>
The <a href="https://msdn.microsoft.com/f697e0db-1db0-4a81-94d8-0ca079885480">FOURCC</a> code is valid.

</td>
</tr>
<tr>
<td>
DDPF_LUMINANCE

</td>
<td>
Luminance data in the pixel format is valid. Use this flag for luminance-only or luminance-plus-alpha surfaces; the bit depth is then specified in the <b>dwLuminanceBitCount</b> member.

</td>
</tr>
<tr>
<td>
DDPF_LUMINANCEPIXELS

</td>
<td>
Luminance data in the pixel format is valid. Use this flag when hanging luminance off, for example, bumpmap surfaces. The bitmask for the luminance portion of the pixel is then specified in the <b>dwBumpLuminanceBitMask</b> member.

</td>
</tr>
<tr>
<td>
DDPF_NOVEL_TEXTURE_FORMAT

</td>
<td>
Indicates a new surface format that the runtime might not expose to all applications.

</td>
</tr>
<tr>
<td>
DDPF_PALETTEINDEXED1

</td>
<td>
The surface is 1-bit color indexed.

</td>
</tr>
<tr>
<td>
DDPF_PALETTEINDEXED2

</td>
<td>
The surface is 2-bit color indexed.

</td>
</tr>
<tr>
<td>
DDPF_PALETTEINDEXED4

</td>
<td>
The surface is 4-bit color indexed.

</td>
</tr>
<tr>
<td>
DDPF_PALETTEINDEXED8

</td>
<td>
The surface is 8-bit color indexed.

</td>
</tr>
<tr>
<td>
DDPF_PALETTEINDEXEDTO8

</td>
<td>
The surface is 1-, 2-, or 4-bit color indexed to an 8-bit palette.

</td>
</tr>
<tr>
<td>
DDPF_RGB

</td>
<td>
The RGB data in the pixel format structure is valid.

</td>
</tr>
<tr>
<td>
DDPF_RGBTOYUV

</td>
<td>
The surface accepts RGB data and translates it during the write operation to YUV data. The format of the data to be written is contained in the pixel format structure. The DDPF_RGB flag is set.

</td>
</tr>
<tr>
<td>
DDPF_STENCILBUFFER

</td>
<td>
The surface encodes stencil and depth information in each pixel of the z-buffer.

</td>
</tr>
<tr>
<td>
DDPF_YUV

</td>
<td>
The YUV data in the pixel format structure is valid.

</td>
</tr>
<tr>
<td>
DDPF_ZBUFFER

</td>
<td>
The pixel format describes a z-buffer-only surface.

</td>
</tr>
<tr>
<td>
DDPF_ZPIXELS

</td>
<td>
The surface is in RGBZ format.

</td>
</tr>
</table>

`dwFourCC`

Specifies a surface format code including any of the codes in the D3DFORMAT enumerated type. Some <a href="https://msdn.microsoft.com/f697e0db-1db0-4a81-94d8-0ca079885480">FOURCC</a> codes are part of D3DFORMAT. For more information about D3DFORMAT, see the SDK documentation. Hardware vendors can also define and supply format codes that are specific to their hardware.

`dwSize`

Specifies the size in bytes of the DDPIXELFORMAT structure. The driver must initialize this member before the structure is used.

<b>DirectX 9.0 and later versions only.</b> Specifies, on input, the version of the Microsoft DirectX runtime being used by the application. This member is set to DD_RUNTIME_VERSION, which is 0x00000900 for DirectX 9.0, in the <b>format</b> member of the <a href="..\d3dhal\ns-d3dhal-_dd_getformatdata.md">DD_GETFORMATDATA</a> structure for a D3DGDI2_TYPE_GETFORMAT query.

## Remarks
The DirectX 8.0 and later runtime imposes the following rules on the operation (op) list:

<ul>
<li>
Only one Endian-ness (big or little) for any DS format is allowed, for example D15S1 or S1D15, not both independent of other bits.

</li>
<li>
A list should only include D3DFORMAT_OP_DISPLAYMODE for exactly one 16bpp format (for example it should not enumerate 5:5:5 and 5:6:5).

</li>
<li>
A list should not contain any alpha formats with D3DFORMAT_OP_DISPLAYMODE or D3DFORMAT_OP_3DACCELLERATION set.

</li>
<li>
The D3DFORMAT_OP_3DACCELLERATION flag can only be set when the D3DFORMAT_OP_DISPLAYMODE flag is also set.

</li>
</ul>
If the driver supports a lockable D16, it should report D3DFMT_D16_LOCKABLE in the op list; otherwise, it should report D3DFMT_D16.

Drivers supporting multisampling must fill in the <b>MultiSampleCaps</b> in the Depth/Stencil formats for which multisampling can be supported. This allows the runtime to detect if a driver supports multisampling for combinations of render target and Z buffer formats. For additional information about the restrictions related to stretch blt multisampling, see the description of D3DPRASTERCAPS_STRETCHBLTMULTISAMPLE cap in the rastercaps contained in the D3DCAPS8 structure in the SDK documentation.

The enumerated type D3DMULTISAMPLE_TYPE defined in <i>d3d8types.h</i> is used when setting the bits in <b>wFlipMSTypes</b> and <b>wBltMSTypes</b>. To specify support for a specific number of samples per pixel, simply logically shift 1 by the appropriate value from the D3DMULTISAMPLE_TYPE enumerated type less 1 and OR this into the appropriate field (<b>wFlipMSTypes</b> and <b>wBltMSTypes</b>).

For example, if the driver supports both two and four samples per pixel when flipping (fullscreen mode) and four samples per pixel when blitting (windowed mode) on X8R8G8B8 surface the following entry would be reported in the surface format list.

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>DDPIXELFORMAT ddpf;
ZeroMemory(&amp;ddpf, sizeof(ddpf));
ddpf.dwSize       = sizeof(DDPIXELFORMAT);
ddpf.dwFlags      = DDPF_D3DFORMAT;
ddpf.dwFourCC     = D3DFMT_X8R8G8B8;
ddpf.dwOperations = D3DFORMAT_OP_DISPLAYMODE |
                    D3DFORMAT_OP_3DACCELERATION;
ddpf.MultiSampleCaps.wFlipMSTypes = (1 &lt;&lt; (D3DMULTISAMPLE_4_SAMPLES âˆ’ 1))
                                  | (1 &lt;&lt; (D3DMULTISAMPLE_2_SAMPLES âˆ’ 1));
ddpf.MultiSampleCaps.wBltMSTypes = (1 &lt;&lt; (D3DMULTISAMPLE_4_SAMPLES âˆ’ 1));</pre>
</td>
</tr>
</table></span></div>
It is not necessary to specify 1 &lt;&lt; (D3DMULTISAMPLE_NONE - 1) when reporting formats. It is assumed that any format reported can also be used without multisampling. If the hardware supports multisample rendering with a z-buffer the z-buffer formats reported should also include the supported samples-per-pixels.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ddraw.h) |