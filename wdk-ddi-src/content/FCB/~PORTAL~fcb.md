# Declarations in the fcb header
This header Fcb contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [FILESIZE_LOCK_DISABLED function](nf-fcb-filesize-lock-disabled.md) | TBD |
| [RxReferenceNetFcb function](nf-fcb-rxreferencenetfcb.md) | TBD |
| [RxCheckFcbStructuresForAlignment function](nf-fcb-rxcheckfcbstructuresforalignment.md) | TBD |
| [RxReferenceSrvCall function](nf-fcb-rxreferencesrvcall.md) | TBD |
| [ASSERT_CORRECT_FCB_STRUCTURE_DBG_ONLY function](nf-fcb-assert-correct-fcb-structure-dbg-only.md) | TBD |
| [RxTransitionSrvCall function](nf-fcb-rxtransitionsrvcall.md) | TBD |
| [RxTransitionNetFcb function](nf-fcb-rxtransitionnetfcb.md) | TBD |
| [RxDereferenceNetFcb function](nf-fcb-rxdereferencenetfcb.md) | TBD |
| [RxpDereferenceAndFinalizeNetFcb function](nf-fcb-rxpdereferenceandfinalizenetfcb.md) | RxpDereferenceAndFinalizeNetFcb decrements the reference count and finalizes an FCB structure. |
| [RxTransitionVNetRoot function](nf-fcb-rxtransitionvnetroot.md) | TBD |
| [RxpReferenceNetFcb function](nf-fcb-rxpreferencenetfcb.md) | RxpReferenceNetFcb increments the reference count on an FCB. |
| [RxWaitForStableSrvCall_Async function](nf-fcb-rxwaitforstablesrvcall-async.md) | TBD |
| [GET_ALREADY_PREFIXED_NAME function](nf-fcb-get-already-prefixed-name.md) | TBD |
| [RxReferenceNetFobx function](nf-fcb-rxreferencenetfobx.md) | TBD |
| [PRINT_REF_COUNT function](nf-fcb-print-ref-count.md) | TBD |
| [RxReferenceVNetRoot function](nf-fcb-rxreferencevnetroot.md) | TBD |
| [RxUninitializeVNetRootParameters function](nf-fcb-rxuninitializevnetrootparameters.md) | TBD |
| [RxReferenceSrvCallAtDpc function](nf-fcb-rxreferencesrvcallatdpc.md) | TBD |
| [RxLoudFcbMsg function](nf-fcb-rxloudfcbmsg.md) | TBD |
| [RxTransitionNetRoot function](nf-fcb-rxtransitionnetroot.md) | TBD |
| [RxpTrackDereference function](nf-fcb-rxptrackdereference.md) | RxpTrackDereference is used in checked builds to track requests to dereference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these dereference requests can be accessed by the logging system and WMI. |
| [RxReferenceNetRoot function](nf-fcb-rxreferencenetroot.md) | TBD |
| [RxWaitForStableNetRoot function](nf-fcb-rxwaitforstablenetroot.md) | TBD |
| [RxFormInitPacket function](nf-fcb-rxforminitpacket.md) | TBD |
| [RxCreateVNetRoot function](nf-fcb-rxcreatevnetroot.md) | RxCreateVNetRoot allocates and initializes a NET_ROOT structure and inserts the name into the net name table on the associated device object. |
| [RxDereferenceSrvCall function](nf-fcb-rxdereferencesrvcall.md) | TBD |
| [RxWriteCachingAllowed function](nf-fcb-rxwritecachingallowed.md) | TBD |
| [RxReferenceSrvOpen function](nf-fcb-rxreferencesrvopen.md) | TBD |
| [RxRemoveNameNetFcb function](nf-fcb-rxremovenamenetfcb.md) | TBD |
| [RxInitializeVNetRootParameters function](nf-fcb-rxinitializevnetrootparameters.md) | TBD |
| [RxCreateNetFcb function](nf-fcb-rxcreatenetfcb.md) | RxCreateNetFCB allocates, initializes, and inserts a new FCB structure into the in-memory data structures for a V_NET_ROOT that this FCB is being opened on. The structure allocated has space for a SRV_OPEN and an FOBX structure. |
| [REF_TRACING_ON function](nf-fcb-ref-tracing-on.md) | TBD |
| [RxWaitForStableVNetRoot function](nf-fcb-rxwaitforstablevnetroot.md) | TBD |
| [RxpTrackReference function](nf-fcb-rxptrackreference.md) | RxpTrackReference tracks requests to reference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these reference requests can be accessed by the logging system and WMI. |
| [RxReleaseFileSizeLock function](nf-fcb-rxreleasefilesizelock.md) | TBD |
| [RxWaitForStableSrvCall function](nf-fcb-rxwaitforstablesrvcall.md) | TBD |
| [RxFinalizeNetRoot function](nf-fcb-rxfinalizenetroot.md) | RxFinalizeNetRoot finalizes the given NET_ROOT structure. The caller must have an exclusive lock on the netname table associated with the device object. |
| [RxAcquireFileSizeLock function](nf-fcb-rxacquirefilesizelock.md) | TBD |
| [RxFinalizeNetFobx function](nf-fcb-rxfinalizenetfobx.md) | RxFinalizeNetFOBX finalizes the given FOBX structure. The caller must have an exclusive lock on the FCB associated with FOBX structure. |
| [RxFinalizeVNetRoot function](nf-fcb-rxfinalizevnetroot.md) | RxFinalizeVNetRoot finalizes the given V_NET_ROOT structure. The caller must have an exclusive lock on the netname table associated with the device object. |
| [RxFinalizeSrvOpen function](nf-fcb-rxfinalizesrvopen.md) | RxFinalizeSrvOpen finalizes the given SRV_OPEN structure. The caller must have an exclusive lock on the FCB associated with the SRV_OPEN and either a shared or exclusive lock on the table lock of the NET_ROOT associated with the FCB. |
| [RxCreateSrvCall function](nf-fcb-rxcreatesrvcall.md) | RxCreateSrvCall builds a SRV_CALL structure and inserts the name into the net name table maintained by RDBSS. |
| [GET_ALREADY_PREFIXED_NAME_FROM_CONTEXT function](nf-fcb-get-already-prefixed-name-from-context.md) | TBD |
| [RxDereferenceNetRoot function](nf-fcb-rxdereferencenetroot.md) | TBD |
| [RxCreateNetRoot function](nf-fcb-rxcreatenetroot.md) | RxCreateNetRoot allocates and initializes a NET_ROOT structure and inserts the name into the net name table on the associated device object. |
| [RxTransitionSrvOpen function](nf-fcb-rxtransitionsrvopen.md) | TBD |
| [RxpDereferenceNetFcb function](nf-fcb-rxpdereferencenetfcb.md) | RxpDereferenceNetFcb decrements the reference count on an FCB structure. |
| [RxDereferenceSrvOpen function](nf-fcb-rxdereferencesrvopen.md) | TBD |
| [RxFinishFcbInitialization function](nf-fcb-rxfinishfcbinitialization.md) | RxFinishFcbInitialization is used to finish initializing an FCB after the successful completion of a create operation by the network mini-redirector. |
| [RxCreateNetFobx function](nf-fcb-rxcreatenetfobx.md) | RxCreateNetFobx allocates, initializes, and inserts a new file object extension (FOBX) structure into the in-memory data structures for a FCB that this FOBX is being opened on. |
| [ASSERT_CORRECT_FCB_STRUCTURE function](nf-fcb-assert-correct-fcb-structure.md) | TBD |
| [RxLoudFcbMsg function](nf-fcb-rxloudfcbmsg~r1.md) | TBD |
| [RxDereferenceVNetRoot function](nf-fcb-rxdereferencevnetroot.md) | TBD |
| [RxInferFileType function](nf-fcb-rxinferfiletype.md) | RxInferFileType tries to infer the file type (directory or non-directory) from a member in the RX_CONTEXT structure. |
| [RxSetFileSizeWithLock function](nf-fcb-rxsetfilesizewithlock.md) | TBD |
| [RxDereferenceAndFinalizeNetFcb function](nf-fcb-rxdereferenceandfinalizenetfcb.md) | TBD |
| [RxCreateSrvOpen function](nf-fcb-rxcreatesrvopen.md) | RxCreateSrvOpen allocates, initializes, and inserts a new SRV_OPEN structure into the in-memory data structures used by RDBSS. If a new structure has to be allocated, it has space for an FOBX structure. |
| [RxFinalizeSrvCall function](nf-fcb-rxfinalizesrvcall.md) | RxFinalizeSrvCall finalizes the given SRV_CALL structure. The caller must have an exclusive lock on the netname table associated with the device object. |
| [RxWaitForStableSrvOpen function](nf-fcb-rxwaitforstablesrvopen.md) | TBD |
| [RxWaitForStableNetFcb function](nf-fcb-rxwaitforstablenetfcb.md) | TBD |
| [RxGetFileSizeWithLock function](nf-fcb-rxgetfilesizewithlock.md) | RxGetFileSizeWithLock gets the file size in the FCB structure using a lock to ensure that the 64-bit value is read consistently. |
| [RxDereferenceNetFobx function](nf-fcb-rxdereferencenetfobx.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [FCB_INIT_PACKET structure](ns-fcb--fcb-init-packet.md) | TBD |
| [NON_PAGED_FCB structure](ns-fcb--non-paged-fcb.md) | TBD |
| [SRV_OPEN structure](ns-fcb--srv-open~r1.md) | TBD |
| [NET_ROOT structure](ns-fcb--net-root.md) | TBD |
| [FCB_INIT_PACKET structure](ns-fcb--fcb-init-packet~r1.md) | TBD |
| [NET_ROOT structure](ns-fcb--net-root~r1.md) | TBD |
| [V_NET_ROOT structure](ns-fcb--v-net-root~r1.md) | TBD |
| [SRV_CALL structure](ns-fcb--srv-call.md) | TBD |
| [SRV_OPEN structure](ns-fcb--srv-open.md) | TBD |
| [SRV_CALL structure](ns-fcb--srv-call~r1.md) | TBD |
| [FCB_BUFFERED_LOCKS structure](ns-fcb--fcb-buffered-locks.md) | TBD |
| [FCB structure](ns-fcb--fcb.md) | TBD |
| [FCB_INIT_PACKET structure](ns-fcb--fcb-init-packet~r2.md) | TBD |
| [FOBX structure](ns-fcb--fobx.md) | TBD |
| [V_NET_ROOT structure](ns-fcb--v-net-root.md) | TBD |
| [FCB_LOCK structure](ns-fcb--fcb-lock.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [RX_FCBTRACKER_CASES enumeration](ne-fcb--rx-fcbtracker-cases.md) | TBD |
| [FCB_CONDITION enumeration](ne-fcb--fcb-condition.md) | TBD |

This header is used in these topics:

- [ifsk](..content/_ifsk)
