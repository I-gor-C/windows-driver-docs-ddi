---
UID: NE.wudfddi_types._WDF_IO_QUEUE_DISPATCH_TYPE
title: WDF_IO_QUEUE_DISPATCH_TYPE
author: windows-driver-content
description: The WDF_IO_QUEUE_DISPATCH_TYPE enumeration contains values that identify how a driver must receive requests from an I/O queue.
old-location: wdf\wdf_io_queue_dispatch_type_umdf.htm
ms.assetid: 40f4cd91-ba84-426c-b248-6027d1e8d1a4
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi_types.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDF_IO_QUEUE_DISPATCH_TYPE
req.alt-loc: Wudfddi_types.h
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
ms.keywords: WRITE_REGISTER_USHORT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_QUEUE_DISPATCH_TYPE enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
      The <a href="https://msdn.microsoft.com/library/windows/hardware/ff552362">WDF_IO_QUEUE_DISPATCH_TYPE</a> enumeration contains values that identify how a driver must receive requests from an I/O queue.</p>


## -syntax

````
typedef enum _WDF_IO_QUEUE_DISPATCH_TYPE { 
  WdfIoQueueDispatchSequential  = 1,
  WdfIoQueueDispatchParallel    = 2,
  WdfIoQueueDispatchManual      = 3,
  WdfIoQueueDispatchMaximum     = ( WdfIoQueueDispatchManual + 1 )
} WDF_IO_QUEUE_DISPATCH_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfIoQueueDispatchSequential"></a><a id="wdfioqueuedispatchsequential"></a><a id="WDFIOQUEUEDISPATCHSEQUENTIAL"></a><b>WdfIoQueueDispatchSequential</b>

<dd>
<p>The I/O queue's requests are presented to the driver's I/O queue callback functions one at a time. The framework delivers the next request after the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> method to complete the current request.</p>
</dd>

### -field <a id="WdfIoQueueDispatchParallel"></a><a id="wdfioqueuedispatchparallel"></a><a id="WDFIOQUEUEDISPATCHPARALLEL"></a><b>WdfIoQueueDispatchParallel</b>

<dd>
<p>The framework presents requests to the driver's I/O queue callback functions as soon as the requests are available.</p>
</dd>

### -field <a id="WdfIoQueueDispatchManual"></a><a id="wdfioqueuedispatchmanual"></a><a id="WDFIOQUEUEDISPATCHMANUAL"></a><b>WdfIoQueueDispatchManual</b>

<dd>
<p>The framework places requests into the queue but does not deliver them to the driver. The driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558967">IWDFIoQueue::RetrieveNextRequest</a> method to retrieve a request from the queue.</p>
</dd>

### -field <a id="WdfIoQueueDispatchMaximum"></a><a id="wdfioqueuedispatchmaximum"></a><a id="WDFIOQUEUEDISPATCHMAXIMUM"></a><b>WdfIoQueueDispatchMaximum</b>

<dd>
<p>Valid enumeration values were exceeded.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi_types.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558967">IWDFIoQueue::RetrieveNextRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_QUEUE_DISPATCH_TYPE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
