---
UID: NS.gnssdriver.PGNSS_EVENT
title: PGNSS_EVENT
author: windows-driver-content
description: This structure defines the information required for a GNSS event.
old-location: sensors\gnss_event.htm
old-project: sensors
ms.assetid: FECF2444-CFF7-4B4D-AC3A-D3DD9B045AFD
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: PGNSS_EVENT, GNSS_EVENT, *PGNSS_EVENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_EVENT
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
req.irql: 
req.iface: 
---

# PGNSS_EVENT structure



## -description
<p>This structure defines the information required for a  GNSS event.</p>


## -syntax

````
typedef struct {
  ULONG           Size;
  ULONG           Version;
  GNSS_EVENT_TYPE EventType;
  ULONG           EventDataSize;
  BYTE            Unused[512];
  union {
    GNSS_FIXDATA                       FixData;
    GNSS_AGNSS_REQUEST_PARAM           AgnssRequest;
    GNSS_NI_REQUEST_PARAM              NiRequest;
    GNSS_ERRORINFO                     ErrorInformation;
    GNSS_NMEA_DATA                     NmeaData;
    GNSS_GEOFENCE_ALERT_DATA           GeofenceAlertData;
    GNSS_BREADCRUMBING_ALERT_DATA      BreadcrumbAlertData;
    GNSS_GEOFENCES_TRACKINGSTATUS_DATA GeofencesTrackingStatus;
    GNSS_DRIVER_REQUEST_DATA           DriverRequestData;
    BYTE                               CustomData[ANYSIZE_ARRAY];
  };
} GNSS_EVENT, *PGNSS_EVENT;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Structure size.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version number.</p>
</dd>

### -field <b>EventType</b>

<dd>
<p>Event type.</p>
<p>Depending on the event type, a specific data element of the union will be filled.</p>
</dd>

### -field <b>EventDataSize</b>

<dd>
<p>The size of the event data union contained in this event.</p>
<p>The GNSS driver must fill in appropriate size to avoid excessive data-copy between the layers. The GNSS adapter will access only the initial bytes of the event data, as specified by this element.</p>
</dd>

### -field <b>Unused[512]</b>

<dd>
<p>Padding buffer.</p>
</dd>

### -field <b>FixData</b>

<dd>
<p>This structure is filled if EventType is GNSS_Fix_Available.</p>
</dd>

### -field <b>AgnssRequest</b>

<dd>
<p>This structure is filled if EventType is GNSS_Require_Agnss.</p>
</dd>

### -field <b>NiRequest</b>

<dd>
<p>This structure is filled if EventType is GNSS_Event_Ni.</p>
</dd>

### -field <b>ErrorInformation</b>

<dd>
<p>This structure is filled if EventType is GNSS_Error.</p>
</dd>

### -field <b>NmeaData</b>

<dd>
<p>This structure is filled if EventType is GNSS_Event_NmeaData.</p>
</dd>

### -field <b>GeofenceAlertData</b>

<dd>
<p>This structure is filled if EventType is GNSS_Event_GeofenceAlertData.</p>
</dd>

### -field <b>BreadcrumbAlertData</b>

<dd>
<p>This structure contains alert information for when the breadcrumb buffer has reached a level where OS read operations should be performed.</p>
</dd>

### -field <b>GeofencesTrackingStatus</b>

<dd>
<p>This structure is filled if EventType is GNSS_Event_GeofencesTrackingStatus.</p>
</dd>

### -field <b>DriverRequestData</b>

<dd>
<p>This structure is filled if EventType is GNSS_Event_DriverRequest.</p>
</dd>

### -field <b>CustomData[ANYSIZE_ARRAY]</b>

<dd>
<p>Custom data field.</p>
</dd>
</dl>

## -remarks
<p>The GNSS driver sends solicited and unsolicited notifications to the GNSS adapter. This is done through a common event protocol between the driver and the GNSS adapter. The adapter registers for one or more types of events and this ensures that one or more I/O requests are always pending for the driver to send the notification up to the adapter. The driver completes the I/O request on the pending IRP and this causes the notification to flow up to the adapter. The adapter creates one or more I/O requests to listen for further notifications.</p>

<p> It is recommended (but not required) that the driver uses separate queues for managing different types of event. Separation of queues allows the driver to process certain types of events in parallel.</p>

<p>The notification model allows for adding custom or vendor-specific events in the future that can optionally be processed by a custom GNSS helper component. The GNSS adapter can act as a broker between the driver and the helper component and ensures that the commands and data are marshaled between these two components back and forth.</p>

<p>Each event type has associate event-specific data that the GNSS adapter uses to determine how to process the specific event. For example, for assistance requirements (AGNSS), the adapter injects the needed assistance data. For data-retrieval type event, the adapter processes and sends the data to an upper layer. Subsequently the adapter re-registers for same event with the driver through well-defined IOCTLs. All events follow the same overall data-structure.</p>

<p>Events can be of various types. Certain events occur as a result of a previous request initiated by the driver (for example, a start fix request). Certain events are raised for informational purpose. Assistance events are raised when the driver requires the adapter to inject specific assistance data.</p>

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