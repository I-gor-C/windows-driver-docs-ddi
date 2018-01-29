---
UID : NE:rilapitypes.RILCALLFORWARDINGSETTINGSPARAMMASK
title : RILCALLFORWARDINGSETTINGSPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallforwardingsettingsparammask_2.htm
old-project : netvista
ms.assetid : 4db4e6fe-1faf-4109-95aa-e2e5bf3b0dd6
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_PARAM_CFS_ALL, RILCALLFORWARDINGSETTINGSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_PARAM_CFS_DELAYTIME, RIL_PARAM_CFS_ALL, rilapitypes/RIL_PARAM_CFS_SUBADDRESS, rilapitypes/RIL_PARAM_CFS_INFOCLASSES, RIL_PARAM_CFS_ADDRESS, RIL_PARAM_CFS_SUBADDRESS, RIL_PARAM_CFS_DELAYTIME, RIL_PARAM_CFS_INFOCLASSES, netvista.rilcallforwardingsettingsparammask_2, rilapitypes/RIL_PARAM_CFS_ADDRESS, rilapitypes/RILCALLFORWARDINGSETTINGSPARAMMASK, RILCALLFORWARDINGSETTINGSPARAMMASK
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
req.typenames : RILCALLFORWARDINGSETTINGSPARAMMASK
req.product : Windows 10 or later.
---

# RILCALLFORWARDINGSETTINGSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLFORWARDINGSETTINGSPARAMMASK { 
  RIL_PARAM_CFS_INFOCLASSES,
  RIL_PARAM_CFS_ADDRESS,
  RIL_PARAM_CFS_SUBADDRESS,
  RIL_PARAM_CFS_DELAYTIME,
  RIL_PARAM_CFS_ALL
} RILCALLFORWARDINGSETTINGSPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_CFS_ADDRESS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CFS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CFS_DELAYTIME</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CFS_INFOCLASSES</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CFS_STATUS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CFS_SUBADDRESS</td>
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