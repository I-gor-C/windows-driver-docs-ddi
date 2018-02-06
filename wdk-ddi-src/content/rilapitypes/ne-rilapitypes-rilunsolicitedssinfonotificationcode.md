---
UID: NE:rilapitypes.RILUNSOLICITEDSSINFONOTIFICATIONCODE
title: RILUNSOLICITEDSSINFONOTIFICATIONCODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilunsolicitedssinfonotificationcode_2.htm
old-project: netvista
ms.assetid: 3747f429-9893-44bd-ab3c-c3e78d8a264c
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER, RIL_UNSSSCODE_ENTEREDMULTIPARTY, rilapitypes/RIL_UNSSSCODE_HELDCALLRELEASED, rilapitypes/RIL_UNSSSCODE_CUGCALL, RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE, RIL_UNSSSCODE_CALLISWAITING, RILUNSOLICITEDSSINFONOTIFICATIONCODE, RIL_UNSSSCODE_OUTGOINGCALLSBARRED, rilapitypes/RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER, RIL_UNSSSCODE_CALLRETRIEVED, rilapitypes/RIL_UNSSSCODE_INCOMINGCALLSBARRED, rilapitypes/RIL_UNSSSCODE_MAX, rilapitypes/RIL_UNSSSCODE_CALLWASFORWARDED, RIL_UNSSSCODE_CALLWASFORWARDED, RIL_UNSSSCODE_CUGCALL, RILUNSOLICITEDSSINFONOTIFICATIONCODE enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_UNSSSCODE_CALLRETRIEVED, RIL_UNSSSCODE_FORWARDCHECKSS, rilapitypes/RIL_UNSSSCODE_FORWARDCHECKSS, rilapitypes/RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER, RIL_UNSSSCODE_UNCONDITIONALCFACTIVE, rilapitypes/RIL_UNSSSCODE_ENTEREDMULTIPARTY, RIL_UNSSSCODE_DEFLECTEDCALL, rilapitypes/RIL_UNSSSCODE_CALLISWAITING, rilapitypes/RIL_UNSSSCODE_DEFLECTEDCALL, rilapitypes/RIL_UNSSSCODE_ADDITIONALINCOMINGCF, netvista.rilunsolicitedssinfonotificationcode_2, RIL_UNSSSCODE_INCOMINGCALLSBARRED, rilapitypes/RIL_UNSSSCODE_UNCONDITIONALCFACTIVE, RIL_UNSSSCODE_HELDCALLRELEASED, rilapitypes/RIL_UNSSSCODE_OUTGOINGCALLSBARRED, rilapitypes/RIL_UNSSSCODE_CALLPUTONHOLD, rilapitypes/RILUNSOLICITEDSSINFONOTIFICATIONCODE, RIL_UNSSSCODE_CALLPUTONHOLD, rilapitypes/RIL_UNSSSCODE_CLIRSUPPRESSREJECT, RIL_UNSSSCODE_ADDITIONALINCOMINGCF, RIL_UNSSSCODE_CLIRSUPPRESSREJECT, RIL_UNSSSCODE_MAX, RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER, rilapitypes/RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE
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
-	RILUNSOLICITEDSSINFONOTIFICATIONCODE
product: Windows
targetos: Windows
req.typenames: RILUNSOLICITEDSSINFONOTIFICATIONCODE
req.product: Windows 10 or later.
---

# RILUNSOLICITEDSSINFONOTIFICATIONCODE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUNSOLICITEDSSINFONOTIFICATIONCODE { 
  RIL_UNSSSCODE_CUGCALL,
  RIL_UNSSSCODE_CALLPUTONHOLD,
  RIL_UNSSSCODE_CALLRETRIEVED,
  RIL_UNSSSCODE_ENTEREDMULTIPARTY,
  RIL_UNSSSCODE_HELDCALLRELEASED,
  RIL_UNSSSCODE_FORWARDCHECKSS,
  RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER,
  RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER,
  RIL_UNSSSCODE_DEFLECTEDCALL,
  RIL_UNSSSCODE_ADDITIONALINCOMINGCF,
  RIL_UNSSSCODE_UNCONDITIONALCFACTIVE,
  RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE,
  RIL_UNSSSCODE_CALLWASFORWARDED,
  RIL_UNSSSCODE_CALLISWAITING,
  RIL_UNSSSCODE_OUTGOINGCALLSBARRED,
  RIL_UNSSSCODE_INCOMINGCALLSBARRED,
  RIL_UNSSSCODE_CLIRSUPPRESSREJECT,
  RIL_UNSSSCODE_MAX
} RILUNSOLICITEDSSINFONOTIFICATIONCODE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_UNSSSCODE_ADDITIONALINCOMINGCF</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_ALERTINGEXPLICITCALLXFER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CALLISWAITING</td>
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
                    <td>RIL_UNSSSCODE_CALLWASFORWARDED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CLIRSUPPRESSREJECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CONNECTEDEXPLICITCALLXFER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_CUGCALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_DEFLECTEDCALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_ENTEREDMULTIPARTY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_FORWARDCHECKSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_FORWARDEDCALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_HELDCALLRELEASED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_INCOMINGCALLSBARRED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_OUTGOINGCALLSBARRED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_SOMECONDITIONALCFACTIVE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UNSSSCODE_UNCONDITIONALCFACTIVE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |