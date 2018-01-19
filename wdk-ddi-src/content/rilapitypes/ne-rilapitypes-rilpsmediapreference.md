---
UID : NE:rilapitypes.RILPSMEDIAPREFERENCE
title : RILPSMEDIAPREFERENCE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilpsmediapreference_2.htm
old-project : netvista
ms.assetid : 607c00a2-6f7e-4a68-87da-f54b8dd73b88
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILPSMEDIAPREFERENCE, RILPSMEDIAPREFERENCE
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
req.alt-api : RILPSMEDIAPREFERENCE
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
req.typenames : RILPSMEDIAPREFERENCE
req.product : Windows 10 or later.
---

# RILPSMEDIAPREFERENCE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPSMEDIAPREFERENCE { 
  RIL_PSMPREF_WIFIONLY,
  RIL_PSMPREF_WIFIPREFERRED,
  RIL_PSMPREF_CELLONLY,
  RIL_PSMPREF_CELLPREFERRED,
  RIL_PSMPREF_NUMBER_OF_VALUES
} RILPSMEDIAPREFERENCE;
````

## Constants

<table>

<tr>
<td>RIL_PSMPREF_CELLONLY</td>
<td></td>
</tr>

<tr>
<td>RIL_PSMPREF_CELLPREFERRED</td>
<td></td>
</tr>

<tr>
<td>RIL_PSMPREF_NUMBER_OF_VALUES</td>
<td></td>
</tr>

<tr>
<td>RIL_PSMPREF_WIFIONLY</td>
<td></td>
</tr>

<tr>
<td>RIL_PSMPREF_WIFIPREFERRED</td>
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