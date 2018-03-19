---
UID: NF:nfccx.NfcCxDeviceInitialize
title: NfcCxDeviceInitialize function
author: windows-driver-content
description: Called by the client driver after a WDF device has been created during the AddDevice routine.
old-location: nfpdrivers\_nfccxdeviceinitialize.htm
old-project: nfpdrivers
ms.assetid: E9282552-93AB-4380-A270-1A538CCF8C0E
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: NfcCxDeviceInitialize, NfcCxDeviceInitialize method [Near-Field Proximity Drivers], nfccx/NfcCxDeviceInitialize, nfpdrivers._nfccxdeviceinitialize
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
-	NfcCxDeviceInitialize
product: Windows
targetos: Windows
req.typenames: NFC_CX_TRANSPORT_TYPE, *PNFC_CX_TRANSPORT_TYPE
---


# NfcCxDeviceInitialize function
Called by the client driver after a WDF device has been created during the AddDevice routine.

## Syntax

````
NTSTATUS  NfcCxDeviceInitialize(
   WDFDEVICE Device
);
````

## Parameters

`Device`

A handle to a framework device object.


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