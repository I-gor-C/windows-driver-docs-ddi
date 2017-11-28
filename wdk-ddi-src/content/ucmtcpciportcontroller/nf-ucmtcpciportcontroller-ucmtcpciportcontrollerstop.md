---
UID: NF.ucmtcpciportcontroller.UcmTcpciPortControllerStop
title: UcmTcpciPortControllerStop
author: windows-driver-content
description: Indicates to the UcmTcpciCx class extension to stop sending hardware requests to the port controller object.
old-location: buses\ucmtcpciportcontrollerstop.htm
old-project: usbref
ms.assetid: 5d1dd418-5a2f-448f-ae65-695c4f97ff29
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UcmTcpciPortControllerStop
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucmtcpciportcontroller.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UcmTcpciPortControllerStop
req.alt-loc: ucmtcpcicxstub.lib,ucmtcpcicxstub.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ucmtcpcicxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UcmTcpciPortControllerStop function



## -description
<p>Indicates to the UcmTcpciCx class extension to stop sending hardware requests to the port controller object. </p>


## -syntax

````
VOID UcmTcpciPortControllerStop(
   UCMTCPCIPORTCONTROLLER PortControllerObject
);
````


## -parameters
<dl>

### -param <i>PortControllerObject</i> 

<dd>
<p>Handle to the port controller object that the client driver received in the previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt805844">UcmTcpciPortControllerCreate</a>.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>After calling <b>UcmTcpciPortControllerStop</b>, the client driver stops processing all requests on the port controller object. This call is synchronous, so it is guaranteed that the class extension will not invoke callback functions or send requests after it returns. The driver must not call this method within a port controller callback, or while any non-cancelable hardware requests are pending.</p>

<p>A client driver calls this method from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540890">EVT_WDF_DEVICE_RELEASE_HARDWARE</a> callback implementation. After doing so, it should also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a>, in case <i>EVT_WDF_DEVICE_RELEASE_HARDWARE</i> is invoked to resource rebalancing. Failure to do so causes the driver to leak objects associated with the port controller object when a resource rebalance occurs. Parenting the UCMPORTCONTROLLER handle to the WDFDEVICE handle is not sufficient, because a WDFDEVICE is not deleted across a resource rebalance.</p>

<p>If the driver is transitioning to a Dx state due to S0-Idle, the driver must not call this method from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540855">EVT_WDF_DEVICE_D0_EXIT</a> callback function.  Synchronization with the driver's power state can be achieved by using a power-managed queue to receive hardware requests.</p>

<p>It is safe to call <b>UcmTcpciPortControllerStop</b> on a port controller that has already been stopped. After this method returns, no other method except for <a href="https://msdn.microsoft.com/library/windows/hardware/mt805846">UcmTcpciPortControllerStart</a> can be called on the port controller.</p>

<p>The client driver must call this method if it needs to stop all actions on the port controller so that it can perform error recovery if it detected any issues during its operation. After the recovery process has been completed, the driver must restart the port controller.
</p>

<p>Stopping the controller ends any active PD contract and the Type-C connection. </p>

<p>After calling <b>UcmTcpciPortControllerStop</b>, the client driver stops processing all requests on the port controller object. This call is synchronous, so it is guaranteed that the class extension will not invoke callback functions or send requests after it returns. The driver must not call this method within a port controller callback, or while any non-cancelable hardware requests are pending.</p>

<p>A client driver calls this method from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540890">EVT_WDF_DEVICE_RELEASE_HARDWARE</a> callback implementation. After doing so, it should also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a>, in case <i>EVT_WDF_DEVICE_RELEASE_HARDWARE</i> is invoked to resource rebalancing. Failure to do so causes the driver to leak objects associated with the port controller object when a resource rebalance occurs. Parenting the UCMPORTCONTROLLER handle to the WDFDEVICE handle is not sufficient, because a WDFDEVICE is not deleted across a resource rebalance.</p>

<p>If the driver is transitioning to a Dx state due to S0-Idle, the driver must not call this method from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff540855">EVT_WDF_DEVICE_D0_EXIT</a> callback function.  Synchronization with the driver's power state can be achieved by using a power-managed queue to receive hardware requests.</p>

<p>It is safe to call <b>UcmTcpciPortControllerStop</b> on a port controller that has already been stopped. After this method returns, no other method except for <a href="https://msdn.microsoft.com/library/windows/hardware/mt805846">UcmTcpciPortControllerStart</a> can be called on the port controller.</p>

<p>The client driver must call this method if it needs to stop all actions on the port controller so that it can perform error recovery if it detected any issues during its operation. After the recovery process has been completed, the driver must restart the port controller.
</p>

<p>Stopping the controller ends any active PD contract and the Type-C connection. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucmtcpciportcontroller.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ucmtcpcicxstub.lib</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt805846">UcmTcpciPortControllerStart</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UcmTcpciPortControllerStop method%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
