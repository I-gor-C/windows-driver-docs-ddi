---
UID: NC.netconfiguration.PFN_NETCONFIGURATIONOPENSUBCONFIGURATION
title: PFN_NETCONFIGURATIONOPENSUBCONFIGURATION
author: windows-driver-content
description: 
ms.assetid: 50435d44-07f0-41de-a1e8-cadcc3ab9164
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netconfiguration.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# PFN_NETCONFIGURATIONOPENSUBCONFIGURATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NETCONFIGURATIONOPENSUBCONFIGURATION PfnNetconfigurationopensubconfiguration; 

// Definition

WDFAPI PfnNetconfigurationopensubconfiguration 
(
	PNET_DRIVER_GLOBALS DriverGlobals
	NETCONFIGURATION Configuration
	PCUNICODE_STRING SubConfigurationName
	PWDF_OBJECT_ATTRIBUTES SubConfigurationAttributes
	NETCONFIGURATION *SubConfiguration
)
{...}

PFN_NETCONFIGURATIONOPENSUBCONFIGURATION 


```

## -parameters

### -param DriverGlobals: 
### -param Configuration: 
### -param SubConfigurationName: 
### -param SubConfigurationAttributes: 
### -param *SubConfiguration: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also