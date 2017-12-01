---
UID: NF.wdfio.WdfIoQueueStopAndPurgeSynchronously
title: WdfIoQueueStopAndPurgeSynchronously
author: windows-driver-content
description: The WdfIoQueueStopAndPurgeSynchronously method prevents an I/O queue from delivering new I/O requests and causes the framework to cancel existing unprocessed requests and driver-owned cancellable requests, but the queue receives and stores new requests.
old-location: wdf\wdfioqueuestopandpurgesynchronously.htm
old-project: wdf
ms.assetid: 406044A5-D1C0-4771-8CDB-CCBC0B801281
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfIoQueueStopAndPurgeSynchronously
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WdfIoQueueStopAndPurgeSynchronously
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: ChangeQueueState, DriverCreate, EvtSurpriseRemoveNoSuspendQueue, NoCancelFromEvtSurpriseRemove
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoQueueStopAndPurgeSynchronously function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>
   The <b>WdfIoQueueStopAndPurgeSynchronously</b> method 
  prevents an I/O queue from delivering new I/O requests and causes the framework to cancel existing unprocessed requests and driver-owned cancellable requests, but the queue receives and stores new requests.</p>


## -syntax

````
void WdfIoQueueStopAndPurgeSynchronously(
  _In_ WDFQUEUE Queue
);
````


## -parameters
<dl>

### -param <i>Queue</i> [in]

<dd>
<p>A handle to a framework queue object.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>This method returns after all the unprocessed and driver-owned requests (not including requests added to the queue after this call is made) are completed or canceled. If new requests are inserted while <b>WdfIoQueueStopAndPurgeSynchronously</b> is in progress, these new requests are not delivered until driver calls <a href="..\wdfio\nf-wdfio-wdfioqueuestart.md">WdfIoQueueStart</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfio.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_changequeuestate">ChangeQueueState</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_evtsurpriseremovenosuspendqueue">EvtSurpriseRemoveNoSuspendQueue</a>, <a href="devtest.kmdf_nocancelfromevtsurpriseremove">NoCancelFromEvtSurpriseRemove</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueuestopandpurge.md">WdfIoQueueStopAndPurge</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoQueueStopAndPurgeSynchronously method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
