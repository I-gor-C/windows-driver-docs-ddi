---
UID: NE:rilapitypes.RILSERVICESETTINGSSTATUS
title: RILSERVICESETTINGSSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilservicesettingsstatus.htm
old-project: netvista
ms.assetid: 69340d17-900f-4c46-aafb-866edcb03d77
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILSERVICESETTINGSSTATUS, RILSERVICESETTINGSSTATUS enumeration [Network Drivers Starting with Windows Vista], RIL_SVCSTAT_DEFAULT, RIL_SVCSTAT_DISABLED, RIL_SVCSTAT_ENABLED, RIL_SVCSTAT_MAX, netvista.rilservicesettingsstatus, ntddrilapitypes/RILSERVICESETTINGSSTATUS, ntddrilapitypes/RIL_SVCSTAT_DEFAULT, ntddrilapitypes/RIL_SVCSTAT_DISABLED, ntddrilapitypes/RIL_SVCSTAT_ENABLED, ntddrilapitypes/RIL_SVCSTAT_MAX
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
-	RILSERVICESETTINGSSTATUS
product:
- Windows
targetos: Windows
req.typenames: RILSERVICESETTINGSSTATUS
req.product: Windows 10 or later.
---

# RILSERVICESETTINGSSTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILSERVICESETTINGSSTATUS {
  RIL_SVCSTAT_UNKNOWN   ,
  RIL_SVCSTAT_DISABLED  ,
  RIL_SVCSTAT_ENABLED   ,
  RIL_SVCSTAT_DEFAULT   ,
  RIL_SVCSTAT_MAX
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_SVCSTAT_UNKNOWN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_SVCSTAT_DISABLED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_SVCSTAT_ENABLED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_SVCSTAT_DEFAULT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_SVCSTAT_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |