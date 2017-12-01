---
UID: NE.nfcsedev._SECURE_ELEMENT_EVENT_TYPE
title: SECURE_ELEMENT_EVENT_TYPE
author: windows-driver-content
description: Indicates the type of secure element events.
old-location: nfpdrivers\_secure_element_event_type.htm
old-project: nfpdrivers
ms.assetid: 45DCE635-6F28-4BE1-8362-568409FA8B1B
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: NFCRM_SET_RADIO_STATE, NFCRM_SET_RADIO_STATE, *PNFCRM_SET_RADIO_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: nfcsedev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SECURE_ELEMENT_EVENT_TYPE
req.alt-loc: nfcsedev.h
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

# SECURE_ELEMENT_EVENT_TYPE enumeration



## -description
<p>Indicates the type of secure element events.</p>


## -syntax

````
typedef enum _SECURE_ELEMENT_EVENT_TYPE { 
  ExternalReaderArrival    = 0,
  ExternalReaderDeparture  = 1,
  ApplicationSelected      = 2,
  Transaction              = 3,
  HceActivated             = 4,
  HceDeactivated           = 5
} SECURE_ELEMENT_EVENT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="ExternalReaderArrival"></a><a id="externalreaderarrival"></a><a id="EXTERNALREADERARRIVAL"></a><b>ExternalReaderArrival</b>

<dd>
<p>This event is fired when an external reader has established a connection with the indicated secure element. No other parameters are given for this event.</p>
</dd>

### -field <a id="ExternalReaderDeparture"></a><a id="externalreaderdeparture"></a><a id="EXTERNALREADERDEPARTURE"></a><b>ExternalReaderDeparture</b>

<dd>
<p>This event is fired when an external reader has terminated a connection with the indicated secure element. No other parameters are given for this event.</p>
</dd>

### -field <a id="ApplicationSelected"></a><a id="applicationselected"></a><a id="APPLICATIONSELECTED"></a><b>ApplicationSelected</b>

<dd>
<p>This event is fired when the external reader has issued a “SELECT” command to select an application on the specified secure element. Additionally, the event notification includes the application ID (AID) of the selected application. Not all types of secure elements support the ability to raise this event.</p>
</dd>

### -field <a id="Transaction"></a><a id="transaction"></a><a id="TRANSACTION"></a><b>Transaction</b>

<dd>
<p>This event is fired when an application that is operating within the secure element notifies the controller that some form of action has occurred. This event sends a list of parameters that is coded in BER-TLV fields. This event is mapped to EVT_TRANSACTION.</p>
</dd>

### -field <a id="HceActivated"></a><a id="hceactivated"></a><a id="HCEACTIVATED"></a><b>HceActivated</b>

<dd>
<p>This event is fired when a listen mode interface is activated to the device host. This event sends the current connection ID, activated RF protocol, and technology.</p>
</dd>

### -field <a id="HceDeactivated"></a><a id="hcedeactivated"></a><a id="HCEDEACTIVATED"></a><b>HceDeactivated</b>

<dd>
<p>This event is fired when a current active HCE session is terminated. This event sends the currently terminated connection ID.</p>
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
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>