---
UID: NS.d3d10umddi.D3D11_1_DDI_RENDER_TARGET_BLEND_DESC
title: D3D11_1_DDI_RENDER_TARGET_BLEND_DESC
author: windows-driver-content
description: Describes a blend state for a render target. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers.
old-location: display\d3d11_1_ddi_render_target_blend_desc.htm
old-project: display
ms.assetid: ad90ad4c-625f-4177-8160-cd6576942c91
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11_1_DDI_RENDER_TARGET_BLEND_DESC, D3D11_1_DDI_RENDER_TARGET_BLEND_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1_DDI_RENDER_TARGET_BLEND_DESC
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
req.iface: 
---

# D3D11_1_DDI_RENDER_TARGET_BLEND_DESC structure



## -description
<p>Describes a blend state for a render target. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers.</p>


## -syntax

````
typedef struct D3D11_1_DDI_RENDER_TARGET_BLEND_DESC {
  BOOL                 BlendEnable;
  BOOL                 LogicOpEnable;
  D3D10_DDI_BLEND      SrcBlend;
  D3D10_DDI_BLEND      DestBlend;
  D3D10_DDI_BLEND_OP   BlendOp;
  D3D10_DDI_BLEND      SrcBlendAlpha;
  D3D10_DDI_BLEND      DestBlendAlpha;
  D3D10_DDI_BLEND_OP   BlendOpAlpha;
  D3D11_1_DDI_LOGIC_OP LogicOp;
  UINT8                RenderTargetWriteMask;
} D3D11_1_DDI_RENDER_TARGET_BLEND_DESC;
````


## -struct-fields
<dl>

### -field <b>BlendEnable</b>

<dd>
<p>[in] A Boolean value that specifies whether blending is enabled for the associated render target. <b>TRUE</b> indicates blending is enabled; <b>FALSE</b> indicates blending is disabled.</p>
<div class="alert"><b>Note</b>  The <b>LogicOpEnable</b> and <b>BlendEnable</b> members must not both be <b>TRUE</b>.</div>
<div> </div>
</dd>

### -field <b>LogicOpEnable</b>

<dd>
<p>Specifies whether shader logic operations given by the <b>LogicOp</b> member are available in the blend state. The user-mode display driver sets <b>LogicOpEnable</b> to <b>TRUE</b> if logic operations are available in the blend state and <b>FALSE</b> otherwise. </p>
<p>This member is <b>FALSE</b> if the   driver supports Direct3D feature level 9.1, 9.2, and 9.3. This member is optional if the driver supports feature level 10, 10.1, and 11.</p>
<p>This member is <b>TRUE</b> if the driver supports feature level 11.1 and later.</p>
<div class="alert"><b>Note</b>  The <b>LogicOpEnable</b> and <b>BlendEnable</b> members must not both be <b>TRUE</b>.</div>
<div> </div>
</dd>

### -field <b>SrcBlend</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541916">D3D10_DDI_BLEND</a> that indicates the blend mode of the source for the enabled render target. </p>
</dd>

### -field <b>DestBlend</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541916">D3D10_DDI_BLEND</a> that indicates the blend mode of the destination for the enabled render target. </p>
</dd>

### -field <b>BlendOp</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541923">D3D10_DDI_BLEND_OP</a> that indicates the blending operation for the enabled render target. </p>
</dd>

### -field <b>SrcBlendAlpha</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541916">D3D10_DDI_BLEND</a> that indicates the transparency blend mode of the source for the enabled render target. </p>
</dd>

### -field <b>DestBlendAlpha</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541916">D3D10_DDI_BLEND</a> that indicates the transparency blend mode of the destination for the enabled render target. </p>
</dd>

### -field <b>BlendOpAlpha</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541923">D3D10_DDI_BLEND_OP</a> that indicates the transparency blending operation for the enabled render target. </p>
</dd>

### -field <b>LogicOp</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/hh451051">D3D11_1_DDI_LOGIC_OP</a> that specifies  shader logic operations that are available in the blend state.</p>
</dd>

### -field <b>RenderTargetWriteMask</b>

<dd>
<p>[in] An 8-bit bitwise value that indicates the write properties for the enabled render target. Each bit must be set to one of the following values from the D3D10_DDI_COLOR_WRITE_ENABLE enumeration.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>D3D10_DDI_COLOR_WRITE_ENABLE_RED</b> (1)</p>
</td>
<td>
<p>Writes red</p>
</td>
</tr>
<tr>
<td>
<p><b>D3D10_DDI_COLOR_WRITE_ENABLE_GREEN</b> (2)</p>
</td>
<td>
<p>Writes green</p>
</td>
</tr>
<tr>
<td>
<p><b>D3D10_DDI_COLOR_WRITE_ENABLE_BLUE</b> (4)</p>
</td>
<td>
<p>Writes blue</p>
</td>
</tr>
<tr>
<td>
<p><b>D3D10_DDI_COLOR_WRITE_ENABLE_ALPHA</b> (8)</p>
</td>
<td>
<p>Writes a transparency level</p>
</td>
</tr>
<tr>
<td>
<p><b>D3D10_DDI_COLOR_WRITE_ENABLE_ALL</b> (1 | 2 | 4 | 8)</p>
</td>
<td>
<p>Writes red, green, blue, and a transparency level</p>
</td>
</tr>
</table>
<p> </p>
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

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-calcprivateblendstatesize.md">CalcPrivateBlendStateSize(D3D11_1)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createblendstate.md">CreateBlendState(D3D11_1)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541916">D3D10_DDI_BLEND</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541923">D3D10_DDI_BLEND_OP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451041">D3D11_1_DDI_BLEND_DESC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451051">D3D11_1_DDI_LOGIC_OP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1_DDI_RENDER_TARGET_BLEND_DESC structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
