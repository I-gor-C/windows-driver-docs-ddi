---
UID : NE:rilapitypes.RILMSGOUTSUBMITVPFORMAT
title : RILMSGOUTSUBMITVPFORMAT
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgoutsubmitvpformat_2.htm
old-project : netvista
ms.assetid : aa383bc9-935d-4883-929d-4ea58a1bf2c9
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMSGOUTSUBMITVPFORMAT, RILMSGOUTSUBMITVPFORMAT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : rilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILMSGOUTSUBMITVPFORMAT
req.alt-loc : rilapitypes.h
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
req.typenames : RILMSGOUTSUBMITVPFORMAT
req.product : Windows 10 or later.
---

# RILMSGOUTSUBMITVPFORMAT Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGOUTSUBMITVPFORMAT { 
  RIL_MSGVP_RELATIVE,
  RIL_MSGVP_ENHANCED,
  RIL_MSGVP_ABSOLUTE,
  RIL_MSGVP_MAX
} RILMSGOUTSUBMITVPFORMAT;
````

## Constants

<table>

<tr>
<td>RIL_MSGVP_ABSOLUTE</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGVP_ENHANCED</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGVP_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGVP_RELATIVE</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |