---
UID: NE:nfccx._NFC_CX_DRIVER_FLAGS
title: "_NFC_CX_DRIVER_FLAGS"
author: windows-driver-content
description: Specifies run-time driver flags.
old-location: nfpdrivers\nfc_cx_driver_flags.htm
old-project: nfpdrivers
ms.assetid: 161CA2C2-F4F4-49F3-9007-ADFBDA905119
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PNFC_CX_DRIVER_FLAGS, NFC_CX_DRIVER_DISABLE_HOST_CARD_EMULATION, NFC_CX_DRIVER_DISABLE_NFCEE_ACTION_NTF, NFC_CX_DRIVER_DISABLE_NFCEE_DISCOVERY, NFC_CX_DRIVER_DISABLE_RECOVERY_MODE, NFC_CX_DRIVER_DISABLE_WTD_TIMER, NFC_CX_DRIVER_ENABLE_EEPROM_WRITE_PROTECTION, NFC_CX_DRIVER_FLAGS, NFC_CX_DRIVER_HCI_NETWORK_PER_NFCEE, NFC_CX_DRIVER_ISODEP_RNAK_PRESENCE_CHK_SUPPORTED, NFC_CX_DRIVER_RF_ROUTING_POWER_SUB_STATES_SUPPORTED, PNFC_CX_DRIVER_FLAGS, PNFC_CX_DRIVER_FLAGS enumeration pointer [Near-Field Proximity Drivers], _NFC_CX_DRIVER_FLAGS, _NFC_CX_DRIVER_FLAGS enumeration [Near-Field Proximity Drivers], nfccx/NFC_CX_DRIVER_DISABLE_HOST_CARD_EMULATION, nfccx/NFC_CX_DRIVER_DISABLE_NFCEE_ACTION_NTF, nfccx/NFC_CX_DRIVER_DISABLE_NFCEE_DISCOVERY, nfccx/NFC_CX_DRIVER_DISABLE_RECOVERY_MODE, nfccx/NFC_CX_DRIVER_DISABLE_WTD_TIMER, nfccx/NFC_CX_DRIVER_ENABLE_EEPROM_WRITE_PROTECTION, nfccx/NFC_CX_DRIVER_HCI_NETWORK_PER_NFCEE, nfccx/NFC_CX_DRIVER_ISODEP_RNAK_PRESENCE_CHK_SUPPORTED, nfccx/NFC_CX_DRIVER_RF_ROUTING_POWER_SUB_STATES_SUPPORTED, nfccx/PNFC_CX_DRIVER_FLAGS, nfccx/_NFC_CX_DRIVER_FLAGS, nfpdrivers.nfc_cx_driver_flags"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: nfccx.h
req.include-header: Ncidef.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
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
req.irql: Requires same
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	nfccx.h
api_name:
-	NFC_CX_DRIVER_FLAGS
product: Windows
targetos: Windows
req.typenames: NFC_CX_DRIVER_FLAGS, *PNFC_CX_DRIVER_FLAGS
---

# _NFC_CX_DRIVER_FLAGS Enumeration
Specifies run-time driver flags.

## Syntax
```
typedef enum _NFC_CX_DRIVER_FLAGS {
  NFC_CX_DRIVER_DISABLE_WTD_TIMER                      ,
  NFC_CX_DRIVER_DISABLE_NFCEE_DISCOVERY                ,
  NFC_CX_DRIVER_DISABLE_RECOVERY_MODE                  ,
  NFC_CX_DRIVER_DISABLE_HOST_CARD_EMULATION            ,
  NFC_CX_DRIVER_HCI_NETWORK_PER_NFCEE                  ,
  NFC_CX_DRIVER_DISABLE_NFCEE_ACTION_NTF               ,
  NFC_CX_DRIVER_ENABLE_EEPROM_WRITE_PROTECTION         ,
  NFC_CX_DRIVER_ISODEP_RNAK_PRESENCE_CHK_SUPPORTED     ,
  NFC_CX_DRIVER_RF_ROUTING_POWER_SUB_STATES_SUPPORTED
} NFC_CX_DRIVER_FLAGS, *PNFC_CX_DRIVER_FLAGS;
```

## Constants

<table>
            
                <tr>
                    <td>NFC_CX_DRIVER_DISABLE_WTD_TIMER</td>
                    <td>Disable watchdog timer in CX.</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_DRIVER_DISABLE_NFCEE_DISCOVERY</td>
                    <td>Disable NFCEE discovery.</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_DRIVER_DISABLE_RECOVERY_MODE</td>
                    <td>Disable NCI recovery mechanism in CX.</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_DRIVER_DISABLE_HOST_CARD_EMULATION</td>
                    <td>Disable host card emulation feature.</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_DRIVER_HCI_NETWORK_PER_NFCEE</td>
                    <td>NFCC implements a separate HCI network per NFCEE.</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_DRIVER_DISABLE_NFCEE_ACTION_NTF</td>
                    <td>Disable NFCEE action notification.</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_DRIVER_ENABLE_EEPROM_WRITE_PROTECTION</td>
                    <td>Enable opt to over-write only when configs change.</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_DRIVER_ISODEP_RNAK_PRESENCE_CHK_SUPPORTED</td>
                    <td>The R-NAK command for ISO-DEP will be used for presence check.</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_DRIVER_RF_ROUTING_POWER_SUB_STATES_SUPPORTED</td>
                    <td>Indicates support for RF routing switched ON power sub-states.</td>
                </tr>
</table>

## Remarks

The NFC CX allows the NFC client driver to provide some driver flags that can be used to configure the run-time implementation of the class extension. These flags enable the NFC CX to implement some standard NCI operations slightly differently to support different firmware implementations due to ambiguities in the NCI specification.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | nfccx.h (include Ncidef.h) |

## See Also

<a href="https://msdn.microsoft.com/windows/hardware/drivers/nfc/nfc-class-extension-">NFC class extension design guide</a>



<a href="http://go.microsoft.com/fwlink/p/?LinkID=785320">Near field communication (NFC) design guide</a>