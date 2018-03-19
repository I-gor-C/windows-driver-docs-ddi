---
UID: NE:ntddrilapitypes.RILUICCLOCKSTATEPARAMMASK
title: RILUICCLOCKSTATEPARAMMASK
author: windows-driver-content
description: This enumeration describes the RILUICCLOCKSTATEPARAMMASK.
old-location: netvista\riluicclockstateparammask.htm
old-project: netvista
ms.assetid: 19366fbe-8a04-4a9f-9acc-8de0211e6e0d
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RILUICCLOCKSTATEPARAMMASK, RILUICCLOCKSTATEPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_UICCLOCKSTATE_ALL, RIL_PARAM_UICCLOCKSTATE_LOCKSTATE, RIL_PARAM_UICCLOCKSTATE_UICCLOCK, RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT, RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT, netvista.riluicclockstateparammask, rilapitypes/RILUICCLOCKSTATEPARAMMASK, rilapitypes/RIL_PARAM_UICCLOCKSTATE_ALL, rilapitypes/RIL_PARAM_UICCLOCKSTATE_LOCKSTATE, rilapitypes/RIL_PARAM_UICCLOCKSTATE_UICCLOCK, rilapitypes/RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT, rilapitypes/RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: Rilapitypes.h, Ntddrilapitypes.h
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
-	rilapitypes.h
api_name:
-	RILUICCLOCKSTATEPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILUICCLOCKSTATEPARAMMASK
---

# RILUICCLOCKSTATEPARAMMASK Enumeration
<div class="alert"><b>Warning</b>  The Cellular COM API is deprecated in Windows 10. This content is provided to support maintenance of OEM and mobile operator created Windows Phone 8.1 applications.</div><div> </div>This enumeration describes the RILUICCLOCKSTATEPARAMMASK.

## Syntax
````
enum RILUICCLOCKSTATEPARAMMASK {
  RIL_PARAM_UICCLOCKSTATE_UICCLOCK             = 0x00000001, 
  RIL_PARAM_UICCLOCKSTATE_LOCKSTATE            = 0x00000002, 
  RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT   = 0x00000004, 
  RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT  = 0x00000008, 
  RIL_PARAM_UICCLOCKSTATE_ALL                  = 0x0000000F 

};
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_UICCLOCKSTATE_UICCLOCK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_UICCLOCKSTATE_LOCKSTATE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_UICCLOCKSTATE_ALL</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h, Ntddrilapitypes.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn946509">Cellular COM enumerations</a>