---
UID: NF.wudfddi.IWDFIoQueue.ConfigureRequestDispatching
title: IWDFIoQueue::ConfigureRequestDispatching
author: windows-driver-content
description: The ConfigureRequestDispatching method configures the queuing of I/O requests of the given type.
old-location: wdf\iwdfioqueue_configurerequestdispatching.htm
old-project: wdf
ms.assetid: 376b0cc3-8189-499e-ad7f-5844f8cb4221
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFIoQueue, ConfigureRequestDispatching, IWDFIoQueue::ConfigureRequestDispatching
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFIoQueue.ConfigureRequestDispatching
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFIoQueue
req.product: Windows 10 or later.
---

# IWDFIoQueue::ConfigureRequestDispatching method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>ConfigureRequestDispatching</b> method configures the queuing of I/O requests of the given type.</p>


## -syntax

````
HRESULT ConfigureRequestDispatching(
  [in] WDF_REQUEST_TYPE RequestType,
  [in] BOOL             Forward
);
````


## -parameters
<dl>

### -param <i>RequestType</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552503">WDF_REQUEST_TYPE</a>-typed value that identifies the request type to be queued. The only valid values are <b>WdfRequestCreate</b>, <b>WdfRequestRead</b>, <b>WdfRequestWrite</b>, and <b>WdfRequestDeviceIoControl</b>.</p>
</dd>

### -param <i>Forward</i> [in]

<dd>
<p>A BOOL value that specifies whether requests of the specified type are queued. <b>TRUE</b> indicates to enable queuing requests; <b>FALSE</b> indicates to disable queuing requests.</p>
</dd>
</dl>

## -returns
<p><b>ConfigureRequestDispatching</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h. </p>

## -remarks
<p>The driver can call the <b>ConfigureRequestDispatching</b> method multiple times to configure how each request type is dispatched to the I/O queue. </p>

<p>The following code example shows how to configure forwarding for IOCTL requests.</p>

<p>The driver can call the <b>ConfigureRequestDispatching</b> method multiple times to configure how each request type is dispatched to the I/O queue. </p>

<p>The following code example shows how to configure forwarding for IOCTL requests.</p>

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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558943">IWDFIoQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552503">WDF_REQUEST_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoQueue::ConfigureRequestDispatching method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
