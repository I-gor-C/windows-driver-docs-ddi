---
UID: NC.sercx.EVT_SERCX2_SET_WAIT_MASK
title: EVT_SERCX2_SET_WAIT_MASK
author: windows-driver-content
description: The EvtSerCx2SetWaitMask event callback function is called by version 2 of the serial framework extension (SerCx2) to configure the serial controller to monitor a set of hardware events that are specified by a wait mask.
old-location: serports\evtsercx2setwaitmask.htm
old-project: serports
ms.assetid: C248FEF0-8E0B-4296-940E-763165F80617
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SENSOR_VALUE_PAIR, SENSOR_VALUE_PAIR, *PSENSOR_VALUE_PAIR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: sercx.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EvtSerCx2SetWaitMask
req.alt-loc: 2.0\Sercx.h
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
req.iface: 
req.product: Windows 10 or later.
---

# EVT_SERCX2_SET_WAIT_MASK callback



## -description
<p>The <i>EvtSerCx2SetWaitMask</i> event callback function is called by version 2 of the serial framework extension (SerCx2) to configure the serial controller to monitor a set of hardware events that are specified by a wait mask.</p>


## -prototype

````
EVT_SERCX2_SET_WAIT_MASK EvtSerCx2SetWaitMask;

VOID EvtSerCx2SetWaitMask(
  _In_ WDFDEVICE  Device,
  _In_ WDFREQUEST Request,
  _In_ ULONG      WaitMask
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A WDFDEVICE handle to the framework device object that represents the serial controller. The serial controller driver created this object in its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function. For more information, see <a href="..\sercx\nf-sercx-sercx2initializedevice.md">SerCx2InitializeDevice</a>.</p>
</dd>

### -param <i>Request</i> [in]

<dd>
<p>A WDFREQUEST handle to the framework request object that represents the <a href="..\ntddser\ni-ntddser-ioctl-serial-set-wait-mask.md">IOCTL_SERIAL_SET_WAIT_MASK</a> request.</p>
</dd>

### -param <i>WaitMask</i> [in]

<dd>
<p>The new wait mask. For more information, see Remarks.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>Your serial controller driver can, as an option, implement this function. If implemented, the driver registers the function in the call to the <a href="..\sercx\nf-sercx-sercx2initializedevice.md">SerCx2InitializeDevice</a> method that finishes the initialization of the framework device object for the serial controller.</p>

<p>When SerCx receives an <a href="..\ntddser\ni-ntddser-ioctl-serial-set-wait-mask.md">IOCTL_SERIAL_SET_WAIT_MASK</a> request from a client, the request handler in SerCx2 calls the <i>EvtSerCx2SetWaitMask</i> function, if it is implemented, to notify the driver that the wait mask has changed. If the wait mask is nonzero, the driver immediately starts to monitor the events in the new wait mask, and discards any old wait mask that might have been supplied in a previous <i>EvtSerCx2SetWaitMask</i> call. If the new wait mask is zero, the driver simply discards the old wait mask and ceases to monitor any wait mask events. For more information about the types of events that can be specified by a wait mask, see <a href="serports.serial_ev_xxx">SERIAL_EV_XXX</a>.</p>

<p>If the driver does not implement this function, SerCx2 fails all <a href="..\ntddser\ni-ntddser-ioctl-serial-set-wait-mask.md">IOCTL_SERIAL_SET_WAIT_MASK</a> requests with error status code STATUS_NOT_SUPPORTED.</p>

<p>To monitor the events in the wait mask, the <i>EvtSerCx2SetWaitMask</i> function typically enables interrupts for these events. Later, when an event in the wait mask is detected, the serial controller driver calls the <a href="..\sercx\nf-sercx-sercx2completewait.md">SerCx2CompleteWait</a> method to notify SerCx2 of the event.</p>

<p>The <i>EvtSerCx2SetWaitMask</i> function is responsible for completing the <b>IOCTL_SERIAL_SET_WAIT_MASK</b> request pointed to by the <i>Request</i> parameter.  After the serial controller driver enables the necessary interrupts, it calls the <a href="..\wdfrequest\nf-wdfrequest-wdfrequestcomplete.md">WdfRequestComplete</a> method and supplies, as input parameters, the <i>Request</i> parameter value and a status value to indicate whether the request was successful.</p>

<p>Before the serial controller driver calls <b>WdfRequestComplete</b> to complete the request, the driver must finish any calls to <b>SerCx2CompleteWait</b> that might be still be pending due to events in the old wait mask.</p>

<p>Initially, after a client opens a logical connection to the serial port and before the first <i>EvtSerCx2SetWaitMask</i> call, the wait mask is effectively zero, and the serial controller driver is not monitoring any <a href="serports.serial_ev_xxx">SERIAL_EV_XXX</a> events.</p>

<p>SerCx2 fails an <b>IOCTL_SERIAL_SET_WAIT_MASK</b> request that has a wait mask that includes any of the following <a href="serports.serial_ev_xxx">SERIAL_EV_XXX</a> event flags:</p>

<p>Thus, the wait mask supplied to your <i>EvtSerCx2SetWaitMask</i> function never contains any of the event flags in the preceding list.</p>

<p>If implemented, your <i>EvtSerCx2SetWaitMask</i> function should support the following event flags:</p>

<p>Also, if the serial controller has a <i>data set ready</i> (DSR) signal line, the <i>EvtSerCx2SetWaitMask</i> function should support SERIAL_EV_DSR. As an option, a driver can support any of the other event flags described in <a href="serports.serial_ev_xxx">SERIAL_EV_XXX</a>. If the wait mask specifies an event that the driver does not support, the <i>EvtSerCx2SetWaitMask</i> function should fail the request and set the status value in the request to STATUS_INVALID_PARAMETER.</p>

<p>To define an <i>EvtSerCx2SetWaitMask</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2SetWaitMask</i> callback function that is named <code>MySetWaitmask</code>, use the <b>EVT_SERCX2_SET_WAIT_MASK</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_SET_WAIT_MASK</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_SET_WAIT_MASK</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

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
<p>Available starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>2.0\Sercx.h</dt>
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
<a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="..\ntddser\ni-ntddser-ioctl-serial-set-wait-mask.md">IOCTL_SERIAL_SET_WAIT_MASK</a>
</dt>
<dt>
<a href="..\sercx\nf-sercx-sercx2completewait.md">SerCx2CompleteWait</a>
</dt>
<dt>
<a href="..\sercx\nf-sercx-sercx2initializedevice.md">SerCx2InitializeDevice</a>
</dt>
<dt>
<a href="serports.serial_ev_xxx">SERIAL_EV_XXX</a>
</dt>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdfrequestcomplete.md">WdfRequestComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20EVT_SERCX2_SET_WAIT_MASK callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
