---
UID: NF:ks.KsValidateClockCreateRequest
title: KsValidateClockCreateRequest function
author: windows-driver-content
description: The KsValidateClockCreateRequest function validates the clock creation request and returns the create structure associated with the request.This can only be called at PASSIVE_LEVEL.
old-location: stream\ksvalidateclockcreaterequest.htm
old-project: stream
ms.assetid: ec10c10e-4604-47fc-a2e7-4df9d90acf0b
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: ks/KsValidateClockCreateRequest, ksfunc_e681d03e-44fb-43fb-b317-dc7e63fe6cb2.xml, stream.ksvalidateclockcreaterequest, KsValidateClockCreateRequest, KsValidateClockCreateRequest function [Streaming Media Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
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
-	KsValidateClockCreateRequest
product: Windows
targetos: Windows
req.typenames: 
---


# KsValidateClockCreateRequest function
The <b>KsValidateClockCreateRequest</b> function validates the clock creation request and returns the create structure associated with the request.

This can only be called at PASSIVE_LEVEL.

## Syntax

````
NTSTATUS KsValidateClockCreateRequest(
  _In_  PIRP            lrp,
  _Out_ PKSCLOCK_CREATE *ClockCreate
);
````

## Parameters

`Irp`

TBD

`ClockCreate`

Specifies the clock create structure pointer passed to the create request.


## Return Value

The <b>KsValidateClockCreateRequest</b> function returns STATUS_SUCCESS if successful, or an error if unsuccessful.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |