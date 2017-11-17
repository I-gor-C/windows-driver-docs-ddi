---
UID: NS.hwnclx._HWN_CLIENT_REGISTRATION_PACKET
title: HWN_CLIENT_REGISTRATION_PACKET
author: windows-driver-content
description: Hardware Notification client driver registration packet that is passed to the class extension when a client driver is registered. Contains version information and client driver callback functions.
old-location: gpiobtn\_hwn_client_registration_packet.htm
ms.assetid: bf8ac72b-c3d6-4965-a1e9-2408d2fa2196
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: gpiobtn
req.header: hwnclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HWN_CLIENT_REGISTRATION_PACKET
req.alt-loc: Hwnclx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: HWN_CLIENT_REGISTRATION_PACKET, HWN_CLIENT_REGISTRATION_PACKET, *PHWN_CLIENT_REGISTRATION_PACKET
req.iface: 
---

# HWN_CLIENT_REGISTRATION_PACKET structure



## -description
<p>Hardware Notification client driver registration packet that is passed to the class
extension when a client driver is registered. Contains version information and
client driver callback functions.</p>


## -syntax

````
typedef struct _HWN_CLIENT_REGISTRATION_PACKET {
  USHORT                                Version;
  USHORT                                Size;
  ULONG                                 DeviceContextSize;
  ULONG                                 Reserved;
  PHWN_CLIENT_INITIALIZE_DEVICE         ClientInitializeDevice;
  PHWN_CLIENT_UNINITIALIZE_DEVICE       ClientUnInitializeDevice;
  PHWN_CLIENT_QUERY_DEVICE_INFORMATION  ClientQueryDeviceInformation;
  PHWN_CLIENT_START_DEVICE              ClientStartDevice;
  PHWN_CLIENT_STOP_DEVICE               ClientStopDevice;
  PHWN_CLIENT_SET_STATE                 ClientSetHwNState;
  PHWN_CLIENT_GET_STATE                 ClientGetHwNState;
} HWN_CLIENT_REGISTRATION_PACKET, HWN_CLIENT_REGISTRATION_PACKET;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Version of this structure.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Size of this structure.</p>
</dd>

### -field <b>DeviceContextSize</b>

<dd>
<p>Size of the driver-defined context structure.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reseved.</p>
</dd>

### -field <b>ClientInitializeDevice</b>

<dd>
<p>A pointer to the client driver's implementation of the <a href="https://msdn.microsoft.com/d08b2435-fb6f-49cd-8da3-c49676623357">HWN_CLIENT_INITIALIZE_DEVICE</a> callback function.</p>
</dd>

### -field <b>ClientUnInitializeDevice</b>

<dd>
<p>A pointer to the client driver's implementation of the <a href="https://msdn.microsoft.com/19ed1c21-d041-4876-8f90-4319e43a7004">HWN_CLIENT_UNINITIALIZE_DEVICE</a> callback function.</p>
</dd>

### -field <b>ClientQueryDeviceInformation</b>

<dd>
<p>A pointer to the client driver's implementation of the  <a href="https://msdn.microsoft.com/e67f0384-79a8-4040-aab4-bf5b865ad989">HWN_CLIENT_QUERY_DEVICE_INFORMATION</a> callback function.</p>
</dd>

### -field <b>ClientStartDevice</b>

<dd>
<p>A pointer to the client driver's implementation of the  <a href="https://msdn.microsoft.com/79ad880a-74a2-48e8-b16b-0d488003889f">HWN_CLIENT_START_DEVICE</a> callback function.</p>
</dd>

### -field <b>ClientStopDevice</b>

<dd>
<p>A pointer to the client driver's implementation of the  <a href="https://msdn.microsoft.com/e481afe8-659a-406d-9574-ffa048ea3c45">HWN_CLIENT_STOP_DEVICE</a> callback function.</p>
</dd>

### -field <b>ClientSetHwNState</b>

<dd>
<p>A pointer to the client driver's implementation of the  <a href="https://msdn.microsoft.com/5d2ccc29-4022-467c-9f37-d49badcceba4">HWN_CLIENT_SET_STATE</a> callback function.</p>
</dd>

### -field <b>ClientGetHwNState</b>

<dd>
<p>A pointer to the client driver's implementation of the  <a href="https://msdn.microsoft.com/c472b4bf-4c7f-4c30-ad03-2017d26d52b4">HWN_CLIENT_GET_STATE</a> callback function.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
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
<dt>Hwnclx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn789335">Hardware notifications support</a></dt>
<dt>
<a href="https://msdn.microsoft.com/405ff6db-9bc0-42f3-a740-49dd3967a8b3">Hardware notifications reference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [gpiobtn\gpiobtn]:%20HWN_CLIENT_REGISTRATION_PACKET structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
