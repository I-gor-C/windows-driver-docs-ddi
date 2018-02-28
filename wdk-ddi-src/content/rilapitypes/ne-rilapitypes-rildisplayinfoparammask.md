---
UID: NE:rilapitypes.RILDISPLAYINFOPARAMMASK
title: RILDISPLAYINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildisplayinfoparammask_2.htm
old-project: netvista
ms.assetid: d8bd093d-ad95-488e-a057-b96fecf58bbb
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RILDISPLAYINFOPARAMMASK, RILDISPLAYINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_DISPLAY_ALL, RIL_PARAM_DISPLAY_MESSAGE, RIL_PARAM_DISPLAY_MESSAGESIZE, RIL_PARAM_DISPLAY_TAG, RIL_PARAM_DISPLAY_TYPE, netvista.rildisplayinfoparammask_2, rilapitypes/RILDISPLAYINFOPARAMMASK, rilapitypes/RIL_PARAM_DISPLAY_ALL, rilapitypes/RIL_PARAM_DISPLAY_MESSAGE, rilapitypes/RIL_PARAM_DISPLAY_MESSAGESIZE, rilapitypes/RIL_PARAM_DISPLAY_TAG, rilapitypes/RIL_PARAM_DISPLAY_TYPE
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	rilapitypes.h
api_name:
-	RILDISPLAYINFOPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILDISPLAYINFOPARAMMASK
req.product: Windows 10 or later.
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
| **Header** | rilapitypes.h |