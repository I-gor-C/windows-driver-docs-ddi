---
UID: NC:mrx.PMRX_FORCECLOSED_CALLDOWN
title: PMRX_FORCECLOSED_CALLDOWN
author: windows-driver-content
description: The MRxForceClosed routine is called by RDBSS to request that a network mini-redirector force a close. This routine is called when the condition of the SRV_OPEN structure is not good or the SRV_OPEN structure is marked as closed.
old-location: ifsk\mrxforceclosed.htm
old-project: ifsk
ms.assetid: 81cbde46-e538-47dd-8b4a-e80dfb5e5b65
ms.author: windowsdriverdev
ms.date: 4/16/2018
ms.keywords: MRxForceClosed, MRxForceClosed routine [Installable File System Drivers], PMRX_FORCECLOSED_CALLDOWN, ifsk.mrxforceclosed, mrx/MRxForceClosed, mrxref_4ebb7c98-0f0f-402e-b6f7-53e75c5cac54.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: mrx.h
req.include-header: Mrx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	mrx.h
api_name:
-	MRxForceClosed
product:
- Windows
targetos: Windows
req.typenames: 
---

# PMRX_FORCECLOSED_CALLDOWN callback function


## -description


The<i> MRxForceClosed</i> routine is called by <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs/the-rdbss-driver-and-library">RDBSS</a> to request that a network mini-redirector force a close. This routine is called when the condition of the SRV_OPEN structure is not good or the SRV_OPEN structure is marked as closed.


## -parameters




### -param SrvOpen








#### - pSrvOpen [in]

A pointer to the SRV_OPEN structure. 


## -returns



<i>MRxForceClosed</i> returns STATUS_SUCCESS on success or an appropriate NTSTATUS value, such as the following: 

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_NOT_IMPLEMENTED</b></dt>
</dl>
</td>
<td width="60%">
This routine is not implemented. 

</td>
</tr>
</table>
 




## -remarks



<i>MRxForceClosed</i> requests that the network mini-redirector force a close of a file system object.

<i>MRxForceClosed</i> is called by <a href="https://msdn.microsoft.com/library/windows/hardware/ff554432">RxFinalizeSrvOpen</a> as part of the process to finalize an SRV_OPEN structure. 




## -see-also




<a href="https://msdn.microsoft.com/library/windows/hardware/ff549838">MRxAreFilesAliased</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549841">MRxCleanupFobx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549845">MRxCloseSrvOpen</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549847">MRxCollapseOpen</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549862">MRxCreate</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549871">MRxDeallocateForFcb</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549872">MRxDeallocateForFobx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549878">MRxExtendForCache</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549879">MRxExtendForNonCache</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550669">MRxFlush</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550691">MRxIsLockRealizable</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550817">MRxShouldTryToCollapseThisOpen</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550839">MRxTruncate</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550844">MRxZeroExtend</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554432">RxFinalizeSrvOpen</a>
 

 

