---
UID: NS:gnssdriver.GNSS_SUPL_NI_INFO
title: GNSS_SUPL_NI_INFO
author: windows-driver-content
description: This structure contains the requested SUPL NI information.
old-location: gnss\gnss_supl_ni_info.htm
old-project: gnss
ms.assetid: 78D19A0C-E247-4DDA-A689-494B5A61A673
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PGNSS_SUPL_NI_INFO, GNSS_SUPL_NI_INFO, GNSS_SUPL_NI_INFO structure [Sensor Devices], PGNSS_SUPL_NI_INFO, PGNSS_SUPL_NI_INFO structure pointer [Sensor Devices], gnss.gnss_supl_ni_info, gnssdriver/GNSS_SUPL_NI_INFO, gnssdriver/PGNSS_SUPL_NI_INFO"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	gnssdriver.h
api_name:
-	GNSS_SUPL_NI_INFO
product: Windows
targetos: Windows
req.typenames: GNSS_SUPL_NI_INFO, *PGNSS_SUPL_NI_INFO
---

# GNSS_SUPL_NI_INFO structure
This structure contains the requested SUPL NI information.

## Syntax
````
typedef struct {
  ULONG Size;
  ULONG Version;
  WCHAR RequestorId[MAX_PATH];
  WCHAR ClientName[MAX_PATH];
  CHAR  SuplNiUrl[MAX_SERVER_URL_NAME];
} GNSS_SUPL_NI_INFO, *PGNSS_SUPL_NI_INFO;
````

## Members


`ClientName`



`RequestorId`



`Size`

Structure size.

`SuplNiUrl`



`Version`

Version number.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |