---
UID: NE:wwan._WWAN_UICCSLOT_STATE
title: "_WWAN_UICCSLOT_STATE"
author: windows-driver-content
description: The WWAN_UICCSLOT_STATE enumeration lists the different states of a UICC (SIM) card slot on a modem. The slot state represents a summary of both the slot state and the card state.
old-location: netvista\wwan_uiccslot_state.htm
old-project: netvista
ms.assetid: 63A3C2AA-6EBF-469D-933A-C51F5EC31C47
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_UICCSLOT_STATE, UICCSlotStateActive, UICCSlotStateEmpty, UICCSlotStateError, UICCSlotStateNotReady, UICCSlotStateOff, UICCSlotStateOffEmpty, UICCSlotStateUnknown, WWAN_UICCSLOT_STATE, WWAN_UICCSLOT_STATE enumeration [Network Drivers Starting with Windows Vista], _WWAN_UICCSLOT_STATE, netvista.wwan_uiccslot_state, wwan/UICCSlotStateActive, wwan/UICCSlotStateEmpty, wwan/UICCSlotStateError, wwan/UICCSlotStateNotReady, wwan/UICCSlotStateOff, wwan/UICCSlotStateOffEmpty, wwan/UICCSlotStateUnknown, wwan/WWAN_UICCSLOT_STATE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
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
-	wwan.h
api_name:
-	WWAN_UICCSLOT_STATE
product: Windows
targetos: Windows
req.typenames: WWAN_UICCSLOT_STATE, *PWWAN_UICCSLOT_STATE
req.product: Windows 10 or later.
---

# _WWAN_UICCSLOT_STATE Enumeration
The <b>WWAN_UICCSLOT_STATE</b> enumeration lists the different states of a UICC (SIM) card slot on a modem. The slot state represents a summary of both the slot state and the card state.

## Syntax
```
typedef enum _WWAN_UICCSLOT_STATE {
  WwanUiccSlotStateUnknown              ,
  WwanUiccSlotStateOffEmpty             ,
  WwanUiccSlotStateOff                  ,
  WwanUiccSlotStateEmpty                ,
  WwanUiccSlotStateNotReady             ,
  WwanUiccSlotStateActive               ,
  WwanUiccSlotStateError                ,
  WwanUiccSlotStateActiveEsim           ,
  WwanUiccSlotStateActiveEsimNoProfile  ,
  WwanUiccSlotStateMax
} *PWWAN_UICCSLOT_STATE, WWAN_UICCSLOT_STATE;
```

## Constants

<table>
            
                <tr>
                    <td>WwanUiccSlotStateUnknown</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanUiccSlotStateOffEmpty</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanUiccSlotStateOff</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanUiccSlotStateEmpty</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanUiccSlotStateNotReady</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanUiccSlotStateActive</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanUiccSlotStateError</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanUiccSlotStateActiveEsim</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanUiccSlotStateActiveEsimNoProfile</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>WwanUiccSlotStateMax</td>
                    <td></td>
                </tr>
</table>

## Remarks

The set of reported states is constrained by the capability of the slot hardware. In the most restrictive case, the slot hardware may only be able to determine that a card is present when it is powered on and active; in such a case the <b>OffEmpty</b> and <b>Off</b> states will not be reported.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1703 Windows 10, version 1703 |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/F45D253E-E7D7-4600-AF8C-6D4EB096030D">WWAN_SLOT_INFO</a>