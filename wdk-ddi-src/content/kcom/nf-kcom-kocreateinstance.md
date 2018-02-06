---
UID: NF:kcom.KoCreateInstance
title: KoCreateInstance function
author: windows-driver-content
description: The KoCreateInstance function creates an object of the class with the specified CLSID.
old-location: stream\kocreateinstance.htm
old-project: stream
ms.assetid: ee719cbe-0933-4adc-b5c7-62b66f2bf4e1
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: stream.kocreateinstance, KoCreateInstance function [Streaming Media Devices], KoCreateInstance, ksfunc_57c8ab23-3163-4ef8-a381-bd81ce01d18e.xml, kcom/KoCreateInstance
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: kcom.h
req.include-header: Kcom.h
req.target-type: Universal
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
req.lib: Ks.lib
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	LibDef
apilocation:
-	Ks.lib
-	Ks.dll
apiname:
-	KoCreateInstance
product: Windows
targetos: Windows
req.typenames: "*PCONNECT_DATA, CONNECT_DATA"
---


# KoCreateInstance function
<i>This function is intended for internal use only.</i>

The <b>KoCreateInstance</b> function creates an object of the class with the specified CLSID.

## Syntax

````
NTSTATUS KoCreateInstance(
  _In_     REFCLSID ClassId,
  _In_opt_ IUnknown *UnkOuter,
  _In_     ULONG    ClsContext,
  _In_     REFIID   InterfaceId,
  _Out_    PVOID    *Interface
);
````

## Parameters

`ClassId`

The CLSID of the object to create an instance of.

`UnkOuter`

The outer unknown object to pass to the new instance.

`ClsContext`

The context in which to create the instance. This must be CLSCTX_KERNEL_SERVER.

`InterfaceId`

Reference to the identifier of the interface that will communicate with the object.

`Interface`

Address of the pointer variable that receives the new interface pointer specified in <i>InterfaceId</i>.


## Return Value

Returns STATUS_SUCCESS if the instance was successfully created. Otherwise, it returns an error.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | kcom.h (include Kcom.h) |
| **Library** | Ks.lib |