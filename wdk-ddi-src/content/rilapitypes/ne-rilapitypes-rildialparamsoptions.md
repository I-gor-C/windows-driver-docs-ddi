---
UID : NE:rilapitypes.RILDIALPARAMSOPTIONS
title : RILDIALPARAMSOPTIONS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rildialparamsoptions_2.htm
old-project : netvista
ms.assetid : c2635f91-005f-45e7-9d6c-92caca7f4452
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILDIALPARAMSOPTIONS, RILDIALPARAMSOPTIONS
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
req.alt-api : RILDIALPARAMSOPTIONS
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
req.typenames : RILDIALPARAMSOPTIONS
req.product : Windows 10 or later.
---

# RILDIALPARAMSOPTIONS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILDIALPARAMSOPTIONS { 
  RIL_DIALOPT_RESTRICTID,
  RIL_DIALOPT_PRESENTID,
  RIL_DIALOPT_ANYEXECUTORFOREMERGENCY,
  RIL_DIALOPT_RTTFULL,
  RIL_DIALOPT_ALL
} RILDIALPARAMSOPTIONS;
````

## Constants

<table>

<tr>
<td>RIL_DIALOPT_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_DIALOPT_ANYEXECUTORFOREMERGENCY</td>
<td></td>
</tr>

<tr>
<td>RIL_DIALOPT_PRESENTID</td>
<td></td>
</tr>

<tr>
<td>RIL_DIALOPT_RESTRICTID</td>
<td></td>
</tr>

<tr>
<td>RIL_DIALOPT_RTTFULL</td>
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