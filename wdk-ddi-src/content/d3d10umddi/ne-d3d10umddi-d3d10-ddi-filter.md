---
UID: NE.d3d10umddi.D3D10_DDI_FILTER
title: D3D10_DDI_FILTER
author: windows-driver-content
description: The D3D10_DDI_FILTER enumeration type contains values that identify filter properties of a sampler in a call to the driver's CreateSampler function.
old-location: display\d3d10_ddi_filter.htm
old-project: display
ms.assetid: 02d0985e-ddf3-49cb-89e4-dcadb908399f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_DDI_FILTER
req.alt-loc: d3d10umddi.h
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

# D3D10_DDI_FILTER enumeration



## -description
<p>The D3D10_DDI_FILTER enumeration type contains values that identify filter properties of a sampler in a call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createsampler.md">CreateSampler</a> function.</p>


## -syntax

````
typedef enum D3D10_DDI_FILTER { 
  D3D10_DDI_FILTER_MIN_MAG_MIP_POINT                            = 0x00000000,
  D3D10_DDI_FILTER_MIN_MAG_POINT_MIP_LINEAR                     = 0x00000001,
  D3D10_DDI_FILTER_MIN_POINT_MAG_LINEAR_MIP_POINT               = 0x00000004,
  D3D10_DDI_FILTER_MIN_POINT_MAG_MIP_LINEAR                     = 0x00000005,
  D3D10_DDI_FILTER_MIN_LINEAR_MAG_MIP_POINT                     = 0x00000010,
  D3D10_DDI_FILTER_MIN_LINEAR_MAG_POINT_MIP_LINEAR              = 0x00000011,
  D3D10_DDI_FILTER_MIN_MAG_LINEAR_MIP_POINT                     = 0x00000014,
  D3D10_DDI_FILTER_MIN_MAG_MIP_LINEAR                           = 0x00000015,
  D3D10_DDI_FILTER_ANISOTROPIC                                  = 0x00000055,
  D3D10_DDI_FILTER_COMPARISON_MIN_MAG_MIP_POINT                 = 0x00000080,
  D3D10_DDI_FILTER_COMPARISON_MIN_MAG_POINT_MIP_LINEAR          = 0x00000081,
  D3D10_DDI_FILTER_COMPARISON_MIN_POINT_MAG_LINEAR_MIP_POINT    = 0x00000084,
  D3D10_DDI_FILTER_COMPARISON_MIN_POINT_MAG_MIP_LINEAR          = 0x00000085,
  D3D10_DDI_FILTER_COMPARISON_MIN_LINEAR_MAG_MIP_POINT          = 0x00000090,
  D3D10_DDI_FILTER_COMPARISON_MIN_LINEAR_MAG_POINT_MIP_LINEAR   = 0x00000091,
  D3D10_DDI_FILTER_COMPARISON_MIN_MAG_LINEAR_MIP_POINT          = 0x00000094,
  D3D10_DDI_FILTER_COMPARISON_MIN_MAG_MIP_LINEAR                = 0x00000095,
  D3D10_DDI_FILTER_COMPARISON_ANISOTROPIC                       = 0x000000d5,
#if D3D11DDI_MINOR_HEADER_VERSION >= 4
  D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_MIP_POINT                = 0x00000100,
  D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_POINT_MIP_LINEAR         = 0x00000101,
  D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_POINT_MAG_LINEAR_MIP_POINT   = 0x00000104,
  D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_POINT_MAG_MIP_LINEAR         = 0x00000105,
  D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_LINEAR_MAG_MIP_POINT         = 0x00000110,
  D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_LINEAR_MAG_POINT_MIP_LINEAR  = 0x00000111,
  D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_LINEAR_MIP_POINT         = 0x00000114,
  D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_MIP_LINEAR               = 0x00000115,
  D3DWDDM1_3DDI_FILTER_MINIMUM_ANISOTROPIC                      = 0x00000155,
  D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_MIP_POINT                = 0x00000180,
  D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_POINT_MIP_LINEAR         = 0x00000181,
  D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_POINT_MAG_LINEAR_MIP_POINT   = 0x00000184,
  D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_POINT_MAG_MIP_LINEAR         = 0x00000185,
  D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_LINEAR_MAG_MIP_POINT         = 0x00000190,
  D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_LINEAR_MAG_POINT_MIP_LINEAR  = 0x00000191,
  D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_LINEAR_MIP_POINT         = 0x00000194,
  D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_MIP_LINEAR               = 0x00000195,
  D3DWDDM1_3DDI_FILTER_MAXIMUM_ANISOTROPIC                      = 0x000000d5,
#endif 
  D3D10_DDI_FILTER_TEXT_1BIT                                    = 0x80000000 
} D3D10_DDI_FILTER;
````


## -enum-fields
<dl>

### -field <a id="D3D10_DDI_FILTER_MIN_MAG_MIP_POINT"></a><a id="d3d10_ddi_filter_min_mag_mip_point"></a><b>D3D10_DDI_FILTER_MIN_MAG_MIP_POINT</b>

<dd>
<p>The sampler uses point filtering for the min (minifying), mag (magnifying), and mip filters. For more information about these types of filters, see Remarks. </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_MIN_MAG_POINT_MIP_LINEAR"></a><a id="d3d10_ddi_filter_min_mag_point_mip_linear"></a><b>D3D10_DDI_FILTER_MIN_MAG_POINT_MIP_LINEAR</b>

<dd>
<p>
      The sampler uses point filtering for the min and mag filters and uses linear filtering for the mip filter. 
     </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_MIN_POINT_MAG_LINEAR_MIP_POINT"></a><a id="d3d10_ddi_filter_min_point_mag_linear_mip_point"></a><b>D3D10_DDI_FILTER_MIN_POINT_MAG_LINEAR_MIP_POINT</b>

<dd>
<p>The sampler uses point filtering for the min and mip filters and uses linear filtering for the mag filter. </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_MIN_POINT_MAG_MIP_LINEAR"></a><a id="d3d10_ddi_filter_min_point_mag_mip_linear"></a><b>D3D10_DDI_FILTER_MIN_POINT_MAG_MIP_LINEAR</b>

<dd>
<p>
      The sampler uses point filtering for the min filter and uses linear filtering for the mag and mip filters. 
     </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_MIN_LINEAR_MAG_MIP_POINT"></a><a id="d3d10_ddi_filter_min_linear_mag_mip_point"></a><b>D3D10_DDI_FILTER_MIN_LINEAR_MAG_MIP_POINT</b>

<dd>
<p>The sampler uses linear filtering for the min filter and uses point filtering for the mag and mip filters. </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_MIN_LINEAR_MAG_POINT_MIP_LINEAR"></a><a id="d3d10_ddi_filter_min_linear_mag_point_mip_linear"></a><b>D3D10_DDI_FILTER_MIN_LINEAR_MAG_POINT_MIP_LINEAR</b>

<dd>
<p>
      The sampler uses linear filtering for the min and mip filters and uses point filtering for the mag filter. 
     </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_MIN_MAG_LINEAR_MIP_POINT"></a><a id="d3d10_ddi_filter_min_mag_linear_mip_point"></a><b>D3D10_DDI_FILTER_MIN_MAG_LINEAR_MIP_POINT</b>

<dd>
<p>The sampler uses linear filtering for the min and mag filters and uses point filtering for the mip filter. </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_MIN_MAG_MIP_LINEAR"></a><a id="d3d10_ddi_filter_min_mag_mip_linear"></a><b>D3D10_DDI_FILTER_MIN_MAG_MIP_LINEAR</b>

<dd>
<p>
      The sampler uses linear filtering for the min, mag, and mip filters. 
     </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_ANISOTROPIC"></a><a id="d3d10_ddi_filter_anisotropic"></a><b>D3D10_DDI_FILTER_ANISOTROPIC</b>

<dd>
<p>The sampler uses anisotropic filtering. </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_COMPARISON_MIN_MAG_MIP_POINT"></a><a id="d3d10_ddi_filter_comparison_min_mag_mip_point"></a><b>D3D10_DDI_FILTER_COMPARISON_MIN_MAG_MIP_POINT</b>

<dd>
<p>
      The sampler uses point filtering for the min, mag, and mip filters. The sampler also uses comparison filtering. 
     </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_COMPARISON_MIN_MAG_POINT_MIP_LINEAR"></a><a id="d3d10_ddi_filter_comparison_min_mag_point_mip_linear"></a><b>D3D10_DDI_FILTER_COMPARISON_MIN_MAG_POINT_MIP_LINEAR</b>

<dd>
<p>The sampler uses point filtering for the min and mag filters and uses linear filtering for the mip filter. The sampler also uses comparison filtering. </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_COMPARISON_MIN_POINT_MAG_LINEAR_MIP_POINT"></a><a id="d3d10_ddi_filter_comparison_min_point_mag_linear_mip_point"></a><b>D3D10_DDI_FILTER_COMPARISON_MIN_POINT_MAG_LINEAR_MIP_POINT</b>

<dd>
<p>
      The sampler uses point filtering for the min and mip filters and uses linear filtering for the mag filter. The sampler also uses comparison filtering. 
     </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_COMPARISON_MIN_POINT_MAG_MIP_LINEAR"></a><a id="d3d10_ddi_filter_comparison_min_point_mag_mip_linear"></a><b>D3D10_DDI_FILTER_COMPARISON_MIN_POINT_MAG_MIP_LINEAR</b>

<dd>
<p>The sampler uses point filtering for the min filter and uses linear filtering for the mag and mip filters. The sampler also uses comparison filtering. </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_COMPARISON_MIN_LINEAR_MAG_MIP_POINT"></a><a id="d3d10_ddi_filter_comparison_min_linear_mag_mip_point"></a><b>D3D10_DDI_FILTER_COMPARISON_MIN_LINEAR_MAG_MIP_POINT</b>

<dd>
<p>
      The sampler uses linear filtering for the min filter and uses point filtering for the mag and mip filters. The sampler also uses comparison filtering. 
     </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_COMPARISON_MIN_LINEAR_MAG_POINT_MIP_LINEAR"></a><a id="d3d10_ddi_filter_comparison_min_linear_mag_point_mip_linear"></a><b>D3D10_DDI_FILTER_COMPARISON_MIN_LINEAR_MAG_POINT_MIP_LINEAR</b>

<dd>
<p>The sampler uses linear filtering for the min and mip filters and uses point filtering for the mag filter. The sampler also uses comparison filtering. </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_COMPARISON_MIN_MAG_LINEAR_MIP_POINT"></a><a id="d3d10_ddi_filter_comparison_min_mag_linear_mip_point"></a><b>D3D10_DDI_FILTER_COMPARISON_MIN_MAG_LINEAR_MIP_POINT</b>

<dd>
<p>The sampler uses linear filtering for the min and mag filters and uses point filtering for the mip filter. The sampler also uses comparison filtering. </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_COMPARISON_MIN_MAG_MIP_LINEAR"></a><a id="d3d10_ddi_filter_comparison_min_mag_mip_linear"></a><b>D3D10_DDI_FILTER_COMPARISON_MIN_MAG_MIP_LINEAR</b>

<dd>
<p>
      The sampler uses linear filtering for the min, mag, and mip filters. The sampler also uses comparison filtering. 
     </p>
</dd>

### -field <a id="D3D10_DDI_FILTER_COMPARISON_ANISOTROPIC"></a><a id="d3d10_ddi_filter_comparison_anisotropic"></a><b>D3D10_DDI_FILTER_COMPARISON_ANISOTROPIC</b>

<dd>
<p>The sampler uses anisotropic and comparison filtering. </p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_MIP_POINT"></a><a id="d3dwddm1_3ddi_filter_minimum_min_mag_mip_point"></a><b>D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_MIP_POINT</b>

<dd>
<p>The sampler uses point filtering for the min (minifying), mag (magnifying), and mip filters. For more information about these types of filters, see Remarks.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_POINT_MIP_LINEAR"></a><a id="d3dwddm1_3ddi_filter_minimum_min_mag_point_mip_linear"></a><b>D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_POINT_MIP_LINEAR</b>

<dd>
<p>
      The sampler uses point filtering for the min and mag filters and uses linear filtering for the mip filter.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_POINT_MAG_LINEAR_MIP_POINT"></a><a id="d3dwddm1_3ddi_filter_minimum_min_point_mag_linear_mip_point"></a><b>D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_POINT_MAG_LINEAR_MIP_POINT</b>

<dd>
<p>The sampler uses point filtering for the min and mip filters and uses linear filtering for the mag filter.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_POINT_MAG_MIP_LINEAR"></a><a id="d3dwddm1_3ddi_filter_minimum_min_point_mag_mip_linear"></a><b>D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_POINT_MAG_MIP_LINEAR</b>

<dd>
<p>
      The sampler uses point filtering for the min filter and uses linear filtering for the mag and mip filters.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_LINEAR_MAG_MIP_POINT"></a><a id="d3dwddm1_3ddi_filter_minimum_min_linear_mag_mip_point"></a><b>D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_LINEAR_MAG_MIP_POINT</b>

<dd>
<p>The sampler uses linear filtering for the min filter and uses point filtering for the mag and mip filters.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_LINEAR_MAG_POINT_MIP_LINEAR"></a><a id="d3dwddm1_3ddi_filter_minimum_min_linear_mag_point_mip_linear"></a><b>D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_LINEAR_MAG_POINT_MIP_LINEAR</b>

<dd>
<p>
      The sampler uses linear filtering for the min and mip filters and uses point filtering for the mag filter.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_LINEAR_MIP_POINT"></a><a id="d3dwddm1_3ddi_filter_minimum_min_mag_linear_mip_point"></a><b>D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_LINEAR_MIP_POINT</b>

<dd>
<p>The sampler uses linear filtering for the min and mag filters and uses point filtering for the mip filter.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_MIP_LINEAR"></a><a id="d3dwddm1_3ddi_filter_minimum_min_mag_mip_linear"></a><b>D3DWDDM1_3DDI_FILTER_MINIMUM_MIN_MAG_MIP_LINEAR</b>

<dd>
<p>
      The sampler uses linear filtering for the min, mag, and mip filters.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MINIMUM_ANISOTROPIC"></a><a id="d3dwddm1_3ddi_filter_minimum_anisotropic"></a><b>D3DWDDM1_3DDI_FILTER_MINIMUM_ANISOTROPIC</b>

<dd>
<p>The sampler uses anisotropic filtering.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_MIP_POINT"></a><a id="d3dwddm1_3ddi_filter_maximum_min_mag_mip_point"></a><b>D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_MIP_POINT</b>

<dd>
<p>
      The sampler uses point filtering for the min, mag, and mip filters. The sampler also uses comparison filtering.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_POINT_MIP_LINEAR"></a><a id="d3dwddm1_3ddi_filter_maximum_min_mag_point_mip_linear"></a><b>D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_POINT_MIP_LINEAR</b>

<dd>
<p>The sampler uses point filtering for the min and mag filters and uses linear filtering for the mip filter. The sampler also uses comparison filtering.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_POINT_MAG_LINEAR_MIP_POINT"></a><a id="d3dwddm1_3ddi_filter_maximum_min_point_mag_linear_mip_point"></a><b>D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_POINT_MAG_LINEAR_MIP_POINT</b>

<dd>
<p>
      The sampler uses point filtering for the min and mip filters and uses linear filtering for the mag filter. The sampler also uses comparison filtering.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_POINT_MAG_MIP_LINEAR"></a><a id="d3dwddm1_3ddi_filter_maximum_min_point_mag_mip_linear"></a><b>D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_POINT_MAG_MIP_LINEAR</b>

<dd>
<p>The sampler uses point filtering for the min filter and uses linear filtering for the mag and mip filters. The sampler also uses comparison filtering.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_LINEAR_MAG_MIP_POINT"></a><a id="d3dwddm1_3ddi_filter_maximum_min_linear_mag_mip_point"></a><b>D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_LINEAR_MAG_MIP_POINT</b>

<dd>
<p>
      The sampler uses linear filtering for the min filter and uses point filtering for the mag and mip filters. The sampler also uses comparison filtering.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_LINEAR_MAG_POINT_MIP_LINEAR"></a><a id="d3dwddm1_3ddi_filter_maximum_min_linear_mag_point_mip_linear"></a><b>D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_LINEAR_MAG_POINT_MIP_LINEAR</b>

<dd>
<p>The sampler uses linear filtering for the min and mip filters and uses point filtering for the mag filter. The sampler also uses comparison filtering.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_LINEAR_MIP_POINT"></a><a id="d3dwddm1_3ddi_filter_maximum_min_mag_linear_mip_point"></a><b>D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_LINEAR_MIP_POINT</b>

<dd>
<p>The sampler uses linear filtering for the min and mag filters and uses point filtering for the mip filter. The sampler also uses comparison filtering.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_MIP_LINEAR"></a><a id="d3dwddm1_3ddi_filter_maximum_min_mag_mip_linear"></a><b>D3DWDDM1_3DDI_FILTER_MAXIMUM_MIN_MAG_MIP_LINEAR</b>

<dd>
<p>
      The sampler uses linear filtering for the min, mag, and mip filters. The sampler also uses comparison filtering.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3DWDDM1_3DDI_FILTER_MAXIMUM_ANISOTROPIC"></a><a id="d3dwddm1_3ddi_filter_maximum_anisotropic"></a><b>D3DWDDM1_3DDI_FILTER_MAXIMUM_ANISOTROPIC</b>

<dd>
<p>The sampler uses anisotropic and comparison filtering.</p>
<p>Supported starting with Windows 8.1, and used by WDDM 1.3 and later drivers.</p>
</dd>

### -field <a id="D3D10_DDI_FILTER_TEXT_1BIT"></a><a id="d3d10_ddi_filter_text_1bit"></a><b>D3D10_DDI_FILTER_TEXT_1BIT</b>

<dd>
<p>A special case of filtering mode that is intended only for text filtering and the DXGI_FORMAT_R1_UNORM texture format. For more information about text filtering, see the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-settextfiltersize.md">SetTextFilterSize</a> function.</p>
</dd>
</dl>

## -remarks
<p>Filtering determines a representative value from the sample coordinates of a texture and derivatives for those coordinates. The magnitude of the derivative determines the level of detail (LOD) on the texture to read.</p>

<p>If the LOD is positive (which indicates that the region that is sampled is smaller than roughly the size of a texel in the largest active MIP-map level of the texture), the filter is a <i>magnifying</i> filter. Otherwise, the filter is a <i>minifying</i> filter. When magnifying, the largest active MIP-map level of the texture is used. When minifying, the two MIP-map levels that are closest to the LOD are used. For a given MIP-map level that is accessed on a texture, filtering can be <i>point</i> or <i>linear</i>. Point filtering returns the nearest texel to the lookup coordinates. Linear filtering returns the linear-weighted blend of the nearest 4 texels to the sample location.</p>

<p>When the driver chooses between two MIP-map levels, the driver uses the <i>mip</i> filter. The mip filter can also be point or linear. Point mip filtering returns the result of sampling from the nearest mip to the calculated LOD. Linear mip filtering returns the linear-weighted blend between the nearest two MIP-map levels to the calculated LOD.</p>

<p>The values of the D3D10_DDI_FILTER enumeration describe many of the possible combinations of min, mag, and mip filtering that can also be point or linear. For example, D3D10_DDI_FILTER_MIN_MAG_POINT_MIP_LINEAR means to use point filtering for the min and mag filters and to use linear filtering for the mip filter.</p>

<p>Another type of filtering is <i>anisotropic</i>. This takes into account anisotropy in the derivatives of the texture coordinates to perform an area sampling of the texture. For example, if a texture is being viewed at a slope, anisotropic filtering accounts for this when computing what the filtered result should be, at greater processing power than the min, mag, or mip filters. No value is derived in mixing anisotropic filtering with other filtering modes for magnifying and minifying. For anisotropic filtering, the mip filter is always linear. Therefore, the anisotropic filtering values of D3D10_DDI_FILTER do not expose choices of min, mag, or mip.</p>

<p>Filtering can also be described by a comparison component. By default (no comparison filtering), the result of a sampling operation is a blend of a number of samples. Comparison filtering performs identically to the default mode in terms of which set of texels are read from the texture except for one difference. Just before blending the values together to produce a final result, each individual value read from the texture is compared against a reference value that is provided from the shader. The type of comparison (greater than, less than, equal to, and so on) is determined by the selected sampler state. The result of each comparison is true (1.0) or false (0.0). Comparison filtering then blends these true and false results together rather than the original values read from the texture. Therefore, the final result of a comparison filter is always in the range 0.0 to 1.0. The primary use for comparison filtering is for shadow-buffer filtering.</p>

<p>Filtering determines a representative value from the sample coordinates of a texture and derivatives for those coordinates. The magnitude of the derivative determines the level of detail (LOD) on the texture to read.</p>

<p>If the LOD is positive (which indicates that the region that is sampled is smaller than roughly the size of a texel in the largest active MIP-map level of the texture), the filter is a <i>magnifying</i> filter. Otherwise, the filter is a <i>minifying</i> filter. When magnifying, the largest active MIP-map level of the texture is used. When minifying, the two MIP-map levels that are closest to the LOD are used. For a given MIP-map level that is accessed on a texture, filtering can be <i>point</i> or <i>linear</i>. Point filtering returns the nearest texel to the lookup coordinates. Linear filtering returns the linear-weighted blend of the nearest 4 texels to the sample location.</p>

<p>When the driver chooses between two MIP-map levels, the driver uses the <i>mip</i> filter. The mip filter can also be point or linear. Point mip filtering returns the result of sampling from the nearest mip to the calculated LOD. Linear mip filtering returns the linear-weighted blend between the nearest two MIP-map levels to the calculated LOD.</p>

<p>The values of the D3D10_DDI_FILTER enumeration describe many of the possible combinations of min, mag, and mip filtering that can also be point or linear. For example, D3D10_DDI_FILTER_MIN_MAG_POINT_MIP_LINEAR means to use point filtering for the min and mag filters and to use linear filtering for the mip filter.</p>

<p>Another type of filtering is <i>anisotropic</i>. This takes into account anisotropy in the derivatives of the texture coordinates to perform an area sampling of the texture. For example, if a texture is being viewed at a slope, anisotropic filtering accounts for this when computing what the filtered result should be, at greater processing power than the min, mag, or mip filters. No value is derived in mixing anisotropic filtering with other filtering modes for magnifying and minifying. For anisotropic filtering, the mip filter is always linear. Therefore, the anisotropic filtering values of D3D10_DDI_FILTER do not expose choices of min, mag, or mip.</p>

<p>Filtering can also be described by a comparison component. By default (no comparison filtering), the result of a sampling operation is a blend of a number of samples. Comparison filtering performs identically to the default mode in terms of which set of texels are read from the texture except for one difference. Just before blending the values together to produce a final result, each individual value read from the texture is compared against a reference value that is provided from the shader. The type of comparison (greater than, less than, equal to, and so on) is determined by the selected sampler state. The result of each comparison is true (1.0) or false (0.0). Comparison filtering then blends these true and false results together rather than the original values read from the texture. Therefore, the final result of a comparison filter is always in the range 0.0 to 1.0. The primary use for comparison filtering is for shadow-buffer filtering.</p>

<p>Filtering determines a representative value from the sample coordinates of a texture and derivatives for those coordinates. The magnitude of the derivative determines the level of detail (LOD) on the texture to read.</p>

<p>If the LOD is positive (which indicates that the region that is sampled is smaller than roughly the size of a texel in the largest active MIP-map level of the texture), the filter is a <i>magnifying</i> filter. Otherwise, the filter is a <i>minifying</i> filter. When magnifying, the largest active MIP-map level of the texture is used. When minifying, the two MIP-map levels that are closest to the LOD are used. For a given MIP-map level that is accessed on a texture, filtering can be <i>point</i> or <i>linear</i>. Point filtering returns the nearest texel to the lookup coordinates. Linear filtering returns the linear-weighted blend of the nearest 4 texels to the sample location.</p>

<p>When the driver chooses between two MIP-map levels, the driver uses the <i>mip</i> filter. The mip filter can also be point or linear. Point mip filtering returns the result of sampling from the nearest mip to the calculated LOD. Linear mip filtering returns the linear-weighted blend between the nearest two MIP-map levels to the calculated LOD.</p>

<p>The values of the D3D10_DDI_FILTER enumeration describe many of the possible combinations of min, mag, and mip filtering that can also be point or linear. For example, D3D10_DDI_FILTER_MIN_MAG_POINT_MIP_LINEAR means to use point filtering for the min and mag filters and to use linear filtering for the mip filter.</p>

<p>Another type of filtering is <i>anisotropic</i>. This takes into account anisotropy in the derivatives of the texture coordinates to perform an area sampling of the texture. For example, if a texture is being viewed at a slope, anisotropic filtering accounts for this when computing what the filtered result should be, at greater processing power than the min, mag, or mip filters. No value is derived in mixing anisotropic filtering with other filtering modes for magnifying and minifying. For anisotropic filtering, the mip filter is always linear. Therefore, the anisotropic filtering values of D3D10_DDI_FILTER do not expose choices of min, mag, or mip.</p>

<p>Filtering can also be described by a comparison component. By default (no comparison filtering), the result of a sampling operation is a blend of a number of samples. Comparison filtering performs identically to the default mode in terms of which set of texels are read from the texture except for one difference. Just before blending the values together to produce a final result, each individual value read from the texture is compared against a reference value that is provided from the shader. The type of comparison (greater than, less than, equal to, and so on) is determined by the selected sampler state. The result of each comparison is true (1.0) or false (0.0). Comparison filtering then blends these true and false results together rather than the original values read from the texture. Therefore, the final result of a comparison filter is always in the range 0.0 to 1.0. The primary use for comparison filtering is for shadow-buffer filtering.</p>

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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createsampler.md">CreateSampler</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542011">D3D10_DDI_SAMPLER_DESC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_DDI_FILTER enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
