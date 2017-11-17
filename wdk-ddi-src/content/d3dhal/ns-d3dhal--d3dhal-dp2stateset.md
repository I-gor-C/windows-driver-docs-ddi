---
UID: NS.d3dhal._D3DHAL_DP2STATESET
title: D3DHAL_DP2STATESET
author: windows-driver-content
description: The D3DHAL_DP2STATESET structure is used to inform the driver about stateset operations to perform.
old-location: display\d3dhal_dp2stateset.htm
ms.assetid: 3405cca6-8d65-4879-98e8-3cd8f66003a5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DHAL_DP2STATESET
req.alt-loc: d3dhal.h
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
ms.keywords: D3DHAL_DP2STATESET, D3DHAL_DP2STATESET
req.iface: 
---

# D3DHAL_DP2STATESET structure



## -description
<p>The D3DHAL_DP2STATESET structure is used to inform the driver about stateset operations to perform.</p>


## -syntax

````
typedef struct _D3DHAL_DP2STATESET {
  DWORD             dwOperation;
  DWORD             dwParam;
  D3DSTATEBLOCKTYPE sbType;
} D3DHAL_DP2STATESET, *LPD3DHAL_DP2STATESET;
````


## -struct-fields
<dl>

### -field <b>dwOperation</b>

<dd>
<p>Specifies the operation to perform. The value of this member can be one of the following:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DHAL_STATESETBEGIN</p>
</td>
<td>
<p>Specifies the beginning of the stateset referenced by <b>dwParam</b>.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHAL_STATESETCAPTURE</p>
</td>
<td>
<p>Specifies that capture is to be done. When this flag is specified, the driver must capture a snapshot of the current state that matches the state block referenced by the handle passed in <b>dwParam</b>. That is, only the state that is specified in the state block is captured. See <a href="https://msdn.microsoft.com/276d3cdb-34bf-49e8-aae5-94315746c5ff">Accelerated State Management</a> for important details about state capture.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHAL_STATESETCREATE</p>
</td>
<td>
<p>DirectX 8.0 and later versions only.</p>
<p>On receipt of this request the driver should create a state block of the type given in the field <b>sbType</b>. The information to record for each state block type is described below.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHAL_STATESETDELETE</p>
</td>
<td>
<p>Specifies that the stateset referenced by <b>dwParam</b> should be deleted.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHAL_STATESETEND</p>
</td>
<td>
<p>Specifies the end of the stateset referenced by <b>dwParam</b>.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHAL_STATESETEXECUTE</p>
</td>
<td>
<p>Specifies that the stateset referenced by <b>dwParam</b> should be executed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwParam</b>

<dd>
<p>Specifies the stateset handle that references the state block being manipulated with the current <b>dwOperation</b>.</p>
</dd>

### -field <b>sbType</b>

<dd>
<p>Specifies the state block type. The driver should ignore this member unless it implements render state extensions, or implements support for <a href="https://msdn.microsoft.com/6ad3412c-fd80-41c0-9abc-117aacc5ddae">pure devices</a> (DirectX 8.0 and later versions only).</p>
<p>If the driver implements extended render states, that is, render states beyond those the Direct3D runtime supplies, it can use <b>sbType</b> to determine what types of predefined render states are being used. From this information the driver can determine how to append the state block appropriately, to support its extensions. </p>
<p>The <b>sbType</b> member, which is valid only for D3DHAL_STATESETBEGIN, D3DHAL_STATESETEND, and D3DHAL_STATECREATE, specifies the state block type with one of the following D3DSTATEBLOCKTYPE enumerated types. For more details see the DirectX SDK documentation.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DSBT_ALL</p>
</td>
<td>
<p>Signals the driver to capture all state.</p>
<p>When requested to capture all state in pure device mode the driver should capture all state with the exception of the current vertex stream state, the current index stream state and the currently realized textures.</p>
<p>The state that should be captured is as follows; the render states listed below, the texture stage states listed below, the viewport, all the world transforms, the view transform, the projection transform, the texture transform for all texture stages, all user clip planes, the current material, all lights that have been used prior to the state block creation, the current vertex shader handle, the current pixel shader handle, the current vertex shader constants and the current pixel shader constants.</p>
<p>The render states to record are as follows:</p>
<pre xml:space="preserve"><code>D3DRENDERSTATE_SPECULARENABLE
D3DRENDERSTATE_ZENABLE
D3DRENDERSTATE_FILLMODE
D3DRENDERSTATE_SHADEMODE
D3DRENDERSTATE_LINEPATTERN
D3DRENDERSTATE_ZWRITEENABLE
D3DRENDERSTATE_ALPHATESTENABLE
D3DRENDERSTATE_LASTPIXEL
D3DRENDERSTATE_SRCBLEND
D3DRENDERSTATE_DESTBLEND
D3DRENDERSTATE_CULLMODE
D3DRENDERSTATE_ZFUNC
D3DRENDERSTATE_ALPHAREF
D3DRENDERSTATE_ALPHAFUNC
D3DRENDERSTATE_DITHERENABLE
D3DRENDERSTATE_FOGENABLE
D3DRENDERSTATE_STIPPLEDALPHA
D3DRENDERSTATE_FOGCOLOR
D3DRENDERSTATE_FOGTABLEMODE
D3DRENDERSTATE_FOGSTART
D3DRENDERSTATE_FOGEND
D3DRENDERSTATE_FOGDENSITY
D3DRENDERSTATE_EDGEANTIALIAS
D3DRENDERSTATE_ALPHABLENDENABLE
D3DRENDERSTATE_ZBIAS
D3DRENDERSTATE_RANGEFOGENABLE
D3DRENDERSTATE_STENCILENABLE
D3DRENDERSTATE_STENCILFAIL
D3DRENDERSTATE_STENCILZFAIL
D3DRENDERSTATE_STENCILPASS
D3DRENDERSTATE_STENCILFUNC
D3DRENDERSTATE_STENCILREF
D3DRENDERSTATE_STENCILMASK
D3DRENDERSTATE_STENCILWRITEMASK
D3DRENDERSTATE_TEXTUREFACTOR
D3DRENDERSTATE_WRAP0
D3DRENDERSTATE_WRAP1
D3DRENDERSTATE_WRAP2
D3DRENDERSTATE_WRAP3
D3DRENDERSTATE_WRAP4
D3DRENDERSTATE_WRAP5
D3DRENDERSTATE_WRAP6
D3DRENDERSTATE_WRAP7
D3DRENDERSTATE_AMBIENT
D3DRENDERSTATE_COLORVERTEX
D3DRENDERSTATE_FOGVERTEXMODE
D3DRENDERSTATE_CLIPPING
D3DRENDERSTATE_LIGHTING
D3DRENDERSTATE_NORMALIZENORMALS
D3DRENDERSTATE_LOCALVIEWER
D3DRENDERSTATE_EMISSIVEMATERIALSOURCE
D3DRENDERSTATE_AMBIENTMATERIALSOURCE
D3DRENDERSTATE_DIFFUSEMATERIALSOURCE
D3DRENDERSTATE_SPECULARMATERIALSOURCE
D3DRENDERSTATE_VERTEXBLEND
D3DRENDERSTATE_CLIPPLANEENABLE
D3DRS_SOFTWAREVERTEXPROCESSING
D3DRS_POINTSIZE
D3DRS_POINTSIZE_MIN
D3DRS_POINTSPRITEENABLE
D3DRS_POINTSCALEENABLE
D3DRS_POINTSCALE_A
D3DRS_POINTSCALE_B
D3DRS_POINTSCALE_C
D3DRS_MULTISAMPLEANTIALIAS
D3DRS_MULTISAMPLEMASK
D3DRS_PATCHEDGESTYLE
D3DRS_PATCHSEGMENTS
D3DRS_POINTSIZE_MAX
D3DRS_INDEXEDVERTEXBLENDENABLE
D3DRS_COLORWRITEENABLE
D3DRS_TWEENFACTOR
D3DRS_BLENDOP</code></pre>
<p>The texture stage states to record are as follows:</p>
<pre xml:space="preserve"><code>D3DTSS_COLOROP
D3DTSS_COLORARG1
D3DTSS_COLORARG2
D3DTSS_ALPHAOP
D3DTSS_ALPHAARG1
D3DTSS_ALPHAARG2
D3DTSS_BUMPENVMAT00
D3DTSS_BUMPENVMAT01
D3DTSS_BUMPENVMAT10
D3DTSS_BUMPENVMAT11
D3DTSS_TEXCOORDINDEX
D3DTSS_ADDRESSU
D3DTSS_ADDRESSV
D3DTSS_BORDERCOLOR
D3DTSS_MAGFILTER
D3DTSS_MINFILTER
D3DTSS_MIPFILTER
D3DTSS_MIPMAPLODBIAS
D3DTSS_MAXMIPLEVEL
D3DTSS_MAXANISOTROPY
D3DTSS_BUMPENVLSCALE
D3DTSS_BUMPENVLOFFSET
D3DTSS_TEXTURETRANSFORMFLAGS
D3DTSS_ADDRESSW
D3DTSS_COLORARG0
D3DTSS_ALPHAARG0
D3DTSS_RESULTARG</code></pre>
</td>
</tr>
<tr>
<td>
<p>D3DSBT_PIXELSTATE</p>
</td>
<td>
<p>Signals the driver to capture pixel state only.</p>
<p>When capturing pixel state in pure device mode the following state should be captured; the pixel processing related render states listed below, the pixel processing texture stage states listed below, the current pixel shader handle and the current pixel shader constants.</p>
<p>The render states to record are as follows:</p>
<pre xml:space="preserve"><code>D3DRENDERSTATE_ZENABLE
D3DRENDERSTATE_FILLMODE
D3DRENDERSTATE_SHADEMODE
D3DRENDERSTATE_LINEPATTERN
D3DRENDERSTATE_ZWRITEENABLE
D3DRENDERSTATE_ALPHATESTENABLE
D3DRENDERSTATE_LASTPIXEL
D3DRENDERSTATE_SRCBLEND
D3DRENDERSTATE_DESTBLEND
D3DRENDERSTATE_ZFUNC
D3DRENDERSTATE_ALPHAREF
D3DRENDERSTATE_ALPHAFUNC
D3DRENDERSTATE_DITHERENABLE
D3DRENDERSTATE_STIPPLEDALPHA
D3DRENDERSTATE_FOGSTART
D3DRENDERSTATE_FOGEND
D3DRENDERSTATE_FOGDENSITY
D3DRENDERSTATE_EDGEANTIALIAS
D3DRENDERSTATE_ALPHABLENDENABLE
D3DRENDERSTATE_ZBIAS
D3DRENDERSTATE_STENCILENABLE
D3DRENDERSTATE_STENCILFAIL
D3DRENDERSTATE_STENCILZFAIL
D3DRENDERSTATE_STENCILPASS
D3DRENDERSTATE_STENCILFUNC
D3DRENDERSTATE_STENCILREF
D3DRENDERSTATE_STENCILMASK
D3DRENDERSTATE_STENCILWRITEMASK
D3DRENDERSTATE_TEXTUREFACTOR
D3DRENDERSTATE_WRAP0
D3DRENDERSTATE_WRAP1
D3DRENDERSTATE_WRAP2
D3DRENDERSTATE_WRAP3
D3DRENDERSTATE_WRAP4
D3DRENDERSTATE_WRAP5
D3DRENDERSTATE_WRAP6
D3DRENDERSTATE_WRAP7
D3DRS_COLORWRITEENABLE
D3DRS_BLENDOP</code></pre>
<p>The texture stage states to record are as follows:</p>
<pre xml:space="preserve"><code>D3DTSS_COLOROP
D3DTSS_COLORARG1
D3DTSS_COLORARG2
D3DTSS_ALPHAOP
D3DTSS_ALPHAARG1
D3DTSS_ALPHAARG2
D3DTSS_BUMPENVMAT00
D3DTSS_BUMPENVMAT01
D3DTSS_BUMPENVMAT10
D3DTSS_BUMPENVMAT11
D3DTSS_TEXCOORDINDEX
D3DTSS_ADDRESSU
D3DTSS_ADDRESSV
D3DTSS_BORDERCOLOR
D3DTSS_MAGFILTER
D3DTSS_MINFILTER
D3DTSS_MIPFILTER
D3DTSS_MIPMAPLODBIAS
D3DTSS_MAXMIPLEVEL
D3DTSS_MAXANISOTROPY
D3DTSS_BUMPENVLSCALE
D3DTSS_BUMPENVLOFFSET
D3DTSS_TEXTURETRANSFORMFLAGS
D3DTSS_ADDRESSW
D3DTSS_COLORARG0
D3DTSS_ALPHAARG0
D3DTSS_RESULTARG</code></pre>
</td>
</tr>
<tr>
<td>
<p>D3DSBT_VERTEXSTATE</p>
</td>
<td>
<p>Signals the driver to capture vertex state only.</p>
<p>When capturing vertex state in pure device mode the following state should be captured; the vertex processing related render states listed below, the vertex processing texture stage states listed below, all lights that have been used prior to the state block creation, the current vertex shader handle and the current vertex shader constants.</p>
<p>The render states to record are as follows:</p>
<pre xml:space="preserve"><code>D3DRENDERSTATE_SHADEMODE
D3DRENDERSTATE_SPECULARENABLE
D3DRENDERSTATE_CULLMODE
D3DRENDERSTATE_FOGENABLE
D3DRENDERSTATE_FOGCOLOR
D3DRENDERSTATE_FOGTABLEMODE
D3DRENDERSTATE_FOGSTART
D3DRENDERSTATE_FOGEND
D3DRENDERSTATE_FOGDENSITY
D3DRENDERSTATE_RANGEFOGENABLE
D3DRENDERSTATE_AMBIENT
D3DRENDERSTATE_COLORVERTEX
D3DRENDERSTATE_FOGVERTEXMODE
D3DRENDERSTATE_CLIPPING
D3DRENDERSTATE_LIGHTING
D3DRENDERSTATE_NORMALIZENORMALS
D3DRENDERSTATE_LOCALVIEWER
D3DRENDERSTATE_EMISSIVEMATERIALSOURCE
D3DRENDERSTATE_AMBIENTMATERIALSOURCE
D3DRENDERSTATE_DIFFUSEMATERIALSOURCE
D3DRENDERSTATE_SPECULARMATERIALSOURCE
D3DRENDERSTATE_VERTEXBLEND
D3DRENDERSTATE_CLIPPLANEENABLE
D3DRS_SOFTWAREVERTEXPROCESSING
D3DRS_POINTSIZE
D3DRS_POINTSIZE_MIN
D3DRS_POINTSPRITEENABLE
D3DRS_POINTSCALEENABLE
D3DRS_POINTSCALE_A
D3DRS_POINTSCALE_B
D3DRS_POINTSCALE_C
D3DRS_MULTISAMPLEANTIALIAS
D3DRS_MULTISAMPLEMASK
D3DRS_PATCHEDGESTYLE
D3DRS_PATCHSEGMENTS
D3DRS_POINTSIZE_MAX
D3DRS_INDEXEDVERTEXBLENDENABLE
D3DRS_TWEENFACTOR</code></pre>
<p>The texture stage states to record are as follows:</p>
<pre xml:space="preserve"><code>D3DTSS_TEXCOORDINDEX
D3DTSS_TEXTURETRANSFORMFLAGS</code></pre>
</td>
</tr>
<tr>
<td>
<p>NULL</p>
</td>
<td>
<p>No predefined state group is specified.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>See <a href="https://msdn.microsoft.com/276d3cdb-34bf-49e8-aae5-94315746c5ff">Accelerated State Management</a> in the Graphics Design Guide for more information about the use of this structure in state block management.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>