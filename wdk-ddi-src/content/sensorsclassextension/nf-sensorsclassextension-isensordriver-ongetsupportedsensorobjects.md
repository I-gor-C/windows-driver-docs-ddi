---
UID : NF:sensorsclassextension.ISensorDriver.OnGetSupportedSensorObjects
title : ISensorDriver::OnGetSupportedSensorObjects method
author : windows-driver-content
description : The ISensorDriver::OnGetSupportedSensorObjects method retrieves the list of sensors that the driver provides.
old-location : sensors\isensordriver_ongetsupportedsensorobjects.htm
old-project : sensors
ms.assetid : a8ea63cf-24ba-467b-9c27-ab8e38be1c04
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : ISensorDriver::OnGetSupportedSensorObjects, ISensorDriver, sensors.isensordriver_ongetsupportedsensorobjects, OnGetSupportedSensorObjects, OnGetSupportedSensorObjects method [Sensor Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : sensorsclassextension.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : SensorsClassExtension.lib
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : SensorConnectionType
req.product : Windows 10 or later.
---


# OnGetSupportedSensorObjects method
The <a href="https://msdn.microsoft.com/library/windows/hardware/ff545633">ISensorDriver::OnGetSupportedSensorObjects</a> method retrieves the list of sensors that the driver provides.

## Syntax

````
HRESULT OnGetSupportedSensorObjects(
   IPortableDeviceValuesCollection ** ppSensorObjectCollection
);
````

## Parameters

`ppSensorObjectCollection`

Address of an IPortableDeviceValuesCollection pointer that receives the list of sensors.


## Return Value

If the operation succeeds, this method returns S_OK. Otherwise, this method returns one of the error codes that are defined in Winerror.h.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | sensorsclassextension.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |