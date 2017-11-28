---
UID: NC.spbcx.EVT_SPB_TARGET_CONNECT
title: EVT_SPB_TARGET_CONNECT
author: windows-driver-content
description: An SPB controller driver's EvtSpbTargetConnect event callback function opens a connection to a target device on the bus.
old-location: spb\evtspbtargetconnect.htm
old-project: SPB
ms.assetid: D90DD169-A989-4D08-B1B8-BDE7EC9B7A82
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SPB_TRANSFER_LIST,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: spbcx.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EvtSpbTargetConnect
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
req.irql: Called at PASSIVE_LEVEL.
req.iface: 
req.product: Windows 10 or later.
---

# EVT_SPB_TARGET_CONNECT callback



## -description
<p>An SPB controller driver's <i>EvtSpbTargetConnect</i> event callback function opens a connection to a target device on the bus.</p>


## -prototype

````
EVT_SPB_TARGET_CONNECT EvtSpbTargetConnect;

NTSTATUS EvtSpbTargetConnect(
  _In_ WDFDEVICE Controller,
  _In_ SPBTARGET Target
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
<p>An <a href="buses.spbtarget_object_handle">SPBTARGET</a> handle to the target to open.  The target is a peripheral device or port that is attached to the bus.</p>
</dd>
</dl>

## -returns
<p><i>EvtSpbTargetConnect</i> returns STATUS_SUCCESS if the driver successfully opens the connection to the target.  Otherwise, the function returns an appropriate NTSTATUS error code.</p>

## -remarks
<p>Implementation of this function by the SPB controller driver is optional.</p>

<p>The SPB framework extension (SpbCx) manages the I/O queue for the SPB controller. If the SPB controller driver registers an <i>EvtSpbTargetConnect</i> callback function, SpbCx calls this function when a client (peripheral driver) of the controller sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> request to open a connection to a target device on the bus. If the <i>EvtSpbTargetConnect</i> function returns an error code, SpbCx fails the <b>IRP_MJ_CREATE</b> request. A client that successfully opens a connection to a target has exclusive access to the target until the connection is closed.</p>

<p>Call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450926">SpbTargetGetConnectionParameters</a> method to get the connection parameters for the target device. An SPB controller driver typically calls this method from the driver's <i>EvtSpbTargetConnect</i> function. <b>SpbTargetGetConnectionParameters</b> writes the connection parameters to a caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/hh406204">SPB_CONNECTION_PARAMETERS</a> structure. The <b>ConnectionParameters</b> member of this structure is a pointer to a buffer that contains the connection settings for the target device. The driver uses these settings to configure the SPB controller to communicate with the device. For more information, see <a href="NULL">How to Get the Connection Settings for a Device</a>.</p>

<p>The <i>EvtSpbTargetConnect</i> callback function is called synchronously from the context of the client thread that requests the connection to the target.</p>

<p>SpbCx calls the <a href="https://msdn.microsoft.com/02756C35-E76C-42C0-80FA-359CADE224A1">EvtSpbTargetDisconnect</a> callback function to close a target connection that was previously opened by an <i>EvtSpbTargetConnect</i> callback.</p>

<p>To register an <i>EvtSpbTargetConnect</i> callback function, call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450919">SpbDeviceInitialize</a> method.</p>

<p>To define an <i>EvtSpbTargetConnect</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSpbTargetConnect</i> callback function that is named <code>MyEvtSpbTargetConnect</code>, use the EVT_SPB_TARGET_CONNECT function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The EVT_SPB_TARGET_CONNECT function type is defined in the Spbcx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the EVT_SPB_TARGET_CONNECT function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

<p>Implementation of this function by the SPB controller driver is optional.</p>

<p>The SPB framework extension (SpbCx) manages the I/O queue for the SPB controller. If the SPB controller driver registers an <i>EvtSpbTargetConnect</i> callback function, SpbCx calls this function when a client (peripheral driver) of the controller sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> request to open a connection to a target device on the bus. If the <i>EvtSpbTargetConnect</i> function returns an error code, SpbCx fails the <b>IRP_MJ_CREATE</b> request. A client that successfully opens a connection to a target has exclusive access to the target until the connection is closed.</p>

<p>Call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450926">SpbTargetGetConnectionParameters</a> method to get the connection parameters for the target device. An SPB controller driver typically calls this method from the driver's <i>EvtSpbTargetConnect</i> function. <b>SpbTargetGetConnectionParameters</b> writes the connection parameters to a caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/hh406204">SPB_CONNECTION_PARAMETERS</a> structure. The <b>ConnectionParameters</b> member of this structure is a pointer to a buffer that contains the connection settings for the target device. The driver uses these settings to configure the SPB controller to communicate with the device. For more information, see <a href="NULL">How to Get the Connection Settings for a Device</a>.</p>

<p>The <i>EvtSpbTargetConnect</i> callback function is called synchronously from the context of the client thread that requests the connection to the target.</p>

<p>SpbCx calls the <a href="https://msdn.microsoft.com/02756C35-E76C-42C0-80FA-359CADE224A1">EvtSpbTargetDisconnect</a> callback function to close a target connection that was previously opened by an <i>EvtSpbTargetConnect</i> callback.</p>

<p>To register an <i>EvtSpbTargetConnect</i> callback function, call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450919">SpbDeviceInitialize</a> method.</p>

<p>To define an <i>EvtSpbTargetConnect</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSpbTargetConnect</i> callback function that is named <code>MyEvtSpbTargetConnect</code>, use the EVT_SPB_TARGET_CONNECT function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The EVT_SPB_TARGET_CONNECT function type is defined in the Spbcx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the EVT_SPB_TARGET_CONNECT function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<p>Called at PASSIVE_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/02756C35-E76C-42C0-80FA-359CADE224A1">EvtSpbTargetDisconnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406204">SPB_CONNECTION_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450919">SpbDeviceInitialize</a>
</dt>
<dt>
<a href="buses.spbtarget_object_handle">SPBTARGET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20EVT_SPB_TARGET_CONNECT callback function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
