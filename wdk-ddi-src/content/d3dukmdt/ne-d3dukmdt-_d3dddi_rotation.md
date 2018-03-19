---
UID: NE:d3dukmdt._D3DDDI_ROTATION
title: "_D3DDDI_ROTATION"
author: windows-driver-content
description: The D3DDDI_ROTATION enumeration type contains values that identify the orientation of a resource.
old-location: display\d3dddi_rotation.htm
old-project: display
ms.assetid: c167b958-bd09-441e-9680-f193da5ad77f
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DDDI_ROTATION, D3DDDI_ROTATION enumeration [Display Devices], D3DDDI_ROTATION_180, D3DDDI_ROTATION_270, D3DDDI_ROTATION_90, D3DDDI_ROTATION_IDENTITY, D3D_other_Structs_0f55b4dd-2156-4590-a2c7-1daebcc16ba3.xml, _D3DDDI_ROTATION, d3dukmdt/D3DDDI_ROTATION, d3dukmdt/D3DDDI_ROTATION_180, d3dukmdt/D3DDDI_ROTATION_270, d3dukmdt/D3DDDI_ROTATION_90, d3dukmdt/D3DDDI_ROTATION_IDENTITY, display.d3dddi_rotation
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
-	d3dukmdt.h
api_name:
-	D3DDDI_ROTATION
product: Windows
targetos: Windows
req.typenames: D3DDDI_ROTATION
---

# _D3DDDI_ROTATION Enumeration
The D3DDDI_ROTATION enumeration type contains values that identify the orientation of a resource.

## Syntax
````
typedef enum _D3DDDI_ROTATION { 
  D3DDDI_ROTATION_IDENTITY  = 1,
  D3DDDI_ROTATION_90        = 2,
  D3DDDI_ROTATION_180       = 3,
  D3DDDI_ROTATION_270       = 4
} D3DDDI_ROTATION;
````

## Constants

<table>
            
                <tr>
                    <td>D3DDDI_ROTATION_IDENTITY</td>
                    <td>Indicates that the resource is not rotated.</td>
                </tr>
            
                <tr>
                    <td>D3DDDI_ROTATION_90</td>
                    <td>Indicates that the resource is rotated 90 degrees.</td>
                </tr>
            
                <tr>
                    <td>D3DDDI_ROTATION_180</td>
                    <td>Indicates that the resource is rotated 180 degrees.</td>
                </tr>
            
                <tr>
                    <td>D3DDDI_ROTATION_270</td>
                    <td>Indicates that the resource is rotated 270 degrees.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="..\d3dukmdt\ns-d3dukmdt-_d3dddiarg_createresource.md">D3DDDIARG_CREATERESOURCE</a>