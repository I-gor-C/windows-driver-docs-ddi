---
UID : NS:gnssdriver.GNSS_AGNSS_INJECTPOSITION
title : GNSS_AGNSS_INJECTPOSITION
author : windows-driver-content
description : This structure defines the format for AGNSS position injection.
old-location : sensors\gnss_agnss_injectposition.htm
old-project : sensors
ms.assetid : 1FB73F94-F8F3-409F-8B34-3CD303512AD0
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : "*PGNSS_AGNSS_INJECTPOSITION, PGNSS_AGNSS_INJECTPOSITION, sensors.gnss_agnss_injectposition, GNSS_AGNSS_INJECTPOSITION structure [Sensor Devices], gnssdriver/PGNSS_AGNSS_INJECTPOSITION, GNSS_AGNSS_INJECTPOSITION, gnssdriver/GNSS_AGNSS_INJECTPOSITION, PGNSS_AGNSS_INJECTPOSITION structure pointer [Sensor Devices]"
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
req.typenames : "*PGNSS_AGNSS_INJECTPOSITION, GNSS_AGNSS_INJECTPOSITION"
---

# GNSS_AGNSS_INJECTPOSITION structure
This structure defines the format for AGNSS position injection.

## Syntax
````
typedef struct {
  ULONG                 Size;
  ULONG                 Version;
  ULONG                 Age;
  GNSS_FIXDATA_BASIC    BasicData;
  GNSS_FIXDATA_ACCURACY AccuracyData;
} GNSS_AGNSS_INJECTPOSITION, *PGNSS_AGNSS_INJECTPOSITION;
````

## Members


`AccuracyData`

Position accuracy.

`Age`

Indicates how long the position has been aged in seconds.

`BasicData`

Position data.

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