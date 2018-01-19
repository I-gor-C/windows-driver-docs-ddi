---
UID : NE:d3dumddi._DXVAHDDDI_ROTATION
title : _DXVAHDDDI_ROTATION
author : windows-driver-content
description : Specifies the clockwise rotation of the display output surface.
old-location : display\dxvahdddi_rotation.htm
old-project : display
ms.assetid : 667f1c5e-c342-40b2-b215-2538669288cc
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXVAHDDDI_ROTATION, DXVAHDDDI_ROTATION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXVAHDDDI_ROTATION
req.alt-loc : D3dumddi.h
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
req.typenames : DXVAHDDDI_ROTATION
---

# _DXVAHDDDI_ROTATION Enumeration
Specifies the clockwise rotation of the display output surface.

## Syntax
````
typedef enum _DXVAHDDDI_ROTATION { 
  DXVAHDDDI_ROTATION_IDENTITY  = 0,
  DXVAHDDDI_ROTATION_90        = 1,
  DXVAHDDDI_ROTATION_180       = 2,
  DXVAHDDDI_ROTATION_270       = 3
} DXVAHDDDI_ROTATION;
````

## Constants

<table>

<tr>
<td>DXVAHDDDI_ROTATION_180</td>
<td>Indicates that rotation is 180 degrees clockwise—inverted landscape mode.</td>
</tr>

<tr>
<td>DXVAHDDDI_ROTATION_270</td>
<td>Indicates that rotation is 270 degrees clockwise—inverted portrait mode.</td>
</tr>

<tr>
<td>DXVAHDDDI_ROTATION_90</td>
<td>Indicates that rotation is 90 degrees clockwise—portrait mode.</td>
</tr>

<tr>
<td>DXVAHDDDI_ROTATION_IDENTITY</td>
<td>Indicates that rotation is 0 degrees—landscape mode.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |