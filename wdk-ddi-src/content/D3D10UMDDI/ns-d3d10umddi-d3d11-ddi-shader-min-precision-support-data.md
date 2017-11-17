---
UID: NS.d3d10umddi.D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA
title: D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA
author: windows-driver-content
description: Describes precision support options for shaders in the user-mode display driver.
old-location: display\d3d11_ddi_shader_min_precision_support_data.htm
ms.assetid: e93649d1-4ad0-4873-99c7-b2f3ed48aac6
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA
req.alt-loc: D3d10umddi.h
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
ms.keywords: D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA, D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA
req.iface: 
---

# D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA structure



## -description
<p>Describes precision support options for shaders in the user-mode display driver.</p>


## -syntax

````
typedef struct D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA {
  UINT PixelShaderMinPrecision;
  UINT AllOtherStagesMinPrecision;
} D3D11_DDI_SHADER_MIN_PRECISION_SUPPORT_DATA;
````


## -struct-fields
<dl>

### -field <b>PixelShaderMinPrecision</b>

<dd>
<p>A combination of values of type <a href="https://msdn.microsoft.com/library/windows/hardware/hh451059">D3D11_DDI_SHADER_MIN_PRECISION</a> that are combined by using a bitwise <b>OR</b> operation. The resulting value specifies minimum precision levels that the driver supports for the pixel shader. A value of zero indicates that the driver supports only the default precision for the shader model, and not a lower precision.</p>
</dd>

### -field <b>AllOtherStagesMinPrecision</b>

<dd>
<p>A combination of values of type <a href="https://msdn.microsoft.com/library/windows/hardware/hh451059">D3D11_DDI_SHADER_MIN_PRECISION</a> that are combined by using a bitwise <b>OR</b> operation. The resulting value specifies minimum precision levels that the driver supports for all other stages in the video processing pipeline that are not pixel shaders. A value of zero indicates that the driver supports only the default precision for the shader model, and not a lower precision.</p>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>