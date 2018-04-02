---
UID: NN:portcls.IServiceGroup
title: IServiceGroup
author: windows-driver-content
description: The IServiceGroup interface encapsulates a group of objects that all require notification of the same service request.
old-location: audio\iservicegroup.htm
old-project: audio
ms.assetid: eef2741e-e1a3-471b-a756-d89990929738
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IServiceGroup, IServiceGroup interface [Audio Devices], IServiceGroup interface [Audio Devices], described, audio.iservicegroup, audmp-routines_10cfd005-be11-47a2-a929-f338f40e6f79.xml, portcls/IServiceGroup
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
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
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	portcls.h
api_name:
-	IServiceGroup
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IServiceGroup interface

The <code>IServiceGroup</code> interface encapsulates a group of objects that all require notification of the same service request. When the service group object receives notification of the request, it forwards the notification to each of the objects in the group. The PortCls system driver implements the <code>IServiceGroup</code> interface and exposes it to miniport drivers. A miniport driver creates an <code>IServiceGroup</code> object by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff537719">PcNewServiceGroup</a>. <code>IServiceGroup</code> inherits from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537006">IServiceSink</a> interface.

Port drivers typically use service group objects to demultiplex requests for interrupt service, although the functionality of a service group is general enough to make it potentially useful for other purposes as well. For more information, see <a href="https://msdn.microsoft.com/00e17e01-8889-4fae-a0ff-e110d7a9b21e">Service Sink and Service Group Objects</a>.

## Methods

<p>The <b>IServiceGroup</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IServiceGroup::AddMember](nf-portcls-iservicegroup-addmember.md) | The AddMember method adds a member to the service group. |
| [IServiceGroup::CancelDelayedService](nf-portcls-iservicegroup-canceldelayedservice.md) | The CancelDelayedService method cancels the previously requested delayed service. |
| [IServiceGroup::RemoveMember](nf-portcls-iservicegroup-removemember.md) | The RemoveMember method removes the specified member from the service group. |
| [IServiceGroup::RequestDelayedService](nf-portcls-iservicegroup-requestdelayedservice.md) | The RequestDelayedService method requests service after the specified delay. |
| [IServiceGroup::RequestService](nf-portcls-iservicegroup-requestservice.md) | TBD |
| [IServiceGroup::SupportDelayedService](nf-portcls-iservicegroup-supportdelayedservice.md) | The SupportDelayedService method indicates that the service group should prepare to support delayed service. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | portcls.h |