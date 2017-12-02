---
UID: NS.ucxusbdevice._UCX_USBDEVICE_EVENT_CALLBACKS
title: UCX_USBDEVICE_EVENT_CALLBACKS
author: windows-driver-content
description: This structure provides a list of UCX USB device event callback functions.
old-location: buses\_ucx_usbdevice_event_callbacks.htm
old-project: usbref
ms.assetid: 7A320D48-E71C-40FE-A2EF-201CFCE55145
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_USBDEVICE_EVENT_CALLBACKS, UCX_USBDEVICE_EVENT_CALLBACKS, *PUCX_USBDEVICE_EVENT_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_USBDEVICE_EVENT_CALLBACKS
req.alt-loc: ucxusbdevice.h
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
req.product: Windows 10 or later.
---

# UCX_USBDEVICE_EVENT_CALLBACKS structure



## -description
<p>This structure provides a list of UCX USB device event callback functions.</p>


## -syntax

````
typedef struct _UCX_USBDEVICE_EVENT_CALLBACKS {
  ULONG                                  Size;
  PFN_UCX_USBDEVICE_ENDPOINTS_CONFIGURE  EvtUsbDeviceEndpointsConfigure;
  PFN_UCX_USBDEVICE_ENABLE               EvtUsbDeviceEnable;
  PFN_UCX_USBDEVICE_DISABLE              EvtUsbDeviceDisable;
  PFN_UCX_USBDEVICE_RESET                EvtUsbDeviceReset;
  PFN_UCX_USBDEVICE_ADDRESS              EvtUsbDeviceAddress;
  PFN_UCX_USBDEVICE_UPDATE               EvtUsbDeviceUpdate;
  PFN_UCX_USBDEVICE_HUB_INFO             EvtUsbDeviceHubInfo;
  PFN_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD EvtUsbDeviceDefaultEndpointAdd;
  PFN_UCX_USBDEVICE_ENDPOINT_ADD         EvtUsbDeviceEndpointAdd;
  PFN_UCX_USBDEVICE_SUSPEND              EvtUsbDeviceSuspend;
  PFN_UCX_USBDEVICE_RESUME               EvtUsbDeviceResume;
  PFN_UCX_USBDEVICE_GET_CHARACTERISTIC   EvtUsbDeviceGetCharacteristic;
} UCX_USBDEVICE_EVENT_CALLBACKS, *P_UCX_USBDEVICE_EVENT_CALLBACKS;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field EvtUsbDeviceEndpointsConfigure

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-endpoints-configure.md">EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE</a> callback function.</p>
</dd>

### -field EvtUsbDeviceEnable

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-enable.md">EVT_UCX_USBDEVICE_ENABLE</a> callback function.</p>
</dd>

### -field EvtUsbDeviceDisable

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-disable.md">EVT_UCX_USBDEVICE_DISABLE</a> callback function.</p>
</dd>

### -field EvtUsbDeviceReset

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-reset.md">EVT_UCX_USBDEVICE_RESET</a> callback function.</p>
</dd>

### -field EvtUsbDeviceAddress

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-address.md">EVT_UCX_USBDEVICE_ADDRESS</a> callback function.</p>
</dd>

### -field EvtUsbDeviceUpdate

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-update.md">EVT_UCX_USBDEVICE_UPDATE</a> callback function.</p>
</dd>

### -field EvtUsbDeviceHubInfo

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-hub-info.md">EVT_UCX_USBDEVICE_HUB_INFO</a> callback function.</p>
</dd>

### -field EvtUsbDeviceDefaultEndpointAdd

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-default-endpoint-add.md">EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD</a> callback function.</p>
</dd>

### -field EvtUsbDeviceEndpointAdd

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-endpoint-add.md">EVT_UCX_USBDEVICE_ENDPOINT_ADD</a> callback function.</p>
</dd>

### -field EvtUsbDeviceSuspend

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-suspend.md">EVT_UCX_USBDEVICE_SUSPEND</a> callback function.</p>
</dd>

### -field EvtUsbDeviceResume

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-resume.md">EVT_UCX_USBDEVICE_RESUME</a> callback function.</p>
</dd>

### -field EvtUsbDeviceGetCharacteristic

<dd>
<p>A pointer to an <a href="..\ucxusbdevice\nc-ucxusbdevice-evt-ucx-usbdevice-get-characteristic.md">EVT_UCX_USBDEVICE_GET_CHARACTERISTIC</a> callback function.</p>
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
<dt>Ucxusbdevice.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ucxusbdevice\nf-ucxusbdevice-ucx-usbdevice-event-callbacks-init.md">UCX_USBDEVICE_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="..\ucxusbdevice\nf-ucxusbdevice-ucxusbdeviceinitseteventcallbacks.md">UcxUsbDeviceInitSetEventCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_USBDEVICE_EVENT_CALLBACKS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
