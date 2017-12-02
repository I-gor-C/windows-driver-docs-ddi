---
UID: NN.sensorsclassextension.ISensorDriver~r1
title: ISensorDriver
author: windows-driver-content
description: The ISensorDriver interface provides callback methods that the sensor class extension uses to provide requests and notifications to the sensor driver.
old-location: sensors\isensordriver.htm
old-project: sensors
ms.assetid: 4f468f1e-598e-46ae-b50e-28f73e73afda
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: ISensorDriver, OnSetProperties, ISensorDriver::OnSetProperties
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: sensorsclassextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISensorDriver
req.alt-loc: SensorsClassExtension.lib,SensorsClassExtension.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: SensorsClassExtension.lib
req.dll: 
req.irql: <= PASSIVE_LEVEL
req.iface: ISensorDriver
req.product: Windows 10 or later.
---

# ISensorDriver interface



## -description
<p>
<p>The ISensorDriver interface provides callback methods that the sensor class extension uses to provide requests and notifications to the sensor driver.</p>
</p>
<p>The ISensorDriver interface provides callback methods that the sensor class extension uses to provide requests and notifications to the sensor driver.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">ISensorDriver</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>ISensorDriver</b> also has these types of members:</p>

<p>The <b>ISensorDriver</b> interface has these methods.</p>

<p> </p>

## -members
<p>The <b>ISensorDriver</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_onclientconnect">ISensorDriver::OnClientConnect</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_onclientdisconnect">ISensorDriver::OnClientDisconnect</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_onclientsubscribetoevents">ISensorDriver::OnClientSubscribeToEvents</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_onclientunsubscribefromevents">ISensorDriver::OnClientUnsubscribeFromEvents</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_ongetdatafields">ISensorDriver::OnGetDataFields</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_ongetproperties">ISensorDriver::OnGetProperties</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_ongetsupporteddatafields">ISensorDriver::OnGetSupportedDataFields</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_ongetsupportedevents">ISensorDriver::OnGetSupportedEvents</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_ongetsupportedproperties">ISensorDriver::OnGetSupportedProperties</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_ongetsupportedsensorobjects">ISensorDriver::OnGetSupportedSensorObjects</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_onprocesswpdmessage">ISensorDriver::OnProcessWpdMessage</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensordriver_onsetproperties">ISensorDriver::OnSetProperties</a>
</td>
<td align="left" width="63%"></td>
</tr>
</table><p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sensorsclassextension.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>SensorsClassExtension.lib</dt>
</dl>
</td>
</tr>
</table>