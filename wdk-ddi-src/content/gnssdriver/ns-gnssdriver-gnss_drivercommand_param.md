---
UID: NS:gnssdriver.GNSS_DRIVERCOMMAND_PARAM
title: GNSS_DRIVERCOMMAND_PARAM
author: windows-driver-content
description: This structure is used to send a command to the GNSS driver.
old-location: sensors\gnss_drivercommand_param.htm
old-project: sensors
ms.assetid: EC6EDD7A-B57F-4350-9EB9-56721EAC19BD
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: "*PGNSS_DRIVERCOMMAND_PARAM, GNSS_DRIVERCOMMAND_PARAM, GNSS_DRIVERCOMMAND_PARAM structure [Sensor Devices], PGNSS_DRIVERCOMMAND_PARAM, PGNSS_DRIVERCOMMAND_PARAM structure pointer [Sensor Devices], gnssdriver/GNSS_DRIVERCOMMAND_PARAM, gnssdriver/PGNSS_DRIVERCOMMAND_PARAM, sensors.gnss_drivercommand_param"
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
-	GNSS_DRIVERCOMMAND_PARAM
product: Windows
targetos: Windows
req.typenames: GNSS_DRIVERCOMMAND_PARAM, *PGNSS_DRIVERCOMMAND_PARAM
---

# GNSS_DRIVERCOMMAND_PARAM structure
This structure is used to send a command to the GNSS driver.

The command may involve configuring certain parameters and state variables of the underlying GNSS driver or device, or executing certain defined actions through the driver.

## Syntax
```
typedef struct GNSS_DRIVERCOMMAND_PARAM {
  ULONG                   Size;
  ULONG                   Version;
  GNSS_DRIVERCOMMAND_TYPE CommandType;
  ULONG                   Reserved;
  ULONG                   CommandDataSize;
  BYTE                    Unused[512];
  BYTE                    CommandData[ANYSIZE_ARRAY];
} *PGNSS_DRIVERCOMMAND_PARAM, GNSS_DRIVERCOMMAND_PARAM;
```

## Members


`Size`

Structure size.

`Version`

Version number.

`CommandType`

Identifies the specific command that the driver is required to execute.

This is a well-defined list of GNSS driver commands, as defined by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925109">GNSS_DRIVERCOMMAND_TYPE</a> enumeration.

`Reserved`



`CommandDataSize`

Size of the configuration data being sent to the driver.

`Unused`



`CommandData`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |