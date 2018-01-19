---
UID : NN:portcls.IServiceGroup
title : IServiceGroup
author : windows-driver-content
description : The IServiceGroup interface encapsulates a group of objects that all require notification of the same service request.
old-location : audio\iservicegroup.htm
old-project : audio
ms.assetid : eef2741e-e1a3-471b-a756-d89990929738
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : PcUnregisterIoTimeout
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : portcls.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IServiceGroup
req.alt-loc : portcls.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Portcls.lib
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IServiceGroup interface

The <code>IServiceGroup</code> interface encapsulates a group of objects that all require notification of the same service request. When the service group object receives notification of the request, it forwards the notification to each of the objects in the group. The PortCls system driver implements the <code>IServiceGroup</code> interface and exposes it to miniport drivers. A miniport driver creates an <code>IServiceGroup</code> object by calling <a href="..\portcls\nf-portcls-pcnewservicegroup.md">PcNewServiceGroup</a>. <code>IServiceGroup</code> inherits from the <a href="..\portcls\nn-portcls-iservicesink.md">IServiceSink</a> interface.

Port drivers typically use service group objects to demultiplex requests for interrupt service, although the functionality of a service group is general enough to make it potentially useful for other purposes as well. For more information, see <a href="https://msdn.microsoft.com/00e17e01-8889-4fae-a0ff-e110d7a9b21e">Service Sink and Service Group Objects</a>.

## Methods

<p>The <b>IServiceGroup</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [portcls.IServiceGroup.AddMember](nf-portcls-iservicegroup-addmember.md) | The AddMember method adds a member to the service group. |
| [portcls.IServiceGroup.CancelDelayedService](nf-portcls-iservicegroup-canceldelayedservice.md) | The CancelDelayedService method cancels the previously requested delayed service. |
| [portcls.IServiceGroup.RemoveMember](nf-portcls-iservicegroup-removemember.md) | The RemoveMember method removes the specified member from the service group. |
| [portcls.IServiceGroup.RequestDelayedService](nf-portcls-iservicegroup-requestdelayedservice.md) | The RequestDelayedService method requests service after the specified delay. |
| [portcls.IServiceGroup.SupportDelayedService](nf-portcls-iservicegroup-supportdelayedservice.md) | The SupportDelayedService method indicates that the service group should prepare to support delayed service. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | portcls.h |
| **DLL** |  |