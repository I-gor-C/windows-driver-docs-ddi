---
UID: NN.sensorsclassextension.ISensorClassExtension~r1
title: ISensorClassExtension
author: windows-driver-content
description: The ISensorClassExtension interface provides methods that the sensor driver uses to communicate with the sensor platform (and, therefore, client applications) through the sensor class extension object.
old-location: sensors\isensorclassextension.htm
old-project: sensors
ms.assetid: db455be3-3aec-47c4-81a8-992aa4926138
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: __MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0002, SensorConnectionType
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
req.alt-api: ISensorClassExtension
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
req.product: Windows 10 or later.
---

# ISensorClassExtension interface



## -description
The ISensorClassExtension interface provides methods that the sensor driver uses to communicate with the sensor platform (and, therefore, client applications) through the sensor class extension object.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">ISensorClassExtension</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>ISensorClassExtension</b> also has these types of members:

The <b>ISensorClassExtension</b> interface has these methods.

 


## -members
The <b>ISensorClassExtension</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensorclassextension_cleanupfile">ISensorClassExtension::CleanupFile</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensorclassextension_initialize">ISensorClassExtension::Initialize</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensorclassextension_postevent">ISensorClassExtension::PostEvent</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensorclassextension_poststatechange">ISensorClassExtension::PostStateChange</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensorclassextension_processiocontrol">ISensorClassExtension::ProcessIoControl</a>
</td>
<td align="left" width="63%"></td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="sensors.isensorclassextension_uninitialize">ISensorClassExtension::Uninitialize</a>
</td>
<td align="left" width="63%"></td>
</tr>
</table> 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Sensorsclassextension.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>SensorsClassExtension.lib</dt>
</dl>
</td>
</tr>
</table>