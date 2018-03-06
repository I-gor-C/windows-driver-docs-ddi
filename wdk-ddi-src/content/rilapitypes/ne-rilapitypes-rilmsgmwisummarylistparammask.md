---
UID: NE:rilapitypes.RILMSGMWISUMMARYLISTPARAMMASK
title: RILMSGMWISUMMARYLISTPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgmwisummarylistparammask_2.htm
old-project: netvista
ms.assetid: cc4253ab-d0f8-4c73-a538-29cac8c0df31
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: RILMSGMWISUMMARYLISTPARAMMASK, RILMSGMWISUMMARYLISTPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_MWISUMMARY_ACCTADDR, RIL_PARAM_MWISUMMARY_ALL, RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS, RIL_PARAM_MWISUMMARY_REFNUM, RIL_PARAM_MWISUMMARY_SUMMARYITEMS, RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS, netvista.rilmsgmwisummarylistparammask_2, rilapitypes/RILMSGMWISUMMARYLISTPARAMMASK, rilapitypes/RIL_PARAM_MWISUMMARY_ACCTADDR, rilapitypes/RIL_PARAM_MWISUMMARY_ALL, rilapitypes/RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS, rilapitypes/RIL_PARAM_MWISUMMARY_REFNUM, rilapitypes/RIL_PARAM_MWISUMMARY_SUMMARYITEMS, rilapitypes/RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS
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
-	RILMSGMWISUMMARYLISTPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILMSGMWISUMMARYLISTPARAMMASK
req.product: Windows 10 or later.
---

# RILMSGMWISUMMARYLISTPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGMWISUMMARYLISTPARAMMASK { 
  RIL_PARAM_MWISUMMARY_REFNUM,
  RIL_PARAM_MWISUMMARY_ACCTADDR,
  RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS,
  RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS,
  RIL_PARAM_MWISUMMARY_SUMMARYITEMS,
  RIL_PARAM_MWISUMMARY_ALL
} RILMSGMWISUMMARYLISTPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_MWISUMMARY_ACCTADDR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MWISUMMARY_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MWISUMMARY_EXECUTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MWISUMMARY_REFNUM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MWISUMMARY_SUMMARYITEMS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |