---
UID: NE.gnssdriver.GNSS_GEOFENCE_STATE
title: GNSS_GEOFENCE_STATE
author: windows-driver-content
description: GNSS_GEOFENCE_STATE enumerates the various states of a single geofence.
old-location: sensors\gnss_geofence_state.htm
ms.assetid: 881363B2-CF4C-4D18-9F45-829771A2D325
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: sensors
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_GEOFENCE_STATE
req.alt-loc: gnssdriver.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_, FWPS_VSWITCH_EVENT_DISPATCH_TABLE0
req.iface: 
---

# GNSS_GEOFENCE_STATE enumeration



## -description
<p>GNSS_GEOFENCE_STATE enumerates the various states of a single geofence.</p>


## -syntax

````
typedef enum  { 
  GNSS_GeofenceState_Unknown  = 0x00,
  GNSS_GeofenceState_Entered  = 0x01,
  GNSS_GeofenceState_Exited   = 0x02
} GNSS_GEOFENCE_STATE;
````


## -enum-fields
<dl>

### -field <a id="GNSS_GeofenceState_Unknown"></a><a id="gnss_geofencestate_unknown"></a><a id="GNSS_GEOFENCESTATE_UNKNOWN"></a><b>GNSS_GeofenceState_Unknown</b>

<dd>
<p>The state of the geofence is unknown.</p>
</dd>

### -field <a id="GNSS_GeofenceState_Entered"></a><a id="gnss_geofencestate_entered"></a><a id="GNSS_GEOFENCESTATE_ENTERED"></a><b>GNSS_GeofenceState_Entered</b>

<dd>
<p>The geofence has been entered.</p>
</dd>

### -field <a id="GNSS_GeofenceState_Exited"></a><a id="gnss_geofencestate_exited"></a><a id="GNSS_GEOFENCESTATE_EXITED"></a><b>GNSS_GeofenceState_Exited</b>

<dd>
<p>The geofence has been exited.</p>
</dd>
</dl>

## -remarks
<p>The following bitmasks are used by the HLOS to request state-change alerts for geofences:</p>

<p>An entry alert is raised when the previous state of the geofence was unknown or exited and the device has now entered the geofence.</p>

<p>An exit alert is raised when the previous state of the geofence was entered and the device has now exited the geofence. If the previous state of the geofence was unknown, and the device is currently outside of the geofence, no exit alert will be generated.</p>

<p>The location platform only sends an exit trigger to apps when the previous known state for a fence is inside the fence. This is a design decision to avoid chattiness of exit events on geofence configuration (For example, when not expecting a user configuring an exit fence from home to need to be notified that they are outside of home if they configure the notification when they are already outside of the home). Nevertheless, the location platform could handle where the GNSS driver sends exit events, but it is not recommend because then the interaction between the GNSS adapter and the GNSS driver will become very verbose. Given that the chances of the user entering a geofence are much smaller than the user being outside a geofences, this behavior reduces the required interaction between the GNSS driver and the GNSS adapter. For example, in the  case of 100 geofences pushed to the GNSS driver, and a user was outside all of them, without this behavior the will need to send to the GNSS adapter 100 exit notifications. The likelihood of something similar to this happening for entry events is very small.</p>

<p>The geofence state transition and the associated alerts are shown below. For simplicity, the hysteresis and geofence boundary conditions are implied.</p>

<p>The key aspects of this state diagram are:</p>

<p>No alert is to be raised when transitioning from GNSS_GeofenceState_Unknown to GNSS_GeofenceState_Exited state.</p>

<p>When the GNSS engine is unable to track any geofences at all, a single global tracking status alert needs to be raised, as opposed to one alert for each geofence. The GNSS engine could maintain the last know state for each fence instead of transitioning to GNSS_GeofenceState_Unknown state, so that when it is able to track again, the needed geofence alerts can be raised based on the new entry/exit detection. </p>

<p>Maintaining this last known state is not currently necessary though, because once the GNSS driver raises the event with gnss_geofences_tracking_status as FAILURE, the location platform in the HLOS will start doing the geofences tracking. During this time, the GNSS engine should continue to check, in a power optimized way, if geofences can be tracked again. The IHV can use optimizations to make this detection at low power. Common techniques for optimization include the following:</p>

<p>Progressive back-off</p>

<p>Waiting for low-cost signals that are indicative of device movements such as accelerator data or cellular/WiFi change notifications.</p>

<p>Requesting a low-accuracy distance tracking session from the HLOS using the public Geolocation WinRT APIs.</p>

<p>Low power checks for satellite signal.</p>

<p>When GNSS engine is able to track geofences again, it communicates so by setting the gnss_geofence_tracking_status as SUCCESS to GNSS adapter/HLOS</p>

<p>The GNSS adapter will issue GNSS_ResetGeofenceTracking commands and re-add currently active geofences with current entry/exit criteria of each geofence. This needs to be done in case the set of geofences to be tracked has changed or in the state for any geofence has changed. </p>

<p>The following bitmasks are used by the HLOS to request state-change alerts for geofences:</p>

<p>An entry alert is raised when the previous state of the geofence was unknown or exited and the device has now entered the geofence.</p>

<p>An exit alert is raised when the previous state of the geofence was entered and the device has now exited the geofence. If the previous state of the geofence was unknown, and the device is currently outside of the geofence, no exit alert will be generated.</p>

<p>The location platform only sends an exit trigger to apps when the previous known state for a fence is inside the fence. This is a design decision to avoid chattiness of exit events on geofence configuration (For example, when not expecting a user configuring an exit fence from home to need to be notified that they are outside of home if they configure the notification when they are already outside of the home). Nevertheless, the location platform could handle where the GNSS driver sends exit events, but it is not recommend because then the interaction between the GNSS adapter and the GNSS driver will become very verbose. Given that the chances of the user entering a geofence are much smaller than the user being outside a geofences, this behavior reduces the required interaction between the GNSS driver and the GNSS adapter. For example, in the  case of 100 geofences pushed to the GNSS driver, and a user was outside all of them, without this behavior the will need to send to the GNSS adapter 100 exit notifications. The likelihood of something similar to this happening for entry events is very small.</p>

<p>The geofence state transition and the associated alerts are shown below. For simplicity, the hysteresis and geofence boundary conditions are implied.</p>

<p>The key aspects of this state diagram are:</p>

<p>No alert is to be raised when transitioning from GNSS_GeofenceState_Unknown to GNSS_GeofenceState_Exited state.</p>

<p>When the GNSS engine is unable to track any geofences at all, a single global tracking status alert needs to be raised, as opposed to one alert for each geofence. The GNSS engine could maintain the last know state for each fence instead of transitioning to GNSS_GeofenceState_Unknown state, so that when it is able to track again, the needed geofence alerts can be raised based on the new entry/exit detection. </p>

<p>Maintaining this last known state is not currently necessary though, because once the GNSS driver raises the event with gnss_geofences_tracking_status as FAILURE, the location platform in the HLOS will start doing the geofences tracking. During this time, the GNSS engine should continue to check, in a power optimized way, if geofences can be tracked again. The IHV can use optimizations to make this detection at low power. Common techniques for optimization include the following:</p>

<p>Progressive back-off</p>

<p>Waiting for low-cost signals that are indicative of device movements such as accelerator data or cellular/WiFi change notifications.</p>

<p>Requesting a low-accuracy distance tracking session from the HLOS using the public Geolocation WinRT APIs.</p>

<p>Low power checks for satellite signal.</p>

<p>When GNSS engine is able to track geofences again, it communicates so by setting the gnss_geofence_tracking_status as SUCCESS to GNSS adapter/HLOS</p>

<p>The GNSS adapter will issue GNSS_ResetGeofenceTracking commands and re-add currently active geofences with current entry/exit criteria of each geofence. This needs to be done in case the set of geofences to be tracked has changed or in the state for any geofence has changed. </p>

<p>The following bitmasks are used by the HLOS to request state-change alerts for geofences:</p>

<p>An entry alert is raised when the previous state of the geofence was unknown or exited and the device has now entered the geofence.</p>

<p>An exit alert is raised when the previous state of the geofence was entered and the device has now exited the geofence. If the previous state of the geofence was unknown, and the device is currently outside of the geofence, no exit alert will be generated.</p>

<p>The location platform only sends an exit trigger to apps when the previous known state for a fence is inside the fence. This is a design decision to avoid chattiness of exit events on geofence configuration (For example, when not expecting a user configuring an exit fence from home to need to be notified that they are outside of home if they configure the notification when they are already outside of the home). Nevertheless, the location platform could handle where the GNSS driver sends exit events, but it is not recommend because then the interaction between the GNSS adapter and the GNSS driver will become very verbose. Given that the chances of the user entering a geofence are much smaller than the user being outside a geofences, this behavior reduces the required interaction between the GNSS driver and the GNSS adapter. For example, in the  case of 100 geofences pushed to the GNSS driver, and a user was outside all of them, without this behavior the will need to send to the GNSS adapter 100 exit notifications. The likelihood of something similar to this happening for entry events is very small.</p>

<p>The geofence state transition and the associated alerts are shown below. For simplicity, the hysteresis and geofence boundary conditions are implied.</p>

<p>The key aspects of this state diagram are:</p>

<p>No alert is to be raised when transitioning from GNSS_GeofenceState_Unknown to GNSS_GeofenceState_Exited state.</p>

<p>When the GNSS engine is unable to track any geofences at all, a single global tracking status alert needs to be raised, as opposed to one alert for each geofence. The GNSS engine could maintain the last know state for each fence instead of transitioning to GNSS_GeofenceState_Unknown state, so that when it is able to track again, the needed geofence alerts can be raised based on the new entry/exit detection. </p>

<p>Maintaining this last known state is not currently necessary though, because once the GNSS driver raises the event with gnss_geofences_tracking_status as FAILURE, the location platform in the HLOS will start doing the geofences tracking. During this time, the GNSS engine should continue to check, in a power optimized way, if geofences can be tracked again. The IHV can use optimizations to make this detection at low power. Common techniques for optimization include the following:</p>

<p>Progressive back-off</p>

<p>Waiting for low-cost signals that are indicative of device movements such as accelerator data or cellular/WiFi change notifications.</p>

<p>Requesting a low-accuracy distance tracking session from the HLOS using the public Geolocation WinRT APIs.</p>

<p>Low power checks for satellite signal.</p>

<p>When GNSS engine is able to track geofences again, it communicates so by setting the gnss_geofence_tracking_status as SUCCESS to GNSS adapter/HLOS</p>

<p>The GNSS adapter will issue GNSS_ResetGeofenceTracking commands and re-add currently active geofences with current entry/exit criteria of each geofence. This needs to be done in case the set of geofences to be tracked has changed or in the state for any geofence has changed. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>