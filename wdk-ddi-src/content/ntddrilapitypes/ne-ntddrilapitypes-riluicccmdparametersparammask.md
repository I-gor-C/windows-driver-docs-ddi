---
UID : NE:ntddrilapitypes.RILUICCCMDPARAMETERSPARAMMASK
title : RILUICCCMDPARAMETERSPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riluicccmdparametersparammask.htm
old-project : netvista
ms.assetid : 721ce7c3-070d-4486-aba8-9a6874721015
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARAM_SCP_PARAM2, ntddrilapitypes/RIL_PARAM_SCP_PARAM3, ntddrilapitypes/RILUICCCMDPARAMETERSPARAMMASK, ntddrilapitypes/RIL_PARAM_SCP_PARAM1, RILUICCCMDPARAMETERSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_PARAM_SCP_PARAM2, RILUICCCMDPARAMETERSPARAMMASK, RIL_PARAM_SCP_PARAM3, RIL_PARAM_SCP_ALL, ntddrilapitypes/RIL_PARAM_SCP_ALL, RIL_PARAM_SCP_PARAM1, netvista.riluicccmdparametersparammask
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddrilapitypes.h
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
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILUICCCMDPARAMETERSPARAMMASK
---

# RILUICCCMDPARAMETERSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUICCCMDPARAMETERSPARAMMASK { 
  RIL_PARAM_SCP_PARAM1,
  RIL_PARAM_SCP_PARAM2,
  RIL_PARAM_SCP_PARAM3,
  RIL_PARAM_SCP_ALL
} RILUICCCMDPARAMETERSPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_SCP_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SCP_FILEPATH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SCP_PARAM1</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SCP_PARAM2</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SCP_PARAM3</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |