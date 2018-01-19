---
UID : NE:ks.KSPROPERTY_CLOCK
title : KSPROPERTY_CLOCK
author : windows-driver-content
description : .
old-location : stream\ksproperty_clock.htm
old-project : stream
ms.assetid : 7269B231-62EC-4AF3-A11E-B51A19B85160
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSPROPERTY_CLOCK, KSPROPERTY_CLOCK
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ks.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSPROPERTY_CLOCK
req.alt-loc : Ks.h
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
req.typenames : KSPROPERTY_CLOCK
---

# KSPROPERTY_CLOCK Enumeration


## Syntax
````
typedef enum  { 
  KSPROPERTY_CLOCK_TIME,
  KSPROPERTY_CLOCK_PHYSICALTIME,
  KSPROPERTY_CLOCK_CORRELATEDTIME,
  KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME,
  KSPROPERTY_CLOCK_STATE,
  KSPROPERTY_CLOCK_RESOLUTION,
#if defined(_NTDDK_)
  KSPROPERTY_CLOCK_FUNCTIONTABLE

#endif } KSPROPERTY_CLOCK;
````

## Constants

<table>

<tr>
<td>KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME</td>
<td></td>
</tr>

<tr>
<td>KSPROPERTY_CLOCK_CORRELATEDTIME</td>
<td></td>
</tr>

<tr>
<td>KSPROPERTY_CLOCK_FUNCTIONTABLE</td>
<td></td>
</tr>

<tr>
<td>KSPROPERTY_CLOCK_PHYSICALTIME</td>
<td></td>
</tr>

<tr>
<td>KSPROPERTY_CLOCK_RESOLUTION</td>
<td></td>
</tr>

<tr>
<td>KSPROPERTY_CLOCK_STATE</td>
<td></td>
</tr>

<tr>
<td>KSPROPERTY_CLOCK_TIME</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h |