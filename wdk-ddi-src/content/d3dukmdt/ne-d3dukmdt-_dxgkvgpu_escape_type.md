---
UID: NE:d3dukmdt._DXGKVGPU_ESCAPE_TYPE
title: "_DXGKVGPU_ESCAPE_TYPE"
author: windows-driver-content
description: An enum that holds information about the escape type.
old-location: display\dxgkvgpu_escape_type.htm
old-project: display
ms.assetid: F7081B59-DB24-4BFE-B1BD-3BE228804AB2
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DXGKVGPU_ESCAPE_TYPE_READ_PCI_CONFIG, DXGKVGPU_ESCAPE_TYPE, _DXGKVGPU_ESCAPE_TYPE, d3dukmdt/DXGKVGPU_ESCAPE_TYPE_GET_VGPU_TYPE, DXGKVGPU_ESCAPE_TYPE enumeration [Display Devices], display.dxgkvgpu_escape_type, d3dukmdt/DXGKVGPU_ESCAPE_TYPE_READ_PCI_CONFIG, DXGKVGPU_ESCAPE_TYPE_GET_VGPU_TYPE, d3dukmdt/DXGKVGPU_ESCAPE_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dukmdt.h
req.include-header: 
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dukmdt.h
apiname:
-	DXGKVGPU_ESCAPE_TYPE
product: Windows
targetos: Windows
req.typenames: DXGKVGPU_ESCAPE_TYPE
---

# _DXGKVGPU_ESCAPE_TYPE Enumeration
An enum that holds information about the escape type.

## Syntax
````
typedef enum _DXGKVGPU_ESCAPE_TYPE { 
  DXGKVGPU_ESCAPE_TYPE_READ_PCI_CONFIG  = 0,
  DXGKVGPU_ESCAPE_TYPE_GET_VGPU_TYPE    = 4
} DXGKVGPU_ESCAPE_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>DXGKVGPU_ESCAPE_TYPE_GET_VGPU_TYPE</td>
                    <td>Indicates the VGPU type of the escape.</td>
                </tr>
            
                <tr>
                    <td>DXGKVGPU_ESCAPE_TYPE_INITIALIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGKVGPU_ESCAPE_TYPE_POWERTRANSITIONCOMPLETE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGKVGPU_ESCAPE_TYPE_READ_PCI_CONFIG</td>
                    <td>Indicates the PCI config of the escape type.</td>
                </tr>
            
                <tr>
                    <td>DXGKVGPU_ESCAPE_TYPE_RELEASE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DXGKVGPU_ESCAPE_TYPE_WRITE_PCI_CONFIG</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dukmdt.h |