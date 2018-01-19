---
UID : NE:ntddrilapitypes.RILREQUESTGEOLOCATIONDATAPARAMMASK
title : RILREQUESTGEOLOCATIONDATAPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilrequestgeolocationdataparammask.htm
old-project : netvista
ms.assetid : 86b89336-56f9-4665-a0d3-37dc6ec6c377
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILREQUESTGEOLOCATIONDATAPARAMMASK, RILREQUESTGEOLOCATIONDATAPARAMMASK
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
req.alt-api : RILREQUESTGEOLOCATIONDATAPARAMMASK
req.alt-loc : ntddrilapitypes.h
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
req.typenames : RILREQUESTGEOLOCATIONDATAPARAMMASK
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
| **Header** | ntddrilapitypes.h |