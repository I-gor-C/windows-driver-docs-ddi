---
UID: NS.mrx._MINIRDR_DISPATCH
title: MINIRDR_DISPATCH
author: windows-driver-content
description: 
ms.assetid: 16f61939-902e-4978-8c9c-e9df1422bfae
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: MINIRDR_DISPATCH, MINIRDR_DISPATCH, *PMINIRDR_DISPATCH
req.header: mrx.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# MINIRDR_DISPATCH structure

## -description



## -struct-fields

### -field NODE_TYPE_CODE NodeTypeCode			
 	
### -field NODE_BYTE_SIZE NodeByteSize			
 	
### -field ULONG MRxFlags			
 	
### -field ULONG MRxSrvCallSize			
 	
### -field ULONG MRxNetRootSize			
 	
### -field ULONG MRxVNetRootSize			
 	
### -field ULONG MRxFcbSize			
 	
### -field ULONG MRxSrvOpenSize			
 	
### -field ULONG MRxFobxSize			
 	
### -field PMRX_CALLDOWN_CTX MRxStart			
 	
### -field PMRX_CALLDOWN_CTX MRxStop			
 	
### -field PMRX_CALLDOWN MRxCancel			
 	
### -field PMRX_CALLDOWN MRxCreate			
 	
### -field PMRX_CALLDOWN MRxCollapseOpen			
 	
### -field PMRX_CALLDOWN MRxShouldTryToCollapseThisOpen			
 	
### -field PMRX_CALLDOWN MRxFlush			
 	
### -field PMRX_CALLDOWN MRxZeroExtend			
 	
### -field PMRX_CALLDOWN MRxTruncate			
 	
### -field PMRX_CALLDOWN MRxCleanupFobx			
 	
### -field PMRX_CALLDOWN MRxCloseSrvOpen			
 	
### -field PMRX_DEALLOCATE_FOR_FCB MRxDeallocateForFcb			
 	
### -field PMRX_DEALLOCATE_FOR_FOBX MRxDeallocateForFobx			
 	
### -field PMRX_IS_LOCK_REALIZABLE MRxIsLockRealizable			
 	
### -field PMRX_FORCECLOSED_CALLDOWN MRxForceClosed			
 	
### -field PMRX_CHKFCB_CALLDOWN MRxAreFilesAliased			
 	
### -field PMRX_CALLDOWN MRxOpenPrintFile			
 	
### -field PMRX_CALLDOWN MRxClosePrintFile			
 	
### -field PMRX_CALLDOWN MRxWritePrintFile			
 	
### -field PMRX_CALLDOWN MRxEnumeratePrintQueue			
 	
### -field PMRX_CALLDOWN MRxClosedSrvOpenTimeOut			
 	
### -field PMRX_CALLDOWN MRxClosedFcbTimeOut			
 	
### -field PMRX_CALLDOWN MRxQueryDirectory			
 	
### -field PMRX_CALLDOWN MRxQueryFileInfo			
 	
### -field PMRX_CALLDOWN MRxSetFileInfo			
 	
### -field PMRX_CALLDOWN MRxSetFileInfoAtCleanup			
 	
### -field PMRX_CALLDOWN MRxQueryEaInfo			
 	
### -field PMRX_CALLDOWN MRxSetEaInfo			
 	
### -field PMRX_CALLDOWN MRxQuerySdInfo			
 	
### -field PMRX_CALLDOWN MRxSetSdInfo			
 	
### -field PMRX_CALLDOWN MRxQueryQuotaInfo			
 	
### -field PMRX_CALLDOWN MRxSetQuotaInfo			
 	
### -field PMRX_CALLDOWN MRxQueryVolumeInfo			
 	
### -field PMRX_CALLDOWN MRxSetVolumeInfo			
 	
### -field PMRX_CHKDIR_CALLDOWN MRxIsValidDirectory			
 	
### -field PMRX_COMPUTE_NEW_BUFFERING_STATE MRxComputeNewBufferingState			
 	
### -field PMRX_CALLDOWN [LOWIO_OP_MAXIMUM + 1] MRxLowIOSubmit			
 	
### -field PMRX_EXTENDFILE_CALLDOWN MRxExtendForCache			
 	
### -field PMRX_EXTENDFILE_CALLDOWN MRxExtendForNonCache			
 	
### -field PMRX_CHANGE_BUFFERING_STATE_CALLDOWN MRxCompleteBufferingStateChangeRequest			
 	
### -field PMRX_CREATE_V_NET_ROOT MRxCreateVNetRoot			
 	
### -field PMRX_FINALIZE_V_NET_ROOT_CALLDOWN MRxFinalizeVNetRoot			
 	
### -field PMRX_FINALIZE_NET_ROOT_CALLDOWN MRxFinalizeNetRoot			
 	
### -field PMRX_UPDATE_NETROOT_STATE MRxUpdateNetRootState			
 	
### -field PMRX_EXTRACT_NETROOT_NAME MRxExtractNetRootName			
 	
### -field PMRX_CREATE_SRVCALL MRxCreateSrvCall			
 	
### -field PMRX_CREATE_SRVCALL MRxCancelCreateSrvCall			
 	
### -field PMRX_SRVCALL_WINNER_NOTIFY MRxSrvCallWinnerNotify			
 	
### -field PMRX_FINALIZE_SRVCALL_CALLDOWN MRxFinalizeSrvCall			
 	
### -field PMRX_CALLDOWN MRxDevFcbXXXControlFile			
 	
### -field PMRX_PREPARSE_NAME MRxPreparseName			
 	
### -field PMRX_GET_CONNECTION_ID MRxGetConnectionId			
 	
### -field ULONG ScavengerTimeout			
 	
## -remarks

## -see-also