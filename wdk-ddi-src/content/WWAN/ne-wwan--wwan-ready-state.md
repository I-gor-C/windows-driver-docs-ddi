---
UID: NE.wwan._WWAN_READY_STATE
title: WWAN_READY_STATE
author: windows-driver-content
description: The WWAN_READY_STATE enumeration lists the different device ready-states that are supported by the MB device.
old-location: netvista\wwan_ready_state.htm
ms.assetid: 46fec377-ba2c-469a-96be-23aa07079f8c
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_READY_STATE
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
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_READY_STATE enumeration



## -description
<p>The WWAN_READY_STATE enumeration lists the different device ready-states that are supported by the MB
  device.</p>


## -syntax

````
typedef enum _WWAN_READY_STATE { 
  WwanReadyStateOff             = 0,
  WwanReadyStateInitialized,
  WwanReadyStateSimNotInserted,
  WwanReadyStateBadSim,
  WwanReadyStateFailure,
  WwanReadyStateNotActivated,
  WwanReadyStateDeviceLocked
} WWAN_READY_STATE, *PWWAN_READY_STATE;
````


## -enum-fields
<dl>

### -field <a id="WwanReadyStateOff"></a><a id="wwanreadystateoff"></a><a id="WWANREADYSTATEOFF"></a><b>WwanReadyStateOff</b>

<dd>
<p>The device firmware stack is OFF or has not yet completed its initialization.</p>
</dd>

### -field <a id="WwanReadyStateInitialized"></a><a id="wwanreadystateinitialized"></a><a id="WWANREADYSTATEINITIALIZED"></a><b>WwanReadyStateInitialized</b>

<dd>
<p>The device is ready to turn on and register with the provider.</p>
</dd>

### -field <a id="WwanReadyStateSimNotInserted"></a><a id="wwanreadystatesimnotinserted"></a><a id="WWANREADYSTATESIMNOTINSERTED"></a><b>WwanReadyStateSimNotInserted</b>

<dd>
<p>The SIM card is not inserted into the device.</p>
</dd>

### -field <a id="WwanReadyStateBadSim"></a><a id="wwanreadystatebadsim"></a><a id="WWANREADYSTATEBADSIM"></a><b>WwanReadyStateBadSim</b>

<dd>
<p>The SIM card inserted into the device is invalid.</p>
</dd>

### -field <a id="WwanReadyStateFailure"></a><a id="wwanreadystatefailure"></a><a id="WWANREADYSTATEFAILURE"></a><b>WwanReadyStateFailure</b>

<dd>
<p>A general device failure has occurred.</p>
</dd>

### -field <a id="WwanReadyStateNotActivated"></a><a id="wwanreadystatenotactivated"></a><a id="WWANREADYSTATENOTACTIVATED"></a><b>WwanReadyStateNotActivated</b>

<dd>
<p>The subscription is not activated.</p>
</dd>

### -field <a id="WwanReadyStateDeviceLocked"></a><a id="wwanreadystatedevicelocked"></a><a id="WWANREADYSTATEDEVICELOCKED"></a><b>WwanReadyStateDeviceLocked</b>

<dd>
<p>The device is locked and requires PIN1 or PUK1 to unlock.
     </p>
<p>Note that if a device is locked because it requires a PIN type other than PIN1 or PUK1 (for example,
     a network personalization PIN), miniport drivers should report 
     <b>WwanReadyStateInitialized</b>. Though miniport drivers should return WWAN_STATUS_PIN_REQUIRED for OID
     requests which are blocked because of PIN. Subsequent OID_WWAN_PIN 
     <i>query</i> requests should return the PIN type needed to unlock the device.</p>
</dd>
</dl>

## -remarks
<p>For devices that use a SIM card, this enumeration indicates if the SIM card has been initialized and
    is ready for access.</p>

<p>For devices that use a SIM card, this enumeration indicates if the SIM card has been initialized and
    is ready for access.</p>

<p>For devices that use a SIM card, this enumeration indicates if the SIM card has been initialized and
    is ready for access.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571226">WWAN_READY_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_READY_STATE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
