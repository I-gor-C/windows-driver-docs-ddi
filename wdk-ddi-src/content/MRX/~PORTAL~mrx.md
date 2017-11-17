# Declarations in the mrx header
This header Mrx contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PMRX_CALLDOWN callback function](nc-mrx-pmrx-calldown.md) | TBD |
| [PMRX_COMPUTE_NEW_BUFFERING_STATE callback function](nc-mrx-pmrx-compute-new-buffering-state.md) | TBD |
| [PMRX_CHKDIR_CALLDOWN callback function](nc-mrx-pmrx-chkdir-calldown.md) | TBD |
| [PMRX_SRVCALL_WINNER_NOTIFY callback function](nc-mrx-pmrx-srvcall-winner-notify.md) | TBD |
| [PMRX_EXTRACT_NETROOT_NAME callback function](nc-mrx-pmrx-extract-netroot-name.md) | TBD |
| [PMRX_FINALIZE_NET_ROOT_CALLDOWN callback function](nc-mrx-pmrx-finalize-net-root-calldown.md) | TBD |
| [PMRX_CREATE_V_NET_ROOT callback function](nc-mrx-pmrx-create-v-net-root.md) | TBD |
| [PMRX_EXTENDFILE_CALLDOWN callback function](nc-mrx-pmrx-extendfile-calldown.md) | TBD |
| [PMRX_GET_CONNECTION_ID callback function](nc-mrx-pmrx-get-connection-id.md) | TBD |
| [PMRX_PREPARSE_NAME callback function](nc-mrx-pmrx-preparse-name.md) | TBD |
| [PMRX_NEWSTATE_CALLDOWN callback function](nc-mrx-pmrx-newstate-calldown.md) | TBD |
| [PMRX_CALLDOWN_CTX callback function](nc-mrx-pmrx-calldown-ctx.md) | TBD |
| [PMRX_DEALLOCATE_FOR_FCB callback function](nc-mrx-pmrx-deallocate-for-fcb.md) | TBD |
| [PMRX_IS_LOCK_REALIZABLE callback function](nc-mrx-pmrx-is-lock-realizable.md) | TBD |
| [PMRX_FORCECLOSED_CALLDOWN callback function](nc-mrx-pmrx-forceclosed-calldown.md) | TBD |
| [PMRX_UPDATE_NETROOT_STATE callback function](nc-mrx-pmrx-update-netroot-state.md) | TBD |
| [PMRX_SRVCALL_CALLBACK callback function](nc-mrx-pmrx-srvcall-callback.md) | TBD |
| [PMRX_CREATE_SRVCALL callback function](nc-mrx-pmrx-create-srvcall.md) | TBD |
| [PMRX_CHKFCB_CALLDOWN callback function](nc-mrx-pmrx-chkfcb-calldown.md) | TBD |
| [PRX_LOCK_ENUMERATOR callback function](nc-mrx-prx-lock-enumerator.md) | TBD |
| [PMRX_NETROOT_CALLBACK callback function](nc-mrx-pmrx-netroot-callback.md) | TBD |
| [PMRX_FINALIZE_V_NET_ROOT_CALLDOWN callback function](nc-mrx-pmrx-finalize-v-net-root-calldown.md) | TBD |
| [PLOWIO_COMPLETION_ROUTINE callback function](nc-mrx-plowio-completion-routine.md) | TBD |
| [PMRX_DEALLOCATE_FOR_FOBX callback function](nc-mrx-pmrx-deallocate-for-fobx.md) | TBD |
| [PMRX_FINALIZE_SRVCALL_CALLDOWN callback function](nc-mrx-pmrx-finalize-srvcall-calldown.md) | TBD |
| [PMRX_CHANGE_BUFFERING_STATE_CALLDOWN callback function](nc-mrx-pmrx-change-buffering-state-calldown.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxRegisterMinirdr function](nf-mrx-rxregisterminirdr.md) | RxRegisterMinirdr is called by a network mini-redirector driver to register the driver with RDBSS, which adds the registration information to an internal registration table. RDBSS also builds a device object for the network mini-redirector. |
| [RxFinalizeLockList function](nf-mrx-rxfinalizelocklist.md) | TBD |
| [RxMakeLateDeviceAvailable function](nf-mrx-rxmakelatedeviceavailable.md) | RxMakeLateDeviceAvailable modifies the device object to make a &#0034;late device&#0034; available. A late device is one that is not created in the driver's load routine. |
| [RxpUnregisterMinirdr function](nf-mrx-rxpunregisterminirdr.md) | RxpUnregisterMinirdr is called by a network mini-redirector driver to de-register the driver with RDBSS and remove the registration information from the internal RDBSS registration table. |
| [RxStopMinirdr function](nf-mrx-rxstopminirdr.md) | RxStopMinirdr is called to stop a network mini-redirector that has previously been started. |
| [RxFsdDispatch function](nf-mrx-rxfsddispatch.md) | RxFsdDispatch implements the file system driver (FSD) dispatch for RDBSS to process an I/O request packet (IRP). |
| [RxStartMinirdr function](nf-mrx-rxstartminirdr.md) | RxStartMinirdr is called to start up a network mini-redirector that has previously called to register with RDBSS. |
| [StableCondition function](nf-mrx-stablecondition.md) | TBD |
| [__RxFillAndInstallFastIoDispatch function](nf-mrx---rxfillandinstallfastiodispatch.md) | RxFillAndInstallFastIoDispatch fills out a fast I/O dispatch vector to be identical with the normal dispatch I/O vector and installs it into the driver object associated with the device object passed. |
| [RxSetDomainForMailslotBroadcast function](nf-mrx-rxsetdomainformailslotbroadcast.md) | RxSetDomainForMailslotBroadcast is called by a network mini-redirector driver to set the domain used for mailslot broadcasts if mailslots are supported by the driver. |
| [RxFillAndInstallFastIoDispatch function](nf-mrx-rxfillandinstallfastiodispatch.md) | TBD |
| [RxGetIoStatusInfo function](nf-mrx-rxgetiostatusinfo.md) | TBD |
| [RxSetIoStatusInfo function](nf-mrx-rxsetiostatusinfo.md) | TBD |
| [RxSetIoStatusStatus function](nf-mrx-rxsetiostatusstatus.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [LOWIO_CONTEXT structure](ns-mrx--lowio-context.md) | TBD |
| [LOWIO_LOCK_LIST structure](ns-mrx--lowio-lock-list.md) | TBD |
| [MRX_CREATENETROOT_CONTEXT structure](ns-mrx--mrx-createnetroot-context.md) | TBD |
| [MRX_SRVCALLDOWN_STRUCTURE structure](ns-mrx--mrx-srvcalldown-structure.md) | TBD |
| [XXCTL_LOWIO_COMPONENT structure](ns-mrx--xxctl-lowio-component.md) | TBD |
| [MINIRDR_DISPATCH structure](ns-mrx--minirdr-dispatch.md) | TBD |
| [MRX_SRVCALL_CALLBACK_CONTEXT structure](ns-mrx--mrx-srvcall-callback-context.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [RX_BLOCK_CONDITION enumeration](ne-mrx--rx-block-condition.md) | TBD |
| [MINIRDR_BUFSTATE_COMMANDS enumeration](ne-mrx--minirdr-bufstate-commands.md) | TBD |
| [LOWIO_OPS enumeration](ne-mrx--lowio-ops.md) | TBD |

This header is used in these topics:

- [ifsk](..content/_ifsk)
