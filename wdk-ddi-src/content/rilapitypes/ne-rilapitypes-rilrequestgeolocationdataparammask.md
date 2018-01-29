---
UID : NE:rilapitypes.RILREQUESTGEOLOCATIONDATAPARAMMASK
title : RILREQUESTGEOLOCATIONDATAPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilrequestgeolocationdataparammask_2.htm
old-project : netvista
ms.assetid : b81cbf26-7164-4082-a505-2a849ec3d1ea
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILREQUESTGEOLOCATIONDATAPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RILREQUESTGEOLOCATIONDATAPARAMMASK, rilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK, RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY, rilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY, RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL, rilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE, rilapitypes/RILREQUESTGEOLOCATIONDATAPARAMMASK, rilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL, RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION, rilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR, RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR, netvista.rilrequestgeolocationdataparammask_2, rilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION, RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK, RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE
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
req.typenames : RILREQUESTGEOLOCATIONDATAPARAMMASK
req.product : Windows 10 or later.
---

# RILREQUESTGEOLOCATIONDATAPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILREQUESTGEOLOCATIONDATAPARAMMASK { 
  RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL
} RILREQUESTGEOLOCATIONDATAPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REQUESTGEOLOCATIONDATA_NONE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE</td>
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