---
UID: NE:rilapitypes.RILUNSOLICITEDSSINFONOTIFICATIONCODE
title: RILUNSOLICITEDSSINFONOTIFICATIONCODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilunsolicitedssinfonotificationcode.htm
old-project: netvista
ms.assetid: 03dd4659-29fc-4426-8d30-2bbc0b71f899
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILUNSOLICITEDSSINFONOTIFICATIONCODE, RILUNSOLICITEDSSINFONOTIFICATIONCODE enumeration [Network Drivers Starting with Windows Vista], RIL_UNSSSCODE_ADDITIONALINCOMINGCF, RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER, RIL_UNSSSCODE_CALLISWAITING, RIL_UNSSSCODE_CALLPUTONHOLD, RIL_UNSSSCODE_CALLRETRIEVED, RIL_UNSSSCODE_CALLWASFORWARDED, RIL_UNSSSCODE_CLIRSUPPRESSREJECT, RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER, RIL_UNSSSCODE_CUGCALL, RIL_UNSSSCODE_DEFLECTEDCALL, RIL_UNSSSCODE_ENTEREDMULTIPARTY, RIL_UNSSSCODE_FORWARDCHECKSS, RIL_UNSSSCODE_HELDCALLRELEASED, RIL_UNSSSCODE_INCOMINGCALLSBARRED, RIL_UNSSSCODE_MAX, RIL_UNSSSCODE_OUTGOINGCALLSBARRED, RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE, RIL_UNSSSCODE_UNCONDITIONALCFACTIVE, netvista.rilunsolicitedssinfonotificationcode, ntddrilapitypes/RILUNSOLICITEDSSINFONOTIFICATIONCODE, ntddrilapitypes/RIL_UNSSSCODE_ADDITIONALINCOMINGCF, ntddrilapitypes/RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER, ntddrilapitypes/RIL_UNSSSCODE_CALLISWAITING, ntddrilapitypes/RIL_UNSSSCODE_CALLPUTONHOLD, ntddrilapitypes/RIL_UNSSSCODE_CALLRETRIEVED, ntddrilapitypes/RIL_UNSSSCODE_CALLWASFORWARDED, ntddrilapitypes/RIL_UNSSSCODE_CLIRSUPPRESSREJECT, ntddrilapitypes/RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER, ntddrilapitypes/RIL_UNSSSCODE_CUGCALL, ntddrilapitypes/RIL_UNSSSCODE_DEFLECTEDCALL, ntddrilapitypes/RIL_UNSSSCODE_ENTEREDMULTIPARTY, ntddrilapitypes/RIL_UNSSSCODE_FORWARDCHECKSS, ntddrilapitypes/RIL_UNSSSCODE_HELDCALLRELEASED, ntddrilapitypes/RIL_UNSSSCODE_INCOMINGCALLSBARRED, ntddrilapitypes/RIL_UNSSSCODE_MAX, ntddrilapitypes/RIL_UNSSSCODE_OUTGOINGCALLSBARRED, ntddrilapitypes/RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE, ntddrilapitypes/RIL_UNSSSCODE_UNCONDITIONALCFACTIVE
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
-	RILUNSOLICITEDSSINFONOTIFICATIONCODE
product: Windows
targetos: Windows
req.typenames: RILUNSOLICITEDSSINFONOTIFICATIONCODE
req.product: Windows 10 or later.
---

# RILUNSOLICITEDSSINFONOTIFICATIONCODE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILUNSOLICITEDSSINFONOTIFICATIONCODE {
  RIL_UNSSSCODE_FORWARDEDCALL              ,
  RIL_UNSSSCODE_CUGCALL                    ,
  RIL_UNSSSCODE_CALLPUTONHOLD              ,
  RIL_UNSSSCODE_CALLRETRIEVED              ,
  RIL_UNSSSCODE_ENTEREDMULTIPARTY          ,
  RIL_UNSSSCODE_HELDCALLRELEASED           ,
  RIL_UNSSSCODE_FORWARDCHECKSS             ,
  RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER   ,
  RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER  ,
  RIL_UNSSSCODE_DEFLECTEDCALL              ,
  RIL_UNSSSCODE_ADDITIONALINCOMINGCF       ,
  RIL_UNSSSCODE_UNCONDITIONALCFACTIVE      ,
  RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE    ,
  RIL_UNSSSCODE_CALLWASFORWARDED           ,
  RIL_UNSSSCODE_CALLISWAITING              ,
  RIL_UNSSSCODE_OUTGOINGCALLSBARRED        ,
  RIL_UNSSSCODE_INCOMINGCALLSBARRED        ,
  RIL_UNSSSCODE_CLIRSUPPRESSREJECT         ,
  RIL_UNSSSCODE_MAX
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_UNSSSCODE_FORWARDEDCALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CUGCALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CALLPUTONHOLD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CALLRETRIEVED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_ENTEREDMULTIPARTY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_HELDCALLRELEASED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_FORWARDCHECKSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_DEFLECTEDCALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_ADDITIONALINCOMINGCF</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_UNCONDITIONALCFACTIVE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CALLWASFORWARDED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CALLISWAITING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_OUTGOINGCALLSBARRED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_INCOMINGCALLSBARRED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CLIRSUPPRESSREJECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |