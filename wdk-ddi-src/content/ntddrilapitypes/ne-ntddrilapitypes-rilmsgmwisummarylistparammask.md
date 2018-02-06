---
UID: NE:ntddrilapitypes.RILMSGMWISUMMARYLISTPARAMMASK
title: RILMSGMWISUMMARYLISTPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgmwisummarylistparammask.htm
old-project: netvista
ms.assetid: f7b9d558-7c95-40d5-9740-ae1b9f7595c1
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RIL_PARAM_MWISUMMARY_REFNUM, RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS, RIL_PARAM_MWISUMMARY_ACCTADDR, RIL_PARAM_MWISUMMARY_SUMMARYITEMS, ntddrilapitypes/RIL_PARAM_MWISUMMARY_TOTALNUMDETAILITEMS, ntddrilapitypes/RILMSGMWISUMMARYLISTPARAMMASK, ntddrilapitypes/RIL_PARAM_MWISUMMARY_ALL, RILMSGMWISUMMARYLISTPARAMMASK enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_PARAM_MWISUMMARY_ACCTADDR, RILMSGMWISUMMARYLISTPARAMMASK, ntddrilapitypes/RIL_PARAM_MWISUMMARY_REFNUM, ntddrilapitypes/RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS, ntddrilapitypes/RIL_PARAM_MWISUMMARY_SUMMARYITEMS, netvista.rilmsgmwisummarylistparammask, RIL_PARAM_MWISUMMARY_ALL, RIL_PARAM_MWISUMMARY_NUMSUMMARYITEMS
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
-	RILMSGMWISUMMARYLISTPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILMSGMWISUMMARYLISTPARAMMASK
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
| **Header** | ntddrilapitypes.h |