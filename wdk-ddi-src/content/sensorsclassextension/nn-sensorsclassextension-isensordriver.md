---
UID: NN:sensorsclassextension.ISensorDriver
title: ISensorDriver
author: windows-driver-content
description: The ISensorDriver interface provides callback methods that the sensor class extension uses to provide requests and notifications to the sensor driver.
old-location: sensors\isensordriver.htm
old-project: sensors
ms.assetid: 4f468f1e-598e-46ae-b50e-28f73e73afda
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: sensors.isensordriver, ISensorDriver interface [Sensor Devices], ISensorDriver interface [Sensor Devices], described, ISensorDriver, sensorsclassextension/ISensorDriver, Sensor_IFaces_014342f2-5466-426b-bb11-cb4e89a7691a.xml
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: SensorsClassExtension.lib
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	SensorsClassExtension.lib
-	SensorsClassExtension.dll
apiname:
-	ISensorDriver
product: Windows
targetos: Windows
req.typenames: SensorConnectionType
req.product: Windows 10 or later.
---

# ISensorDriver interface

The ISensorDriver interface provides callback methods that the sensor class extension uses to provide requests and notifications to the sensor driver.

## Methods

<p>The <b>ISensorDriver</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [sensorsclassextension.ISensorDriver.OnClientConnect](nf-sensorsclassextension-isensordriver-onclientconnect.md) | The ISensorDriver::OnClientConnect method notifies the sensor driver that a client application has connected. |
| [sensorsclassextension.ISensorDriver.OnClientDisconnect](nf-sensorsclassextension-isensordriver-onclientdisconnect.md) | The ISensorDriver::OnClientDisconnect method notifies the sensor driver that a client application has disconnected. |
| [sensorsclassextension.ISensorDriver.OnClientSubscribeToEvents](nf-sensorsclassextension-isensordriver-onclientsubscribetoevents.md) | The ISensorDriver::OnClientSubscribeToEvents method notifies the sensor driver that an authorized client application is requesting event notifications. |
| [sensorsclassextension.ISensorDriver.OnClientUnsubscribeFromEvents](nf-sensorsclassextension-isensordriver-onclientunsubscribefromevents.md) | The ISensorDriver::OnClientUnsubscribeFromEvents method notifies the sensor driver that a client application no longer requests event notifications. |
| [sensorsclassextension.ISensorDriver.OnGetDataFields](nf-sensorsclassextension-isensordriver-ongetdatafields.md) | The ISensorDriver::OnGetDataFields method retrieves current sensor data. |
| [sensorsclassextension.ISensorDriver.OnGetProperties](nf-sensorsclassextension-isensordriver-ongetproperties.md) | The ISensorDriver::OnGetProperties method retrieves values for the specified properties from the specified sensor. |
| [sensorsclassextension.ISensorDriver.OnGetSupportedDataFields](nf-sensorsclassextension-isensordriver-ongetsupporteddatafields.md) | The ISensorDriver::OnGetSupportedDataFields method retrieves the list of data fields that the specified sensor can provide. |
| [sensorsclassextension.ISensorDriver.OnGetSupportedEvents](nf-sensorsclassextension-isensordriver-ongetsupportedevents.md) | The ISensorDriver::OnGetSupportedEvents method retrieves the list of events that the specified sensor can raise. |
| [sensorsclassextension.ISensorDriver.OnGetSupportedProperties](nf-sensorsclassextension-isensordriver-ongetsupportedproperties.md) | The ISensorDriver::OnGetSupportedProperties method retrieves the list of properties that the specified sensor provides. |
| [sensorsclassextension.ISensorDriver.OnGetSupportedSensorObjects](nf-sensorsclassextension-isensordriver-ongetsupportedsensorobjects.md) | The ISensorDriver::OnGetSupportedSensorObjects method retrieves the list of sensors that the driver provides. |
| [sensorsclassextension.ISensorDriver.OnProcessWpdMessage](nf-sensorsclassextension-isensordriver-onprocesswpdmessage.md) | The ISensorDriver::OnProcessWpdMessage method handles Windows Portable Device (WPD) commands that the ISensorClassExtension::ProcessIoControl method does not handle internally. |
| [sensorsclassextension.ISensorDriver.OnSetProperties](nf-sensorsclassextension-isensordriver-onsetproperties.md) | The ISensorDriver::OnSetProperties method specifies values for the specified list of properties. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | sensorsclassextension.h |