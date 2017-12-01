---
UID: NS.wwan._WWAN_RADIO_STATE
title: WWAN_RADIO_STATE
author: windows-driver-content
description: The WWAN_RADIO_STATE structure represents the hardware-based and software-based radio power states of the MB device.
old-location: netvista\wwan_radio_state.htm
old-project: netvista
ms.assetid: 15c02819-bae8-48f5-8782-97823b6907bd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WWAN_RADIO_STATE, WWAN_RADIO_STATE, *PWWAN_RADIO_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_RADIO_STATE
req.alt-loc: wwan.h
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
req.product: Windows 10 or later.
---

# WWAN_RADIO_STATE structure



## -description
<p>The WWAN_RADIO_STATE structure represents the hardware-based and software-based radio power states of
  the MB device.</p>


## -syntax

````
typedef struct _WWAN_RADIO_STATE {
  WWAN_RADIO HwRadioState;
  WWAN_RADIO SwRadioState;
} WWAN_RADIO_STATE, *PWWAN_RADIO_STATE;
````


## -struct-fields
<dl>

### -field <b>HwRadioState</b>

<dd>
<p>The hardware radio power state of the device. The MB Service cannot set this state because it is
     read-only. The following table shows the possible values for this member.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WwanRadioOff</p>
</td>
<td>
<p>The hardware radio is off.</p>
</td>
</tr>
<tr>
<td>
<p>WwanRadioOn</p>
</td>
<td>
<p>The hardware radio is on, or no switch exists to control power to the hardware radio.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>SwRadioState</b>

<dd>
<p>The software-based radio power state of the device. The MB Service can get and set this state. The
     following table shows the possible values for this member.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WwanRadioOff</p>
</td>
<td>
<p>The radio is turned off by Windows.</p>
</td>
</tr>
<tr>
<td>
<p>WwanRadioOn</p>
</td>
<td>
<p>The radio is turned on by Windows.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>Miniport drivers should continue the software-based radio power state across system restart or device
    removal and reinsertion. Miniport drivers should store the device software-based radio power state
    information and use it to set the device radio power state for each restart or reinsertion of the
    device.</p>

<p>The following table defines the relationship between hardware-based and software-based radio power
    state settings and their effective result.</p>

<p>WwanRadioOff</p>

<p>WwanRadioOn</p>

<p>The miniport driver should send all applicable status indications such as
    NDIS_STATUS_WWAN_CONTEXT_STATE, NDIS_STATUS_WWAN_PACKET_SERVICE, and NDIS_STATUS_WWAN_REGISTER_STATE
    whenever the effective radio state changes from 
    <b>WwanRadioOn</b> to 
    <b>WwanRadioOff</b> or from 
    <b>WwanRadioOff</b> to 
    <b>WwanRadioOn</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wwan\ne-wwan--wwan-radio.md">WWAN_RADIO</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-radio-state.md">NDIS_WWAN_RADIO_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_RADIO_STATE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
