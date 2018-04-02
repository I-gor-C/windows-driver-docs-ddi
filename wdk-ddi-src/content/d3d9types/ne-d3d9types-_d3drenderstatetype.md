---
UID: NE:d3d9types._D3DRENDERSTATETYPE
title: "_D3DRENDERSTATETYPE"
author: windows-driver-content
description: The D3DRENDERSTATETYPE enumerated type lists a variety of attributes, or render states.
old-location: display\d3drenderstatetype.htm
old-project: display
ms.assetid: 82978b22-1538-4da0-bcf2-c4c52d2e3429
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DRENDERSTATETYPE, D3DRENDERSTATE_EVICTMANAGEDTEXTURES, D3DRENDERSTATE_SCENECAPTURE, D3DRS_DELETERTPATCH, D3DRS_MAXPIXELSHADERINST, D3DRS_MAXVERTEXSHADERINST, _D3DRENDERSTATETYPE, d3d9types/, d3d9types/D3DRENDERSTATE_EVICTMANAGEDTEXTURES, d3d9types/D3DRENDERSTATE_SCENECAPTURE, d3d9types/D3DRS_DELETERTPATCH, d3d9types/D3DRS_MAXPIXELSHADERINST, d3d9types/D3DRS_MAXVERTEXSHADERINST, d3denum_6b8d96f8-ff88-43c3-9850-a213d84d548f.xml, display.d3drenderstatetype, enumeration [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d9types.h
req.include-header: D3dhal.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3d9types.h
api_name:
-	D3DRENDERSTATETYPE
product: Windows
targetos: Windows
req.typenames: D3DRENDERSTATETYPE
---

# _D3DRENDERSTATETYPE Enumeration
The D3DRENDERSTATETYPE enumerated type lists a variety of attributes, or render states. 
  The enumerators of D3DRENDERSTATETYPE that are used exclusively by drivers can specify either rendering information or a texture attribute. The following render states are used by display drivers:

## Syntax
```
typedef enum _D3DRENDERSTATETYPE {
  D3DRS_ZENABLE                     ,
  D3DRS_FILLMODE                    ,
  D3DRS_SHADEMODE                   ,
  D3DRS_ZWRITEENABLE                ,
  D3DRS_ALPHATESTENABLE             ,
  D3DRS_LASTPIXEL                   ,
  D3DRS_SRCBLEND                    ,
  D3DRS_DESTBLEND                   ,
  D3DRS_CULLMODE                    ,
  D3DRS_ZFUNC                       ,
  D3DRS_ALPHAREF                    ,
  D3DRS_ALPHAFUNC                   ,
  D3DRS_DITHERENABLE                ,
  D3DRS_ALPHABLENDENABLE            ,
  D3DRS_FOGENABLE                   ,
  D3DRS_SPECULARENABLE              ,
  D3DRS_FOGCOLOR                    ,
  D3DRS_FOGTABLEMODE                ,
  D3DRS_FOGSTART                    ,
  D3DRS_FOGEND                      ,
  D3DRS_FOGDENSITY                  ,
  D3DRS_RANGEFOGENABLE              ,
  D3DRS_STENCILENABLE               ,
  D3DRS_STENCILFAIL                 ,
  D3DRS_STENCILZFAIL                ,
  D3DRS_STENCILPASS                 ,
  D3DRS_STENCILFUNC                 ,
  D3DRS_STENCILREF                  ,
  D3DRS_STENCILMASK                 ,
  D3DRS_STENCILWRITEMASK            ,
  D3DRS_TEXTUREFACTOR               ,
  D3DRS_WRAP0                       ,
  D3DRS_WRAP1                       ,
  D3DRS_WRAP2                       ,
  D3DRS_WRAP3                       ,
  D3DRS_WRAP4                       ,
  D3DRS_WRAP5                       ,
  D3DRS_WRAP6                       ,
  D3DRS_WRAP7                       ,
  D3DRS_CLIPPING                    ,
  D3DRS_LIGHTING                    ,
  D3DRS_AMBIENT                     ,
  D3DRS_FOGVERTEXMODE               ,
  D3DRS_COLORVERTEX                 ,
  D3DRS_LOCALVIEWER                 ,
  D3DRS_NORMALIZENORMALS            ,
  D3DRS_DIFFUSEMATERIALSOURCE       ,
  D3DRS_SPECULARMATERIALSOURCE      ,
  D3DRS_AMBIENTMATERIALSOURCE       ,
  D3DRS_EMISSIVEMATERIALSOURCE      ,
  D3DRS_VERTEXBLEND                 ,
  D3DRS_CLIPPLANEENABLE             ,
  D3DRS_POINTSIZE                   ,
  D3DRS_POINTSIZE_MIN               ,
  D3DRS_POINTSPRITEENABLE           ,
  D3DRS_POINTSCALEENABLE            ,
  D3DRS_POINTSCALE_A                ,
  D3DRS_POINTSCALE_B                ,
  D3DRS_POINTSCALE_C                ,
  D3DRS_MULTISAMPLEANTIALIAS        ,
  D3DRS_MULTISAMPLEMASK             ,
  D3DRS_PATCHEDGESTYLE              ,
  D3DRS_DEBUGMONITORTOKEN           ,
  D3DRS_POINTSIZE_MAX               ,
  D3DRS_INDEXEDVERTEXBLENDENABLE    ,
  D3DRS_COLORWRITEENABLE            ,
  D3DRS_TWEENFACTOR                 ,
  D3DRS_BLENDOP                     ,
  D3DRS_POSITIONDEGREE              ,
  D3DRS_NORMALDEGREE                ,
  D3DRS_SCISSORTESTENABLE           ,
  D3DRS_SLOPESCALEDEPTHBIAS         ,
  D3DRS_ANTIALIASEDLINEENABLE       ,
  D3DRS_MINTESSELLATIONLEVEL        ,
  D3DRS_MAXTESSELLATIONLEVEL        ,
  D3DRS_ADAPTIVETESS_X              ,
  D3DRS_ADAPTIVETESS_Y              ,
  D3DRS_ADAPTIVETESS_Z              ,
  D3DRS_ADAPTIVETESS_W              ,
  D3DRS_ENABLEADAPTIVETESSELLATION  ,
  D3DRS_TWOSIDEDSTENCILMODE         ,
  D3DRS_CCW_STENCILFAIL             ,
  D3DRS_CCW_STENCILZFAIL            ,
  D3DRS_CCW_STENCILPASS             ,
  D3DRS_CCW_STENCILFUNC             ,
  D3DRS_COLORWRITEENABLE1           ,
  D3DRS_COLORWRITEENABLE2           ,
  D3DRS_COLORWRITEENABLE3           ,
  D3DRS_BLENDFACTOR                 ,
  D3DRS_SRGBWRITEENABLE             ,
  D3DRS_DEPTHBIAS                   ,
  D3DRS_WRAP8                       ,
  D3DRS_WRAP9                       ,
  D3DRS_WRAP10                      ,
  D3DRS_WRAP11                      ,
  D3DRS_WRAP12                      ,
  D3DRS_WRAP13                      ,
  D3DRS_WRAP14                      ,
  D3DRS_WRAP15                      ,
  D3DRS_SEPARATEALPHABLENDENABLE    ,
  D3DRS_SRCBLENDALPHA               ,
  D3DRS_DESTBLENDALPHA              ,
  D3DRS_BLENDOPALPHA                ,
  D3DRS_FORCE_DWORD
} D3DRENDERSTATETYPE;
```

## Constants

<table>
            
                <tr>
                    <td>D3DRS_ZENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_FILLMODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_SHADEMODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ZWRITEENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ALPHATESTENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_LASTPIXEL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_SRCBLEND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_DESTBLEND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_CULLMODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ZFUNC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ALPHAREF</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ALPHAFUNC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_DITHERENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ALPHABLENDENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_FOGENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_SPECULARENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_FOGCOLOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_FOGTABLEMODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_FOGSTART</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_FOGEND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_FOGDENSITY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_RANGEFOGENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_STENCILENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_STENCILFAIL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_STENCILZFAIL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_STENCILPASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_STENCILFUNC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_STENCILREF</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_STENCILMASK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_STENCILWRITEMASK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_TEXTUREFACTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP1</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP3</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP4</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP5</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP6</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP7</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_CLIPPING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_LIGHTING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_AMBIENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_FOGVERTEXMODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_COLORVERTEX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_LOCALVIEWER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_NORMALIZENORMALS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_DIFFUSEMATERIALSOURCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_SPECULARMATERIALSOURCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_AMBIENTMATERIALSOURCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_EMISSIVEMATERIALSOURCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_VERTEXBLEND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_CLIPPLANEENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_POINTSIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_POINTSIZE_MIN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_POINTSPRITEENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_POINTSCALEENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_POINTSCALE_A</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_POINTSCALE_B</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_POINTSCALE_C</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_MULTISAMPLEANTIALIAS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_MULTISAMPLEMASK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_PATCHEDGESTYLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_DEBUGMONITORTOKEN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_POINTSIZE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_INDEXEDVERTEXBLENDENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_COLORWRITEENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_TWEENFACTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_BLENDOP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_POSITIONDEGREE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_NORMALDEGREE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_SCISSORTESTENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_SLOPESCALEDEPTHBIAS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ANTIALIASEDLINEENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_MINTESSELLATIONLEVEL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_MAXTESSELLATIONLEVEL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ADAPTIVETESS_X</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ADAPTIVETESS_Y</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ADAPTIVETESS_Z</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ADAPTIVETESS_W</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_ENABLEADAPTIVETESSELLATION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_TWOSIDEDSTENCILMODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_CCW_STENCILFAIL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_CCW_STENCILZFAIL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_CCW_STENCILPASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_CCW_STENCILFUNC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_COLORWRITEENABLE1</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_COLORWRITEENABLE2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_COLORWRITEENABLE3</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_BLENDFACTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_SRGBWRITEENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_DEPTHBIAS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP8</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP9</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP10</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP11</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP12</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP13</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP14</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_WRAP15</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_SEPARATEALPHABLENDENABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_SRCBLENDALPHA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_DESTBLENDALPHA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_BLENDOPALPHA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DRS_FORCE_DWORD</td>
                    <td></td>
                </tr>
</table>

## Remarks

The driver uses these render states when it performs graphics rendering. Only render states that are specific to drivers are included in the Windows Driver Kit (WDK) documentation. The render states accessible to DirectX applications are included in the DirectX SDK documentation. These application-level render states include such characteristics as whether alpha blending is enabled, whether dithering is enabled, whether Direct3D lighting is used, and the type of shading to be used. 

To update a particular render state, Direct3D stores information about the render state, and then calls the driver's <a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a> callback routine. The information provided to the driver enables it to:

<ul>
<li>
Determine that it should update one or more render states.

</li>
<li>
Identify which render states to update, and what the new render state values should be.

</li>
</ul>
Note that for certain render states to be honored, the driver must have previously set capability flags in the relevant member of the D3DPRIMCAPS structure.

In order to indicate a specific render state update, Direct3D inserts a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a> structure into the command buffer, setting the <b>bCommand</b> member of this structure to D3DDP2OP_RENDERSTATE (see the description for D3DDP2OP_RENDERSTATE in <a href="https://msdn.microsoft.com/library/windows/hardware/ff545678">D3DHAL_DP2OPERATION</a>), and setting the <b>wStateCount</b> member of the same structure to the number of render states to be updated.

Immediately following the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a> structure, Direct3D inserts one <a href="https://msdn.microsoft.com/library/windows/hardware/ff545705">D3DHAL_DP2RENDERSTATE</a> structure into the command buffer for each render state to be updated. The <b>RenderState</b> member of this structure identifies the render state to be changed; the new value of this render state is specified in either the <b>dwState</b> member (for DWORD values) or the <b>fState</b> member (for D3DVALUE values).

The following figure shows a portion of the command buffer containing a D3DDP2OP_RENDERSTATE command and two D3DHAL_DP2RENDERSTATE structures. The first of the three structures indicates that two render states are to be updated. The second structure indicates that the D3DRENDERSTATE_FILLMODE render state is to be changed to D3DFILL_SOLID. The third structure indicates that the D3DRENDERSTATE_SHADEMODE render state should be updated to D3DSHADE_GOURAUD.

<img alt="Figure showing a command buffer with a D3DDP2OP_RENDERSTATE command and two D3DHAL_DP2RENDERSTATE structures" src="images/dp2rs.png"/>
<b>
     Additional Notes</b>

See the D3DTEXTURESTAGESTATETYPE, D3DTEXTUREOP, and D3DTEXTUREFILTER enumerated types in the DirectX SDK documentation for complete listings of all of the enabled render state types.

Some changes have been made to the D3DRENDERSTATETYPE enumerated type for DirectX 5.0 and beyond. D3DRENDERSTATE_BLENDENABLE has been removed completely although it is defined as D3DRENDERSTATE_ALPHABLENDENABLE in the <i>d3dtypes.h</i> header file. See D3DRENDERSTATE_COLORKEYENABLE for an explanation. The 128 integer values in the interval [128, 255] are reserved for texture coordinate wrap flags. These are constructed with the D3DWRAP_U and D3DWRAP_V macros. Using a flags word preserves forward compatibility with texture coordinates of higher dimension than 2D.

Multitexture macro ops and D3DRENDERSTATE_TEXTUREFACTOR override all of the per-texture stage blending controls (COLOR{OP,ARG1,ARG2} &amp; ALPHA{OP,ARG1,ARG2}).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d9types.h (include D3dhal.h) |