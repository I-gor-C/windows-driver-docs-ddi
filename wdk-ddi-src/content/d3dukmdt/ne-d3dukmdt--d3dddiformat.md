---
UID: NE.d3dukmdt._D3DDDIFORMAT
title: D3DDDIFORMAT
author: windows-driver-content
description: The D3DDDIFORMAT enumeration type contains values that identify surface formats.
old-location: display\d3dddiformat.htm
old-project: display
ms.assetid: 1ab8f431-867a-4ae2-a1d1-2eeceb6a6966
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_PRESENT_MULTIPLANE_OVERLAY, D3DKMT_PRESENT_MULTIPLANE_OVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIFORMAT
req.alt-loc: d3dukmdt.h
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

# D3DDDIFORMAT enumeration



## -description
<p>The D3DDDIFORMAT enumeration type contains values that identify surface formats.</p>


## -syntax

````
typedef enum _D3DDDIFORMAT { 
  D3DDDIFMT_UNKNOWN                  = 0,
  D3DDDIFMT_R8G8B8                   = 20,
  D3DDDIFMT_A8R8G8B8                 = 21,
  D3DDDIFMT_X8R8G8B8                 = 22,
  D3DDDIFMT_R5G6B5                   = 23,
  D3DDDIFMT_X1R5G5B5                 = 24,
  D3DDDIFMT_A1R5G5B5                 = 25,
  D3DDDIFMT_A4R4G4B4                 = 26,
  D3DDDIFMT_R3G3B2                   = 27,
  D3DDDIFMT_A8                       = 28,
  D3DDDIFMT_A8R3G3B2                 = 29,
  D3DDDIFMT_X4R4G4B4                 = 30,
  D3DDDIFMT_A2B10G10R10              = 31,
  D3DDDIFMT_A8B8G8R8                 = 32,
  D3DDDIFMT_X8B8G8R8                 = 33,
  D3DDDIFMT_G16R16                   = 34,
  D3DDDIFMT_A2R10G10B10              = 35,
  D3DDDIFMT_A16B16G16R16             = 36,
  D3DDDIFMT_A8P8                     = 40,
  D3DDDIFMT_P8                       = 41,
  D3DDDIFMT_L8                       = 50,
  D3DDDIFMT_A8L8                     = 51,
  D3DDDIFMT_A4L4                     = 52,
  D3DDDIFMT_V8U8                     = 60,
  D3DDDIFMT_L6V5U5                   = 61,
  D3DDDIFMT_X8L8V8U8                 = 62,
  D3DDDIFMT_Q8W8V8U8                 = 63,
  D3DDDIFMT_V16U16                   = 64,
  D3DDDIFMT_W11V11U10                = 65,
  D3DDDIFMT_A2W10V10U10              = 67,
  D3DDDIFMT_UYVY                     = MAKEFOURCC('U', 'Y', 'V', 'Y'),
  D3DDDIFMT_R8G8_B8G8                = MAKEFOURCC('R', 'G', 'B', 'G'),
  D3DDDIFMT_YUY2                     = MAKEFOURCC('Y', 'U', 'U', '2'),
  D3DDDIFMT_G8R8_G8B8                = MAKEFOURCC('G', 'R', 'G', 'B'),
  D3DDDIFMT_DXT1                     = MAKEFOURCC('D', 'X', 'T', '1'),
  D3DDDIFMT_DXT2                     = MAKEFOURCC('D', 'X', 'T', '2'),
  D3DDDIFMT_DXT3                     = MAKEFOURCC('D', 'X', 'T', '3'),
  D3DDDIFMT_DXT4                     = MAKEFOURCC('D', 'X', 'T', '4'),
  D3DDDIFMT_DXT5                     = MAKEFOURC('D', 'X', 'T', '5')C,
  D3DDDIFMT_D16_LOCKABLE             = 70,
  D3DDDIFMT_D32                      = 71,
  D3DDDIFMT_D15S1                    = 73,
  D3DDDIFMT_D24S8                    = 75,
  D3DDDIFMT_D24X8                    = 77,
  D3DDDIFMT_D24X4S4                  = 79,
  D3DDDIFMT_D16                      = 80,
  D3DDDIFMT_D32F_LOCKABLE            = 82,
  D3DDDIFMT_D24FS8                   = 83,
  D3DDDIFMT_D32_LOCKABLE             = 84,
  D3DDDIFMT_S8_LOCKABLE              = 85,
  D3DDDIFMT_S1D15                    = 72,
  D3DDDIFMT_S8D24                    = 74,
  D3DDDIFMT_X8D24                    = 76,
  D3DDDIFMT_X4S4D24                  = 78,
  D3DDDIFMT_L16                      = 81,
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3)
  D3DDDIFMT_G8R8                     = 91,
  D3DDDIFMT_R8                       = 92,
#endif 
  D3DDDIFMT_VERTEXDATA               = 100,
  D3DDDIFMT_INDEX16                  = 101,
  D3DDDIFMT_INDEX32                  = 102,
  D3DDDIFMT_Q16W16V16U16             = 110,
  D3DDDIFMT_MULTI2_ARGB8             = MAKEFOURCC('M', 'E', 'T', '1'),
  D3DDDIFMT_R16F                     = 111,
  D3DDDIFMT_G16R16F                  = 112,
  D3DDDIFMT_A16B16G16R16F            = 113,
  D3DDDIFMT_R32F                     = 114,
  D3DDDIFMT_G32R32F                  = 115,
  D3DDDIFMT_A32B32G32R32F            = 116,
  D3DDDIFMT_CxV8U8                   = 117,
  D3DDDIFMT_A1                       = 118,
  D3DDDIFMT_A2B10G10R10_XR_BIAS      = 119,
  D3DDDIFMT_DXVACOMPBUFFER_BASE      = 150,
  D3DDDIFMT_PICTUREPARAMSDATA        = D3DDDIFMT_DXVACOMPBUFFER_BASE+0,
  D3DDDIFMT_MACROBLOCKDATA           = D3DDDIFMT_DXVACOMPBUFFER_BASE+1,
  D3DDDIFMT_RESIDUALDIFFERENCEDATA   = D3DDDIFMT_DXVACOMPBUFFER_BASE+2,
  D3DDDIFMT_DEBLOCKINGDATA           = D3DDDIFMT_DXVACOMPBUFFER_BASE+3,
  D3DDDIFMT_INVERSEQUANTIZATIONDATA  = D3DDDIFMT_DXVACOMPBUFFER_BASE+4,
  D3DDDIFMT_SLICECONTROLDATA         = D3DDDIFMT_DXVACOMPBUFFER_BASE+5,
  D3DDDIFMT_BITSTREAMDATA            = D3DDDIFMT_DXVACOMPBUFFER_BASE+6,
  D3DDDIFMT_MOTIONVECTORBUFFER       = D3DDDIFMT_DXVACOMPBUFFER_BASE+7,
  D3DDDIFMT_FILMGRAINBUFFER          = D3DDDIFMT_DXVACOMPBUFFER_BASE+8,
  D3DDDIFMT_DXVA_RESERVED9           = D3DDDIFMT_DXVACOMPBUFFER_BASE+9,
  D3DDDIFMT_DXVA_RESERVED10          = D3DDDIFMT_DXVACOMPBUFFER_BASE+10,
  D3DDDIFMT_DXVA_RESERVED11          = D3DDDIFMT_DXVACOMPBUFFER_BASE+11,
  D3DDDIFMT_DXVA_RESERVED12          = D3DDDIFMT_DXVACOMPBUFFER_BASE+12,
  D3DDDIFMT_DXVA_RESERVED13          = D3DDDIFMT_DXVACOMPBUFFER_BASE+13,
  D3DDDIFMT_DXVA_RESERVED14          = D3DDDIFMT_DXVACOMPBUFFER_BASE+14,
  D3DDDIFMT_DXVA_RESERVED15          = D3DDDIFMT_DXVACOMPBUFFER_BASE+15,
  D3DDDIFMT_DXVA_RESERVED16          = D3DDDIFMT_DXVACOMPBUFFER_BASE+16,
  D3DDDIFMT_DXVA_RESERVED17          = D3DDDIFMT_DXVACOMPBUFFER_BASE+17,
  D3DDDIFMT_DXVA_RESERVED18          = D3DDDIFMT_DXVACOMPBUFFER_BASE+18,
  D3DDDIFMT_DXVA_RESERVED19          = D3DDDIFMT_DXVACOMPBUFFER_BASE+19,
  D3DDDIFMT_DXVA_RESERVED20          = D3DDDIFMT_DXVACOMPBUFFER_BASE+20,
  D3DDDIFMT_DXVA_RESERVED21          = D3DDDIFMT_DXVACOMPBUFFER_BASE+21,
  D3DDDIFMT_DXVA_RESERVED22          = D3DDDIFMT_DXVACOMPBUFFER_BASE+22,
  D3DDDIFMT_DXVA_RESERVED23          = D3DDDIFMT_DXVACOMPBUFFER_BASE+23,
  D3DDDIFMT_DXVA_RESERVED24          = D3DDDIFMT_DXVACOMPBUFFER_BASE+24,
  D3DDDIFMT_DXVA_RESERVED25          = D3DDDIFMT_DXVACOMPBUFFER_BASE+25,
  D3DDDIFMT_DXVA_RESERVED26          = D3DDDIFMT_DXVACOMPBUFFER_BASE+26,
  D3DDDIFMT_DXVA_RESERVED27          = D3DDDIFMT_DXVACOMPBUFFER_BASE+27,
  D3DDDIFMT_DXVA_RESERVED28          = D3DDDIFMT_DXVACOMPBUFFER_BASE+28,
  D3DDDIFMT_DXVA_RESERVED29          = D3DDDIFMT_DXVACOMPBUFFER_BASE+29,
  D3DDDIFMT_DXVA_RESERVED30          = D3DDDIFMT_DXVACOMPBUFFER_BASE+30,
  D3DDDIFMT_DXVA_RESERVED31          = D3DDDIFMT_DXVACOMPBUFFER_BASE+31,
  D3DDDIFMT_DXVACOMPBUFFER_MAX       = D3DDDIFMT_DXVA_RESERVED31,
  D3DDDIFMT_BINARYBUFFER             = 199,
  D3DDDIFMT_FORCE_UINT               = 0x7fffffff
} D3DDDIFORMAT;
````


## -enum-fields
<dl>

### -field <a id="D3DDDIFMT_UNKNOWN"></a><a id="d3dddifmt_unknown"></a><b>D3DDDIFMT_UNKNOWN</b>

<dd>
<p>An unknown format.</p>
</dd>

### -field <a id="D3DDDIFMT_R8G8B8"></a><a id="d3dddifmt_r8g8b8"></a><b>D3DDDIFMT_R8G8B8</b>

<dd>
<p>24-bit RGB unsigned pixel format with 8 bits for each channel.</p>
</dd>

### -field <a id="D3DDDIFMT_A8R8G8B8"></a><a id="d3dddifmt_a8r8g8b8"></a><b>D3DDDIFMT_A8R8G8B8</b>

<dd>
<p>32-bit ARGB unsigned pixel format with alpha that uses 8 bits for each channel.</p>
</dd>

### -field <a id="D3DDDIFMT_X8R8G8B8"></a><a id="d3dddifmt_x8r8g8b8"></a><b>D3DDDIFMT_X8R8G8B8</b>

<dd>
<p>32-bit RGB unsigned pixel format, where 8 bits are reserved for each color.</p>
</dd>

### -field <a id="D3DDDIFMT_R5G6B5"></a><a id="d3dddifmt_r5g6b5"></a><b>D3DDDIFMT_R5G6B5</b>

<dd>
<p>16-bit RGB unsigned pixel format with 5 bits for red, 6 bits for green, and 5 bits for blue.</p>
</dd>

### -field <a id="D3DDDIFMT_X1R5G5B5"></a><a id="d3dddifmt_x1r5g5b5"></a><b>D3DDDIFMT_X1R5G5B5</b>

<dd>
<p>16-bit unsigned pixel format where 5 bits are reserved for each color.</p>
</dd>

### -field <a id="D3DDDIFMT_A1R5G5B5"></a><a id="d3dddifmt_a1r5g5b5"></a><b>D3DDDIFMT_A1R5G5B5</b>

<dd>
<p>16-bit unsigned pixel format where 5 bits are reserved for each color and 1 bit is reserved for alpha.</p>
</dd>

### -field <a id="D3DDDIFMT_A4R4G4B4"></a><a id="d3dddifmt_a4r4g4b4"></a><b>D3DDDIFMT_A4R4G4B4</b>

<dd>
<p>16-bit ARGB unsigned pixel format with 4 bits for each channel.</p>
</dd>

### -field <a id="D3DDDIFMT_R3G3B2"></a><a id="d3dddifmt_r3g3b2"></a><b>D3DDDIFMT_R3G3B2</b>

<dd>
<p>8-bit RGB unsigned texture format that uses 3 bits for red, 3 bits for green, and 2 bits for blue.</p>
</dd>

### -field <a id="D3DDDIFMT_A8"></a><a id="d3dddifmt_a8"></a><b>D3DDDIFMT_A8</b>

<dd>
<p>8-bit alpha only.</p>
</dd>

### -field <a id="D3DDDIFMT_A8R3G3B2"></a><a id="d3dddifmt_a8r3g3b2"></a><b>D3DDDIFMT_A8R3G3B2</b>

<dd>
<p>16-bit ARGB unsigned texture format that uses 8 bits for alpha, 3 bits each for red and green, and 2 bits for blue.</p>
</dd>

### -field <a id="D3DDDIFMT_X4R4G4B4"></a><a id="d3dddifmt_x4r4g4b4"></a><b>D3DDDIFMT_X4R4G4B4</b>

<dd>
<p>16-bit RGB unsigned pixel format that uses 4 bits for each color.</p>
</dd>

### -field <a id="D3DDDIFMT_A2B10G10R10"></a><a id="d3dddifmt_a2b10g10r10"></a><b>D3DDDIFMT_A2B10G10R10</b>

<dd>
<p>32-bit unsigned pixel format that uses 10 bits for each color and 2 bits for alpha.</p>
</dd>

### -field <a id="D3DDDIFMT_A8B8G8R8"></a><a id="d3dddifmt_a8b8g8r8"></a><b>D3DDDIFMT_A8B8G8R8</b>

<dd>
<p>32-bit ARGB unsigned pixel format with alpha that uses 8 bits for each channel.</p>
</dd>

### -field <a id="D3DDDIFMT_X8B8G8R8"></a><a id="d3dddifmt_x8b8g8r8"></a><b>D3DDDIFMT_X8B8G8R8</b>

<dd>
<p>32-bit RGB unsigned pixel format, where 8 bits are reserved for each color.</p>
</dd>

### -field <a id="D3DDDIFMT_G16R16"></a><a id="d3dddifmt_g16r16"></a><b>D3DDDIFMT_G16R16</b>

<dd>
<p>32-bit unsigned pixel format that uses 16 bits each for green and red.</p>
</dd>

### -field <a id="D3DDDIFMT_A2R10G10B10"></a><a id="d3dddifmt_a2r10g10b10"></a><b>D3DDDIFMT_A2R10G10B10</b>

<dd>
<p>32-bit unsigned pixel format that uses 10 bits for each color and 2 bits for alpha.</p>
</dd>

### -field <a id="D3DDDIFMT_A16B16G16R16"></a><a id="d3dddifmt_a16b16g16r16"></a><b>D3DDDIFMT_A16B16G16R16</b>

<dd>
<p>64-bit unsigned pixel format that uses 16 bits for each component.</p>
</dd>

### -field <a id="D3DDDIFMT_A8P8"></a><a id="d3dddifmt_a8p8"></a><b>D3DDDIFMT_A8P8</b>

<dd>
<p>8-bit color indexed with 8 bits of alpha.</p>
</dd>

### -field <a id="D3DDDIFMT_P8"></a><a id="d3dddifmt_p8"></a><b>D3DDDIFMT_P8</b>

<dd>
<p>8-bit color indexed.</p>
</dd>

### -field <a id="D3DDDIFMT_L8"></a><a id="d3dddifmt_l8"></a><b>D3DDDIFMT_L8</b>

<dd>
<p>8-bit luminance only.</p>
</dd>

### -field <a id="D3DDDIFMT_A8L8"></a><a id="d3dddifmt_a8l8"></a><b>D3DDDIFMT_A8L8</b>

<dd>
<p>16-bit format that uses 8 bits each for alpha and luminance.</p>
</dd>

### -field <a id="D3DDDIFMT_A4L4"></a><a id="d3dddifmt_a4l4"></a><b>D3DDDIFMT_A4L4</b>

<dd>
<p>8-bit format that uses 4 bits each for alpha and luminance.</p>
</dd>

### -field <a id="D3DDDIFMT_V8U8"></a><a id="d3dddifmt_v8u8"></a><b>D3DDDIFMT_V8U8</b>

<dd>
<p>16-bit signed bump-map format that uses 8 bits each for u and v data.</p>
</dd>

### -field <a id="D3DDDIFMT_L6V5U5"></a><a id="d3dddifmt_l6v5u5"></a><b>D3DDDIFMT_L6V5U5</b>

<dd>
<p>16-bit mixed signed and unsigned bump-map format with luminance that uses 6 bits for luminance and 5 bits each for v and u data.</p>
</dd>

### -field <a id="D3DDDIFMT_X8L8V8U8"></a><a id="d3dddifmt_x8l8v8u8"></a><b>D3DDDIFMT_X8L8V8U8</b>

<dd>
<p>32-bit mixed signed and unsigned bump-map format with luminance that uses 8 bits for each channel.</p>
</dd>

### -field <a id="D3DDDIFMT_Q8W8V8U8"></a><a id="d3dddifmt_q8w8v8u8"></a><b>D3DDDIFMT_Q8W8V8U8</b>

<dd>
<p>32-bit signed bump-map format that uses 8 bits for each channel.</p>
</dd>

### -field <a id="D3DDDIFMT_V16U16"></a><a id="d3dddifmt_v16u16"></a><b>D3DDDIFMT_V16U16</b>

<dd>
<p>32-bit signed bump-map format using 16 bits each for u and v data.</p>
</dd>

### -field <a id="D3DDDIFMT_W11V11U10"></a><a id="d3dddifmt_w11v11u10"></a><b>D3DDDIFMT_W11V11U10</b>

<dd>
<p>32-bit signed bump-map format that uses 11 bits each for w and v and 10 bits for u.</p>
</dd>

### -field <a id="D3DDDIFMT_A2W10V10U10"></a><a id="d3dddifmt_a2w10v10u10"></a><b>D3DDDIFMT_A2W10V10U10</b>

<dd>
<p>32-bit mixed signed and unsigned bump-map format that uses 2 bits for alpha and 10 bits each for w, v, and u.</p>
</dd>

### -field <a id="D3DDDIFMT_UYVY"></a><a id="d3dddifmt_uyvy"></a><b>D3DDDIFMT_UYVY</b>

<dd>
<p>UYVY FOURCC format (MAKEFOURCC('U', 'Y', 'V', 'Y')).</p>
</dd>

### -field <a id="D3DDDIFMT_R8G8_B8G8"></a><a id="d3dddifmt_r8g8_b8g8"></a><b>D3DDDIFMT_R8G8_B8G8</b>

<dd>
<p>RGBG FOURCC format (MAKEFOURCC('R', 'G', 'B', 'G')).</p>
<p>A 16-bit packed RGB format that is analogous to UYVY (U0Y0, V0Y1, U2Y2, and so on). RGBG FOURCC format requires a pixel pair to represent the color value. The first pixel in the pair contains 8 bits of green (in the low 8 bits) and 8 bits of red (in the high 8 bits). The second pixel contains 8 bits of green (in the low 8 bits) and 8 bits of blue (in the high 8 bits). The two pixels share the red and blue components, and each has a unique green component (R0G0, B0G1, R2G2, and so on). </p>
<p>The texture sampler does not normalize the colors when looking up into a pixel shader; they remain in the range from 0.0f through 255.0f. This situation occurs for all programmable pixel shader models. For the fixed function pixel shader, the hardware should normalize to the range from 0.f through 1.f and treat it as the YUY2 texture. Hardware that exposes this format must have the <b>PixelShader1xMaxValue</b> member of the D3DCAPS9 structure set to a value that is capable of handling that range (0.f through 1.f).</p>
</dd>

### -field <a id="D3DDDIFMT_YUY2"></a><a id="d3dddifmt_yuy2"></a><b>D3DDDIFMT_YUY2</b>

<dd>
<p>YUY2 FOURCC format (MAKEFOURCC('Y', 'U', 'Y', '2')).</p>
</dd>

### -field <a id="D3DDDIFMT_G8R8_G8B8"></a><a id="d3dddifmt_g8r8_g8b8"></a><b>D3DDDIFMT_G8R8_G8B8</b>

<dd>
<p>GRGB FOURCC format (MAKEFOURCC('G', 'R', 'G', 'B')).</p>
<p>A 16-bit packed RGB format that is analogous to YUY2 (Y0U0, Y1V0, Y2U2, and so on). GRGB FOURCC format requires a pixel pair to represent the color value. The first pixel in the pair contains 8 bits of green (in the high 8 bits) and 8 bits of red (in the low 8 bits). The second pixel contains 8 bits of green (in the high 8 bits) and 8 bits of blue (in the low 8 bits). The two pixels share the red and blue components, and each has a unique green component (G0R0, G1B0, G2R2, and so on). </p>
<p>The texture sampler does not normalize the colors when looking up into a pixel shader; they remain in the range from 0.0f through 255.0f. This situation occurs for all programmable pixel shader models. For the fixed function pixel shader, the hardware should normalize to the range from 0.f through 1.f and treat it as the YUY2 texture. Hardware that exposes this format must have the <b>PixelShader1xMaxValue</b> member of D3DCAPS9 set to a value that is capable of handling that range (0.f through 1.f).</p>
</dd>

### -field <a id="D3DDDIFMT_DXT1"></a><a id="d3dddifmt_dxt1"></a><b>D3DDDIFMT_DXT1</b>

<dd>
<p>DXT1 FOURCC compression texture format (MAKEFOURCC('D', 'X', 'T', '1')).</p>
</dd>

### -field <a id="D3DDDIFMT_DXT2"></a><a id="d3dddifmt_dxt2"></a><b>D3DDDIFMT_DXT2</b>

<dd>
<p>DXT2 FOURCC compression texture format (MAKEFOURCC('D', 'X', 'T', '2')).</p>
</dd>

### -field <a id="D3DDDIFMT_DXT3"></a><a id="d3dddifmt_dxt3"></a><b>D3DDDIFMT_DXT3</b>

<dd>
<p>DXT3 FOURCC compression texture format (MAKEFOURCC('D', 'X', 'T', '3')).</p>
</dd>

### -field <a id="D3DDDIFMT_DXT4"></a><a id="d3dddifmt_dxt4"></a><b>D3DDDIFMT_DXT4</b>

<dd>
<p>DXT4 FOURCC compression texture format (MAKEFOURCC('D', 'X', 'T', '4')).</p>
</dd>

### -field <a id="D3DDDIFMT_DXT5"></a><a id="d3dddifmt_dxt5"></a><b>D3DDDIFMT_DXT5</b>

<dd>
<p>DXT5 FOURCC compression texture format (MAKEFOURCC('D', 'X', 'T', '5')).</p>
</dd>

### -field <a id="D3DDDIFMT_D16_LOCKABLE"></a><a id="d3dddifmt_d16_lockable"></a><b>D3DDDIFMT_D16_LOCKABLE</b>

<dd>
<p>16-bit z-buffer bit depth.</p>
</dd>

### -field <a id="D3DDDIFMT_D32"></a><a id="d3dddifmt_d32"></a><b>D3DDDIFMT_D32</b>

<dd>
<p>32-bit z-buffer bit depth.</p>
</dd>

### -field <a id="D3DDDIFMT_D15S1"></a><a id="d3dddifmt_d15s1"></a><b>D3DDDIFMT_D15S1</b>

<dd>
<p>16-bit z-buffer bit depth where 15 bits are reserved for the depth channel and 1 bit is reserved for the stencil channel.</p>
</dd>

### -field <a id="D3DDDIFMT_D24S8"></a><a id="d3dddifmt_d24s8"></a><b>D3DDDIFMT_D24S8</b>

<dd>
<p>32-bit z-buffer bit depth that uses 24 bits for the depth channel and 8 bits for the stencil channel.</p>
</dd>

### -field <a id="D3DDDIFMT_D24X8"></a><a id="d3dddifmt_d24x8"></a><b>D3DDDIFMT_D24X8</b>

<dd>
<p>32-bit z-buffer bit depth that uses 24 bits for the depth channel.</p>
</dd>

### -field <a id="D3DDDIFMT_D24X4S4"></a><a id="d3dddifmt_d24x4s4"></a><b>D3DDDIFMT_D24X4S4</b>

<dd>
<p>32-bit z-buffer bit depth that uses 24 bits for the depth channel and 4 bits for the stencil channel.</p>
</dd>

### -field <a id="D3DDDIFMT_D16"></a><a id="d3dddifmt_d16"></a><b>D3DDDIFMT_D16</b>

<dd>
<p>16-bit z-buffer bit depth.</p>
</dd>

### -field <a id="D3DDDIFMT_D32F_LOCKABLE"></a><a id="d3dddifmt_d32f_lockable"></a><b>D3DDDIFMT_D32F_LOCKABLE</b>

<dd>
<p>A lockable buffer format where the depth value is represented as a standard IEEE floating-point number.</p>
</dd>

### -field <a id="D3DDDIFMT_D24FS8"></a><a id="d3dddifmt_d24fs8"></a><b>D3DDDIFMT_D24FS8</b>

<dd>
<p>A non-lockable buffer format that contains 24 bits of depth (in a 24-bit floating point format: - 20e4) and 8 bits of stencil.</p>
</dd>

### -field <a id="D3DDDIFMT_D32_LOCKABLE"></a><a id="d3dddifmt_d32_lockable"></a><b>D3DDDIFMT_D32_LOCKABLE</b>

<dd>
<p>A lockable buffer format that uses 32 bits for the depth channel.</p>
</dd>

### -field <a id="D3DDDIFMT_S8_LOCKABLE"></a><a id="d3dddifmt_s8_lockable"></a><b>D3DDDIFMT_S8_LOCKABLE</b>

<dd>
<p>A lockable buffer format that uses 8 bits for the stencil channel.</p>
</dd>

### -field <a id="D3DDDIFMT_S1D15"></a><a id="d3dddifmt_s1d15"></a><b>D3DDDIFMT_S1D15</b>

<dd>
<p>16-bit z-buffer bit depth where 15 bits are reserved for the depth channel and 1 bit is reserved for the stencil channel.</p>
</dd>

### -field <a id="D3DDDIFMT_S8D24"></a><a id="d3dddifmt_s8d24"></a><b>D3DDDIFMT_S8D24</b>

<dd>
<p>32-bit z-buffer bit depth that uses 24 bits for the depth channel and 8 bits for the stencil channel.</p>
</dd>

### -field <a id="D3DDDIFMT_X8D24"></a><a id="d3dddifmt_x8d24"></a><b>D3DDDIFMT_X8D24</b>

<dd>
<p>32-bit z-buffer bit depth that uses 24 bits for the depth channel.</p>
</dd>

### -field <a id="D3DDDIFMT_X4S4D24"></a><a id="d3dddifmt_x4s4d24"></a><b>D3DDDIFMT_X4S4D24</b>

<dd>
<p>32-bit z-buffer bit depth that uses 24 bits for the depth channel and 4 bits for the stencil channel.</p>
</dd>

### -field <a id="D3DDDIFMT_L16"></a><a id="d3dddifmt_l16"></a><b>D3DDDIFMT_L16</b>

<dd>
<p>16-bit luminance only.</p>
</dd>

### -field <a id="D3DDDIFMT_G8R8"></a><a id="d3dddifmt_g8r8"></a><b>D3DDDIFMT_G8R8</b>

<dd>
<p>A two-component, 16-bit unsigned-normalized-integer format that supports 8 bits for the red channel and 8 bits for the green channel. Equivalent to <b>DXGI_FORMAT_R8G8_UNORM</b> from the <a href="direct3ddxgi.dxgi_format">DXGI_FORMAT</a> enumeration.</p>
</dd>

### -field <a id="D3DDDIFMT_R8"></a><a id="d3dddifmt_r8"></a><b>D3DDDIFMT_R8</b>

<dd>
<p>A single-component, 8-bit unsigned-normalized-integer format that supports 8 bits for the red channel. Equivalent to <b>DXGI_FORMAT_R8_UNORM</b> from the <a href="direct3ddxgi.dxgi_format">DXGI_FORMAT</a> enumeration.</p>
</dd>

### -field <a id="D3DDDIFMT_VERTEXDATA"></a><a id="d3dddifmt_vertexdata"></a><b>D3DDDIFMT_VERTEXDATA</b>

<dd>
<p>A vertex buffer surface.</p>
</dd>

### -field <a id="D3DDDIFMT_INDEX16"></a><a id="d3dddifmt_index16"></a><b>D3DDDIFMT_INDEX16</b>

<dd>
<p>16-bit index buffer bit depth.</p>
</dd>

### -field <a id="D3DDDIFMT_INDEX32"></a><a id="d3dddifmt_index32"></a><b>D3DDDIFMT_INDEX32</b>

<dd>
<p>32-bit index buffer bit depth.</p>
</dd>

### -field <a id="D3DDDIFMT_Q16W16V16U16"></a><a id="d3dddifmt_q16w16v16u16"></a><b>D3DDDIFMT_Q16W16V16U16</b>

<dd>
<p>64-bit signed bump-map format that uses 16 bits for each channel.</p>
</dd>

### -field <a id="D3DDDIFMT_MULTI2_ARGB8"></a><a id="d3dddifmt_multi2_argb8"></a><b>D3DDDIFMT_MULTI2_ARGB8</b>

<dd>
<p>MultiElement FOURCC noncompressed texture (MAKEFOURCC('M','E','T','1')).</p>
</dd>

### -field <a id="D3DDDIFMT_R16F"></a><a id="d3dddifmt_r16f"></a><b>D3DDDIFMT_R16F</b>

<dd>
<p>16-bit s10e5 floating-point surface format that uses 16 bits for the red channel.</p>
</dd>

### -field <a id="D3DDDIFMT_G16R16F"></a><a id="d3dddifmt_g16r16f"></a><b>D3DDDIFMT_G16R16F</b>

<dd>
<p>32-bit s10e5 floating-point surface format that uses 16 bits for the red channel and 16 bits for the green channel.</p>
</dd>

### -field <a id="D3DDDIFMT_A16B16G16R16F"></a><a id="d3dddifmt_a16b16g16r16f"></a><b>D3DDDIFMT_A16B16G16R16F</b>

<dd>
<p>64-bit s10e5 floating-point surface format that uses 16 bits for each channel (alpha, blue, green, and red).</p>
</dd>

### -field <a id="D3DDDIFMT_R32F"></a><a id="d3dddifmt_r32f"></a><b>D3DDDIFMT_R32F</b>

<dd>
<p>32-bit s23e8 floating-point surface format that uses 32 bits for the red channel.</p>
</dd>

### -field <a id="D3DDDIFMT_G32R32F"></a><a id="d3dddifmt_g32r32f"></a><b>D3DDDIFMT_G32R32F</b>

<dd>
<p>64-bit s23e8 floating-point surface format that uses 32 bits for the red channel and 32 bits for the green channel.</p>
</dd>

### -field <a id="D3DDDIFMT_A32B32G32R32F"></a><a id="d3dddifmt_a32b32g32r32f"></a><b>D3DDDIFMT_A32B32G32R32F</b>

<dd>
<p>128-bit s23e8 floating-point surface format that uses 32 bits for the each channel (alpha, blue, green, and red).</p>
</dd>

### -field <a id="D3DDDIFMT_CxV8U8"></a><a id="d3dddifmt_cxv8u8"></a><a id="D3DDDIFMT_CXV8U8"></a><b>D3DDDIFMT_CxV8U8</b>

<dd>
<p>16-bit signed normal compression format. The texture sampler computes the C channel from: C = sqrt(1 - U2 - V2).</p>
</dd>

### -field <a id="D3DDDIFMT_A1"></a><a id="d3dddifmt_a1"></a><b>D3DDDIFMT_A1</b>

<dd>
<p>A monochrome 1-bit per pixel format. </p>
</dd>

### -field <a id="D3DDDIFMT_A2B10G10R10_XR_BIAS"></a><a id="d3dddifmt_a2b10g10r10_xr_bias"></a><b>D3DDDIFMT_A2B10G10R10_XR_BIAS</b>

<dd>
<p>Supported in Windows 7 and later versions.</p>
<p>32-bit unsigned pixel format that uses 10 bits for each color and 2 bits for alpha along with 2.8 biased fixed point. </p>
</dd>

### -field <a id="D3DDDIFMT_DXVACOMPBUFFER_BASE"></a><a id="d3dddifmt_dxvacompbuffer_base"></a><b>D3DDDIFMT_DXVACOMPBUFFER_BASE</b>

<dd>
<p>A base compressed buffer format value. </p>
</dd>

### -field <a id="D3DDDIFMT_PICTUREPARAMSDATA"></a><a id="d3dddifmt_pictureparamsdata"></a><b>D3DDDIFMT_PICTUREPARAMSDATA</b>

<dd>
<p>Picture parameters decode compressed buffer format.</p>
</dd>

### -field <a id="D3DDDIFMT_MACROBLOCKDATA"></a><a id="d3dddifmt_macroblockdata"></a><b>D3DDDIFMT_MACROBLOCKDATA</b>

<dd>
<p>Macroblock control command decode compressed buffer format.</p>
</dd>

### -field <a id="D3DDDIFMT_RESIDUALDIFFERENCEDATA"></a><a id="d3dddifmt_residualdifferencedata"></a><b>D3DDDIFMT_RESIDUALDIFFERENCEDATA</b>

<dd>
<p>Residual block difference decode compressed buffer format.</p>
</dd>

### -field <a id="D3DDDIFMT_DEBLOCKINGDATA"></a><a id="d3dddifmt_deblockingdata"></a><b>D3DDDIFMT_DEBLOCKINGDATA</b>

<dd>
<p>Deblocking filter control command decode compressed buffer format.</p>
</dd>

### -field <a id="D3DDDIFMT_INVERSEQUANTIZATIONDATA"></a><a id="d3dddifmt_inversequantizationdata"></a><b>D3DDDIFMT_INVERSEQUANTIZATIONDATA</b>

<dd>
<p>Inverse-quantization matrix decode compressed buffer format.</p>
</dd>

### -field <a id="D3DDDIFMT_SLICECONTROLDATA"></a><a id="d3dddifmt_slicecontroldata"></a><b>D3DDDIFMT_SLICECONTROLDATA</b>

<dd>
<p>Slice-control decode compressed buffer format.</p>
</dd>

### -field <a id="D3DDDIFMT_BITSTREAMDATA"></a><a id="d3dddifmt_bitstreamdata"></a><b>D3DDDIFMT_BITSTREAMDATA</b>

<dd>
<p>Bitstream data decode compressed buffer format.</p>
</dd>

### -field <a id="D3DDDIFMT_MOTIONVECTORBUFFER"></a><a id="d3dddifmt_motionvectorbuffer"></a><b>D3DDDIFMT_MOTIONVECTORBUFFER</b>

<dd>
<p>Motion-vector decode compressed buffer format.</p>
</dd>

### -field <a id="D3DDDIFMT_FILMGRAINBUFFER"></a><a id="d3dddifmt_filmgrainbuffer"></a><b>D3DDDIFMT_FILMGRAINBUFFER</b>

<dd>
<p>Film-grain decode compressed buffer format.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED9"></a><a id="d3dddifmt_dxva_reserved9"></a><b>D3DDDIFMT_DXVA_RESERVED9</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED10"></a><a id="d3dddifmt_dxva_reserved10"></a><b>D3DDDIFMT_DXVA_RESERVED10</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED11"></a><a id="d3dddifmt_dxva_reserved11"></a><b>D3DDDIFMT_DXVA_RESERVED11</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED12"></a><a id="d3dddifmt_dxva_reserved12"></a><b>D3DDDIFMT_DXVA_RESERVED12</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED13"></a><a id="d3dddifmt_dxva_reserved13"></a><b>D3DDDIFMT_DXVA_RESERVED13</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED14"></a><a id="d3dddifmt_dxva_reserved14"></a><b>D3DDDIFMT_DXVA_RESERVED14</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED15"></a><a id="d3dddifmt_dxva_reserved15"></a><b>D3DDDIFMT_DXVA_RESERVED15</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED16"></a><a id="d3dddifmt_dxva_reserved16"></a><b>D3DDDIFMT_DXVA_RESERVED16</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED17"></a><a id="d3dddifmt_dxva_reserved17"></a><b>D3DDDIFMT_DXVA_RESERVED17</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED18"></a><a id="d3dddifmt_dxva_reserved18"></a><b>D3DDDIFMT_DXVA_RESERVED18</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED19"></a><a id="d3dddifmt_dxva_reserved19"></a><b>D3DDDIFMT_DXVA_RESERVED19</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED20"></a><a id="d3dddifmt_dxva_reserved20"></a><b>D3DDDIFMT_DXVA_RESERVED20</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED21"></a><a id="d3dddifmt_dxva_reserved21"></a><b>D3DDDIFMT_DXVA_RESERVED21</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED22"></a><a id="d3dddifmt_dxva_reserved22"></a><b>D3DDDIFMT_DXVA_RESERVED22</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED23"></a><a id="d3dddifmt_dxva_reserved23"></a><b>D3DDDIFMT_DXVA_RESERVED23</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED24"></a><a id="d3dddifmt_dxva_reserved24"></a><b>D3DDDIFMT_DXVA_RESERVED24</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED25"></a><a id="d3dddifmt_dxva_reserved25"></a><b>D3DDDIFMT_DXVA_RESERVED25</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED26"></a><a id="d3dddifmt_dxva_reserved26"></a><b>D3DDDIFMT_DXVA_RESERVED26</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED27"></a><a id="d3dddifmt_dxva_reserved27"></a><b>D3DDDIFMT_DXVA_RESERVED27</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED28"></a><a id="d3dddifmt_dxva_reserved28"></a><b>D3DDDIFMT_DXVA_RESERVED28</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED29"></a><a id="d3dddifmt_dxva_reserved29"></a><b>D3DDDIFMT_DXVA_RESERVED29</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED30"></a><a id="d3dddifmt_dxva_reserved30"></a><b>D3DDDIFMT_DXVA_RESERVED30</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVA_RESERVED31"></a><a id="d3dddifmt_dxva_reserved31"></a><b>D3DDDIFMT_DXVA_RESERVED31</b>

<dd>
<p>Reserved for a DirectX VA format type.</p>
</dd>

### -field <a id="D3DDDIFMT_DXVACOMPBUFFER_MAX"></a><a id="d3dddifmt_dxvacompbuffer_max"></a><b>D3DDDIFMT_DXVACOMPBUFFER_MAX</b>

<dd>
<p>Indicates that the maximum compressed buffer format value was reached.</p>
</dd>

### -field <a id="D3DDDIFMT_BINARYBUFFER"></a><a id="d3dddifmt_binarybuffer"></a><b>D3DDDIFMT_BINARYBUFFER</b>

<dd>
<p>A binary-buffer format.</p>
</dd>

### -field <a id="D3DDDIFMT_FORCE_UINT"></a><a id="d3dddifmt_force_uint"></a><b>D3DDDIFMT_FORCE_UINT</b>

<dd>
<p>Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. You should not use this value.</p>
</dd>
</dl>

## -remarks
<p>Note that formats are supplied by hardware vendors and many FOURCC codes are not listed in the D3DDDIFORMAT enumeration type. The formats in D3DDDIFORMAT are unique because they are sanctioned by the Microsoft Direct3D runtime; that is, the reference rasterizer operates on all of them. Vendors support vendor-supplied formats on a card-by-card basis.</p>

<p>Note that formats are supplied by hardware vendors and many FOURCC codes are not listed in the D3DDDIFORMAT enumeration type. The formats in D3DDDIFORMAT are unique because they are sanctioned by the Microsoft Direct3D runtime; that is, the reference rasterizer operates on all of them. Vendors support vendor-supplied formats on a card-by-card basis.</p>

<p>Note that formats are supplied by hardware vendors and many FOURCC codes are not listed in the D3DDDIFORMAT enumeration type. The formats in D3DDDIFORMAT are unique because they are sanctioned by the Microsoft Direct3D runtime; that is, the reference rasterizer operates on all of them. Vendors support vendor-supplied formats on a card-by-card basis.</p>

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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542963">D3DDDIARG_CREATERESOURCE</a>
</dt>
<dt>
<a href="direct3ddxgi.dxgi_format">DXGI_FORMAT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIFORMAT enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
