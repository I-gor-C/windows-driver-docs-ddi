---
UID : NE:rilapitypes.RILUICCAPPPERSOCHECKSTATUSPARAMMASK
title : RILUICCAPPPERSOCHECKSTATUSPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riluiccapppersocheckstatusparammask_2.htm
old-project : netvista
ms.assetid : 0d722f10-d29d-4197-a2c1-5c2a77004abf
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILUICCAPPPERSOCHECKSTATUSPARAMMASK, RILUICCAPPPERSOCHECKSTATUSPARAMMASK
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
req.alt-api : RILUICCAPPPERSOCHECKSTATUSPARAMMASK
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
req.typenames : RILUICCAPPPERSOCHECKSTATUSPARAMMASK
req.product : Windows 10 or later.
---

# RILUICCAPPPERSOCHECKSTATUSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUICCAPPPERSOCHECKSTATUSPARAMMASK { 
  RIL_PARAM_UAPCS_PERSOFEATURE,
  RIL_PARAM_UAPCS_PERSOCHECKSTATE,
  RIL_PARAM_UAPCS_ALL
} RILUICCAPPPERSOCHECKSTATUSPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_UAPCS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UAPCS_PERSOCHECKSTATE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_UAPCS_PERSOFEATURE</td>
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