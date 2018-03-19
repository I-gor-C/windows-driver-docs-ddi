---
UID: NE:d3dumddi._DXVAHDDDI_DEVICE_USAGE
title: "_DXVAHDDDI_DEVICE_USAGE"
author: windows-driver-content
description: The DXVAHDDDI_DEVICE_USAGE enumeration contains values that identify how the decode device plays video.
old-location: display\dxvahdddi_device_usage.htm
old-project: display
ms.assetid: 9a2e74fa-ee02-46f9-a51e-b2ffcdf7617a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXVA2_Structs_37d96cb2-48a3-4538-9225-e63bfe0b5b5f.xml, DXVAHDDDI_DEVICE_USAGE, DXVAHDDDI_DEVICE_USAGE enumeration [Display Devices], DXVAHDDDI_DEVICE_USAGE_OPTIMAL_QUALITY, DXVAHDDDI_DEVICE_USAGE_OPTIMAL_SPEED, DXVAHDDDI_DEVICE_USAGE_PLAYBACK_NORMAL, _DXVAHDDDI_DEVICE_USAGE, d3dumddi/DXVAHDDDI_DEVICE_USAGE, d3dumddi/DXVAHDDDI_DEVICE_USAGE_OPTIMAL_QUALITY, d3dumddi/DXVAHDDDI_DEVICE_USAGE_OPTIMAL_SPEED, d3dumddi/DXVAHDDDI_DEVICE_USAGE_PLAYBACK_NORMAL, display.dxvahdddi_device_usage
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_DEVICE_USAGE is supported beginning with the Windows 7 operating system.
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
-	DXVAHDDDI_DEVICE_USAGE
product: Windows
targetos: Windows
req.typenames: DXVAHDDDI_DEVICE_USAGE
---

# _DXVAHDDDI_DEVICE_USAGE Enumeration
The DXVAHDDDI_DEVICE_USAGE enumeration contains values that identify how the decode device plays video.

## Syntax
````
typedef enum _DXVAHDDDI_DEVICE_USAGE { 
  DXVAHDDDI_DEVICE_USAGE_PLAYBACK_NORMAL  = 0,
  DXVAHDDDI_DEVICE_USAGE_OPTIMAL_SPEED    = 1,
  DXVAHDDDI_DEVICE_USAGE_OPTIMAL_QUALITY  = 2
} DXVAHDDDI_DEVICE_USAGE;
````

## Constants

<table>
            
                <tr>
                    <td>DXVAHDDDI_DEVICE_USAGE_PLAYBACK_NORMAL</td>
                    <td>A value that specifies that the device plays video at normal speed.</td>
                </tr>
            
                <tr>
                    <td>DXVAHDDDI_DEVICE_USAGE_OPTIMAL_SPEED</td>
                    <td>A value that specifies that the device plays video at optimal speed.</td>
                </tr>
            
                <tr>
                    <td>DXVAHDDDI_DEVICE_USAGE_OPTIMAL_QUALITY</td>
                    <td>A value that specifies that the device plays video at optimal quality.</td>
                </tr>
</table>

## Remarks

A DXVAHDDDI_DEVICE_USAGE-typed value is specified in the <b>Usage</b> member of a <a href="..\d3dumddi\ns-d3dumddi-_dxvahdddi_device_desc.md">DXVAHDDDI_DEVICE_DESC</a> structure to help describe a decode device.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | DXVAHDDDI_DEVICE_USAGE is supported beginning with the Windows 7 operating system. DXVAHDDDI_DEVICE_USAGE is supported beginning with the Windows 7 operating system. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_dxvahdddi_device_desc.md">DXVAHDDDI_DEVICE_DESC</a>