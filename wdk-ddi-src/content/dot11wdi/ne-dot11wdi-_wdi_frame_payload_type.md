---
UID : NE:dot11wdi._WDI_FRAME_PAYLOAD_TYPE
title : _WDI_FRAME_PAYLOAD_TYPE
author : windows-driver-content
description : The WDI_FRAME_PAYLOAD_TYPE enumeration defines the frame payload type.
old-location : netvista\wdi_frame_payload_type.htm
old-project : netvista
ms.assetid : 28aef1bd-915a-4f05-a4b0-bec63ddfdfb5
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _WDI_FRAME_PAYLOAD_TYPE, WDI_FRAME_PAYLOAD_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : dot11wdi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WDI_FRAME_PAYLOAD_TYPE
req.alt-loc : dot11wdi.h
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
req.typenames : WDI_FRAME_PAYLOAD_TYPE
---

# _WDI_FRAME_PAYLOAD_TYPE Enumeration
The WDI_FRAME_PAYLOAD_TYPE enumeration defines the frame payload type.

## Syntax
````
typedef enum _WDI_FRAME_PAYLOAD_TYPE { 
  WDI_FRAME_MSDU           = 0,
  WDI_FRAME_MSDU_FRAGMENT  = 1
} WDI_FRAME_PAYLOAD_TYPE;
````

## Constants

<table>

<tr>
<td>WDI_FRAME_MSDU</td>
<td>MAC service data unit (MSDU).</td>
</tr>

<tr>
<td>WDI_FRAME_MSDU_FRAGMENT</td>
<td>MAC service data unit (MSDU) fragment.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dot11wdi.h |