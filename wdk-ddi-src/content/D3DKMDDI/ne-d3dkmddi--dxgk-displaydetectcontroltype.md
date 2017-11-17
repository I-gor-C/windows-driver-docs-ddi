---
UID: NE.d3dkmddi._DXGK_DISPLAYDETECTCONTROLTYPE
title: DXGK_DISPLAYDETECTCONTROLTYPE
author: windows-driver-content
description: Enumeration indicating the type of display detection action.
old-location: display\dxgk_displaydetectcontroltype.htm
ms.assetid: D777342E-439E-4BEF-9DCC-7962B1AF8EAB
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DISPLAYDETECTCONTROLTYPE
req.alt-loc: d3dkmddi.h
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
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
req.iface: 
---

# DXGK_DISPLAYDETECTCONTROLTYPE enumeration



## -description
<p>Enumeration indicating the type of display detection action.</p>


## -syntax

````
typedef enum _DXGK_DISPLAYDETECTCONTROLTYPE { 
  DXGK_DDCT_UNINITIALIZED  = 0,
  DXGK_DDCT_POLLONE,
  DXGK_DDCT_POLLALL,
  DXGK_DDCT_ENABLEHPD,
  DXGK_DDCT_DISABLEHPD
} DXGK_DISPLAYDETECTCONTROLTYPE;
````


## -enum-fields
<dl>

### -field <a id="DXGK_DDCT_UNINITIALIZED"></a><a id="dxgk_ddct_uninitialized"></a><b>DXGK_DDCT_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type DXGK_DISPLAYDETECTCONTROLTYPE has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="DXGK_DDCT_POLLONE"></a><a id="dxgk_ddct_pollone"></a><b>DXGK_DDCT_POLLONE</b>

<dd>
<p>Requests a poll of the target specified in the TargetId field.  The driver should initiate polling the target if the current status is not known.  If the status is not the same as the last reported status for the target, an updated status should be reported using DxgkCbIndicateConnectorChange.</p>
</dd>

### -field <a id="DXGK_DDCT_POLLALL"></a><a id="dxgk_ddct_pollall"></a><b>DXGK_DDCT_POLLALL</b>

<dd>
<p>Request to initiate polls for all targets where the driver does not have current status before completing the call but the driver should not wait for the results of polling before returning.
As status of each target is discovered, if it is not the same as the previously updated status should be reported using DxgkCbIndicateConnectorChange.
</p>
</dd>

### -field <a id="DXGK_DDCT_ENABLEHPD"></a><a id="dxgk_ddct_enablehpd"></a><b>DXGK_DDCT_ENABLEHPD</b>

<dd>
<p>Applies to all targets and requires that the driver enables new notifications and indicates any pending notifications using DxgkCbIndicateConnectorChange before completing the call.  It must also initiate polls for all targets where the driver does not have current status before completing the call but it should not wait for the results of polling before returning. For the POST adapter, it is important that the display which was initialized by firmware be included in the set of displays which is reported before returning from the call made during boot so that the OS is aware of the monitor before it requests the boot functional VidPn.  Since firmware has already detected and initialized the boot display and the driver has been able to query for the frame buffer state, the connection status should naturally be known by the driver and pending notification to the OS.</p>
</dd>

### -field <a id="DXGK_DDCT_DISABLEHPD"></a><a id="dxgk_ddct_disablehpd"></a><b>DXGK_DDCT_DISABLEHPD</b>

<dd>
<p>Applies to all targets and requires that the driver disables new notifications. It is understood that, this does not prevent an in-flight notification from being reported after the driver has returned.</p>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>