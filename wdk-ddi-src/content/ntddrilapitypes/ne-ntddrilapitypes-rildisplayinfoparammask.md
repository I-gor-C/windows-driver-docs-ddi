---
UID : NE:ntddrilapitypes.RILDISPLAYINFOPARAMMASK
title : RILDISPLAYINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rildisplayinfoparammask.htm
old-project : netvista
ms.assetid : deb9da97-7a61-4642-bebd-ab0e4082b410
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RIL_PARAM_DISPLAY_MESSAGESIZE, RILDISPLAYINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_DISPLAY_TYPE, ntddrilapitypes/RIL_PARAM_DISPLAY_ALL, RIL_PARAM_DISPLAY_TYPE, RILDISPLAYINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_PARAM_DISPLAY_MESSAGE, RIL_PARAM_DISPLAY_TAG, RIL_PARAM_DISPLAY_MESSAGESIZE, RIL_PARAM_DISPLAY_ALL, RIL_PARAM_DISPLAY_MESSAGE, ntddrilapitypes/RILDISPLAYINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_DISPLAY_TAG, netvista.rildisplayinfoparammask
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
req.typenames : RILDISPLAYINFOPARAMMASK
---

# RILDISPLAYINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILDISPLAYINFOPARAMMASK { 
  RIL_PARAM_DISPLAY_TYPE,
  RIL_PARAM_DISPLAY_TAG,
  RIL_PARAM_DISPLAY_MESSAGESIZE,
  RIL_PARAM_DISPLAY_MESSAGE,
  RIL_PARAM_DISPLAY_ALL
} RILDISPLAYINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_DISPLAY_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_DISPLAY_EXECUTOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_DISPLAY_MESSAGE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_DISPLAY_MESSAGESIZE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_DISPLAY_TAG</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_DISPLAY_TYPE</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |