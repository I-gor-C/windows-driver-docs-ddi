---
UID: NF.wudfddi.IQueueCallbackDeviceIoControl.OnDeviceIoControl
title: IQueueCallbackDeviceIoControl::OnDeviceIoControl
author: windows-driver-content
description: The OnDeviceIoControl method is called to handle a device I/O control request when an application performs a specific operation on a device through the Microsoft Win32 OnDeviceIoControl function.
old-location: wdf\iqueuecallbackdeviceiocontrol_ondeviceiocontrol.htm
old-project: wdf
ms.assetid: ed0eac1a-8e41-44c3-a538-9ec48492425f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IQueueCallbackDeviceIoControl, OnDeviceIoControl, IQueueCallbackDeviceIoControl::OnDeviceIoControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IQueueCallbackDeviceIoControl.OnDeviceIoControl
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IQueueCallbackDeviceIoControl
req.product: Windows 10 or later.
---

# IQueueCallbackDeviceIoControl::OnDeviceIoControl method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnDeviceIoControl</b> method is called to handle a device I/O control request when an application performs a specific operation on a device through the Microsoft Win32 <b>OnDeviceIoControl</b> function. </p>


## -syntax

````
void  OnDeviceIoControl(
  [in] IWDFIoQueue   *pWdfQueue,
  [in] IWDFIoRequest *pWdfRequest,
  [in] ULONG         ControlCode,
  [in] SIZE_T        InBufferSize,
  [in] SIZE_T        OutBufferSize
);
````


## -parameters
<dl>

### -param <i>pWdfQueue</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558943">IWDFIoQueue</a> interface for the I/O queue object that the request arrives from. </p>
</dd>

### -param <i>pWdfRequest</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a> interface that represents the framework request object. </p>
</dd>

### -param <i>ControlCode</i> [in]

<dd>
<p>The driver-defined or system-defined I/O control code (IOCTL) that identifies the specific operation to be performed and that is associated with the request.</p>
</dd>

### -param <i>InBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the input buffer for the request.</p>
</dd>

### -param <i>OutBufferSize</i> [in]

<dd>
<p>The size, in bytes, of the output buffer for the request.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556852">IQueueCallbackDeviceIoControl</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. </p>

<p>A driver can implement a single <b>OnDeviceIoControl</b> method for all I/O queues or separate <b>OnDeviceIoControl</b> methods for each I/O queue. </p>

<p>The <b>OnDeviceIoControl</b> method receives every device I/O control request type from a queue. (The request type is identified by the <b>WdfRequestDeviceIoControl</b> value of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552503">WDF_REQUEST_TYPE</a> enumeration type for the request.) </p>

<p>For more information about the driver's methods that are associated with queues and that the framework calls, see <a href="wdf.i_o_queue_event_callback_functions">I/O Queue Event Callback Functions</a>. The <b>OnDeviceIoControl</b> method must process each received device I/O control request. For more information about how UMDF drivers process I/O requests, see <a href="wdf.processing_i_o_requests">Processing I/O Requests</a>.</p>

<p>The driver can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559095">IWDFIoRequest::GetDeviceIoControlParameters</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559100">IWDFIoRequest::GetInputMemory</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff559112">IWDFIoRequest::GetOutputMemory</a> methods to retrieve information about the request and the input and output buffers.</p>

<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556852">IQueueCallbackDeviceIoControl</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. </p>

<p>A driver can implement a single <b>OnDeviceIoControl</b> method for all I/O queues or separate <b>OnDeviceIoControl</b> methods for each I/O queue. </p>

<p>The <b>OnDeviceIoControl</b> method receives every device I/O control request type from a queue. (The request type is identified by the <b>WdfRequestDeviceIoControl</b> value of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552503">WDF_REQUEST_TYPE</a> enumeration type for the request.) </p>

<p>For more information about the driver's methods that are associated with queues and that the framework calls, see <a href="wdf.i_o_queue_event_callback_functions">I/O Queue Event Callback Functions</a>. The <b>OnDeviceIoControl</b> method must process each received device I/O control request. For more information about how UMDF drivers process I/O requests, see <a href="wdf.processing_i_o_requests">Processing I/O Requests</a>.</p>

<p>The driver can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559095">IWDFIoRequest::GetDeviceIoControlParameters</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559100">IWDFIoRequest::GetInputMemory</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff559112">IWDFIoRequest::GetOutputMemory</a> methods to retrieve information about the request and the input and output buffers.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556852">IQueueCallbackDeviceIoControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558943">IWDFIoQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552503">WDF_REQUEST_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IQueueCallbackDeviceIoControl::OnDeviceIoControl method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
