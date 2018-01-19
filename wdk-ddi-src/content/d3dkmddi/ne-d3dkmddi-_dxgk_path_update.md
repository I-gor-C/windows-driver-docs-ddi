---
UID : NE:d3dkmddi._DXGK_PATH_UPDATE
title : _DXGK_PATH_UPDATE
author : windows-driver-content
description : Enum which indicates how this path has been modified since the previous successful call to SetTimingsFromVidPn.
old-location : display\dxgk_path_update.htm
old-project : display
ms.assetid : DCBBFBF7-73B2-4298-BB87-83E1C6D76BD0
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_PATH_UPDATE, DXGK_PATH_UPDATE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dkmddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_PATH_UPDATE
req.alt-loc : d3dkmddi.h
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
req.typenames : DXGK_PATH_UPDATE
---

# _DXGK_PATH_UPDATE Enumeration
Enum which indicates how this path has been modified since the previous successful call to SetTimingsFromVidPn.

## Syntax
````
typedef enum _DXGK_PATH_UPDATE { 
  DXGK_PATH_UPDATE_UNMODIFED  = 0,
  DXGK_PATH_UPDATE_ADDED      = 1,
  DXGK_PATH_UPDATE_MODIFIED   = 2,
  DXGK_PATH_UPDATE_REMOVED    = 3
} DXGK_PATH_UPDATE;
````

## Constants

<table>

<tr>
<td>DXGK_PATH_UPDATE_ADDED</td>
<td>Indicates that this path is new so the driver will have to fully comprehend the description of what is required.  Since there is no allocation from which to scan out, the driver must scan out black until the OS associates one or more planes to be scanned out.</td>
</tr>

<tr>
<td>DXGK_PATH_UPDATE_MODIFIED</td>
<td>Indicates that this path has been changed since the last call to SetTimingsFromVidPn.  The driver will have to interrogate the VidPn and check the other path info fields in order to understand what has changed.  The OS will have removed all pixel planes prior to making this call so the driver must scan out black until the OS associates one or more planes to be scanned out.</td>
</tr>

<tr>
<td>DXGK_PATH_UPDATE_REMOVED</td>
<td>Indicates that this path was present in the previous VidPn but has been removed. The driver should be able to optimize the removal without interrogating VidPn to see that the path has been removed.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h |