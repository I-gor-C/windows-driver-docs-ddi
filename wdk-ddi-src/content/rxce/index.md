---
UID : NA:rxce
ms.assetid : 21be7cda-22a7-31c2-8fd4-74b9d08f24bf
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# rxce.h header



rxce.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [RxCeAllocateIrpWithMDL](nf-rxce-rxceallocateirpwithmdl.md) | RxCeAllocateIrpWithMDL allocates an IRP and associates it with an existing memory descriptor list. |
| [RxCeBuildAddress](nf-rxce-rxcebuildaddress.md) | RxCeBuildAddress associates a transport address with a transport binding. |
| [RxCeBuildConnection](nf-rxce-rxcebuildconnection.md) | RxCeBuildConnection establishes a connection between a local RDBSS connection address and a given remote address. |
| [RxCeBuildConnectionOverMultipleTransports](nf-rxce-rxcebuildconnectionovermultipletransports.md) | RxCeBuildConnectionOverMultipleTransports establishes a connection between a local RDBSS connection address and a given remote address and supports multiple transports. |
| [RxCeBuildTransport](nf-rxce-rxcebuildtransport.md) | RxCeBuildTransport binds an RDBSS transport object to a specified transport name. |
| [RxCeBuildVC](nf-rxce-rxcebuildvc.md) | RxCeBuildVC adds a virtual circuit to a specified RDBSS connection.. |
| [RxCeCancelConnectRequest](nf-rxce-rxcecancelconnectrequest.md) | RxCeCancelConnectRequest cancels a previously issued connection request. Note that this routine is not currently implemented. |
| [RxCeFreeIrp](nf-rxce-rxcefreeirp.md) | RxCeFreeIrp frees an IRP. |
| [RxCeInitiateVCDisconnect](nf-rxce-rxceinitiatevcdisconnect.md) | RxCeInitiateVCDisconnect initiates a disconnect on the virtual circuit. |
| [RxCeQueryAdapterStatus](nf-rxce-rxcequeryadapterstatus.md) | RxCeQueryAdapterStatus returns the ADAPTER_STATUS structure for a given transport in a caller-allocated buffer. |
| [RxCeQueryInformation](nf-rxce-rxcequeryinformation.md) | RxCeQueryInformation queries information about a connection in a caller-allocated buffer. |
| [RxCeQueryTransportInformation](nf-rxce-rxcequerytransportinformation.md) | RxCeQueryTransportInformation queries transport information for a given transport. |
| [RxCeSend](nf-rxce-rxcesend.md) | RxCeSend sends a transport service data unit (TSDU) along the specified connection on a virtual circuit. |
| [RxCeSendDatagram](nf-rxce-rxcesenddatagram.md) | RxCeSendDatagram sends a transport service data unit (TSDU) along the specified connection on a virtual circuit. |
| [RxCeTearDownAddress](nf-rxce-rxceteardownaddress.md) | RxCeTearDownAddress deregisters a transport address from a transport binding. |
| [RxCeTearDownConnection](nf-rxce-rxceteardownconnection.md) | RxCeTearDownConnection tears down a given connection between a local RDBSS connection address and a remote address. |
| [RxCeTearDownTransport](nf-rxce-rxceteardowntransport.md) | RxCeTearDownTransport unbinds an RDBSS transport object. |
| [RxCeTearDownVC](nf-rxce-rxceteardownvc.md) | RxCeTearDownVC deregisters a virtual circuit from a specified RDBSS connection. |