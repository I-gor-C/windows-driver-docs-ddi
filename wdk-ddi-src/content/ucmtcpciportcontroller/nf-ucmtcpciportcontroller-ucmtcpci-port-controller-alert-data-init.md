---
UID: NF.ucmtcpciportcontroller.UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT
title: UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT
author: windows-driver-content
description: Initializes the UCMTCPCI_PORT_CONTROLLER_ALERT_DATA structure.
old-location: buses\ucmtcpci_port_controller_alert_data_init.htm
old-project: usbref
ms.assetid: 7c3276cc-9194-4c18-b1d8-2795efbeb357
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucmtcpciportcontroller.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT
req.alt-loc: ucmtcpciportcontroller.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT function



## -description
<p>
                        Initializes the <b>UCMTCPCI_PORT_CONTROLLER_ALERT_DATA</b> structure.
                
            
        Call this function before calling <a href="..\ucmtcpciportcontroller\nf-ucmtcpciportcontroller-ucmtcpciportcontrolleralert.md">UcmTcpciPortControllerAlert</a>.</p>


## -syntax

````
VOID UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT(
  _Out_ PUCMTCPCI_PORT_CONTROLLER_ALERT_DATA AlertData
);
````


## -parameters
<dl>

### -param AlertData [out]

<dd>
<p>A pointer to the driver-allocated <b>UCMTCPCI_PORT_CONTROLLER_ALERT_DATA</b> structure.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucmtcpciportcontroller.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>