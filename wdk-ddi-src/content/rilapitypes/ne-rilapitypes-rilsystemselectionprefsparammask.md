---
UID : NE:rilapitypes.RILSYSTEMSELECTIONPREFSPARAMMASK
title : RILSYSTEMSELECTIONPREFSPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsystemselectionprefsparammask_2.htm
old-project : netvista
ms.assetid : 7ae85902-d990-45d9-9e9d-e609aea24091
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARAM_SSP_PLMNINFO, netvista.rilsystemselectionprefsparammask_2, rilapitypes/RIL_PARAM_SSP_SYSTEMTYPES, RIL_PARAM_SSP_ACQUISITIONORDERSIZE, rilapitypes/RIL_PARAM_SSP_ACQUISITIONORDER, RIL_PARAM_SSP_MODE, RIL_PARAM_SSP_SYSTEMTYPES, rilapitypes/RILSYSTEMSELECTIONPREFSPARAMMASK, rilapitypes/RIL_PARAM_SSP_ALL, rilapitypes/RIL_PARAM_SSP_MODE, RIL_PARAM_SSP_ROAMINGMODE, RIL_PARAM_SSP_ALL, RILSYSTEMSELECTIONPREFSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_PARAM_SSP_ACQUISITIONORDERSIZE, RIL_PARAM_SSP_ACQUISITIONORDER, rilapitypes/RIL_PARAM_SSP_ROAMINGMODE, rilapitypes/RIL_PARAM_SSP_PLMNINFO, RILSYSTEMSELECTIONPREFSPARAMMASK
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
req.typenames : RILSYSTEMSELECTIONPREFSPARAMMASK
req.product : Windows 10 or later.
---

# RILSYSTEMSELECTIONPREFSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSYSTEMSELECTIONPREFSPARAMMASK { 
  RIL_PARAM_SSP_SYSTEMTYPES,
  RIL_PARAM_SSP_MODE,
  RIL_PARAM_SSP_PLMNINFO,
  RIL_PARAM_SSP_ROAMINGMODE,
  RIL_PARAM_SSP_ACQUISITIONORDERSIZE,
  RIL_PARAM_SSP_ACQUISITIONORDER,
  RIL_PARAM_SSP_ALL
} RILSYSTEMSELECTIONPREFSPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_SSP_ACQUISITIONORDER</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SSP_ACQUISITIONORDERSIZE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SSP_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SSP_EXECUTOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SSP_MODE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SSP_PLMNINFO</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SSP_ROAMINGMODE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SSP_SYSTEMTYPES</td>
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