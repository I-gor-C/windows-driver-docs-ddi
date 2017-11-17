---
UID: NS.ksmedia._KSAUDIOMODULE_NOTIFICATION
title: KSAUDIOMODULE_NOTIFICATION
author: windows-driver-content
description: The KSAUDIOMODULE_NOTIFICATION structure describes the properties associated with audio modules change notification.
old-location: audio\ksaudiomodule_notification.htm
ms.assetid: 92A9462C-0E8C-4012-9374-3437BB220502
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSAUDIOMODULE_NOTIFICATION
req.alt-loc: Ksmedia.h
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
ms.keywords: KSAUDIOMODULE_NOTIFICATION, KSAUDIOMODULE_NOTIFICATION, *PKSAUDIOMODULE_NOTIFICATION
req.iface: 
---

# KSAUDIOMODULE_NOTIFICATION structure



## -description
<p>The <b>KSAUDIOMODULE_NOTIFICATION</b> structure describes the  properties associated with audio  modules change notification.</p>


## -syntax

````
typedef struct _KSAUDIOMODULE_NOTIFICATION {
  union {
    struct {
      GUID  DeviceId;
      GUID  ClassId;
      ULONG InstanceId;
      ULONG Reserved;
    } ProviderId;
    LONGLONG  Alignment;
  };
} KSAUDIOMODULE_NOTIFICATION, *PKSAUDIOMODULE_NOTIFICATION;
````


## -struct-fields
<dl>

### -field <b>ProviderId</b>

<dd>
<p>A structure that specifies the ProviderId of the audio module notification.</p>
<dl>

### -field <b>DeviceId</b>

<dd>
<p>Specifies the DeviceId of the audio module notification. The DeviceId matches the value returned in <a href="https://msdn.microsoft.com/CD9C5FCD-FB2A-4B21-A15E-BA520C3311A7">KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID</a>.</p>
</dd>

### -field <b>ClassId</b>

<dd>
<p>The ClassId of the audio module. The ClassId is an identifier that establishes what type of module this is. The value and mapping is established by the ISV and IHV. </p>
</dd>

### -field <b>InstanceId</b>

<dd>
<p>The InstanceId of the audio module.  The InstanceId is a unique identifier that distinguishes this instance of a module from another instance of an module. </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved.</p>
</dd>
</dl>
</dd>

### -field <b>Alignment</b>

<dd>
<p>Specifies the value that is used for alignment. </p>
</dd>
</dl>

## -remarks
<p>The Audio module notification KSNOTIFICATIONID_AudioModule is defined in Ksmedia.h as shown here. </p>

<p></p>

<p>For more information about audio modules, see  <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/audio/implementing-audio-module-communication">Implementing Audio Module Discovery</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>