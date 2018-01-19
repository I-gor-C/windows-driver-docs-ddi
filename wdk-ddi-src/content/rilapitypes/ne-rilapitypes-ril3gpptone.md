---
UID : NE:rilapitypes.RIL3GPPTONE
title : RIL3GPPTONE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\ril3gpptone_2.htm
old-project : netvista
ms.assetid : 05981a37-ce5c-4214-82b7-c8705102bd6a
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RIL3GPPTONE, RIL3GPPTONE
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
req.alt-api : RIL3GPPTONE
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
req.typenames : RIL3GPPTONE
req.product : Windows 10 or later.
---

# RIL3GPPTONE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RIL3GPPTONE { 
  RIL_3GPPTONE_RINGBACK,
  RIL_3GPPTONE_BUSY,
  RIL_3GPPTONE_CONGESTION,
  RIL_3GPPTONE_AUTHENTICATIONFAILURE,
  RIL_3GPPTONE_NUMBERUNOBTAINABLE,
  RIL_3GPPTONE_CALLDROPPED,
  RIL_3GPPTONE_MAX
} RIL3GPPTONE;
````

## Constants

<table>

<tr>
<td>RIL_3GPPTONE_AUTHENTICATIONFAILURE</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPPTONE_BUSY</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPPTONE_CALLDROPPED</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPPTONE_CONGESTION</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPPTONE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPPTONE_NUMBERUNOBTAINABLE</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPPTONE_RINGBACK</td>
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