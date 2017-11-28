---
UID: NS.ksmedia.PKSPROPERTY_CROSSBAR_PININFO_S
title: PKSPROPERTY_CROSSBAR_PININFO_S
author: windows-driver-content
description: The KSPROPERTY_CROSSBAR_PININFO_S structure describes the crossbar pin information for a device.
old-location: stream\ksproperty_crossbar_pininfo_s.htm
old-project: stream
ms.assetid: 7ddef9cf-aa2f-4383-b37f-8c2f3e9c99d6
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSPROPERTY_CROSSBAR_PININFO_S, KSPROPERTY_CROSSBAR_PININFO_S, *PKSPROPERTY_CROSSBAR_PININFO_S
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
req.alt-api: KSPROPERTY_CROSSBAR_PININFO_S
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

# PKSPROPERTY_CROSSBAR_PININFO_S structure



## -description
<p>The KSPROPERTY_CROSSBAR_PININFO_S structure describes the crossbar pin information for a device.</p>


## -syntax

````
typedef struct {
  KSPROPERTY     Property;
  KSPIN_DATAFLOW Direction;
  ULONG          Index;
  ULONG          PinType;
  ULONG          RelatedPinIndex;
  KSPIN_MEDIUM   Medium;
} KSPROPERTY_CROSSBAR_PININFO_S, *PKSPROPERTY_CROSSBAR_PININFO_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>Direction</b>

<dd>
<p>Specifies the minidriver-provided direction of data flow for the pin specified in <b>Index</b>. This value can be either <b>KSPIN_DATAFLOW_IN</b> or KSPIN_DATAFLOW_OUT.</p>
</dd>

### -field <b>Index</b>

<dd>
<p>Specifies the zero-based index of the pin for which crossbar information is being queried. Input pins are queried separately from output pins.</p>
</dd>

### -field <b>PinType</b>

<dd>
<p>Specifies the minidriver-provided type of physical connector. This member must be set to one of the KS_PhysicalConnectorType enumerated values defined in <i>ksmedia.h</i>:</p>
<p>KS_PhysConn_Video_Tuner</p>
<p>KS_PhysConn_Video_Composite</p>
<p>KS_PhysConn_Video_Svideo</p>
<p>KS_PhysConn_Video_RGB</p>
<p>KS_PhysConn_Video_YRYBY</p>
<p>KS_PhysConn_Video_SerialDigital</p>
<p>KS_PhysConn_Video_ParallelDigital</p>
<p>KS_PhysConn_Video_SCSI</p>
<p>KS_PhysConn_Video_AUX</p>
<p>KS_PhysConn_Video_Video_1394</p>
<p>KS_PhysConn_Video_USB</p>
<p>KS_PhysConn_Video_VideoDecoder</p>
<p>KS_PhysConn_Video_VideoEncoder</p>
<p>KS_PhysConn_Video_SCART</p>
<p>KS_PhysConn_Audio_Tuner</p>
<p>KS_PhysConn_Audio_Line</p>
<p>KS_PhysConn_Audio_Misc</p>
<p>KS_PhysConn_Audio_AESDigital</p>
<p>KS_PhysConn_Audio_SPDIFDigital</p>
<p>KS_PhysConn_Audio_SCSI</p>
<p>KS_PhysConn_Audio_AUX</p>
<p>KS_PhysConn_Audio_1394</p>
<p>KS_PhysConn_Audio_USB</p>
<p>KS_PhysConn_Audio_AudioDecoder</p>
</dd>

### -field <b>RelatedPinIndex</b>

<dd>
<p>Specifies the optional pin index of a pin that is related to the pin specified in <b>Index</b>. For example, the minidriver can set the <b>RelatedPinIndex</b> to the pin index of the audio stream that goes with a video stream in <b>Index</b>. <b>RelatedPinIndex</b> applies only to pins of the same direction (input or output) as the pin being queried. If no other pins are related to the current pin, the minidriver should return (-1).</p>
</dd>

### -field <b>Medium</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a> structure that represents the hardware connection for the pin. This information is returned by the minidriver.</p>
</dd>
</dl>

## -remarks
<p>All index values are zero-based, and input pins are counted separately from output pins.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567804">PROPSETID_VIDCAP_CROSSBAR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565121">KSPROPERTY_CROSSBAR_PININFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_CROSSBAR_PININFO_S structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
