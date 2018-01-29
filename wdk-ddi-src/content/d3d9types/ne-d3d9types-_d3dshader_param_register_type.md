---
UID : NE:d3d9types._D3DSHADER_PARAM_REGISTER_TYPE
title : _D3DSHADER_PARAM_REGISTER_TYPE
author : windows-driver-content
description : Pixel and vertex shader operations specify register types in bits 28, 29, 30, 11, and 12 of destination and source parameter tokens.
old-location : display\shader_register_types.htm
old-project : display
ms.assetid : e1763ae1-5583-43fe-a342-3b9b5a92ef3f
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DSHADER_PARAM_REGISTER_TYPE, d3d9types/D3DSPR_INPUT, D3DSPR_COLOROUT, d3d9types/D3DSPR_LOOP, D3DSPR_MISCTYPE, d3d9types/D3DSPR_SAMPLER, D3DSPR_ADDR, D3DSPR_CONST2, d3d9types/D3DSPR_MISCTYPE, d3d9types/D3DSPR_CONSTBOOL, d3d9types/D3DSPR_CONST4, d3d9types/D3DSPR_FORCE_DWORD, D3DSPR_SAMPLER, D3DSPR_PREDICATE, d3d9types/D3DSPR_TEXCRDOUT, D3DSPR_RASTOUT, d3d9types/D3DSPR_CONSTINT, d3d9types/D3DSPR_OUTPUT, _D3DSHADER_PARAM_REGISTER_TYPE, D3DSPR_TEXTURE, d3d9types/D3DSPR_PREDICATE, D3DSPR_CONSTBOOL, display.shader_register_types, d3d9types/D3DSPR_COLOROUT, D3DSPR_ATTROUT, D3DSHADER_PARAM_REGISTER_TYPE enumeration [Display Devices], d3d9types/D3DSPR_TEMP, d3d9types/D3DSPR_DEPTHOUT, D3DSPR_TEMPFLOAT16, D3DSPR_FORCE_DWORD, D3DSPR_CONST4, D3DSPR_DEPTHOUT, d3d9types/D3DSHADER_PARAM_REGISTER_TYPE, d3d9types/ D3DSPR_CONST, d3d9types/D3DSPR_ADDR, d3d9types/D3DSPR_CONST3, UserModeDisplayDriver_Shader_1968e381-80d3-44f2-a02d-7625ba93f95a.xml, D3DSPR_CONSTINT, d3d9types/D3DSPR_CONST2, D3DSPR_CONST3, d3d9types/D3DSPR_TEMPFLOAT16, D3DSPR_TEXCRDOUT, d3d9types/D3DSPR_ATTROUT, D3DSPR_CONST, D3DSPR_OUTPUT, D3DSPR_TEMP, D3DSPR_INPUT, D3DSPR_LOOP, d3d9types/D3DSPR_RASTOUT, d3d9types/D3DSPR_TEXTURE, d3d9types/D3DSPR_LABEL, D3DSPR_LABEL
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3d9types.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3DSHADER_PARAM_REGISTER_TYPE
---

# _D3DSHADER_PARAM_REGISTER_TYPE Enumeration
Pixel and vertex shader operations specify register types in bits 28, 29, 30, 11, and 12 of destination and source parameter tokens. The following register types can be specified:

## Syntax
````
typedef enum _D3DSHADER_PARAM_REGISTER_TYPE { 
  D3DSPR_TEMP         = 0,
  D3DSPR_INPUT        = 1,
   D3DSPR_CONST       = 2,
  D3DSPR_ADDR         = 3,
  D3DSPR_TEXTURE      = 3,
  D3DSPR_RASTOUT      = 4,
  D3DSPR_ATTROUT      = 5,
  D3DSPR_TEXCRDOUT    = 6,
  D3DSPR_OUTPUT       = 6,
  D3DSPR_CONSTINT     = 7,
  D3DSPR_COLOROUT     = 8,
  D3DSPR_DEPTHOUT     = 9,
  D3DSPR_SAMPLER      = 10,
  D3DSPR_CONST2       = 11,
  D3DSPR_CONST3       = 12,
  D3DSPR_CONST4       = 13,
  D3DSPR_CONSTBOOL    = 14,
  D3DSPR_LOOP         = 15,
  D3DSPR_TEMPFLOAT16  = 16,
  D3DSPR_MISCTYPE     = 17,
  D3DSPR_LABEL        = 18,
  D3DSPR_PREDICATE    = 19,
  D3DSPR_FORCE_DWORD  = 0x7fffffff
} D3DSHADER_PARAM_REGISTER_TYPE;
````

## Constants

<table>

<tr>
<td>D3DSPR_ADDR</td>
<td>Address register (VS).</td>
</tr>

<tr>
<td>D3DSPR_ATTROUT</td>
<td>Attribute output register file.</td>
</tr>

<tr>
<td>D3DSPR_COLOROUT</td>
<td>Color output register file.</td>
</tr>

<tr>
<td>D3DSPR_CONST</td>
<td>For PS, constant register file  0 - 2047 (DEF instruction). For VS, reserved.</td>
</tr>

<tr>
<td>D3DSPR_CONST2</td>
<td>Constant register file  2048 - 4095.</td>
</tr>

<tr>
<td>D3DSPR_CONST3</td>
<td>Constant register file  4096 - 6143.</td>
</tr>

<tr>
<td>D3DSPR_CONST4</td>
<td>Constant register file  6144 - 8191.</td>
</tr>

<tr>
<td>D3DSPR_CONSTBOOL</td>
<td>Constant Boolean register file.</td>
</tr>

<tr>
<td>D3DSPR_CONSTINT</td>
<td>Constant integer vector register file.</td>
</tr>

<tr>
<td>D3DSPR_DEPTHOUT</td>
<td>Depth output register file.</td>
</tr>

<tr>
<td>D3DSPR_FORCE_DWORD</td>
<td>Force 32-bit size enumeration.</td>
</tr>

<tr>
<td>D3DSPR_INPUT</td>
<td>Input register file.</td>
</tr>

<tr>
<td>D3DSPR_LABEL</td>
<td>Label.</td>
</tr>

<tr>
<td>D3DSPR_LOOP</td>
<td>Loop counter register file.</td>
</tr>

<tr>
<td>D3DSPR_MISCTYPE</td>
<td>Miscellaneous (single) registers.</td>
</tr>

<tr>
<td>D3DSPR_OUTPUT</td>
<td>For &amp;lt; VS 3_0, texture coordinate output register file. For &amp;gt;/= VS 3_0, output register file. For PS, reserved.</td>
</tr>

<tr>
<td>D3DSPR_PREDICATE</td>
<td>Predicate register.</td>
</tr>

<tr>
<td>D3DSPR_RASTOUT</td>
<td>For VS, rasterizer output register file.</td>
</tr>

<tr>
<td>D3DSPR_SAMPLER</td>
<td>Sampler state register file.</td>
</tr>

<tr>
<td>D3DSPR_TEMP</td>
<td>Temporary register file.</td>
</tr>

<tr>
<td>D3DSPR_TEMPFLOAT16</td>
<td>16-bit float temp register file.</td>
</tr>

<tr>
<td>D3DSPR_TEXCRDOUT</td>
<td>Texture coordinate output register file.</td>
</tr>

<tr>
<td>D3DSPR_TEXTURE</td>
<td>Texture register file (PS).</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d9types.h |