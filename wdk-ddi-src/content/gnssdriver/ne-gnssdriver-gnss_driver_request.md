---
UID: NE:gnssdriver.GNSS_DRIVER_REQUEST
title: GNSS_DRIVER_REQUEST
author: windows-driver-content
description: GNSS_DRIVER_REQUEST enumerates the GNSS driver data request types.
old-location: sensors\gnss_driver_request.htm
old-project: sensors
ms.assetid: 923774E0-4F4E-470A-9793-8AD4261AEB64
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: GNSS_DRIVER_REQUEST, GNSS_DRIVER_REQUEST enumeration [Sensor Devices], SUPL_CONFIG_DATA, gnssdriver/GNSS_DRIVER_REQUEST, gnssdriver/SUPL_CONFIG_DATA, sensors.gnss_driver_request
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: gnssdriver.h
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
req.lib: 
req.dll: 
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	gnssdriver.h
api_name:
-	GNSS_DRIVER_REQUEST
product:
- Windows
targetos: Windows
req.typenames: GNSS_DRIVER_REQUEST
---

# GNSS_DRIVER_REQUEST Enumeration
GNSS_DRIVER_REQUEST enumerates  the GNSS driver data request types.

## Syntax
```
typedef enum GNSS_DRIVER_REQUEST {
  SUPL_CONFIG_DATA
} ;
```

## Constants

<table>
            
                <tr>
                    <td>SUPL_CONFIG_DATA</td>
                    <td>This is used by the GNSS driver to  request SUPL configuration data.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |