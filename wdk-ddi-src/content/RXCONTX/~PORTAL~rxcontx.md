# Declarations in the rxcontx header
This header Rxcontx contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [MINIRDR_CALL_THROUGH function](nf-rxcontx-minirdr-call-through.md) | TBD |
| [RxReinitializeContext function](nf-rxcontx-rxreinitializecontext.md) | TBD |
| [RxRestoreExceptionNoBreakpointFlag function](nf-rxcontx-rxrestoreexceptionnobreakpointflag.md) | TBD |
| [RxDereferenceAndDeleteRxContext_Real function](nf-rxcontx-rxdereferenceanddeleterxcontext-real.md) | RxDereferenceAndDeleteRxContext_Real dereferences an RX_CONTEXT data structure and if the ReferenceCount member goes to zero, then it deallocates and removes the specified RX_CONTEXT structure from the RDBSS in-memory data structures. |
| [RxInitializeContext function](nf-rxcontx-rxinitializecontext.md) | RxInitializeContext initializes an existing RX_CONTEXT data structure. |
| [RxResumeBlockedOperations_ALL function](nf-rxcontx-rxresumeblockedoperations-all.md) | TBD |
| [RxCancelBlockingOperation function](nf-rxcontx-rxcancelblockingoperation.md) | TBD |
| [RxGetTopIrpIfRdbssIrp function](nf-rxcontx-rxgettopirpifrdbssirp.md) | TBD |
| [RxSynchronizeBlockingOperationsAndDropFcbLock function](nf-rxcontx-rxsynchronizeblockingoperationsanddropfcblock.md) | TBD |
| [RxPrepareContextForReuse function](nf-rxcontx-rxpreparecontextforreuse.md) | RxPrepareContextForReuse prepares an RX_CONTEXT data structure for reuse by resetting all of the operation-specific allocations and acquisitions that have been made (the ReferenceCount member to the RX_CONTEXT structure is set to zero). |
| [MINIRDR_CALL function](nf-rxcontx-minirdr-call.md) | TBD |
| [RxSignalSynchronousWaiter function](nf-rxcontx-rxsignalsynchronouswaiter.md) | TBD |
| [RxSaveAndSetExceptionNoBreakpointFlag function](nf-rxcontx-rxsaveandsetexceptionnobreakpointflag.md) | TBD |
| [__RxSynchronizeBlockingOperations function](nf-rxcontx---rxsynchronizeblockingoperations.md) | __RxSynchronizeBlockingOperations synchronizes blocking I/O requests to the same work queue. |
| [RxSynchronizeBlockingOperations function](nf-rxcontx-rxsynchronizeblockingoperations.md) | TBD |
| [RxSetMinirdrCancelRoutine function](nf-rxcontx-rxsetminirdrcancelroutine.md) | RxSetMinirdrCancelRoutine is called by a network mini-redirector driver to set up a network mini-redirector cancel routine for an RX_CONTEXT structure. |
| [RxInitializeTopLevelIrpContext function](nf-rxcontx-rxinitializetoplevelirpcontext.md) | TBD |
| [RxCancelNotifyChangeDirectoryRequestsForVNetRoot function](nf-rxcontx-rxcancelnotifychangedirectoryrequestsforvnetroot.md) | TBD |
| [RxWaitSync function](nf-rxcontx-rxwaitsync.md) | TBD |
| [RxTryToBecomeTheTopLevelIrp function](nf-rxcontx-rxtrytobecomethetoplevelirp.md) | TBD |
| [__RxInitializeTopLevelIrpContext function](nf-rxcontx---rxinitializetoplevelirpcontext.md) | TBD |
| [RxIsThisTheTopLevelIrp function](nf-rxcontx-rxisthisthetoplevelirp.md) | TBD |
| [RxTransferListWithMutex function](nf-rxcontx-rxtransferlistwithmutex.md) | TBD |
| [RxInsertContextInSerializationQueue function](nf-rxcontx-rxinsertcontextinserializationqueue.md) | TBD |
| [RxDereferenceAndDeleteRxContext function](nf-rxcontx-rxdereferenceanddeleterxcontext.md) | TBD |
| [RxResumeBlockedOperations_Serially function](nf-rxcontx-rxresumeblockedoperations-serially.md) | TBD |
| [RxCreateRxContext function](nf-rxcontx-rxcreaterxcontext.md) | RxCreateRxContext allocates a new RX_CONTEXT structure and initializes the data structure. |
| [RxTransferList function](nf-rxcontx-rxtransferlist.md) | TBD |
| [RxCancelNotifyChangeDirectoryRequestsForFobx function](nf-rxcontx-rxcancelnotifychangedirectoryrequestsforfobx.md) | TBD |
| [RxRemoveOperationFromBlockingQueue function](nf-rxcontx-rxremoveoperationfromblockingqueue.md) | TBD |
| [RxUnwindTopLevelIrp function](nf-rxcontx-rxunwindtoplevelirp.md) | TBD |
| [RxRemoveFirstContextFromSerializationQueue function](nf-rxcontx-rxremovefirstcontextfromserializationqueue.md) | TBD |
| [RxGetTopDeviceObjectIfRdbssIrp function](nf-rxcontx-rxgettopdeviceobjectifrdbssirp.md) | TBD |
| [__RxItsTheSameContext function](nf-rxcontx---rxitsthesamecontext.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [NT_CREATE_PARAMETERS structure](ns-rxcontx--nt-create-parameters.md) | TBD |
| [RX_CONTEXT structure](ns-rxcontx--rx-context.md) | The RX_CONTEXT structure encapsulates an IRP for use by RDBSS, network mini-redirectors, and the file system. |
| [DFS_NAME_CONTEXT_ structure](ns-rxcontx--dfs-name-context-.md) | TBD |
| [RX_TOPLEVELIRP_CONTEXT structure](ns-rxcontx--rx-toplevelirp-context.md) | TBD |
| [RX_FCBTRACKER_CALLINFO structure](ns-rxcontx--rx-fcbtracker-callinfo.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [RX_CONTEXT_CREATE_FLAGS enumeration](ne-rxcontx-rx-context-create-flags.md) | TBD |
| [RX_CONTEXT_LOWIO_FLAGS enumeration](ne-rxcontx-rx-context-lowio-flags.md) | TBD |
| [RX_CONTEXT_CREATE_FLAGS enumeration](ne-rxcontx-rx-context-create-flags~r1.md) | TBD |
| [RX_CONTEXT_FLAGS enumeration](ne-rxcontx-rx-context-flags.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PRX_DISPATCH callback function](nc-rxcontx-prx-dispatch.md) | TBD |

This header is used in these topics:

- [ifsk](..content/_ifsk)
