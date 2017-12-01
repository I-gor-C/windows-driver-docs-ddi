---
UID: NS.ks._KSDEVICE_DISPATCH
title: KSDEVICE_DISPATCH
author: windows-driver-content
description: The KSDEVICE_DISPATCH structure describes the callbacks that a client can provide to receive notification of device creation and PnP events.
old-location: stream\ksdevice_dispatch.htm
old-project: stream
ms.assetid: 1ae7af1d-5e1c-4728-82c5-efc8d60b5df6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KSDEVICE_DISPATCH,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSDEVICE_DISPATCH
req.alt-loc: ks.h
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
req.iface: 
---

# KSDEVICE_DISPATCH structure



## -description
<p>The KSDEVICE_DISPATCH structure describes the callbacks that a client can provide to receive notification of device creation and PnP events.</p>


## -syntax

````
typedef struct _KSDEVICE_DISPATCH {
  PFNKSDEVICECREATE            Add;
  PFNKSDEVICEPNPSTART          Start;
  PFNKSDEVICE                  PostStart;
  PFNKSDEVICEIRP               QueryStop;
  PFNKSDEVICEIRPVOID           CancelStop;
  PFNKSDEVICEIRPVOID           Stop;
  PFNKSDEVICEIRP               QueryRemove;
  PFNKSDEVICEIRPVOID           CancelRemove;
  PFNKSDEVICEIRPVOID           Remove;
  PFNKSDEVICEQUERYCAPABILITIES QueryCapabilities;
  PFNKSDEVICEIRPVOID           SurpriseRemoval;
  PFNKSDEVICEQUERYPOWER        QueryPower;
  PFNKSDEVICESETPOWER          SetPower;
  PFNKSDEVICEIRP               QueryInterface;
} KSDEVICE_DISPATCH, *PKSDEVICE_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>Add</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminideviceadd">AVStrMiniDeviceAdd</a> callback routine.</p>
</dd>

### -field <b>Start</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicestart">AVStrMiniDeviceStart</a> callback routine.</p>
</dd>

### -field <b>PostStart</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicepoststart">AVStrMiniDevicePostStart</a> callback routine.</p>
</dd>

### -field <b>QueryStop</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicequerystop">AVStrMiniDeviceQueryStop</a> callback routine.</p>
</dd>

### -field <b>CancelStop</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicecancelstop">AVStrMiniDeviceCancelStop</a> callback routine.</p>
</dd>

### -field <b>Stop</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicestop">AVStrMiniDeviceStop</a> callback routine.</p>
</dd>

### -field <b>QueryRemove</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicequeryremove">AVStrMiniDeviceQueryRemove</a> callback routine.</p>
</dd>

### -field <b>CancelRemove</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicecancelremove">AVStrMiniDeviceCancelRemove</a> callback routine.</p>
</dd>

### -field <b>Remove</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminideviceremove">AVStrMiniDeviceRemove</a> callback routine.</p>
</dd>

### -field <b>QueryCapabilities</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicequerycapabilities">AVStrMiniDeviceQueryCapabilities</a> callback routine.</p>
</dd>

### -field <b>SurpriseRemoval</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicesurpriseremoval">AVStrMiniDeviceSurpriseRemoval</a> callback routine.</p>
</dd>

### -field <b>QueryPower</b>

<dd>
<p>Optional. can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicequerypower">AVStrMiniDeviceQueryPower</a> callback routine.</p>
</dd>

### -field <b>SetPower</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicesetpower">AVStrMiniDeviceSetPower</a> callback routine.</p>
</dd>

### -field <b>QueryInterface</b>

<dd>
<p>Optional. Can be <b>NULL</b>. A pointer to a minidriver-supplied <a href="stream.avstrminidevicequeryinterface">AVStrMiniDeviceQueryInterface</a> callback routine.</p>
</dd>
</dl>

## -remarks
<p>In describing a device with the <a href="..\ks\ns-ks--ksdevice-descriptor.md">KSDEVICE_DESCRIPTOR</a> structure, clients include a pointer to a dispatch table defined by this structure. Any member of this structure may be <b>NULL</b> indicating that the minidriver receives no notification for that particular message.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ns-ks--ksdevice-descriptor.md">KSDEVICE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSDEVICE_DISPATCH structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
