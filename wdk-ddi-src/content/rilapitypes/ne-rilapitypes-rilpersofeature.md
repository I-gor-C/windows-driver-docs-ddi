---
UID: NE:rilapitypes.RILPERSOFEATURE
title: RILPERSOFEATURE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpersofeature.htm
old-project: netvista
ms.assetid: e212ab20-e9b4-4ccc-b0db-a82ca5b59573
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILPERSOFEATURE, RILPERSOFEATURE enumeration [Network Drivers Starting with Windows Vista], RIL_PERSOFEATURE_3GPP2_CORP, RIL_PERSOFEATURE_3GPP2_HRPD, RIL_PERSOFEATURE_3GPP2_NETTYPE1, RIL_PERSOFEATURE_3GPP2_NETTYPE2, RIL_PERSOFEATURE_3GPP2_SP, RIL_PERSOFEATURE_3GPP2_UIM, RIL_PERSOFEATURE_3GPP_CORP, RIL_PERSOFEATURE_3GPP_NET, RIL_PERSOFEATURE_3GPP_NETSUB, RIL_PERSOFEATURE_3GPP_SP, RIL_PERSOFEATURE_3GPP_USIM, RIL_PERSOFEATURE_ALL, netvista.rilpersofeature, ntddrilapitypes/RILPERSOFEATURE, ntddrilapitypes/RIL_PERSOFEATURE_3GPP2_CORP, ntddrilapitypes/RIL_PERSOFEATURE_3GPP2_HRPD, ntddrilapitypes/RIL_PERSOFEATURE_3GPP2_NETTYPE1, ntddrilapitypes/RIL_PERSOFEATURE_3GPP2_NETTYPE2, ntddrilapitypes/RIL_PERSOFEATURE_3GPP2_SP, ntddrilapitypes/RIL_PERSOFEATURE_3GPP2_UIM, ntddrilapitypes/RIL_PERSOFEATURE_3GPP_CORP, ntddrilapitypes/RIL_PERSOFEATURE_3GPP_NET, ntddrilapitypes/RIL_PERSOFEATURE_3GPP_NETSUB, ntddrilapitypes/RIL_PERSOFEATURE_3GPP_SP, ntddrilapitypes/RIL_PERSOFEATURE_3GPP_USIM, ntddrilapitypes/RIL_PERSOFEATURE_ALL
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
-	RILPERSOFEATURE
product: Windows
targetos: Windows
req.typenames: RILPERSOFEATURE
req.product: Windows 10 or later.
---

# RILPERSOFEATURE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPERSOFEATURE { 
  RIL_PERSOFEATURE_3GPP_NET,
  RIL_PERSOFEATURE_3GPP_NETSUB,
  RIL_PERSOFEATURE_3GPP_SP,
  RIL_PERSOFEATURE_3GPP_CORP,
  RIL_PERSOFEATURE_3GPP_USIM,
  RIL_PERSOFEATURE_3GPP2_NETTYPE1,
  RIL_PERSOFEATURE_3GPP2_NETTYPE2,
  RIL_PERSOFEATURE_3GPP2_HRPD,
  RIL_PERSOFEATURE_3GPP2_SP,
  RIL_PERSOFEATURE_3GPP2_CORP,
  RIL_PERSOFEATURE_3GPP2_UIM,
  RIL_PERSOFEATURE_ALL
} RILPERSOFEATURE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP_CORP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP_NET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP_NETSUB</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP_SP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP_USIM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP2_CORP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP2_HRPD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP2_NETTYPE1</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP2_NETTYPE2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP2_SP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_3GPP2_UIM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PERSOFEATURE_NONE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |