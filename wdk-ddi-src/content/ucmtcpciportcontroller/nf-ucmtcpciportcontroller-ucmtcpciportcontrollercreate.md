---
UID: NF.ucmtcpciportcontroller.UcmTcpciPortControllerCreate
title: UcmTcpciPortControllerCreate
author: windows-driver-content
description: Creates a port controller object to register with UcmTcpciCx.
old-location: buses\ucmtcpciportcontrollercreate.htm
old-project: usbref
ms.assetid: 29862d9b-c004-445b-b90b-6990e5e01966
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UcmTcpciPortControllerCreate
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
req.alt-api: UcmTcpciPortControllerCreate
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

# UcmTcpciPortControllerCreate function



## -description
<p>Creates a port controller object to register with UcmTcpciCx. </p>


## -syntax

````
NTSTATUS UcmTcpciPortControllerCreate(
   WDFDEVICE                        WdfDevice,
   PUCMTCPCI_PORT_CONTROLLER_CONFIG Config,
   PWDF_OBJECT_ATTRIBUTES           Attributes,
   UCMTCPCIPORTCONTROLLER*          PortControllerObject
);
````


## -parameters
<dl>

### -param WdfDevice 

<dd>
<p>A handle to a framework device object that the client driver received in the previous call to <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>. </p>
</dd>

### -param Config 

<dd>
<p>A pointer to the <a href="..\ucmtcpciportcontroller\ns-ucmtcpciportcontroller--ucmtcpci-port-controller-config.md">UCMTCPCI_PORT_CONTROLLER_CONFIG</a> that is initialized by calling <b>UCMTCPCI_PORT_CONTROLLER_CONFIG_INIT</b>. This value cannot be NULL.</p>
</dd>

### -param Attributes 

<dd>
<p>A pointer to a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that contains driver-supplied attributes for the new object. This parameter is optional and can be <b>WDF_NO_OBJECT_ATTRIBUTES</b>.</p>
</dd>

### -param PortControllerObject 

<dd>
<p>A pointer to a location that receives a handle to the new port controller object. </p>
</dd>
</dl>

## -returns
<p>
(NTSTATUS) The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.
                    </p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The handle to a framework device object is invalid.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>Invalid size for the structure pointed to by <i>Config</i> or <i> Config-&gt;Capabilities</i>. Must be size of <a href="..\ucmtcpciportcontroller\ns-ucmtcpciportcontroller--ucmtcpci-port-controller-config.md">UCMTCPCI_PORT_CONTROLLER_CONFIG</a> or <a href="..\ucmtcpciportcontroller\ns-ucmtcpciportcontroller--ucmtcpci-port-controller-capabilities.md">UCMTCPCI_PORT_CONTROLLER_CAPABILITIES</a>, respectively. </p>

<p> </p>

## -remarks


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
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>
</dt>
<dt>
<a href="..\ucmtcpciportcontroller\ns-ucmtcpciportcontroller--ucmtcpci-port-controller-config.md">UCMTCPCI_PORT_CONTROLLER_CONFIG</a>
</dt>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EVT_WDF_DRIVER_DEVICE_ADD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UcmTcpciPortControllerCreate method%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
