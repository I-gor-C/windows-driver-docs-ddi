---
UID: NE:ntddrilapitypes.RILUMTSKIND
title: RILUMTSKIND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilumtskind.htm
old-project: netvista
ms.assetid: aedabb82-73d5-4953-bb7a-4ed526bff5a1
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: ntddrilapitypes/RIL_UMTSKIND_MAX, RILUMTSKIND, ntddrilapitypes/RIL_UMTSKIND_HSPAPLUS, ntddrilapitypes/RIL_UMTSKIND_HSUPA, RIL_UMTSKIND_HSDPA, RIL_UMTSKIND_MAX, ntddrilapitypes/RIL_UMTSKIND_HSDPA, RIL_UMTSKIND_HSPAPLUS, netvista.rilumtskind, ntddrilapitypes/RIL_UMTSKIND_DC_HSPAPLUS, RIL_UMTSKIND_DC_HSPAPLUS, ntddrilapitypes/RIL_UMTSKIND_HSPAPLUS_64QAM, ntddrilapitypes/RILUMTSKIND, RIL_UMTSKIND_HSUPA, RILUMTSKIND enumeration [Network Drivers Starting with Windows Vista], RIL_UMTSKIND_HSPAPLUS_64QAM
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
-	RILUMTSKIND
product: Windows
targetos: Windows
req.typenames: RILUMTSKIND
---

# RILUMTSKIND Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUMTSKIND { 
  RIL_UMTSKIND_HSDPA,
  RIL_UMTSKIND_HSUPA,
  RIL_UMTSKIND_HSPAPLUS,
  RIL_UMTSKIND_DC_HSPAPLUS,
  RIL_UMTSKIND_HSPAPLUS_64QAM,
  RIL_UMTSKIND_MAX
} RILUMTSKIND;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_UMTSKIND_DC_HSPAPLUS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UMTSKIND_HSDPA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UMTSKIND_HSPAPLUS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UMTSKIND_HSPAPLUS_64QAM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UMTSKIND_HSUPA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UMTSKIND_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UMTSKIND_UMTS</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |