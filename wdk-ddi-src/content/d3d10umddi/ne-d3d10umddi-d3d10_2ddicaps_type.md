---
UID: NE:d3d10umddi.D3D10_2DDICAPS_TYPE
title: D3D10_2DDICAPS_TYPE
author: windows-driver-content
description: The D3D10_2DDICAPS_TYPE enumeration type contains values that identify the type of capability information that is retrieved from a call to the driver's GetCaps(D3D10_2) function.
old-location: display\d3d10_2ddicaps_type.htm
old-project: display
ms.assetid: 2ca906d4-6d09-4624-a985-a47794acc959
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D10_2DDICAPS_TYPE, D3D10_2DDICAPS_TYPE enumeration [Display Devices], D3D11DDICAPS_3DPIPELINESUPPORT, D3D11DDICAPS_SHADER, D3D11DDICAPS_THREADING, D3D11_1DDICAPS_ARCHITECTURE_INFO, D3D11_1DDICAPS_D3D11_OPTIONS, D3D11_1DDICAPS_SHADER_MIN_PRECISION_SUPPORT, D3DWDDM1_3DDICAPS_D3D11_OPTIONS1, D3DWDDM1_3DDICAPS_MARKER, UMDisplayDriver_Dx11param_Structs_cde2c336-2e65-43c4-970c-83b83765df38.xml, d3d10umddi/D3D10_2DDICAPS_TYPE, d3d10umddi/D3D11DDICAPS_3DPIPELINESUPPORT, d3d10umddi/D3D11DDICAPS_SHADER, d3d10umddi/D3D11DDICAPS_THREADING, d3d10umddi/D3D11_1DDICAPS_ARCHITECTURE_INFO, d3d10umddi/D3D11_1DDICAPS_D3D11_OPTIONS, d3d10umddi/D3D11_1DDICAPS_SHADER_MIN_PRECISION_SUPPORT, d3d10umddi/D3DWDDM1_3DDICAPS_D3D11_OPTIONS1, d3d10umddi/D3DWDDM1_3DDICAPS_MARKER, display.d3d10_2ddicaps_type
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D10_2DDICAPS_TYPE is supported beginning with the Windows 7 operating system.
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
-	d3d10umddi.h
api_name:
-	D3D10_2DDICAPS_TYPE
product:
- Windows
targetos: Windows
req.typenames: D3D10_2DDICAPS_TYPE
---

# D3D10_2DDICAPS_TYPE Enumeration
The D3D10_2DDICAPS_TYPE enumeration type contains values that identify the type of capability information that is retrieved from a call to the driver's <a href="https://msdn.microsoft.com/83cd5f34-5f12-4ead-ad33-366fc3c6e804">GetCaps(D3D10_2)</a> function.

## Syntax
```
typedef enum D3D10_2DDICAPS_TYPE {
  D3D11DDICAPS_THREADING                       ,
  D3D11DDICAPS_SHADER                          ,
  D3D11DDICAPS_3DPIPELINESUPPORT               ,
  D3D11_1DDICAPS_D3D11_OPTIONS                 ,
  D3D11_1DDICAPS_ARCHITECTURE_INFO             ,
  D3D11_1DDICAPS_SHADER_MIN_PRECISION_SUPPORT  ,
  D3DWDDM1_3DDICAPS_D3D11_OPTIONS1             ,
  D3DWDDM1_3DDICAPS_MARKER                     ,
  D3DWDDM2_0DDICAPS_D3D11_OPTIONS2             ,
  D3DWDDM2_0DDICAPS_MEMORY_ARCHITECTURE        ,
  D3DWDDM2_0DDICAPS_TEXTURE_LAYOUT_SETS        ,
  D3DWDDM2_0DDICAPS_TEXTURE_LAYOUT             ,
  D3DWDDM2_0DDICAPS_SWIZZLE_PATTERN            ,
  D3DWDDM2_0DDICAPS_D3D11_OPTIONS3             ,
  D3DWDDM2_0DDICAPS_GPUVA_CAPS                 ,
  D3DWDDM2_0DDICAPS_TEXTURE_LAYOUT1            ,
  D3DWDDM2_2DDICAPS_SHADERCACHE                ,
  D3DWDDM2_2DDICAPS_TEXTURE_LAYOUT             ,
  D3DWDDM2_2DDICAPS_SWIZZLE_PATTERN
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3D11DDICAPS_THREADING</td>
                    <td>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a> structure that describes the threading capabilities that the driver supports.</td>
                </tr>
            
                <tr>
                    <td>D3D11DDICAPS_SHADER</td>
                    <td>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff542153">D3D11DDI_SHADER_CAPS</a> structure that describes the shader capabilities that the driver supports.</td>
                </tr>
            
                <tr>
                    <td>D3D11DDICAPS_3DPIPELINESUPPORT</td>
                    <td>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff542134">D3D11DDI_3DPIPELINESUPPORT_CAPS</a> structure that describes the pipeline capabilities that the driver supports.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDICAPS_D3D11_OPTIONS</td>
                    <td>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406442">D3D11_1DDI_D3D11_OPTIONS_DATA</a>  structure that specifies options to provide data to the user-mode driver.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDICAPS_ARCHITECTURE_INFO</td>
                    <td>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451150">D3DDDICAPS_ARCHITECTURE_INFO</a> structure that describes information about Direct3D 11.1 adapter architecture.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDICAPS_SHADER_MIN_PRECISION_SUPPORT</td>
                    <td>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451154">D3DDDICAPS_SHADER_MIN_PRECISION_SUPPORT</a> structure that describes the precision support options for shaders in the user-mode display driver.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM1_3DDICAPS_D3D11_OPTIONS1</td>
                    <td>The driver retrieves a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn475744">D3DWDDM1_3DDI_D3D11_OPTIONS_DATA1</a> structure that describes the tiled resource support options in the user-mode display driver.

Supported starting with Windows 8. Used by WDDM 1.3 and later drivers.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM1_3DDICAPS_MARKER</td>
                    <td>Supported starting with Windows 8. Used by WDDM 1.3 and later drivers.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDICAPS_D3D11_OPTIONS2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDICAPS_MEMORY_ARCHITECTURE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDICAPS_TEXTURE_LAYOUT_SETS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDICAPS_TEXTURE_LAYOUT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDICAPS_SWIZZLE_PATTERN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDICAPS_D3D11_OPTIONS3</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDICAPS_GPUVA_CAPS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDICAPS_TEXTURE_LAYOUT1</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_2DDICAPS_SHADERCACHE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_2DDICAPS_TEXTURE_LAYOUT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_2DDICAPS_SWIZZLE_PATTERN</td>
                    <td></td>
                </tr>
</table>

## Remarks

To allow a driver to unify capability concepts, the values in the D3D10_2DDICAPS_TYPE enumeration are set up so they do not overlap with the values in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a> enumeration.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3D10_2DDICAPS_TYPE is supported beginning with the Windows 7 operating system. D3D10_2DDICAPS_TYPE is supported beginning with the Windows 7 operating system. |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542134">D3D11DDI_3DPIPELINESUPPORT_CAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542153">D3D11DDI_SHADER_CAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542163">D3D11DDI_THREADING_CAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406442">D3D11_1DDI_D3D11_OPTIONS_DATA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451154">D3DDDICAPS_SHADER_MIN_PRECISION_SUPPORT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn475744">D3DWDDM1_3DDI_D3D11_OPTIONS_DATA1</a>