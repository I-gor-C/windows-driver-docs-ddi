---
UID: NF:nfccx.NfcCxSetRfDiscoveryConfig
title: NfcCxSetRfDiscoveryConfig function
author: windows-driver-content
description: Called by the client driver to configure the RF discovery parameters.
old-location: nfpdrivers\_nfccxsetrfdiscoveryconfig.htm
old-project: nfpdrivers
ms.assetid: D0190BA1-196D-4F8B-A367-80272F094B6B
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: NfcCxSetRfDiscoveryConfig, NfcCxSetRfDiscoveryConfig method [Near-Field Proximity Drivers], nfccx/NfcCxSetRfDiscoveryConfig, nfpdrivers._nfccxsetrfdiscoveryconfig
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
req.lib: Nfccxstub.lib
req.dll: NfcCx.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NfcCx.dll
api_name:
-	NfcCxSetRfDiscoveryConfig
product: Windows
targetos: Windows
req.typenames: NFC_CX_TRANSPORT_TYPE, *PNFC_CX_TRANSPORT_TYPE
---


# NfcCxSetRfDiscoveryConfig function
Called by the client driver to configure the RF discovery parameters.

## Syntax

````
NTSTATUS NfcCxSetRfDiscoveryConfig(
   WDFDEVICE                    Device,
   PCNFC_CX_RF_DISCOVERY_CONFIG Config
);
````

## Parameters

`Device`

A handle to a framework device object.

`Config`

A pointer to an <a href="..\nfccx\ns-nfccx-_nfc_cx_rf_discovery_config.md">NFC_CX_RF_DISCOVERY_CONFIG</a> structure.


## Return Value

If the operation succeeds, the function returns STATUS_SUCCESS.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 None supported |
| **Target Platform** | Windows |
| **Header** | nfccx.h (include Ncidef.h) |
| **Library** | Nfccxstub.lib |
| **DLL** | NfcCx.dll |

## See Also

<a href="https://msdn.microsoft.com/windows/hardware/drivers/nfc/nfc-class-extension-">NFC class extension design guide</a>



<a href="http://go.microsoft.com/fwlink/p/?LinkID=785320">Near field communication (NFC) design guide</a>