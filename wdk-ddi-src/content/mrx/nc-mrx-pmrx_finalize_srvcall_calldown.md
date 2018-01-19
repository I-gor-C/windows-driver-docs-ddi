---
UID : NC:mrx.PMRX_FINALIZE_SRVCALL_CALLDOWN
title : PMRX_FINALIZE_SRVCALL_CALLDOWN
author : windows-driver-content
description : The MRxFinalizeSrvCall routine is called by RDBSS to request that a network mini-redirector finalize an SRV_CALL structure.
old-location : ifsk\mrxfinalizesrvcall.htm
old-project : ifsk
ms.assetid : f870334a-cf39-47a2-868a-f6fd7c3aee1c
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _SetDSMCounters_IN, SetDSMCounters_IN, *PSetDSMCounters_IN
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : mrx.h
req.include-header : Mrx.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : MRxFinalizeSrvCall
req.alt-loc : mrx.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : SetDSMCounters_IN, *PSetDSMCounters_IN
---


# PMRX_FINALIZE_SRVCALL_CALLDOWN callback function
The <i>MRxFinalizeSrvCall</i> routine is called by <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs/the-rdbss-driver-and-library">RDBSS</a> to request that a network mini-redirector finalize an SRV_CALL structure.

## Syntax

```
PMRX_FINALIZE_SRVCALL_CALLDOWN PmrxFinalizeSrvcallCalldown;

NTSTATUS PmrxFinalizeSrvcallCalldown(
  IN OUT PMRX_SRV_CALL SrvCall,
  IN BOOLEAN Force
)
{...}
```

## Parameters

`SrvCall`



`Force`

A pointer to a Boolean value that indicates if the disconnect is to be enforced immediately, ignoring the reference count on the SRV_CALL structure. The <i>Force</i> parameter is the <i>ForceFinalize</i> parameter passed to the <a href="..\fcb\nf-fcb-rxfinalizesrvcall.md">RxFinalizeSrvCall</a> routine. This action triggers a call to <i>MRxFinalizeSrvCall</i>.


## Return Value

<i>MRxFinalizeSrvCall</i> returns STATUS_SUCCESS on success.

## Remarks

<i>MRxFinalizeSrvCall</i> is called when RDBSS is tearing down an SRV_CALL structure. The network mini-redirector is expected to close its connection to the server. 

<i>MRxFinalizeSrvCall</i> is called by RDBSS after receiving an <a href="..\fcb\nf-fcb-rxfinalizesrvcall.md">RxFinalizeSrvCall</a> call. If <a href="..\fcb\nf-fcb-rxfinalizenetroot.md">RxFinalizeNetRoot</a> is called from a different process than the RDBSS system process, then the call to <i>MRxFinalizeSrvCall</i> is posted to a worker thread for later execution. At some later time <b>RxFinalizeSrvCall</b> is called to complete the finalization of the SRV_CALL structure. 

RDBSS ignores the return value from the <i>MRxFinalizeSrvCall</i> call.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | mrx.h (include Mrx.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549864">MRxCreateSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549869">MRxCreateVNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550649">MRxExtractNetRootName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550653">MRxFinalizeNetRoot</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxfinalizesrvcall.md">RxFinalizeSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550663">MRxFinalizeVNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550750">MRxPreparseName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550824">MRxSrvCallWinnerNotify</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxFinalizeSrvCall routine%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>