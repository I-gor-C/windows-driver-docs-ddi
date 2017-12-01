---
UID: NE.wdfrequest._WDF_REQUEST_STOP_ACTION_FLAGS
title: WDF_REQUEST_STOP_ACTION_FLAGS
author: windows-driver-content
description: The WDF_REQUEST_STOP_ACTION_FLAGS enumeration type defines flags that the framework passes to a driver's EvtIoStop callback function.
old-location: wdf\wdf_request_stop_action_flags.htm
old-project: wdf
ms.assetid: 01f95aee-60aa-4d6f-88a9-c0fa6ea6a09a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfRegistryWdmGetHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_REQUEST_STOP_ACTION_FLAGS
req.alt-loc: wdfrequest.h
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
req.iface: 
req.product: Windows 10 or later.
---

# WDF_REQUEST_STOP_ACTION_FLAGS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_REQUEST_STOP_ACTION_FLAGS</b> enumeration type defines flags that the framework passes to a driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function.</p>


## -syntax

````
typedef enum _WDF_REQUEST_STOP_ACTION_FLAGS { 
  WdfRequestStopActionInvalid      = 0,
  WdfRequestStopActionSuspend      = 0x01,
  WdfRequestStopActionPurge        = 0x2,
  WdfRequestStopRequestCancelable  = 0x10000000
} WDF_REQUEST_STOP_ACTION_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="WdfRequestStopActionInvalid"></a><a id="wdfrequeststopactioninvalid"></a><a id="WDFREQUESTSTOPACTIONINVALID"></a><b>WdfRequestStopActionInvalid</b>

<dd>
<p>Reserved for internal use only.</p>
</dd>

### -field <a id="WdfRequestStopActionSuspend"></a><a id="wdfrequeststopactionsuspend"></a><a id="WDFREQUESTSTOPACTIONSUSPEND"></a><b>WdfRequestStopActionSuspend</b>

<dd>
<p>The framework is stopping the I/O queue because the device is leaving its working (D0) state.</p>
</dd>

### -field <a id="WdfRequestStopActionPurge"></a><a id="wdfrequeststopactionpurge"></a><a id="WDFREQUESTSTOPACTIONPURGE"></a><b>WdfRequestStopActionPurge</b>

<dd>
<p>The framework is stopping the I/O queue because the device is being removed. </p>
</dd>

### -field <a id="WdfRequestStopRequestCancelable"></a><a id="wdfrequeststoprequestcancelable"></a><a id="WDFREQUESTSTOPREQUESTCANCELABLE"></a><b>WdfRequestStopRequestCancelable</b>

<dd>
<p>The I/O request is cancelable.</p>
</dd>
</dl>

## -remarks
<p>When the framework calls a driver's <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function, it sets either the <b>WdfRequestStopActionSuspend</b> or <b>WdfRequestStopActionPurge</b> flag. If the request is cancelable, the framework also sets the <b>WdfRequestStopRequestCancelable</b> flag.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
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
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REQUEST_STOP_ACTION_FLAGS enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
