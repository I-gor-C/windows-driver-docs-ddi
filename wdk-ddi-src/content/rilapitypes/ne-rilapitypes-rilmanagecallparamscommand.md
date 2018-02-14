---
UID: NE:rilapitypes.RILMANAGECALLPARAMSCOMMAND
title: RILMANAGECALLPARAMSCOMMAND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmanagecallparamscommand_2.htm
old-project: netvista
ms.assetid: 0749f3fb-261c-4b98-961f-f2720100b8e6
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: rilapitypes/RIL_CALLCMD_HOLDALLBUTONE, RILMANAGECALLPARAMSCOMMAND, RIL_CALLCMD_BLINDCALLTRANSFER, rilapitypes/RIL_CALLCMD_BLINDCALLTRANSFER, RIL_CALLCMD_RELEASEPROCEEDING, RILMANAGECALLPARAMSCOMMAND enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_CALLCMD_RTT, rilapitypes/RIL_CALLCMD_MAX, RIL_CALLCMD_ACCEPTINCOMINGCALL, rilapitypes/RIL_CALLCMD_ACCEPTINCOMINGCALL, RIL_CALLCMD_CONSULTATIVECALLTRANSFER, rilapitypes/RIL_CALLCMD_RELEASEPROCEEDING, RIL_CALLCMD_ASSUREDCALLTRANSFER, RIL_CALLCMD_RTT, RIL_CALLCMD_RELEASEALLCALLS, rilapitypes/RILMANAGECALLPARAMSCOMMAND, rilapitypes/RIL_CALLCMD_ADDHELDTOCONF, RIL_CALLCMD_HOLDACTIVE_ACCEPTHELD, rilapitypes/RIL_CALLCMD_RELEASECALL, netvista.rilmanagecallparamscommand_2, rilapitypes/RIL_CALLCMD_RELEASEALLCALLS, RIL_CALLCMD_RELEASECALL, rilapitypes/RIL_CALLCMD_HOLDACTIVE_ACCEPTHELD, RIL_CALLCMD_ADDHELDTOCONF, rilapitypes/RIL_CALLCMD_ADDHELDTOCONF_DISCONNECT, RIL_CALLCMD_RELEASEHELDCONFCALL, RIL_CALLCMD_MAX, rilapitypes/RIL_CALLCMD_OFFERMEDIA, RIL_CALLCMD_ADDHELDTOCONF_DISCONNECT, rilapitypes/RIL_CALLCMD_RELEASEHELDCONFCALL, RIL_CALLCMD_OFFERMEDIA, rilapitypes/RIL_CALLCMD_CONSULTATIVECALLTRANSFER, RIL_CALLCMD_HOLDALLBUTONE, RIL_CALLCMD_ANSWERMEDIAOFFER, rilapitypes/RIL_CALLCMD_ANSWERMEDIAOFFER, rilapitypes/RIL_CALLCMD_ASSUREDCALLTRANSFER
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
-	RILMANAGECALLPARAMSCOMMAND
product: Windows
targetos: Windows
req.typenames: RILMANAGECALLPARAMSCOMMAND
req.product: Windows 10 or later.
---

# RILMANAGECALLPARAMSCOMMAND Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMANAGECALLPARAMSCOMMAND { 
  RIL_CALLCMD_RELEASECALL,
  RIL_CALLCMD_HOLDACTIVE_ACCEPTHELD,
  RIL_CALLCMD_HOLDALLBUTONE,
  RIL_CALLCMD_ADDHELDTOCONF,
  RIL_CALLCMD_ADDHELDTOCONF_DISCONNECT,
  RIL_CALLCMD_RELEASEPROCEEDING,
  RIL_CALLCMD_RELEASEALLCALLS,
  RIL_CALLCMD_RELEASEHELDCONFCALL,
  RIL_CALLCMD_ACCEPTINCOMINGCALL,
  RIL_CALLCMD_OFFERMEDIA,
  RIL_CALLCMD_ANSWERMEDIAOFFER,
  RIL_CALLCMD_BLINDCALLTRANSFER,
  RIL_CALLCMD_ASSUREDCALLTRANSFER,
  RIL_CALLCMD_CONSULTATIVECALLTRANSFER,
  RIL_CALLCMD_RTT,
  RIL_CALLCMD_MAX
} RILMANAGECALLPARAMSCOMMAND;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_CALLCMD_ACCEPTINCOMINGCALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_ADDHELDTOCONF</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_ADDHELDTOCONF_DISCONNECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_ANSWERMEDIAOFFER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_ASSUREDCALLTRANSFER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_BLINDCALLTRANSFER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_CONSULTATIVECALLTRANSFER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_HOLDACTIVE_ACCEPTHELD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_HOLDALLBUTONE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_OFFERMEDIA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_RELEASEACTIVE_ACCEPTHELD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_RELEASEALLCALLS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_RELEASECALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_RELEASEHELDCONFCALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_RELEASEPROCEEDING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLCMD_RTT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |