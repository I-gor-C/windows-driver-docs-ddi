---
UID : NE:d3dukmdt._DXGK_MIRACAST_CHUNK_TYPE
title : "_DXGK_MIRACAST_CHUNK_TYPE"
author : windows-driver-content
description : Specifies the types of wireless display (Miracast) chunk info that is to be processed.
old-location : display\dxgk_miracast_chunk_type.htm
old-project : display
ms.assetid : 6C44EFD1-9366-4119-945E-688176D9F5D5
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : DXGK_MIRACAST_CHUNK_TYPE_FRAME_DROPPED, DXGK_MIRACAST_CHUNK_TYPE enumeration [Display Devices], _DXGK_MIRACAST_CHUNK_TYPE, DXGK_MIRACAST_CHUNK_TYPE, DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1, d3dukmdt/DXGK_MIRACAST_CHUNK_TYPE_UNKNOWN, DXGK_MIRACAST_CHUNK_TYPE_FRAME_START, d3dukmdt/DXGK_MIRACAST_CHUNK_TYPE, d3dukmdt/DXGK_MIRACAST_CHUNK_TYPE_FRAME_DROPPED, DXGK_MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE, d3dukmdt/DXGK_MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE, DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2, DXGK_MIRACAST_CHUNK_TYPE_UNKNOWN, d3dukmdt/DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2, d3dukmdt/DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1, d3dukmdt/DXGK_MIRACAST_CHUNK_TYPE_FRAME_START, DXGK_MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE, d3dukmdt/DXGK_MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE, display.dxgk_miracast_chunk_type
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dukmdt.h
req.include-header : D3dukmdt.h, D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 8.1
req.target-min-winversvr : Windows Server 2012 R2
req.kmdf-ver : 
req.umdf-ver : 
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGK_MIRACAST_CHUNK_TYPE
---

# _DXGK_MIRACAST_CHUNK_TYPE Enumeration
Specifies the types of wireless display (Miracast) chunk info that is to be processed.

## Syntax
````
typedef enum _DXGK_MIRACAST_CHUNK_TYPE { 
  DXGK_MIRACAST_CHUNK_TYPE_UNKNOWN                  = 0,
  DXGK_MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE   = 1,
  DXGK_MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE          = 2,
  DXGK_MIRACAST_CHUNK_TYPE_FRAME_START              = 3,
  DXGK_MIRACAST_CHUNK_TYPE_FRAME_DROPPED            = 4,
  DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1  = 0x80000000,
  DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2  = 0x80000001
} DXGK_MIRACAST_CHUNK_TYPE;
````

## Constants

<table>

<tr>
<td>DXGK_MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE</td>
<td>Color conversion has completed on the chunk.</td>
</tr>

<tr>
<td>DXGK_MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE</td>
<td>Encoding has completed on the chunk.</td>
</tr>

<tr>
<td>DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1</td>
<td>Encoding is driver-defined, of type 1.</td>
</tr>

<tr>
<td>DXGK_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_2</td>
<td>Encoding is driver-defined, of type 2.</td>
</tr>

<tr>
<td>DXGK_MIRACAST_CHUNK_TYPE_FRAME_DROPPED</td>
<td>The chunk is in a dropped Wi-Fi frame.</td>
</tr>

<tr>
<td>DXGK_MIRACAST_CHUNK_TYPE_FRAME_START</td>
<td>The chunk is at the start of the Wi-Fi frame.</td>
</tr>

<tr>
<td>DXGK_MIRACAST_CHUNK_TYPE_UNKNOWN</td>
<td>An unknown or undefined chunk type.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dukmdt.h (include D3dukmdt.h, D3dkmddi.h) |