---
UID: NE:rilapitypes.RILSIGNALQUALITYPARAMMASK
title: RILSIGNALQUALITYPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsignalqualityparammask_2.htm
old-project: netvista
ms.assetid: be6c46bb-9c14-4daf-b76a-679d71269965
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: rilapitypes/RIL_PARAM_SQ_SIGNALSTRENGTH, RILSIGNALQUALITYPARAMMASK, rilapitypes/RILSIGNALQUALITYPARAMMASK, rilapitypes/RIL_PARAM_SQ_NUMSIGNALBARS, RIL_PARAM_SQ_SYSTEMTYPE, RIL_PARAM_SQ_SNR, rilapitypes/RIL_PARAM_SQ_SNR, rilapitypes/RIL_PARAM_SQ_SYSTEMTYPE, RIL_PARAM_SQ_SIGNALSTRENGTH, netvista.rilsignalqualityparammask_2, RIL_PARAM_SQ_NUMSIGNALBARS, RIL_PARAM_SQ_ALL, RILSIGNALQUALITYPARAMMASK enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_PARAM_SQ_ALL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
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
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	rilapitypes.h
apiname:
-	RILSIGNALQUALITYPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILSIGNALQUALITYPARAMMASK
req.product: Windows 10 or later.
---

# RILSIGNALQUALITYPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSIGNALQUALITYPARAMMASK { 
  RIL_PARAM_SQ_SYSTEMTYPE,
  RIL_PARAM_SQ_NUMSIGNALBARS,
  RIL_PARAM_SQ_SIGNALSTRENGTH,
  RIL_PARAM_SQ_SNR,
  RIL_PARAM_SQ_ALL
} RILSIGNALQUALITYPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_SQ_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SQ_EXECUTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SQ_NUMSIGNALBARS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SQ_SIGNALSTRENGTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SQ_SNR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SQ_SYSTEMTYPE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |