---
UID : NE:rilapitypes.RILUICCRESPONSEPARAMMASK
title : RILUICCRESPONSEPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riluiccresponseparammask_2.htm
old-project : netvista
ms.assetid : b281375a-a2bf-4b19-af94-a3902cf462b2
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARAM_SR_RESPONSE, netvista.riluiccresponseparammask_2, RILUICCRESPONSEPARAMMASK, rilapitypes/RIL_PARAM_SR_STATUSWORD2, RIL_PARAM_SR_ALL, RIL_PARAM_SR_RESPONSESIZE, RILUICCRESPONSEPARAMMASK enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_PARAM_SR_RESPONSE, rilapitypes/RILUICCRESPONSEPARAMMASK, rilapitypes/RIL_PARAM_SR_RESPONSESIZE, rilapitypes/RIL_PARAM_SR_ALL, RIL_PARAM_SR_STATUSWORD2
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
req.typenames : RILUICCRESPONSEPARAMMASK
req.product : Windows 10 or later.
---

# RILUICCRESPONSEPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUICCRESPONSEPARAMMASK { 
  RIL_PARAM_SR_STATUSWORD2,
  RIL_PARAM_SR_RESPONSESIZE,
  RIL_PARAM_SR_RESPONSE,
  RIL_PARAM_SR_ALL
} RILUICCRESPONSEPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_SR_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SR_RESPONSE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SR_RESPONSESIZE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SR_STATUSWORD1</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SR_STATUSWORD2</td>
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