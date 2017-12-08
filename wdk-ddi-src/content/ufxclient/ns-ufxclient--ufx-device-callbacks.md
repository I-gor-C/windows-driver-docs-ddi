---
UID: NS.ufxclient._UFX_DEVICE_CALLBACKS
title: UFX_DEVICE_CALLBACKS
author: windows-driver-content
description: The UFX_DEVICE_CALLBACKS structure is used to define then event callback functions supported by the client driver.
old-location: buses\ufx_device_callbacks.htm
old-project: usbref
ms.assetid: 71D83E2C-8557-45FC-9769-DB71F5FF61FF
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UFX_DEVICE_CALLBACKS, UFX_DEVICE_CALLBACKS, *PUFX_DEVICE_CALLBACKS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ufxclient.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFX_DEVICE_CALLBACKS
req.alt-loc: ufxclient.h
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

# UFX_DEVICE_CALLBACKS structure



## -description
<p>The <b>UFX_DEVICE_CALLBACKS</b> structure is used to define then event callback functions supported by the client driver. </p>


## -syntax

````
typedef struct _UFX_DEVICE_CALLBACKS {
  ULONG                                           Size;
  PFN_UFX_DEVICE_HOST_CONNECT                     EvtDeviceHostConnect;
  PFN_UFX_DEVICE_HOST_DISCONNECT                  EvtDeviceHostDisconnect;
   PFN_UFX_DEVICE_ADDRESSED                       EvtDeviceAddressed;
  PFN_UFX_DEVICE_ENDPOINT_ADD                     EvtDeviceEndpointAdd;
  PFN_UFX_DEVICE_DEFAULT_ENDPOINT_ADD             EvtDeviceDefaultEndpointAdd;
  PFN_UFX_DEVICE_USB_STATE_CHANGE                 EvtDeviceUsbStateChange;
  PFN_UFX_DEVICE_PORT_CHANGE                      EvtDevicePortChange;
  PFN_UFX_DEVICE_PORT_DETECT                      EvtDevicePortDetect;
  PFN_UFX_DEVICE_REMOTE_WAKEUP_SIGNAL             EvtDeviceRemoteWakeupSignal;
  PFN_UFX_DEVICE_CONTROLLER_RESET                 EvtDeviceControllerReset;
   PFN_UFX_DEVICE_TEST_MODE_SET                   EvtDeviceTestModeSet;
  PFN_UFX_DEVICE_TESTHOOK                         EvtDeviceTestHook;
  PFN_UFX_DEVICE_SUPER_SPEED_POWER_FEATURE        EvtDeviceSuperSpeedPowerFeature;
  PFN_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT       EvtDeviceProprietaryChargerDetect;
  PFN_UFX_DEVICE_PROPRIETARY_CHARGER_SET_PROPERTY EvtDeviceProprietaryChargerSetProperty;
  PFN_UFX_DEVICE_PROPRIETARY_CHARGER_RESET        EvtDeviceProprietaryChargerReset;
} UFX_DEVICE_CALLBACKS, *PUFX_DEVICE_CALLBACKS;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size of the <b>UFX_DEVICE_CALLBACKS</b> structure.</p>
</dd>

### -field EvtDeviceHostConnect

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-host-connect.md">EVT_UFX_DEVICE_HOST_CONNECT</a> callback routine.</p>
</dd>

### -field EvtDeviceHostDisconnect

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-host-disconnect.md">EVT_UFX_DEVICE_HOST_DISCONNECT</a> callback routine.</p>
</dd>

### -field EvtDeviceAddressed

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-addressed.md">EVT_UFX_DEVICE_ADDRESSED</a> callback routine.</p>
</dd>

### -field EvtDeviceEndpointAdd

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-endpoint-add.md">EVT_UFX_DEVICE_ENDPOINT_ADD</a> callback routine.</p>
</dd>

### -field EvtDeviceDefaultEndpointAdd

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-default-endpoint-add.md">EVT_UFX_DEVICE_DEFAULT_ENDPOINT_ADD</a> callback routine.</p>
</dd>

### -field EvtDeviceUsbStateChange

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-usb-state-change.md">EVT_UFX_DEVICE_USB_STATE_CHANGE</a> callback routine.</p>
</dd>

### -field EvtDevicePortChange

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-port-change.md">EVT_UFX_DEVICE_PORT_CHANGE</a> callback routine.</p>
</dd>

### -field EvtDevicePortDetect

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-port-detect.md">EVT_UFX_DEVICE_PORT_DETECT</a> callback routine.</p>
</dd>

### -field EvtDeviceRemoteWakeupSignal

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-remote-wakeup-signal.md">EVT_UFX_DEVICE_REMOTE_WAKEUP_SIGNAL</a> callback routine.  </p>
</dd>

### -field EvtDeviceControllerReset

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-controller-reset.md">EVT_UFX_DEVICE_CONTROLLER_RESET</a> callback routine.</p>
</dd>

### -field EvtDeviceTestModeSet

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-test-mode-set.md">EVT_UFX_DEVICE_TEST_MODE_SET</a> callback routine.</p>
</dd>

### -field EvtDeviceTestHook

<dd>
<p>Reserved.  Should be set to NULL.</p>
</dd>

### -field EvtDeviceSuperSpeedPowerFeature

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-super-speed-power-feature.md">EVT_UFX_DEVICE_SUPER_SPEED_POWER_FEATURE</a> callback routine.</p>
</dd>

### -field EvtDeviceProprietaryChargerDetect

<dd>
<p>A pointer to the client driver’s <a href="buses.evt_ufx_device_detect_proprietary_charger">EVT_UFX_DEVICE_DETECT_PROPRIETARY_CHARGER</a> callback routine.</p>
</dd>

### -field EvtDeviceProprietaryChargerSetProperty

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-proprietary-charger-set-property.md">EVT_UFX_DEVICE_PROPRIETARY_CHARGER_SET_PROPERTY</a> callback routine.</p>
</dd>

### -field EvtDeviceProprietaryChargerReset

<dd>
<p>A pointer to the client driver’s <a href="..\ufxclient\nc-ufxclient-evt-ufx-device-proprietary-charger-reset.md">EVT_UFX_DEVICE_PROPRIETARY_CHARGER_RESET</a> callback routine.</p>
</dd>
</dl>

## -remarks
<p>The client driver shall use the <a href="..\ufxclient\nf-ufxclient-ufx-device-callbacks-init.md">UFX_DEVICE_CALLBACKS_INIT</a> macro to initialize the <b>UFX_DEVICE_CALLBACKS</b> structure, and then shall set fields of structure to the appropriate event callback routines prior to calling the <a href="..\ufxclient\nf-ufxclient-ufxdevicecreate.md">UfxDeviceCreate</a> export function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufxclient.h</dt>
</dl>
</td>
</tr>
</table>