---
UID: NE:gnssdriver.GNSS_NI_REQUEST_TYPE
title: GNSS_NI_REQUEST_TYPE
author: windows-driver-content
description: This enumeration indicates the network initiated (NI) request type represented by the GNSS_NI_REQUEST_PARAM structure.
old-location: sensors\gnss_ni_request_type.htm
old-project: sensors
ms.assetid: 79AFC7D8-5A51-49CC-8ADA-7D21C6859254
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: gnssdriver/GNSS_NI_Request_AreaTrigger, GNSS_NI_REQUEST_TYPE enumeration [Sensor Devices], sensors.gnss_ni_request_type, gnssdriver/GNSS_NI_REQUEST_TYPE, GNSS_NI_Request_AreaTrigger, gnssdriver/GNSS_NI_Request_SingleShot, GNSS_NI_Request_SingleShot, GNSS_NI_REQUEST_TYPE
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	gnssdriver.h
apiname:
-	GNSS_NI_REQUEST_TYPE
product: Windows
targetos: Windows
req.typenames: GNSS_NI_REQUEST_TYPE
---

# GNSS_NI_REQUEST_TYPE Enumeration
This enumeration indicates the network initiated (NI) request type represented by the <a href="..\gnssdriver\ns-gnssdriver-gnss_ni_request_param.md">GNSS_NI_REQUEST_PARAM</a> structure.

## Syntax
````
typedef enum  { 
  GNSS_NI_Request_SingleShot   = 0x01,
  GNSS_NI_Request_AreaTrigger  = 0x02
} GNSS_NI_REQUEST_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>GNSS_NI_Request_AreaTrigger</td>
                    <td>Indicates the request type is tracking.</td>
                </tr>
            
                <tr>
                    <td>GNSS_NI_Request_SingleShot</td>
                    <td>Indicates the request type is single shot.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |