---
UID: NF.ucmtcpciportcontroller.UcmTcpciPortControllerStart
title: UcmTcpciPortControllerStart
author: windows-driver-content
description: Indicates to the UcmTcpciCx class extension that the client driver is now ready to service hardware requests for the port controller.
old-location: buses\ucmtcpciportcontrollerstart.htm
ms.assetid: 94e7c36a-e45c-4d98-aeb7-f23769347ca5
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: usbref
req.header: ucmtcpciportcontroller.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UcmTcpciPortControllerStart
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
ms.keywords: UcmTcpciPortControllerStart
req.iface: 
req.product: Windows 10 or later.
---

# UcmTcpciPortControllerStart function



## -description
<p>Indicates to the UcmTcpciCx class extension that the client driver  is now ready to service hardware requests for the port controller.</p>


## -syntax

````
NTSTATUS UcmTcpciPortControllerStart(
   UCMTCPCIPORTCONTROLLER PortControllerObject
);
````


## -parameters
<dl>

### -param <i>PortControllerObject</i> 

<dd>
<p>Handle to the port controller  object that the client driver received in the previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/mt805844">UcmTcpciPortControllerCreate</a>.</p>
</dd>
</dl>

## -returns
<p>
(NTSTATUS) The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.
                    </p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The port controller is already in Start state.</p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>Hardware request queue has not been set by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt805845">UcmTcpciPortControllerSetHardwareRequestQueue</a>.</p>

<p> </p>

## -remarks
<p>After the client driver has received the UCMPORTCONTROLLER handle for the port controller object, the driver calls this method to notify the class extension that the driver can start receiving hardware requests. This method call allows the client driver to perform initialization of its framework context space on the port controller object, before the class extension can invoke the driver's callback functions or requests for the port controller object. The driver cannot call <a href="https://msdn.microsoft.com/library/windows/hardware/mt805843">UcmTcpciPortControllerAlert</a> or  <a href="https://msdn.microsoft.com/library/windows/hardware/mt805847">UcmTcpciPortControllerStop</a> until the port controller has been started.</p>

<p>The client driver calls this method right after calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt805844">UcmTcpciPortControllerCreate</a> and initializing its context structure, if it was specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure as the <i>Attributes</i> parameter value.
The driver must assume that the class extension may submit requests even before <b>UcmTcpciPortControllerStart</b> returns, i.e., from within this DDI call. If the driver is holding a lock while calling <b>UcmTcpciPortControllerStart</b> and also attempts to acquire a lock while handling a hardware request (in its hardware request queue callback), it might result in a deadlock.
</p>

<p>A call to <b>UcmTcpciPortControllerStart</b> to start a port controller object already in Start state, results in an error. 
</p>

<p>On boot, if the BIOS had already negotiated a PD contract, UcmTcpciCx starts from an unattached state.</p>

<p>After the client driver has received the UCMPORTCONTROLLER handle for the port controller object, the driver calls this method to notify the class extension that the driver can start receiving hardware requests. This method call allows the client driver to perform initialization of its framework context space on the port controller object, before the class extension can invoke the driver's callback functions or requests for the port controller object. The driver cannot call <a href="https://msdn.microsoft.com/library/windows/hardware/mt805843">UcmTcpciPortControllerAlert</a> or  <a href="https://msdn.microsoft.com/library/windows/hardware/mt805847">UcmTcpciPortControllerStop</a> until the port controller has been started.</p>

<p>The client driver calls this method right after calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt805844">UcmTcpciPortControllerCreate</a> and initializing its context structure, if it was specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure as the <i>Attributes</i> parameter value.
The driver must assume that the class extension may submit requests even before <b>UcmTcpciPortControllerStart</b> returns, i.e., from within this DDI call. If the driver is holding a lock while calling <b>UcmTcpciPortControllerStart</b> and also attempts to acquire a lock while handling a hardware request (in its hardware request queue callback), it might result in a deadlock.
</p>

<p>A call to <b>UcmTcpciPortControllerStart</b> to start a port controller object already in Start state, results in an error. 
</p>

<p>On boot, if the BIOS had already negotiated a PD contract, UcmTcpciCx starts from an unattached state.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt805847">UcmTcpciPortControllerStop</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UcmTcpciPortControllerStart method%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
