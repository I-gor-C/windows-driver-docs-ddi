---
UID: NE:rilapitypes.RILMSGDCSINDICATION
title: RILMSGDCSINDICATION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgdcsindication.htm
old-project: netvista
ms.assetid: 709980c8-e13f-48a7-9af7-26f0bb79e699
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILMSGDCSINDICATION, RILMSGDCSINDICATION enumeration [Network Drivers Starting with Windows Vista], RIL_DCSINDICATION_EMAIL, RIL_DCSINDICATION_FAX, RIL_DCSINDICATION_MAX, RIL_DCSINDICATION_OTHER, netvista.rilmsgdcsindication, ntddrilapitypes/RILMSGDCSINDICATION, ntddrilapitypes/RIL_DCSINDICATION_EMAIL, ntddrilapitypes/RIL_DCSINDICATION_FAX, ntddrilapitypes/RIL_DCSINDICATION_MAX, ntddrilapitypes/RIL_DCSINDICATION_OTHER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
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
-	RILMSGDCSINDICATION
product: Windows
targetos: Windows
req.typenames: RILMSGDCSINDICATION
req.product: Windows 10 or later.
---

# RILMSGDCSINDICATION Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGDCSINDICATION { 
  RIL_DCSINDICATION_FAX,
  RIL_DCSINDICATION_EMAIL,
  RIL_DCSINDICATION_OTHER,
  RIL_DCSINDICATION_MAX
} RILMSGDCSINDICATION;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_DCSINDICATION_VOICEMAIL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSINDICATION_FAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSINDICATION_EMAIL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSINDICATION_OTHER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSINDICATION_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |