# Declarations in the rxce header
This header Rxce contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxCeIsTransportValid function](nf-rxce-rxceistransportvalid.md) | TBD |
| [RxCeBuildTransport function](nf-rxce-rxcebuildtransport.md) | RxCeBuildTransport binds an RDBSS transport object to a specified transport name. |
| [RxCeFreeIrp function](nf-rxce-rxcefreeirp.md) | RxCeFreeIrp frees an IRP. |
| [RxCeSendDatagram function](nf-rxce-rxcesenddatagram.md) | RxCeSendDatagram sends a transport service data unit (TSDU) along the specified connection on a virtual circuit. |
| [RxCeIsAddressValid function](nf-rxce-rxceisaddressvalid.md) | TBD |
| [RxCeBuildAddress function](nf-rxce-rxcebuildaddress.md) | RxCeBuildAddress associates a transport address with a transport binding. |
| [RxCeCancelConnectRequest function](nf-rxce-rxcecancelconnectrequest.md) | RxCeCancelConnectRequest cancels a previously issued connection request. Note that this routine is not currently implemented. |
| [RxCeBuildConnection function](nf-rxce-rxcebuildconnection.md) | RxCeBuildConnection establishes a connection between a local RDBSS connection address and a given remote address. |
| [RxCeBuildConnectionOverMultipleTransports function](nf-rxce-rxcebuildconnectionovermultipletransports.md) | RxCeBuildConnectionOverMultipleTransports establishes a connection between a local RDBSS connection address and a given remote address and supports multiple transports. |
| [RxCeAllocateIrpWithMDL function](nf-rxce-rxceallocateirpwithmdl.md) | RxCeAllocateIrpWithMDL allocates an IRP and associates it with an existing memory descriptor list. |
| [RxCeSend function](nf-rxce-rxcesend.md) | RxCeSend sends a transport service data unit (TSDU) along the specified connection on a virtual circuit. |
| [RxCeTearDownAddress function](nf-rxce-rxceteardownaddress.md) | RxCeTearDownAddress deregisters a transport address from a transport binding. |
| [RxCeTearDownVC function](nf-rxce-rxceteardownvc.md) | RxCeTearDownVC deregisters a virtual circuit from a specified RDBSS connection. |
| [RxCeIsConnectionValid function](nf-rxce-rxceisconnectionvalid.md) | TBD |
| [RxCeBuildVC function](nf-rxce-rxcebuildvc.md) | RxCeBuildVC adds a virtual circuit to a specified RDBSS connection.. |
| [RxCeQueryAdapterStatus function](nf-rxce-rxcequeryadapterstatus.md) | RxCeQueryAdapterStatus returns the ADAPTER_STATUS structure for a given transport in a caller-allocated buffer. |
| [RxCeIsVcValid function](nf-rxce-rxceisvcvalid.md) | TBD |
| [RxCeInitiateVCDisconnect function](nf-rxce-rxceinitiatevcdisconnect.md) | RxCeInitiateVCDisconnect initiates a disconnect on the virtual circuit. |
| [RxCeQueryTransportInformation function](nf-rxce-rxcequerytransportinformation.md) | RxCeQueryTransportInformation queries transport information for a given transport. |
| [RxCeTearDownConnection function](nf-rxce-rxceteardownconnection.md) | RxCeTearDownConnection tears down a given connection between a local RDBSS connection address and a remote address. |
| [RxCeTearDownTransport function](nf-rxce-rxceteardowntransport.md) | RxCeTearDownTransport unbinds an RDBSS transport object. |
| [RxCeQueryInformation function](nf-rxce-rxcequeryinformation.md) | RxCeQueryInformation queries information about a connection in a caller-allocated buffer. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [RXCE_TRANSPORT_ structure](ns-rxce--rxce-transport-~r1.md) | TBD |
| [RXCE_ADDRESS_ structure](ns-rxce--rxce-address-~r1.md) | TBD |
| [RXCE_CONNECTION_ structure](ns-rxce--rxce-connection-~r1.md) | TBD |
| [RXCE_TRANSPORT_ structure](ns-rxce--rxce-transport-.md) | TBD |
| [RXCE_CONNECTION_COMPLETION_CONTEXT_ structure](ns-rxce--rxce-connection-completion-context-.md) | TBD |
| [RXCE_SIGNATURE_ structure](ns-rxce--rxce-signature-.md) | TBD |
| [RXCE_ADDRESS_ structure](ns-rxce--rxce-address-.md) | TBD |
| [RXCE_CONNECTION_ structure](ns-rxce--rxce-connection-.md) | TBD |
| [RXCE_VC_ structure](ns-rxce--rxce-vc-~r1.md) | TBD |
| [RXCE_VC_ structure](ns-rxce--rxce-vc-.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [RXCE_CONNECTION_CREATE_OPTIONS_ enumeration](ne-rxce--rxce-connection-create-options-.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PRXCE_CONNECTION_COMPLETION_ROUTINE callback function](nc-rxce-prxce-connection-completion-routine.md) | TBD |

This header is used in these topics:

- [ifsk](..content/_ifsk)
