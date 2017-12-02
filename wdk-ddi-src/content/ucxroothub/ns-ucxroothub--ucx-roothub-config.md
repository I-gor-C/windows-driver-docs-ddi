---
UID: NS.ucxroothub._UCX_ROOTHUB_CONFIG
title: UCX_ROOTHUB_CONFIG
author: windows-driver-content
description: Contains pointers to event callback functions for creating the root hub by calling UcxRootHubCreate. Initialize this structure by calling UCX_ROOTHUB_CONFIG_INIT initialization function (see Ucxclass.h).
old-location: buses\_ucx_roothub_config.htm
old-project: usbref
ms.assetid: 27E54F0D-2163-4D7C-B204-336EE0227488
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_ROOTHUB_CONFIG, UCX_ROOTHUB_CONFIG, *PUCX_ROOTHUB_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxroothub.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_ROOTHUB_CONFIG
req.alt-loc: ucxroothub.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UCX_ROOTHUB_CONFIG structure



## -description
<p>Contains pointers to event callback functions for creating the root hub by calling <a href="buses._ucxroothubcreate">UcxRootHubCreate</a>. Initialize this structure by calling <b>UCX_ROOTHUB_CONFIG_INIT</b> initialization function (see Ucxclass.h).</p>


## -syntax

````
typedef struct _UCX_ROOTHUB_CONFIG {
  ULONG                            Size;
  ULONG                            NumberOfPresentedControlUrbCallbacks;
  PEVT_UCX_ROOTHUB_CONTROL_URB     EvtRootHubClearHubFeature;
  PEVT_UCX_ROOTHUB_CONTROL_URB     EvtRootHubClearPortFeature;
  PEVT_UCX_ROOTHUB_CONTROL_URB     EvtRootHubGetHubStatus;
  PEVT_UCX_ROOTHUB_CONTROL_URB     EvtRootHubGetPortStatus;
  PEVT_UCX_ROOTHUB_CONTROL_URB     EvtRootHubSetHubFeature;
  PEVT_UCX_ROOTHUB_CONTROL_URB     EvtRootHubSetPortFeature;
  PEVT_UCX_ROOTHUB_CONTROL_URB     EvtRootHubGetPortErrorCount;
  PEVT_UCX_ROOTHUB_CONTROL_URB     EvtRootHubControlUrb;
  PEVT_UCX_ROOTHUB_INTERRUPT_TX    EvtRootHubInterruptTx;
  PEVT_UCX_ROOTHUB_GET_INFO        EvtRootHubGetInfo;
  PEVT_UCX_ROOTHUB_GET_20PORT_INFO EvtRootHubGet20PortInfo;
  PEVT_UCX_ROOTHUB_GET_30PORT_INFO EvtRootHubGet30PortInfo;
  WDF_OBJECT_ATTRIBUTES            WdfRequestAttributes;
} UCX_ROOTHUB_CONFIG, *P_UCX_ROOTHUB_CONFIG;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field NumberOfPresentedControlUrbCallbacks

<dd>
<p>The number of control requests sent to the default endpoint.</p>
</dd>

### -field EvtRootHubClearHubFeature

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-control-urb.md">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field EvtRootHubClearPortFeature

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-control-urb.md">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field EvtRootHubGetHubStatus

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-control-urb.md">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field EvtRootHubGetPortStatus

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-control-urb.md">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field EvtRootHubSetHubFeature

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-control-urb.md">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field EvtRootHubSetPortFeature

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-control-urb.md">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field EvtRootHubGetPortErrorCount

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-control-urb.md">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field EvtRootHubControlUrb

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-control-urb.md">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field EvtRootHubInterruptTx

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-interrupt-tx.md">EVT_UCX_ROOTHUB_INTERRUPT_TX</a> callback function.</p>
</dd>

### -field EvtRootHubGetInfo

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-get-info.md">EVT_UCX_ROOTHUB_GET_INFO</a> callback function.</p>
</dd>

### -field EvtRootHubGet20PortInfo

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-get-20port-info.md">EVT_UCX_ROOTHUB_GET_20PORT_INFO</a> callback function.</p>
</dd>

### -field EvtRootHubGet30PortInfo

<dd>
<p>A pointer to the <a href="..\ucxroothub\nc-ucxroothub-evt-ucx-roothub-get-30port-info.md">EVT_UCX_ROOTHUB_GET_30PORT_INFO</a> callback function.</p>
</dd>

### -field WdfRequestAttributes

<dd>
<p>A pointer to a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that specifies initialization parameters.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucxroothub.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>