---
UID : NE:ks.PKSSTATE
title : "*PKSSTATE"
author : windows-driver-content
description : The KSSTATE enumeration lists possible states of a kernel streaming object.
old-location : stream\ksstate.htm
old-project : stream
ms.assetid : 6f5a3c65-9d6c-4d5f-af99-71aba16eb254
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : "*PKSSTATE, *PKSSTATE, KSSTATE"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSSTATE
req.alt-loc : ks.h
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
req.typenames : "*PKSSTATE, KSSTATE"
---

# *PKSSTATE Enumeration
The KSSTATE enumeration lists possible states of a kernel streaming object.

## Syntax
````
typedef enum  { 
  KSSTATE_STOP     = 0,
  KSSTATE_ACQUIRE  = 1,
  KSSTATE_PAUSE    = 2,
  KSSTATE_RUN      = 3
} KSSTATE, *PKSSTATE;
````

## Constants

<table>

<tr>
<td>KSSTATE_ACQUIRE</td>
<td>Indicates that the object is acquiring resources.</td>
</tr>

<tr>
<td>KSSTATE_PAUSE</td>
<td>Indicates that the object is preparing to make instant transition to Run state.</td>
</tr>

<tr>
<td>KSSTATE_RUN</td>
<td>Indicates that the object is actively streaming.</td>
</tr>

<tr>
<td>KSSTATE_STOP</td>
<td>Indicates that the object is in minimum resource consumption mode.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |