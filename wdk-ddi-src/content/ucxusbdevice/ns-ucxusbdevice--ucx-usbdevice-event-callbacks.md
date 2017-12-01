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

### -field <b>Size</b>

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field <b>EvtUsbDeviceEndpointsConfigure</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_endpoints_configure">EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceEnable</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_enable">EVT_UCX_USBDEVICE_ENABLE</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceDisable</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_disable">EVT_UCX_USBDEVICE_DISABLE</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceReset</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_reset">EVT_UCX_USBDEVICE_RESET</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceAddress</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_address">EVT_UCX_USBDEVICE_ADDRESS</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceUpdate</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_update">EVT_UCX_USBDEVICE_UPDATE</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceHubInfo</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_hub_info">EVT_UCX_USBDEVICE_HUB_INFO</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceDefaultEndpointAdd</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_default_endpoint_add">EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceEndpointAdd</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_endpoint_add">EVT_UCX_USBDEVICE_ENDPOINT_ADD</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceSuspend</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_suspend">EVT_UCX_USBDEVICE_SUSPEND</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceResume</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_resume">EVT_UCX_USBDEVICE_RESUME</a> callback function.</p>
</dd>

### -field <b>EvtUsbDeviceGetCharacteristic</b>

<dd>
<p>A pointer to an <a href="buses.evt_ucx_usbdevice_get_characteristic">EVT_UCX_USBDEVICE_GET_CHARACTERISTIC</a> callback function.</p>
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
<a href="buses._ucx_usbdevice_event_callbacks_init">UCX_USBDEVICE_EVENT_CALLBACKS_INIT</a>
</dt>
<dt>
<a href="buses._ucxusbdeviceinitseteventcallbacks">UcxUsbDeviceInitSetEventCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_USBDEVICE_EVENT_CALLBACKS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
