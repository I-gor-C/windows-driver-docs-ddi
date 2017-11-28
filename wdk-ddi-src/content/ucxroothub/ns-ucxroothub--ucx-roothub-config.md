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
<p>Contains pointers to event callback functions for creating the root hub by calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt188048">UcxRootHubCreate</a>. Initialize this structure by calling <b>UCX_ROOTHUB_CONFIG_INIT</b> initialization function (see Ucxclass.h).</p>


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

### -field <b>Size</b>

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field <b>NumberOfPresentedControlUrbCallbacks</b>

<dd>
<p>The number of control requests sent to the default endpoint.</p>
</dd>

### -field <b>EvtRootHubClearHubFeature</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187833">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field <b>EvtRootHubClearPortFeature</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187833">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field <b>EvtRootHubGetHubStatus</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187833">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field <b>EvtRootHubGetPortStatus</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187833">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field <b>EvtRootHubSetHubFeature</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187833">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field <b>EvtRootHubSetPortFeature</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187833">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field <b>EvtRootHubGetPortErrorCount</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187833">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field <b>EvtRootHubControlUrb</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187833">EVT_UCX_ROOTHUB_CONTROL_URB</a> callback function.</p>
</dd>

### -field <b>EvtRootHubInterruptTx</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187837">EVT_UCX_ROOTHUB_INTERRUPT_TX</a> callback function.</p>
</dd>

### -field <b>EvtRootHubGetInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187836">EVT_UCX_ROOTHUB_GET_INFO</a> callback function.</p>
</dd>

### -field <b>EvtRootHubGet20PortInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187834">EVT_UCX_ROOTHUB_GET_20PORT_INFO</a> callback function.</p>
</dd>

### -field <b>EvtRootHubGet30PortInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187835">EVT_UCX_ROOTHUB_GET_30PORT_INFO</a> callback function.</p>
</dd>

### -field <b>WdfRequestAttributes</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that specifies initialization parameters.</p>
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