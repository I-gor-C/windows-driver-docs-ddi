---
UID : NC:drmk.PFNDRMFORWARDCONTENTTOINTERFACE
title : PFNDRMFORWARDCONTENTTOINTERFACE
author : windows-driver-content
description : This callback function is reserved for system use.
old-location : audio\pfndrmforwardcontenttointerface.htm
old-project : audio
ms.assetid : DFD077B7-307B-439B-828D-DC225FC5AAA0
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : audio.pfndrmforwardcontenttointerface, DRMForwardContentToInterface callback function [Audio Devices], DRMForwardContentToInterface, PFNDRMFORWARDCONTENTTOINTERFACE, PFNDRMFORWARDCONTENTTOINTERFACE, drmk/DRMForwardContentToInterface, DRMForwardContentToInterface callback function [Audio Devices], DRMForwardContentToInterface
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : drmk.h
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
req.typenames : "*PWDI_TX_METADATA, WDI_TX_METADATA"
---


# PFNDRMFORWARDCONTENTTOINTERFACE callback function
This callback function is reserved for system use.

## Syntax

```
PFNDRMFORWARDCONTENTTOINTERFACE Pfndrmforwardcontenttointerface;

NTSTATUS Pfndrmforwardcontenttointerface(
  ULONG ContentId,
  PUNKNOWN pUnknown,
  ULONG NumMethods
)
{...}
```

## Parameters

`ContentId`

This parameter is reserved for system use.

`pUnknown`

This parameter is reserved for system use.

`NumMethods`

This parameter is reserved for system use.


## Return Value

This return value is reserved for system use.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | drmk.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |