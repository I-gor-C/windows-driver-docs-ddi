---
UID : NE:ntddrilapitypes.RILCALLERIDSETTINGSPARAMMASK
title : RILCALLERIDSETTINGSPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcalleridsettingsparammask.htm
old-project : netvista
ms.assetid : 3a8b4be6-91b5-4368-8f54-efa73deb41c0
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILCALLERIDSETTINGSPARAMMASK, RIL_PARAM_CIDS_STATUS, ntddrilapitypes/RIL_PARAM_CIDS_PROVISIONING, netvista.rilcalleridsettingsparammask, ntddrilapitypes/RIL_PARAM_CIDS_ALL, RIL_PARAM_CIDS_PROVISIONING, ntddrilapitypes/RIL_PARAM_CIDS_STATUS, RIL_PARAM_CIDS_ALL, RILCALLERIDSETTINGSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RILCALLERIDSETTINGSPARAMMASK
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
req.typenames : RILCALLERIDSETTINGSPARAMMASK
---

# RILCALLERIDSETTINGSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLERIDSETTINGSPARAMMASK { 
  RIL_PARAM_CIDS_PROVISIONING,
  RIL_PARAM_CIDS_STATUS,
  RIL_PARAM_CIDS_ALL
} RILCALLERIDSETTINGSPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_CIDS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CIDS_EXECUTOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CIDS_PROVISIONING</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CIDS_STATUS</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |