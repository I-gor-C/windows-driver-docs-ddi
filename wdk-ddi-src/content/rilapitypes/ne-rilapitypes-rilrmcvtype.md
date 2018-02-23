---
UID: NE:rilapitypes.RILRMCVTYPE
title: RILRMCVTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilrmcvtype_2.htm
old-project: netvista
ms.assetid: 7517d3fd-723d-4fd7-b5ce-3d08443b8f59
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RIL_RMCV_TYPE_BOOLEAN, rilapitypes/RILRMCVTYPE, rilapitypes/RIL_RMCV_TYPE_DWORD, RILRMCVTYPE, RILRMCVTYPE enumeration [Network Drivers Starting with Windows Vista], netvista.rilrmcvtype_2, rilapitypes/RIL_RMCV_TYPE_BOOLEAN, RIL_RMCV_TYPE_DWORD, rilapitypes/RIL_RMCV_TYPE_STRING, RIL_RMCV_TYPE_STRING
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
-	RILRMCVTYPE
product: Windows
targetos: Windows
req.typenames: RILRMCVTYPE
req.product: Windows 10 or later.
---

# RILRMCVTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILRMCVTYPE { 
  RIL_RMCV_TYPE_BOOLEAN,
  RIL_RMCV_TYPE_DWORD,
  RIL_RMCV_TYPE_STRING
} RILRMCVTYPE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_RMCV_TYPE_BOOLEAN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RMCV_TYPE_DWORD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RMCV_TYPE_NONE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RMCV_TYPE_STRING</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |