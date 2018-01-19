---
UID : NA:rxcontx
ms.assetid : 8c6d4a7f-608f-3a47-b2a9-e46284870bd4
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# rxcontx.h header



rxcontx.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [__RxSynchronizeBlockingOperations](nf-rxcontx-__rxsynchronizeblockingoperations.md) | __RxSynchronizeBlockingOperations synchronizes blocking I/O requests to the same work queue. |
| [RxCreateRxContext](nf-rxcontx-rxcreaterxcontext.md) | RxCreateRxContext allocates a new RX_CONTEXT structure and initializes the data structure. |
| [RxDereferenceAndDeleteRxContext_Real](nf-rxcontx-rxdereferenceanddeleterxcontext_real.md) | RxDereferenceAndDeleteRxContext_Real dereferences an RX_CONTEXT data structure and if the ReferenceCount member goes to zero, then it deallocates and removes the specified RX_CONTEXT structure from the RDBSS in-memory data structures. |
| [RxInitializeContext](nf-rxcontx-rxinitializecontext.md) | RxInitializeContext initializes an existing RX_CONTEXT data structure. |
| [RxPrepareContextForReuse](nf-rxcontx-rxpreparecontextforreuse.md) | RxPrepareContextForReuse prepares an RX_CONTEXT data structure for reuse by resetting all of the operation-specific allocations and acquisitions that have been made (the ReferenceCount member to the RX_CONTEXT structure is set to zero). |
| [RxResumeBlockedOperations_Serially](nf-rxcontx-rxresumeblockedoperations_serially.md) | RxResumeBlockedOperations_Serially wakes up the next waiting thread, if any, on the serialized blocking I/O queue. |
| [RxSetMinirdrCancelRoutine](nf-rxcontx-rxsetminirdrcancelroutine.md) | RxSetMinirdrCancelRoutine is called by a network mini-redirector driver to set up a network mini-redirector cancel routine for an RX_CONTEXT structure. |



## Structures
| Title | Description |
| ---- |:---- |
| [_RX_CONTEXT](ns-rxcontx-_rx_context.md) | The RX_CONTEXT structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system. |