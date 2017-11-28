---
UID: NE.gnssdriver.GNSS_EVENT_TYPE
title: GNSS_EVENT_TYPE
author: windows-driver-content
description: This enumeration indicates the type of an event and is used by the GNSS_EVENT structure.
old-location: sensors\gnss_event_type.htm
old-project: sensors
ms.assetid: BC862E22-992E-497D-B370-97ABE8897728
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_, FWPS_VSWITCH_EVENT_DISPATCH_TABLE0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_EVENT_TYPE
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
req.iface: 
---

# GNSS_EVENT_TYPE enumeration



## -description
<p>This enumeration indicates the type of an event and is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925134">GNSS_EVENT</a> structure.</p>
<p>The GNSS driver utilizes events to send solicited and unsolicited information to the GNSS adapter. Events can occur for various reasons, such as a driver request to the GNSS adapter for the injection of assistance data or for informational purposes.
</p>


## -syntax

````
typedef enum  { 
  GNSS_Event_FixAvailable             = 0x0001,
  GNSS_Event_RequireAgnss             = 0x0002,
  GNSS_Event_Error                    = 0x0003,
  GNSS_Event_NiRequest                = 0x000C,
  GNSS_Event_NmeaData                 = 0x000D,
  GNSS_Event_GeofenceAlertData        = 0x000E,
  GNSS_Event_GeofencesTrackingStatus  = 0x000F,
  GNSS_Event_DriverRequest            = 0x0010,
  GNSS_Event_BreadcrumbAlertEvent     = 0x0011,
  GNSS_Event_Custom                   = 0x8000
} GNSS_EVENT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="GNSS_Event_FixAvailable"></a><a id="gnss_event_fixavailable"></a><a id="GNSS_EVENT_FIXAVAILABLE"></a><b>GNSS_Event_FixAvailable</b>

<dd>
<p>This event is raised as a result of a prior <a href="https://msdn.microsoft.com/library/windows/hardware/dn917731">IOCTL_GNSS_GET_FIXDATA</a> call from the adapter. The GNSS driver raises this event when a fix is available for the adapter to collect. The fix data is included in the event data in form of <a href="https://msdn.microsoft.com/library/windows/hardware/dn925139">GNSS_FIXDATA</a> structure.</p>
</dd>

### -field <a id="GNSS_Event_RequireAgnss"></a><a id="gnss_event_requireagnss"></a><a id="GNSS_EVENT_REQUIREAGNSS"></a><b>GNSS_Event_RequireAgnss</b>

<dd>
<p>This event is raised as a result of a prior <a href="https://msdn.microsoft.com/library/windows/hardware/dn917733">IOCTL_GNSS_LISTEN_AGNSS</a> call from the adapter. The driver raises this event whenever it needs injection of certain AGNSS assistance data. The specifics of the injection are available in the event data in form of <a href="https://msdn.microsoft.com/library/windows/hardware/dn925096">GNSS_AGNSS_REQUEST_PARAM</a> structure.</p>
</dd>

### -field <a id="GNSS_Event_Error"></a><a id="gnss_event_error"></a><a id="GNSS_EVENT_ERROR"></a><b>GNSS_Event_Error</b>

<dd>
<p>This event is raised as a result of a prior <a href="..\gnssdriver\ni-gnssdriver-ioctl-gnss-listen-error.md">IOCTL_GNSS_LISTEN_ERROR</a> call from the adapter. The driver raises this event when an out-of-band error occurs that the adapter needs to be aware of. The error details are available in the event data in form of <a href="https://msdn.microsoft.com/library/windows/hardware/dn925130">GNSS_ERRORINFO</a> structure. The information can be used by Microsoft to capture telemetry data about what type of errors are seen in the field by different devices, and the data could be shared with OEMs/IHVs to help understand common issues and increase the quality of GNSS engine implementations.</p>
</dd>

### -field <a id="GNSS_Event_NiRequest"></a><a id="gnss_event_nirequest"></a><a id="GNSS_EVENT_NIREQUEST"></a><b>GNSS_Event_NiRequest</b>

<dd>
<p>This event is raised when the driver wants to notify an NI request. The HLOS will process the request (for example, display a dialog if requested) then inject a response back to the driver.</p>
</dd>

### -field <a id="GNSS_Event_NmeaData"></a><a id="gnss_event_nmeadata"></a><a id="GNSS_EVENT_NMEADATA"></a><b>GNSS_Event_NmeaData</b>

<dd>
<p>This event is raised as a result of a prior <a href="https://msdn.microsoft.com/library/windows/hardware/dn917739">IOCTL_GNSS_LISTEN_NMEA</a> call, if NMEA logging is enabled in the device. The GNSS driver raises this event when NMEA data is ready to be read by the calling client. The calling client will typically be a test tool. The NMEA sentences data is included in the event data in form of <a href="https://msdn.microsoft.com/library/windows/hardware/dn925202">GNSS_NMEA_DATA</a> structure.
</p>
</dd>

### -field <a id="GNSS_Event_GeofenceAlertData"></a><a id="gnss_event_geofencealertdata"></a><a id="GNSS_EVENT_GEOFENCEALERTDATA"></a><b>GNSS_Event_GeofenceAlertData</b>

<dd>
<p>A previously created geofence has been breached. At the creation time of the geofence, the HLOS had specifically asked for an alert when such a breach happens. For example, an alert for entry should not be raised if the HLOS has requested only exit alerts.</p>
</dd>

### -field <a id="GNSS_Event_GeofencesTrackingStatus"></a><a id="gnss_event_geofencestrackingstatus"></a><a id="GNSS_EVENT_GEOFENCESTRACKINGSTATUS"></a><b>GNSS_Event_GeofencesTrackingStatus</b>

<dd>
<p>The GNSS engine is unable to track one or more geofences due to bad signal conditions or other positioning issues. A status is also raised when the GNSS engine has recovered from a previous failure condition and is now able to track all the geofences.</p>
</dd>

### -field <a id="GNSS_Event_DriverRequest"></a><a id="gnss_event_driverrequest"></a><a id="GNSS_EVENT_DRIVERREQUEST"></a><b>GNSS_Event_DriverRequest</b>

<dd>
<p>Reserved for future extension. The GNSS driver is requesting some out-of-band information from the HLOS.</p>
</dd>

### -field <a id="GNSS_Event_BreadcrumbAlertEvent"></a><a id="gnss_event_breadcrumbalertevent"></a><a id="GNSS_EVENT_BREADCRUMBALERTEVENT"></a><b>GNSS_Event_BreadcrumbAlertEvent</b>

<dd>
<p>Reserved for future extension:</p>
<table>
<tr>
<td>
<p>0x0012- 0x7FFF</p>
</td>
<td>
<p>For each new event type, there will be a well-defined IOCTL describing the initiation process of this event by the adapter, and a well-defined event data structure describing the data/command associated with this event.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="GNSS_Event_Custom"></a><a id="gnss_event_custom"></a><a id="GNSS_EVENT_CUSTOM"></a><b>GNSS_Event_Custom</b>

<dd>
<p>Reserved for vendor-specific custom actions:</p>
<table>
<tr>
<td>
<p>0x8000-0xFFFF</p>
</td>
<td>
<p>The GNSS driver raises this event as needed. The command and data are packaged in an opaque blob as part of the event data. The package is sent up to the adapter for marshaling to the GNSS helper component.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>Events can be of various types. Certain events occur as a result of a previous request initiated by the driver, for example, start fix request. Certain events are raised for informational purpose. Assistance events are raised when the driver requires the adapter to inject specific assistance data.</p>

<p>Events can be of various types. Certain events occur as a result of a previous request initiated by the driver, for example, start fix request. Certain events are raised for informational purpose. Assistance events are raised when the driver requires the adapter to inject specific assistance data.</p>

<p>Events can be of various types. Certain events occur as a result of a previous request initiated by the driver, for example, start fix request. Certain events are raised for informational purpose. Assistance events are raised when the driver requires the adapter to inject specific assistance data.</p>

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