---
UID: NE:ntddrilapitypes.RILUICCFILELOCKSTATUSACCESSCONDITION
title: RILUICCFILELOCKSTATUSACCESSCONDITION
author: windows-driver-content
description: This enumeration describes the RILUICCFILELOCKSTATUSACCESSCONDITION.
old-location: netvista\riluiccfilelockstatusaccesscondition.htm
old-project: netvista
ms.assetid: 994bfab2-6bab-4aeb-87a9-a5b825efcb23
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RILUICCFILELOCKSTATUSACCESSCONDITION, RILUICCFILELOCKSTATUSACCESSCONDITION enumeration [Network Drivers Starting with Windows Vista], RIL_UICCFILEACCESSCONDITION_ADM5, RIL_UICCFILEACCESSCONDITION_ADM6, RIL_UICCFILEACCESSCONDITION_ALW, RIL_UICCFILEACCESSCONDITION_NEV, RIL_UICCFILEACCESSCONDITION_PIN1, RIL_UICCFILEACCESSCONDITION_PIN2, RIL_UICCFILEACCESSCONDITION_RFU3, RIL_UICCFILEACCESSCONDITION_RFU4, netvista.riluiccfilelockstatusaccesscondition, rilapitypes/RILUICCFILELOCKSTATUSACCESSCONDITION, rilapitypes/RIL_UICCFILEACCESSCONDITION_ADM5, rilapitypes/RIL_UICCFILEACCESSCONDITION_ADM6, rilapitypes/RIL_UICCFILEACCESSCONDITION_ALW, rilapitypes/RIL_UICCFILEACCESSCONDITION_NEV, rilapitypes/RIL_UICCFILEACCESSCONDITION_PIN1, rilapitypes/RIL_UICCFILEACCESSCONDITION_PIN2, rilapitypes/RIL_UICCFILEACCESSCONDITION_RFU3, rilapitypes/RIL_UICCFILEACCESSCONDITION_RFU4
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
-	RILUICCFILELOCKSTATUSACCESSCONDITION
product:
- Windows
targetos: Windows
req.typenames: RILUICCFILELOCKSTATUSACCESSCONDITION
---

# RILUICCFILELOCKSTATUSACCESSCONDITION Enumeration
<div class="alert"><b>Warning</b>  The Cellular COM API is deprecated in Windows 10. This content is provided to support maintenance of OEM and mobile operator created Windows Phone 8.1 applications.</div><div> </div>This enumeration describes the RILUICCFILELOCKSTATUSACCESSCONDITION.

## Syntax
````
enum RILUICCFILELOCKSTATUSACCESSCONDITION {
  RIL_UICCFILEACCESSCONDITION_ALW   = 0x00, 
  RIL_UICCFILEACCESSCONDITION_PIN1  = 0x01, 
  RIL_UICCFILEACCESSCONDITION_PIN2  = 0x02, 
  RIL_UICCFILEACCESSCONDITION_RFU3  = 0x03, 
  RIL_UICCFILEACCESSCONDITION_RFU4  = 0x04, 
  RIL_UICCFILEACCESSCONDITION_ADM5  = 0x05, 
  RIL_UICCFILEACCESSCONDITION_ADM6  = 0x06, 
  RIL_UICCFILEACCESSCONDITION_NEV   = 0x07 

};
````

## Constants

<table>
            
                <tr>
                    <td>RIL_UICCFILEACCESSCONDITION_ALW</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCFILEACCESSCONDITION_PIN1</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCFILEACCESSCONDITION_PIN2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCFILEACCESSCONDITION_RFU3</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCFILEACCESSCONDITION_RFU4</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCFILEACCESSCONDITION_ADM5</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCFILEACCESSCONDITION_ADM6</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCFILEACCESSCONDITION_NEV</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_UICCFILEACCESSCONDITION_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h, Ntddrilapitypes.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn946509">Cellular COM enumerations</a>