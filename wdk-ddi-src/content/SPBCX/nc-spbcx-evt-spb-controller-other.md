---
UID: NC.spbcx.EVT_SPB_CONTROLLER_OTHER
title: EVT_SPB_CONTROLLER_OTHER
author: windows-driver-content
description: An SPB controller driver's EvtSpbControllerIoOther event callback function handles device I/O control requests that are not handled by other event callback functions or by the SPB framework extension (SpbCx).
old-location: spb\evtspbcontrollerioother.htm
ms.assetid: 5A4BC061-4703-4C46-BD5D-A891F3DA8842
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: SPB
req.header: spbcx.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EvtSpbControllerIoOther
req.alt-loc: Spbcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Called at IRQL <= DISPATCH_LEVEL.
ms.keywords: SPB_TRANSFER_LIST_INIT
req.iface: 
req.product: Windows 10 or later.
---

# EVT_SPB_CONTROLLER_OTHER callback



## -description
<p>An SPB controller driver's <i>EvtSpbControllerIoOther</i> event callback function handles device I/O control requests that are not handled by other event callback functions or by the SPB framework extension (SpbCx).</p>


## -prototype

````
EVT_SPB_CONTROLLER_OTHER EvtSpbControllerIoOther;

VOID EvtSpbControllerIoOther(
  _In_ WDFDEVICE  Controller,
  _In_ SPBTARGET  Target,
  _In_ SPBREQUEST Request,
  _In_ size_t     OutputBufferLength,
  _In_ size_t     InputBufferLength,
  _In_ ULONG      IoControlCode
)
{ ... }
````


## -parameters
<dl>

### -param <i>Controller</i> [in]

<dd>
<p>A WDFDEVICE handle to the <a href="kmdf.creating_a_framework_device_object">framework device object</a> that represents the SPB controller.</p>
</dd>

### -param <i>Target</i> [in]

<dd>
<p>An <a href="buses.spbtarget_object_handle">SPBTARGET</a> handle to the target for this I/O request. The target is a peripheral device or port that is attached to the bus. The SPB framework extension (SpbCx) previously assigned this handle to the target in the <a href="https://msdn.microsoft.com/D90DD169-A989-4D08-B1B8-BDE7EC9B7A82">EvtSpbTargetConnect</a> callback that opened the connection to the target.</p>
</dd>

### -param <i>Request</i> [in]

<dd>
<p>The <a href="buses.spbrequest_object_handle">SPBREQUEST</a> handle to the I/O request. Your SPB controller driver must complete this request. For more information, see Remarks.</p>
</dd>

### -param <i>OutputBufferLength</i> [in]

<dd>
<p>The length, in bytes, of the output buffer, if an output buffer is supplied with the request.</p>
</dd>

### -param <i>InputBufferLength</i> [in]

<dd>
<p>The length, in bytes, of the input buffer, if an input buffer is supplied with the request.</p>
</dd>

### -param <i>IoControlCode</i> [in]

<dd>
<p>The I/O control code (IOCTL) for the request. This value is an IOCTL that the SPB framework extension (SpbCx) does not recognize.  For more information, see Remarks.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>SpbCx manages the I/O queue for the SPB controller. If the SPB controller driver registers an <i>EvtSpbControllerIoOther</i> callback function, SpbCx calls this function when a device I/O control request that SpbCx does not support arrives in the controller's I/O queue. The <i>Request</i> parameter value is a handle that encapsulates this request. The SPB controller driver must complete this request either by performing the requested operation or by returning an error status. If the driver does not support the specified IOCTL, the driver should return the STATUS_NOT_SUPPORTED error status. For a list of IOCTLs that SpbCx supports, see <a href="https://msdn.microsoft.com/EED1CBA4-8691-4BEA-89CB-F93DD7E1874F">SpbCx I/O Control Codes</a>.</p>

<p>The <i>EvtSpbControllerIoOther</i> callback enables bus-specific or driver-specific commands to be dispatched to the SPB controller driver as IOCTLs. For example, clients (peripheral drivers) might use these IOCTLs to coordinate bus-specific operations, such as full-duplex data exchanges with a target device on an SPI bus. Such IOCTLs are subject to the same flow-control as the IOCTLs that are supported by SpbCx.</p>

<p>The <i>EvtSpbControllerIoOther</i> callback function is similar to the <a href="https://msdn.microsoft.com/3e3c4c53-e557-4bd1-8b7d-be59dde4b9ce">EvtIoDeviceControl</a> and processes IOCTLs in a similar way. For general information about how WDF drivers handle I/O requests, see <a href="kmdf.framework_request_objects">Framework Request Objects</a>.</p>

<p>An <i>EvtSpbControllerIoOther</i> callback does not return a status value. Instead, the SPB controller driver indicates the status of the requested operation in the completion status for the I/O request.</p>

<p>If an I/O request cannot be completed immediately, the callback function should return without waiting for the SPB controller driver to finish processing the request. The SPB controller driver can later complete the request asynchronously.</p>

<p>An <i>EvtSpbControllerIoOther</i> function must validate the parameter values in the I/O control requests that it receives from user-mode clients. For all <i>EvtSpb</i>Xxx callback functions other than <i>EvtSpbControllerIoOther</i>, SpbCx validates the user-mode parameters before it calls the function.</p>

<p>To register an <i>EvtSpbControllerIoOther</i> callback function, call the <a href="https://msdn.microsoft.com/605E2353-8C82-4005-BB72-4CB44146A253">SpbControllerSetIoOther</a> method.</p>

<p>To define an <i>EvtSpbControllerIoOther</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSpbControllerIoOther</i> callback function that is named <code>MyEvtSpbControllerIoOther</code>, use the EVT_SPB_CONTROLLER_OTHER function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The EVT_SPB_CONTROLLER_OTHER function type is defined in the Spbcx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the EVT_SPB_CONTROLLER_OTHER function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

<p>SpbCx manages the I/O queue for the SPB controller. If the SPB controller driver registers an <i>EvtSpbControllerIoOther</i> callback function, SpbCx calls this function when a device I/O control request that SpbCx does not support arrives in the controller's I/O queue. The <i>Request</i> parameter value is a handle that encapsulates this request. The SPB controller driver must complete this request either by performing the requested operation or by returning an error status. If the driver does not support the specified IOCTL, the driver should return the STATUS_NOT_SUPPORTED error status. For a list of IOCTLs that SpbCx supports, see <a href="https://msdn.microsoft.com/EED1CBA4-8691-4BEA-89CB-F93DD7E1874F">SpbCx I/O Control Codes</a>.</p>

<p>The <i>EvtSpbControllerIoOther</i> callback enables bus-specific or driver-specific commands to be dispatched to the SPB controller driver as IOCTLs. For example, clients (peripheral drivers) might use these IOCTLs to coordinate bus-specific operations, such as full-duplex data exchanges with a target device on an SPI bus. Such IOCTLs are subject to the same flow-control as the IOCTLs that are supported by SpbCx.</p>

<p>The <i>EvtSpbControllerIoOther</i> callback function is similar to the <a href="https://msdn.microsoft.com/3e3c4c53-e557-4bd1-8b7d-be59dde4b9ce">EvtIoDeviceControl</a> and processes IOCTLs in a similar way. For general information about how WDF drivers handle I/O requests, see <a href="kmdf.framework_request_objects">Framework Request Objects</a>.</p>

<p>An <i>EvtSpbControllerIoOther</i> callback does not return a status value. Instead, the SPB controller driver indicates the status of the requested operation in the completion status for the I/O request.</p>

<p>If an I/O request cannot be completed immediately, the callback function should return without waiting for the SPB controller driver to finish processing the request. The SPB controller driver can later complete the request asynchronously.</p>

<p>An <i>EvtSpbControllerIoOther</i> function must validate the parameter values in the I/O control requests that it receives from user-mode clients. For all <i>EvtSpb</i>Xxx callback functions other than <i>EvtSpbControllerIoOther</i>, SpbCx validates the user-mode parameters before it calls the function.</p>

<p>To register an <i>EvtSpbControllerIoOther</i> callback function, call the <a href="https://msdn.microsoft.com/605E2353-8C82-4005-BB72-4CB44146A253">SpbControllerSetIoOther</a> method.</p>

<p>To define an <i>EvtSpbControllerIoOther</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSpbControllerIoOther</i> callback function that is named <code>MyEvtSpbControllerIoOther</code>, use the EVT_SPB_CONTROLLER_OTHER function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The EVT_SPB_CONTROLLER_OTHER function type is defined in the Spbcx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the EVT_SPB_CONTROLLER_OTHER function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Spbcx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Called at IRQL &lt;= DISPATCH_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/3e3c4c53-e557-4bd1-8b7d-be59dde4b9ce">EvtIoDeviceControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/D90DD169-A989-4D08-B1B8-BDE7EC9B7A82">EvtSpbTargetConnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/605E2353-8C82-4005-BB72-4CB44146A253">SpbControllerSetIoOther</a>
</dt>
<dt>
<a href="buses.spbrequest_object_handle">SPBREQUEST</a>
</dt>
<dt>
<a href="buses.spbtarget_object_handle">SPBTARGET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20EVT_SPB_CONTROLLER_OTHER callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
