---
UID : NE:rilapitypes.RILUMTSKIND
title : RILUMTSKIND
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilumtskind_2.htm
old-project : netvista
ms.assetid : 66322f97-e249-4337-b228-826ab4728220
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILUMTSKIND, RILUMTSKIND
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
req.alt-api : RILUMTSKIND
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
req.typenames : RILUMTSKIND
req.product : Windows 10 or later.
---

# RILUMTSKIND Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUMTSKIND { 
  RIL_UMTSKIND_HSDPA,
  RIL_UMTSKIND_HSUPA,
  RIL_UMTSKIND_HSPAPLUS,
  RIL_UMTSKIND_DC_HSPAPLUS,
  RIL_UMTSKIND_HSPAPLUS_64QAM,
  RIL_UMTSKIND_MAX
} RILUMTSKIND;
````

## Constants

<table>

<tr>
<td>RIL_UMTSKIND_DC_HSPAPLUS</td>
<td></td>
</tr>

<tr>
<td>RIL_UMTSKIND_HSDPA</td>
<td></td>
</tr>

<tr>
<td>RIL_UMTSKIND_HSPAPLUS</td>
<td></td>
</tr>

<tr>
<td>RIL_UMTSKIND_HSPAPLUS_64QAM</td>
<td></td>
</tr>

<tr>
<td>RIL_UMTSKIND_HSUPA</td>
<td></td>
</tr>

<tr>
<td>RIL_UMTSKIND_MAX</td>
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