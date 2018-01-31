---
UID : NE:rilapitypes.RILCALLMEDIAOFFERANSWERPARAMMASK
title : RILCALLMEDIAOFFERANSWERPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallmediaofferanswerparammask_2.htm
old-project : netvista
ms.assetid : 2dd7a85e-b284-42be-89d4-a4a7361d5c6d
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_PARAM_CMOA_NEW_STATE, rilapitypes/RILCALLMEDIAOFFERANSWERPARAMMASK, RIL_PARAM_CMOA_NEW_STATE, rilapitypes/RIL_PARAM_CMOA_OLD_STATE, rilapitypes/RIL_PARAM_CMOA_ACTION, rilapitypes/RIL_PARAM_CMOA_CHANGE, RIL_PARAM_CMOA_ACTION, RIL_PARAM_CMOA_CHANGE, RILCALLMEDIAOFFERANSWERPARAMMASK enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_PARAM_CMOA_ALL, RILCALLMEDIAOFFERANSWERPARAMMASK, netvista.rilcallmediaofferanswerparammask_2, RIL_PARAM_CMOA_OLD_STATE, RIL_PARAM_CMOA_ALL
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILCALLMEDIAOFFERANSWERPARAMMASK
req.product : Windows 10 or later.
---

# RILCALLMEDIAOFFERANSWERPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLMEDIAOFFERANSWERPARAMMASK { 
  RIL_PARAM_CMOA_CHANGE,
  RIL_PARAM_CMOA_ACTION,
  RIL_PARAM_CMOA_OLD_STATE,
  RIL_PARAM_CMOA_NEW_STATE,
  RIL_PARAM_CMOA_ALL
} RILCALLMEDIAOFFERANSWERPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_CMOA_ACTION</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CMOA_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CMOA_CHANGE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CMOA_ID</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CMOA_NEW_STATE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CMOA_OLD_STATE</td>
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