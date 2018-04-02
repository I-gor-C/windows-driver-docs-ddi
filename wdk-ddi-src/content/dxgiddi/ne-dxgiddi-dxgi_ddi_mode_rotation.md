---
UID: NE:dxgiddi.DXGI_DDI_MODE_ROTATION
title: DXGI_DDI_MODE_ROTATION
author: windows-driver-content
description: The DXGI_DDI_MODE_ROTATION enumeration type contains values that identify the orientation of the display.
old-location: display\dxgi_ddi_mode_rotation.htm
old-project: display
ms.assetid: 8cc413c4-e4fe-449b-a66a-c79da01ad3be
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGI_DDI_MODE_ROTATION, DXGI_DDI_MODE_ROTATION enumeration [Display Devices], DXGI_DDI_MODE_ROTATION_IDENTITY, DXGI_DDI_MODE_ROTATION_ROTATE180, DXGI_DDI_MODE_ROTATION_ROTATE270, DXGI_DDI_MODE_ROTATION_ROTATE90, DXGI_DDI_MODE_ROTATION_UNSPECIFIED, UMDisplayDriver_Dx10param_Structs_61b842eb-a4b4-4d86-95b8-eca448b35b5e.xml, display.dxgi_ddi_mode_rotation, dxgiddi/DXGI_DDI_MODE_ROTATION, dxgiddi/DXGI_DDI_MODE_ROTATION_IDENTITY, dxgiddi/DXGI_DDI_MODE_ROTATION_ROTATE180, dxgiddi/DXGI_DDI_MODE_ROTATION_ROTATE270, dxgiddi/DXGI_DDI_MODE_ROTATION_ROTATE90, dxgiddi/DXGI_DDI_MODE_ROTATION_UNSPECIFIED
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
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
-	dxgiddi.h
api_name:
-	DXGI_DDI_MODE_ROTATION
product: Windows
targetos: Windows
req.typenames: DXGI_DDI_MODE_ROTATION
---

# DXGI_DDI_MODE_ROTATION Enumeration
The DXGI_DDI_MODE_ROTATION enumeration type contains values that identify the orientation of the display.

## Syntax
```
typedef enum DXGI_DDI_MODE_ROTATION {
  DXGI_DDI_MODE_ROTATION_UNSPECIFIED  ,
  DXGI_DDI_MODE_ROTATION_IDENTITY     ,
  DXGI_DDI_MODE_ROTATION_ROTATE90     ,
  DXGI_DDI_MODE_ROTATION_ROTATE180    ,
  DXGI_DDI_MODE_ROTATION_ROTATE270
} ;
```

## Constants

<table>
            
                <tr>
                    <td>DXGI_DDI_MODE_ROTATION_UNSPECIFIED</td>
                    <td>A DXGI_DDI_MODE_ROTATION-typed variable has not yet been assigned a meaningful value.</td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MODE_ROTATION_IDENTITY</td>
                    <td>The display is not rotated.</td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MODE_ROTATION_ROTATE90</td>
                    <td>The display is rotated 90 degrees.</td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MODE_ROTATION_ROTATE180</td>
                    <td>The display is rotated 180 degrees.</td>
                </tr>
            
                <tr>
                    <td>DXGI_DDI_MODE_ROTATION_ROTATE270</td>
                    <td>The display is rotated 270 degrees.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | dxgiddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557499">DXGI_DDI_MODE_DESC</a>