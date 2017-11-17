---
UID: NF.mrxfcb.RxReleaseFcbResourceForThreadInMRx
title: RxReleaseFcbResourceForThreadInMRx
author: windows-driver-content
description: RxReleaseFcbResourceForThreadInMRx releases the FCB resource acquired by a network mini-redirector driver with a particular thread ID.
old-location: ifsk\rxreleasefcbresourceforthreadinmrx.htm
ms.assetid: 86b6f18b-4088-4fa3-ace3-f083f61ef0d0
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: mrxfcb.h
req.include-header: Mrxfcb.h
req.target-type: Desktop
req.target-min-winverclnt: RxReleaseFcbResourceForThreadInMRx is only available on Windows Server 2003 SP1 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxReleaseFcbResourceForThreadInMRx
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
ms.keywords: RxReleaseFcbResourceForThreadInMRx
req.iface: 
---

# RxReleaseFcbResourceForThreadInMRx function



## -description
<p><b>RxReleaseFcbResourceForThreadInMRx</b> releases the FCB resource acquired by a network mini-redirector driver with a particular thread ID. </p>


## -syntax

````
VOID RxReleaseFcbResourceForThreadInMRx(
  _In_    PRX_CONTEXT      pRxContext,
  _Inout_ PMRX_FCB         MrxFcb,
  _In_    ERESOURCE_THREAD ResourceThreadId
);
````


## -parameters
<dl>

### -param <i>pRxContext</i> [in]

<dd>
<p>A pointer to the RX_CONTEXT structure.</p>
</dd>

### -param <i>MrxFcb</i> [in, out]

<dd>
<p>A pointer to the FCB. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>ResourceThreadId</i> [in]

<dd>
<p>The thread ID that originally acquired the resource.</p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>The synchronization resources of interest to a network mini-redirector driver are primarily associated with the FCB. There is a paging I/O resource and a regular resource. The paging I/O resource is managed internally by RDBSS. The only resource accessible to a network mini-redirector driver is the regular resource. </p>

<p>The <b>RxReleaseFcbResourceForThreadInMRx</b> routine will release an FCB resource previously acquired for a particular thread ID. This resource would have been acquired by calling <b>RxAcquireExclusiveFcbResourceInMRx</b>, <b>RxAcquireSharedFcbResourceInMRx</b>, or <b>RxAcquireSharedFcbResourceInMRxEx</b>. If there are any pending buffering state change requests for this FCB, then these buffering state changes will be processed first before the <b>RxReleaseFcbResourceForThreadInMRx</b> routine returns.</p>

<p>The synchronization resources of interest to a network mini-redirector driver are primarily associated with the FCB. There is a paging I/O resource and a regular resource. The paging I/O resource is managed internally by RDBSS. The only resource accessible to a network mini-redirector driver is the regular resource. </p>

<p>The <b>RxReleaseFcbResourceForThreadInMRx</b> routine will release an FCB resource previously acquired for a particular thread ID. This resource would have been acquired by calling <b>RxAcquireExclusiveFcbResourceInMRx</b>, <b>RxAcquireSharedFcbResourceInMRx</b>, or <b>RxAcquireSharedFcbResourceInMRxEx</b>. If there are any pending buffering state change requests for this FCB, then these buffering state changes will be processed first before the <b>RxReleaseFcbResourceForThreadInMRx</b> routine returns.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>RxReleaseFcbResourceForThreadInMRx is only available on Windows Server 2003 SP1 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mrxfcb.h (include Mrxfcb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553363">RxAcquireExclusiveFcbResourceInMRx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553372">RxAcquireSharedFcbResourceInMRx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553375">RxAcquireSharedFcbResourceInMRxEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554699">RxReleaseFcbResourceInMRx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxReleaseFcbResourceForThreadInMRx function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
