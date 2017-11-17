---
UID: NS.ufxclient._UFX_DEVICE_CALLBACKS
title: UFX_DEVICE_CALLBACKS
author: windows-driver-content
description: The UFX_DEVICE_CALLBACKS structure is used to define then event callback functions supported by the client driver.
old-location: buses\ufx_device_callbacks.htm
ms.assetid: 71D83E2C-8557-45FC-9769-DB71F5FF61FF
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
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
ms.keywords: UFX_DEVICE_CALLBACKS, UFX_DEVICE_CALLBACKS, *PUFX_DEVICE_CALLBACKS
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

### -field <b>Size</b>

<dd>
<p>The size of the <b>UFX_DEVICE_CALLBACKS</b> structure.</p>
</dd>

### -field <b>EvtDeviceHostConnect</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187852">EVT_UFX_DEVICE_HOST_CONNECT</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceHostDisconnect</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187853">EVT_UFX_DEVICE_HOST_DISCONNECT</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceAddressed</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187847">EVT_UFX_DEVICE_ADDRESSED</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceEndpointAdd</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187851">EVT_UFX_DEVICE_ENDPOINT_ADD</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceDefaultEndpointAdd</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187849">EVT_UFX_DEVICE_DEFAULT_ENDPOINT_ADD</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceUsbStateChange</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187863">EVT_UFX_DEVICE_USB_STATE_CHANGE</a> callback routine.</p>
</dd>

### -field <b>EvtDevicePortChange</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187854">EVT_UFX_DEVICE_PORT_CHANGE</a> callback routine.</p>
</dd>

### -field <b>EvtDevicePortDetect</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187855">EVT_UFX_DEVICE_PORT_DETECT</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceRemoteWakeupSignal</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187859">EVT_UFX_DEVICE_REMOTE_WAKEUP_SIGNAL</a> callback routine.  </p>
</dd>

### -field <b>EvtDeviceControllerReset</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187848">EVT_UFX_DEVICE_CONTROLLER_RESET</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceTestModeSet</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187862">EVT_UFX_DEVICE_TEST_MODE_SET</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceTestHook</b>

<dd>
<p>Reserved.  Should be set to NULL.</p>
</dd>

### -field <b>EvtDeviceSuperSpeedPowerFeature</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187860">EVT_UFX_DEVICE_SUPER_SPEED_POWER_FEATURE</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceProprietaryChargerDetect</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187850">EVT_UFX_DEVICE_DETECT_PROPRIETARY_CHARGER</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceProprietaryChargerSetProperty</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187858">EVT_UFX_DEVICE_PROPRIETARY_CHARGER_SET_PROPERTY</a> callback routine.</p>
</dd>

### -field <b>EvtDeviceProprietaryChargerReset</b>

<dd>
<p>A pointer to the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187857">EVT_UFX_DEVICE_PROPRIETARY_CHARGER_RESET</a> callback routine.</p>
</dd>
</dl>

## -remarks
<p>The client driver shall use the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187972">UFX_DEVICE_CALLBACKS_INIT</a> macro to initialize the <b>UFX_DEVICE_CALLBACKS</b> structure, and then shall set fields of structure to the appropriate event callback routines prior to calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187951">UfxDeviceCreate</a> export function.</p>

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