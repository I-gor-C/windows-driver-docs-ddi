---
UID: NS.ucxusbdevice._USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS
title: USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS
author: windows-driver-content
description: Contains parameters for a request to update USB 2.0 link power management (LPM). UCX passes this structure in the EVT_UCX_USBDEVICE_UPDATE callback function.
old-location: buses\_usbdevice_update_20_hardware_lpm_parameters.htm
old-project: usbref
ms.assetid: B02CB10F-18C9-4E2C-9F30-042588800EA5
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS, USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS
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
req.alt-api: USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS
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

# USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS structure



## -description
<p>Contains parameters for a request to update USB 2.0 link power management (LPM). UCX passes this structure in the  <a href="buses.evt_ucx_usbdevice_update">EVT_UCX_USBDEVICE_UPDATE</a> callback function.</p>


## -syntax

````
typedef struct _USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS {
  ULONG HardwareLpmEnable  :1;
  ULONG RemoteWakeEnable  :1;
  ULONG HostInitiatedResumeDurationMode  :1;
  ULONG BestEffortServiceLatency  :4;
  ULONG BestEffortServiceLatencyDeep  :4;
  ULONG L1Timeout  :8;
  ULONG Reserved  :13;
} USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS, *P_USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>HardwareLpmEnable</b>

<dd>
<p>If set, indicates are request to enable hardware LPM.</p>
</dd>

### -field <b>RemoteWakeEnable</b>

<dd>
<p>If set, indicates are request to enable remote wake signal.</p>
</dd>

### -field <b>HostInitiatedResumeDurationMode</b>

<dd>
<p>The requested resume period.</p>
</dd>

### -field <b>BestEffortServiceLatency</b>

<dd>
<p>The requested best effort service latency.</p>
</dd>

### -field <b>BestEffortServiceLatencyDeep</b>

<dd>
<p>The requested best effort service latency deep.</p>
</dd>

### -field <b>L1Timeout</b>

<dd>
<p>The requested L1 timeout.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Do not use.</p>
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
<a href="buses._roothub_20port_info">ROOTHUB_20PORT_INFO</a>
</dt>
<dt>
<a href="buses._usbdevice_update">USBDEVICE_UPDATE</a>
</dt>
<dt>
<a href="buses._usbdevice_update_flags">USBDEVICE_UPDATE_FLAGS</a>
</dt>
<dt>
<a href="buses._usbdevice_update_failure_flags">USBDEVICE_UPDATE_FAILURE_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
