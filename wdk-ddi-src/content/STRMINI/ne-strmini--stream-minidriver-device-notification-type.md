---
UID: NE.strmini._STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE
title: STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE
author: windows-driver-content
description: TBD.
old-location: stream\stream_minidriver_device_notification_type.htm
ms.assetid: 34DAA236-ACD0-4C25-BB45-00A81D2F131D
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
req.header: strmini.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE
req.alt-loc: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
req.iface: 
req.product: Windows 10 or later.
---

# STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE enumeration



## -description
<p>TBD</p>


## -syntax

````
typedef enum _STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE { 
  ReadyForNextDeviceRequest,
  DeviceRequestComplete,
  SignalMultipleDeviceEvents,
  SignalDeviceEvent,
  DeleteDeviceEvent,
#if (NTDDI_VERSION >= NTDDI_WINXP)
  SignalMultipleDeviceInstanceEvents,
#endif 
  DeviceNotificationMaximum
} STREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE, *PSTREAM_MINIDRIVER_DEVICE_NOTIFICATION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="ReadyForNextDeviceRequest"></a><a id="readyfornextdevicerequest"></a><a id="READYFORNEXTDEVICEREQUEST"></a><b>ReadyForNextDeviceRequest</b>

<dd>
<p>Indicates that the minidriver is ready for the next device request.</p>
</dd>

### -field <a id="DeviceRequestComplete"></a><a id="devicerequestcomplete"></a><a id="DEVICEREQUESTCOMPLETE"></a><b>DeviceRequestComplete</b>

<dd>
<p>Indicates that the specified device SRB has completed.</p>
</dd>

### -field <a id="SignalMultipleDeviceEvents"></a><a id="signalmultipledeviceevents"></a><a id="SIGNALMULTIPLEDEVICEEVENTS"></a><b>SignalMultipleDeviceEvents</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="SignalDeviceEvent"></a><a id="signaldeviceevent"></a><a id="SIGNALDEVICEEVENT"></a><b>SignalDeviceEvent</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="DeleteDeviceEvent"></a><a id="deletedeviceevent"></a><a id="DELETEDEVICEEVENT"></a><b>DeleteDeviceEvent</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="SignalMultipleDeviceInstanceEvents"></a><a id="signalmultipledeviceinstanceevents"></a><a id="SIGNALMULTIPLEDEVICEINSTANCEEVENTS"></a><b>SignalMultipleDeviceInstanceEvents</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="DeviceNotificationMaximum"></a><a id="devicenotificationmaximum"></a><a id="DEVICENOTIFICATIONMAXIMUM"></a><b>DeviceNotificationMaximum</b>

<dd>
<p>TBD</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h</dt>
</dl>
</td>
</tr>
</table>