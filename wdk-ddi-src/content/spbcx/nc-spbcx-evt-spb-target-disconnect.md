---
UID: NC.spbcx.EVT_SPB_TARGET_DISCONNECT
title: EVT_SPB_TARGET_DISCONNECT
author: windows-driver-content
description: An SPB controller driver's EvtSpbTargetDisconnect event callback function closes a connection to a target device that was previously opened by a call to the driver's EvtSpbTargetConnect event callback function.
old-location: spb\evtspbtargetdisconnect.htm
old-project: SPB
ms.assetid: 02756C35-E76C-42C0-80FA-359CADE224A1
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: EvtSpbTargetDisconnect
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

# EVT_SPB_TARGET_DISCONNECT callback



## -description
<p>An SPB controller driver's <i>EvtSpbTargetDisconnect</i> event callback function closes a connection to a target device that was previously opened by a call to the driver's  <a href="https://msdn.microsoft.com/D90DD169-A989-4D08-B1B8-BDE7EC9B7A82">EvtSpbTargetConnect</a> event callback function.</p>


## -prototype

````
EVT_SPB_TARGET_DISCONNECT EvtSpbTargetDisconnect;

VOID EvtSpbTargetDisconnect(
  _In_ WDFDEVICE Controller,
  _In_ SPBTARGET Target
)
{ ... }
````


## -parameters
<dl>

### -param Controller [in]

<dd>
<p>A WDFDEVICE handle to the <a href="kmdf.creating_a_framework_device_object">framework device object</a> that represents the SPB controller.</p>
</dd>

### -param Target [in]

<dd>
<p>A <a href="buses.spbtarget_object_handle">SPBTARGET</a> handle to the target to close. The target is a peripheral device or port that is attached to the bus. The SPB framework extension (SpbCx) previously assigned this handle to the target in the <a href="https://msdn.microsoft.com/D90DD169-A989-4D08-B1B8-BDE7EC9B7A82">EvtSpbTargetConnect</a> callback that opened the connection to the target.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>Implementation of this function by the SPB controller driver is optional.</p>

<p>SpbCx manages the I/O queue for the SPB controller. If the SPB controller driver registers an <i>EvtSpbTargetDisconnect</i> callback function, SpbCx calls this function when a client (peripheral driver) of the controller driver sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> request to close an SPBTARGET handle. This handle represents a connection to a target device on the bus that the client opened in a previous <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> request. If the <i>EvtSpbTargetDisconnect</i> function returns an error code, SpbCx fails the <b>IRP_MJ_CLOSE</b> request.</p>

<p>The <i>EvtSpbTargetDisconnect</i> function is called synchronously from the context of the client's closing thread after all client-initiated I/O operations have ended and after the client has unlocked the controller (if the client previously locked the controller).</p>

<p>If the SPB controller driver has allocated I/O requests and sent them to the next-lower driver in the I/O-request chain for the target device, the <i>EvtSpbTargetDisconnect</i> function should cancel these requests before it returns.</p>

<p>A client driver's <a href="kernel.dispatchcleanup">DispatchCleanup</a> and <a href="kernel.createprocessnotifyex">CreateProcessNotifyEx</a> callback routines can be called at any time after the <i>EvtSpbTargetDisconnect</i> callback returns. When the client driver's process exits, its <i>CreateProcessNotifyEx</i> routine is called just before the last thread to exit the process is destroyed.</p>

<p>To register an <i>EvtSpbTargetDisconnect</i> callback function, call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450919">SpbDeviceInitialize</a> method.</p>

<p>To define an <i>EvtSpbTargetDisconnect</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSpbTargetDisconnect</i> callback function that is named <code>MyEvtSpbTargetDisconnect</code>, use the EVT_SPB_TARGET_DISCONNECT function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The EVT_SPB_TARGET_DISCONNECT function type is defined in the Spbcx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the EVT_SPB_TARGET_DISCONNECT function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/73a408ba-0219-4fde-8dad-ca330e4e67c3">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<a href="https://msdn.microsoft.com/D90DD169-A989-4D08-B1B8-BDE7EC9B7A82">EvtSpbTargetConnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20EVT_SPB_TARGET_DISCONNECT callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
