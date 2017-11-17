---
UID: NC.spbcx.EVT_SPB_CONTROLLER_READ
title: EVT_SPB_CONTROLLER_READ
author: windows-driver-content
description: An SPB controller driver's EvtSpbControllerIoRead event callback function reads data from the specified target device into the buffers that are supplied with the read request.
old-location: spb\evtspbcontrollerioread.htm
ms.assetid: 2BC0E6E7-7EE1-487A-9276-AE8EBB3FFD43
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
req.alt-api: EvtSpbControllerIoRead
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

# EVT_SPB_CONTROLLER_READ callback



## -description
<p>An SPB controller driver's <i>EvtSpbControllerIoRead</i> event callback function reads data from the specified target device into the buffers that are supplied with the read request.</p>


## -prototype

````
EVT_SPB_CONTROLLER_READ EvtSpbControllerIoRead;

VOID EvtSpbControllerIoRead(
  _In_ WDFDEVICE  Controller,
  _In_ SPBTARGET  Target,
  _In_ SPBREQUEST Request,
  _In_ size_t     Length
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
<p>An <a href="buses.spbrequest_object_handle">SPBREQUEST</a> handle to the I/O request. Your SPB controller driver must complete this request either by performing the requested operation or by returning an error status. For more information, see Remarks.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes to read from the target device.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>SpbCx manages the I/O queue for the SPB controller. SpbCx calls the SPB controller driver's <i>EvtSpbControllerIoRead</i> callback function when a client (peripheral driver) of the SPB controller sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> request to a target device that is attached to the bus. The <i>Request</i> parameter value is a handle that encapsulates this request.</p>

<p>An <i>EvtSpbControllerIoRead</i> callback does not return a status value. Instead, the SPB controller driver indicates the status of the read operation in the completion status for the I/O request.</p>

<p>An <i>EvtSpbControllerIoRead</i> callback is asynchronous.  That is, the callback function should initiate the requested read operation and then return without waiting for the operation to complete. Later, the SPB controller driver completes the read request during an interrupt DPC or a timer DPC.</p>

<p>If the read operation completes in full, the SPB controller driver should set the completion status to  STATUS_SUCCESS. If the target device indicates that it can supply some but not all  of the data requested, the SPB controller driver should retrieve as much data as is available, specify the number of data bytes retrieved, and set the completion status in the I/O request to  STATUS_SUCCESS. Such a partially completed read operation cannot occur on an SPI or I²C bus, but might occur on another type of bus.</p>

<p>If the read operation fails due to line noise, a controller hardware error, or a driver error, then the SPB controller driver should set the completion status in the I/O request to an appropriate error code. Not all buses provide a mechanism for a target device to report a transport error or a partially completed transfer, and not all controllers can detect these conditions.</p>

<p>To register an <i>EvtSpbControllerIoRead</i> callback function, call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450919">SpbDeviceInitialize</a> method.</p>

<p>To define an <i>EvtSpbControllerIoRead</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSpbControllerIoRead</i> callback function that is named <code>MyEvtSpbControllerIoRead</code>, use the EVT_SPB_CONTROLLER_READ function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The EVT_SPB_CONTROLLER_READ function type is defined in the Spbcx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the EVT_SPB_CONTROLLER_READ function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

<p>SpbCx manages the I/O queue for the SPB controller. SpbCx calls the SPB controller driver's <i>EvtSpbControllerIoRead</i> callback function when a client (peripheral driver) of the SPB controller sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> request to a target device that is attached to the bus. The <i>Request</i> parameter value is a handle that encapsulates this request.</p>

<p>An <i>EvtSpbControllerIoRead</i> callback does not return a status value. Instead, the SPB controller driver indicates the status of the read operation in the completion status for the I/O request.</p>

<p>An <i>EvtSpbControllerIoRead</i> callback is asynchronous.  That is, the callback function should initiate the requested read operation and then return without waiting for the operation to complete. Later, the SPB controller driver completes the read request during an interrupt DPC or a timer DPC.</p>

<p>If the read operation completes in full, the SPB controller driver should set the completion status to  STATUS_SUCCESS. If the target device indicates that it can supply some but not all  of the data requested, the SPB controller driver should retrieve as much data as is available, specify the number of data bytes retrieved, and set the completion status in the I/O request to  STATUS_SUCCESS. Such a partially completed read operation cannot occur on an SPI or I²C bus, but might occur on another type of bus.</p>

<p>If the read operation fails due to line noise, a controller hardware error, or a driver error, then the SPB controller driver should set the completion status in the I/O request to an appropriate error code. Not all buses provide a mechanism for a target device to report a transport error or a partially completed transfer, and not all controllers can detect these conditions.</p>

<p>To register an <i>EvtSpbControllerIoRead</i> callback function, call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450919">SpbDeviceInitialize</a> method.</p>

<p>To define an <i>EvtSpbControllerIoRead</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSpbControllerIoRead</i> callback function that is named <code>MyEvtSpbControllerIoRead</code>, use the EVT_SPB_CONTROLLER_READ function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The EVT_SPB_CONTROLLER_READ function type is defined in the Spbcx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the EVT_SPB_CONTROLLER_READ function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<a href="https://msdn.microsoft.com/C56F1528-5FDA-4BC9-AB32-7882FB0F7713">EvtSpbControllerIoSequence</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/D90DD169-A989-4D08-B1B8-BDE7EC9B7A82">EvtSpbTargetConnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450857">IOCTL_SPB_EXECUTE_SEQUENCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450919">SpbDeviceInitialize</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20EVT_SPB_CONTROLLER_READ callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
