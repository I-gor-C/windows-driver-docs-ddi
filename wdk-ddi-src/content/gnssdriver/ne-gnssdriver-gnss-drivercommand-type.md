---
UID: NE.gnssdriver.GNSS_DRIVERCOMMAND_TYPE
title: GNSS_DRIVERCOMMAND_TYPE
author: windows-driver-content
description: This enumeration indicates the type of driver command or configuration for the GNSS driver provided in the GNSS_DRIVERCOMMAND_PARAM structure.
old-location: sensors\gnss_drivercommand_type.htm
ms.assetid: 61D7C52C-D8C9-4BBE-9DCA-B5E934A02FAE
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
req.alt-api: GNSS_DRIVERCOMMAND_TYPE
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

# GNSS_DRIVERCOMMAND_TYPE enumeration



## -description
<p>This enumeration indicates the type of driver command or configuration for the GNSS driver provided in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925107">GNSS_DRIVERCOMMAND_PARAM</a> structure.</p>


## -syntax

````
typedef enum  { 
  GNSS_SetLocationServiceEnabled    = 0x01,
  GNSS_SetLocationNIRequestAllowed  = 0x02,
  GNSS_ForceSatelliteSystem         = 0x03,
  GNSS_ForceOperationMode           = 0x04,
  GNSS_ResetEngine                  = 0x09,
  GNSS_ClearAgnssData               = 0x0A,
  GNSS_SetSuplVersion               = 0x0C,
  GNSS_SetNMEALogging               = 0x0D,
  GNSS_SetUplServerAccessInterval   = 0x0E,
  GNSS_SetNiTimeoutInterval         = 0x0F,
  GNSS_ResetGeofencesTracking       = 0x10,
  GNSS_CustomCommand                = 0x0100
} GNSS_DRIVERCOMMAND_TYPE;
````


## -enum-fields
<dl>

### -field <a id="GNSS_SetLocationServiceEnabled"></a><a id="gnss_setlocationserviceenabled"></a><a id="GNSS_SETLOCATIONSERVICEENABLED"></a><b>GNSS_SetLocationServiceEnabled</b>

<dd>
<p>Informs the driver whether location is enabled on the device. This command is issued each time the location service is enabled/disabled on the device. The associated command data is a <b>BOOL</b>.</p>
<p>Upon receiving this command set to FALSE the GNSS driver and GNSS device must:</p>
<ul>
<li>
<p>Stop any ongoing location sessions of any kind and from any HLOS application (if multiple applications are supported).</p>
</li>
<li>
<p>If the GNSS device or driver does any operations in the background, for example, geofence tracking, assistance data refresh, etc., they should also be stopped. The GNSS adapter will stop all offloaded operations  when location is disabled.</p>
</li>
<li>
<p>In relation to location requests from the mobile operator:</p>
<ul>
<li>
<p>Location requests from the mobile operator for emergency location, to meet CALEA requirements, etc, should still be served regardless of the location switch status. These requests are expected to have the privacy override flag set or/and be initiated around the time of the user making an emergency call.</p>
</li>
<li>
<p>Other network initiated location requests should honor the <b>GNSS_SetLocationNIRequestAllowed</b> command if this behavior is required by the mobile operator and implemented by the GNSS driver.</p>
</li>
</ul>
</li>
</ul>
<p>If the HLOS needs to initiate any new location request, for example to enable the user to remotely find the device, the GNSS adapter will send a command to set the <b>GNSS_SetLocationServiceEnabled</b> to TRUE, initiate the fix session, and when the results are received it will send another command to set the <b>GNSS_SetLocationServiceEnabled</b> to FALSE.</p>
<ul>
<li>
<p><b>GNSS_SetLocationServiceEnabled</b> set to TRUE=1-&gt; Enabled</p>
</li>
<li>
<p><b>GNSS_SetLocationServiceEnabled</b> set to FALSE=0-&gt; Disabled</p>
</li>
</ul>
<p>Unless this command is issued by the GNSS adapter, the driver must assume that the location service is disabled on the system. </p>
</dd>

### -field <a id="GNSS_SetLocationNIRequestAllowed"></a><a id="gnss_setlocationnirequestallowed"></a><a id="GNSS_SETLOCATIONNIREQUESTALLOWED"></a><b>GNSS_SetLocationNIRequestAllowed</b>

<dd>
<p>Informs the driver if it is allowed to entertain network initiated location requests coming from the mobile network. The command only needs to be supported if required by the mobile operator. As of Windows 10, Microsoft is not aware of any mobile operator requiring this any longer, but this remains to avoid  any blocking issues during commercialization. If the command is not implemented, the GNSS driver should simply keep its default behavior.</p>
<p>The associated command data is a <b>BOOL</b>.</p>
<ul>
<li>
<p><b>GNSS_SetLocationNIRequestAllowed</b> set to TRUE=1-&gt; Allow</p>
</li>
<li>
<p><b>GNSS_SetLocationNIRequestAllowed</b> set to FALSE=0-&gt; NotAllow</p>
</li>
</ul>
<p>Unless this command is explicitly issued by the GNSS adapter, the driver must assume that the NI requests are enabled on the system.</p>
<p>The GNSS adapter maintains a system-wide state indicating whether NI requests are allowed. This state is determined by the location master switch (the setting that the user can toggle to turn location on or off) and a setting configured by the mobile operator to indicate if NI requests depend on the location master switch or not.</p>
<p>The GNSS adapter will evaluate the value of these two settings and will indicate to the GNSS driver if NI requests are allowed or not.</p>
<p>The location requests for emergency services or for CALEA (for example, the case of privacy override being set) must be served regardless of the value of this setting.</p>
</dd>

### -field <a id="GNSS_ForceSatelliteSystem"></a><a id="gnss_forcesatellitesystem"></a><a id="GNSS_FORCESATELLITESYSTEM"></a><b>GNSS_ForceSatelliteSystem</b>

<dd>
<p>This command causes the GNSS driver to use the specified satellite system(s) for getting fixes. The parameter is a <b>DWORD</b> with the following values:</p>
<pre class="syntax" xml:space="preserve"><code>#define GNSS_SATELLITE_ANY          0x00
#define GNSS_SATELLITE_GPS          0x01
#define GNSS_SATELLITE_GLONASS      0x02
#define GNSS_SATELLITE_BEIDOU       0x04
#define GNSS_SATELLITE_GALILEO      0x08
</code></pre>
<p>0x03-0xFF: Reserved </p>
<p>This is expected to be used only for test purposes. Some mobile operators do require validations using a single satellite system.</p>
</dd>

### -field <a id="GNSS_ForceOperationMode"></a><a id="gnss_forceoperationmode"></a><a id="GNSS_FORCEOPERATIONMODE"></a><b>GNSS_ForceOperationMode</b>

<dd>
<p>This command causes the GNSS driver to use the specified operation mode. The parameter is a <b>DWORD</b> with the following values:</p>
<pre class="syntax" xml:space="preserve"><code>#define GNSS_OPERMODE_ANY          0x00
#define GNSS_OPERMODE_MSA          0x01
#define GNSS_OPERMODE_MSB          0x02
#define GNSS_OPERMODE_MSS          0x04
#define GNSS_OPERMODE_CELLID       0x08
#define GNSS_OPERMODE_AFLT         0x10
#define GNSS_OPERMODE_OTDOA        0x20
</code></pre>
<p>0x40-0xFF: Reserved</p>
<p>This command is used for two purposes:</p>
<ul>
<li>
<p>To configure the mode of operation in the case of SUPL configuration. It is expected that mobile operators will only configure the device to work in Microsoft-based mode by which the SUPL service is used to obtain assistance data (<b>GNSS_OPERMODE_MSB</b>), or in standalone mode (<b>GNSS_OPERMODE_MSS</b>) in which the GNSS device can work really standalone or use assistance obtained from sources other than the SUPL service. The standalone mode is actually equivalent to the default mode (<b>GNSS_OPERMODE_ANY</b>).</p>
</li>
<li>
<p>To configure different modes of operation for test purposes. This would mostly be used by mobile operators or OEMs for validation purposes.</p>
</li>
</ul>
<div class="alert"><b>Note</b>  Setting the SUPL <b>GNSS_ForceOperationMode</b> to <b>GNSS_OPERMODE_MSS</b> is an indication to the GNSS system to not do any kind of interaction with the SUPL server for AGNSS data.</div>
<div> </div>
</dd>

### -field <a id="GNSS_ResetEngine"></a><a id="gnss_resetengine"></a><a id="GNSS_RESETENGINE"></a><b>GNSS_ResetEngine</b>

<dd>
<p>This command clears up the state of the GNSS engine. After this command is issued the engine will be ready for a cold start fix:</p>
<ul>
<li>
<p>All assistance data will be deleted.</p>
</li>
<li>
<p>The almanac will persist.</p>
</li>
<li>
<p>The GNSS engine configuration parameters will persist.</p>
</li>
</ul>
<p>This command should only be called when there is no active fix session. This command is typically used for recursively testing the GNSS time to first fix on cold start.</p>
</dd>

### -field <a id="GNSS_ClearAgnssData"></a><a id="gnss_clearagnssdata"></a><a id="GNSS_CLEARAGNSSDATA"></a><b>GNSS_ClearAgnssData</b>

<dd>
<p>This command clears the AGNSS assistance data from the GNSS engine. This is used mainly for testing purpose to ensure that the driver requests for assistance data when a fix is requested. The associated command data contains the specific <a href="https://msdn.microsoft.com/library/windows/hardware/dn925097">GNSS_AGNSS_REQUEST_TYPE</a> enumeration to indicate the specific data element to be cleared:</p>
<ul>
<li>
<p>If <b>GNSS_AGNSS_TimeInjection</b> is specified, the time reference will be deleted in the GNSS engine. This may cause the GNSS engine to request again time injection.</p>
</li>
<li>
<p>If <b>GNSS_AGNSS_PositionInjection</b> is specified, the coarse position reference will be deleted in the GNSS engine. This may cause the GNSS engine to request again coarse position injection.</p>
</li>
<li>
<p>If <b>GNSS_AGNSS_BlobInjection</b> is specified, both ephemeris acquired from the satellites and any assistance blob injected will be deleted in the GNSS engine. This may cause the GNSS engine to request again an assistance blob.</p>
</li>
</ul>
<p>It is highly recommended that this command is supported for test purposes even if the assistance data is not obtained from the OS location platform.</p>
</dd>

### -field <a id="GNSS_SetSuplVersion_"></a><a id="gnss_setsuplversion_"></a><a id="GNSS_SETSUPLVERSION_"></a><b>GNSS_SetSuplVersion </b>

<dd>
<p>This command sets the SUPL version that the mobile operator wants supported. The command data contains a value of <a href="https://msdn.microsoft.com/library/windows/hardware/dn925233">GNSS_SUPL_VERSION</a> structure which includes both the major and the minor SUPL versions indicated by the mobile operator. The SUPL client should use the SUPL version as specifies in the OMA SUPL standards, summarizing:</p>
<ul>
<li>
<p>For network initiated scenarios, the SUPL INIT message from the H-SLP or E-SLP to the SET carries the intended SUPL major and minor version M1.m1 (normally the highest version supported by the SLP) in the version parameter. The SUPL INIT message also carries the minimum SUPL major version number M2 for which continuation of the session by the SET is possible in the minimum version parameter. The value of M2 will depend on the intended SUPL service – for example, for a single location fix M2 may be one; for triggered location M2 may be two. A SUPL session can be conducted between the SLP and the SET as long as the SET is using a SUPL major version between M2 and M1. The SET continues the SUPL session normally if it supports a major version M of SUPL between M2 and M1 (for example, M2 ≤ M ≤ M1) – and indicates this major version and a supported minor version m in the next message (for example, implicitly in the version parameter of the message).</p>
</li>
<li>
<p>For SET initiated SUPL sessions, the initial SUPL message from the SET carries the supported SUPL major and minor version M1.m1 (implicitly in the version parameter). The H-SLP continues the session if it supports the same major version M1 and otherwise sends a SUPL END and terminates the session.</p>
</li>
</ul>
</dd>

### -field <a id="GNSS_SetNMEALogging"></a><a id="gnss_setnmealogging"></a><a id="GNSS_SETNMEALOGGING"></a><b>GNSS_SetNMEALogging</b>

<dd>
<p>This command sets the status for NMEA logging.</p>
<p>This command causes the GNSS driver to start/stop providing the data fix information via NMEA strings. The GNSS driver must continue providing fixes in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925139">GNSS_FIXDATA</a> structure. The parameter is a <b>DWORD</b> with the following values:</p>
<pre class="syntax" xml:space="preserve"><code>#define GNSS_NMEALOGGING_NONE         0x00
#define GNSS_NMEALOGGING_ALL          0xFF
</code></pre>
<p>The default value for this command is no NMEA logging. This command should not persist across system restart.</p>
<p>This command has been introduced to support OEM testing. This command is not used by the location framework or by Microsoft test tools.</p>
</dd>

### -field <a id="GNSS_SetUplServerAccessInterval"></a><a id="gnss_setuplserveraccessinterval"></a><a id="GNSS_SETUPLSERVERACCESSINTERVAL"></a><b>GNSS_SetUplServerAccessInterval</b>

<dd>
<p>This command sets the minimum time in between requests to the server for assisted position to prevent service overload. The time interval is specified in seconds.</p>
<p>Mobile operators may use the configuration service provider to tune this setting, if they require it.  If this parameter is not supported, if can be ignored, but the SUPL configuration commands must not fail.</p>
</dd>

### -field <a id="GNSS_SetNiTimeoutInterval"></a><a id="gnss_setnitimeoutinterval"></a><a id="GNSS_SETNITIMEOUTINTERVAL"></a><b>GNSS_SetNiTimeoutInterval</b>

<dd>
<p>This command sets how much time the device must wait for input from a user before it responds to the NI request executing the default action. The time interval is specified in seconds and the default value is 35 seconds. This timeout is 5 seconds larger than the timeout used by the operating system to wait for response from the user, and it is simply a failsafe in case of the operating system not responding. This command is applicable only to network initiated requests in which the verification from the user is requested. Mobile operators may use the configuration service provider to override the default value from the operating system. In such case the default values specified above should be replaced by the values provided by the mobile operator.</p>
</dd>

### -field <a id="GNSS_ResetGeofencesTracking"></a><a id="gnss_resetgeofencestracking"></a><a id="GNSS_RESETGEOFENCESTRACKING"></a><b>GNSS_ResetGeofencesTracking</b>

<dd>
<p>This command resets the geofence tracking operation. The GNSS driver must delete all geofences from the GNSS engine, stop geofence tracking and stop monitoring for signal conditions. The geofence tracking operation will begin as usual only when the HLOS creates one or more new geofences.</p>
</dd>

### -field <a id="GNSS_CustomCommand"></a><a id="gnss_customcommand"></a><a id="GNSS_CUSTOMCOMMAND"></a><b>GNSS_CustomCommand</b>

<dd>
<p>Range for custom IHV-specific GNSS commands:  0x0100 – 0x01FF</p>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>