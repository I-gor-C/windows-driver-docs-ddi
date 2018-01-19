---
UID : NE:d3d9types._D3DRENDERSTATETYPE
title : _D3DRENDERSTATETYPE
author : windows-driver-content
description : The D3DRENDERSTATETYPE enumerated type lists a variety of attributes, or render states.
old-location : display\d3drenderstatetype.htm
old-project : display
ms.assetid : 82978b22-1538-4da0-bcf2-c4c52d2e3429
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DRENDERSTATETYPE, D3DRENDERSTATETYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3d9types.h
req.include-header : D3dhal.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DRENDERSTATETYPE
req.alt-loc : d3d9types.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : D3DRENDERSTATETYPE
---

# _D3DRENDERSTATETYPE Enumeration
The D3DRENDERSTATETYPE enumerated type lists a variety of attributes, or render states. 
  The enumerators of D3DRENDERSTATETYPE that are used exclusively by drivers can specify either rendering information or a texture attribute. The following render states are used by display drivers:

## Syntax
````
enum  {
  D3DRENDERSTATE_EVICTMANAGEDTEXTURES  = 61, 
  D3DRENDERSTATE_SCENECAPTURE          = 62, 
  D3DRS_DELETERTPATCH                  = 169, 
  D3DRS_MAXVERTEXSHADERINST            = 196, 
  D3DRS_MAXPIXELSHADERINST             = 197 

};
````

## Constants

<table>
</table>

## Remarks

The driver uses these render states when it performs graphics rendering. Only render states that are specific to drivers are included in the Windows Driver Kit (WDK) documentation. The render states accessible to DirectX applications are included in the DirectX SDK documentation. These application-level render states include such characteristics as whether alpha blending is enabled, whether dithering is enabled, whether Direct3D lighting is used, and the type of shading to be used. 

To update a particular render state, Direct3D stores information about the render state, and then calls the driver's <a href="..\d3dhal\nc-d3dhal-lpd3dhal_drawprimitives2cb.md">D3dDrawPrimitives2</a> callback routine. The information provided to the driver enables it to:

Determine that it should update one or more render states.

Identify which render states to update, and what the new render state values should be.

Note that for certain render states to be honored, the driver must have previously set capability flags in the relevant member of the D3DPRIMCAPS structure.

In order to indicate a specific render state update, Direct3D inserts a <a href="..\d3dhal\ns-d3dhal-_d3dhal_dp2command.md">D3DHAL_DP2COMMAND</a> structure into the command buffer, setting the <b>bCommand</b> member of this structure to D3DDP2OP_RENDERSTATE (see the description for D3DDP2OP_RENDERSTATE in <a href="..\d3dhal\ne-d3dhal-_d3dhal_dp2operation.md">D3DHAL_DP2OPERATION</a>), and setting the <b>wStateCount</b> member of the same structure to the number of render states to be updated.

Immediately following the <a href="..\d3dhal\ns-d3dhal-_d3dhal_dp2command.md">D3DHAL_DP2COMMAND</a> structure, Direct3D inserts one <a href="..\d3dhal\ns-d3dhal-_d3dhal_dp2renderstate.md">D3DHAL_DP2RENDERSTATE</a> structure into the command buffer for each render state to be updated. The <b>RenderState</b> member of this structure identifies the render state to be changed; the new value of this render state is specified in either the <b>dwState</b> member (for DWORD values) or the <b>fState</b> member (for D3DVALUE values).

The following figure shows a portion of the command buffer containing a D3DDP2OP_RENDERSTATE command and two D3DHAL_DP2RENDERSTATE structures. The first of the three structures indicates that two render states are to be updated. The second structure indicates that the D3DRENDERSTATE_FILLMODE render state is to be changed to D3DFILL_SOLID. The third structure indicates that the D3DRENDERSTATE_SHADEMODE render state should be updated to D3DSHADE_GOURAUD.

<b>
     Additional Notes</b>

See the D3DTEXTURESTAGESTATETYPE, D3DTEXTUREOP, and D3DTEXTUREFILTER enumerated types in the DirectX SDK documentation for complete listings of all of the enabled render state types.

Some changes have been made to the D3DRENDERSTATETYPE enumerated type for DirectX 5.0 and beyond. D3DRENDERSTATE_BLENDENABLE has been removed completely although it is defined as D3DRENDERSTATE_ALPHABLENDENABLE in the <i>d3dtypes.h</i> header file. See D3DRENDERSTATE_COLORKEYENABLE for an explanation. The 128 integer values in the interval [128, 255] are reserved for texture coordinate wrap flags. These are constructed with the D3DWRAP_U and D3DWRAP_V macros. Using a flags word preserves forward compatibility with texture coordinates of higher dimension than 2D.

Multitexture macro ops and D3DRENDERSTATE_TEXTUREFACTOR override all of the per-texture stage blending controls (COLOR{OP,ARG1,ARG2} &amp; ALPHA{OP,ARG1,ARG2}).</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d9types.h (include D3dhal.h) |