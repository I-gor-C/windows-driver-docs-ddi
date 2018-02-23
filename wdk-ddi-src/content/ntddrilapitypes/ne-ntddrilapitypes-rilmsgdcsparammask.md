---
UID: NE:ntddrilapitypes.RILMSGDCSPARAMMASK
title: RILMSGDCSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgdcsparammask.htm
old-project: netvista
ms.assetid: 2cd5afcd-1d69-475f-95ea-165a405d8ee8
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: ntddrilapitypes/RIL_PARAM_MDCS_FLAGS, ntddrilapitypes/RIL_PARAM_MDCS_LANGUAGE, RILMSGDCSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_MDCS_MSGCLASS, ntddrilapitypes/RIL_PARAM_MDCS_MSGCLASS, RIL_PARAM_MDCS_ALPHABET, ntddrilapitypes/RIL_PARAM_MDCS_ALPHABET, netvista.rilmsgdcsparammask, ntddrilapitypes/RIL_PARAM_MDCS_INDICATION, RIL_PARAM_MDCS_LANGUAGE, RIL_PARAM_MDCS_ALL, RILMSGDCSPARAMMASK, RIL_PARAM_MDCS_INDICATION, ntddrilapitypes/RIL_PARAM_MDCS_ALL, RIL_PARAM_MDCS_FLAGS, ntddrilapitypes/RILMSGDCSPARAMMASK
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
-	RILMSGDCSPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILMSGDCSPARAMMASK
---

# RILMSGDCSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGDCSPARAMMASK { 
  RIL_PARAM_MDCS_FLAGS,
  RIL_PARAM_MDCS_MSGCLASS,
  RIL_PARAM_MDCS_ALPHABET,
  RIL_PARAM_MDCS_INDICATION,
  RIL_PARAM_MDCS_LANGUAGE,
  RIL_PARAM_MDCS_ALL
} RILMSGDCSPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_MDCS_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_ALPHABET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_FLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_INDICATION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_LANGUAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_MSGCLASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_TYPE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |