---
UID: NS:d3dumddi._D3DDDIARG_SETMATERIAL
title: "_D3DDDIARG_SETMATERIAL"
author: windows-driver-content
description: The D3DDDIARG_SETMATERIAL structure describes the material properties that are used for rendering.
old-location: display\d3dddiarg_setmaterial.htm
old-project: display
ms.assetid: 66c35c60-9f6c-44d7-b6d5-9d50a3e33c2e
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DDDIARG_SETMATERIAL, D3DDDIARG_SETMATERIAL structure [Display Devices], UMDisplayDriver_param_Structs_5a3ecda9-5303-46f4-b7a2-42243e3a66d1.xml, _D3DDDIARG_SETMATERIAL, d3dumddi/D3DDDIARG_SETMATERIAL, display.d3dddiarg_setmaterial
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	d3dumddi.h
api_name:
-	D3DDDIARG_SETMATERIAL
product: Windows
targetos: Windows
req.typenames: D3DDDIARG_SETMATERIAL
---

# _D3DDDIARG_SETMATERIAL structure
The D3DDDIARG_SETMATERIAL structure describes the material properties that are used for rendering.

## Syntax
````
typedef struct _D3DDDIARG_SETMATERIAL {
  D3DCOLORVALUE Diffuse;
  D3DCOLORVALUE Ambient;
  D3DCOLORVALUE Specular;
  D3DCOLORVALUE Emissive;
  FLOAT         Power;
} D3DDDIARG_SETMATERIAL;
````

## Members


`Diffuse`

[in] A D3DCOLORVALUE structure that indicates the diffuse color of the material. For more information about D3DCOLORVALUE, see the Microsoft Windows SDK documentation.

`Ambient`

[in] A D3DCOLORVALUE structure that indicates the ambient color of the material.

`Specular`

[in] A D3DCOLORVALUE structure that indicates the specular color of the material.

`Emissive`

[in] A D3DCOLORVALUE structure that indicates the emissive color of the material.

`Power`

[in] A FLOAT value that indicates the sharpness of specular highlights. To turn off specular highlights for a material, set <b>Power</b> to 0 (setting <b>Specular</b> to 0 is not enough).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_setmaterial.md">SetMaterial</a>