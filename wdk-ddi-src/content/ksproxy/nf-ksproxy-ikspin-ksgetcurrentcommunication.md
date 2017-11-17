---
UID: NF.ksproxy.IKsPin.KsGetCurrentCommunication
title: IKsPin::KsGetCurrentCommunication
author: windows-driver-content
description: The KsGetCurrentCommunication method retrieves the current communication direction, interface, and medium of a pin.
old-location: stream\ikspin_ksgetcurrentcommunication.htm
ms.assetid: 3fca9bf5-5430-4877-846e-e796e54991a2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsPin.KsGetCurrentCommunication
req.alt-loc: ksproxy.h
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
ms.keywords: IKsPin, KsGetCurrentCommunication, IKsPin::KsGetCurrentCommunication
req.iface: IKsPin
---

# IKsPin::KsGetCurrentCommunication method



## -description
<p>The <b>KsGetCurrentCommunication</b> method retrieves the current communication direction, interface, and medium of a pin. </p>


## -syntax

````
HRESULT KsGetCurrentCommunication(
  [out, optional] KSPIN_COMMUNICATION *Communication,
  [out, optional] KSPIN_INTERFACE     *Interface,
  [out, optional] KSPIN_MEDIUM        *Medium
);
````


## -parameters
<dl>

### -param <i>Communication</i> [out, optional]

<dd>
<p>Pointer to a variable that receives one of the following values from the KSPIN_COMMUNICATION enumerated type describing the current communication direction for a pin: </p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>KSPIN_COMMUNICATION_NONE</p>
</td>
<td>
<p>The pin factory does not create any pin instances.</p>
</td>
</tr>
<tr>
<td>
<p>KSPIN_COMMUNICATION_SINK</p>
</td>
<td>
<p>The pin factory creates instances of IRP sink pins. Such pins can only be connected to IRP source pins.</p>
</td>
</tr>
<tr>
<td>
<p>KSPIN_COMMUNICATION_SOURCE</p>
</td>
<td>
<p>The pin factory creates instances of IRP source pins. Such pins can only be connected to IRP sink pins.</p>
</td>
</tr>
<tr>
<td>
<p>KSPIN_COMMUNICATION_BOTH</p>
</td>
<td>
<p>The pin factory creates instances of pins that are both IRP sinks and IRP sources. </p>
</td>
</tr>
<tr>
<td>
<p>KSPIN_COMMUNICATION_BRIDGE</p>
</td>
<td>
<p>The pin cannot connect to other pins, but instances may be created on it to receive non-KS I/O requests.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Interface</i> [out, optional]

<dd>
<p>Pointer to a variable that receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563537">KSPIN_INTERFACE</a> structure that describes the current interface for a pin. </p>
</dd>

### -param <i>Medium</i> [out, optional]

<dd>
<p>Pointer to a variable that receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a> structure that describes the current medium for a pin. </p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>Source pins send IRPs to sink pins. Do not confuse the communication direction with data flow direction. (See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565197">KSPROPERTY_PIN_DATAFLOW</a>.) A source pin may read or write data, and a sink pin may have data read to it or written from it.</p>

<p>The current communication direction, interface, and medium of a pin are a subset of those available to the pin, and are selected when the pin handle is created.</p>

<p>Source pins send IRPs to sink pins. Do not confuse the communication direction with data flow direction. (See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565197">KSPROPERTY_PIN_DATAFLOW</a>.) A source pin may read or write data, and a sink pin may have data read to it or written from it.</p>

<p>The current communication direction, interface, and medium of a pin are a subset of those available to the pin, and are selected when the pin handle is created.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563537">KSPIN_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565197">KSPROPERTY_PIN_DATAFLOW</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPin::KsGetCurrentCommunication method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
