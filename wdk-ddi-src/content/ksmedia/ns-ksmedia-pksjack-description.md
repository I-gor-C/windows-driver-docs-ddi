---
UID: NS.ksmedia.PKSJACK_DESCRIPTION
title: PKSJACK_DESCRIPTION
author: windows-driver-content
description: The KSJACK_DESCRIPTION structure specifies the physical attributes of an audio jack.
old-location: audio\ksjack_description.htm
old-project: audio
ms.assetid: 303bc73a-fe47-499b-97b3-7c49a40e8cfa
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PKSJACK_DESCRIPTION, KSJACK_DESCRIPTION, *PKSJACK_DESCRIPTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSJACK_DESCRIPTION
req.alt-loc: ksmedia.h
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

# PKSJACK_DESCRIPTION structure



## -description
<p>The KSJACK_DESCRIPTION structure specifies the physical attributes of an audio jack.</p>


## -syntax

````
typedef struct {
  DWORD              ChannelMapping;
  DWORD              Color;
  EPcxConnectionType ConnectionType;
  EPcxGeoLocation    GeoLocation;
  EPcxGenLocation    GenLocation;
  EPxcPortConnection PortConnection;
  BOOL               IsConnected;
} KSJACK_DESCRIPTION, *PKSJACK_DESCRIPTION;
````


## -struct-fields
<dl>

### -field <b>ChannelMapping</b>

<dd>
<p>Specifies the mapping of the audio channels to the corresponding speaker positions. <b>ChannelMapping</b> is a bitmask of the KSAUDIO_SPEAKER_<i>XXX</i> flags (for example, SPEAKER_FRONT_LEFT | SPEAKER_FRONT_RIGHT), which are defined in the header file Ksmedia.h. <b>ChannelMapping</b> should be nonzero only for analog rendering pins. For capture pins or for digital rendering pins, set this member to 0.</p>
<div class="alert"><b>Note</b>  Devicetopology.h originally defined <b>ChannelMapping</b> as an enumeration of type <b>EChannelMapping</b>. The <b>EChannelMapping</b> enumeration has since been deprecated and is no longer used in Windows Vista and later versions of the Windows operating systems. </div>
<div> </div>
</dd>

### -field <b>Color</b>

<dd>
<p>Specifies the jack color. The color is expressed as a 32-bit RGB value that is formed by concatenating the 8-bit blue, green, and red color components. The blue component occupies the 8 least-significant bits (bits 0-7), the green component occupies bits 8-15, and the red component occupies bits 16-23. The 8 most-significant bits are zeros. If the jack color is unknown or the physical connector has no identifiable color, the value of this member is 0x00000000, which represents black.</p>
</dd>

### -field <b>ConnectionType</b>

<dd>
<p>Specifies the physical connection type for this jack. The value of this member is one of the <b>EPcxConnectionType</b> enumeration values shown in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Connector type</th>
</tr>
<tr>
<td>
<p>eConnTypeUnknown</p>
</td>
<td>
<p>Unknown</p>
</td>
</tr>
<tr>
<td>
<p>eConnType3Point5mm</p>
</td>
<td>
<p>3.5 mm minijack</p>
</td>
</tr>
<tr>
<td>
<p>eConnTypeQuarter</p>
</td>
<td>
<p>1/4-inch jack</p>
</td>
</tr>
<tr>
<td>
<p>eConnTypeAtapiInternal</p>
</td>
<td>
<p>ATAPI internal connector</p>
</td>
</tr>
<tr>
<td>
<p>eConnTypeRCA</p>
</td>
<td>
<p>RCA jack</p>
</td>
</tr>
<tr>
<td>
<p>eConnTypeOptical</p>
</td>
<td>
<p>Optical connector</p>
</td>
</tr>
<tr>
<td>
<p>eConnTypeOtherDigital</p>
</td>
<td>
<p>Generic digital connector</p>
</td>
</tr>
<tr>
<td>
<p>eConnTypeOtherAnalog</p>
</td>
<td>
<p>Generic analog connector</p>
</td>
</tr>
<tr>
<td>
<p>eConnTypeMultichannelAnalogDIN</p>
</td>
<td>
<p>Multichannel analog DIN connector</p>
</td>
</tr>
<tr>
<td>
<p>eConnTypeXlrProfessional</p>
</td>
<td>
<p>XLR connector</p>
</td>
</tr>
<tr>
<td>
<p>eConnTypeRJ11Modem</p>
</td>
<td>
<p>RJ11 modem connector</p>
</td>
</tr>
<tr>
<td>
<p>eConnTypeCombination</p>
</td>
<td>
<p>Connector combination</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>GeoLocation</b>

<dd>
<p>The geometric location of the jack. The value of this member is one of the <b>EPcxGeoLocation</b> enumeration values shown in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Geometric location</th>
</tr>
<tr>
<td>
<p>eGeoLocRear</p>
</td>
<td>
<p>Rear</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocFront</p>
</td>
<td>
<p>Front</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocLeft</p>
</td>
<td>
<p>Left</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocRight</p>
</td>
<td>
<p>Right</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocTop</p>
</td>
<td>
<p>Top</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocBottom</p>
</td>
<td>
<p>Bottom</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocRearPanel</p>
</td>
<td>
<p>Rear slide-open or pull-open panel</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocRiser</p>
</td>
<td>
<p>Riser card</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocInsideMobileLid</p>
</td>
<td>
<p>Inside lid of mobile computer</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocDrivebay</p>
</td>
<td>
<p>Drive bay</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocHDMI</p>
</td>
<td>
<p>HDMI connector</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocOutsideMobileLid</p>
</td>
<td>
<p>Outside lid of mobile computer</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocATAPI</p>
</td>
<td>
<p>ATAPI connector</p>
</td>
</tr>
<tr>
<td>
<p>eGeoLocNotApplicable</p>
</td>
<td>
<p>Not applicable. See <b>Remarks</b> section.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>GenLocation</b>

<dd>
<p>Specifies the general location of the jack. The value of this member is one of the <b>EPcxGenLocation</b> enumeration values shown in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>General location</th>
</tr>
<tr>
<td>
<p>eGenLocPrimaryBox</p>
</td>
<td>
<p>On primary chassis</p>
</td>
</tr>
<tr>
<td>
<p>eGenLocInternal</p>
</td>
<td>
<p>Inside primary chassis</p>
</td>
</tr>
<tr>
<td>
<p>eGenLocSeparate</p>
</td>
<td>
<p>On separate chassis</p>
</td>
</tr>
<tr>
<td>
<p>eGenLocOther</p>
</td>
<td>
<p>Other location</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PortConnection</b>

<dd>
<p>Specifies the type of port represented by the jack. The value of this member is one of the <b>EPxcPortConnection</b> enumeration values shown in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Port connection type</th>
</tr>
<tr>
<td>
<p>ePortConnJack</p>
</td>
<td>
<p>Jack</p>
</td>
</tr>
<tr>
<td>
<p>ePortConnIntegratedDevice</p>
</td>
<td>
<p>Slot for an integrated device</p>
</td>
</tr>
<tr>
<td>
<p>ePortConnBothIntegratedAndJack</p>
</td>
<td>
<p>Both a jack and a slot for an integrated device</p>
</td>
</tr>
<tr>
<td>
<p>ePortConnUnknown</p>
</td>
<td>
<p>Unknown</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>IsConnected</b>

<dd>
<p>Indicates whether there is an external device connected to the jack. If the audio controller supports jack detection on this pin, the value of <b>IsConnected</b> should accurately indicate whether the jack is occupied by a plug at any given time. This value should always be set to <b>TRUE</b> for devices that do not support jack detection.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537364">KSPROPERTY_JACK_DESCRIPTION</a> property in Windows Vista and later. It describes an audio jack that is part of a connection between an endpoint device and a hardware device in an audio adapter. When a user needs to plug an endpoint device into a jack or unplug it from a jack, an audio application can use the descriptive information in the structure to help the user to find the jack.</p>

<p>When an audio device does not expose a physically accessible jack, the audio device uses the <b>eGeoLocNotApplicable</b> value to indicate to Windows and Windows-based apps that there is no physical jack. As such, there is no geometric location either. For example, the audio device can be integrated into the motherboard, without any accessible jacks.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537364">KSPROPERTY_JACK_DESCRIPTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20KSJACK_DESCRIPTION structure%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
