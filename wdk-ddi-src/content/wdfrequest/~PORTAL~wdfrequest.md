# Declarations in the wdfrequest header
This header Wdfrequest contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_REQUEST_FORWARD_OPTIONS structure](ns-wdfrequest--wdf-request-forward-options.md) | The WDF_REQUEST_FORWARD_OPTIONS structure contains options for requeuing an I/O request from a child device's I/O queue to the parent device's I/O queue. |
| [WDF_REQUEST_COMPLETION_PARAMS structure](ns-wdfrequest--wdf-request-completion-params.md) | The WDF_REQUEST_COMPLETION_PARAMS structure contains parameters that are associated with the completion of an I/O request. |
| [WDF_REQUEST_PARAMETERS structure](ns-wdfrequest--wdf-request-parameters.md) | The WDF_REQUEST_PARAMETERS structure receives parameters that are associated with an I/O request. |
| [WDF_REQUEST_REUSE_PARAMS structure](ns-wdfrequest--wdf-request-reuse-params.md) | The WDF_REQUEST_REUSE_PARAMS structure specifies information that is associated with a reused I/O request. |
| [WDF_USB_REQUEST_COMPLETION_PARAMS structure](ns-wdfrequest--wdf-usb-request-completion-params.md) | TBD |
| [WDF_REQUEST_SEND_OPTIONS structure](ns-wdfrequest--wdf-request-send-options.md) | The WDF_REQUEST_SEND_OPTIONS structure specifies options that are associated with sending an I/O request to an I/O target. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFREQUESTGETEFFECTIVEIOTYPE callback function](nc-wdfrequest-pfn-wdfrequestgeteffectiveiotype.md) | TBD |
| [PFN_WDFREQUESTRETRIEVEINPUTMEMORY callback function](nc-wdfrequest-pfn-wdfrequestretrieveinputmemory.md) | TBD |
| [PFN_WDFREQUESTSETCOMPLETIONROUTINE callback function](nc-wdfrequest-pfn-wdfrequestsetcompletionroutine.md) | TBD |
| [PFN_WDFREQUESTGETSTATUS callback function](nc-wdfrequest-pfn-wdfrequestgetstatus.md) | TBD |
| [PFN_WDFREQUESTGETREQUESTORMODE callback function](nc-wdfrequest-pfn-wdfrequestgetrequestormode.md) | TBD |
| [PFN_WDFREQUESTRETRIEVEACTIVITYID callback function](nc-wdfrequest-pfn-wdfrequestretrieveactivityid.md) | TBD |
| [PFN_WDFREQUESTRETRIEVEINPUTWDMMDL callback function](nc-wdfrequest-pfn-wdfrequestretrieveinputwdmmdl.md) | TBD |
| [PFN_WDFREQUESTRETRIEVEINPUTBUFFER callback function](nc-wdfrequest-pfn-wdfrequestretrieveinputbuffer.md) | TBD |
| [PFN_WDFREQUESTRETRIEVEUNSAFEUSEROUTPUTBUFFER callback function](nc-wdfrequest-pfn-wdfrequestretrieveunsafeuseroutputbuffer.md) | TBD |
| [PFN_WDFREQUESTWDMFORMATUSINGSTACKLOCATION callback function](nc-wdfrequest-pfn-wdfrequestwdmformatusingstacklocation.md) | TBD |
| [PFN_WDFREQUESTCOMPLETE callback function](nc-wdfrequest-pfn-wdfrequestcomplete.md) | TBD |
| [PFN_WDFREQUESTGETIOQUEUE callback function](nc-wdfrequest-pfn-wdfrequestgetioqueue.md) | TBD |
| [PFN_WDFREQUESTIMPERSONATE callback function](nc-wdfrequest-pfn-wdfrequestimpersonate.md) | TBD |
| [PFN_WDFREQUESTMARKCANCELABLE callback function](nc-wdfrequest-pfn-wdfrequestmarkcancelable.md) | TBD |
| [PFN_WDFREQUESTRETRIEVEOUTPUTBUFFER callback function](nc-wdfrequest-pfn-wdfrequestretrieveoutputbuffer.md) | TBD |
| [PFN_WDFREQUESTWDMGETIRP callback function](nc-wdfrequest-pfn-wdfrequestwdmgetirp.md) | TBD |
| [PFN_WDFREQUESTFORMATREQUESTUSINGCURRENTTYPE callback function](nc-wdfrequest-pfn-wdfrequestformatrequestusingcurrenttype.md) | TBD |
| [EVT_WDF_REQUEST_CANCEL callback](nc-wdfrequest-evt-wdf-request-cancel.md) | A driver's EvtRequestCancel event callback function handles operations that must be performed when an I/O request is canceled. |
| [PFN_WDFREQUESTCREATEFROMIRP callback function](nc-wdfrequest-pfn-wdfrequestcreatefromirp.md) | TBD |
| [PFN_WDFREQUESTREQUEUE callback function](nc-wdfrequest-pfn-wdfrequestrequeue.md) | TBD |
| [PFN_WDFREQUESTFORWARDTOIOQUEUE callback function](nc-wdfrequest-pfn-wdfrequestforwardtoioqueue.md) | TBD |
| [PFN_WDFREQUESTREUSE callback function](nc-wdfrequest-pfn-wdfrequestreuse.md) | TBD |
| [PFN_WDFREQUESTRETRIEVEUNSAFEUSERINPUTBUFFER callback function](nc-wdfrequest-pfn-wdfrequestretrieveunsafeuserinputbuffer.md) | TBD |
| [PFN_WDFREQUESTCREATE callback function](nc-wdfrequest-pfn-wdfrequestcreate.md) | TBD |
| [PFN_WDFREQUESTGETCOMPLETIONPARAMS callback function](nc-wdfrequest-pfn-wdfrequestgetcompletionparams.md) | TBD |
| [PFN_WDFREQUESTSETACTIVITYID callback function](nc-wdfrequest-pfn-wdfrequestsetactivityid.md) | TBD |
| [PFN_WDFREQUESTUNMARKCANCELABLE callback function](nc-wdfrequest-pfn-wdfrequestunmarkcancelable.md) | TBD |
| [PFN_WDFREQUESTSTOPACKNOWLEDGE callback function](nc-wdfrequest-pfn-wdfrequeststopacknowledge.md) | TBD |
| [PFN_WDFREQUESTGETFILEOBJECT callback function](nc-wdfrequest-pfn-wdfrequestgetfileobject.md) | TBD |
| [PFN_WDFREQUESTGETUSERMODEDRIVERINITIATEDIO callback function](nc-wdfrequest-pfn-wdfrequestgetusermodedriverinitiatedio.md) | TBD |
| [PFN_WDFREQUESTISFROMUSERMODEDRIVER callback function](nc-wdfrequest-pfn-wdfrequestisfromusermodedriver.md) | TBD |
| [PFN_WDFREQUESTSETUSERMODEDRIVERINITIATEDIO callback function](nc-wdfrequest-pfn-wdfrequestsetusermodedriverinitiatedio.md) | TBD |
| [PFN_WDFREQUESTSEND callback function](nc-wdfrequest-pfn-wdfrequestsend.md) | TBD |
| [PFN_WDFREQUESTGETINFORMATION callback function](nc-wdfrequest-pfn-wdfrequestgetinformation.md) | TBD |
| [PFN_WDFREQUESTRETRIEVEOUTPUTMEMORY callback function](nc-wdfrequest-pfn-wdfrequestretrieveoutputmemory.md) | TBD |
| [PFN_WDFREQUESTRETRIEVEOUTPUTWDMMDL callback function](nc-wdfrequest-pfn-wdfrequestretrieveoutputwdmmdl.md) | TBD |
| [PFN_WDFREQUESTCOMPLETEWITHINFORMATION callback function](nc-wdfrequest-pfn-wdfrequestcompletewithinformation.md) | TBD |
| [PFN_WDFREQUESTISCANCELED callback function](nc-wdfrequest-pfn-wdfrequestiscanceled.md) | TBD |
| [PFN_WDFREQUESTGETPARAMETERS callback function](nc-wdfrequest-pfn-wdfrequestgetparameters.md) | TBD |
| [PFN_WDFREQUESTALLOCATETIMER callback function](nc-wdfrequest-pfn-wdfrequestallocatetimer.md) | TBD |
| [PFN_WDFREQUESTCANCELSENTREQUEST callback function](nc-wdfrequest-pfn-wdfrequestcancelsentrequest.md) | TBD |
| [PFN_WDFREQUESTCOMPLETEWITHPRIORITYBOOST callback function](nc-wdfrequest-pfn-wdfrequestcompletewithpriorityboost.md) | TBD |
| [PFN_WDFREQUESTMARKCANCELABLEEX callback function](nc-wdfrequest-pfn-wdfrequestmarkcancelableex.md) | TBD |
| [EVT_WDF_REQUEST_IMPERSONATE callback](nc-wdfrequest-evt-wdf-request-impersonate.md) | A driver's EvtRequestImpersonate event callback function performs tasks at the requested impersonation level, such as opening a protected file. |
| [EVT_WDF_REQUEST_COMPLETION_ROUTINE callback](nc-wdfrequest-evt-wdf-request-completion-routine.md) | A driver's CompletionRoutine event callback function executes when another driver completes a specified I/O request. |
| [PFN_WDFREQUESTISFROM32BITPROCESS callback function](nc-wdfrequest-pfn-wdfrequestisfrom32bitprocess.md) | TBD |
| [PFN_WDFREQUESTGETREQUESTORPROCESSID callback function](nc-wdfrequest-pfn-wdfrequestgetrequestorprocessid.md) | TBD |
| [PFN_WDFREQUESTPROBEANDLOCKUSERBUFFERFORREAD callback function](nc-wdfrequest-pfn-wdfrequestprobeandlockuserbufferforread.md) | TBD |
| [PFN_WDFREQUESTCHANGETARGET callback function](nc-wdfrequest-pfn-wdfrequestchangetarget.md) | TBD |
| [PFN_WDFREQUESTFORWARDTOPARENTDEVICEIOQUEUE callback function](nc-wdfrequest-pfn-wdfrequestforwardtoparentdeviceioqueue.md) | TBD |
| [PFN_WDFREQUESTISRESERVED callback function](nc-wdfrequest-pfn-wdfrequestisreserved.md) | TBD |
| [PFN_WDFREQUESTSETINFORMATION callback function](nc-wdfrequest-pfn-wdfrequestsetinformation.md) | TBD |
| [PFN_WDFREQUESTPROBEANDLOCKUSERBUFFERFORWRITE callback function](nc-wdfrequest-pfn-wdfrequestprobeandlockuserbufferforwrite.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfRequestCreateFromIrp function](nf-wdfrequest-wdfrequestcreatefromirp.md) | The WdfRequestCreateFromIrp method creates a framework request object from a specified WDM IRP. |
| [WdfRequestSetUserModeDriverInitiatedIo function](nf-wdfrequest-wdfrequestsetusermodedriverinitiatedio.md) | The WdfRequestSetUserModeDriverInitiatedIo method indicates to kernel-mode drivers that sit below the UMDF driver in the same device stack that a particular request should be treated as though it came from a UMDF driver. |
| [WDF_REQUEST_FORWARD_OPTIONS_INIT function](nf-wdfrequest-wdf-request-forward-options-init.md) | The WDF_REQUEST_FORWARD_OPTIONS_INIT function initializes a WDF_REQUEST_FORWARD_OPTIONS structure. |
| [WdfRequestGetUserModeDriverInitiatedIo function](nf-wdfrequest-wdfrequestgetusermodedriverinitiatedio.md) | TBD |
| [WdfRequestRetrieveUnsafeUserInputBuffer function](nf-wdfrequest-wdfrequestretrieveunsafeuserinputbuffer.md) | The WdfRequestRetrieveUnsafeUserInputBuffer method retrieves an I/O request's input buffer, if the request's technique for accessing data buffers is neither buffered nor direct I/O. |
| [WdfRequestMarkCancelableEx function](nf-wdfrequest-wdfrequestmarkcancelableex.md) | The WdfRequestMarkCancelableEx method enables cancellation of a specified I/O request. |
| [WdfRequestWdmGetIrp function](nf-wdfrequest-wdfrequestwdmgetirp.md) | The WdfRequestWdmGetIrp method returns the WDM IRP structure that is associated with a specified framework request object. |
| [WDF_REQUEST_PARAMETERS_INIT function](nf-wdfrequest-wdf-request-parameters-init.md) | The WDF_REQUEST_PARAMETERS_INIT function initializes a WDF_REQUEST_PARAMETERS structure. |
| [WDF_REQUEST_SEND_OPTIONS_INIT function](nf-wdfrequest-wdf-request-send-options-init.md) | The WDF_REQUEST_SEND_OPTIONS_INIT function initializes a driver's WDF_REQUEST_SEND_OPTIONS structure. |
| [WdfRequestProbeAndLockUserBufferForRead function](nf-wdfrequest-wdfrequestprobeandlockuserbufferforread.md) | The WdfRequestProbeAndLockUserBufferForRead method verifies that an I/O request's user-mode buffer is readable, and then it locks the buffer's physical memory pages so drivers in the driver stack can read the buffer. |
| [WdfRequestGetRequestorMode function](nf-wdfrequest-wdfrequestgetrequestormode.md) | The WdfRequestGetRequestorMode method returns the processor access mode of the originator of a specified I/O request. |
| [WDF_REQUEST_COMPLETION_PARAMS_INIT function](nf-wdfrequest-wdf-request-completion-params-init.md) | The WDF_REQUEST_COMPLETION_PARAMS_INIT function initializes a WDF_REQUEST_COMPLETION_PARAMS structure. |
| [WdfRequestIsFrom32BitProcess function](nf-wdfrequest-wdfrequestisfrom32bitprocess.md) | The WdfRequestIsFrom32BitProcess method checks whether the originator of a specified I/O request is a 32-bit user-mode application. |
| [WdfRequestGetRequestorProcessId function](nf-wdfrequest-wdfrequestgetrequestorprocessid.md) | The WdfRequestGetRequestorProcessId method retrieves the identifier of the process that sent an I/O request. |
| [WdfRequestGetInformation function](nf-wdfrequest-wdfrequestgetinformation.md) | The WdfRequestGetInformation method returns completion status information for a specified I/O request. |
| [WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT function](nf-wdfrequest-wdf-request-send-options-set-timeout.md) | The WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT function sets a time-out value in a driver's WDF_REQUEST_SEND_OPTIONS structure. |
| [WdfRequestProbeAndLockUserBufferForWrite function](nf-wdfrequest-wdfrequestprobeandlockuserbufferforwrite.md) | The WdfRequestProbeAndLockUserBufferForWrite method verifies that an I/O request's user-mode buffer is writeable, and then it locks the buffer's physical memory pages so drivers in the driver stack can write into the buffer. |
| [WdfRequestCompleteWithInformation function](nf-wdfrequest-wdfrequestcompletewithinformation.md) | The WdfRequestCompleteWithInformation method stores completion information and then completes a specified I/O request with a supplied completion status. |
| [WdfRequestSetCompletionRoutine function](nf-wdfrequest-wdfrequestsetcompletionroutine.md) | The WdfRequestSetCompletionRoutine method registers or deregisters a completion routine for the specified framework request object. |
| [WdfRequestRetrieveOutputWdmMdl function](nf-wdfrequest-wdfrequestretrieveoutputwdmmdl.md) | The WdfRequestRetrieveOutputWdmMdl method retrieves a memory descriptor list (MDL) that represents an I/O request's output buffer. |
| [WdfRequestReuse function](nf-wdfrequest-wdfrequestreuse.md) | The WdfRequestReuse method reinitializes a framework request object so that it can be reused. |
| [WdfRequestRetrieveInputWdmMdl function](nf-wdfrequest-wdfrequestretrieveinputwdmmdl.md) | The WdfRequestRetrieveInputWdmMdl method retrieves a memory descriptor list (MDL) that represents an I/O request's input buffer. |
| [WDF_REQUEST_REUSE_PARAMS_INIT function](nf-wdfrequest-wdf-request-reuse-params-init.md) | The WDF_REQUEST_REUSE_PARAMS_INIT function initializes a driver's WDF_REQUEST_REUSE_PARAMS structure. |
| [WdfRequestGetParameters function](nf-wdfrequest-wdfrequestgetparameters.md) | The WdfRequestGetParameters method retrieves the parameters that are associated with a specified framework request object. |
| [WdfRequestIsFromUserModeDriver function](nf-wdfrequest-wdfrequestisfromusermodedriver.md) | The WdfRequestIsFromUserModeDriver method indicates whether an I/O request came from a user-mode driver or an application. |
| [WdfRequestGetStatus function](nf-wdfrequest-wdfrequestgetstatus.md) | The WdfRequestGetStatus method returns the status of an I/O request. |
| [WDF_REQUEST_REUSE_PARAMS_SET_NEW_IRP function](nf-wdfrequest-wdf-request-reuse-params-set-new-irp.md) | The WDF_REQUEST_REUSE_PARAMS_SET_NEW_IRP function sets a new IRP in a driver's WDF_REQUEST_REUSE_PARAMS structure. |
| [WdfRequestSetActivityId function](nf-wdfrequest-wdfrequestsetactivityid.md) | The WdfRequestSetActivityId method associates an activity identifier with an I/O request. |
| [WdfRequestRetrieveInputBuffer function](nf-wdfrequest-wdfrequestretrieveinputbuffer.md) | The WdfRequestRetrieveInputBuffer method retrieves an I/O request's input buffer. |
| [WdfRequestGetFileObject function](nf-wdfrequest-wdfrequestgetfileobject.md) | The WdfRequestGetFileObject method retrieves the framework file object that is associated with a specified I/O request. |
| [WdfRequestForwardToParentDeviceIoQueue function](nf-wdfrequest-wdfrequestforwardtoparentdeviceioqueue.md) | The WdfRequestForwardToParentDeviceIoQueue method requeues an I/O request from a child device's I/O queue to a specified I/O queue of the child's parent device. |
| [WdfRequestForwardToIoQueue function](nf-wdfrequest-wdfrequestforwardtoioqueue.md) | The WdfRequestForwardToIoQueue method requeues an I/O request to one of the calling driver's I/O queues. |
| [WdfRequestRetrieveUnsafeUserOutputBuffer function](nf-wdfrequest-wdfrequestretrieveunsafeuseroutputbuffer.md) | The WdfRequestRetrieveUnsafeUserOutputBuffer method retrieves an I/O request's output buffer, if the request's technique for accessing data buffers is neither buffered nor direct I/O. |
| [WdfRequestFormatRequestUsingCurrentType function](nf-wdfrequest-wdfrequestformatrequestusingcurrenttype.md) | The WdfRequestFormatRequestUsingCurrentType method formats a specified I/O request so that the driver can forward it, unmodified, to the driver's local I/O target. |
| [WdfRequestImpersonate function](nf-wdfrequest-wdfrequestimpersonate.md) | The WdfRequestImpersonate method registers a driver-supplied event callback function that the framework should call for impersonation. |
| [WdfRequestRetrieveInputMemory function](nf-wdfrequest-wdfrequestretrieveinputmemory.md) | The WdfRequestRetrieveInputMemory method retrieves a handle to a framework memory object that represents an I/O request's input buffer. |
| [WdfRequestAllocateTimer function](nf-wdfrequest-wdfrequestallocatetimer.md) | The WdfRequestAllocateTimer method allocates a timer for a specified I/O request. |
| [WdfRequestCreate function](nf-wdfrequest-wdfrequestcreate.md) | The WdfRequestCreate method creates an empty framework request object. |
| [WdfRequestWdmFormatUsingStackLocation function](nf-wdfrequest-wdfrequestwdmformatusingstacklocation.md) | The WdfRequestWdmFormatUsingStackLocation method formats an I/O request by copying the contents of a specified WDM I/O stack location structure to the next stack location in the request. |
| [WdfRequestChangeTarget function](nf-wdfrequest-wdfrequestchangetarget.md) | The WdfRequestChangeTarget method verifies that a specified I/O request can be sent to a specified I/O target. |
| [WdfRequestRetrieveOutputBuffer function](nf-wdfrequest-wdfrequestretrieveoutputbuffer.md) | The WdfRequestRetrieveOutputBuffer method retrieves an I/O request's output buffer. |
| [WdfRequestStopAcknowledge function](nf-wdfrequest-wdfrequeststopacknowledge.md) | The WdfRequestStopAcknowledge method informs the framework that the driver has stopped processing a specified I/O request. |
| [WdfRequestMarkCancelable function](nf-wdfrequest-wdfrequestmarkcancelable.md) | The WdfRequestMarkCancelable method enables cancellation of a specified I/O request. |
| [WdfRequestGetCompletionParams function](nf-wdfrequest-wdfrequestgetcompletionparams.md) | The WdfRequestGetCompletionParams method retrieves the I/O completion parameters that are associated with a specified framework request object. |
| [WdfRequestGetIoQueue function](nf-wdfrequest-wdfrequestgetioqueue.md) | The WdfRequestGetIoQueue method returns a handle to the framework queue object from which a specified I/O request was delivered. |
| [WdfRequestRequeue function](nf-wdfrequest-wdfrequestrequeue.md) | The WdfRequestRequeue method returns an I/O request to the head of the I/O queue from which it was delivered to the driver. |
| [WdfRequestUnmarkCancelable function](nf-wdfrequest-wdfrequestunmarkcancelable.md) | The WdfRequestUnmarkCancelable method disables cancellation of a specified I/O request. |
| [WdfRequestCompleteWithPriorityBoost function](nf-wdfrequest-wdfrequestcompletewithpriorityboost.md) | The WdfRequestCompleteWithPriorityBoost method completes a specified I/O request and supplies a completion status. It also specifies a value that the system can use to boost the run-time priority of the thread that requested the I/O operation. |
| [WdfRequestCancelSentRequest function](nf-wdfrequest-wdfrequestcancelsentrequest.md) | The WdfRequestCancelSentRequest method attempts to cancel an I/O request that the caller previously submitted to an I/O target. |
| [WdfRequestComplete function](nf-wdfrequest-wdfrequestcomplete.md) | The WdfRequestComplete method completes a specified I/O request and supplies a completion status. |
| [WdfRequestIsCanceled function](nf-wdfrequest-wdfrequestiscanceled.md) | The WdfRequestIsCanceled method determines whether the I/O manager has attempted to cancel a specified I/O request. |
| [WdfRequestGetEffectiveIoType function](nf-wdfrequest-wdfrequestgeteffectiveiotype.md) | The WdfRequestGetEffectiveIoType method returns the buffer access method that UMDF is using for the data buffers of the specified I/O request. |
| [WdfRequestIsReserved function](nf-wdfrequest-wdfrequestisreserved.md) | The WdfRequestIsReserved method determines whether a specified request object is one that the framework reserved to support guaranteed forward progress during low-memory situations. |
| [WdfRequestRetrieveActivityId function](nf-wdfrequest-wdfrequestretrieveactivityid.md) | The WdfRequestRetrieveActivityId method retrieves the current activity identifier associated with an I/O request. |
| [WdfRequestSend function](nf-wdfrequest-wdfrequestsend.md) | The WdfRequestSend method sends a specified I/O request to a specified I/O target. |
| [WdfRequestRetrieveOutputMemory function](nf-wdfrequest-wdfrequestretrieveoutputmemory.md) | The WdfRequestRetrieveOutputMemory method retrieves a handle to a framework memory object that represents an I/O request's output buffer. |
| [WdfRequestSetInformation function](nf-wdfrequest-wdfrequestsetinformation.md) | The WdfRequestSetInformation method sets completion status information for a specified I/O request. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_REQUEST_FORWARD_OPTIONS_FLAGS enumeration](ne-wdfrequest--wdf-request-forward-options-flags.md) | The WDF_REQUEST_FORWARD_OPTIONS_FLAGS enumeration type defines flags that are used in a driver's WDF_REQUEST_FORWARD_OPTIONS structure. |
| [WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration](ne-wdfrequest--wdf-request-send-options-flags.md) | The WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration type defines flags that are used in a driver's WDF_REQUEST_SEND_OPTIONS structure. |
| [WDF_REQUEST_TYPE enumeration](ne-wdfrequest--wdf-request-type.md) | The WDF_REQUEST_TYPE enumeration type identifies types of requests that a framework request object might contain. |
| [WDF_REQUEST_STOP_ACTION_FLAGS enumeration](ne-wdfrequest--wdf-request-stop-action-flags.md) | The WDF_REQUEST_STOP_ACTION_FLAGS enumeration type defines flags that the framework passes to a driver's EvtIoStop callback function. |
| [WDF_REQUEST_REUSE_FLAGS enumeration](ne-wdfrequest--wdf-request-reuse-flags.md) | The WDF_REQUEST_REUSE_FLAGS enumeration type defines flags that are used in a driver's WDF_REQUEST_REUSE_PARAMS structure. |

This header is used in these topics:

- [wdf](..content/_wdf)
