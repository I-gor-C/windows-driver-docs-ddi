---
UID: NF.mrxfcb.RxReleaseFcbResourceInMRx
title: RxReleaseFcbResourceInMRx function
author: windows-driver-content
description: RxReleaseFcbResourceInMRx releases the FCB resource acquired by a network mini-redirector driver.
old-location: ifsk\rxreleasefcbresourceinmrx.htm
old-project: ifsk
ms.assetid: 48308dcd-e423-4c25-9fec-3a423043e988
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RxReleaseFcbResourceInMRx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mrxfcb.h
req.include-header: Mrxfcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxReleaseFcbResourceInMRx
req.alt-loc: mrxfcb.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
---

# RxReleaseFcbResourceInMRx function



## -description
<b>RxReleaseFcbResourceInMRx</b> releases the FCB resource acquired by a network mini-redirector driver. 


## -syntax

````
VOID RxReleaseFcbResourceInMRx(
   PMRX_FCB pFcb
);
````


## -parameters

### -param pFcb 

A pointer to the FCB. This parameter is required and cannot be <b>NULL</b>. 

## -returns
None 

## -remarks
The synchronization resources of interest to a network mini-redirector driver are primarily associated with the FCB. There is a paging I/O resource and a regular resource. The paging I/O resource is managed internally by RDBSS. The only resource accessible to a network mini-redirector driver is the regular resource. 

The <b>RxReleaseFcbResourceInMRx</b> routine will release an FCB resource previously acquired by calling <b>RxAcquireExclusiveFcbResourceInMRx</b>, <b>RxAcquireSharedFcbResourceInMRx</b>, or <b>RxAcquireSharedFcbResourceInMRxEx</b>. If there are any pending buffering state change requests for this FCB, then these buffering state changes will be processed first before the <b>RxReleaseFcbResourceInMRx</b> routine returns. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Mrxfcb.h (include Mrxfcb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= APC_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.rxacquireexclusivefcbresourceinmrx">RxAcquireExclusiveFcbResourceInMRx</a>
</dt>
<dt>
<a href="ifsk.rxacquiresharedfcbresourceinmrx">RxAcquireSharedFcbResourceInMRx</a>
</dt>
<dt>
<a href="ifsk.rxacquiresharedfcbresourceinmrxex">RxAcquireSharedFcbResourceInMRxEx</a>
</dt>
<dt>
<a href="ifsk.rxreleasefcbresourceforthreadinmrx">RxReleaseFcbResourceForThreadInMRx</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxReleaseFcbResourceInMRx function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
