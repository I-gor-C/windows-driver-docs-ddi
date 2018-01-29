---
UID : NF:ndis.NdisGetVersion
title : NdisGetVersion function
author : windows-driver-content
description : The NdisGetVersion function returns the version number of NDIS.
old-location : netvista\ndisgetversion.htm
old-project : netvista
ms.assetid : d3e2c799-f789-499f-9948-f41d7576296e
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ndis/NdisGetVersion, ndis_configuration_ref_fcdf5ece-888e-4f1a-b855-367cbe4c68fe.xml, netvista.ndisgetversion, NdisGetVersion, NdisGetVersion function [Network Drivers Starting with Windows Vista]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ndis.h
req.include-header : Ndis.h
req.target-type : Universal
req.target-min-winverclnt : Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisGetVersion (NDIS 5.1)) in   Windows Vista. Supported for NDIS 5.1 drivers (see    NdisGetVersion (NDIS 5.1)) in   Windows XP.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : Irql_Miscellaneous_Function
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ndis.lib
req.dll : 
req.irql : <= DISPATCH_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PNDIS_SHARED_MEMORY_USAGE, NDIS_SHARED_MEMORY_USAGE"
---


# NdisGetVersion function
The 
  <b>NdisGetVersion</b> function returns the version number of NDIS.

## Syntax

````
UINT NdisGetVersion(void);
````

## Parameters

This function has no parameters.

## Return Value

Returns the major and minor numbers for the NDIS version in the high and low halves of the
     unsigned integer respectively.

## Remarks

System support for 
    <b>NdisGetVersion</b> is available in Windows XP and later versions.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndis.h (include Ndis.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL |
| **DDI compliance rules** | Irql_Miscellaneous_Function |