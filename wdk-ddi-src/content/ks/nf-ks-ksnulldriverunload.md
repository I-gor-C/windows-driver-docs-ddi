---
UID : NF:ks.KsNullDriverUnload
title : KsNullDriverUnload function
author : windows-driver-content
description : The KsNullDriverUnload function is a default function a driver can use when it has no other tasks to do in its unload function, but must still allow the device to be unloaded by its presence.
old-location : stream\ksnulldriverunload.htm
old-project : stream
ms.assetid : 1fe4c3b7-4627-4a59-9779-fa2be29f387a
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ks/KsNullDriverUnload, KsNullDriverUnload, ksfunc_449d73af-488d-4c4b-b5cb-f706fd48beab.xml, KsNullDriverUnload function [Streaming Media Devices], stream.ksnulldriverunload
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ks.h
req.include-header : Ks.h
req.target-type : Universal
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
req.lib : Ks.lib
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---


# KsNullDriverUnload function
The <b>KsNullDriverUnload</b> function is a default function a driver can use when it has no other tasks to do in its unload function, but must still allow the device to be unloaded by its presence.

## Syntax

````
VOID KsNullDriverUnload(
  _In_ PDRIVER_OBJECT DriverObject 
);
````

## Parameters

`DriverObject`

Specifies the driver object for this device.


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |