# Mrx.h header


This header is used by unknown technology.

Mrx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [RxFsdDispatch function](nf-mrx-rxfsddispatch.md) | RxFsdDispatch implements the file system driver (FSD) dispatch for RDBSS to process an I/O request packet (IRP). |
| [RxMakeLateDeviceAvailable function](nf-mrx-rxmakelatedeviceavailable.md) | RxMakeLateDeviceAvailable modifies the device object to make a &#0034;late device&#0034; available. A late device is one that is not created in the driver's load routine. |
| [RxRegisterMinirdr function](nf-mrx-rxregisterminirdr.md) | RxRegisterMinirdr is called by a network mini-redirector driver to register the driver with RDBSS, which adds the registration information to an internal registration table. RDBSS also builds a device object for the network mini-redirector. |
| [RxSetDomainForMailslotBroadcast function](nf-mrx-rxsetdomainformailslotbroadcast.md) | RxSetDomainForMailslotBroadcast is called by a network mini-redirector driver to set the domain used for mailslot broadcasts if mailslots are supported by the driver. |
| [RxStartMinirdr function](nf-mrx-rxstartminirdr.md) | RxStartMinirdr is called to start up a network mini-redirector that has previously called to register with RDBSS. |
| [RxStopMinirdr function](nf-mrx-rxstopminirdr.md) | RxStopMinirdr is called to stop a network mini-redirector that has previously been started. |
| [RxpUnregisterMinirdr function](nf-mrx-rxpunregisterminirdr.md) | RxpUnregisterMinirdr is called by a network mini-redirector driver to de-register the driver with RDBSS and remove the registration information from the internal RDBSS registration table. |
| [__RxFillAndInstallFastIoDispatch function](nf-mrx---rxfillandinstallfastiodispatch.md) | RxFillAndInstallFastIoDispatch fills out a fast I/O dispatch vector to be identical with the normal dispatch I/O vector and installs it into the driver object associated with the device object passed. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PMRX_CALLDOWN callback](nc-mrx-pmrx-calldown.md) | The MRxCleanupFobx routine is called by RDBSS to request the network mini-redirector to close a file system object extension. RDBSS issues this call in response to receiving an IRP_MJ_CLEANUP request on a file object. |
| [PMRX_CALLDOWN_CTX callback](nc-mrx-pmrx-calldown-ctx.md) | TheMRxStart routine is called by RDBSS to start the network mini-redirector. |
| [PMRX_CHANGE_BUFFERING_STATE_CALLDOWN callback](nc-mrx-pmrx-change-buffering-state-calldown.md) | TheMRxCompleteBufferingStateChangeRequest routine is called by RDBSS to notify the network mini-redirector that a buffering state change request has been completed. |
| [PMRX_CHKDIR_CALLDOWN callback](nc-mrx-pmrx-chkdir-calldown.md) | TheMRxIsValidDirectory routine is called by RDBSS to request that a network mini-redirector check for the existence of a remote directory. |
| [PMRX_CHKFCB_CALLDOWN callback](nc-mrx-pmrx-chkfcb-calldown.md) | The MRxAreFilesAliased routine is called by RDBSS to request the network mini-redirector to determine if two FCB structures represent the same file. |
| [PMRX_COMPUTE_NEW_BUFFERING_STATE callback](nc-mrx-pmrx-compute-new-buffering-state.md) | TheMRxComputeNewBufferingState routine is called by RDBSS to request that the network mini-redirector compute a new buffering state change. |
| [PMRX_CREATE_SRVCALL callback](nc-mrx-pmrx-create-srvcall.md) | The MRxCreateSrvCall routine is called by RDBSS to request that the network mini-redirector create an SRV_CALL structure and establish connection with a server. |
| [PMRX_CREATE_V_NET_ROOT callback](nc-mrx-pmrx-create-v-net-root.md) | The MRxCreateVNetRoot routine is called by RDBSS to request that the network mini-redirector create a V_NET_ROOT structure and, in some cases, a NET_ROOT structure. |
| [PMRX_DEALLOCATE_FOR_FCB callback](nc-mrx-pmrx-deallocate-for-fcb.md) | The MRxDeallocateForFcb routine is called by RDBSS to request that the network mini-redirector deallocate an FCB structure. This call is in response to a request to close a file system object. |
| [PMRX_DEALLOCATE_FOR_FOBX callback](nc-mrx-pmrx-deallocate-for-fobx.md) | The MRxDeallocateForFobx routine is called by RDBSS to request that the network mini-redirector deallocate an FOBX structure. This call is in response to a request to close a file system object. |
| [PMRX_EXTENDFILE_CALLDOWN callback](nc-mrx-pmrx-extendfile-calldown.md) | The MRxExtendForCache routine is called by RDBSS to request that a network mini-redirector extend a file when the file is being cached by the cache manager. |
| [PMRX_EXTRACT_NETROOT_NAME callback](nc-mrx-pmrx-extract-netroot-name.md) | The MRxExtractNetRootName routine is called by RDBSS to request that a network mini-redirector extract the name of the NET_ROOT structure from a given pathname. |
| [PMRX_FINALIZE_NET_ROOT_CALLDOWN callback](nc-mrx-pmrx-finalize-net-root-calldown.md) | The MRxFinalizeNetRoot routine is called by RDBSS to request that a network mini-redirector finalize a NET_ROOT structure. |
| [PMRX_FINALIZE_SRVCALL_CALLDOWN callback](nc-mrx-pmrx-finalize-srvcall-calldown.md) | The MRxFinalizeSrvCall routine is called by RDBSS to request that a network mini-redirector finalize an SRV_CALL structure. |
| [PMRX_FINALIZE_V_NET_ROOT_CALLDOWN callback](nc-mrx-pmrx-finalize-v-net-root-calldown.md) | The MRxFinalizeVNetRoot routine is called by RDBSS to request that a network mini-redirector finalize a V_NET_ROOT structure. |
| [PMRX_FORCECLOSED_CALLDOWN callback](nc-mrx-pmrx-forceclosed-calldown.md) | The MRxForceClosed routine is called by RDBSS to request that a network mini-redirector force a close. This routine is called when the condition of the SRV_OPEN structure is not good or the SRV_OPEN structure is marked as closed. |
| [PMRX_GET_CONNECTION_ID callback](nc-mrx-pmrx-get-connection-id.md) | TheMRxGetConnectionId routine is called by RDBSS to request that a network mini-redirector return a connection ID, which can be used for handling multiple sessions. |
| [PMRX_IS_LOCK_REALIZABLE callback](nc-mrx-pmrx-is-lock-realizable.md) | The MRxIsLockRealizable routine is called by RDBSS to request that a network mini-redirector indicate whether a specific byte-range lock is supported on this NET_ROOT structure. |
| [PMRX_PREPARSE_NAME callback](nc-mrx-pmrx-preparse-name.md) | The MRxPreparseName routine is called by RDBSS to give a network mini-redirector the opportunity to preparse a name. |
| [PMRX_SRVCALL_WINNER_NOTIFY callback](nc-mrx-pmrx-srvcall-winner-notify.md) | The MRxSrvCallWinnerNotify routine is called by RDBSS to notify a network mini-redirector that it was chosen when multiple redirectors could fulfill the request. |
