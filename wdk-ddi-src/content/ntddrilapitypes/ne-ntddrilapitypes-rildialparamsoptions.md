---
UID : NE:ntddrilapitypes.RILDIALPARAMSOPTIONS
title : RILDIALPARAMSOPTIONS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rildialparamsoptions.htm
old-project : netvista
ms.assetid : 78fef8f7-e6cd-4da6-9c2a-2eaf1da6339b
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_DIALOPT_ANYEXECUTORFOREMERGENCY, ntddrilapitypes/RIL_DIALOPT_RESTRICTID, RILDIALPARAMSOPTIONS enumeration [Network Drivers Starting with Windows Vista], RIL_DIALOPT_RTTFULL, ntddrilapitypes/RILDIALPARAMSOPTIONS, RIL_DIALOPT_RESTRICTID, netvista.rildialparamsoptions, RILDIALPARAMSOPTIONS, RIL_DIALOPT_PRESENTID, ntddrilapitypes/RIL_DIALOPT_PRESENTID, ntddrilapitypes/RIL_DIALOPT_ANYEXECUTORFOREMERGENCY, RIL_DIALOPT_ALL, ntddrilapitypes/RIL_DIALOPT_RTTFULL, ntddrilapitypes/RIL_DIALOPT_ALL
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
req.typenames : RILDIALPARAMSOPTIONS
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
<td>RIL_DIALOPT_NONE</td>
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
| **Header** | ntddrilapitypes.h |