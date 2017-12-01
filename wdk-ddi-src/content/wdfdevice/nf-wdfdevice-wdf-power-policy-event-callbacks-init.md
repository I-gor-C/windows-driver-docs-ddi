---
UID: NF.wdfdevice.WDF_POWER_POLICY_EVENT_CALLBACKS_INIT
title: WDF_POWER_POLICY_EVENT_CALLBACKS_INIT
author: windows-driver-content
description: The WDF_POWER_POLICY_EVENT_CALLBACKS_INIT function initializes a driver's WDF_POWER_POLICY_EVENT_CALLBACKS structure.
old-location: wdf\wdf_power_policy_event_callbacks_init.htm
old-project: wdf
ms.assetid: 09ab4995-58be-4d87-adf7-e843e637ac09
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_POWER_POLICY_EVENT_CALLBACKS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_POWER_POLICY_EVENT_CALLBACKS_INIT
req.alt-loc: wdfdevice.h
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

# WDF_POWER_POLICY_EVENT_CALLBACKS_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_POWER_POLICY_EVENT_CALLBACKS_INIT</b> function initializes a driver's <a href="..\wdfdevice\ns-wdfdevice--wdf-power-policy-event-callbacks.md">WDF_POWER_POLICY_EVENT_CALLBACKS</a> structure.</p>


## -syntax

````
VOID WDF_POWER_POLICY_EVENT_CALLBACKS_INIT(
  _Out_ PWDF_POWER_POLICY_EVENT_CALLBACKS Callbacks
);
````


## -parameters
<dl>

### -param <i>Callbacks</i> [out]

<dd>
<p>A pointer to a driver-allocated <a href="..\wdfdevice\ns-wdfdevice--wdf-power-policy-event-callbacks.md">WDF_POWER_POLICY_EVENT_CALLBACKS</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_POWER_POLICY_EVENT_CALLBACKS_INIT</b> function zeros the specified <a href="..\wdfdevice\ns-wdfdevice--wdf-power-policy-event-callbacks.md">WDF_POWER_POLICY_EVENT_CALLBACKS</a> structure and sets the structures <b>Size</b> member.</p>

<p>For a code example that uses <b>WDF_POWER_POLICY_EVENT_CALLBACKS_INIT</b>, see <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks.md">WdfDeviceInitSetPowerPolicyEventCallbacks</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>