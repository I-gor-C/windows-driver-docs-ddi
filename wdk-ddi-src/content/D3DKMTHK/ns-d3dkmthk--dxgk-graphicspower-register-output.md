---
UID: NS.d3dkmthk._DXGK_GRAPHICSPOWER_REGISTER_OUTPUT
title: DXGK_GRAPHICSPOWER_REGISTER_OUTPUT
author: windows-driver-content
description: A structure containing output data used to manage shared power components.
old-location: display\dxgk_graphicspower_register_output.htm
ms.assetid: 13F74BB4-91FE-4B5C-B0EB-B3524D0BD959
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_GRAPHICSPOWER_REGISTER_OUTPUT
req.alt-loc: d3dkmthk.h
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
ms.keywords: DXGK_GRAPHICSPOWER_REGISTER_OUTPUT, DXGK_GRAPHICSPOWER_REGISTER_OUTPUT, *PDXGK_GRAPHICSPOWER_REGISTER_OUTPUT
req.iface: 
---

# DXGK_GRAPHICSPOWER_REGISTER_OUTPUT structure



## -description
<p>A structure containing output data used to manage shared power components.</p>


## -syntax

````
typedef struct _DXGK_GRAPHICSPOWER_REGISTER_OUTPUT {
  PVOID                                  DeviceHandle;
  DEVICE_POWER_STATE                     InitialGrfxPowerState;
  PDXGK_SET_SHARED_POWER_COMPONENT_STATE SetSharedPowerComponentStateCb;
  PDXGK_GRAPHICSPOWER_UNREGISTER         UnregisterCb;
} DXGK_GRAPHICSPOWER_REGISTER_OUTPUT, *PDXGK_GRAPHICSPOWER_REGISTER_OUTPUT;
````


## -struct-fields
<dl>

### -field <b>DeviceHandle</b>

<dd>
<p>An opaque handle that should be provided when making callbacks to the graphics device.</p>
</dd>

### -field <b>InitialGrfxPowerState</b>

<dd>
<p>The power state of the graphics device represented by the DeviceHandle at the time of internal IOCTL handling.</p>
</dd>

### -field <b>SetSharedPowerComponentStateCb</b>

<dd>
<p>A callback to indicate whether the specified power component is active.  The component index should match the index used by the graphics driver when the component was indicated at driver initialization and the component must be one of the shared power component types. If this callback is used to set a state which has already been set by this driver for this graphics device, the call will have no effect. If setting a component active, the graphics driver will be notified synchronously before this callback returns.</p>
</dd>

### -field <b>UnregisterCb</b>

<dd>
<p> A callback to un-register itself with the graphics driver.  All shared power components should no longer be active.  The system will behave as if SetSharedPowerComponentStateCb had been called for all active shared power components with a new active state of FALSE.  Upon return, previously provided callbacks can no longer be used.</p>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>