---
UID: NE:d3d10umddi.D3DWDDM2_0DDI_CONTEXTTYPE_FLAG
title: D3DWDDM2_0DDI_CONTEXTTYPE_FLAG
author: windows-driver-content
description: D3DWDDM2_0DDI_CONTEXTTYPE_FLAG describes the type of context being created for interacting with JPEG hardware.
old-location: display\d3dwddm2_0ddi_contexttype_flag.htm
old-project: display
ms.assetid: F767C051-637A-4912-80B0-36C4DF7E46DD
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: d3d10umddi/D3DWDDM2_0DDI_CONTEXTTYPE_COMPUTE, D3DWDDM2_0DDI_CONTEXTTYPE_COMPUTE, d3d10umddi/D3DWDDM2_0DDI_CONTEXTTYPE_3D, D3DWDDM2_0DDI_CONTEXTTYPE_ALL, d3d10umddi/D3DWDDM2_0DDI_CONTEXTTYPE_VIDEO, d3d10umddi/D3DWDDM2_0DDI_CONTEXTTYPE_COPY, d3d10umddi/D3DWDDM2_0DDI_CONTEXTTYPE_IMAGE, display.d3dwddm2_0ddi_contexttype_flag, D3DWDDM2_0DDI_CONTEXTTYPE_IMAGE, D3DWDDM2_0DDI_CONTEXTTYPE_COPY, D3DWDDM2_0DDI_CONTEXTTYPE_FLAG enumeration [Display Devices], d3d10umddi/D3DWDDM2_0DDI_CONTEXTTYPE_ALL, D3DWDDM2_0DDI_CONTEXTTYPE_3D, D3DWDDM2_0DDI_CONTEXTTYPE_FLAG, D3DWDDM2_0DDI_CONTEXTTYPE_VIDEO, d3d10umddi/D3DWDDM2_0DDI_CONTEXTTYPE_FLAG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	D3d10umddi.h
apiname:
-	D3DWDDM2_0DDI_CONTEXTTYPE_FLAG
product: Windows
targetos: Windows
req.typenames: D3DWDDM2_0DDI_CONTEXTTYPE_FLAG
---

# D3DWDDM2_0DDI_CONTEXTTYPE_FLAG Enumeration
<b>D3DWDDM2_0DDI_CONTEXTTYPE_FLAG</b> describes the type of context being created for interacting with JPEG hardware.

## Syntax
````
typedef enum _D3DWDDM2_0DDI_CONTEXTTYPE_FLAG { 
  D3DWDDM2_0DDI_CONTEXTTYPE_ALL      = 0x00000000,
  D3DWDDM2_0DDI_CONTEXTTYPE_3D       = 0x00000001,
  D3DWDDM2_0DDI_CONTEXTTYPE_COMPUTE  = 0x00000002,
  D3DWDDM2_0DDI_CONTEXTTYPE_COPY     = 0x00000004,
  D3DWDDM2_0DDI_CONTEXTTYPE_VIDEO    = 0x00000008,
  D3DWDDM2_0DDI_CONTEXTTYPE_IMAGE    = 0x00000010
} D3DWDDM2_0DDI_CONTEXTTYPE_FLAG;
````

## Constants

<table>
            
                <tr>
                    <td>D3DWDDM2_0DDI_CONTEXTTYPE_3D</td>
                    <td>Indicates that a JPEG 3D context should be created.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_CONTEXTTYPE_ALL</td>
                    <td>Indicates that all JPEG contexts should be created.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_CONTEXTTYPE_COMPUTE</td>
                    <td>Indicates that a JPEG compute context should be created.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_CONTEXTTYPE_COPY</td>
                    <td>Indicates that  a JPEG copy context should be created.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_CONTEXTTYPE_VIDEO</td>
                    <td>Indicates that a JPEG video context should be created.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |