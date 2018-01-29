---
UID : NS:gnssdriver.GNSS_SUPL_HSLP_CONFIG
title : GNSS_SUPL_HSLP_CONFIG
author : windows-driver-content
description : This structure contains SUPL H-SLP configuration information.
old-location : sensors\gnss_supl_hslp_config.htm
old-project : sensors
ms.assetid : 08CCC4A8-2D85-436D-B18E-77C91A24F59C
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : GNSS_SUPL_HSLP_CONFIG structure [Sensor Devices], gnssdriver/PGNSS_SUPL_HSLP_CONFIG, PGNSS_SUPL_HSLP_CONFIG structure pointer [Sensor Devices], sensors.gnss_supl_hslp_config, gnssdriver/GNSS_SUPL_HSLP_CONFIG, *PGNSS_SUPL_HSLP_CONFIG, PGNSS_SUPL_HSLP_CONFIG, GNSS_SUPL_HSLP_CONFIG
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
req.typenames : "*PGNSS_SUPL_HSLP_CONFIG, GNSS_SUPL_HSLP_CONFIG"
---

# GNSS_SUPL_HSLP_CONFIG structure
This structure contains SUPL H-SLP configuration information.

## Syntax
````
typedef struct {
  ULONG Size;
  ULONG Version;
  WCHAR SuplHslp[MAX_SERVER_URL_NAME];
  WCHAR SuplHslpFromImsi[MAX_SERVER_URL_NAME];
  ULONG Reserved;
  BYTE  Unused[512];
} GNSS_SUPL_HSLP_CONFIG, *PGNSS_SUPL_HSLP_CONFIG;
````

## Members


`Reserved`

Reserved for future use.

`Size`

Structure size.

`SuplHslp`



`SuplHslpFromImsi`



`Unused`



`Version`

Version number.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | gnssdriver.h |