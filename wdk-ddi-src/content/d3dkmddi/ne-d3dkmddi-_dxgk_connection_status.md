---
UID: NE:d3dkmddi._DXGK_CONNECTION_STATUS
title: "_DXGK_CONNECTION_STATUS"
author: windows-driver-content
description: Enumeration indicating the connection status values which can be reported.
old-location: display\dxgk_connection_status.htm
old-project: display
ms.assetid: D78A845E-1F5D-42F7-9391-8F3F6555B7E5
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PDXGK_CONNECTION_STATUS, ConnectionStatusUninitialized, DXGK_CONNECTION_STATUS, DXGK_CONNECTION_STATUS enumeration [Display Devices], LinkConfigurationFailed, LinkConfigurationStarted, LinkConfigurationSucceeded, MonitorStatusConnected, MonitorStatusDisconnected, MonitorStatusUnknown, TargetStatusConnected, TargetStatusDisconnected, TargetStatusJoined, _DXGK_CONNECTION_STATUS, d3dkmddi/ConnectionStatusUninitialized, d3dkmddi/DXGK_CONNECTION_STATUS, d3dkmddi/LinkConfigurationFailed, d3dkmddi/LinkConfigurationStarted, d3dkmddi/LinkConfigurationSucceeded, d3dkmddi/MonitorStatusConnected, d3dkmddi/MonitorStatusDisconnected, d3dkmddi/MonitorStatusUnknown, d3dkmddi/TargetStatusConnected, d3dkmddi/TargetStatusDisconnected, d3dkmddi/TargetStatusJoined, display.dxgk_connection_status"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_CONNECTION_STATUS
product: Windows
targetos: Windows
req.typenames: DXGK_CONNECTION_STATUS, *PDXGK_CONNECTION_STATUS
---

# _DXGK_CONNECTION_STATUS Enumeration
Enumeration indicating the connection status values which can be reported.

## Syntax
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

## Constants

<table>
            
                <tr>
                    <td>ConnectionStatusUninitialized</td>
                    <td>Indicates that a variable of type DXGK_CONNECTION_STATUS has not yet been assigned a meaningful value.</td>
                </tr>
            
                <tr>
                    <td>LinkConfigurationFailed</td>
                    <td>Indicates that link configuration has failed so the OS will need to retry SetTimingsFromVidPn after re-enumerating co-functional timings in order to find out the timings available based on the now completed configuration.</td>
                </tr>
            
                <tr>
                    <td>LinkConfigurationStarted</td>
                    <td>Indicates that link configuration  is occurring on the specified target.  

If the target was enabled, then scan-out of pixels has stopped and any pending v-blank interrupts should be assumed to be lost as if the monitor had been disconnected.

If the target was not enabled, then there is no impact on this target.  Any targets daisy-chained downstream from the specified target need to be notified to the OS as in configuration separately. Although the OS comprehends daisy-chaining, configuration is link generic so the OS does not attempt to infer the link configuration status of downstream devices.</td>
                </tr>
            
                <tr>
                    <td>LinkConfigurationSucceeded</td>
                    <td>Indicates that link configuration has completed successfully and that the requested display timing is active.

If the target was previously enabled, then scan-out of pixels has resumed.  The OS will respond by turning v-blank interrupts back on and resuming flips as needed.</td>
                </tr>
            
                <tr>
                    <td>MonitorStatusConnected</td>
                    <td>Indicates that a monitor has been detected.</td>
                </tr>
            
                <tr>
                    <td>MonitorStatusDisconnected</td>
                    <td>Indicates that the monitor has been disconnected.</td>
                </tr>
            
                <tr>
                    <td>MonitorStatusUnknown</td>
                    <td>Indicates that the driver cannot detect if a monitor is connected to the target and that the driver can support sending a valid timing to the target.  This is only valid for analog targets.</td>
                </tr>
            
                <tr>
                    <td>TargetStatusConnected</td>
                    <td>Indicates that a new target has been detected.  The new target is downstream, a child, of the original target.  The new target Id must be unique.</td>
                </tr>
            
                <tr>
                    <td>TargetStatusDisconnected</td>
                    <td>Indicates that a target has been disconnected.  This implies that any other targets or monitors which are connected via this target have also been removed.  The implied removals do not need to be reported to the OS separately as the OS will comprehend that they have also been removed.  For joined targets, even though each constituent target must be reported, the disconnect is identified by the target which has gone away so only one report is required.</td>
                </tr>
            
                <tr>
                    <td>TargetStatusJoined</td>
                    <td>Indicates that a new target has been detected and that multiple targets are being joined together to form this new target.  Each target being joined together must be indicated to the OS with a DXGK_CONNECTION_CHANGE and all target join indications for a new target must be indicated within a single batch.</td>
                </tr>
            
                <tr>
                    <td>UINT</td>
                    <td></td>
                </tr>
</table>

## Remarks

Other than the uninitialized state, the values fall into three categories: target changes, monitor changes and link configuration changes.  Target changes represent the addition and removal of targets; monitor changes report the connection status of monitors which are attached to targets and link configuration changes report the status of the link to a monitor.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |