---
UID : NC:drmk.PFNDRMFORWARDCONTENTTOFILEOBJECT
title : PFNDRMFORWARDCONTENTTOFILEOBJECT
author : windows-driver-content
description : This callback function is reserved for system use.
old-location : audio\pfndrmforwardcontenttofileobject.htm
old-project : audio
ms.assetid : 00ACCBFF-FEDE-4223-8503-4D75426E2BD6
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : audio.pfndrmforwardcontenttofileobject, DRMForwardContentToFileObject callback function [Audio Devices], DRMForwardContentToFileObject, PFNDRMFORWARDCONTENTTOFILEOBJECT, PFNDRMFORWARDCONTENTTOFILEOBJECT, drmk/DRMForwardContentToFileObject, DRMForwardContentToFileObject callback function [Audio Devices], DRMForwardContentToFileObject
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


# PFNDRMFORWARDCONTENTTOFILEOBJECT callback function
This callback function is reserved for system use.

## Syntax

```
PFNDRMFORWARDCONTENTTOFILEOBJECT Pfndrmforwardcontenttofileobject;

NTSTATUS Pfndrmforwardcontenttofileobject(
  ULONG ContentId,
  PFILE_OBJECT FileObject
)
{...}
```

## Parameters

`ContentId`

This parameter is reserved for system use.

`FileObject`

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