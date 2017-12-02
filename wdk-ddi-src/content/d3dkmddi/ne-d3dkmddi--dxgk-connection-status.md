---
UID: NE.d3dkmddi._DXGK_CONNECTION_STATUS
title: DXGK_CONNECTION_STATUS
author: windows-driver-content
description: Enumeration indicating the connection status values which can be reported.
old-location: display\dxgk_connection_status.htm
old-project: display
ms.assetid: D78A845E-1F5D-42F7-9391-8F3F6555B7E5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CONNECTION_STATUS
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_CONNECTION_STATUS enumeration



## -description
<p>Enumeration indicating the connection status values which can be reported.  </p>


## -syntax

````
typedef enum _DXGK_CONNECTION_STATUS { 
  ConnectionStatusUninitialized  = 0,
  TargetStatusDisconnected       = 4,
  TargetStatusConnected,
  TargetStatusJoined,
  MonitorStatusDisconnected      = 8,
  MonitorStatusUnknown,
  MonitorStatusConnected,
  LinkConfigurationStarted       = 12,
  LinkConfigurationFailed,
  LinkConfigurationSucceeded
} DXGK_CONNECTION_STATUS;
````


## -enum-fields
<dl>

### -field ConnectionStatusUninitialized

<dd>
<p>Indicates that a variable of type DXGK_CONNECTION_STATUS has not yet been assigned a meaningful value.</p>
</dd>

### -field TargetStatusDisconnected

<dd>
<p>Indicates that a target has been disconnected.  This implies that any other targets or monitors which are connected via this target have also been removed.  The implied removals do not need to be reported to the OS separately as the OS will comprehend that they have also been removed.  For joined targets, even though each constituent target must be reported, the disconnect is identified by the target which has gone away so only one report is required.</p>
</dd>

### -field TargetStatusConnected

<dd>
<p>Indicates that a new target has been detected.  The new target is downstream, a child, of the original target.  The new target Id must be unique.</p>
</dd>

### -field TargetStatusJoined

<dd>
<p>Indicates that a new target has been detected and that multiple targets are being joined together to form this new target.  Each target being joined together must be indicated to the OS with a DXGK_CONNECTION_CHANGE and all target join indications for a new target must be indicated within a single batch.</p>
</dd>

### -field MonitorStatusDisconnected

<dd>
<p>Indicates that the monitor has been disconnected.</p>
</dd>

### -field MonitorStatusUnknown

<dd>
<p>Indicates that the driver cannot detect if a monitor is connected to the target and that the driver can support sending a valid timing to the target.  This is only valid for analog targets.</p>
</dd>

### -field MonitorStatusConnected

<dd>
<p>Indicates that a monitor has been detected.</p>
</dd>

### -field LinkConfigurationStarted

<dd>
<p>Indicates that link configuration  is occurring on the specified target.  </p>
<p>If the target was enabled, then scan-out of pixels has stopped and any pending v-blank interrupts should be assumed to be lost as if the monitor had been disconnected.</p>
<p>If the target was not enabled, then there is no impact on this target.  Any targets daisy-chained downstream from the specified target need to be notified to the OS as in configuration separately. Although the OS comprehends daisy-chaining, configuration is link generic so the OS does not attempt to infer the link configuration status of downstream devices.</p>
</dd>

### -field LinkConfigurationFailed

<dd>
<p>Indicates that link configuration has failed so the OS will need to retry SetTimingsFromVidPn after re-enumerating co-functional timings in order to find out the timings available based on the now completed configuration.</p>
</dd>

### -field LinkConfigurationSucceeded

<dd>
<p>Indicates that link configuration has completed successfully and that the requested display timing is active.</p>
<p>If the target was previously enabled, then scan-out of pixels has resumed.  The OS will respond by turning v-blank interrupts back on and resuming flips as needed.
</p>
</dd>
</dl>

## -remarks
<p>Other than the uninitialized state, the values fall into three categories: target changes, monitor changes and link configuration changes.  Target changes represent the addition and removal of targets; monitor changes report the connection status of monitors which are attached to targets and link configuration changes report the status of the link to a monitor.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>