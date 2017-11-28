# Rxcontx.h header


This header is used by unknown technology.

Rxcontx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [RxCreateRxContext function](nf-rxcontx-rxcreaterxcontext.md) | RxCreateRxContext allocates a new RX_CONTEXT structure and initializes the data structure. |
| [RxDereferenceAndDeleteRxContext_Real function](nf-rxcontx-rxdereferenceanddeleterxcontext-real.md) | RxDereferenceAndDeleteRxContext_Real dereferences an RX_CONTEXT data structure and if the ReferenceCount member goes to zero, then it deallocates and removes the specified RX_CONTEXT structure from the RDBSS in-memory data structures. |
| [RxInitializeContext function](nf-rxcontx-rxinitializecontext.md) | RxInitializeContext initializes an existing RX_CONTEXT data structure. |
| [RxPrepareContextForReuse function](nf-rxcontx-rxpreparecontextforreuse.md) | RxPrepareContextForReuse prepares an RX_CONTEXT data structure for reuse by resetting all of the operation-specific allocations and acquisitions that have been made (the ReferenceCount member to the RX_CONTEXT structure is set to zero). |
| [RxResumeBlockedOperations_Serially function](nf-rxcontx-rxresumeblockedoperations-serially.md) | RxResumeBlockedOperations_Serially wakes up the next waiting thread, if any, on the serialized blocking I/O queue. |
| [RxSetMinirdrCancelRoutine function](nf-rxcontx-rxsetminirdrcancelroutine.md) | RxSetMinirdrCancelRoutine is called by a network mini-redirector driver to set up a network mini-redirector cancel routine for an RX_CONTEXT structure. |
| [__RxSynchronizeBlockingOperations function](nf-rxcontx---rxsynchronizeblockingoperations.md) | __RxSynchronizeBlockingOperations synchronizes blocking I/O requests to the same work queue. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [RX_CONTEXT structure](ns-rxcontx--rx-context.md) | The RX_CONTEXT structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system. |
