---
UID : NF:ks.KsValidateTopologyNodeCreateRequest
title : KsValidateTopologyNodeCreateRequest function
author : windows-driver-content
description : The KsValidateTopologyNodeCreateRequest function validates a topology node creation request and returns the create structure associated with the request. The function can only be called at PASSIVE_LEVEL.
old-location : stream\ksvalidatetopologynodecreaterequest.htm
old-project : stream
ms.assetid : a7d69bf8-7aa8-46c2-98f9-769ee174757b
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ksfunc_f2b7fc56-1bca-4de5-981b-68364aa96fa7.xml, ks/KsValidateTopologyNodeCreateRequest, KsValidateTopologyNodeCreateRequest function [Streaming Media Devices], stream.ksvalidatetopologynodecreaterequest, KsValidateTopologyNodeCreateRequest
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


# KsValidateTopologyNodeCreateRequest function
The <b>KsValidateTopologyNodeCreateRequest</b> function validates a topology node creation request and returns the create structure associated with the request. The function can only be called at PASSIVE_LEVEL.

## Syntax

````
NTSTATUS KsValidateTopologyNodeCreateRequest(
  _In_  PIRP           Irp,
  _In_  PKSTOPOLOGY    Topology,
  _Out_ PKSNODE_CREATE *NodeCreate
);
````

## Parameters

`Irp`

Specifies the IRP with the node create request being handled.

`Topology`

Specifies the topology structure associated with the parent object. This is used to validate the create request.

`NodeCreate`

Location for the node create structure pointer passed to the create request.


## Return Value

The <b>KsValidateTopologyNodeCreateRequest</b> function returns a STATUS_SUCCESS if successful, or else an error if unsuccessful.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | ks.h (include Ks.h) |
| **Library** | Ks.lib |