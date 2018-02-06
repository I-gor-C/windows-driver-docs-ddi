---
UID: NE:ntddrilapitypes.RILCALLMEDIATYPE
title: RILCALLMEDIATYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediatype.htm
old-project: netvista
ms.assetid: 993013f1-5026-4c30-b4df-958606adc8fa
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: netvista.rilcallmediatype, ntddrilapitypes/RIL_CALLMEDIATYPE_AUDIO, ntddrilapitypes/RIL_CALLMEDIATYPE_CUSTOM, RILCALLMEDIATYPE enumeration [Network Drivers Starting with Windows Vista], RIL_CALLMEDIATYPE_MAX, ntddrilapitypes/RILCALLMEDIATYPE, RILCALLMEDIATYPE, RIL_CALLMEDIATYPE_VIDEO, ntddrilapitypes/RIL_CALLMEDIATYPE_VIDEO, RIL_CALLMEDIATYPE_CUSTOM, RIL_CALLMEDIATYPE_AUDIO, ntddrilapitypes/RIL_CALLMEDIATYPE_MAX
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
-	RILCALLMEDIATYPE
product: Windows
targetos: Windows
req.typenames: RILCALLMEDIATYPE
---

# RILCALLMEDIATYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLMEDIATYPE { 
  RIL_CALLMEDIATYPE_AUDIO,
  RIL_CALLMEDIATYPE_VIDEO,
  RIL_CALLMEDIATYPE_CUSTOM,
  RIL_CALLMEDIATYPE_MAX
} RILCALLMEDIATYPE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_CALLMEDIATYPE_AUDIO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLMEDIATYPE_CUSTOM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLMEDIATYPE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLMEDIATYPE_UNKNOWN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLMEDIATYPE_VIDEO</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |