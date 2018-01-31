---
UID : NS:gnssdriver.GNSS_AGNSS_REQUEST_PARAM
title : GNSS_AGNSS_REQUEST_PARAM
author : windows-driver-content
description : This structure defines AGNSS request parameters.
old-location : sensors\gnss_agnss_request_param.htm
old-project : sensors
ms.assetid : 67A1DAEF-13D3-4D47-B10C-0CA30C8EB22F
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : gnssdriver/GNSS_AGNSS_REQUEST_PARAM, *PGNSS_AGNSS_REQUEST_PARAM, sensors.gnss_agnss_request_param, PGNSS_AGNSS_REQUEST_PARAM, gnssdriver/PGNSS_AGNSS_REQUEST_PARAM, GNSS_AGNSS_REQUEST_PARAM structure [Sensor Devices], GNSS_AGNSS_REQUEST_PARAM, PGNSS_AGNSS_REQUEST_PARAM structure pointer [Sensor Devices]
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
req.typenames : "*PGNSS_AGNSS_REQUEST_PARAM, GNSS_AGNSS_REQUEST_PARAM"
---

# GNSS_AGNSS_REQUEST_PARAM structure
This structure defines AGNSS request parameters.

## Syntax
````
typedef struct {
  ULONG                   Size;
  ULONG                   Version;
  GNSS_AGNSS_REQUEST_TYPE RequestType;
  ULONG                   BlobFormat;
} GNSS_AGNSS_REQUEST_PARAM, *PGNSS_AGNSS_REQUEST_PARAM;
````

## Members


`BlobFormat`

If the RequestType is GNSS_AGNSS_BlobInjection, this contains the required  blob format.

`RequestType`

Specifies the type of the request (for example, time injection, blob injection).

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