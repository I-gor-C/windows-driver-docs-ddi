---
UID : NS:gnssdriver.GNSS_CP_NI_INFO
title : GNSS_CP_NI_INFO
author : windows-driver-content
description : This structure contains CP NI information.
old-location : sensors\gnss_cp_ni_info.htm
old-project : sensors
ms.assetid : FC05C59C-F8B5-4573-A1F0-722A25BDA151
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : sensors.gnss_cp_ni_info, GNSS_CP_NI_INFO structure [Sensor Devices], GNSS_CP_NI_INFO, PGNSS_CP_NI_INFO, gnssdriver/PGNSS_CP_NI_INFO, gnssdriver/GNSS_CP_NI_INFO, *PGNSS_CP_NI_INFO, PGNSS_CP_NI_INFO structure pointer [Sensor Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : gnssdriver.h
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
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PGNSS_CP_NI_INFO, GNSS_CP_NI_INFO"
---

# GNSS_CP_NI_INFO structure
This structure contains CP NI information.

## Syntax
````
typedef struct {
  ULONG Size;
  ULONG Version;
  WCHAR RequestorId[MAX_PATH];
  WCHAR NotificationText[MAX_PATH];
} GNSS_CP_NI_INFO, *PGNSS_CP_NI_INFO;
````

## Members


`NotificationText`



`RequestorId`



`Size`

Structure size.

`Version`

Version number.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | gnssdriver.h |