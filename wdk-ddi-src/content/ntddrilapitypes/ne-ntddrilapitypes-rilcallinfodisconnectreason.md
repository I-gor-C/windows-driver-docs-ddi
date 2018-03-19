---
UID: NE:ntddrilapitypes.RILCALLINFODISCONNECTREASON
title: RILCALLINFODISCONNECTREASON
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfodisconnectreason.htm
old-project: netvista
ms.assetid: 2e339b56-9130-4459-8ccd-171f721ae83e
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILCALLINFODISCONNECTREASON, RILCALLINFODISCONNECTREASON enumeration [Network Drivers Starting with Windows Vista], RIL_DISCREASON_BUSY, RIL_DISCREASON_CONGESTION, RIL_DISCREASON_EMERGENCYFAILOVER, RIL_DISCREASON_EMERGENCYONLY, RIL_DISCREASON_HANDOVER_MERGE, RIL_DISCREASON_MAX, RIL_DISCREASON_NETWORKERROR, RIL_DISCREASON_NOSERVICE, RIL_DISCREASON_OTHEREXECUTORBUSY, RIL_DISCREASON_RADIOFADE, netvista.rilcallinfodisconnectreason, ntddrilapitypes/RILCALLINFODISCONNECTREASON, ntddrilapitypes/RIL_DISCREASON_BUSY, ntddrilapitypes/RIL_DISCREASON_CONGESTION, ntddrilapitypes/RIL_DISCREASON_EMERGENCYFAILOVER, ntddrilapitypes/RIL_DISCREASON_EMERGENCYONLY, ntddrilapitypes/RIL_DISCREASON_HANDOVER_MERGE, ntddrilapitypes/RIL_DISCREASON_MAX, ntddrilapitypes/RIL_DISCREASON_NETWORKERROR, ntddrilapitypes/RIL_DISCREASON_NOSERVICE, ntddrilapitypes/RIL_DISCREASON_OTHEREXECUTORBUSY, ntddrilapitypes/RIL_DISCREASON_RADIOFADE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: Rilapitypes.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddrilapitypes.h
api_name:
-	RILCALLINFODISCONNECTREASON
product: Windows
targetos: Windows
req.typenames: RILCALLINFODISCONNECTREASON
---

# RILCALLINFODISCONNECTREASON Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLINFODISCONNECTREASON { 
  RIL_DISCREASON_BUSY,
  RIL_DISCREASON_NETWORKERROR,
  RIL_DISCREASON_RADIOFADE,
  RIL_DISCREASON_CONGESTION,
  RIL_DISCREASON_EMERGENCYONLY,
  RIL_DISCREASON_NOSERVICE,
  RIL_DISCREASON_OTHEREXECUTORBUSY,
  RIL_DISCREASON_EMERGENCYFAILOVER,
  RIL_DISCREASON_HANDOVER_MERGE,
  RIL_DISCREASON_MAX
} RILCALLINFODISCONNECTREASON;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_DISCREASON_NULL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DISCREASON_BUSY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DISCREASON_NETWORKERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DISCREASON_RADIOFADE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DISCREASON_CONGESTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DISCREASON_EMERGENCYONLY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DISCREASON_NOSERVICE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DISCREASON_OTHEREXECUTORBUSY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DISCREASON_EMERGENCYFAILOVER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DISCREASON_HANDOVER_MERGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DISCREASON_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |