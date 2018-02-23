---
UID: NE:ntddrilapitypes.RILUICCSERVICESERVICE
title: RILUICCSERVICESERVICE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccserviceservice.htm
old-project: netvista
ms.assetid: 1aeb4642-d718-4e39-a6c7-dc33146c9687
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: ntddrilapitypes/RIL_UICCOPERATION_SERVICE_BDN, RIL_UICCOPERATION_SERVICE_BDN, RILUICCSERVICESERVICE enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RILUICCSERVICESERVICE, netvista.riluiccserviceservice, ntddrilapitypes/RIL_UICCOPERATION_SERVICE_MAX, RILUICCSERVICESERVICE, ntddrilapitypes/RIL_UICCOPERATION_SERVICE_ACL, RIL_UICCOPERATION_SERVICE_ACL, RIL_UICCOPERATION_SERVICE_MAX
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
-	RILUICCSERVICESERVICE
product: Windows
targetos: Windows
req.typenames: RILUICCSERVICESERVICE
---

# RILUICCSERVICESERVICE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUICCSERVICESERVICE { 
  RIL_UICCOPERATION_SERVICE_BDN,
  RIL_UICCOPERATION_SERVICE_ACL,
  RIL_UICCOPERATION_SERVICE_MAX
} RILUICCSERVICESERVICE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_UICCOPERATION_SERVICE_ACL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCOPERATION_SERVICE_BDN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCOPERATION_SERVICE_FDN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCOPERATION_SERVICE_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |