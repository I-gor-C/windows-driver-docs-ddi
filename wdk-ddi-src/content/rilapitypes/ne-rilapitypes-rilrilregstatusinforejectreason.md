---
UID: NE:rilapitypes.RILRILREGSTATUSINFOREJECTREASON
title: RILRILREGSTATUSINFOREJECTREASON
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilrilregstatusinforejectreason.htm
old-project: netvista
ms.assetid: 17aad504-4223-4764-8a24-536a81807650
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILRILREGSTATUSINFOREJECTREASON, RILRILREGSTATUSINFOREJECTREASON enumeration [Network Drivers Starting with Windows Vista], RIL_REGREJECTREASON_CONGESTION, RIL_REGREJECTREASON_CSG_NOTAUTHORIZED, RIL_REGREJECTREASON_GSMAUTH_NOTACCEPTED, RIL_REGREJECTREASON_ILLEGAL_ME, RIL_REGREJECTREASON_ILLEGAL_MS, RIL_REGREJECTREASON_IMSIUNK_HLR, RIL_REGREJECTREASON_IMSIUNK_VLR, RIL_REGREJECTREASON_IMSI_NOTACCEPTED, RIL_REGREJECTREASON_LOCAREA_NOTALLOWED, RIL_REGREJECTREASON_MACFAILURE, RIL_REGREJECTREASON_NETWORKFAILURE, RIL_REGREJECTREASON_NOSUITABLECELL, RIL_REGREJECTREASON_PLMN_NOTALLOWED, RIL_REGREJECTREASON_REQSVCOPT_NOTSUBSCRIBED, RIL_REGREJECTREASON_ROAMING_NOTALLOWED, RIL_REGREJECTREASON_SVCOPT_NOTSUPPORTED, RIL_REGREJECTREASON_SVCOPT_OUTOFORDER, RIL_REGREJECTREASON_SYNCHFAILURE, netvista.rilrilregstatusinforejectreason, ntddrilapitypes/RILRILREGSTATUSINFOREJECTREASON, ntddrilapitypes/RIL_REGREJECTREASON_CONGESTION, ntddrilapitypes/RIL_REGREJECTREASON_CSG_NOTAUTHORIZED, ntddrilapitypes/RIL_REGREJECTREASON_GSMAUTH_NOTACCEPTED, ntddrilapitypes/RIL_REGREJECTREASON_ILLEGAL_ME, ntddrilapitypes/RIL_REGREJECTREASON_ILLEGAL_MS, ntddrilapitypes/RIL_REGREJECTREASON_IMSIUNK_HLR, ntddrilapitypes/RIL_REGREJECTREASON_IMSIUNK_VLR, ntddrilapitypes/RIL_REGREJECTREASON_IMSI_NOTACCEPTED, ntddrilapitypes/RIL_REGREJECTREASON_LOCAREA_NOTALLOWED, ntddrilapitypes/RIL_REGREJECTREASON_MACFAILURE, ntddrilapitypes/RIL_REGREJECTREASON_NETWORKFAILURE, ntddrilapitypes/RIL_REGREJECTREASON_NOSUITABLECELL, ntddrilapitypes/RIL_REGREJECTREASON_PLMN_NOTALLOWED, ntddrilapitypes/RIL_REGREJECTREASON_REQSVCOPT_NOTSUBSCRIBED, ntddrilapitypes/RIL_REGREJECTREASON_ROAMING_NOTALLOWED, ntddrilapitypes/RIL_REGREJECTREASON_SVCOPT_NOTSUPPORTED, ntddrilapitypes/RIL_REGREJECTREASON_SVCOPT_OUTOFORDER, ntddrilapitypes/RIL_REGREJECTREASON_SYNCHFAILURE
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
-	RILRILREGSTATUSINFOREJECTREASON
product:
- Windows
targetos: Windows
req.typenames: RILRILREGSTATUSINFOREJECTREASON
req.product: Windows 10 or later.
---

# RILRILREGSTATUSINFOREJECTREASON Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILRILREGSTATUSINFOREJECTREASON {
  RIL_REGREJECTREASON_NULL                     ,
  RIL_REGREJECTREASON_IMSIUNK_HLR              ,
  RIL_REGREJECTREASON_ILLEGAL_MS               ,
  RIL_REGREJECTREASON_IMSIUNK_VLR              ,
  RIL_REGREJECTREASON_IMSI_NOTACCEPTED         ,
  RIL_REGREJECTREASON_ILLEGAL_ME               ,
  RIL_REGREJECTREASON_PLMN_NOTALLOWED          ,
  RIL_REGREJECTREASON_LOCAREA_NOTALLOWED       ,
  RIL_REGREJECTREASON_ROAMING_NOTALLOWED       ,
  RIL_REGREJECTREASON_NOSUITABLECELL           ,
  RIL_REGREJECTREASON_NETWORKFAILURE           ,
  RIL_REGREJECTREASON_MACFAILURE               ,
  RIL_REGREJECTREASON_SYNCHFAILURE             ,
  RIL_REGREJECTREASON_CONGESTION               ,
  RIL_REGREJECTREASON_GSMAUTH_NOTACCEPTED      ,
  RIL_REGREJECTREASON_CSG_NOTAUTHORIZED        ,
  RIL_REGREJECTREASON_SVCOPT_NOTSUPPORTED      ,
  RIL_REGREJECTREASON_REQSVCOPT_NOTSUBSCRIBED  ,
  RIL_REGREJECTREASON_SVCOPT_OUTOFORDER
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_REGREJECTREASON_NULL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_IMSIUNK_HLR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_ILLEGAL_MS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_IMSIUNK_VLR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_IMSI_NOTACCEPTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_ILLEGAL_ME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_PLMN_NOTALLOWED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_LOCAREA_NOTALLOWED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_ROAMING_NOTALLOWED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_NOSUITABLECELL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_NETWORKFAILURE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_MACFAILURE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_SYNCHFAILURE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_CONGESTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_GSMAUTH_NOTACCEPTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_CSG_NOTAUTHORIZED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_SVCOPT_NOTSUPPORTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_REQSVCOPT_NOTSUBSCRIBED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REGREJECTREASON_SVCOPT_OUTOFORDER</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |