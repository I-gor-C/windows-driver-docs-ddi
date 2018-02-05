---
UID : NF:nfccx.NfcCxRegisterSequenceHandler
title : NfcCxRegisterSequenceHandler function
author : windows-driver-content
description : Called by the client driver during initialization to register for handling specific sequences.
old-location : nfpdrivers\_nfccxregistersequencehandler.htm
old-project : nfpdrivers
ms.assetid : 30957475-D02B-434D-9FAB-BBCD5732DCA5
ms.author : windowsdriverdev
ms.date : 12/18/2017
ms.keywords : NfcCxRegisterSequenceHandler, NfcCxRegisterSequenceHandler method [Near-Field Proximity Drivers], nfccx/NfcCxRegisterSequenceHandler, nfpdrivers._nfccxregistersequencehandler
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : nfccx.h
req.include-header : Ncidef.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : None supported
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Nfccxstub.lib
req.dll : NfcCx.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : NFC_CX_TRANSPORT_TYPE, *PNFC_CX_TRANSPORT_TYPE
---


# NfcCxRegisterSequenceHandler function
Called by the client driver during initialization to register for handling specific sequences.

## Syntax

````
NTSTATUS NfcCxRegisterSequenceHandler(
   WDFDEVICE                   Device,
   NFC_CX_SEQUENCE             Sequence,
   PFN_NFC_CX_SEQUENCE_HANDLER EvtNfcCxSequenceHandler
);
````

## Parameters

`Device`

A handle to a framework device object.

`Sequence`

An <a href="..\nfccx\ne-nfccx-_nfc_cx_sequence.md">NFC_CX_SEQUENCE</a>-typed enumerator.

`EvtNfcCxSequenceHandler`

A pointer to an <a href="..\nfccx\nc-nfccx-evt_nfc_cx_sequence_handler.md">EvtNfcCxSequenceHandler</a> callback function.


## Return Value

If the operation succeeds, the function returns STATUS_SUCCESS.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Target Platform** | Windows |
| **Header** | nfccx.h (include Ncidef.h) |
| **Library** | Nfccxstub.lib |
| **DLL** | NfcCx.dll |

## See Also

<a href="http://go.microsoft.com/fwlink/p/?LinkID=785320">Near field communication (NFC) design guide</a>

<a href="https://msdn.microsoft.com/windows/hardware/drivers/nfc/nfc-class-extension-">NFC class extension design guide</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [nfpdrivers\nfpdrivers]:%20NfcCxRegisterSequenceHandler method%20 RELEASE:%20(12/18/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>