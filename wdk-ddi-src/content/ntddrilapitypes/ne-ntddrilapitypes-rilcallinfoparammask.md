---
UID : NE:ntddrilapitypes.RILCALLINFOPARAMMASK
title : RILCALLINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallinfoparammask.htm
old-project : netvista
ms.assetid : 7e6138f6-4728-4072-9600-749594f23b68
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARAM_CI_DISCONNECTREASON, RILCALLINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_CI_RTTMODETYPE, RIL_PARAM_CI_TYPE, RIL_PARAM_CI_NAME_PRES_IND, RIL_PARAM_CI_SUBADDRESS, RIL_PARAM_CI_DISCONNECTINITIATOR, RIL_PARAM_CI_CALLMODIFICATIONCAUSE, RIL_PARAM_CI_RTTCAPINFO, ntddrilapitypes/RIL_PARAM_CI_SUBADDRESS, RIL_PARAM_CI_ADDRESS, RIL_PARAM_CI_STATUS, ntddrilapitypes/RILCALLINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_CI_DISCONNECTDETAILS, ntddrilapitypes/RIL_PARAM_CI_MULTIPARTY, netvista.rilcallinfoparammask, ntddrilapitypes/RIL_PARAM_CI_ADDRESS, RIL_PARAM_CI_MULTIPARTY, ntddrilapitypes/RIL_PARAM_CI_ALL, ntddrilapitypes/RIL_PARAM_CI_DISCONNECTINITIATOR, RIL_PARAM_CI_DIRECTION, RIL_PARAM_CI_ALL, ntddrilapitypes/RIL_PARAM_CI_DIRECTION, ntddrilapitypes/RIL_PARAM_CI_ID, RIL_PARAM_CI_RTTACTION, RIL_PARAM_CI_DESCRIPTION, ntddrilapitypes/RIL_PARAM_CI_DISCONNECTREASON, RIL_PARAM_CI_HANDOVERSTATE, ntddrilapitypes/RIL_PARAM_CI_FLAGS, ntddrilapitypes/RIL_PARAM_CI_TYPE, RIL_PARAM_CI_FLAGS, ntddrilapitypes/RIL_PARAM_CI_DESCRIPTION, RIL_PARAM_CI_ID, ntddrilapitypes/RIL_PARAM_CI_NUM_PRES_IND, ntddrilapitypes/RIL_PARAM_CI_NAME_PRES_IND, ntddrilapitypes/RIL_PARAM_CI_HANDOVERSTATE, ntddrilapitypes/RIL_PARAM_CI_CALLMODIFICATIONCAUSE, RIL_PARAM_CI_NUM_PRES_IND, RIL_PARAM_CI_RTTMODETYPE, ntddrilapitypes/RIL_PARAM_CI_STATUS, RIL_PARAM_CI_OFFERANSWER, ntddrilapitypes/RIL_PARAM_CI_RTTCAPINFO, ntddrilapitypes/RIL_PARAM_CI_RTTACTION, RILCALLINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_CI_DISCONNECTDETAILS, ntddrilapitypes/RIL_PARAM_CI_OFFERANSWER
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
req.typenames : RILCALLINFOPARAMMASK
---

# RILCALLINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLINFOPARAMMASK { 
  RIL_PARAM_CI_ID,
  RIL_PARAM_CI_DIRECTION,
  RIL_PARAM_CI_STATUS,
  RIL_PARAM_CI_TYPE,
  RIL_PARAM_CI_MULTIPARTY,
  RIL_PARAM_CI_ADDRESS,
  RIL_PARAM_CI_SUBADDRESS,
  RIL_PARAM_CI_DESCRIPTION,
  RIL_PARAM_CI_NUM_PRES_IND,
  RIL_PARAM_CI_NAME_PRES_IND,
  RIL_PARAM_CI_FLAGS,
  RIL_PARAM_CI_DISCONNECTINITIATOR,
  RIL_PARAM_CI_DISCONNECTREASON,
  RIL_PARAM_CI_DISCONNECTDETAILS,
  RIL_PARAM_CI_OFFERANSWER,
  RIL_PARAM_CI_HANDOVERSTATE,
  RIL_PARAM_CI_CALLMODIFICATIONCAUSE,
  RIL_PARAM_CI_RTTMODETYPE,
  RIL_PARAM_CI_RTTCAPINFO,
  RIL_PARAM_CI_RTTACTION,
  RIL_PARAM_CI_ALL
} RILCALLINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_CI_ADDRESS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_CALLMODIFICATIONCAUSE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_DESCRIPTION</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_DIRECTION</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_DISCONNECTDETAILS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_DISCONNECTINITIATOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_DISCONNECTREASON</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_EXECUTOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_FLAGS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_HANDOVERSTATE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_ID</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_MULTIPARTY</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_NAME_PRES_IND</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_NUM_PRES_IND</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_OFFERANSWER</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_RTTACTION</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_RTTCAPINFO</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_RTTMODETYPE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_STATUS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_SUBADDRESS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CI_TYPE</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |