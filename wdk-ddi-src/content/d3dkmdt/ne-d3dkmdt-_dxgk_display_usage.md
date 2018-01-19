---
UID : NE:d3dkmdt._DXGK_DISPLAY_USAGE
title : _DXGK_DISPLAY_USAGE
author : windows-driver-content
description : Enum used to specify the display type being used.
old-location : display\dxgk_display_usage.htm
old-project : display
ms.assetid : 07B51679-4E9B-4360-AA4A-D5BD9BADB4FC
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_DISPLAY_USAGE, *PDXGK_DISPLAY_USAGE, DXGK_DISPLAY_USAGE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dkmdt.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_DISPLAY_USAGE
req.alt-loc : d3dkmdt.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PDXGK_DISPLAY_USAGE, DXGK_DISPLAY_USAGE"
---

# _DXGK_DISPLAY_USAGE Enumeration
Enum used to specify the display type being used.

## Syntax
````
typedef enum _DXGK_DISPLAY_USAGE { 
  DXGK_DU_INVALID  = 0,
  DXGK_DU_GENERIC,
  DXGK_DU_AR,
  DXGK_DU_VR
} DXGK_DISPLAY_USAGE, *PDXGK_DISPLAY_USAGE;
````

## Constants

<table>

<tr>
<td>DXGK_DU_AR</td>
<td>A head mounted augmented reality display.</td>
</tr>

<tr>
<td>DXGK_DU_GENERIC</td>
<td>Generic display type.</td>
</tr>

<tr>
<td>DXGK_DU_INVALID</td>
<td>Invalid type.</td>
</tr>

<tr>
<td>DXGK_DU_VR</td>
<td>A head mounted virtual reality display.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmdt.h |