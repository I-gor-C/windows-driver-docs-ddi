---
UID : NE:rilapitypes.RILRADIOCONFIGURATIONRADIOTYPE
title : RILRADIOCONFIGURATIONRADIOTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilradioconfigurationradiotype_2.htm
old-project : netvista
ms.assetid : 5ac7d462-53bb-4540-8889-f2f6c71d4823
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILRADIOCONFIGURATIONRADIOTYPE, RILRADIOCONFIGURATIONRADIOTYPE
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
req.alt-api : RILRADIOCONFIGURATIONRADIOTYPE
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
req.typenames : RILRADIOCONFIGURATIONRADIOTYPE
req.product : Windows 10 or later.
---

# RILRADIOCONFIGURATIONRADIOTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILRADIOCONFIGURATIONRADIOTYPE { 
  RIL_RADIOTYPE_SINGLE,
  RIL_RADIOTYPE_MULTIMODE,
  RIL_RADIOTYPE_1XCSFB,
  RIL_RADIOTYPE_SVLTE,
  RIL_RADIOTYPE_DUALSTANDBY,
  RIL_RADIOTYPE_DUALACTIVE,
  RIL_RADIOTYPE_SGLTE,
  RIL_RADIOTYPE_SVLTE_DUALACTIVE,
  RIL_RADIOTYPE_SGLTE_DUALACTIVE,
  RIL_RADIOTYPE_SRLTE,
  RIL_RADIOTYPE_MAX
} RILRADIOCONFIGURATIONRADIOTYPE;
````

## Constants

<table>

<tr>
<td>RIL_RADIOTYPE_1XCSFB</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOTYPE_DUALACTIVE</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOTYPE_DUALSTANDBY</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOTYPE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOTYPE_MULTIMODE</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOTYPE_SGLTE</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOTYPE_SGLTE_DUALACTIVE</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOTYPE_SINGLE</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOTYPE_SRLTE</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOTYPE_SVLTE</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOTYPE_SVLTE_DUALACTIVE</td>
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