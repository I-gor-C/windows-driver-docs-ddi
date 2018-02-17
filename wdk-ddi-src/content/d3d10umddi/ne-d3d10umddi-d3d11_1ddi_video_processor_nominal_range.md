---
UID: NE:d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE
title: D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE
author: windows-driver-content
description: Indicates the luminance range of YUV data.
old-location: display\d3d11_1ddi_video_processor_nominal_range.htm
old-project: display
ms.assetid: E8D77D49-9E7C-45B3-850C-1E814B44464B
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_0_255, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_UNDEFINED, DXVAHDDDI_NOMINAL_RANGE, display.d3d11_1ddi_video_processor_nominal_range, D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE, D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_16_235, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_16_235, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_0_255, d3d10umddi/D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE, D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE enumeration [Display Devices], DXVAHDDDI_NOMINAL_RANGE enumeration [Display Devices], D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_UNDEFINED
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
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
-	DXVAHDDDI_NOMINAL_RANGE
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE
---

# D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE Enumeration
Indicates the luminance range of YUV data.

## Syntax
````
typedef enum _DXVAHDDDI_NOMINAL_RANGE { 
  D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_UNDEFINED  = 0,
  D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_16_235     = 1,
  D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_0_255      = 2
} DXVAHDDDI_NOMINAL_RANGE;
````

## Constants

<table>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_0_255</td>
                    <td>The <i>full luminance range</i>, or <i>extended range</i>, of 0 to 255, inclusive [0, 255].</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_16_235</td>
                    <td>The <i>studio luminance range</i> of 16 to 235, inclusive [16, 235].</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_UNDEFINED</td>
                    <td>The driver default value, which is the <i>studio luminance range</i> of 16 to 235, inclusive [16, 235].</td>
                </tr>
</table>

    ## Remarks

        For more information on luminance range, see <a href="https://msdn.microsoft.com/D76FFB8C-CA42-446E-826F-52982B1849E5">YUV format ranges in Windows 8.1</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |