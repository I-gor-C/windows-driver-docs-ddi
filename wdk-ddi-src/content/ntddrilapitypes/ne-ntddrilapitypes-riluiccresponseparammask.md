---
UID: NE:ntddrilapitypes.RILUICCRESPONSEPARAMMASK
title: RILUICCRESPONSEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccresponseparammask.htm
old-project: netvista
ms.assetid: 2a87655f-8c8c-48c7-982e-dcb70ca600fb
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RIL_PARAM_SR_STATUSWORD2, RIL_PARAM_SR_ALL, RILUICCRESPONSEPARAMMASK, ntddrilapitypes/RILUICCRESPONSEPARAMMASK, ntddrilapitypes/RIL_PARAM_SR_RESPONSESIZE, ntddrilapitypes/RIL_PARAM_SR_STATUSWORD2, ntddrilapitypes/RIL_PARAM_SR_RESPONSE, netvista.riluiccresponseparammask, RIL_PARAM_SR_RESPONSESIZE, ntddrilapitypes/RIL_PARAM_SR_ALL, RIL_PARAM_SR_RESPONSE, RILUICCRESPONSEPARAMMASK enumeration [Network Drivers Starting with Windows Vista]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddrilapitypes.h
apiname:
-	RILUICCRESPONSEPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILUICCRESPONSEPARAMMASK
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
| **Header** | ntddrilapitypes.h |