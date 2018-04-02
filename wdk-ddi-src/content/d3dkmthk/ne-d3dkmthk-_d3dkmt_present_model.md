---
UID: NE:d3dkmthk._D3DKMT_PRESENT_MODEL
title: "_D3DKMT_PRESENT_MODEL"
author: windows-driver-content
description: The D3DKMT_PRESENT_MODEL enumeration type contains values that indicate the model for a present operation.
old-location: display\d3dkmt_present_model.htm
old-project: display
ms.assetid: 4663cc8e-ce69-4454-afff-03d4a8d82dfb
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_PM_REDIRECTED_BLT, D3DKMT_PM_REDIRECTED_COMPOSITION, D3DKMT_PM_REDIRECTED_FLIP, D3DKMT_PM_REDIRECTED_GDI, D3DKMT_PM_REDIRECTED_GDI_SYSMEM, D3DKMT_PM_REDIRECTED_VISTABLT, D3DKMT_PM_SCREENCAPTUREFENCE, D3DKMT_PM_UNINITIALIZED, D3DKMT_PRESENT_MODEL, D3DKMT_PRESENT_MODEL enumeration [Display Devices], OpenGL_Structs_b2e4c00b-9072-449d-84c0-7958200e7d9a.xml, _D3DKMT_PRESENT_MODEL, d3dkmthk/D3DKMT_PM_REDIRECTED_BLT, d3dkmthk/D3DKMT_PM_REDIRECTED_COMPOSITION, d3dkmthk/D3DKMT_PM_REDIRECTED_FLIP, d3dkmthk/D3DKMT_PM_REDIRECTED_GDI, d3dkmthk/D3DKMT_PM_REDIRECTED_GDI_SYSMEM, d3dkmthk/D3DKMT_PM_REDIRECTED_VISTABLT, d3dkmthk/D3DKMT_PM_SCREENCAPTUREFENCE, d3dkmthk/D3DKMT_PM_UNINITIALIZED, d3dkmthk/D3DKMT_PRESENT_MODEL, display.d3dkmt_present_model
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: D3DKMT_PRESENT_MODEL is supported beginning with the Windows 7 operating system.
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
-	d3dkmthk.h
api_name:
-	D3DKMT_PRESENT_MODEL
product: Windows
targetos: Windows
req.typenames: D3DKMT_PRESENT_MODEL
---

# _D3DKMT_PRESENT_MODEL Enumeration
The D3DKMT_PRESENT_MODEL enumeration type contains values that indicate the model for a present operation.

## Syntax
```
typedef enum _D3DKMT_PRESENT_MODEL {
  D3DKMT_PM_UNINITIALIZED           ,
  D3DKMT_PM_REDIRECTED_GDI          ,
  D3DKMT_PM_REDIRECTED_FLIP         ,
  D3DKMT_PM_REDIRECTED_BLT          ,
  D3DKMT_PM_REDIRECTED_VISTABLT     ,
  D3DKMT_PM_SCREENCAPTUREFENCE      ,
  D3DKMT_PM_REDIRECTED_GDI_SYSMEM   ,
  D3DKMT_PM_REDIRECTED_COMPOSITION  ,
  D3DKMT_PM_SURFACECOMPLETE
} D3DKMT_PRESENT_MODEL;
```

## Constants

<table>
            
                <tr>
                    <td>D3DKMT_PM_UNINITIALIZED</td>
                    <td>The present-operation model is not initialized.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_PM_REDIRECTED_GDI</td>
                    <td>The present-operation model is redirected GDI.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_PM_REDIRECTED_FLIP</td>
                    <td>The present-operation model is redirected flip.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_PM_REDIRECTED_BLT</td>
                    <td>The present-operation model is redirected bit-block transfer (bitblt).</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_PM_REDIRECTED_VISTABLT</td>
                    <td>The present-operation model is redirected Windows Vista bitblt.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_PM_SCREENCAPTUREFENCE</td>
                    <td>The present-operation model is screen capture through a fence.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_PM_REDIRECTED_GDI_SYSMEM</td>
                    <td>The present-operation model is redirected system GDI.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_PM_REDIRECTED_COMPOSITION</td>
                    <td>The present-operation model is redirected composition swap chain presentation. This type of presentation is used for XAML-based apps.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_PM_SURFACECOMPLETE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3DKMT_PRESENT_MODEL is supported beginning with the Windows 7 operating system. D3DKMT_PRESENT_MODEL is supported beginning with the Windows 7 operating system. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548188">D3DKMT_PRESENTHISTORYTOKEN</a>