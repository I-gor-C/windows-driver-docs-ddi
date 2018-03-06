---
UID: NE:ntddrilapitypes.RILMSGINSTATUSTGTDLVSTATUS
title: RILMSGINSTATUSTGTDLVSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsginstatustgtdlvstatus.htm
old-project: netvista
ms.assetid: 6e22ae6d-55a2-4aa7-993b-67474acc6f7b
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: RILMSGINSTATUSTGTDLVSTATUS, RILMSGINSTATUSTGTDLVSTATUS enumeration [Network Drivers Starting with Windows Vista], RIL_MSGDLVSTATUS_CONGESTION, RIL_MSGDLVSTATUS_CONGESTION_TRYING, RIL_MSGDLVSTATUS_CONNECTIONREJECTED, RIL_MSGDLVSTATUS_DELETEDBYORIGSME, RIL_MSGDLVSTATUS_DELETEDBYSC, RIL_MSGDLVSTATUS_FORWARDEDTOSME, RIL_MSGDLVSTATUS_INCOMPATIBLEDEST, RIL_MSGDLVSTATUS_MAX, RIL_MSGDLVSTATUS_NOINTERNETWORKING, RIL_MSGDLVSTATUS_NOLONGEREXISTS, RIL_MSGDLVSTATUS_NOTOBTAINABLE, RIL_MSGDLVSTATUS_QUALITYUNAVAIL, RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TEMP, RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TRYING, RIL_MSGDLVSTATUS_REMOTEPROCERROR, RIL_MSGDLVSTATUS_REPLACEDBYSC, RIL_MSGDLVSTATUS_RESERVED_COMPLETED, RIL_MSGDLVSTATUS_RESERVED_ERROR, RIL_MSGDLVSTATUS_RESERVED_TMPERROR, RIL_MSGDLVSTATUS_RESERVED_TRYING, RIL_MSGDLVSTATUS_SCSPECIFIC_COMPLETED, RIL_MSGDLVSTATUS_SCSPECIFIC_ERROR, RIL_MSGDLVSTATUS_SCSPECIFIC_TMPERROR, RIL_MSGDLVSTATUS_SCSPECIFIC_TRYING, RIL_MSGDLVSTATUS_SMEBUSY, RIL_MSGDLVSTATUS_SMEBUSY_TRYING, RIL_MSGDLVSTATUS_SMEERROR, RIL_MSGDLVSTATUS_SMEERROR_TRYING, RIL_MSGDLVSTATUS_SMENOTRESPONDING, RIL_MSGDLVSTATUS_SMENOTRESPONDING_TRYING, RIL_MSGDLVSTATUS_SVCREJECTED, RIL_MSGDLVSTATUS_SVCREJECTED_TRYING, RIL_MSGDLVSTATUS_VPEXPIRED, netvista.rilmsginstatustgtdlvstatus, ntddrilapitypes/RILMSGINSTATUSTGTDLVSTATUS, ntddrilapitypes/RIL_MSGDLVSTATUS_CONGESTION, ntddrilapitypes/RIL_MSGDLVSTATUS_CONGESTION_TRYING, ntddrilapitypes/RIL_MSGDLVSTATUS_CONNECTIONREJECTED, ntddrilapitypes/RIL_MSGDLVSTATUS_DELETEDBYORIGSME, ntddrilapitypes/RIL_MSGDLVSTATUS_DELETEDBYSC, ntddrilapitypes/RIL_MSGDLVSTATUS_FORWARDEDTOSME, ntddrilapitypes/RIL_MSGDLVSTATUS_INCOMPATIBLEDEST, ntddrilapitypes/RIL_MSGDLVSTATUS_MAX, ntddrilapitypes/RIL_MSGDLVSTATUS_NOINTERNETWORKING, ntddrilapitypes/RIL_MSGDLVSTATUS_NOLONGEREXISTS, ntddrilapitypes/RIL_MSGDLVSTATUS_NOTOBTAINABLE, ntddrilapitypes/RIL_MSGDLVSTATUS_QUALITYUNAVAIL, ntddrilapitypes/RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TEMP, ntddrilapitypes/RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TRYING, ntddrilapitypes/RIL_MSGDLVSTATUS_REMOTEPROCERROR, ntddrilapitypes/RIL_MSGDLVSTATUS_REPLACEDBYSC, ntddrilapitypes/RIL_MSGDLVSTATUS_RESERVED_COMPLETED, ntddrilapitypes/RIL_MSGDLVSTATUS_RESERVED_ERROR, ntddrilapitypes/RIL_MSGDLVSTATUS_RESERVED_TMPERROR, ntddrilapitypes/RIL_MSGDLVSTATUS_RESERVED_TRYING, ntddrilapitypes/RIL_MSGDLVSTATUS_SCSPECIFIC_COMPLETED, ntddrilapitypes/RIL_MSGDLVSTATUS_SCSPECIFIC_ERROR, ntddrilapitypes/RIL_MSGDLVSTATUS_SCSPECIFIC_TMPERROR, ntddrilapitypes/RIL_MSGDLVSTATUS_SCSPECIFIC_TRYING, ntddrilapitypes/RIL_MSGDLVSTATUS_SMEBUSY, ntddrilapitypes/RIL_MSGDLVSTATUS_SMEBUSY_TRYING, ntddrilapitypes/RIL_MSGDLVSTATUS_SMEERROR, ntddrilapitypes/RIL_MSGDLVSTATUS_SMEERROR_TRYING, ntddrilapitypes/RIL_MSGDLVSTATUS_SMENOTRESPONDING, ntddrilapitypes/RIL_MSGDLVSTATUS_SMENOTRESPONDING_TRYING, ntddrilapitypes/RIL_MSGDLVSTATUS_SVCREJECTED, ntddrilapitypes/RIL_MSGDLVSTATUS_SVCREJECTED_TRYING, ntddrilapitypes/RIL_MSGDLVSTATUS_VPEXPIRED
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddrilapitypes.h
api_name:
-	RILMSGINSTATUSTGTDLVSTATUS
product: Windows
targetos: Windows
req.typenames: RILMSGINSTATUSTGTDLVSTATUS
---

# RILMSGINSTATUSTGTDLVSTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGINSTATUSTGTDLVSTATUS { 
  RIL_MSGDLVSTATUS_FORWARDEDTOSME,
  RIL_MSGDLVSTATUS_REPLACEDBYSC,
  RIL_MSGDLVSTATUS_CONGESTION_TRYING,
  RIL_MSGDLVSTATUS_SMEBUSY_TRYING,
  RIL_MSGDLVSTATUS_SMENOTRESPONDING_TRYING,
  RIL_MSGDLVSTATUS_SVCREJECTED_TRYING,
  RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TRYING,
  RIL_MSGDLVSTATUS_SMEERROR_TRYING,
  RIL_MSGDLVSTATUS_CONGESTION,
  RIL_MSGDLVSTATUS_SMEBUSY,
  RIL_MSGDLVSTATUS_SMENOTRESPONDING,
  RIL_MSGDLVSTATUS_SVCREJECTED,
  RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TEMP,
  RIL_MSGDLVSTATUS_SMEERROR,
  RIL_MSGDLVSTATUS_REMOTEPROCERROR,
  RIL_MSGDLVSTATUS_INCOMPATIBLEDEST,
  RIL_MSGDLVSTATUS_CONNECTIONREJECTED,
  RIL_MSGDLVSTATUS_NOTOBTAINABLE,
  RIL_MSGDLVSTATUS_NOINTERNETWORKING,
  RIL_MSGDLVSTATUS_VPEXPIRED,
  RIL_MSGDLVSTATUS_DELETEDBYORIGSME,
  RIL_MSGDLVSTATUS_DELETEDBYSC,
  RIL_MSGDLVSTATUS_NOLONGEREXISTS,
  RIL_MSGDLVSTATUS_QUALITYUNAVAIL,
  RIL_MSGDLVSTATUS_RESERVED_COMPLETED,
  RIL_MSGDLVSTATUS_RESERVED_TRYING,
  RIL_MSGDLVSTATUS_RESERVED_ERROR,
  RIL_MSGDLVSTATUS_RESERVED_TMPERROR,
  RIL_MSGDLVSTATUS_SCSPECIFIC_COMPLETED,
  RIL_MSGDLVSTATUS_SCSPECIFIC_TRYING,
  RIL_MSGDLVSTATUS_SCSPECIFIC_ERROR,
  RIL_MSGDLVSTATUS_SCSPECIFIC_TMPERROR,
  RIL_MSGDLVSTATUS_MAX
} RILMSGINSTATUSTGTDLVSTATUS;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_CONGESTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_CONGESTION_TRYING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_CONNECTIONREJECTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_DELETEDBYORIGSME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_DELETEDBYSC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_FORWARDEDTOSME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_INCOMPATIBLEDEST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_NOINTERNETWORKING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_NOLONGEREXISTS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_NOTOBTAINABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_QUALITYUNAVAIL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TEMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TRYING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_RECEIVEDBYSME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_REMOTEPROCERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_REPLACEDBYSC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_RESERVED_COMPLETED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_RESERVED_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_RESERVED_TMPERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_RESERVED_TRYING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SCSPECIFIC_COMPLETED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SCSPECIFIC_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SCSPECIFIC_TMPERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SCSPECIFIC_TRYING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SMEBUSY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SMEBUSY_TRYING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SMEERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SMEERROR_TRYING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SMENOTRESPONDING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SMENOTRESPONDING_TRYING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SVCREJECTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_SVCREJECTED_TRYING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDLVSTATUS_VPEXPIRED</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |